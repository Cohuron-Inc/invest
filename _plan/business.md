# invest — business design

> Companion to [`design.md`](design.md), which covers architecture and engineering
> decisions. This document covers what the repo is *for*: the business outcome, the use
> cases, the products it produces, what each costs, how success is measured, and what it
> deliberately does not do. Status as of 2026-09-07: first corpus captured (six accounts,
> 7 Jul to 6 Sep 2026), first Corpus Probe and first Runway Probe published, the
> three-skill chain in `.claude/skills/` documented and runnable.

---

## 1. The business outcome

**Turn a stream of market commentary into a compounding, auditable research asset that
tells one book what to own, at what size, and why, with a record of whether it was
right.**

The operator follows a small set of X market commentators. Reading them daily is slow,
the signal is buried under noise, and nothing is retained: a call made in July is
forgotten by September, and no one knows which accounts actually lead. The outcome this
repo buys is threefold:

1. **Memory.** Every post from the allowlist is captured once, structured, and kept.
   Questions that a folder of screenshots cannot answer become queries: who called a name
   first, which themes recur, which accounts revisit their calls, which merely echo.
2. **Judgment on demand.** Three repeatable analyses turn the corpus into decisions for a
   stated mandate: what to tier as Core, Watch or Satellite; which names still have room
   from today's price; and what would prove each verdict wrong.
3. **Accountability.** Every pick is cited to a real post, every outside figure carries
   its source and date, and every verdict is registered with a price, a scenario tree and
   a kill criterion, so later probes score earlier ones. The system learns which accounts
   and which signals deserve trust.

The asset is the structured corpus plus the verdict ledger. The pages are renderings.

---

## 2. Who it is for, and the mandate

A single operator managing a personal or small-fund equity book with a stated mandate.
The mandate used for the first probes: **high return, medium-to-low risk, one to three
years.** The mandate is an input to every probe, not a constant; a different book states
a different one and gets a different tiering from the same corpus.

The operator is technical enough to run `pnpm` tasks and Claude Code skills, and wants
to read a finished page, not a spreadsheet. The repo is private by design: X's developer
terms restrict redistribution of post content, and the verdicts are the operator's own.

---

## 3. Use cases

| # | Use case | Question it answers | Product |
|---|---|---|---|
| U1 | **Build the corpus for a window** | What did these accounts post between two dates, structured and cited? | `/fetch`: raw posts, normalized layers, one analysis per account, the picks layer |
| U2 | **Tier the corpus against a mandate** | Across all accounts, what should this book own, watch, or hold only as a satellite, and what did the accounts know that never became a pick? | `/corpus-probe`: the Corpus Probe page |
| U3 | **Rank remaining upside** | Of those names, which still have room from today's price, judged by earnings, flows, chart, macro fit and narrative, with a verdict that can be proven wrong? | `/runway-probe`: the Runway Probe page, the evidence file, the verdict ledger |
| U4 | **Audit an account** | How does this commentator actually operate: beat, style, whether they revisit calls, what should discount their record? | `data/analysis/accounts/<handle>.json` and the trust section of each probe |
| U5 | **Answer a corpus question directly** | Who mentioned NVDA first? Which names did two or more accounts take a position on? How crowded is ASTS among these accounts? | `pnpm q <saved query>` over DuckDB views |
| U6 | **Score the record** | Were the September verdicts right? Are the scenario probabilities too confident? | `analysis_output/verdicts.jsonl`, read by every later Runway Probe |

U1 through U3 form the chain and are run in that order. U4 and U5 are byproducts
available at any time. U6 is the feedback loop that makes the chain improve.

---

## 4. The value chain

```
X accounts ──$──► raw posts ──► normalized posts, mentions ──► account analyses, picks
                (fetch, X API)   (free to recompute)            (subagents in session)
                                                                        │
mandate ──────────────────────────────────────────────────────► Corpus Probe (page)
                                                                        │
outside evidence (pinned public pages) + macro regime ────────► Runway Probe (page + records)
                                                                        │
                                                                verdict ledger ──► next probe's calibration
```

Value is added at three points, and only the first costs money:

- **Acquisition** turns unbuyable history into a kept asset. X reads are metered and
  recent search reaches back seven days, so the raw layer is expensive, irreplaceable and
  append-only.
- **Structuring** turns text into cited claims with enums a query can group by. It runs
  inside a Claude Code session with subagents, so it has no API bill; the gate that
  verifies every citation against the corpus is what makes the output trustworthy.
- **Judgment** turns claims into decisions. The Corpus Probe reads past the pick lists
  into the evidence the accounts relayed. The Runway Probe adds twelve outside signals,
  computes the mechanical scores deterministically, applies a written perception
  doctrine, red-teams the top names, and registers falsifiable verdicts.

---

## 5. The products

### 5.1 The corpus (U1)

Layers under `data/`: `raw/` (gzip JSONL, append-only, with a manifest per run),
`posts/` and `mentions/` (Parquet, deduped, ticker-resolved, sessionized to ET trading
days), `picks/` and `pick_tags/` (Parquet, cited, provenance-stamped), and
`analysis/accounts/` (one JSON per account: profile, narrative, picks). Read through the
views in `sql/views.sql`, which are the only sanctioned read path.

First corpus: 4,992 posts read for $24.96, six of fourteen accounts before credits ran
out, window 7 Jul to 6 Sep 2026, 108 formal picks across 26 symbols after the citation
gate.

### 5.2 The Corpus Probe (U2)

A fixed-format page: tier cards (Core, Watch, Satellite), the regime the corpus itself
describes and the one portfolio rule it implies, a five-axis table for every Core name
(theme, sentiment, earnings, analyst and insider, risk), the deep-inside signals no
account turned into a pick, contested names with both sides kept, satellites, how much to
trust each account, and what the probe cannot tell you. Saved under
`data/analysis/probes/`, published as an artifact.

First probe: 12 Core, 14 Watch, 11 Satellite names; the regime rule was that with
single-A corporate paper at 6% the hurdle for equity is a visible free-cash-flow yield or
a demonstrated earnings inflection.

### 5.3 The Runway Probe (U3, U6)

The same page discipline applied to the forward question. Inputs are the Corpus Probe's
names; signals are twelve, in four groups: fundamentals (earnings, prospect,
competition), flows and positioning (insider, institutional, retail crowding from the
corpus), price and chart (upside, risk to reward, daily chart), and context (macro
climate, narrative harmony, catalysts). Four gates set the tier; a 100-point rubric sets
the order; a doctrine sets how each data point is perceived and how a verdict is reached;
a red team argues the bear case; every verdict is registered with a scenario tree and a
kill criterion. Outputs under `analysis_output/`: the page, the evidence file, the
per-ticker records, and the ledger.

First probe (three-signal version, before the twelve-signal rebuild): ten Runway names,
ten One-leg-missing, sixteen No-runway, with VST, AVGO, GOOGL, AMZN and SNOW named as the
mandate's fits.

---

## 6. Economics

| Item | Cost | Notes |
|---|---|---|
| X API reads | ~$0.005 per post | The only metered input. ~$25 per two-month window for six accounts; ~$60 for all fourteen. A hard `--max-posts` cap is the spend limit |
| Extraction | $0 | Subagents inside the Claude Code session; no Anthropic API key |
| Outside evidence for the Runway Probe | $0 | Public aggregator and filing pages, fetched by subagents from a pinned registry |
| Storage and query | $0 | git, Parquet, DuckDB |
| Daily capture (when enabled) | ~$38 per month | GitHub Action at 16:15 ET; incremental, never re-reads |
| Operator time per probe | tens of minutes of session time | most of it is subagents running in parallel |

The design keeps the metered input small and everything derived free to recompute, so
the marginal cost of a second mandate, a second window, or a rerun with a corrected
rubric is close to zero.

---

## 7. Success measures

| Measure | How it is read | First reading |
|---|---|---|
| Corpus coverage | `pnpm q corpus-coverage`: first and last day per account against the window paid for | 5 of 6 accounts complete; StockSavvyShay reached only 29 Aug of a 7 Jul window |
| Citation integrity | `session-ingest --check` rejections | 0 of 6 files rejected on the first ingest |
| Pick concentration | `pnpm q account-repertoire`: picks per account, high-conviction share | 8 to 32 picks per account; the accounts differ 4x in volume |
| Cross-account convergence | `pnpm q account-convergence`: names with two or more stances | ASTS, MU, NBIS, TSLA |
| Verdict hit rate | ledger verdicts scored against realized price at horizon, by tier and by signal | not yet available; the ledger is seeded by the next Runway Probe |
| Calibration | scenario probabilities against outcomes across all verdicts | not yet available |
| Account trust | which accounts' picks preceded moves, from `mention_episodes` and the price layer | blocked until the price layer is rebuilt |

The measures that matter most, hit rate and calibration, need the price layer and time.
That is by design: the system is built to be judged on outcomes, and the first months
are spent building the record that makes the judgment possible.

---

## 8. What it is not

- **Not investment advice and not execution.** Every page carries the disclaimer. There
  is no order routing, no positions, no P&L.
- **Not a price service.** The price layer exists and is empty; Stooq stopped serving
  scripts on 6 Sep 2026 and Finnhub is the named replacement. Until it is rebuilt, no
  return is ever computed from corpus data, and the probes say so.
- **Not a market-data platform.** The Runway Probe's outside evidence comes from
  pinned public pages read by subagents, recorded with source and date. It is
  deterministic in procedure, not in infrastructure. A keyed provider layer is the next
  step if the probe cadence justifies it.
- **Not public.** Post content is restricted by X's terms. The repo, the pages and the
  ledger stay private.
- **Not a sentiment scorer.** The tag taxonomy is eight fixed values with a dated
  history. The corpus records stances; it does not grade mood.

---

## 9. Risks and the response

| Risk | Response |
|---|---|
| A commentator's post is deleted or the account goes private | X's terms expect use to stop. `data/raw/` is append-only, so the fix is a tombstone list filtered in the views, not a mutation of raw. Not yet built |
| Aggregator pages change shape or block | The source registry lists a fallback order and a failure log; a blocked source is recorded in the run manifest and the page says which figures were unverifiable |
| Model output invents a citation or a number | The ingest gate rejects any pick whose post_id or quote does not resolve; the extraction contract forbids prices and returns outside verbatim quotes; the Runway Probe's mechanical scores are computed by a script, not by the model |
| The operator trusts a loud account | The trust section is mandatory in every probe; retail crowding is scored as a contrarian signal; the ledger scores the accounts over time |
| Cost overrun on capture | `--max-posts` is a hard cap; a run that dies still writes its manifest; the skill estimates the bill before running |
| Two probes drift in format and stop being comparable | Templates and section order are fixed and the skills forbid changing them |

---

## 10. Roadmap, in business terms

1. **Complete the allowlist.** Eight of fourteen accounts have never been fetched. One
   `/fetch --accounts` run after topping up credits.
2. **Seed the ledger.** Run the twelve-signal Runway Probe once so the calibration loop
   has its first entries.
3. **Rebuild the price layer.** Finnhub or equivalent, so account lead/lag, verdict hit
   rate and post-earnings claims can be scored.
4. **Promote insider filings to a first-class layer.** The filing-feed account's posts
   are the best medium-risk leads in the corpus and are currently read as text.
5. **Second copy of raw.** Nightly sync to object storage; one copy of an unrepurchasable
   dataset is not a backup.
6. **Tombstones for deleted posts**, to honour X's terms.
7. **A keyed market-data layer**, only if probe cadence makes the per-run web research
   the bottleneck.
