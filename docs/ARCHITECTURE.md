# invest — architecture

A private, compounding research corpus built from a strict 12-account X allowlist,
plus a daily human-readable briefing.

The lasting asset is the **structured corpus**, not the prose. The questions worth
answering a year in — who called a name before it moved, which themes recur, which
accounts lead and which echo — are not answerable from a folder of markdown. So the
`.md` is a *rendering* of the corpus, never the corpus itself.

## The two economic facts that shape everything

1. **X API reads are metered per post (~$0.005), not a flat subscription.** Every
   re-read costs money. Capture-once-derive-many is the cost model, not just hygiene.
2. **Recent search reaches back ~7 days; full archive is Enterprise-only (~$42k/mo).**
   History not captured is effectively unbuyable.

Therefore: **`data/raw/` is expensive, irreplaceable, and append-only. Everything
downstream is free to recompute.**

## Storage: git + Parquet + DuckDB ($0/month)

~250 posts/day → ~90k rows/year → well under 100MB/year. At that size the whole
multi-year corpus fits in RAM; any option involving a server or a bill is
over-engineering. Git holds the data, DuckDB queries it.

**The decisive rule: DuckDB is a query engine over files, never a committed database
file.** A binary `.db` is rewritten wholesale on every commit and git cannot
delta-compress its pages — a 20MB db committed daily is ~7GB of git objects a year.
Date-partitioned Parquet adds one small file per day and never rewrites history.

That rule applies to **every** layer, including prices. See "append-only" below.

## Layout

```
data/raw/       ingest_dt=YYYY-MM-DD/posts-<run_id>-<attempt>-p<page>.jsonl.gz
data/posts/     ingest_dt=YYYY-MM-DD/posts-<run_id>.parquet
data/mentions/  ingest_dt=YYYY-MM-DD/mentions-<run_id>.parquet
data/picks/     ingest_dt=YYYY-MM-DD/picks-<prompt_version>-<run_id>.parquet
data/pick_tags/ ingest_dt=YYYY-MM-DD/pick_tags-<prompt_version>-<run_id>.parquet
data/prices/    ingest_dt=YYYY-MM-DD/eod.parquet
data/analysis/  YYYY-MM-DD.json          verbatim LLM output, git-diffable
ref/            tag_taxonomy.csv, symbols.csv, blocklist.csv, enums.json
sql/views.sql   the only sanctioned read path
```

### `ingest_dt` is the CAPTURE date, never the post's creation date

Recent search reaches back 7 days, so a post created on the 1st can be captured on the
6th. Keying partitions on creation date would force rewrites of already-committed
files — binary churn, and the end of immutability. Keying on capture date keeps every
file write-once. `created_at` / `created_date` are carried as ordinary columns, and
date-range queries filter on those.

**Corollary: the same `post_id` will appear in more than one partition.** Never read
the Parquet directly; always read through `sql/views.sql`, which dedupes. This is
enforced by a test (`src/duck/views.test.ts`).

### Run-scoped filenames

A retry, a same-day second run, or a partial-page failure must never overwrite a
complete file — that is a live data-loss path. Every file carries `run_id` and
`attempt`, so a crashed run leaves a harmless orphan that the dedupe views ignore.

### Append-only layers

`raw`, `picks`, `pick_tags`, and `prices` are append-only and are **never
regenerated**:

- **prices** because adjusted closes change retroactively after splits and dividends.
  Overwriting `eod.parquet` destroys the as-of-then value with no error, and makes any
  backtest silently unreproducible. Append with the observation date; the read view
  takes the latest.
- **picks** because LLM output is not deterministic and the model that produced a given
  day will eventually not exist. `prompt_version` is in the filename, so re-running
  history with a new prompt is *additive* — you can A/B two prompts over the same posts
  instead of destroying the older judgment.

`pnpm rebuild` regenerates `posts` and `mentions` only, and refuses to touch the
append-only layers.

### What "regenerable" actually guarantees

Not byte equality — Parquet embeds the writer version in its footer, and gzip embeds an
mtime. The guarantee is **content equality** for `posts` and `mentions`: same row set,
same values, verified by a canonical hash over a deterministic sort. Raw is written with
`gzip -n` so at least that layer is byte-stable.

## Correctness boundaries

**Price facts have exactly one source, and it is not the model.** `ytd`/`mtd`/`yoy` are
computed in `src/prices/` from cached closes. The extraction lane is forbidden from
importing the price layer — enforced by `no-restricted-imports` in `eslint.config.js`.

**Attribution excludes echoes.** A retweet is not a call, and an LLM-inferred mention is
not testimony. `mention_events` filters both out, or the lead/lag leaderboard is quietly
wrong.

**Lead/lag is measured within episodes, not against all history.** A ticker's global
first mention happens once; every "lag" after that week is a meaningless four-digit
number. Mentions are sessionized into episodes (a >7-day gap starts a new one) and lead
time is computed inside each.

**Tag drift needs a denominator.** `ref/tag_taxonomy.csv` records when each tag entered
and left the vocabulary. Without it, adding a tag shows up as a fake regime shift.

**Engagement metrics are snapshots at capture time.** Capture latency varies from minutes
to 7 days, so counts are not comparable across posts. They are named `*_at_ingest` and
always accompanied by `metric_age_seconds`, which cannot be reconstructed later.

## Querying

```bash
pnpm repl          # DuckDB with every view pre-created
pnpm q first-mention --symbol NVDA
```

`INVEST_DATA_ROOT` repoints the identical views at a fixture, or at object storage —
DuckDB reads `s3://` and `r2://` natively, so outgrowing git is one environment
variable, not a migration.

## Not this

No trading execution, no positions or P&L, no web UI, no backfill before day one.
The repo stays **private**: X's developer terms restrict redistribution of post content.
Nothing here is investment advice.
