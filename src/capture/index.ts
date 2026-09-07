import { readdirSync, readFileSync, writeFileSync, existsSync, mkdirSync } from 'node:fs'
import { join } from 'node:path'
import { XClient, estimateCostUsd } from '../x/client.js'
import { loadResolvedAccounts, requireEnv } from '../lib/config.js'
import { dataRoot } from '../duck/connect.js'
import { buildQueries } from './query.js'
import { readCursor } from './cursor.js'
import { rawPath, manifestPath, runIdentity, writeJsonlGz } from './writer.js'
import { marketDate, isoUtc } from '../lib/time.js'
import { log, ghError } from '../lib/log.js'
import type { CapturedPost } from '../x/types.js'

/** Cold start: sweep everything recent search still exposes. */
const COLD_START_LOOKBACK_DAYS = 7
/** Abort rather than let a malformed query or a viral day 10x the bill. */
const COST_GUARD_MULTIPLE = 3
const COST_GUARD_FLOOR = 1500

export type CaptureManifest = {
  run_id: string
  attempt: number
  ingest_dt: string
  started_at: string
  finished_at: string
  queries: string[]
  cursor_before: string | null
  cursor_after: string | null
  pages: number
  posts_read: number
  estimated_cost_usd: number
  files: { path: string; bytes: number; posts: number }[]
  status: 'ok' | 'aborted_cost_guard'
}

function readManifests(root: string): CaptureManifest[] {
  const base = join(root, 'raw')
  if (!existsSync(base)) return []
  const out: CaptureManifest[] = []
  for (const dir of readdirSync(base)) {
    const partition = join(base, dir)
    let entries: string[]
    try { entries = readdirSync(partition) } catch { continue }
    for (const f of entries) {
      if (!f.startsWith('_manifest-')) continue
      try { out.push(JSON.parse(readFileSync(join(partition, f), 'utf8')) as CaptureManifest) } catch { /* ignore */ }
    }
  }
  return out
}

/** Trailing median posts-per-run, used as the cost guard baseline. */
function trailingMedianPosts(manifests: CaptureManifest[]): number | null {
  const counts = manifests
    .filter((m) => m.status === 'ok' && m.cursor_before !== null)
    .map((m) => m.posts_read)
    .sort((a, b) => a - b)
  if (counts.length < 5) return null
  return counts[Math.floor(counts.length / 2)] ?? null
}

export async function capture(): Promise<CaptureManifest> {
  const started = new Date()
  const root = dataRoot()
  const accounts = loadResolvedAccounts()
  const queries = buildQueries(accounts)
  const { runId, attempt } = runIdentity()
  const ingestDt = marketDate(started)

  const cursorBefore = await readCursor(root)
  const startTime = cursorBefore
    ? undefined
    : isoUtc(new Date(started.getTime() - COLD_START_LOOKBACK_DAYS * 86_400_000))

  log.info('capture.start', {
    runId, attempt, ingestDt, queries: queries.length,
    cursor_before: cursorBefore, cold_start: !cursorBefore,
  })

  const client = new XClient(requireEnv('X_BEARER_TOKEN'))
  const files: CaptureManifest['files'] = []
  const guard = trailingMedianPosts(readManifests(root))
  const guardLimit = guard === null ? Infinity : Math.max(COST_GUARD_FLOOR, guard * COST_GUARD_MULTIPLE)
  let pages = 0
  let aborted = false
  let newestId: string | null = null

  outer: for (const query of queries) {
    for await (const { tweets, users, pageNo } of client.searchRecent({ query, sinceId: cursorBefore ?? undefined, startTime })) {
      pages++
      if (tweets.length === 0) continue

      // Resolve the author handle at capture time. It is recorded as a
      // point-in-time observation; author_id remains the join key.
      const ingestedAt = isoUtc(new Date())
      const enriched: CapturedPost[] = tweets.map((t) => ({
        ...t,
        _author_username: users.get(t.author_id) ?? '',
        _ingested_at: ingestedAt,
        _run_id: runId,
      }))
      for (const t of tweets) {
        if (newestId === null || BigInt(t.id) > BigInt(newestId)) newestId = t.id
      }

      const path = rawPath(root, ingestDt, runId, attempt, pages)
      const bytes = writeJsonlGz(path, enriched)
      files.push({ path: path.slice(root.length + 1), bytes, posts: enriched.length })
      log.info('capture.page', { pageNo, posts: enriched.length, postsRead: client.postsRead })

      if (client.postsRead > guardLimit) {
        aborted = true
        ghError(
          `Cost guard tripped: ${client.postsRead} posts read exceeds ${guardLimit} ` +
          `(${COST_GUARD_MULTIPLE}x trailing median ${guard}). Captured pages are kept; investigate before rerunning.`,
        )
        break outer
      }
    }
  }

  const manifest: CaptureManifest = {
    run_id: runId,
    attempt,
    ingest_dt: ingestDt,
    started_at: isoUtc(started),
    finished_at: isoUtc(new Date()),
    queries,
    cursor_before: cursorBefore,
    cursor_after: newestId ?? cursorBefore,
    pages,
    posts_read: client.postsRead,
    estimated_cost_usd: estimateCostUsd(client.postsRead),
    files,
    status: aborted ? 'aborted_cost_guard' : 'ok',
  }

  mkdirSync(join(root, `raw/ingest_dt=${ingestDt}`), { recursive: true })
  writeFileSync(manifestPath(root, ingestDt, runId, attempt), JSON.stringify(manifest, null, 2) + '\n')
  log.info('capture.done', {
    posts_read: manifest.posts_read,
    estimated_cost_usd: manifest.estimated_cost_usd,
    files: files.length,
    status: manifest.status,
  })
  return manifest
}

if (import.meta.url === `file://${process.argv[1]}`) {
  capture()
    .then((m) => { if (m.status !== 'ok') process.exitCode = 1 })
    .catch((err) => {
      ghError(String(err))
      log.error('capture.failed', { error: String(err) })
      process.exit(1)
    })
}
