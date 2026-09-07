import { mkdirSync, writeFileSync, rmSync, existsSync } from 'node:fs'
import { join } from 'node:path'
import { connect, rows, dataRoot, requireLayers } from '../../duck/connect.js'
import { activeTags, loadEnums, loadTagTaxonomy } from '../../lib/config.js'
import { log } from '../../lib/log.js'

/**
 * Bundles the corpus into one text-only file per account, for the
 * session-subagent extraction lane.
 *
 * The daily lane (src/extract/run.ts) sends one trading session to the
 * Anthropic API. This lane instead slices by AUTHOR across the whole captured
 * window and hands each slice to a subagent inside an interactive Claude Code
 * session - no API key, no per-call billing. The trade is deliberate: an
 * author-sliced pass answers "how does this commentator actually operate"
 * (their repertoire, their conviction language, whether they ever revisit a
 * call), which a day-sliced pass structurally cannot see.
 *
 * Two invariants the bundle enforces:
 *   - RETWEETS ARE EXCLUDED. A retweet is an echo, not a call, and the
 *     attribution views already refuse to credit one. Feeding them to an
 *     extractor would let an account earn a pick for someone else's words.
 *   - TEXT ONLY. media_keys and image references never enter the bundle. The
 *     corpus stores media keys, not image bytes, and nothing here resolves
 *     them, so no image can reach a model along this path.
 */

export const SESSION_PROMPT_VERSION = 'v1-acct'

export type BundlePost = {
  post_id: string
  created_at: string
  trading_day: string
  post_type: string
  text: string
}

/** The extraction contract, generated from ref/ so the enums cannot drift. */
export function buildSpec(): string {
  const enums = loadEnums()
  const tags = loadTagTaxonomy().filter((t) => t.removed_date === '')
  return `# Account extraction contract (${SESSION_PROMPT_VERSION})

You are a research analyst reading everything ONE market commentator posted over a
two-month window. You are reporting what this account claimed. You are not
evaluating whether they were right, and you are not offering investment advice.

## Input

\`<handle>.posts.jsonl\` — one JSON object per line, oldest first:
\`{ post_id, created_at, trading_day, post_type, text }\`.
Retweets are already excluded. There are no images anywhere in this task.

## Output

Write exactly one JSON file to the path you are given. No markdown fence, no prose
around it. It must match this shape:

\`\`\`json
{
  "account": "<handle>",
  "profile": {
    "beat": "What this account actually covers, in 1-2 sentences.",
    "style": "How they express a view: conviction language, position sizing talk, chart vs fundamentals, etc. 2-4 sentences.",
    "cadence": "Post rhythm and format — threads, one-liners, replies, recurring series.",
    "revisits": "Do they revisit or update earlier calls, or only post new ones? Cite post_ids if so.",
    "caveats": "Anything that should make a reader discount this account's record. Say 'none observed' if so."
  },
  "narrative": "The dominant arc of this account's two months, in 4-8 sentences. Where their view changed, say when and why.",
  "picks": [
    {
      "symbol": "TICKER, uppercase, no $",
      "direction": ${JSON.stringify(enums.direction)},
      "prospect": "What the author expects to happen.",
      "risk_reward": "The stated or clearly implied downside against the upside. Say so plainly if the author never addressed risk.",
      "thesis": "Why, in the author's own logic.",
      "time_frame": ${JSON.stringify(enums.time_frame)},
      "tags": ["zero or more of the tags below"],
      "conviction": 0.0,
      "first_seen": "YYYY-MM-DD — trading_day of the earliest post supporting this pick",
      "sources": [
        { "post_id": "must exist in the input", "quote": "verbatim span from THAT post" }
      ]
    }
  ]
}
\`\`\`

### Allowed tags
${tags.map((t) => `- \`${t.tag}\` — ${t.description}`).join('\n')}

## Rules

1. **Every pick cites at least one real post_id from the input.** A pick citing a
   post_id that is not in the file is rejected by the ingest gate and fails the run.
2. **Quotes are verbatim.** Copy the span exactly as written. Never paraphrase inside
   a quote field. Do not fix typos.
3. **A mention is not a pick.** Only include a symbol where the author expressed an
   actual stance. Naming a ticker in passing, or reporting someone else's view, is not
   a pick.
4. **Never state or imply a price, a return, or a percentage move** in any field
   except inside a verbatim quote. Returns are computed elsewhere from real closes; a
   number invented here would silently corrupt the corpus.
5. **conviction is 0-1** and reflects how strongly THIS author committed — hedged
   language is low, "this is my largest position" is high.
6. **Prefer fewer, well-supported picks.** A name the author returned to six times is
   worth more than six names mentioned once.
7. If the author never addressed risk for a pick, say exactly that in \`risk_reward\`.
8. \`first_seen\` must be the trading_day of the earliest post you cite for that pick.
`
}

export async function dumpAccounts(opts: { outDir?: string } = {}): Promise<string[]> {
  const root = dataRoot()
  requireLayers(['posts'], root)
  const outDir = opts.outDir ?? join(root, '_session')
  if (existsSync(outDir)) rmSync(outDir, { recursive: true, force: true })
  mkdirSync(outDir, { recursive: true })

  const connection = await connect({ data: root })
  const accounts = (await rows(connection, `
    SELECT author_username AS handle, count(*) AS n
      FROM posts_v WHERE post_type <> 'retweet'
     GROUP BY 1 ORDER BY n DESC`)).map((r) => String(r['handle']))

  writeFileSync(join(outDir, 'SPEC.md'), buildSpec())

  const written: string[] = []
  for (const handle of accounts) {
    // COALESCE(full_text, text): note_tweet carries the untruncated body of a
    // long post, and extracting from the truncated form would cite a quote the
    // author's actual post does not contain.
    const posts = (await rows(connection, `
      SELECT post_id, created_at::VARCHAR AS created_at, trading_day::VARCHAR AS trading_day,
             post_type, COALESCE(full_text, text) AS text
        FROM posts_v
       WHERE author_username = '${handle.replace(/'/g, "''")}' AND post_type <> 'retweet'
       ORDER BY created_at, post_id`)) as unknown as BundlePost[]

    const path = join(outDir, `${handle}.posts.jsonl`)
    writeFileSync(path, posts.map((p) => JSON.stringify(p)).join('\n') + '\n')
    written.push(path)
    log.info('session.dump', { handle, posts: posts.length, bytes: Buffer.byteLength(JSON.stringify(posts)) })
  }
  log.info('session.dump.done', { accounts: written.length, outDir, tags: activeTags().length })
  return written
}

if (import.meta.url === `file://${process.argv[1]}`) {
  dumpAccounts().catch((err) => { console.error(String(err)); process.exit(1) })
}
