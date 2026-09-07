# invest

Daily research corpus built from a strict 12-account X allowlist, plus a daily briefing.

- **Architecture and the invariants that matter:** [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md)
- **The only sanctioned read path:** [`sql/views.sql`](sql/views.sql)
- **Saved analyses:** [`queries/`](queries/)

```bash
pnpm install
pnpm task:resolve-accounts   # once, needs X_BEARER_TOKEN -> fills accounts.json
pnpm task:capture            # daily, metered
pnpm repl                    # DuckDB with every view pre-created
```

Two facts govern the design: X API reads cost ~$0.005 each, and recent search only
reaches back 7 days. So captured data is expensive and unrepurchasable, while everything
derived from it is free to recompute. `data/raw/` is append-only; the rest is rebuilt.

Private by design — X's developer terms restrict redistribution of post content.
Nothing here is investment advice.
