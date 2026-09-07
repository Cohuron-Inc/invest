# invest

Daily research corpus built from a strict 14-account X allowlist, plus a daily briefing.

- **Design — architecture, decisions, and what was rejected:** [`_plan/design.md`](_plan/design.md)
- **Business design — outcome, use cases, products, economics, success measures:** [`_plan/business.md`](_plan/business.md)
- **The only sanctioned read path:** [`sql/views.sql`](sql/views.sql)
- **Saved analyses:** [`queries/`](queries/)

```bash
pnpm install

# once
pnpm task:resolve-accounts   # needs X_BEARER_TOKEN -> fills in accounts.json
pnpm task:sync-universe      # listed symbols from nasdaqtrader.com (free, no key)

# the daily chain (GitHub Actions runs this at 16:15 ET)
pnpm task:capture            # metered: ~$0.005 per post read
pnpm task:normalize          # raw -> posts/mentions parquet
pnpm task:extract            # one claude-opus-5 call per session
pnpm task:enrich             # end-of-day closes -> YTD/MTD/YoY
pnpm task:render             # daily/*.md, tickers/*.md, INDEX.md

# historical backfill — user timeline, NOT recent search, so it reaches past 7 days
pnpm task:backfill --start 2026-07-07T00:00:00Z --max-posts 16000
                             # metered, one-off; --max-posts is a real spend cap

pnpm task:backfill --accounts h1,h2 --start ...   # resume only the handles a 402 or the cap cut off

# analysis without an API key: one subagent per account, inside a Claude Code session
pnpm task:session-dump [--from YYYY-MM-DD --to YYYY-MM-DD]
                             # corpus -> data/_session/<handle>.posts.jsonl (+ SPEC.md, WINDOW.json); keeps out/
                             # ...run one subagent per bundle, writing data/_session/out/<handle>.json
pnpm task:session-ingest --check   # validate citations, write nothing; hand rejections back to the subagent
pnpm task:session-ingest     # -> picks/pick_tags + data/analysis/accounts/ stamped with WINDOW.json dates
pnpm q corpus-coverage       # first/last day per account against the window you paid for
pnpm q retail-interest --symbols "VST,AVGO"   # corpus attention per symbol: accounts, posts, engagement, stances

# any time
pnpm rebuild --from 2026-09-08   # re-derives posts/mentions/markdown only
pnpm repl                        # DuckDB with every view pre-created
pnpm q account-lead-lag          # saved analyses
pnpm q first-mention --symbol NVDA
pnpm q account-convergence       # names more than one account took a position on
pnpm q account-repertoire        # what each account actually does

# The Claude Code chain (skills in .claude/skills/). Each SKILL.md explains the problem it
# solves step by step; run them in this order.
/fetch "from 2026-07-07 to 2026-09-06"   # X API backfill -> normalize -> bundles -> one subagent per
                                        # account in this session (no Anthropic key) -> ingest -> render
/corpus-probe "high return, medium-to-low risk, 1 to 3 years"
                                        # mandate-driven Core/Watch/Satellite read -> data/analysis/probes/
/runway-probe                           # rank those names by twelve signals: earnings, prospect, competition,
                                        # insiders, 13F flow, retail crowding, upside, risk:reward, chart, macro
                                        # fit, narrative harmony, catalysts -> analysis_output/<window_end>-runway-probe.html
                                        # plus the scorecard per name in <window_end>-runway-evidence.md
```

### Two capture paths, and why

`task:capture` is the daily incremental one: `search/recent`, one cursor, ~7-day reach.
`task:backfill` walks each account's **user timeline**, which has no 7-day wall, and is the
only affordable way to acquire history recent search has already dropped. Both write the
same `data/raw/` layout, so nothing downstream can tell them apart. Backfill is not
incremental — re-running it re-reads and re-pays — which is why it takes an explicit
`--max-posts` cap and writes its manifest even when the run dies mid-sweep.

### Two extraction lanes, one contract

`task:extract` sends one trading session to the Anthropic API. The session lane slices by
**author** instead and runs inside an interactive Claude Code session, so it needs no API
key and no per-call billing — the trade is that it answers "how does this commentator
operate" rather than "what happened today". Both land in the same `picks` layer, tagged by
`prompt_version` (`v1` vs `v1-acct`) so they never overwrite each other. The lane swaps the
model call, **not** the validation: `task:session-ingest` re-checks every citation against
the corpus and additionally requires each quote to appear verbatim in the exact post it
cites.

Two facts govern the design: X API reads cost ~$0.005 each, and recent search only
reaches back 7 days. So captured data is expensive and unrepurchasable, while everything
derived from it is free to recompute. `data/raw/` is append-only; the rest is rebuilt.

Private by design — X's developer terms restrict redistribution of post content.
Nothing here is investment advice.
