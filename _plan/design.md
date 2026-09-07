# invest — design

> Status: **all five pipeline stages shipped 2026-09-06.** Capture and normalize verified
> against the live X API on 2026-09-06 (10 posts, $0.05). Extraction awaits a live
> `claude-opus-5` call; everything else is proven end to end.
> This is the single design document for the repo: what the system is, why it is shaped
> this way, what was rejected, and what remains.

---

## 1. What this is for

A private, compounding research corpus built from a strict 14-account X allowlist, plus a
daily human-readable briefing.

The lasting asset is the **structured corpus**, not the prose. The questions worth
answering a year in — who called a name before it moved, which themes recur, which
accounts lead and which merely echo — cannot be answered from a folder of markdown files.
So the `.md` is a *rendering* of the corpus, never the corpus itself.

### The two economic facts that shape everything

1. **X API reads are metered per post (~$0.005), not a flat subscription.** X moved to
   pay-per-use with no free tier; the legacy $200/mo Basic and $5,000/mo Pro tiers are
   closed to new signups. At ~250 posts/day this is ~$38/month — but *every re-read costs
   money*, so capture-once-derive-many is the cost model, not merely good hygiene.
2. **Recent search reaches back ~7 days; full archive is Enterprise-only (~$42k/mo).**
   History not captured is effectively unbuyable.

Together: **`data/raw/` is expensive, irreplaceable, and append-only. Everything
downstream is free to recompute.** Nearly every decision below follows from that
asymmetry.

---

## 2. Storage: git + Parquet + DuckDB ($0/month)

### The workload is small

| Metric | Value |
|---|---|
| Rows written | ~250/day → ~90k/year |
| All layers combined | ~90 MB/year |
| Writers | 1 (the cron) |
| Readers | 1 (analyst), analytical, latency-insensitive |
| Query shape | scans, group-bys, window functions over ≤1M rows |

At this size the entire multi-year corpus fits in RAM. **Any option involving a server, an
account, or a monthly bill is over-engineering.** The real question was which zero-cost
option has the best query ergonomics.

### Options considered

| Option | Cost/mo | Real SQL | Verdict |
|---|---|---|---|
| **Git repo (Parquet) + DuckDB** | **$0** | ✅ incl. window fns | **Chosen** |
| SQLite committed to repo | $0 | ✅ | ❌ git trap — below |
| `.duckdb` file committed | $0 | ✅ | ❌ same git trap |
| Cloudflare R2 + DuckDB | ~$0.01 | ✅ | Escape hatch, not day 1 |
| Turso / libSQL free tier | $0 | ✅ | Entrusting an irreplaceable dataset to a startup free tier, for no gain at 90k rows/yr |
| Neon / Supabase free | $0 | ✅ | No diffability or audit trail over data changes; you'd need a backup pipeline anyway, at which point Postgres is a redundant middleman |
| DynamoDB | ~$0.10 | ❌ | OLTP key-value store; all five query shapes are scans with grouping and windowing. Wrong even with GSIs |
| S3 + Athena | ~$0.02 + $5/TB | ✅ | Glue catalog, latency, per-query cost, AWS coupling — for scale we won't reach in a decade. Note DuckDB reads S3 with **no** catalog, so "S3 + DuckDB" is already the escape hatch |

### The git trap

A binary database file is rewritten wholesale on every daily commit, and git cannot
delta-compress its pages. A 20 MB `.db` committed daily produces **~7 GB of git objects per
year**. Date-partitioned Parquet instead *adds one small file per day* and never rewrites
history — exactly the write pattern git is good at.

**The decisive rule: DuckDB is a query engine over files, never a committed binary database.**

That rule applies to *every* layer. The first draft of this design violated it in the price
layer (see §6.1).

### Concrete thresholds

At ~90 MB/year of immutable new bytes: GitHub's 1 GB "recommended" ceiling is reached
around **year 11**, the 5 GB "we may contact you" mark around **year 55**. File count
reaches ~15,000 at year 10 — the Linux kernel is ~80,000. Since every file is written once
and never rewritten, there is no delta opportunity to defeat; the cost is exactly the
compressed byte size.

`actions/checkout` defaults to `fetch-depth: 1`, so history growth is free for CI; only the
working tree grows. Sparse-checkout is the fix if that ever bites — cheap now, a path audit
later.

### Why this isn't a cheap-now trap

DuckDB reads `s3://`, `r2://` and `https://` natively with predicate pushdown, and the view
definitions are parameterised through `INVEST_DATA_ROOT`. Outgrowing git is **one
environment variable**, not a migration.

### The bonus only this option gives

The storage layer *is* the version history and *is* the backup. "What did the corpus look
like before I changed the extraction prompt" is a `git checkout`.

---

## 3. Layout

```
data/raw/       ingest_dt=YYYY-MM-DD/posts-<run_id>-a<attempt>-p<page>.jsonl.gz
data/posts/     ingest_dt=YYYY-MM-DD/posts.parquet
data/mentions/  ingest_dt=YYYY-MM-DD/mentions.parquet
data/picks/     ingest_dt=YYYY-MM-DD/picks-<prompt_version>-<day>.parquet
data/pick_tags/ ingest_dt=YYYY-MM-DD/pick_tags-<prompt_version>-<day>.parquet
data/prices/    ingest_dt=YYYY-MM-DD/eod-<provider>.parquet
data/analysis/  YYYY-MM-DD.json          verbatim LLM output, git-diffable
ref/            accounts are in /accounts.json; tag_taxonomy, symbols,
                bare_allowlist, blocklist, universe, enums
sql/views.sql   the only sanctioned read path
queries/        saved analyses
daily/ tickers/ INDEX.md                 rendered output
```

### `ingest_dt` is the CAPTURE date, never the post's creation date

Recent search reaches back 7 days, so a post created on the 1st can be captured on the 6th.
Keying partitions on creation date would force rewrites of already-committed files — binary
churn, and the end of immutability. Keying on capture date keeps every file write-once.
`created_at`, `created_date` and `trading_day` are ordinary columns.

**Corollary: the same `post_id` will appear in more than one partition.** Never read the
Parquet directly; always read through `sql/views.sql`, which dedupes. Enforced by test.

### Run-scoped filenames

A retry, a same-day second run, or a partial-page failure must never overwrite a complete
file — that is a live data-loss path. Every raw file carries `run_id`, `attempt` and page,
so a crashed run leaves a harmless orphan the dedupe views ignore.

### Append-only layers

`raw`, `picks`, `pick_tags` and `prices` are append-only and **never regenerated**:

- **prices**, because adjusted closes are restated retroactively after splits and
  dividends. Overwriting destroys the as-of-then value with no error, making backtests
  silently unreproducible.
- **picks**, because LLM output is not deterministic and the model that produced a given
  day will eventually be retired. `prompt_version` is in the filename, so re-running
  history with a new prompt is *additive* — you can A/B two prompts over the same posts
  rather than destroying the earlier judgment.

`pnpm rebuild` regenerates `posts`, `mentions` and the markdown only, and **refuses**
`--picks`/`--prices` with a non-zero exit.

### What "regenerable" actually guarantees

Not byte equality — Parquet embeds the writer version in its footer. The guarantee is
**content equality** for `posts` and `mentions`: same rows, same values. Raw is written
with a zero gzip MTIME (asserted on the header bytes, since Node exposes no option for it)
so that layer *is* byte-stable, and rendered markdown is byte-identical across runs.

---

## 4. Pipeline

| # | Stage | Input | Output | Entry point |
|---|---|---|---|---|
| 1 | **capture** | X API | `data/raw/` | `pnpm task:capture` |
| 2 | **normalize** | raw | `posts`, `mentions` | `pnpm task:normalize` |
| 3 | **extract** | posts | `analysis/*.json`, `picks`, `pick_tags` | `pnpm task:extract` |
| 4 | **enrich** | mentions + Stooq | `prices` | `pnpm task:enrich` |
| 5 | **render** | all | `daily/`, `tickers/`, `INDEX.md` | `pnpm task:render` |

**capture** — one `GET /2/tweets/search/recent` with a `from:` disjunction covering all 13
accounts (~290 chars, inside the 512 limit), so one request, one cursor, one rate budget.
`buildQueries` splits rather than truncates if the allowlist ever outgrows the cap. Cold
start sweeps the full 7-day window. A cost guard aborts at 3× the trailing median.

**normalize** — dedup, ticker resolution, `post_type` and `metric_age_seconds`
materialised, deterministic sort.

**extract** — one `claude-opus-5` call per session, adaptive thinking, native
`output_config.format` structured outputs. Separate retry budgets for bad output vs.
provider overload. Provenance (`model`, `prompt_version`, `prompt_sha256`, `schema_hash`,
`llm_response_sha256`) travels with every pick.

**enrich** — behind a one-function provider interface. Stooq (free, no key, no signup; full
daily history in one CSV request) was the day-one provider and is **currently blocked** — see
§7.1. Finnhub is the named alternative.

**render** — daily briefings, rolling per-ticker pages, index. Idempotent.

---

## 5. Correctness boundaries

**Price facts have exactly one source, and it is not the model.** `ytd`/`mtd`/`yoy` are
computed in `src/prices/` from real closes. The extraction lane is barred from importing
the price layer by `no-restricted-imports` in `eslint.config.js` — a lint rule rather than
a convention, because a model asked for "YTD" will always produce a confident, invented
number. Absent data renders as an em dash, never `0`, which would read as "flat".

**Every claim is cited, and citations are checked.** The schema guarantees shape, not
truth: a model can emit a well-formed `post_id` that does not exist. `assertCitationsResolve`
fails the run rather than writing a fabricated citation to disk.

**Bare tickers are an allowlist, not the universe.** Syncing the real 12,632-symbol listed
universe surfaced ~41 ordinary English words that are live tickers — `HOLD`, `NOW`, `TOP`,
`OPEN`, `TIME`, `LOW`, `HIGH`, `PLAY`, `CASH`, `ALL`, `IT`, `ON`. Matching those bare would
put a false mention in nearly every post, and one false mention corrupts recurrence,
lead/lag and hit-rate simultaneously. So `$CASHTAG` always resolves; a bare token resolves
only from `ref/bare_allowlist.csv`. Listed-but-not-allowlisted tokens land in the
`unresolved` column — the feedback loop that grows the allowlist from evidence.

**Nothing is discarded at normalize time.** Re-deriving is free; re-reading is $0.005/post
and impossible past 7 days. Crypto and private names are recorded with `asset_class` set
and price fields left `NULL`, so adding crypto later is a `rebuild`, not a re-purchase.

**Attribution excludes echoes.** A retweet is not a call and an LLM-inferred mention is not
testimony; `mention_events` filters both out, or the lead/lag leaderboard is quietly wrong.

**Lead/lag is measured within episodes.** A ticker's global first mention happens once;
every "lag" after that week is a meaningless four-digit number. Mentions are sessionized
(a >7-day gap starts a new episode) and lead time is computed inside each.

**Tag drift needs a denominator.** `ref/tag_taxonomy.csv` records when each tag entered and
left the vocabulary. Without it, adding a tag reads as a regime shift.

**Engagement metrics are capture-time snapshots.** Capture latency varies from minutes to 7
days, so counts are not comparable across posts. They are named `*_at_ingest` and always
accompanied by `metric_age_seconds`, which cannot be reconstructed after the fact.

**The capture cursor comes from the raw layer.** Not a state file — the only path two runs
would both rewrite, and the sole source of rebase conflicts. Not the normalized layer —
which can lag or fail while capture has already committed, causing us to re-read and re-pay.
`max(post_id)` over raw is the cursor, since post ids are snowflakes.

---

## 6. Corrections made during design review

An adversarial review of the first draft found six flaws in the "expensive to change later"
class. All were fixed before pipeline code was written against the wrong layout.

### 6.1 The price layer was a git-churn bomb

The draft had `data/prices/symbol=NVDA/eod.parquet` **rewritten in place daily** — exactly
the committed-binary trap argued against for SQLite, reproduced in the price layer. At ~400
symbols that is ~2.9 GB/year of git objects versus ~90 MB for everything else, hitting
GitHub's 5 GB threshold in year two. Now append-only by capture date, which also preserves
point-in-time adjusted closes.

### 6.2 "Regenerable byte-identically" was false

Parquet embeds the writer version, gzip embeds an mtime, and LLM output is not
deterministic. Worse, the draft's own rollback step ("delete `data/picks/` and re-run")
would have destroyed a year of one model's judgments. Replaced with content equality for
derived layers, and append-only protection for the rest.

### 6.3 Partition key was ambiguous

Resolved to `ingest_dt` (capture date) — see §3.

### 6.4 A retry could truncate a complete capture

One fixed file per day forced overwrite semantics on the append-only layer. Filenames now
carry run/attempt/page.

### 6.5 `metric_age_seconds` was missing

Cannot be reconstructed later; without it every engagement analysis is silently biased.

### 6.6 Lead/lag needed episodes

See §5.

### A correction to the record

The first draft rejected Neon/Supabase on "free tiers auto-suspend and break the cron."
That reasoning was **wrong** — Neon resumes on connection in ~1s, and Supabase pauses only
after 7 days of inactivity, which a daily cron prevents. The conclusion stands for the
reasons in the §2 table.

---

## 7. Findings from writing the code

Three things the implementation contradicted:

- **`occurrences` was always 1.** Each extraction pass skipped symbols an earlier pass had
  seen, so repeats never incremented. Rewritten with span-masking, so `$NVDA` is counted
  once as a cashtag rather than twice (again as the bare token inside it).
- **`mtime` is not a real Node zlib option.** The determinism test passed anyway because
  Node already writes zero. Now asserted on the gzip header bytes directly — verifying the
  property rather than trusting an option that does not exist.
- **`source` is a DuckDB reserved word.** Renamed to `mention_source` / `price_source`
  before it became a permanent quoting hazard.

Two dependency traps caught before installing: `typescript-eslint` does not support
TypeScript 7, and vitest 5 requires Node ≥22. Pinned TypeScript 5.9.3 and vitest 4.1.11.

### 7.1 Stooq stopped serving CSV to scripts (observed 2026-09-06)

`https://stooq.com/q/d/l/` now answers with **HTTP 200 and a JavaScript proof-of-work
challenge page** rather than CSV, for every symbol. A first enrich run over 698 corpus
symbols wrote zero rows.

The provider interface did its job: `fetchDaily` checks that the body starts with `Date,`
and returns `null` otherwise, so 698 unusable responses produced 698 skips, no exception,
and no garbage in the price layer. The `Bar[] | null` contract — "null means no series, not
an error" — is what kept a vendor outage from becoming a data-corruption event.

Not done, deliberately: the challenge is a hashcash the client could solve in a few lines.
Defeating a site's bot control to keep taking its free data is not a dependency, it is a
liability. The price layer stays empty until a provider we are actually entitled to query
is wired in.

**Consequence:** `ytd`/`mtd`/`yoy` render as em dashes, which is the designed behaviour for
absent data (§5) and not a silent zero. Nothing else in the corpus depends on prices, so
capture, normalize, extract and render are unaffected.

### 7.2 X's cashtag entities are not all cashtags (found in the first backfill)

`entities.cashtags` from the X API is looser than the name implies. In a post reading
"CFO sold $1.77M of stock" it returns `1.77M` as a cashtag entity — and an insider-filing
feed is nothing but such sentences.

The resolver's own `CASHTAG_RE` already required a letter-initial token of at most six
characters, so the text-scanning path had always rejected these. The entity path skipped
the check entirely, so **the two paths disagreed about what a ticker is**, and the looser
one won whenever X supplied an entity. Each money amount became a distinct "symbol" with
its own ticker page and its own mention history.

Real cost in the 4,992-post backfill: 11 fabricated symbols out of 698 — 0.3% of mentions.
Small, but exactly the class of error §5 says corrupts recurrence and lead/lag, and it
scales with how much of the corpus is filing-style commentary.

Fixed by extracting the shape rule into `isTickerShaped()` and applying it to both paths.
The span is still masked when rejected, so a discarded `$25MM` cannot reappear as a bare
`MM` match. Private names (ANTHROPIC, OPENAI, SPACEX) resolve through the security-name
path and are unaffected by the six-character cap.

**Only `mentions` had to be rebuilt** — no re-reading, no re-payment. This is the
append-only/derived split doing the job it was designed for.

---

## 8. Deployment

`.github/workflows/daily.yml`, cron at 20:15 UTC (16:15 ET), `concurrency: { group: daily,
cancel-in-progress: false }` — a cancelled capture spends money and commits nothing.

**Two jobs, and the split is the point.** `capture` runs alone, uploads the raw bytes as an
artifact *before* attempting the commit, then commits and pushes with rebase-retry.
`derive` runs after it from a fresh checkout. Capture's failure mode differs in kind from
everything downstream: reads cost money and cannot be replayed past 7 days, while every
derived stage re-runs for free. A render bug must never cost a day of paid data.

Repo-scoped Actions secrets: `X_BEARER_TOKEN`, `ANTHROPIC_API_KEY`.
A ruleset on `main` blocks deletion and force-push, with **no bypass even for admins**.

### Running cost

| Item | Monthly |
|---|---|
| X API (~250 posts/day @ ~$0.005) | ~$38 |
| Claude (one Opus 5 call/day) | ~$12 |
| Storage + query | **$0** |
| GitHub Actions | $0 (within the Team allowance) |
| **Total** | **~$50** |

The X API is ~75% of the bill, which is why read discipline is a *cost control*.

---

## 9. Verification

67 tests, typecheck and lint green in CI.

| Claim | How it is proven |
|---|---|
| Dedupe across partitions | `src/duck/views.test.ts` — a post in two ingest partitions returns once, attributed to the earliest capture |
| ET session boundary, incl. both DST transitions | `src/lib/time.test.ts` |
| Retry cannot truncate a good file | `src/capture/writer.test.ts` |
| Raw bytes are stable across time | gzip header MTIME asserted zero |
| Common words are not tickers | `src/normalize/tickers.test.ts`, run against the **real** 12,632-symbol universe |
| Fabricated citations fail the run | `src/extract/validate.test.ts` |
| Private names are never priced | `src/prices/returns.test.ts`, `src/render/daily.test.ts` |
| Whole chain, raw → markdown | `src/pipeline.test.ts`, including byte-identical re-render |

### Verified against the live API (2026-09-06, 10 posts, $0.05)

A deliberately capped run (`--max-pages 1 --max-results 10`) into a scratch data root:

| Check | Result |
|---|---|
| Field completeness across 10 real posts | 0 missing handles, hashes, ages, sessions |
| `post_type` from real `referenced_tweets` | original / reply / quote / retweet all present and correct |
| ET session roll | posts created 09-06 after 16:00 ET correctly assigned to the 09-07 session |
| Attribution excludes echoes | 4 mentions, 3 attributable, 1 retweet excluded |
| Ticker resolution | GOOGL, NVDA, TSLA, UBER — all via cashtag, all classified `equity` |
| Bare-allowlist precision | `AGI` appeared in an AI-themed post. It is a real listed ticker (Alamos Gold), and the resolver correctly did **not** create a mention — it surfaced in `unresolved` instead |
| `metric_age_seconds` spread | 94s to 9,398s — a 100x range in observation age within a single page, which is the bias this column exists to make conditionable |

**Still unverified:** a live `claude-opus-5` structured-output call. Fixtures cannot prove it.

---

## 10. Non-goals

No trading execution, no positions or P&L, no web UI, no backfill before day one, no
sentiment scoring beyond the tag enum. The repo stays **private**: X's developer terms
restrict redistribution of post content. Nothing here is investment advice.

---

## 11. Remaining work

1. **First full production capture.** Recent search reaches back 7 days, so the cold-start
   sweep should run soon — that week is otherwise unbuyable.
2. **Verify extraction against a live model call.** The only stage never exercised end to end.
3. **Honour deletions.** X's developer terms expect content to stop being used once a post
   is deleted or an account goes private. `data/raw/` is append-only and never revisited, so
   nothing currently enforces this. A periodic re-check that drops content for posts which
   no longer resolve is the fix; it conflicts with strict append-only, and the resolution is
   probably a tombstone list plus a filter in the views rather than mutating raw.
4. **Replace the price provider.** Stooq is blocked (§7.1); the layer is empty. Finnhub's
   free tier needs a key and a signup, which is the cost of a source that wants to be
   queried. `toStooqSymbol` is the only Stooq-shaped thing outside the provider, so the
   swap is one file.
5. Grow `ref/bare_allowlist.csv` from the `unresolved` column as real data accumulates.
6. **Second copy.** For a dataset costing ~$450/yr to acquire and unrecoverable past 7
   days, one copy is not a backup. Nightly `rclone` to R2 (10 GB free tier) is the
   escape hatch and a future UI backend at the same time.
7. Weekly integrity job: gunzip every raw file, verify counts against manifests, assert
   every `posts.raw_sha256` resolves.
8. Sparse-checkout in CI before the working tree grows enough to matter.
