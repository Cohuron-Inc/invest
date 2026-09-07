# invest

Daily research corpus built from a strict 13-account X allowlist, plus a daily briefing.

- **Design — architecture, decisions, and what was rejected:** [`_plan/design.md`](_plan/design.md)
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

# any time
pnpm rebuild --from 2026-09-08   # re-derives posts/mentions/markdown only
pnpm repl                        # DuckDB with every view pre-created
pnpm q account-lead-lag          # saved analyses
pnpm q first-mention --symbol NVDA
```

Two facts govern the design: X API reads cost ~$0.005 each, and recent search only
reaches back 7 days. So captured data is expensive and unrepurchasable, while everything
derived from it is free to recompute. `data/raw/` is append-only; the rest is rebuilt.

Private by design — X's developer terms restrict redistribution of post content.
Nothing here is investment advice.
