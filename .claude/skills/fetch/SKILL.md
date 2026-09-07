---
name: fetch
description: Fetch the X posts of the allowlisted accounts for a timeframe given in the prompt ("last 30 days", "from 2026-07-07 to 2026-09-06"), normalize them, and extract one account analysis per handle using subagents inside this Claude Code session, with no Anthropic API key. Produces data/raw, data/posts, data/_session bundles, data/analysis/accounts/*.json and the picks layer. Run this before /corpus-probe.
argument-hint: "'last N days' | 'from YYYY-MM-DD to YYYY-MM-DD' [--accounts h1,h2] [--budget-usd N]"
---

# Fetch

## The problem, and how it is solved

The corpus is a strict allowlist of X accounts (`accounts.json`, 14 handles). Reading
their posts costs real money on the X API, about $0.005 per post, and the recent-search
endpoint only reaches back seven days. Turning those posts into structured account
analyses needs a large model reading thousands of posts per account, which on the
Anthropic API would be a second bill. The first fetch solved both like this:

1. **Acquire once, keep forever.** Posts are pulled with the X API's *user timeline*
   endpoint, which has no seven-day wall, and written gzip-compressed and append-only
   to `data/raw/`. Everything downstream is derived and free to recompute. A hard
   `--max-posts` cap is the spend limit.
2. **Extract inside the session, not through an API.** The corpus is sliced by author
   into text-only bundles, and one subagent per bundle, running inside this Claude Code
   session, reads it and writes a JSON analysis against a fixed contract. No
   `ANTHROPIC_API_KEY` is used anywhere. The model recorded on every pick is
   `claude-opus-5[1m]/session-subagent`.
3. **Trust the gate, not the agent.** Every pick must cite a real post_id with a
   verbatim quote, and `session-ingest` re-checks each one against the corpus before
   anything is written.

This skill is that procedure, made repeatable for any timeframe. The X API bill is the
only cost. The first run fetched 4,992 posts for six accounts over 62 days for $24.96
and stopped on a 402 when the developer-console credits ran out.

## Preconditions

| Need | Check | Fix |
|---|---|---|
| Dependencies | `pnpm install` done, Node 20+ | `pnpm install` |
| X bearer token | `.env` contains `X_BEARER_TOKEN=` | create the token in the X developer portal, Keys and tokens tab. `.env` is gitignored |
| Credits | pay-per-use balance in the X developer console covers the budget below | top up first. A 402 mid-sweep keeps what was paid for but stops the rest |
| Resolved accounts | every entry in `accounts.json` has a `user_id` | `pnpm task:resolve-accounts` once, then commit |
| Ticker universe | `ref/` has the listed-symbol universe | `pnpm task:sync-universe` (free, no key) |

Nothing here needs an Anthropic key. Do not set one; `task:extract` is the other lane
and is not part of this skill.

## Step 1. Turn the prompt into a window and a budget

Parse the argument into `--start` and optional `--end`, ISO 8601 UTC:

| Prompt says | Flags |
|---|---|
| "last 30 days" | `--start <today minus 30 days>T00:00:00Z` |
| "from 2026-07-07 to 2026-09-06" | `--start 2026-07-07T00:00:00Z --end 2026-09-07T00:00:00Z` (end is exclusive, so add a day) |
| nothing | the backfill default, `--months 2` |

Estimate the bill before spending. The observed rate from the first run:

| Account | Posts per day |
|---|---|
| TheLongInvest | 37 |
| LogicalThesis | 18 |
| CEOStockWatcher | 11 |
| stocktalkweekly | 8 |
| deerpointmacro | 2 |
| unknown account | assume 15 |

Posts = sum over accounts of (rate × days). Dollars = posts × 0.005. Set
`--max-posts` to `budget ÷ 0.005`, rounded down, and say the estimate to the user
before running. A 60-day sweep of all 14 accounts is roughly 12,000 posts, about $60.

**Seven days or less:** use `pnpm task:capture` instead. It is the incremental daily
lane, takes its cursor from `data/raw/`, and never re-reads a post it already paid for.
The GitHub Action runs it weekdays at 16:15 ET. Backfill is for anything older.

## Step 2. Smoke-test for five cents, then run

`--dry-run` still reads pages and still bills; it only skips writing. The cheap test is
a capped real run into the real layout:

```bash
pnpm task:backfill --start <START> --max-pages 1 --max-results 10 --max-posts 200
```

That reads at most one page of ten posts per account, about $0.05 for 14 accounts, and
proves the token, the credits and the write path. Then the real sweep:

```bash
pnpm task:backfill --start <START> [--end <END>] --max-posts <CAP> [--accounts h1,h2]
```

The first run's exact command was
`pnpm task:backfill --start 2026-07-07T00:00:00Z --max-posts 16000`.

Backfill is **not incremental**. Re-running it re-reads and re-pays for every account it
touches. `--accounts` exists so that a sweep cut off partway down the allowlist can be
resumed for the remaining handles only.

## Step 3. Read the manifest before anything else

Every run writes `data/raw/ingest_dt=<capture date>/_manifest-<run_id>-backfill-a<n>.json`,
including runs that die on an error. Check four fields:

- `status`: `ok`, `aborted_budget` (the cap hit; raise it and resume with `--accounts`),
  or `aborted_error` (read `error`; a 402 means credits, a 401 means the token).
- `estimated_cost_usd` and `posts_read`: what was actually paid.
- per account, `oldest` against `start_time`. An account whose oldest post is later than
  the start was not fully reached even when `truncated` is false. The first run's
  StockSavvyShay bundle reached only 29 Aug of a 7 Jul window because the timeline
  endpoint stopped paginating. Record every such gap; the probes must state it.
- which handles are missing entirely. The first run stopped at account 7 of 14
  (MarcosMillaYT) on a 402, so eight accounts were never fetched.

## Step 4. Normalize and verify coverage

```bash
pnpm task:normalize
pnpm q corpus-coverage
```

Normalize writes `data/posts/ingest_dt=…/posts.parquet` and `data/mentions/…`, dedupes
across partitions, resolves tickers, and materializes `post_type` and `trading_day`
(ET session, so a post after 16:00 ET belongs to the next trading day). The coverage
query prints posts, retweet share, first and last day and capture runs per account.
Compare it to the window you paid for and note any account that fell short.

## Step 5. Bundle by author

```bash
pnpm task:session-dump [--from YYYY-MM-DD --to YYYY-MM-DD]
```

Writes to `data/_session/` (gitignored, regenerable):

- `<handle>.posts.jsonl`, one post per line, oldest first, `{post_id, created_at,
  trading_day, post_type, text}`. Retweets are excluded because an echo is not a call.
  Text only; no media ever reaches a model along this path. Long posts use the
  untruncated `note_tweet` body so quotes can be verified.
- `SPEC.md`, the extraction contract, generated from `ref/` so the enums and tag
  taxonomy cannot drift from what ingest validates.
- `WINDOW.json`, the inclusive trading-day bounds the bundles cover. Ingest stamps the
  analyses with these dates. Pass `--from/--to` when the corpus holds more history than
  the window you want analysed.

Re-dumping replaces the bundles and the contract but never touches `out/`.

## Step 6. Extract with subagents inside this session

This is the step that replaces the API call. Launch **one `general-purpose` subagent per
bundle, all in a single message**, each with the brief in `extraction-brief.md`, its
handle, and its output path `data/_session/out/<handle>.json`. Never read a bundle in the
main context; the largest was 1,909 posts and 58 KB of JSON output.

What the brief makes each subagent do:

1. Read `data/_session/SPEC.md` in full. It is the contract; the shape, the allowed tags,
   and the eight rules.
2. Read its bundle in full, linearly, once.
3. Write exactly one JSON file to the output path. No fences, no prose.
4. Run `pnpm task:session-ingest --check` and fix its own file until the gate passes.

When all subagents report, run the check yourself:

```bash
pnpm task:session-ingest --check
```

The gate rejects a file for a post_id not in the corpus, a quote that is not verbatim in
the post it cites (unicode punctuation and whitespace are forgiven, rewording is not), a
post cited from another account, or an enum outside `ref/`. Hand each rejection line
back to the subagent that produced the file with SendMessage; it still has the bundle in
context and can fix the quote in one turn. Do not fix quotes by hand in the main context.

## Step 7. Ingest and render

```bash
pnpm task:session-ingest
pnpm task:render
```

Ingest writes `data/analysis/accounts/<handle>.json` (profile, narrative, picks, with
`model`, `prompt_version` `v1-acct`, `spec_sha256`, `window_start`, `window_end`), and
the picks layer at `data/picks/ingest_dt=<today>/picks-v1-acct-accounts.parquet` plus
`pick_tags`. Nothing is written if any file fails. Re-ingesting the same window on a
later day is safe: the views keep the latest ingest per `pick_id`.

Render produces `tickers/<SYMBOL>.md` and `INDEX.md`. The `daily/` briefings need the
price layer, which is currently empty, so they stay empty.

## Step 8. Commit, then probe

`data/raw/` is the only unrepurchasable thing in the repo. Commit it with the derived
layers and the analyses in one commit named for the window. The repo is private by
design; X's terms restrict redistribution of post content.

Then run `/corpus-probe`, which reads the analyses and bundles this skill produced, and
after it `/runway-probe`, which ranks the corpus probe's names by outside signals.

## Done when

- the manifest status is `ok`, or every shortfall is listed by handle with its reason
- `pnpm q corpus-coverage` shows every fetched account with first and last day inside the window
- `data/analysis/accounts/` holds one JSON per fetched account and `pnpm task:session-ingest --check` passes
- the final message states posts read, dollars spent, the window, and the accounts that fell short
