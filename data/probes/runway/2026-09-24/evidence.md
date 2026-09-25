# September Runway Probe: evidence, 2026-09-24

## Manifest

- Price date 2026-09-24; 13F vintage 2026-06-30; horizon 3-6 months inside the 1-3 year mandate.
- Universe: every symbol any of the 14 allowlisted accounts mentioned 2026-07-07..2026-09-25 (pnpm q ticker-universe --days 120), kept if 3+ accounts or 10+ posts, operating US-listed equities only (ETFs, indices, crypto and private companies dropped), plus 15 operator additions. 123 names screened on Finviz (`data/probes/runs/2026-09-24/screen.py`), 74 researched in ten subagent groups. Dropped before the screen: ANTHROPIC OPENAI SPACEX STRIPE (private);  SPY QQQ SMH IGV IWM XLK XBI MAGS XLV QQQM SPMO VOO VGT (ETFs);  VIX SPX (indices);  BTC ETH (crypto);  GOOG (duplicate of GOOGL); non-operating: DRAM, AOTG.
- Screen overrides (researched despite the proxy): SPCX, SKHY, NBIS, ALAB, CRM, each with its reason in screen.py.
- Sources failed:
  - finance.yahoo.com /quote/T/analysis/ (most of the 74): 'Oops, something went wrong' or empty EPS Trend tables; quoteSummary API 429
  - zacks.com detailed-estimates (G1, G6 (CRM, ALAB)): bot wall on some names; worked on others
  - fintel.io (all): not tried: failure log says 403
  - stockanalysis.com /forecast/ (all): FY2 estimates and FY2 EBIT behind Pro paywall; only the 5-8 newest analyst actions shown
  - stockanalysis.com /stocks/plpc/forecast/ (PLPC): 404
  - marketbeat.com /price-target/ (all): 301 redirect; table is on /forecast/
  - cnbc.com (several): 403 to WebFetch
  - finviz.com via curl without a browser UA (SPY, sector ETFs): empty body; the repo fetcher's UA works
  - finviz insider table (SE, BABA, GOOGL): capped at 100 rows (SE back to 8/11 only); BABA sale valued at per-ADS price x ordinary shares (8x); GOOGL table carried GV rows for another issuer
- Rubric changes made in this run: no-guidance policy is neutral on the delivery gate; an R:R anchor within 5% of the close is rejected; unverified plan status is no longer labelled 10b5-1.
- Disclosure: one research subagent sent the operator's email in the SEC EDGAR User-Agent header without asking.

## Macro

| Item | Value | As of |
|---|---|---|
| fed_target_pct | 3.75-4.00 | 2026-09-24 |
| dgs2_pct | 4.85 | 2026-09-23 |
| dgs10_pct | 5.11 | 2026-09-23 |
| dgs30_pct | 5.4 | 2026-09-23 |
| real10y_pct | 2.76 | 2026-09-23 |
| t10y2y_pct | 0.26 | 2026-09-23 |
| ig_oas_pct | 0.77 | 2026-09-23 |
| hy_oas_pct | 2.73 | 2026-09-23 |
| vix | 14.21 | 2026-09-22 |
| move | 104.58 | 2026-09-24 |
| dxy | 101.25 | 2026-09-24 |
| wti | 96.41 | 2026-09-22 |
| mortgage30_pct | 7.03 | 2026-09-24 |
| unrate_pct | 4.1 | 2026-08-01 |

Regime: Lean risk-off (-4.8). Long duration headwind (fit -1.3); against: R_REAL10, R_10Y_1M, R_LONG_END; for: none. Hurdle: single-A about 5.6% a year, 2.8% for six months; equity bar +8% core, +20% satellite over six months.

## Scorecard (generated)

| # | Ticker | Tier | Close | Upside | R:R | Earn | Prosp | Comp | Insd | Inst | Retail | Up | RR | Chart | Macro | Narr | Total | Gates failed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | NXPI | runway | 230.16 | 35% | 2.0 | 14 | 5 | 5 | 2 | 7 | 9 | 8 | 7 | 2 | 5 | 3 | 67 | none |
| 2 | CSCO | runway | 106.97 | 28% | 3.0 | 14 | 5 | 4 | 2 | 7 | 9 | 6 | 7 | 3 | 5 | 3 | 65 | none |
| 3 | UNH | runway | 375.01 | 28% | 5.4 | 14 | 6 | 5 | 2 | 7 | 3 | 6 | 10 | 3 | 5 | 3 | 64 | none |
| 4 | KURA | runway | 10.86 | 195% | 20.1 | 6 | 5 | 4 | 9 | 7 | 6 | 10 | 10 | 3 | 1 | 2 | 63 | none |
| 5 | GRAB | runway | 3.11 | 87% | 7.3 | 6 | 5 | 4 | 7 | 7 | 6 | 10 | 10 | 0 | 3 | 2 | 60 | none |
| 6 | AMBA | runway | 69.86 | 28% | 4.0 | 10 | 4 | 3 | 2 | 7 | 9 | 6 | 10 | 3 | 2 | 3 | 59 | none |
| 7 | AVGO | runway | 350.36 | 52% | 3.0 | 10 | 5 | 4 | 2 | 7 | 3 | 10 | 10 | 0 | 4 | 3 | 58 | none |
| 8 | STIM | runway | 2.82 | 104% | 2.9 | 6 | 3 | 2 | 4 | 7 | 9 | 10 | 7 | 5 | 0 | 1 | 54 | none |
| 9 | DAL | runway | 82.76 | 25% | 2.8 | 10 | 4 | 4 | 0 | 7 | 9 | 6 | 7 | 3 | 2 | 2 | 54 | none |
| 10 | RARE | runway | 14.77 | 90% | 6.5 | 6 | 3 | 3 | 2 | 7 | 9 | 10 | 10 | 0 | 1 | 1 | 52 | none |
| 11 | APLD | runway | 27.06 | 145% | 7.7 | 6 | 4 | 3 | 2 | 7 | 6 | 10 | 10 | 0 | 1 | 1 | 50 | none |
| 12 | GRRR | runway | 14.36 | 140% | 3.8 | 6 | 2 | 2 | 3 | 7 | 3 | 10 | 10 | 3 | 1 | 2 | 49 | none |
| 13 | ORCL | runway | 139.54 | 71% | 3.9 | 6 | 5 | 4 | 2 | 7 | 3 | 10 | 10 | 0 | 1 | 1 | 49 | none |
| 14 | WYFI | runway | 20.26 | 100% | 2.1 | 6 | 2 | 2 | 3 | 3 | 6 | 10 | 7 | 0 | 0 | 1 | 40 | none |
| 15 | TXN | one_leg_missing | 270.65 | 20% | 2.2 | 14 | 6 | 5 | 2 | 7 | 9 | 3 | 7 | 3 | 5 | 3 | 64 | upside |
| 16 | UBER | one_leg_missing | 69.22 | 46% | 8.4 | 6 | 6 | 5 | 7 | 7 | 6 | 8 | 10 | 0 | 5 | 3 | 63 | delivery |
| 17 | ASML | one_leg_missing | 1722.50 | 24% | 2.1 | 14 | 6 | 7 | 0 | 7 | 6 | 6 | 7 | 3 | 4 | 3 | 63 | insider |
| 18 | WDC | one_leg_missing | 450.31 | 48% | 7.1 | 6 | 6 | 5 | 0 | 7 | 9 | 8 | 10 | 3 | 4 | 4 | 62 | upside |
| 19 | AMAT | one_leg_missing | 474.25 | 35% | 3.1 | 6 | 6 | 5 | 2 | 7 | 9 | 8 | 10 | 3 | 4 | 2 | 62 | insider |
| 20 | NVDA | one_leg_missing | 224.58 | 46% | 4.1 | 6 | 7 | 6 | 2 | 7 | 0 | 8 | 10 | 5 | 4 | 5 | 60 | insider |
| 21 | LRCX | one_leg_missing | 307.16 | 21% | 3.8 | 6 | 6 | 5 | 2 | 7 | 9 | 6 | 10 | 3 | 4 | 2 | 60 | insider |
| 22 | NU | one_leg_missing | 13.56 | 38% | 3.3 | 6 | 6 | 5 | 0 | 7 | 9 | 8 | 10 | 2 | 3 | 3 | 59 | insider |
| 23 | AMZN | one_leg_missing | 249.38 | 32% | 4.1 | 6 | 6 | 6 | 2 | 7 | 3 | 6 | 10 | 3 | 4 | 6 | 59 | insider |
| 24 | VST | one_leg_missing | 137.94 | 58% | 2.5 | 3 | 4 | 5 | 4 | 9 | 6 | 10 | 7 | 0 | 5 | 4 | 57 | delivery |
| 25 | BABA | one_leg_missing | 110.63 | 68% | 4.9 | 3 | 4 | 4 | 7 | 7 | 6 | 10 | 10 | 0 | 2 | 3 | 56 | delivery |
| 26 | RDDT | one_leg_missing | 152.72 | 40% | 2.7 | 10 | 5 | 4 | 2 | 7 | 9 | 8 | 7 | 0 | 2 | 2 | 56 | insider |
| 27 | SPCX | one_leg_missing | 148.03 | 50% | 9.3 | 6 | 5 | 6 | 2 | 7 | 3 | 10 | 10 | 3 | 1 | 2 | 55 | insider |
| 28 | GLW | one_leg_missing | 154.15 | 25% | 1.5 | 10 | 5 | 4 | 2 | 7 | 9 | 6 | 4 | 3 | 3 | 2 | 55 | upside |
| 29 | UUUU | one_leg_missing | 11.32 | 113% | 20.4 | 3 | 3 | 3 | 7 | 9 | 6 | 10 | 10 | 0 | 1 | 1 | 53 | delivery |
| 30 | CRDO | one_leg_missing | 195.97 | 43% | 7.7 | 10 | 6 | 4 | 0 | 7 | 3 | 8 | 10 | 3 | 1 | 1 | 53 | insider |
| 31 | OSCR | one_leg_missing | 28.87 | 20% | 2.0 | 14 | 6 | 4 | 0 | 7 | 3 | 3 | 4 | 3 | 3 | 3 | 50 | upside |
| 32 | ACHR | one_leg_missing | 5.71 | 86% | 4.0 | 6 | 1 | 2 | 2 | 9 | 6 | 10 | 10 | 2 | 0 | 1 | 49 | delivery |
| 33 | IREN | one_leg_missing | 46.15 | 71% | 10.4 | 3 | 4 | 3 | 3 | 7 | 3 | 10 | 10 | 3 | 1 | 2 | 49 | delivery |
| 34 | AKAM | one_leg_missing | 110.41 | 39% | 2.5 | 3 | 3 | 3 | 2 | 7 | 6 | 8 | 7 | 2 | 5 | 3 | 49 | delivery |
| 35 | RKLB | one_leg_missing | 73.61 | 49% | 3.7 | 6 | 4 | 4 | 0 | 9 | 3 | 8 | 10 | 2 | 1 | 1 | 48 | insider |
| 36 | PLPC | one_leg_missing | 429.82 | n/f% | n/f | 6 | 6 | 5 | 0 | 7 | 9 | 0 | 0 | 5 | 4 | 4 | 46 | upside |
| 37 | WULF | one_leg_missing | 16.29 | 111% | 14.0 | 3 | 3 | 2 | 4 | 3 | 6 | 10 | 10 | 0 | 0 | 1 | 42 | delivery |
| 38 | EOSE | one_leg_missing | 3.24 | 104% | 14.7 | 3 | 2 | 1 | 4 | 3 | 6 | 10 | 10 | 0 | 0 | 2 | 41 | delivery |
| 39 | APP | one_leg_missing | 312.47 | 59% | n/f | 3 | 4 | 5 | 2 | 7 | 6 | 10 | 0 | 0 | 2 | 2 | 41 | delivery |
| 40 | ONDS | one_leg_missing | 7.60 | 156% | 4.5 | 3 | 3 | 2 | 2 | 3 | 6 | 10 | 10 | 0 | 0 | 1 | 40 | delivery |
| 41 | CIFR | one_leg_missing | 18.10 | 72% | 1.8 | 3 | 3 | 2 | 2 | 7 | 6 | 10 | 4 | 2 | 0 | 1 | 40 | delivery |
| 42 | SOFI | one_leg_missing | 16.80 | 21% | 1.8 | 6 | 5 | 3 | 2 | 7 | 3 | 6 | 4 | 0 | 2 | 2 | 40 | upside |
| 43 | CAT | no_runway | 805.25 | 21% | 0.7 | 14 | 7 | 6 | 2 | 7 | 9 | 6 | 1 | 3 | 5 | 4 | 64 | none |
| 44 | ANET | no_runway | 205.70 | 18% | 2.3 | 14 | 7 | 6 | 0 | 7 | 9 | 3 | 7 | 5 | 3 | 3 | 64 | upside, insider |
| 45 | VIAV | no_runway | 37.23 | 65% | 1.0 | 14 | 5 | 4 | 0 | 7 | 9 | 10 | 1 | 3 | 3 | 3 | 59 | none |
| 46 | GEV | no_runway | 955.04 | 30% | 0.7 | 10 | 6 | 6 | 3 | 9 | 6 | 6 | 1 | 3 | 5 | 4 | 59 | none |
| 47 | LITE | no_runway | 929.04 | 24% | 2.0 | 14 | 7 | 6 | 0 | 7 | 3 | 6 | 7 | 5 | 2 | 1 | 58 | upside, insider |
| 48 | ON | no_runway | 73.15 | 42% | 1.1 | 14 | 4 | 4 | 3 | 7 | 9 | 8 | 1 | 0 | 4 | 3 | 57 | none |
| 49 | SNDK | no_runway | 1753.62 | 22% | 0.6 | 14 | 7 | 4 | 2 | 7 | 3 | 6 | 1 | 3 | 4 | 5 | 56 | insider |
| 50 | SNOW | no_runway | 334.00 | 27% | 0.8 | 14 | 7 | 4 | 0 | 7 | 6 | 6 | 1 | 5 | 1 | 3 | 54 | insider |
| 51 | STLN | no_runway | 6.51 | 38% | 1.1 | 6 | 5 | 3 | 4 | 7 | 6 | 8 | 1 | 5 | 3 | 3 | 51 | none |
| 52 | ISRG | no_runway | 399.52 | 19% | 1.1 | 10 | 5 | 5 | 2 | 7 | 9 | 3 | 1 | 2 | 3 | 4 | 51 | upside |
| 53 | GOOGL | no_runway | 342.36 | 25% | 0.8 | 6 | 6 | 6 | 2 | 7 | 3 | 6 | 1 | 3 | 4 | 5 | 49 | none |
| 54 | CRM | no_runway | 238.22 | 18% | 1.2 | 6 | 5 | 4 | 4 | 7 | 6 | 3 | 1 | 5 | 5 | 3 | 49 | upside |
| 55 | COHR | no_runway | 290.61 | 43% | 0.7 | 6 | 6 | 5 | 0 | 7 | 9 | 8 | 1 | 3 | 2 | 1 | 48 | none |
| 56 | CCJ | no_runway | 88.12 | 45% | 3.8 | 3 | 4 | 4 | 0 | 9 | 6 | 8 | 10 | 0 | 1 | 1 | 46 | insider, delivery |
| 57 | MU | no_runway | 1080.53 | 40% | 1.0 | 6 | 7 | 5 | 0 | 7 | 0 | 8 | 1 | 3 | 4 | 5 | 46 | upside, insider |
| 58 | SKHY | no_runway | 186.37 | 33% | 2.8 | 6 | 7 | 5 | 0 | 3 | 0 | 6 | 7 | 3 | 4 | 5 | 46 | flow, insider, delivery |
| 59 | PYPL | no_runway | 52.60 | 8% | 0.3 | 10 | 4 | 4 | 2 | 7 | 6 | 1 | 1 | 3 | 5 | 3 | 46 | upside |
| 60 | ALAB | no_runway | 360.51 | 8% | 0.2 | 14 | 6 | 4 | 2 | 7 | 6 | 1 | 1 | 3 | 1 | 1 | 46 | upside, insider |
| 61 | ARM | no_runway | 306.34 | -6% | -0.2 | 14 | 5 | 3 | 2 | 7 | 6 | 0 | 0 | 3 | 3 | 3 | 46 | upside |
| 62 | SE | no_runway | 100.73 | 56% | 2.4 | 3 | 5 | 3 | 0 | 7 | 3 | 10 | 7 | 0 | 3 | 2 | 43 | insider, delivery |
| 63 | ABCL | no_runway | 12.65 | 35% | 1.2 | 3 | 3 | 3 | 3 | 7 | 6 | 8 | 1 | 5 | 1 | 3 | 43 | delivery |
| 64 | GS | no_runway | 923.29 | 24% | 1.2 | 6 | 5 | 5 | 0 | 7 | 9 | 6 | 1 | 0 | 3 | 1 | 43 | none |
| 65 | AMKR | no_runway | 52.69 | 45% | 1.0 | 3 | 3 | 2 | 2 | 7 | 6 | 8 | 1 | 2 | 3 | 2 | 39 | delivery |
| 66 | ADUR | no_runway | 12.56 | 115% | 4.1 | 3 | 1 | 2 | 0 | 7 | 3 | 10 | 10 | 0 | 0 | 1 | 37 | insider, delivery |
| 67 | META | no_runway | 777.59 | -2% | -0.1 | 3 | 7 | 6 | 2 | 7 | 0 | 0 | 0 | 3 | 4 | 5 | 37 | upside, insider, delivery |
| 68 | AAOI | no_runway | 101.03 | 62% | 0.8 | 3 | 3 | 2 | 2 | 7 | 6 | 10 | 1 | 0 | 1 | 1 | 36 | delivery |
| 69 | CRWV | no_runway | 90.13 | 56% | 1.7 | 3 | 4 | 2 | 0 | 7 | 3 | 10 | 4 | 2 | 0 | 1 | 36 | insider, delivery |
| 70 | NKE | no_runway | 35.99 | 31% | 0.9 | 3 | 2 | 2 | 2 | 7 | 6 | 6 | 1 | 0 | 3 | 1 | 33 | delivery |
| 71 | AI | no_runway | 10.76 | -23% | -0.8 | 10 | 2 | 1 | 0 | 3 | 9 | 0 | 0 | 3 | 1 | 2 | 31 | upside |
| 72 | ASTS | no_runway | 61.06 | 30% | 1.4 | 3 | 2 | 2 | 4 | 3 | 6 | 6 | 1 | 2 | 0 | 1 | 30 | delivery |
| 73 | NBIS | no_runway | 243.48 | 13% | 0.4 | 3 | 4 | 3 | 2 | 7 | 3 | 3 | 1 | 3 | 0 | 1 | 30 | upside, delivery |
| 74 | PSNL | no_runway | 16.57 | -7% | -0.3 | 6 | 1 | 3 | 2 | 7 | 3 | 0 | 0 | 3 | 2 | 2 | 29 | upside |

Why, per mechanical signal:

- **NXPI** earnings: beat both, guide raised, revisions up; insider: no buys; sells $226,040 (all 10b5-1); institutional: net adds or holders up 674 vs down 504; retail: quiet with fundamentals: 4 posts, 3 accounts; chart: below the 200 (-6.2%) in a base
- **CSCO** earnings: beat both, guide raised, revisions up; insider: no buys; sells $6,028,616 (all 10b5-1); institutional: net adds or holders up 2433 vs down 1923; retail: quiet with fundamentals: 3 posts, 3 accounts; chart: above the 200 (+10.5%) or breaking out; RS 3m -15.58
- **UNH** earnings: beat both, guide raised, revisions up; insider: no buys; sells $660,910 (some outside a plan); institutional: net adds or holders up 2311 vs down 1897; retail: loud: 41 posts across 2 accounts; chart: above the 200 (+5.6%) or breaking out; RS 3m -18.9
- **KURA** earnings: mixed print; insider: 2 buys incl. officer; $2,351,000; institutional: net adds or holders up 120 vs down 58; retail: moderate: 14 posts, 2 accounts; chart: above the 200 (+10.7%) or breaking out; RS 3m -4.32
- **GRAB** earnings: beat both, guide raised, revisions up; cash conversion below 70% caps at 6; insider: 2 buys, $30,743,149; institutional: net adds or holders up 310 vs down 167; retail: moderate: 13 posts, 2 accounts; chart: below both (-8.7% / -20.2%), structure trend_down
- **AMBA** earnings: beat, guide held or raised, revisions not down; insider: no buys; sells $2,963,921 (some outside a plan); institutional: net adds or holders up 182 vs down 123; retail: quiet with fundamentals: 4 posts, 3 accounts; chart: above the 200 (+2.2%) or breaking out; RS 3m 3.4800000000000004
- **AVGO** earnings: beat, guide held or raised, revisions not down; insider: no buys; sells $20,840,209 (plan status unverified); institutional: net adds or holders up 3483 vs down 2447; retail: loud: 64 posts across 6 accounts; chart: below both (-7.1% / -5.0%), structure trend_down
- **STIM** earnings: mixed print; insider: small buys $106,540; institutional: net adds or holders up 45 vs down 8; retail: quiet with fundamentals: 11 posts, 2 accounts; chart: above both averages, RS 3m 112.89999999999999
- **DAL** earnings: beat, guide held or raised, revisions not down; insider: clustered or CEO selling $33,081,037, no buys; institutional: net adds or holders up 782 vs down 463; retail: quiet with fundamentals: 3 posts, 3 accounts; chart: above the 200 (+9.8%) or breaking out; RS 3m -1.8499999999999996
- **RARE** earnings: mixed print; insider: no buys; sells $339,679 (plan status unverified); institutional: net adds or holders up 183 vs down 84; retail: quiet with fundamentals: 1 posts, 1 accounts; chart: below both (-35.3% / -40.3%), structure breakdown
- **APLD** earnings: mixed print; insider: no buys; sells $2,336,250 (plan status unverified); institutional: net adds or holders up 310 vs down 117; retail: moderate: 17 posts, 4 accounts; chart: below both (-2.0% / -16.1%), structure trend_down
- **GRRR** earnings: mixed print; insider: verified no qualifying insider activity; neutral, not positive conviction; institutional: net adds or holders up 26 vs down 8; retail: loud: 32 posts across 1 accounts; chart: above the 200 (+4.8%) or breaking out; RS 3m -20.52
- **ORCL** earnings: beat, guide held or raised, revisions not down; cash conversion below 70% caps at 6; insider: no buys; sells $5,342,124 (plan status unverified); institutional: net adds or holders up 2629 vs down 2104; retail: loud: 39 posts across 7 accounts; chart: below both (-1.7% / -15.4%), structure trend_down
- **WYFI** earnings: mixed print; insider: verified no qualifying insider activity; neutral, not positive conviction; institutional: net adds or holders up 70 vs down 6; short interest 50.49% of float; retail: loud after a -57% drawdown: capitulation watch; chart: below both (-9.6% / -5.9%), structure trend_down
- **TXN** earnings: beat both, guide raised, revisions up; insider: no buys; sells $1,852,413 (plan status unverified); institutional: net adds or holders up 1595 vs down 1200; retail: quiet with fundamentals: 4 posts, 3 accounts; chart: above the 200 (+10.1%) or breaking out; RS 3m -18.689999999999998
- **UBER** earnings: mixed print; insider: 2 buys, $15,314,016; institutional: net adds or holders up 1847 vs down 1063; retail: moderate: 10 posts, 5 accounts; chart: below both (-5.7% / -8.0%), structure trend_down
- **ASML** earnings: beat both, guide raised, revisions up; insider: insider coverage unverified; no conviction credit; institutional: net adds or holders up 1496 vs down 909; retail: moderate: 23 posts, 7 accounts; chart: above the 200 (+13.2%) or breaking out; RS 3m -11.940000000000001
- **WDC** earnings: beat both, guide raised, revisions up; cash conversion below 70% caps at 6; insider: clustered or CEO selling $15,777,915, no buys; institutional: net adds or holders up 1009 vs down 424; retail: quiet with fundamentals: 9 posts, 5 accounts; chart: above the 200 (+14.9%) or breaking out; RS 3m -38.82
- **AMAT** earnings: beat both, guide raised, revisions up; cash conversion below 70% caps at 6; insider: no buys; sells $59,609,696 (plan status unverified); institutional: net adds or holders up 1918 vs down 1408; retail: quiet with fundamentals: 9 posts, 4 accounts; chart: above the 200 (+12.8%) or breaking out; RS 3m -34.49
- **NVDA** earnings: beat both, guide raised, revisions up; cash conversion below 70% caps at 6; insider: no buys; sells $967,599,312 (plan status unverified); institutional: net adds or holders up 4283 vs down 3487; retail: loudest: 259 posts, 10 accounts, 3 high-conviction longs, near high; chart: above both averages, RS 3m 9.24
- **LRCX** earnings: beat both, guide raised, revisions up; cash conversion below 70% caps at 6; insider: no buys; sells $58,329,210 (plan status unverified); institutional: net adds or holders up 1842 vs down 1199; retail: quiet with fundamentals: 11 posts, 4 accounts; chart: above the 200 (+13.7%) or breaking out; RS 3m -29.049999999999997
- **NU** earnings: mixed print; cash conversion below 70% caps at 6; insider: insider coverage unverified; no conviction credit; institutional: net adds or holders up 594 vs down 302; retail: quiet with fundamentals: 5 posts, 3 accounts; chart: below the 200 (-8.5%) in a base
- **AMZN** earnings: beat, guide held or raised, revisions not down; cash conversion below 70% caps at 6; insider: no buys; sells $365,022,212 (all 10b5-1); institutional: net adds or holders up 4634 vs down 3077; retail: loud: 76 posts across 9 accounts; chart: above the 200 (+3.6%) or breaking out; RS 3m 12.52
- **VST** earnings: miss, guide cut, or revisions down; insider: small buys $1,173,069; institutional: net +3,094,073 sh, new 235 vs exited 135, named adds; retail: moderate: 9 posts, 4 accounts; chart: below both (-5.5% / -11.4%), structure trend_down
- **BABA** earnings: miss, guide cut, or revisions down; cash conversion below 70% caps at 6; insider: 3 buys, $25,691,200; institutional: net adds or holders up 853 vs down 545; retail: loud after a -43% drawdown: capitulation watch; chart: below both (-6.2% / -16.4%), structure trend_down
- **RDDT** earnings: beat, guide held or raised, revisions not down; insider: no buys; sells $50,058,820 (some outside a plan); institutional: net adds or holders up 647 vs down 277; retail: quiet with fundamentals: 7 posts, 3 accounts; chart: below both (-4.7% / -10.7%), structure trend_down
- **SPCX** earnings: mixed print; insider: no buys; sells $52,546,493 (all 10b5-1); institutional: net adds or holders up 144 vs down 0; retail: loud: 82 posts across 6 accounts; chart: above the 200 (+3.5%) or breaking out; RS 3m 5.050000000000001
- **GLW** earnings: beat, guide held or raised, revisions not down; insider: no buys; sells $3,485,642 (some outside a plan); institutional: net adds or holders up 1446 vs down 903; retail: quiet with fundamentals: 10 posts, 3 accounts; chart: above the 200 (+3.8%) or breaking out; RS 3m -37.88
- **UUUU** earnings: miss, guide cut, or revisions down; insider: 2 buys, $1,018,700; institutional: net +18,866,054 sh, new 65 vs exited 48, named adds; retail: moderate: 3 posts, 3 accounts; chart: below both (-14.5% / -34.4%), structure breakdown
- **CRDO** earnings: beat, guide held or raised, revisions not down; insider: clustered or CEO selling $101,508,977, no buys; institutional: net adds or holders up 582 vs down 277; retail: loud: 68 posts across 5 accounts; chart: above the 200 (+11.3%) or breaking out; RS 3m -32.38
- **OSCR** earnings: beat both, guide raised, revisions up; insider: clustered or CEO selling $25,707,525, no buys; institutional: net adds or holders up 204 vs down 94; retail: loud: 89 posts across 1 accounts; chart: above the 200 (+34.2%) or breaking out; RS 3m -8.450000000000001
- **ACHR** earnings: mixed print; insider: no buys; sells $1,690,731 (plan status unverified); institutional: net +14,982,467 sh, new 82 vs exited 79, named adds; retail: moderate: 3 posts, 3 accounts; chart: below the 200 (-9.4%) in a base
- **IREN** earnings: miss, guide cut, or revisions down; insider: verified no qualifying insider activity; neutral, not positive conviction; institutional: net adds or holders up 319 vs down 90; retail: loud: 71 posts across 6 accounts; chart: above the 200 (+1.2%) or breaking out; RS 3m -8.82
- **AKAM** earnings: miss, guide cut, or revisions down; insider: no buys; sells $720,440 (all 10b5-1); institutional: net adds or holders up 392 vs down 247; retail: moderate: 4 posts, 2 accounts; chart: below the 200 (-0.5%) in a base
- **RKLB** earnings: mixed print; insider: clustered or CEO selling $303,448,138, no buys; institutional: net +32,527,328 sh, new 329 vs exited 79, named adds; retail: loud: 45 posts across 7 accounts; chart: below the 200 (-9.1%) in a base
- **PLPC** earnings: mixed print; insider: clustered or CEO selling $3,009,746, no buys; institutional: net adds or holders up 91 vs down 37; retail: quiet with fundamentals: 0 posts, 0 accounts; chart: above both averages, RS 3m 14.43
- **WULF** earnings: miss, guide cut, or revisions down; insider: small buys $189,916; institutional: net adds or holders up 289 vs down 103; short interest 34.67% of float; retail: moderate: 12 posts, 2 accounts; chart: below both (-3.6% / -9.8%), structure trend_down
- **EOSE** earnings: miss, guide cut, or revisions down; insider: small buys $58,700; institutional: net +28,038,849 sh, new 79 vs exited 45, named adds; short interest 33.65% of float; retail: moderate: 11 posts, 2 accounts; chart: below both (-14.3% / -58.0%), structure trend_down
- **APP** earnings: miss, guide cut, or revisions down; insider: no buys; sells $1,603,489 (all 10b5-1); institutional: net adds or holders up 1204 vs down 689; retail: moderate: 12 posts, 2 accounts; chart: below both (-9.7% / -33.3%), structure trend_down
- **ONDS** earnings: miss, guide cut, or revisions down; cash conversion below 70% caps at 6; insider: no buys; sells $67,177 (all 10b5-1); institutional: net adds or holders up 214 vs down 41; short interest 42.19% of float; retail: moderate: 23 posts, 3 accounts; chart: below both (-4.8% / -19.8%), structure trend_down
- **CIFR** earnings: miss, guide cut, or revisions down; insider: no buys; sells $4,935,375 (plan status unverified); institutional: net adds or holders up 260 vs down 82; retail: moderate: 23 posts, 3 accounts; chart: below the 200 (-1.5%) in a base
- **SOFI** earnings: beat, guide held or raised, revisions not down; cash conversion below 70% caps at 6; insider: no buys; sells $890,704 (all 10b5-1); institutional: net adds or holders up 668 vs down 282; retail: loud: 29 posts across 3 accounts; chart: below both (-4.5% / -12.8%), structure trend_down
- **CAT** earnings: beat both, guide raised, revisions up; insider: no buys; sells $26,211,761 (some outside a plan); institutional: net adds or holders up 2540 vs down 1817; retail: quiet with fundamentals: 4 posts, 4 accounts; chart: above the 200 (+2.1%) or breaking out; RS 3m -15.52
- **ANET** earnings: beat both, guide raised, revisions up; insider: clustered or CEO selling $857,795,311, no buys; institutional: net adds or holders up 1474 vs down 939; retail: quiet with fundamentals: 6 posts, 3 accounts; chart: above both averages, RS 3m 18.839999999999996
- **VIAV** earnings: beat both, guide raised, revisions up; insider: clustered or CEO selling $8,405,393, no buys; institutional: net adds or holders up 259 vs down 127; retail: quiet with fundamentals: 3 posts, 3 accounts; chart: above the 200 (+3.2%) or breaking out; RS 3m -31.68
- **GEV** earnings: beat, guide held or raised, revisions not down; insider: verified no qualifying insider activity; neutral, not positive conviction; institutional: net +6,931,187 sh, new 500 vs exited 134, named adds; retail: moderate: 13 posts, 4 accounts; chart: above the 200 (+5.1%) or breaking out; RS 3m -3.719999999999999
- **LITE** earnings: beat both, guide raised, revisions up; insider: clustered or CEO selling $63,123,980, no buys; institutional: net adds or holders up 670 vs down 290; retail: loud: 26 posts across 4 accounts; chart: above both averages, RS 3m 2.29
- **ON** earnings: beat both, guide raised, revisions up; insider: verified no qualifying insider activity; neutral, not positive conviction; institutional: net adds or holders up 399 vs down 306; retail: quiet with fundamentals: 9 posts, 3 accounts; chart: below both (-6.2% / -8.3%), structure trend_down
- **SNDK** earnings: beat both, guide raised, revisions up; insider: no buys; sells $121,370,866 (all 10b5-1); institutional: net adds or holders up 897 vs down 196; retail: loud: 121 posts across 7 accounts; chart: above the 200 (+59.4%) or breaking out; RS 3m -30.39
- **SNOW** earnings: beat both, guide raised, revisions up; insider: clustered or CEO selling $555,829,747, no buys; institutional: net adds or holders up 889 vs down 503; retail: moderate: 14 posts, 3 accounts; chart: above both averages, RS 3m 41.61
- **STLN** earnings: mixed print; insider: small buys $261,090; institutional: net adds or holders up 74 vs down 22; retail: moderate: 16 posts, 1 accounts; chart: above both averages, RS 3m 18.0
- **ISRG** earnings: beat, guide held or raised, revisions not down; insider: no buys; sells $4,980,791 (all 10b5-1); institutional: net adds or holders up 1616 vs down 1003; retail: quiet with fundamentals: 4 posts, 3 accounts; chart: below the 200 (-11.6%) in a base
- **GOOGL** earnings: mixed print; cash conversion below 70% caps at 6; insider: no buys; sells $3,540,328 (all 10b5-1); institutional: net adds or holders up 3756 vs down 3288; retail: loud: 90 posts across 5 accounts; chart: above the 200 (+1.3%) or breaking out; RS 3m -8.36
- **CRM** earnings: mixed print; insider: small buys $999,451; institutional: net adds or holders up 2003 vs down 1565; retail: moderate: 23 posts, 4 accounts; chart: above both averages, RS 3m 53.12
- **COHR** earnings: beat both, guide raised, revisions up; cash conversion below 70% caps at 6; insider: clustered or CEO selling $8,491,314, no buys; institutional: net adds or holders up 709 vs down 359; retail: quiet with fundamentals: 6 posts, 3 accounts; chart: above the 200 (+1.8%) or breaking out; RS 3m -34.13
- **CCJ** earnings: miss, guide cut, or revisions down; insider: insider coverage unverified; no conviction credit; institutional: net +5,122,203 sh, new 127 vs exited 100, named adds; retail: moderate: 3 posts, 3 accounts; chart: below both (-7.0% / -16.7%), structure trend_down
- **MU** earnings: beat both, guide raised, revisions up; cash conversion below 70% caps at 6; insider: clustered or CEO selling $182,156,235, no buys; institutional: net adds or holders up 2462 vs down 1246; retail: loudest: 242 posts, 9 accounts, 3 high-conviction longs, near high; chart: above the 200 (+64.5%) or breaking out; RS 3m -16.450000000000003
- **SKHY** earnings: mixed print; cash conversion below 70% caps at 6; insider: insider coverage unverified; no conviction credit; institutional: not cleanly measurable; retail: loudest: 112 posts, 5 accounts, 3 high-conviction longs, near high; chart: above the 200 (+13.7%) or breaking out; RS 3m None
- **PYPL** earnings: beat, guide held or raised, revisions not down; insider: no buys; sells $848,121 (all 10b5-1); institutional: net adds or holders up 960 vs down 906; retail: moderate: 14 posts, 4 accounts; chart: above the 200 (+4.2%) or breaking out; RS 3m 22.1
- **ALAB** earnings: beat both, guide raised, revisions up; insider: no buys; sells $209,459,339 (plan status unverified); institutional: net adds or holders up 605 vs down 257; retail: moderate: 15 posts, 4 accounts; chart: above the 200 (+53.2%) or breaking out; RS 3m -14.91
- **ARM** earnings: beat both, guide raised, revisions up; insider: no buys; sells $5,775,432 (plan status unverified); institutional: net adds or holders up 427 vs down 225; retail: moderate: 13 posts, 5 accounts; chart: above the 200 (+45.2%) or breaking out; RS 3m -17.39
- **SE** earnings: miss, guide cut, or revisions down; insider: insider coverage unverified; no conviction credit; institutional: net adds or holders up 89 vs down 44; retail: loud: 43 posts across 2 accounts; chart: below both (-9.3% / -2.9%), structure trend_down
- **ABCL** earnings: miss, guide cut, or revisions down; insider: verified no qualifying insider activity; neutral, not positive conviction; institutional: net adds or holders up 77 vs down 29; retail: moderate: 3 posts, 3 accounts; chart: above both averages, RS 3m 80.78999999999999
- **GS** earnings: mixed print; cash conversion below 70% caps at 6; insider: clustered or CEO selling $1,092,676, no buys; institutional: net adds or holders up 2056 vs down 1370; retail: quiet with fundamentals: 4 posts, 3 accounts; chart: below both (-9.8% / -3.7%), structure breakdown
- **AMKR** earnings: miss, guide cut, or revisions down; cash conversion below 70% caps at 6; insider: no buys; sells $3,974,597 (plan status unverified); institutional: net adds or holders up 324 vs down 153; retail: moderate: 4 posts, 3 accounts; chart: below the 200 (-7.6%) in a base
- **ADUR** earnings: miss, guide cut, or revisions down; insider: insider coverage unverified; no conviction credit; institutional: net adds or holders up 15 vs down 1; retail: loud: 105 posts across 1 accounts; chart: below both (-11.1% / -4.5%), structure trend_down
- **META** earnings: miss, guide cut, or revisions down; cash conversion below 70% caps at 6; insider: no buys; sells $82,728,510 (some outside a plan); institutional: net adds or holders up 3968 vs down 2687; retail: loudest: 140 posts, 12 accounts, 3 high-conviction longs, near high; chart: above the 200 (+24.2%) or breaking out; RS 3m 35.27
- **AAOI** earnings: miss, guide cut, or revisions down; insider: no buys; sells $6,671,570 (some outside a plan); institutional: net adds or holders up 197 vs down 54; retail: moderate: 12 posts, 4 accounts; chart: below both (-9.5% / -5.3%), structure trend_down
- **CRWV** earnings: miss, guide cut, or revisions down; insider: insider coverage unverified; no conviction credit; institutional: net adds or holders up 667 vs down 150; retail: loud: 54 posts across 6 accounts; chart: below the 200 (-2.2%) in a base
- **NKE** earnings: miss, guide cut, or revisions down; insider: no buys; sells $771,333 (some outside a plan); institutional: net adds or holders up 1170 vs down 1011; retail: moderate: 20 posts, 2 accounts; chart: below both (-9.7% / -27.5%), structure trend_down
- **AI** earnings: beat, guide held or raised, revisions not down; insider: clustered or CEO selling $16,872,672, no buys; institutional: net adds or holders up 145 vs down 63; short interest 32.88% of float; retail: quiet with fundamentals: 0 posts, 0 accounts; chart: above the 200 (+3.5%) or breaking out; RS 3m 17.479999999999997
- **ASTS** earnings: miss, guide cut, or revisions down; insider: small buys $619,200; institutional: net +9,364,085 sh, new 180 vs exited 102, named adds; short interest 34.17% of float; retail: loud after a -54% drawdown: capitulation watch; chart: below the 200 (-25.2%) in a base
- **NBIS** earnings: miss, guide cut, or revisions down; cash conversion below 70% caps at 6; insider: no buys; sells $46,328,029 (plan status unverified); institutional: net adds or holders up 571 vs down 199; retail: loud: 163 posts across 7 accounts; chart: above the 200 (+49.0%) or breaking out; RS 3m -10.61
- **PSNL** earnings: mixed print; insider: no buys; sells $5,350,153 (plan status unverified); institutional: net adds or holders up 64 vs down 35; retail: loud: 33 posts across 1 accounts; chart: above the 200 (+60.6%) or breaking out; RS 3m 22.46

Forward quality (separate from the legacy total; unknown is not zero):

- **NXPI**: 3/3 covered checkpoints passed (6 possible); analyst_buy_pct=73.33; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=68.00; peg=0.76; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **CSCO**: 1/3 covered checkpoints passed (6 possible); analyst_buy_pct=67.86; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=0.00; peg=2.25; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **UNH**: 3/3 covered checkpoints passed (6 possible); analyst_buy_pct=85.19; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=16.00; peg=1.37; ev_fcf=n/f
  - fy1.ebit: missing, invalid, future-dated or older than 120 days
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **KURA**: 1/1 covered checkpoints passed (6 possible); analyst_buy_pct=93.33; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=n/f; peg=n/f; ev_fcf=n/f
  - fy1.ebit: missing, invalid, future-dated or older than 120 days
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - periods_aligned must confirm consecutive fiscal years, consistent currency/units/accounting
  - revisions.up_30d: missing, invalid, future-dated or older than 120 days
  - revisions.down_30d: missing, invalid, future-dated or older than 120 days
  - revisions.analysts: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **GRAB**: 2/3 covered checkpoints passed (6 possible); analyst_buy_pct=100.00; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=50.00; peg=3.11; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **AMBA**: 1/3 covered checkpoints passed (6 possible); analyst_buy_pct=42.86; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=66.67; peg=2.21; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **AVGO**: 3/3 covered checkpoints passed (6 possible); analyst_buy_pct=94.00; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=17.39; peg=0.45; ev_fcf=n/f
  - fy1.ebit: missing, invalid, future-dated or older than 120 days
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **STIM**: 1/1 covered checkpoints passed (6 possible); analyst_buy_pct=100.00; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=n/f; peg=n/f; ev_fcf=n/f
  - fy1.ebit: missing, invalid, future-dated or older than 120 days
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - periods_aligned must confirm consecutive fiscal years, consistent currency/units/accounting
  - revisions.up_30d: missing, invalid, future-dated or older than 120 days
  - revisions.down_30d: missing, invalid, future-dated or older than 120 days
  - revisions.analysts: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **DAL**: 2/3 covered checkpoints passed (6 possible); analyst_buy_pct=96.00; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=-16.67; peg=0.37; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **RARE**: 0/1 covered checkpoints passed (6 possible); analyst_buy_pct=55.00; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=n/f; peg=n/f; ev_fcf=n/f
  - fy1.ebit: missing, invalid, future-dated or older than 120 days
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - periods_aligned must confirm consecutive fiscal years, consistent currency/units/accounting
  - revisions.up_30d: missing, invalid, future-dated or older than 120 days
  - revisions.down_30d: missing, invalid, future-dated or older than 120 days
  - revisions.analysts: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **APLD**: 1/1 covered checkpoints passed (6 possible); analyst_buy_pct=85.71; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=n/f; peg=n/f; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - revisions.up_30d: missing, invalid, future-dated or older than 120 days
  - revisions.down_30d: missing, invalid, future-dated or older than 120 days
  - revisions.analysts: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **GRRR**: 1/1 covered checkpoints passed (6 possible); analyst_buy_pct=100.00; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=n/f; peg=n/f; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - revisions.up_30d: missing, invalid, future-dated or older than 120 days
  - revisions.down_30d: missing, invalid, future-dated or older than 120 days
  - revisions.analysts: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **ORCL**: 3/3 covered checkpoints passed (6 possible); analyst_buy_pct=81.40; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=10.81; peg=0.49; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **WYFI**: 1/2 covered checkpoints passed (6 possible); analyst_buy_pct=90.00; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=0.00; peg=n/f; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **TXN**: 2/3 covered checkpoints passed (6 possible); analyst_buy_pct=55.56; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=96.15; peg=1.70; ev_fcf=n/f
  - fy1.ebit: missing, invalid, future-dated or older than 120 days
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **UBER**: 3/3 covered checkpoints passed (6 possible); analyst_buy_pct=82.35; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=65.79; peg=0.66; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **ASML**: 3/3 covered checkpoints passed (6 possible); analyst_buy_pct=90.70; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=90.32; peg=1.13; ev_fcf=n/f
  - fy1.ebit: missing, invalid, future-dated or older than 120 days
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **WDC**: 2/3 covered checkpoints passed (6 possible); analyst_buy_pct=80.77; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=0.00; peg=0.39; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **AMAT**: 3/3 covered checkpoints passed (6 possible); analyst_buy_pct=84.62; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=93.33; peg=0.84; ev_fcf=n/f
  - fy1.ebit: missing, invalid, future-dated or older than 120 days
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **NVDA**: 3/3 covered checkpoints passed (6 possible); analyst_buy_pct=95.08; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=74.51; peg=0.35; ev_fcf=n/f
  - fy1.ebit: missing, invalid, future-dated or older than 120 days
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **LRCX**: 3/3 covered checkpoints passed (6 possible); analyst_buy_pct=82.86; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=6.67; peg=1.38; ev_fcf=n/f
  - fy1.ebit: missing, invalid, future-dated or older than 120 days
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **NU**: 3/3 covered checkpoints passed (6 possible); analyst_buy_pct=81.82; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=40.00; peg=0.57; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.enterprise_value: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **AMZN**: 2/2 covered checkpoints passed (6 possible); analyst_buy_pct=96.67; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=7.69; peg=n/f; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **VST**: 2/3 covered checkpoints passed (6 possible); analyst_buy_pct=95.00; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=-28.57; peg=0.79; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **BABA**: 1/2 covered checkpoints passed (6 possible); analyst_buy_pct=95.00; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=-20.00; peg=n/f; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - periods_aligned must confirm consecutive fiscal years, consistent currency/units/accounting
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **RDDT**: 2/3 covered checkpoints passed (6 possible); analyst_buy_pct=64.71; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=0.00; peg=0.76; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **SPCX**: 3/3 covered checkpoints passed (6 possible); analyst_buy_pct=80.56; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=26.67; peg=0.83; ev_fcf=n/f
  - fy1.ebit: missing, invalid, future-dated or older than 120 days
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **GLW**: 3/3 covered checkpoints passed (6 possible); analyst_buy_pct=76.47; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=66.67; peg=1.44; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **UUUU**: 1/2 covered checkpoints passed (6 possible); analyst_buy_pct=100.00; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=0.00; peg=n/f; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **CRDO**: 3/3 covered checkpoints passed (6 possible); analyst_buy_pct=94.74; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=63.16; peg=0.58; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **OSCR**: 2/3 covered checkpoints passed (6 possible); analyst_buy_pct=27.27; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=100.00; peg=1.11; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **ACHR**: 1/2 covered checkpoints passed (6 possible); analyst_buy_pct=66.67; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=0.00; peg=n/f; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **IREN**: 2/2 covered checkpoints passed (6 possible); analyst_buy_pct=82.35; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=25.00; peg=n/f; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **AKAM**: 2/3 covered checkpoints passed (6 possible); analyst_buy_pct=60.00; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=4.00; peg=2.12; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **RKLB**: 1/2 covered checkpoints passed (6 possible); analyst_buy_pct=80.00; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=0.00; peg=n/f; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **PLPC**: 0/1 covered checkpoints passed (6 possible); analyst_buy_pct=50.00; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=n/f; peg=n/f; ev_fcf=n/f
  - fy1.revenue: missing, invalid, future-dated or older than 120 days
  - fy1.ebit: missing, invalid, future-dated or older than 120 days
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.eps: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.revenue: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.eps: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - periods_aligned must confirm consecutive fiscal years, consistent currency/units/accounting
  - revisions.up_30d: missing, invalid, future-dated or older than 120 days
  - revisions.down_30d: missing, invalid, future-dated or older than 120 days
  - revisions.analysts: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **WULF**: 1/2 covered checkpoints passed (6 possible); analyst_buy_pct=100.00; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=-50.00; peg=n/f; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **EOSE**: 0/2 covered checkpoints passed (6 possible); analyst_buy_pct=36.36; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=-66.67; peg=n/f; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **APP**: 2/3 covered checkpoints passed (6 possible); analyst_buy_pct=81.82; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=0.00; peg=0.72; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **ONDS**: 1/2 covered checkpoints passed (6 possible); analyst_buy_pct=100.00; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=0.00; peg=n/f; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **CIFR**: 1/1 covered checkpoints passed (6 possible); analyst_buy_pct=100.00; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=n/f; peg=n/f; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - revisions.up_30d: missing, invalid, future-dated or older than 120 days
  - revisions.down_30d: missing, invalid, future-dated or older than 120 days
  - revisions.analysts: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **SOFI**: 1/3 covered checkpoints passed (6 possible); analyst_buy_pct=34.62; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=0.00; peg=0.76; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **CAT**: 2/3 covered checkpoints passed (6 possible); analyst_buy_pct=50.00; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=7.69; peg=1.55; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **ANET**: 3/3 covered checkpoints passed (6 possible); analyst_buy_pct=100.00; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=92.86; peg=1.90; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **VIAV**: 3/3 covered checkpoints passed (6 possible); analyst_buy_pct=87.50; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=87.50; peg=1.20; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **GEV**: 2/3 covered checkpoints passed (6 possible); analyst_buy_pct=81.08; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=-5.00; peg=0.96; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **LITE**: 3/3 covered checkpoints passed (6 possible); analyst_buy_pct=84.62; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=84.00; peg=0.72; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **ON**: 1/3 covered checkpoints passed (6 possible); analyst_buy_pct=44.83; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=0.00; peg=0.55; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **SNDK**: 3/3 covered checkpoints passed (6 possible); analyst_buy_pct=84.00; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=23.81; peg=0.35; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **SNOW**: 2/3 covered checkpoints passed (6 possible); analyst_buy_pct=86.00; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=66.67; peg=4.19; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **STLN**: 1/1 covered checkpoints passed (6 possible); analyst_buy_pct=100.00; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=n/f; peg=n/f; ev_fcf=n/f
  - fy1.ebit: missing, invalid, future-dated or older than 120 days
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.eps: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.eps: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - periods_aligned must confirm consecutive fiscal years, consistent currency/units/accounting
  - revisions.up_30d: missing, invalid, future-dated or older than 120 days
  - revisions.down_30d: missing, invalid, future-dated or older than 120 days
  - revisions.analysts: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **ISRG**: 1/3 covered checkpoints passed (6 possible); analyst_buy_pct=75.00; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=0.00; peg=3.05; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **GOOGL**: 2/2 covered checkpoints passed (6 possible); analyst_buy_pct=91.94; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=11.76; peg=n/f; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **CRM**: 1/1 covered checkpoints passed (6 possible); analyst_buy_pct=69.64; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=n/f; peg=n/f; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.revenue: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.eps: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - periods_aligned must confirm consecutive fiscal years, consistent currency/units/accounting
  - revisions.up_30d: missing, invalid, future-dated or older than 120 days
  - revisions.down_30d: missing, invalid, future-dated or older than 120 days
  - revisions.analysts: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **COHR**: 3/3 covered checkpoints passed (6 possible); analyst_buy_pct=78.26; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=81.82; peg=0.64; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **CCJ**: 1/2 covered checkpoints passed (6 possible); analyst_buy_pct=90.48; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=0.00; peg=n/f; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - periods_aligned must confirm consecutive fiscal years, consistent currency/units/accounting
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **MU**: 2/3 covered checkpoints passed (6 possible); analyst_buy_pct=91.84; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=0.00; peg=0.13; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **SKHY**: 3/3 covered checkpoints passed (6 possible); analyst_buy_pct=93.33; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=12.82; peg=0.16; ev_fcf=n/f
  - fy1.ebit: missing, invalid, future-dated or older than 120 days
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.enterprise_value: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **PYPL**: 2/3 covered checkpoints passed (6 possible); analyst_buy_pct=16.28; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=78.57; peg=1.31; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **ALAB**: 2/2 covered checkpoints passed (6 possible); analyst_buy_pct=73.08; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=n/f; peg=1.53; ev_fcf=n/f
  - fy1.ebit: missing, invalid, future-dated or older than 120 days
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - revisions.up_30d: missing, invalid, future-dated or older than 120 days
  - revisions.down_30d: missing, invalid, future-dated or older than 120 days
  - revisions.analysts: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **ARM**: 2/3 covered checkpoints passed (6 possible); analyst_buy_pct=65.12; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=58.97; peg=3.69; ev_fcf=n/f
  - fy1.ebit: missing, invalid, future-dated or older than 120 days
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **SE**: 2/3 covered checkpoints passed (6 possible); analyst_buy_pct=96.55; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=0.00; peg=0.74; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **ABCL**: 1/1 covered checkpoints passed (6 possible); analyst_buy_pct=100.00; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=n/f; peg=n/f; ev_fcf=n/f
  - fy1.ebit: missing, invalid, future-dated or older than 120 days
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - periods_aligned must confirm consecutive fiscal years, consistent currency/units/accounting
  - revisions.up_30d: missing, invalid, future-dated or older than 120 days
  - revisions.down_30d: missing, invalid, future-dated or older than 120 days
  - revisions.analysts: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **GS**: 0/3 covered checkpoints passed (6 possible); analyst_buy_pct=28.00; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=0.00; peg=2.79; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.enterprise_value: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **AMKR**: 2/3 covered checkpoints passed (6 possible); analyst_buy_pct=63.64; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=66.67; peg=2.20; ev_fcf=n/f
  - fy1.ebit: missing, invalid, future-dated or older than 120 days
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **ADUR**: 1/2 covered checkpoints passed (6 possible); analyst_buy_pct=100.00; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=-50.00; peg=n/f; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - periods_aligned must confirm consecutive fiscal years, consistent currency/units/accounting
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **META**: 1/3 covered checkpoints passed (6 possible); analyst_buy_pct=90.32; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=-17.65; peg=2.07; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **AAOI**: 1/3 covered checkpoints passed (6 possible); analyst_buy_pct=50.00; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=-33.33; peg=0.26; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **CRWV**: 2/2 covered checkpoints passed (6 possible); analyst_buy_pct=70.00; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=5.00; peg=n/f; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **NKE**: 1/3 covered checkpoints passed (6 possible); analyst_buy_pct=23.81; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=-11.43; peg=0.63; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **AI**: 1/2 covered checkpoints passed (6 possible); analyst_buy_pct=0.00; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=71.43; peg=n/f; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **ASTS**: 0/2 covered checkpoints passed (6 possible); analyst_buy_pct=35.71; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=-50.00; peg=n/f; ev_fcf=n/f
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **NBIS**: 1/2 covered checkpoints passed (6 possible); analyst_buy_pct=55.56; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=14.29; peg=n/f; ev_fcf=n/f
  - fy1.ebit: missing, invalid, future-dated or older than 120 days
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days
- **PSNL**: 0/1 covered checkpoints passed (6 possible); analyst_buy_pct=40.00; operating_margin_expansion_pp=n/f; fcf_margin_expansion_pp=n/f; fcf_growth_pct=n/f; forward_roic_pct=n/f; roic_wacc_spread_pp=n/f; eps_revision_breadth_pct=n/f; peg=n/f; ev_fcf=n/f
  - fy1.ebit: missing, invalid, future-dated or older than 120 days
  - fy1.cfo: missing, invalid, future-dated or older than 120 days
  - fy1.capex: missing, invalid, future-dated or older than 120 days
  - fy1.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy1.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - fy2.ebit: missing, invalid, future-dated or older than 120 days
  - fy2.cfo: missing, invalid, future-dated or older than 120 days
  - fy2.capex: missing, invalid, future-dated or older than 120 days
  - fy2.tax_rate_pct: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_begin: missing, invalid, future-dated or older than 120 days
  - fy2.invested_capital_end: missing, invalid, future-dated or older than 120 days
  - periods_aligned must confirm consecutive fiscal years, consistent currency/units/accounting
  - revisions.up_30d: missing, invalid, future-dated or older than 120 days
  - revisions.down_30d: missing, invalid, future-dated or older than 120 days
  - revisions.analysts: missing, invalid, future-dated or older than 120 days
  - valuation.wacc_pct: missing, invalid, future-dated or older than 120 days


## Verdicts after the red team

| Ticker | Mechanical tier | Final tier | Expected 6m | Bear | Size | Kill (by) |
|---|---|---|---:|---:|---|---|
| VST | one_leg_missing | one_leg_missing | +11.1% | -17% | watch | EBITDA guide cut below $6.8B, or no new PPA announced (2026-12-31) |
| NU | one_leg_missing | one_leg_missing | +9.9% | -19% | watch | 90-day NPL above 7.5% or ROE below 28% at the Q3 print (2026-11-20) |
| BABA | one_leg_missing | one_leg_missing | +9.8% | -23% | watch | operating income down more than 50% y/y again at the late-November print (2026-12-15) |
| CRDO | one_leg_missing | one_leg_missing | +9.7% | -18% | watch | FQ2 gross margin below 63% or revenue below $525M (2026-12-10) |
| WDC | one_leg_missing | one_leg_missing | +9.0% | -18% | watch | FQ1 revenue below $4.0B or gross margin below 50% on 29 Oct (2026-11-05) |
| GRAB | runway | one_leg_missing | +9.0% | -23% | watch | Q3 adjusted EBITDA implying below $720M for the year, or a close below the $2.74 52-week low (2026-12-31) |
| NVDA | one_leg_missing | one_leg_missing | +8.4% | -18% | core-starter | Q4 FY27 revenue guide below $118B at the November print, or FY28 EPS consensus below 15.0 on 15 Dec (2026-12-15) |
| UBER | one_leg_missing | one_leg_missing | +7.6% | -16% | watch | Q3 gross bookings below $58.25B on about 3 Nov, or a close below the $65.41 52-week low (2026-11-15) |
| UUUU | one_leg_missing | one_leg_missing | +6.9% | -29% | watch | Q3 revenue below $30M, or another equity raise (2026-12-31) |
| UNH | runway | runway | +6.9% | -8% | core-starter | the 13 Oct Q3 print holds or cuts the FY26 range below its $19.75 midpoint, or reports a medical care ratio above guidance (2026-10-20) |
| KURA | runway | one_leg_missing | +6.8% | -36% | watch | Q3 KOMZIFTI sales below $12M on about 3 Nov, or no KOMET-007/008 ASH abstract by 5 Nov (2026-11-05) |
| AMZN | one_leg_missing | one_leg_missing | +6.7% | -14% | watch | AWS growth below 30% in the Q3 print (2026-11-05) |
| LRCX | one_leg_missing | one_leg_missing | +6.6% | -17% | watch | December-quarter revenue guide below $7.7B on 21 Oct (2026-10-31) |
| ASML | one_leg_missing | one_leg_missing | +5.9% | -16% | watch | Q3 bookings below EUR 5B on 14 Oct, or 2027 revenue commentary below EUR 50B (2026-10-20) |
| AMAT | one_leg_missing | one_leg_missing | +5.6% | -18% | watch | FQ4 revenue guide below $9.8B, or China below 25% with total down q/q (2026-11-20) |
| TXN | one_leg_missing | no_runway | +4.9% | -11% | pass | Q4 revenue guide midpoint below $6.0B, or gross margin below 60%, at the 27 Oct print (2026-10-31) |
| NXPI | runway | one_leg_missing | +4.6% | -15% | watch | Q4 revenue guide below $3.7B at the Q3 print, or a close below $210 on 6 Nov (2026-11-06) |
| APP | one_leg_missing | one_leg_missing | +3.9% | -23% | watch | Q4 revenue guide below $2.1B on about 4 Nov (2026-11-15) |
| AVGO | runway | one_leg_missing | +3.8% | -16% | watch | FY27 EPS consensus below 19.0 on 9 Dec, or a Q1 FY27 guide below consensus (2026-12-15) |
| CSCO | runway | one_leg_missing | +3.4% | -11% | watch | FQ1 gross margin below 63.5% on about 11 Nov, or FY27 EPS consensus below 5.11 on 25 Nov (2026-11-25) |
| OSCR | one_leg_missing | one_leg_missing | +2.9% | -27% | watch | enhanced ACA subsidies not extended, or Q3 medical loss ratio above 82% (2026-12-31) |
| GLW | one_leg_missing | one_leg_missing | +2.8% | -16% | watch | Q4 core EPS guide below $0.85 on 27 Oct (2026-11-05) |
| SOFI | one_leg_missing | one_leg_missing | +2.7% | -29% | watch | FY adjusted net revenue guide below $4.75B (2026-11-05) |
| RDDT | one_leg_missing | one_leg_missing | +2.5% | -25% | watch | US logged-in DAU below 52M at the Q3 print (2026-11-05) |
| PLPC | one_leg_missing | one_leg_missing | +1.9% | -16% | watch | Q3 gross margin below 31% or revenue below $200M (2026-11-10) |
| AKAM | one_leg_missing | one_leg_missing | +1.8% | -18% | watch | FY EPS guide below $6.90 on about 5 Nov (2026-11-15) |
| APLD | runway | one_leg_missing | +1.3% | -30% | pass | FQ1 on about 8 Oct shows no new energised MW, or new secured notes above 9% before year end (2026-12-31) |
| SPCX | one_leg_missing | one_leg_missing | +0.8% | -29% | watch | price below the $135 IPO after the 24 Oct lock-up tranche (2026-11-15) |
| ORCL | runway | one_leg_missing | -1.1% | -25% | pass | any new bond, ATM or equity issuance, or a rating below BBB-, before the Q2 print (2026-12-15) |
| IREN | one_leg_missing | one_leg_missing | -1.8% | -39% | pass | FY27 EPS consensus below -4.00, or a new equity or convert raise above $1B (2026-12-31) |
| AMBA | runway | no_runway | -2.1% | -21% | pass | FQ3 guide midpoint below $119M on about 1 Dec (2026-12-05) |
| ACHR | one_leg_missing | one_leg_missing | -3.7% | -39% | pass | no piloted transition flight or UAE certificate (2027-03-31) |
| WULF | one_leg_missing | one_leg_missing | -4.2% | -45% | pass | any new equity or convert raise, or Q3 revenue below $50M (2026-12-31) |
| DAL | runway | no_runway | -4.4% | -15% | pass | Q3 on about 9 Oct cuts FY26 adjusted EPS below $6.50, or WTI above $95 that day (2026-10-09) |
| RARE | runway | no_runway | -4.5% | -32% | pass | FAYUVI first shipments not confirmed by 17 Oct, or no voucher sale by 24 Mar 2027 (2027-03-24) |
| RKLB | one_leg_missing | one_leg_missing | -4.6% | -35% | pass | Neutron first launch not on the pad by 31 Dec (2026-12-31) |
| CIFR | one_leg_missing | one_leg_missing | -5.0% | -39% | pass | Q3 gross margin below 0% (2026-11-15) |
| ONDS | one_leg_missing | one_leg_missing | -9.2% | -47% | pass | any new equity raise (2026-12-31) |
| EOSE | one_leg_missing | one_leg_missing | -11.9% | -54% | pass | Q3 gross margin below -50% (2026-11-15) |
| GRRR | runway | no_runway | -14.2% | -41% | pass | Q3 gross margin below 15%, or any 424B5 takedown before year end (2026-12-31) |
| STIM | runway | no_runway | -14.9% | -57% | pass | no covenant amendment by the Q3 print, or any equity offering filed (2027-03-24) |
| WYFI | runway | no_runway | -19.3% | -48% | pass | NC-1 financing close not announced by the Q3 print (2026-11-15) |

## Per ticker

### NXPI

Tier runway -> one_leg_missing; total 67; gates failed: none.

Research row: | NXPI | 230.16 / 339.95-183.00 / -32.3% | Buy / 30 | 311.10 | 400 / 190 | 35.2 | Bernstein Hold 290; UBS downgrade to Hold 305→270 (08-03); JPM Hold 300; Cantor Buy 400; GS Buy 325 | 07-28: rev 3.50B vs 3.47B, EPS 3.61 vs 3.52; raised (EPS 3.89-4.32 vs 3.92; rev 3.7-3.9B) | -7.0% / -10.8% | flat / up (15.06 / 15.06 / 14.76) | 2.81B vs 2.98B (0.94); 3.3% | Case: auto/industrial upcycle; 2030 goal to double non-GAAP EPS | TXN, ON; GM 56.3→54.6→56.2→57.3; P/E 12.7 vs 26.3 / 16.3 | none | 1 sale, $0.23M (COO, 10b5-1) | 674/504 (TTM); State Street +6.4% (11.7M sh); Amundi new 1.83M sh | 2.89%, 2.2d, 09-15 | -2.8% / -6.2%; yes; RS SPY +2.2/-27.4, XLK -4.7/-28.4; base; gap not held | 10-27 Q3 (estimate) | -7% on 07-29 on wide guide ranges and doubts over the 2030 targets; worst semis July in over a decade (Motley Fool) |

- Judgment (analyst call): prospect 5: auto upcycle in the raised Q3 guide; 2030 EPS doubling is a story; competition 5: GM 56.3 to 57.3% stable; fwd P/E 12.7 cheapest in analog; macro 5: quality megacap 4 plus 1: 12.7x forward earnings with 0.94x cash conversion suits the plateau; narrative 3: semis improving; auto outside the AI theme.
- Avg target: 311.1 · https://stockanalysis.com/stocks/nxpi/forecast/ · 2026-09-24
- Revenue actual: 3500000000.0 · https://www.marketbeat.com/stocks/NASDAQ/NXPI/earnings/ · 2026-09-24
- Guide: raised · https://www.marketbeat.com/stocks/NASDAQ/NXPI/earnings/ · 2026-07-28
- Revisions 90d: up · https://finance.yahoo.com/quote/NXPI/analysis/ · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=NXPI · 2026-09-24
- Holders up: 674 · https://www.marketbeat.com/stocks/NASDAQ/NXPI/institutional-ownership/ · 2026-09-24
- Verdict: edge Cash-flow shape at 15.3x FY26 earnings after a -10.8% post-print week; estimates are flat, not up. Pre-mortem: Auto demand rolled over under the oil shock and the wide guide range resolved low. Red team / strongest fact: FY26 EPS 15.06 now and 30 days ago: flat on the probe's own band; UBS cut to Hold $270 on 3 Aug.

### CSCO

Tier runway -> one_leg_missing; total 65; gates failed: none.

Research row: | CSCO | 106.97 / 130.37-66.81 / -18.0% | Buy / 28 | 137.25 | 170 / 115 | 28.3 | Piper Hold 132→125; DB init Buy 135; Truist 140; MS 135; Evercore 150 | 08-12: rev 17.25B vs 16.84B, EPS 1.22 vs 1.17; raised (FQ1 rev 18.0-18.2B vs 16.7B; EPS 1.32-1.34 vs 1.11) | -8.4% / -11.5% | flat / up (Zacks 5.11 / 5.11 / 4.78) | 12.8B vs 13.3B (0.96); 6.1% | Case: hyperscaler AI orders ($9.3B FY26); EPS 5.15 (+19%) | ANET, HPE; GM 65.5→65.0→63.6→64.1; P/E 19.3 vs 39.4 / 13.8 | none | 10 sales, $6.0M, all 10b5-1 (CEO Robbins $2.4M) | 2433/1923 (TTM); State Street +7.0% (207M sh) | 1.46%, 4.4d, 09-15 | -4.9% / +10.5%; yes; RS SPY -3.9/-14.6, XLK -10.9/-15.6; trend_down; gap not held | 10-02 ex-dividend; 11-11 FQ1 (estimate) | n/a |

- Judgment (analyst call): prospect 5: hyperscaler AI orders $9.3B FY26; FQ1 guide raised above consensus; competition 4: GM 65.5 to 64.1% drifting; fwd P/E 19.3 vs ANET 39.4; macro 5: cash-flow value shape: 0.96x conversion, dividend, 19x; narrative 3: outside the AI networking basket's direction; mixed.
- Avg target: 137.25 · https://stockanalysis.com/stocks/csco/forecast/ · 2026-09-24
- Revenue actual: 17250000000.0 · https://www.marketbeat.com/stocks/NASDAQ/CSCO/earnings/ · 2026-09-24
- Guide: raised · https://www.marketbeat.com/stocks/NASDAQ/CSCO/earnings/ · 2026-08-12
- Revisions 90d: up · https://www.zacks.com/stock/quote/CSCO/detailed-earning-estimates · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=CSCO · 2026-09-24
- Holders up: 2433 · https://www.marketbeat.com/stocks/NASDAQ/CSCO/institutional-ownership/ · 2026-09-24
- Verdict: edge Cash-flow value at 19x with a hyperscaler AI order book; the FQ1 guide is timing inside an in-line FY27. Pre-mortem: The AI mix diluted margin and the full year was already priced. Red team / strongest fact: The FY27 guide midpoint of $72.8B sits below the $73.16B consensus; 30-day revisions 0 up / 0 down.

### UNH

Tier runway; total 64; gates failed: none.

Research row: | UNH | 375.01 / 461.62-255.96 / -18.8% | Buy / 26 | 481.72 (MB 456.56) | 529 / 380 | 28.5 | Reiterations (Wells Fargo 526, Evercore 480, UBS 490, Barclays 441, Bernstein 512); Erste downgrade to Hold | 07-16: rev 112.03B vs 110.81B; EPS 6.38 vs 4.94; guide raised (FY 19.50-20.00) | +1.2%, +1.2% | up / up (18.39→19.87; 4 up/0 down) | 23.6B vs 14.1B (1.67) | Case: repricing restores margins, EPS +22% in 2026 and +14% in 2027 | ELV, HUM; GM n/m (insurer); fwd P/E 17.6 vs 14.7/30.6; EV/S 0.85 vs 0.53/0.37 | none | Optum CEO Conway $0.66M, no plan | 2311/1897 (TTM); Amundi -1.3M, Vulcan -93%; Envestnet +0.33M | 1.48%, 2.6d, 09-15; SI -14% | -5.4%/-9.8%; 50>200; RS -5.6/-14.2 vs SPY, -2.4/-18.9 vs XLV; trend_down; gap held at +5d, now -11% | Q3 10-13 (confirmed) | n/a |

- Judgment (analyst call): prospect 6: repricing in the beat and raise to $19.50-20.00; competition 5: fwd P/E 17.6 vs ELV 14.7; macro 5: defensive with FCF 1.67x NI: plateau-tolerant; narrative 3: managed care outside the themes.
- Avg target: 481.72 · https://stockanalysis.com/stocks/unh/forecast/ · 2026-09-24
- Revenue actual: 112030000000.0 · https://www.marketbeat.com/stocks/NYSE/UNH/earnings/ · 2026-09-24
- Guide: raised · https://www.businesswire.com/news/home/20260716830877/en/UnitedHealth-Group-Reports-Second-Quarter-2026-Results · 2026-07-16
- Revisions 90d: up · https://finance.yahoo.com/quote/UNH/analysis/ · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=UNH · 2026-09-24
- Holders up: 2311 · https://www.marketbeat.com/stocks/NYSE/UNH/institutional-ownership/ · 2026-09-24
- Verdict: edge Timing: 4 up / 0 down revisions, a beat and raise to $19.50-20.00, 17.6x forward earnings with FCF 1.67x net income, and the price 10% lower over 3 months. The edge is modest: the FY26 level moved only +0.3% in 30 days. Pre-mortem: Medical-cost trend re-accelerated and the midterms put Medicare Advantage rates back in play. Red team / strongest fact: Revisions up is FY26 EPS 19.81 to 19.87 (+0.3%); the Optum CEO sold $661k outside a plan in August.

### KURA

Tier runway -> one_leg_missing; total 63; gates failed: none.

Research row: | KURA | $10.86 (9/24) / 13.90-7.36 / -21.9% | Strong Buy / 15 | $32.00 | $76 / $15 | +194.7 | Lake St $23, Leerink $12, Barclays $28 (9/10); HCW $40 (9/9); Mizuho $25 (8/31), all Buy | 8/12: rev $20.9M vs $20.2M; EPS -0.77 vs -0.88; no financial guide (runway statement only) | +1.5%, +17.8% (CEO buy inside the window) | n/a (Yahoo error) | FCF TTM -$117M vs NI -$297M (Q4-25 had a $135M milestone); SBC 50%. **Cash $519M; burn about $75M/q; runway about 7q, or about 9.4q with $180M expected from Kyowa Kirin** | Case: KOMZIFTI sales ramp ($9.1M, +57% q/q) plus Q4-26 frontline combination data | SNDX (revumenib), J&J bleximenib; GM 97.6% TTM; EV/S 6.1 | CEO Wilson: 8/17 100k @ $11.12 ($1.11M); 8/24 100k @ $12.39 ($1.24M) | CLO Bair $398K (8/19); CCO Powl $52K (8/21); plan status unknown | TTM buyers 120 / sellers 58; add Corient +134%; exits Pale Fire -93%, Squarepoint -88% | 18.0% (Finviz 17.2%), DTC 8.8, 9/15 | -2.8% / +10.7%; 50>200 yes; RS 1m -20.3 / 3m +0.4 vs SPY; base; gap held | Q3 print about 11/3 (est.); KOMET-007/008 data guided 2H26 (likely ASH, early Dec, venue unconfirmed). **No offering in 2026** | n/a (-22%) |

- Judgment (analyst call): prospect 5: KOMZIFTI launch ramp +57% q/q is reported; the frontline combination data is ahead; competition 4: menin class against SNDX; GM 97.6%; macro 1: SMID biotech: long duration; narrative 2: SMID biotech fading.
- Avg target: 32.0 · https://stockanalysis.com/stocks/kura/forecast/ · 2026-09-24
- Revenue actual: 20.87 · https://www.marketbeat.com/stocks/NASDAQ/KURA/earnings/ · 2026-08-12
- Guide: none · https://www.biospace.com/press-releases/kura-oncology-reports-second-quarter-2026-financial-results · 2026-08-12
- Revisions 90d: None · None · None
- Insider coverage: True · https://finviz.com/quote.ashx?t=KURA · 2026-09-24
- Holders up: 120 · https://www.marketbeat.com/stocks/NASDAQ/KURA/institutional-ownership/ · 2026-09-24
- Verdict: edge Discounted signal: the CEO bought $2.35M on the open market in August; KOMZIFTI sales +57% q/q. Base case misses the satellite hurdle. Pre-mortem: The frontline update was Phase 1 noise against a first-to-market competitor, and burn outran the launch. Red team / strongest fact: The Q4 readout is a Phase 1 combination update at an unconfirmed ASH venue; burn about $75M a quarter against $9.1M of sales.

### GRAB

Tier runway -> one_leg_missing; total 60; gates failed: none.

Research row: | GRAB | 3.11 / 6.60–2.74 / -52.9% | Strong Buy / 25 (MB 11, $6.11) | $5.82 | $8.00 / $4.60 | +87.1 | 10 actions, all Buy. Targets trimmed after Atome: DBS 5.93 to 5.00, Maybank 6.25 to 5.40. KeyBanc $7 | 8/4: rev $997M vs $995M; EPS $0.06 vs $0.05. Raised FY rev to $4.10–4.15B and adj. EBITDA to $720–740M; $750M buyback | +1.4% / +1.9% | flat / up (0.13 / 0.13 / 0.09; 4 estimates) | FCF -$160M vs NI $598M (adj. FCF $450M); SBC 6.4% | Case: profitable SEA super-app, adj. EBITDA +54%, buybacks | UBER, DASH. GM 43.8/43.4/30.7/43.8. Fwd P/E 18.0 vs UBER 15.6, DASH 39.9 | CEO Tan $29.9M and COO $0.87M (9/21), code P, not 10b5-1 (ADR: coverage null) | 13 routine officer sales, $4.9M (CEO sold 400k shares twice) | 310 / 167. Adds: Uber $536M, Toyota, Norges. Sells: MS, UBS | 5.39%, 3.6d, 9/15 (Finviz 7.64%) | -8.7% / -20.2%; 50>200 no; RS SPY -13.3/-14.6, XLI -7.8/-1.8; trend_down; gap held | Q3 print about 11/3 (est.); Atome closing | Year-long derating; 3-year low after the $1.49B Atome (BNPL) deal on 9/15 |

- Judgment (analyst call): prospect 5: adj. EBITDA +54% and the FY guide raised; competition 4: fwd P/E 18.0 vs UBER 15.6; macro 3: EM archetype 3; narrative 2: outside the themes; the Atome deal clouds it.
- Avg target: 5.82 · https://stockanalysis.com/stocks/grab/forecast/ · 2026-09-24
- Revenue actual: 997000000.0 · https://www.marketbeat.com/stocks/NASDAQ/GRAB/earnings/ · 2026-09-24
- Guide: raised · https://www.investing.com/news/company-news/grab-q2-2026-slides-profit-surges-54-amid-fuel-crisis-guidance-raised-93CH-4832677 · 2026-09-24
- Revisions 90d: up · https://finance.yahoo.com/quote/GRAB/analysis/ · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=GRAB · 2026-09-24
- Holders up: 310 · https://www.marketbeat.com/stocks/NASDAQ/GRAB/institutional-ownership/ · 2026-09-24
- Verdict: edge Discounted signal: the CEO bought $29.9M on the open market after a 53% drawdown; FY guide raised. Base case misses the satellite hurdle. Pre-mortem: The Atome credit book and a strong dollar outweighed the CEO's buy. Red team / strongest fact: The CEO sold $3.0M in July and August before the buy, and the price kept falling after it.

### AMBA

Tier runway -> no_runway; total 59; gates failed: none.

Research row: | AMBA | 69.86 / 96.69-48.30 / -27.8% | Buy / 14 (8 Hold) | 89.36 | 120 / 65 | 27.9 | MS Buy 96; Northland 101; Oppenheimer Hold; Susquehanna 110; Rosenblatt 120 | 09-03: rev 108.13M vs 107.76M, EPS 0.18 vs 0.171; held (rev guide 115-124M vs 119.3M) | -0.8% / +1.0% | up / up (Zacks 0.80 / 0.77 / 0.78) | 9.7M vs -56.3M (n/m); **SBC 21.9%** | Case: edge-AI vision SoCs; EPS 0.80 to 1.12 | MBLY, QCOM; GM 59.6→58.4→58.4→57.7; P/E 66.0 vs 15.2 / 19.2 | none | 5 sales, $3.0M (CEO Wang $1.46M on 07-01 under 10b5-1); $0.9M of sell-to-cover on 09-17 excluded | 182/123 (TTM); Squarepoint -22%, Handelsbanken -66% | 13.54% (+30.8% on the month), 2.3d, 09-15 | -2.7% / +2.2%; no; RS SPY -1.5/+4.5, XLK -8.4/+3.5; base; gap held | 12-01 FQ3 (estimate) | n/a |

- Judgment (analyst call): prospect 4: edge-AI SoC growth guided; EPS 0.80 to 1.12 is consensus; competition 3: GM 59.6 to 57.7% falling; fwd P/E 66; macro 2: small cap and GAAP loss-making with SBC 22% of revenue: long duration; narrative 3: edge AI is outside the main themes.
- Avg target: 89.36 · https://stockanalysis.com/stocks/amba/forecast/ · 2026-09-24
- Revenue actual: 108130000.0 · https://www.marketbeat.com/stocks/NASDAQ/AMBA/earnings/ · 2026-09-24
- Guide: held · https://www.marketbeat.com/stocks/NASDAQ/AMBA/earnings/ · 2026-09-03
- Revisions 90d: up · https://www.zacks.com/stock/quote/AMBA/detailed-earning-estimates · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=AMBA · 2026-09-24
- Holders up: 182 · https://www.marketbeat.com/stocks/NASDAQ/AMBA/institutional-ownership/ · 2026-09-24
- Verdict: edge None stated: beta. Pre-mortem: No edge and a 66x multiple in a 2.76% real-yield regime. Red team / strongest fact: Base case +5.9% against a +20% hurdle; SBC 21.9% of revenue; short 13.5%.

### AVGO

Tier runway -> one_leg_missing; total 58; gates failed: none.

Research row: | AVGO | 350.36 / 495.00-289.96 / -29.2% | Strong Buy / 50 | 531.85 | 715 / 215.88 | +51.8 | Bernstein Buy 575; Mizuho Buy 530; Piper init Buy 460; DBS 390→470; Citi 500→515 | 09-02: $29.59B vs $29.24B, $3.32 vs $3.22; guide held (Q4 ~$34.8B vs $35.03B) | -2.7% / -1.4% | flat / flat (FY2 cut, 25 down / 11 up) | FCF $39.4B vs NI $38.3B (1.03x); SBC 9.5% | The case: AI revenue ~$115B FY27, ~$230B FY28 (CEO) | MRVL, NVDA; GM 76.6→74.2% (falling); fwd P/E 18.2 vs 38.3 / 14.3 | none | 4 sales, $20.8M (CLO Brazeal $19.5M) | MB 3,483 / 2,447 TTM; State Street +8.7%, AP4 +25.9% | 1.08% / 2.17d / n/f | -7.1% / -5.0%, yes; RS 1m -2.0 / -8.9, 3m -12.0 / -13.0; trend_down; gap not held (down gap) | Q4 ~12-09 (est.) | n/a (29.2% off the high) |

- Judgment (analyst call): prospect 5: AI revenue path of ~$115B FY27 is CEO guidance; Q4 guide sat just under consensus; competition 4: GM 76.6 to 74.2% diluting on AI mix; fwd P/E 18.2 mid-peer; macro 4: quality megacap archetype 4; narrative 3: semis improving, but FY2 estimates cut 25 down / 11 up and the chart is below both lines.
- Avg target: 531.85 · https://stockanalysis.com/stocks/avgo/forecast/ · 2026-09-24
- Revenue actual: 29.59 · https://www.marketbeat.com/stocks/NASDAQ/AVGO/earnings/ · 2026-09-02
- Guide: held · https://www.marketbeat.com/stocks/NASDAQ/AVGO/earnings/ · 2026-09-02
- Revisions 90d: flat · https://finance.yahoo.com/quote/AVGO/analysis/ · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=AVGO · 2026-09-24
- Holders up: 3483 · https://www.marketbeat.com/stocks/NASDAQ/AVGO/institutional-ownership/ · 2026-09-24
- Verdict: edge Quality after a 29% drawdown, but FY2 revisions are down (25 down / 11 up): a lagging label until they turn. Pre-mortem: Custom-silicon margin dilution met estimate cuts. Red team / strongest fact: FY27 EPS 19.57 to 19.38 in 30 days with 25 down / 11 up; the Q4 guide of $34.8B sat below $35.03B.

### STIM

Tier runway -> no_runway; total 54; gates failed: none.

Research row: | STIM | $2.82 / 3.44-0.80 / -18.0% | Strong Buy / 4 | $5.75 | $7 / $5 | +103.9 | BTIG Buy $6 (9/18); B. Riley init Buy $5 (9/11) | 8/11: rev $41.6M vs $40.2M; EPS -0.05 vs -0.12; FY rev narrowed to $160-164M (held); cash-use guide improved | +47%, +45% (held) | n/a | FCF TTM -$11.3M vs NI -$30.4M. **Cash $19.2M plus $5.8M restricted; burn about $5.5M/q in H1, guided lower in H2; $65M Perceptive loan; going-concern doubt** | Case: Greenbrook integration, GM 51%, adj. EBITDA positive; 10% owner Chernett buying | BWAY, Magnus (private); EV/S 1.8 | Chernett (10% owner): $44K (8/14), $62K (7/14) | none on Form 4 (former officer Macan filed a Form 144 for about $0.85M) | TTM 45/8; Madryn 18.5M sh, BlackRock 597k | 8.9% (Finviz 21.5%), DTC 3.7, 9/15 | +7.7% / +57%; 50>200; RS 1m -5.5 / 3m +117.6; trend_up; gap held | $2M minimum-liquidity covenant runs through 9/30; Q3 about 11/3 (est.); **3/31/27 minimum-revenue covenant test the company expects to miss** | n/a |

- Judgment (analyst call): prospect 3: adj. EBITDA positive but a going-concern flag; competition 2: GM 51%; macro 0: a covenant breach it expects on 31 Mar 2027; narrative 1: psychedelics and CNS lagging and worsening.
- Avg target: 5.75 · https://stockanalysis.com/stocks/stim/forecast/ · 2026-09-24
- Revenue actual: 41.57 · https://www.marketbeat.com/stocks/NASDAQ/STIM/earnings/ · 2026-08-11
- Guide: held · https://www.globenewswire.com/news-release/2026/08/11/3342616/0/en/neuronetics-reports-second-quarter-2026-financial-and-operating-results.html · 2026-08-11
- Revisions 90d: None · None · None
- Insider coverage: True · https://finviz.com/quote.ashx?t=STIM · 2026-09-24
- Holders up: 45 · https://www.marketbeat.com/stocks/NASDAQ/STIM/institutional-ownership/ · 2026-09-24
- Verdict: edge Outside-holder buying; a live going-concern doubt. Pre-mortem: The covenant forced a dilutive raise. Red team / strongest fact: The 10-Q projects TTM revenue below the Perceptive loan covenant on 31 Mar 2027.

### DAL

Tier runway -> no_runway; total 54; gates failed: none.

Research row: | DAL | 82.76 / 95.68-55.03 / -13.5% | Strong Buy / 25 | 103.44 (MB 100.62) | 125 / 50 | 25.0 | Cuts on fuel (Barclays 95, UBS 99, Raymond James 98, TD Cowen 105); UBS back to 105 and Redburn 105 in Sep; no rating changes | 07-10: rev 17.67B vs 17.43B; EPS 1.56 vs 1.49; guide held (FY 6.50-7.50 reinstated, Q3 2.00-2.50) | -1.8%, -5.4% | down / up (Zacks 6.42→6.23 over 30d; 5.58 90d ago) | 3.41B vs 3.95B (0.86); SBC n/a | Case: premium and loyalty revenue plus fuel normalisation give FY27 EPS +36% | UAL, AAL; GM 20.9→19.9→15.1→18.4; fwd P/E 10.7 vs 9.2/13.9; EV/S 1.02 vs 0.85/0.62 | none | about $33M, 08-03 to 08-05: CEO Bastian $19.2M, Carter $3.7M, Sear $3.8M, Bellemare $3.2M (all option exercise-and-sell), 2 directors; none under a 10b5-1 plan | 782/463 (TTM); Wellington -16.7%; Baird +45% | 4.01%, 4.1d, 09-15 | -1.6%/+9.8%; 50>200; RS -1.2/-14.6 vs SPY, +4.3/-1.9 vs XLI; base; gap not held | Q3 10-09 (estimate) | n/a |

- Judgment (analyst call): prospect 4: premium revenue in the last print; consensus below its own guide on fuel; competition 4: fwd P/E 10.7 vs UAL 9.2; macro 2: oil shock is the direct headwind for an airline; narrative 2: consumer and travel lagging.
- Avg target: 103.44 · https://stockanalysis.com/stocks/dal/forecast/ · 2026-09-24
- Revenue actual: 17670000000.0 · https://www.marketbeat.com/stocks/NYSE/DAL/earnings/ · 2026-09-24
- Guide: held · https://finance.yahoo.com/markets/stocks/article/delta-q2-earnings-top-estimates-reinstates-full-year-guidance-as-fuel-prices-bite-175815467.html · 2026-07-10
- Revisions 90d: up · https://www.zacks.com/stock/quote/DAL/detailed-earning-estimates · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=DAL · 2026-09-24
- Holders up: 782 · https://www.marketbeat.com/stocks/NYSE/DAL/institutional-ownership/ · 2026-09-24
- Verdict: edge None under an oil shock. Pre-mortem: Jet fuel stayed at records. Red team / strongest fact: FY26 consensus 6.42 to 6.23 in 30 days, below the $6.50 guided low; insiders sold about $33M in August.

### RARE

Tier runway -> no_runway; total 52; gates failed: none.

Research row: | RARE | $14.77 / 39.89-12.73 / -63.0% | Buy / 20 (11B/9H) | $28.05 | $40 / $18 | +89.9 | Evercore Hold $16→18, MS Hold $18→20 (9/21); Leerink Buy $33, Wedbush Hold $23, Canaccord Buy $37→39 (9/18) | 8/4: rev $214M vs $183M; EPS -0.90 vs -1.22; FY rev $730-760M **held** | -3.4%, +4.1% (gap reversed) | n/a | FCF TTM -$489M vs NI -$586M; SBC 19%. **Cash $436M; burn about $98M/q; runway about 4.4q before any sale of its two PRVs (est. $360-410M)** | Case: GENGLYCOS (8/19) and FAYUVI (9/17) approvals, 2027 opex down at least 15%, path to profit in 2027 | BMRN, SRPT; GM 78.5%; EV/S 3.3 | none | CFO Horn $118K (8/3) and $156K (7/1) (monthly pattern); CLO $47K; CAO $20K | TTM 183/84; add Corient +7%; exits Engineers Gate -46%, Squarepoint -24% | 17.7% (Finviz 18.4%), DTC 2.2, 9/15 | -35% / -40%; 50<200; RS 1m -44.4 / 3m -54.0; breakdown; gap not held | FAYUVI first shipments in 30-60 days (about 10/17-11/16); Q3 about 11/3 (est.); UX701 Wilson data Q4-26; possible PRV sale (undated) | Phase 3 Aspire (GTX-102, Angelman) missed primary and key secondary endpoints on 9/2; stock -44% on 9/3 |

- Judgment (analyst call): prospect 3: two approvals landed; the Angelman Phase 3 failed; competition 3: BMRN and SRPT; EV/S 3.3; macro 1: long duration with about 4.4 quarters of cash; narrative 1: SMID biotech fading.
- Avg target: 28.05 · https://stockanalysis.com/stocks/rare/forecast/ · 2026-09-24
- Revenue actual: 214.0 · https://www.marketbeat.com/stocks/NASDAQ/RARE/earnings/ · 2026-08-04
- Guide: held · https://www.sec.gov/Archives/edgar/data/0001515673/000119312526332802/rare-ex99_1.htm · 2026-08-04
- Revisions 90d: None · None · None
- Insider coverage: True · https://finviz.com/quote.ashx?t=RARE · 2026-09-24
- Holders up: 183 · https://www.marketbeat.com/stocks/NASDAQ/RARE/institutional-ownership/ · 2026-09-24
- Verdict: edge Two approvals and two vouchers; the flagship Phase 3 failed. Pre-mortem: Cash ran out before the vouchers were sold. Red team / strongest fact: Angelman Phase 3 missed on 2 Sep (-44%); 4.4 quarters of cash.

### APLD

Tier runway -> one_leg_missing; total 50; gates failed: none.

Research row: | APLD | 27.06 / 50.72-19.00 / -46.7% | Strong Buy / 14 | 66.18 (MB 60.88) | 109 / 22 | 144.6 | UBS init Buy 38; Redburn init Hold 22; MS Hold 38; B. Riley 75; Needham 83 | 7/27: rev $240.4M vs 96.9M, EPS -0.39 vs -0.09; no guidance | +0.9% / +18.5% | n/a (Yahoo error) | FCF -$2.78B vs NI -$0.25B; 36% | $36.2B take-or-pay leases (1,410MW) | CIFR, WULF; GM 15.7/42.5/33.9/13.4; EV/S 18.7 vs 47.5/64.2 | none | director Nottenburg $2.3M | 310 / 117 | 21.9%, 4.1d, 9/15 | -2.0% / -16.1%; 50<200; -6.4/-38.4; trend_down; gap held | FQ1 about 10/8 (est.) | Rotation out of AI infrastructure; Hold initiations at $22-38 |

- Judgment (analyst call): prospect 4: $36.2B take-or-pay leases contracted; delivery ahead; competition 3: GM volatile 13-43%; EV/S 18.7 below CIFR and WULF; macro 1: long duration with project debt at 7-9.25%; narrative 1: neoclouds lagging.
- Avg target: 66.18 · https://stockanalysis.com/stocks/apld/forecast/ · 2026-09-24
- Revenue actual: 240.35 · https://www.marketbeat.com/stocks/NASDAQ/APLD/earnings/ · 2026-07-27
- Guide: none · https://ir.applieddigital.com/news-events/press-releases/detail/159/applied-digital-reports-fiscal-fourth-quarter-and-full-year · 2026-07-27
- Revisions 90d: None · None · None
- Insider coverage: True · https://finviz.com/quote.ashx?t=APLD · 2026-09-24
- Holders up: 310 · https://www.marketbeat.com/stocks/NASDAQ/APLD/institutional-ownership/ · 2026-09-24
- Verdict: edge Contracted $36.2B of leases; the headline consensus is stale. Pre-mortem: Financing costs and tenant credit repriced in a 5% 10-year. Red team / strongest fact: The newest coverage is $22, $38 and $38 (average about $33) against the $66 consensus.

### GRRR

Tier runway -> no_runway; total 49; gates failed: none.

Research row: | GRRR | 14.36 / 23.49-9.04 / -38.9% | Strong Buy / 5 | 34.40 (MB 37.25) | 44 / 24 | 139.6 | Northland 40; B. Riley init 25; AGP 39; Compass Point init 44 | 8/24: Q2 rev $50.1M vs 38.7M, EPS -0.40 vs +0.03; guide raised (FY26 ≥$200M; FY27 $450-500M, below consensus) | -11.3% / -11.0% | n/a (Yahoo error) | FCF -$35M vs NI -$50M; 21% | Yotta and Supermicro AI programmes; 2027 revenue up to $0.58B | WYFI, NBIS; GM -4.2/21.1/29.7/37.3 (falling); fwd P/E 27.5; EV/S 2.1 | none (EDGAR: code J awards only) | none in window | 26 / 8 | 19.4%, 4.4d, 9/15 | +6.0% / +4.8%; 50<200; +2.1/-19.5; base; gap not held | Q3 about 11/16 (est.) | June shelf filing, widening losses, FY27 guide below consensus |

- Judgment (analyst call): prospect 2: Yotta and Supermicro programmes; FY27 guide below consensus; competition 2: GM volatile; share count +63% y/y; macro 1: long duration small cap with a shelf; narrative 2: outside any basket; AI infrastructure financing trade fading.
- Avg target: 34.4 · https://stockanalysis.com/stocks/grrr/forecast/ · 2026-09-24
- Revenue actual: 50.13 · https://www.marketbeat.com/stocks/NASDAQ/GRRR/earnings/ · 2026-08-24
- Guide: raised · https://investors.gorilla-technology.com/gorilla-technology-h1-revenue-surges-99-to-us78-4-million-raises-fy2026-revenue-outlook-to-at-least-us200-million/ · 2026-08-24
- Revisions 90d: None · None · None
- Insider coverage: True · https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001903145&type=4&dateb=&owner=include&count=40 · 2026-09-24
- Holders up: 26 · https://www.marketbeat.com/stocks/NASDAQ/GRRR/institutional-ownership/ · 2026-09-24
- Verdict: edge None: single-account story with dilution. Pre-mortem: Dilution against widening losses. Red team / strongest fact: Q2 gross margin -4.2%; shares +63% y/y; a resale prospectus filed 21 Aug.

### ORCL

Tier runway -> one_leg_missing; total 49; gates failed: none.

Research row: | ORCL | 139.54 (9/24) / 322.54-114.50 / -56.7% | Buy / 43 | 238.27 (MB 252.58) | 400 / 110 | 70.8 | Mizuho Buy 320; WFC Buy 280; MS Hold 210; Phillip cut to 225; Redburn Sell 110 | 9/10: rev $19.35B vs 19.13B, EPS 1.92 vs 1.74; guide held (FY27 rev ≥$90B, EPS $8.10; capex guide unchanged) | -1.7% / -3.5% | up / up (8.04→8.14) | FCF -$28.7B vs NI +$18.7B; SBC 6.7% | RPO $664B converts to OCI revenue; FY28 revenue $131B | MSFT, AMZN; GM 60.0/65.2/64.6/66.5 (falling); fwd P/E 12.7 (SA 16.4) vs 21.2/23.5; EV/S 7.7 | none | CEO Sicilia $4.9M; CAO $0.4M (Form 144s) | TTM buyers 2,629 / sellers 2,104; net n/a | 2.84%, 1.4d, 9/15 | -1.7% / -15.4%; 50<200; RS vs SPY -3.8/-12.9 (vs XLK -10.8/-14.0); trend_down; gap not held | ex-div 10/9 (confirmed); Q2 about 12/9 (est.) | Debt-funded AI capex, $20B ATM, record CDS, rising yields |

- Judgment (analyst call): prospect 5: RPO of $664B is contracted; conversion to OCI revenue is ahead; competition 4: GM 60.0 to 66.5% volatile; fwd P/E 12.7-16.4 below MSFT and AMZN; macro 1: neocloud archetype 1: $169B debt, FCF -$28.7B, $20B ATM at 2.76% real yields; the thesis needs the regime to change; narrative 1: neocloud and data centers lagging; the corpus macro account is short.
- Avg target: 238.27 · https://stockanalysis.com/stocks/orcl/forecast/ · 2026-09-24
- Revenue actual: 19350 · https://www.marketbeat.com/stocks/NYSE/ORCL/earnings/ · 2026-09-10
- Guide: held · https://www.sec.gov/Archives/edgar/data/0001341439/000119312526387905/orcl-ex99_1.htm · 2026-09-10
- Revisions 90d: up · https://finance.yahoo.com/quote/ORCL/analysis/ · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=ORCL · 2026-09-24
- Holders up: 2629 · https://www.marketbeat.com/stocks/NYSE/ORCL/institutional-ownership/ · 2026-09-24
- Verdict: edge RPO of $664B is contracted; the balance sheet needs the regime to change. Pre-mortem: Credit, not demand, set the price. Red team / strongest fact: FCF -$28.7B against $169B of debt; a $20B ATM ran in FQ1 and CDS sit at a record.

### WYFI

Tier runway -> no_runway; total 40; gates failed: none.

Research row: | WYFI | 20.26 / 46.87-10.51 / -56.8% | Strong Buy / 10 | 40.50 (MB 38.64) | 50 / 32 | 99.9 | HCW 37; Needham raised to 41; Cantor upgrade 36; Clear St 44; Barclays Hold 32 | 8/12: rev $28.8M vs ~18.6M, EPS -0.39 vs -0.40; no guidance | +18.0% / -11.7% | flat / up (FY27 cut 0.52→0.15) | FCF -$341M vs NI -$44M; 30% | NC-1 $865M/10y (Nscale); RPO $933M | NBIS, APLD; GM 84/85/152/66; EV/S 11.1 | none | none | 70 / 6; Tidal +116% | 50.5% (9.5M float), 1.9d, 9/15 | -9.6% / -5.9%; 50>200; -0.9/-49.5; trend_down; gap faded | Q3 about 11/12 (est.); NC-1 financing close | $310M convert and note exchange right after the print |

- Judgment (analyst call): prospect 2: NC-1 $865M lease contracted; financing not closed; competition 2: tiny float, 50% short, FY27 estimates cut 0.52 to 0.15; macro 0: long duration, fresh 5% converts; narrative 1: neoclouds lagging.
- Avg target: 40.5 · https://stockanalysis.com/stocks/wyfi/forecast/ · 2026-09-24
- Revenue actual: 28.84 · https://www.marketbeat.com/stocks/NASDAQ/WYFI/earnings/ · 2026-08-12
- Guide: none · https://finance.yahoo.com/news/whitefiber-inc-reports-second-quarter-110000364.html · 2026-08-12
- Revisions 90d: up · https://finance.yahoo.com/quote/WYFI/analysis/ · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=WYFI · 2026-09-24
- Holders up: 70 · https://www.marketbeat.com/stocks/NASDAQ/WYFI/institutional-ownership/ · 2026-09-24
- Verdict: edge None: a 9.5M-share float, 50% short. Pre-mortem: Financing failed to close. Red team / strongest fact: FY27 EPS cut 0.52 to 0.15 in 30 days; $56M cash against $321M debt.

### TXN

Tier one_leg_missing -> no_runway; total 64; gates failed: upside.

Research row: | TXN | 270.65 / 334.03-152.73 / -19.0% | Buy / 36 | 324.71 | 400 / 225 | +20.0 | Bernstein Hold 290; TD Cowen Buy 340; Cantor Hold; Citi Buy; Mizuho Hold 305 | 07-22: $5.46B vs $5.26B, $2.14 vs $1.91; guide raised (Q3 $5.7-6.2B vs $5.5B) | -3.1% / -5.2% | flat / up | FCF $5.36B vs NI $6.05B (0.88x); SBC 2.1% | The case: analog recovery; capex roll-off lifts FCF; GM back to 61% | NXPI, ON; GM 57.4→61.4%; fwd P/E 26.3 vs 12.7 / 16.3 | none | SVP Abraham $1.85M | MB 1,595 / 1,200 TTM | 2.17% / 2.65d / n/f | -0.2% / +10.1%, yes; RS 1m +3.9 / -3.1, 3m -17.7 / -18.7; base; gap not held | Q3 ~10-27 (est.) | n/a |

- Judgment (analyst call): prospect 6: analog recovery visible in the raised Q3 guide; capex roll-off lifts FCF; competition 5: GM 57.4 to 61.4% rising; fwd P/E 26.3 above NXPI 12.7 and ON 16.3; macro 5: quality megacap 4 plus 1: FCF 0.88x NI and a dividend fit a cash-flow regime; narrative 3: semis improving; analog outside the AI narrative.
- Avg target: 324.71 · https://stockanalysis.com/stocks/txn/forecast/ · 2026-09-24
- Revenue actual: 5.46 · https://www.marketbeat.com/stocks/NASDAQ/TXN/earnings/ · 2026-07-22
- Guide: raised · https://www.marketbeat.com/stocks/NASDAQ/TXN/earnings/ · 2026-07-22
- Revisions 90d: up · https://finance.yahoo.com/quote/TXN/analysis/ · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=TXN · 2026-09-24
- Holders up: 1595 · https://www.marketbeat.com/stocks/NASDAQ/TXN/institutional-ownership/ · 2026-09-24
- Verdict: edge Timing: analog recovery with 25 up / 0 down revisions and a gross margin back at 61%, priced at exactly the 20% upside line. Pre-mortem: The recovery was priced; 26x forward earnings de-rated under a 5% 10-year. Red team / strongest fact: Upside is 19.97% and the base case +5.3% sits below the 8% core hurdle at 26.3x against NXPI 12.7x.

### UBER

Tier one_leg_missing; total 63; gates failed: delivery.

Research row: | UBER | 69.22 (9/24) / 101.29–65.41 / -31.7% | Buy / 50 (MB 43, $103.03) | $101.24 | $150 / $70 | +46.3 | 24 actions. Mostly held at $90–119. Arete cut to Neutral ($74, 9/10). Scotiabank and Rosenblatt started coverage at Buy. Five target cuts on 8/6 | 8/5: rev $14.19B vs $14.24B (miss); EPS $0.81 vs $0.805. Quarterly guide only: Q3 GB $58.25–60.25B, EPS $0.84–0.88. Recorded as "held" | -5.3% / +4.7% (the down gap filled) | flat / up (Yahoo FY26 3.19 vs 3.23 30d vs 3.04 90d; 27 up, 2 down) | FCF $10.12B vs NI $9.58B; SBC 3.5% | Case: demand aggregator for rides and delivery. Bookings +18–22%, EPS about +30%, AV partners route through Uber | DASH, LYFT. GM 39.3/39.3/49.6/34.3. Fwd P/E 15.6 vs DASH 39.9, LYFT 14.5 | CEO Khosrowshahi $10.0M (9/10) and COO Macdonald $5.3M (9/4). Code P on EDGAR, not 10b5-1 | Hazelbaker (SVP) $2.0M, not 10b5-1 | TTM buyers 1,847 vs sellers 1,063. Adds: Norges, PIF, CRGI, Pershing. Sells: Jennison, Jump | 2.33%, 2.3d, 9/15 | -5.7% / -8.0%; 50>200 no; RS vs SPY -14.0/-8.7, vs XLI -8.5/+4.1; trend_down; gap filled | Q3 print about 11/3 (est.) | Robotaxi fear: Tesla Cybercab Austin 9/8 (UBER -4% that day); Waymo own app Jan 2028; print-day -5% |

- Judgment (analyst call): prospect 6: bookings +18-22% and EPS growth in the last prints; competition 5: GM ~39% stable; fwd P/E 15.6 vs DASH 39.9; the AV partner fear is a story; macro 5: cash-flow value shape: FCF $10.1B at 15.6x; narrative 3: internet platforms fading; robotaxi fear.
- Avg target: 101.24 · https://stockanalysis.com/stocks/uber/forecast/ · 2026-09-24
- Revenue actual: 14190000000.0 · https://www.marketbeat.com/stocks/NYSE/UBER/earnings/ · 2026-09-24
- Guide: held · https://investor.uber.com/news-events/news/press-release-details/2026/Uber-Announces-Results-for-Second-Quarter-2026/default.aspx · 2026-09-24
- Revisions 90d: up · https://finance.yahoo.com/quote/UBER/analysis/ · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=UBER · 2026-09-24
- Holders up: 1847 · https://www.marketbeat.com/stocks/NYSE/UBER/institutional-ownership/ · 2026-09-24
- Verdict: edge Discounted signal: the CEO bought $10.0M and the COO $5.3M on the open market in September after a 32% drawdown, while 30-day revisions run 27 up / 2 down. The delivery leg failed on a $50M revenue miss. Pre-mortem: Robotaxi disintermediation became a numbers story, not a fear story. Red team / strongest fact: An SVP sold $2.0M outside a plan the day after the CEO bought; Tesla Cybercab is live in Austin about 30% below Uber's prices.

### ASML

Tier one_leg_missing; total 63; gates failed: insider.

Research row: | ASML | 1722.50 / 1999.96-935.41 / -13.9% | Strong Buy / 42 | 2135 (MB 1970) | 2843 / 887.8 | +23.9 (MB +14.4) | BofA Buy (09-08); others before the window | 07-15: $10.64B vs $10.24B, $8.65 vs $7.98; guide raised (Q3 $12.8-14.0B vs $11.3B, USD-converted) | +2.2% / +1.5% | up / up | FCF €10.04B vs NI €10.64B (0.94x); SBC 0.6% | The case: EUV/High-NA; 2026 €42.9B, 2027 €54.6B | AMAT, LRCX; GM 51.6→54.0%; fwd P/E 28.4 vs 25.3 / 25.9 | coverage unknown (no Form 4) | coverage unknown | MB 1,496 / 909 TTM; inst own 26% | 0.40% / 0.94d / n/f | +0.2% / +13.2%, yes; RS 1m -1.4 / -8.4, 3m -10.9 / -11.9; base; gap held | Q3 10-14 BMO (est.) | n/a |

- Judgment (analyst call): prospect 6: EUV and High-NA demand in the raised Q3 guide; competition 7: EUV monopoly; GM 51.6 to 54.0% rising; fwd P/E 28.4 near peers; macro 4: quality megacap archetype 4; narrative 3: semis improving, semicap lagging; mixed.
- Avg target: 2135 · https://stockanalysis.com/stocks/asml/forecast/ · 2026-09-24
- Revenue actual: 10.64 · https://www.marketbeat.com/stocks/NASDAQ/ASML/earnings/ · 2026-07-15
- Guide: raised · https://www.marketbeat.com/stocks/NASDAQ/ASML/earnings/ · 2026-07-15
- Revisions 90d: up · https://finance.yahoo.com/quote/ASML/analysis/ · 2026-09-24
- Insider coverage: False · https://finviz.com/quote.ashx?t=ASML · 2026-09-24
- Holders up: 1496 · https://www.marketbeat.com/stocks/NASDAQ/ASML/institutional-ownership/ · 2026-09-24
- Verdict: edge Quality with guide raised and revisions 28 up / 0 down; the insider leg fails only because a foreign issuer files no Form 4. Pre-mortem: Semicap de-rated as memory capex paused after the pricing peak. Red team / strongest fact: not red-teamed: one-leg name; the probe's own strongest fact against: the semicap basket is lagging and worsening, -24pp vs SPY over 3 months.

### WDC

Tier one_leg_missing; total 62; gates failed: upside.

Research row: | WDC | 450.31 / 799.87-105.42 / -43.7% | Buy / 26 | 664.92 (MB 534.56) | 1050 / 420 | 47.7 (MB 18.7) | Citi 800→740 Buy; Evercore 575; Wedbush 530→650; BofA 720; GS Hold 650→615 | 08-05: rev 3.75B vs 3.70B, EPS 3.56 vs 3.31; raised (EPS 3.85-4.15 vs 3.63; rev 4.0-4.2B vs 3.9B) | -13.0% / -6.1% | flat / up (Zacks 20.03 / 20.03 / 18.32) | 3.5B vs 9.4B (0.37; GAAP net income includes non-operating gains); 1.6% | Case: AI nearline HDD exabytes with pricing discipline; FY27 revenue 19.2B (+49%) | STX, SNDK; GM 43.5→45.7→50.2→54.1; P/E 13.7 vs 15.9 / 6.7 | none | 12 sales, $15.8M; CEO Tan $8.9M (10b5-1); director Streeter $2.5M with no plan | 1009/424 (TTM); NPS trimmed 4% | 5.02%, 3.1d, 09-15 | -5.0% / +14.9%; yes; RS SPY -0.3/-37.8, XLK -7.2/-38.8; base; gap not held | 10-29 FQ1 (estimate) | Fell 13% on 08-06 despite a beat and an above-consensus guide, after about a 190% YTD run (Benzinga) |

- Judgment (analyst call): prospect 6: HDD exabyte growth and pricing in the beat and above-consensus guide; competition 5: duopoly with STX; GM 43.5 to 54.1% rising; macro 4: materials/industrials 4; narrative 4: memory and storage improving, but the stock fell 13% on the beat.
- Avg target: 664.92 · https://stockanalysis.com/stocks/wdc/forecast/ · 2026-09-24
- Revenue actual: 3750000000.0 · https://www.marketbeat.com/stocks/NASDAQ/WDC/earnings/ · 2026-09-24
- Guide: raised · https://www.marketbeat.com/stocks/NASDAQ/WDC/earnings/ · 2026-08-05
- Revisions 90d: up · https://www.zacks.com/stock/quote/WDC/detailed-earning-estimates · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=WDC · 2026-09-24
- Holders up: 1009 · https://www.marketbeat.com/stocks/NASDAQ/WDC/institutional-ownership/ · 2026-09-24
- Verdict: edge Estimates up after a beat-and-raise met with a -13% print day; the upside leg fails only on MarketBeat's lagging average. Pre-mortem: The storage cycle peaked with memory. Red team / strongest fact: not red-teamed: one-leg name; the probe's own strongest fact against: cash conversion 0.37x on GAAP gains.

### AMAT

Tier one_leg_missing; total 62; gates failed: insider.

Research row: | AMAT | 474.25 / 739.67-196.20 / -35.9% | Strong Buy / 39 | 640.89 | 900 / 358 | +35.1 | Bernstein Buy 700; GS Buy 670; UBS 675→695; Mizuho 650→590; JPM Buy | 08-13: $9.12B vs $8.99B, $3.50 vs $3.40; guide raised (Q4 $9.8-10.8B vs $9.5B) | -5.1% / -7.9% | flat / up | FCF $5.62B vs NI $9.27B (0.61x); SBC 2.3% | The case: WFE upcycle; FY27 revenue $46.1B (+35%) | LRCX, ASML; GM 48.0→50.3% rising; fwd P/E 25.3 vs 25.9 / 28.4 | none | 4 sales, $59.6M (CEO Dickerson $55.6M, 06-29/30) | MB 1,918 / 1,408 TTM; State Street +85% (looks anomalous) | 1.98% / 1.84d / n/f | -3.6% / +12.8%, yes; RS 1m -1.4 / -8.4, 3m -33.5 / -34.5; base; gap not held | Q4 ~11-12 (est.) | Sell-the-news after beat-and-raise: 178% 1y run, China share ~28% (from ~35%), semis pullback |

- Judgment (analyst call): prospect 6: WFE upcycle visible in the raised Q4 guide; FY27 revenue +35% is consensus; competition 5: GM 48.0 to 50.3% rising; fwd P/E 25.3 in line with LRCX and ASML; China share falling; macro 4: materials/industrials archetype 4; narrative 2: semicap basket lagging and worsening, -24pp vs SPY over 3m.
- Avg target: 640.89 · https://stockanalysis.com/stocks/amat/forecast/ · 2026-09-24
- Revenue actual: 9.12 · https://www.marketbeat.com/stocks/NASDAQ/AMAT/earnings/ · 2026-08-13
- Guide: raised · https://www.marketbeat.com/stocks/NASDAQ/AMAT/earnings/ · 2026-08-13
- Revisions 90d: up · https://query2.finance.yahoo.com/v10/finance/quoteSummary/AMAT?modules=earningsTrend · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=AMAT · 2026-09-24
- Holders up: 1918 · https://www.marketbeat.com/stocks/NASDAQ/AMAT/institutional-ownership/ · 2026-09-24
- Verdict: edge Estimates up (29 up / 1 down) after a sell-the-news print; the insider leg fails on the CEO's $55.6M sale. Pre-mortem: The CEO sold near the top for a reason: WFE digested in 2027. Red team / strongest fact: not red-teamed: one-leg name; the probe's own strongest fact against: CEO Dickerson sold $55.6M on 29-30 June.

### NVDA

Tier one_leg_missing; total 60; gates failed: insider.

Research row: | NVDA | 224.58 (09-24) / 236.54-164.27 / -5.1% | Strong Buy / 61 | 327.7 | 515 / 180 | +45.9 | Redburn Buy 325; Bernstein Buy 400; GS Buy 300; Piper init Buy 300; Needham Buy 300 | 08-26: $96.22B vs $92.27B, $2.22 vs $2.09; guide raised (Q3 $105.8-110.2B vs $103.5B) | +8.7% / +9.0% | up / up | FCF $127.0B vs NI $192.9B (0.66x); SBC 2.4% | The case: AI data-center compounding; FY28 revenue consensus $683B | AMD, AVGO; GM 73.4→75.0%; fwd P/E 14.3 vs AMD 39.6 / AVGO 18.2 | none | 9 sales, $968M, 3 sellers (director Stevens ~$947M; CFO Kress $7.6M; GC Teter $13.3M); 10b5-1 unverified | Q2-26; MB TTM 4,283 buyers / 3,487 sellers; State Street +1.6%, AP4 -15.6% | 1.29% / 2.34d / date n/f | +4.2% / +12.7%, yes; RS 1m +5.2 SPY / -1.7 XLK, 3m +10.3 / +9.2; trend_up; gap held | Q3 ~11-18 (est.) | n/a |

- Judgment (analyst call): prospect 7: the case is in the last two prints: Q2 beat and Q3 guide raised to $105.8-110.2B; FY28 revenue consensus $683B; competition 6: GM 73.4 to 75.0% rising with share held; fwd P/E 14.3 below AMD 39.6 and AVGO 18.2; macro 4: quality megacap archetype 4; self-funding, net cash; narrative 5: Mag 7 accelerating but semis only improving; loudest name in the corpus.
- Avg target: 327.7 · https://stockanalysis.com/stocks/nvda/forecast/ · 2026-09-24
- Revenue actual: 96.22 · https://www.marketbeat.com/stocks/NASDAQ/NVDA/earnings/ · 2026-08-26
- Guide: raised · https://www.marketbeat.com/stocks/NASDAQ/NVDA/earnings/ · 2026-08-26
- Revisions 90d: up · https://finance.yahoo.com/quote/NVDA/analysis/ · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=NVDA · 2026-09-24
- Holders up: 4283 · https://www.marketbeat.com/stocks/NASDAQ/NVDA/institutional-ownership/ · 2026-09-24
- Verdict: edge Earnings momentum at 14.3x forward: guide raised to $105.8-110.2B and revisions 39 up / 1 down. Insider leg fails on director Stevens' $947M sale. Pre-mortem: AI capex digested and the loudest name in the corpus had no marginal buyer. Red team / strongest fact: On FY27 EPS the multiple is 24x, not 14x; FCF is 0.66x net income; the corpus has 259 posts from 10 accounts on it.

### LRCX

Tier one_leg_missing; total 60; gates failed: insider.

Research row: | LRCX | 307.16 / 438.50-125.02 / -30.0% | Strong Buy / 35 | 373.13 | 500 / 290 | +21.5 | Bernstein 385; Mizuho 365; SIG 475; Berenberg 350→420; UBS 435→425 | 07-29: $6.72B vs $6.66B, $1.82 vs $1.69; guide raised (Q1 $7.7-8.5B vs $7.0B) | +18.0% / +21.2% | up / up | FCF $4.89B vs NI $7.27B (0.67x); SBC 1.7% | The case: memory and GAA etch/dep; FY27 revenue $34.9B (+50%) | AMAT, ASML; GM 49.6→51.8%; fwd P/E 25.9 vs 25.3 / 28.4 | none | 7 sales, $58.3M, 5 sellers (CEO Archer 3×30k, $30.3M) | MB 1,842 / 1,199 TTM; State Street +2.6% | 2.22% / 2.62d / n/f | +0.8% / +13.7%, yes; RS 1m -2.6 / -9.5, 3m -28.0 / -29.1; base; gap held | Q1 ~10-21 (est.) | n/a (29.95%, just under the threshold) |

- Judgment (analyst call): prospect 6: memory and GAA etch in the raised Q1 guide; FY27 revenue +50% consensus; competition 5: GM 49.6 to 51.8% rising; valuation in line with peers; macro 4: materials/industrials archetype 4; narrative 2: semicap basket lagging and worsening.
- Avg target: 373.13 · https://stockanalysis.com/stocks/lrcx/forecast/ · 2026-09-24
- Revenue actual: 6.72 · https://www.marketbeat.com/stocks/NASDAQ/LRCX/earnings/ · 2026-07-29
- Guide: raised · https://www.marketbeat.com/stocks/NASDAQ/LRCX/earnings/ · 2026-07-29
- Revisions 90d: up · https://finance.yahoo.com/quote/LRCX/analysis/ · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=LRCX · 2026-09-24
- Holders up: 1842 · https://www.marketbeat.com/stocks/NASDAQ/LRCX/institutional-ownership/ · 2026-09-24
- Verdict: edge Beat-and-raise with estimates up; the insider leg fails on 10b5-1 sales totalling $58M. Pre-mortem: Memory makers cut capex after the pricing peak. Red team / strongest fact: not red-teamed: one-leg name; the probe's own strongest fact against: the semicap basket is lagging and worsening.

### NU

Tier one_leg_missing; total 59; gates failed: insider.

Research row: | NU | 13.56 / 18.98–11.20 / -28.6% | Buy / 22 (MB 14, $17.92) | $18.78 | $23 / $12 | +38.5 | 8 actions. Itau BBA cut to Market Perform ($18, 9/16). BofA Sell $10. GS Buy $23 (9/24). UBS, Susquehanna raised targets | 8/13: rev $5.88B vs $5.39B; EPS $0.216 vs $0.198. Guide: none (policy) | +9.3% / +4.7% | flat / up (Zacks 0.86 / 0.85 / 0.83) | FCF -$10.3B vs NI $3.61B (loan growth); SBC 4.2% | Case: 139M-customer LatAm bank, ROE 33%, EPS +40% / +27% | MELI, ITUB. GM n/m. Fwd P/E 12.1 vs MELI 32.4, ITUB 8.2 | none seen | CRO Fragelli $3.5M (not 10b5-1); US CEO Junqueira $2.1M | 594 / 302. Adds: Norges, Baillie Gifford, State St. Sells: CRGI, Jennison, Orbis | 2.74%, 2.0d, 9/15 | -5.8% / -8.5%; 50>200 no; RS SPY -10.6/+4.4, XLF -4.0/+6.8; base; gap held (faded) | Q3 print about 11/12 (est.) | n/a (<30%) |

- Judgment (analyst call): prospect 6: 139M customers, ROE 33% reported; competition 5: fwd P/E 12.1 vs MELI 32.4; macro 3: EM archetype 3; narrative 3: fintech fading.
- Avg target: 18.78 · https://stockanalysis.com/stocks/nu/forecast/ · 2026-09-24
- Revenue actual: 5880000000.0 · https://www.marketbeat.com/stocks/NYSE/NU/earnings/ · 2026-09-24
- Guide: none · https://www.nasdaq.com/press-release/nu-holdings-ltd-reports-second-quarter-2026-financial-results-2026-08-13 · 2026-09-24
- Revisions 90d: up · https://www.zacks.com/stock/quote/NU/detailed-earning-estimates · 2026-09-24
- Insider coverage: None · None · None
- Holders up: 594 · https://www.marketbeat.com/stocks/NYSE/NU/institutional-ownership/ · 2026-09-24
- Verdict: edge ROE 33% at 12x forward earnings; the insider leg fails because the Form 4 record is not verified complete. Pre-mortem: Brazilian credit turned while the dollar strengthened. Red team / strongest fact: not red-teamed: one-leg name; the probe's own strongest fact against: fintech fading; the chart below both averages.

### AMZN

Tier one_leg_missing; total 59; gates failed: insider.

Research row: | AMZN | 249.38 / 287.20-196.00 / -13.2% | Strong Buy / 60 | 328.22 | 405/230 | +31.6 | Wells Fargo target 328→338; Goldman 375; Citi 350; Redburn Hold 230 | 7/30: rev $200.61B vs $197.03B; GAAP EPS $5.75 vs $1.82 (includes an investment gain; adjusted $1.97); guide held (Q3 sales $197-202B, operating income $22.5-26.5B) | +15.32%, +16.55% | flat/up | -$11.6B vs $135.3B; SBC 2.5% | AWS growth re-accelerated (+37%) on AI demand and lifts operating income | MSFT, GOOGL; GM 48.5-52.3% rising; fwd P/E 23.5 vs 21.2/22.6; EV/S 3.6 vs 11.3/9.1 | none | $365.0M, 7 sellers; Bezos $346.5M; all 10b5-1 | 4634/3077; State St +5.5%, Dragoneer new, Junto +79% | 0.83%, 2.8, 9/15 | -2.7/+3.6; 50>200 yes; vs SPY -4.6/+5.4, vs XLY +2.0/+12.5; base; held | Q3 earnings ~10/29 (estimated) | n/a |

- Judgment (analyst call): prospect 6: AWS re-accelerated to +37% in the last print; competition 6: GM 48.5 to 52.3% rising; macro 4: quality megacap 4; narrative 6: Mag 7 accelerating.
- Avg target: 328.22 · https://stockanalysis.com/stocks/amzn/forecast/ · 2026-09-24
- Revenue actual: 200610000000.0 · https://www.marketbeat.com/stocks/NASDAQ/AMZN/earnings/ · 2026-09-24
- Guide: held · https://www.cnbc.com/2026/07/30/amazon-amzn-q2-earnings-report-2026.html · 2026-09-24
- Revisions 90d: up · https://www.zacks.com/stock/quote/AMZN/detailed-earning-estimates · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=AMZN · 2026-09-24
- Holders up: 4634 · https://www.marketbeat.com/stocks/NASDAQ/AMZN/institutional-ownership/ · 2026-09-24
- Verdict: edge AWS re-acceleration to +37% at 23.5x; the insider leg fails on Bezos's $346.5M planned sale. Pre-mortem: FCF turned negative and the market repriced the capex. Red team / strongest fact: not red-teamed: one-leg name; the probe's own strongest fact against: FY1 FCF consensus -$34.2B.

### VST

Tier one_leg_missing; total 57; gates failed: delivery.

Research row: | VST | 137.94 (09-24) / 217.10-132.66 / -36.5% | Strong Buy / 20 (19B-0H-1S) | 217.58 | 305 / 106 | 57.7 | MS $227 hold; WFC $212 hold; Mizuho init Buy $169; BNP cut 282→255; TD Cowen cut 222→221 | 08-07: rev $4.02B vs $5.46B, EPS 0.76 vs 1.61 (both missed); guide **held**: EBITDA $6.8-7.6B reaffirmed | -0.6% / +4.8% | down (0↑/2↓) / n/f | FCF $2.26B vs NI $2.22B; SBC 0.8% | Nuclear and gas fleet re-rates on hyperscaler PPAs; EBITDA at or above the guide midpoint funds buybacks | CEG (fwd P/E 19.7), NRG; VST fwd P/E 13.6, EV/S 3.9; batteries compress ERCOT prices | CEO Burke, 3 buys over 8-24 to 9-01, 8,665 sh, $1.17M (Form 4 checked, code P, not 10b5-1) | CFO Moldovan $3.02M, Retail President Hudson $6.75M (9-08; plan not verified) | +3.09M sh; 877/570; 235/135; adds GS +42%, Norges +26%, UBS +17%; cuts JPM -57%, FMR -10% | 3.24% (SA 3.44%), 2.46, date n/f | -5.5% / -11.4%; no; RS vs SPY -1/-22, vs XLU +8/-4; trend_down near low; gap held yes | Q3 ~11-05 (estimated) | ERCOT forward prices softened as batteries flooded the grid; big Q2 revenue miss |

- Judgment (analyst call): prospect 4: EBITDA guide held after a large Q2 revenue miss; PPAs are the story; competition 5: nuclear and gas fleet; fwd P/E 13.6 below CEG 19.7; macro 5: cash-flow value archetype 5: FCF equals net income, buybacks; narrative 4: AI power improving from a low base; quiet improvement.
- Avg target: 217.58 · https://stockanalysis.com/stocks/vst/forecast/ · 2026-09-24
- Revenue actual: 4020000000.0 · https://www.marketbeat.com/stocks/NYSE/VST/earnings/ · 2026-09-24
- Guide: held · https://ts2.tech/en/vistra-nysevst-shares-fall-despite-31-rise-in-ebitda-maintains-2026-outlook/ · 2026-09-24
- Revisions 90d: None · None · None
- Insider coverage: True · https://finviz.com/quote.ashx?t=VST · 2026-09-24
- Holders up: 877 · https://api.nasdaq.com/api/company/VST/institutional-holdings?limit=15&type=TOTAL&sortColumn=marketValue · 2026-09-24
- Verdict: edge Discounted signal: CEO Burke made 3 open-market buys ($1.17M) near the 52-week low; cash-flow shape the regime rewards. Delivery fails on the Q2 revenue miss. Pre-mortem: Batteries flattened the ERCOT curve faster than PPAs arrived. Red team / strongest fact: not red-teamed: one-leg name; the probe's own strongest fact against: revisions 0 up / 2 down.

### BABA

Tier one_leg_missing; total 56; gates failed: delivery.

Research row: | BABA | 110.63 / 192.67–91.99 / -42.6% | Strong Buy / 40 (MB 21, $187.05) | $185.88 | $238.56 / $95.34 | +68.0 | 13 actions, all Buy. Targets $160–210. Round of reiterations 9/21–24 | 8/20: rev $39.64B vs $39.52B; EPS $1.26 vs $1.94 (miss). Guide: none. $10.2B placement on 8/24 | +1.3% / -9.8% | flat / down (Yahoo CNY 44.05 / 44.86 / 45.02; 11 up, 17 down) | FCF -$11.4B vs NI $10.8B; SBC n/a | Case: leading China AI cloud (+45%), EPS +70% / +40% | PDD, JD. GM 38.2/34.5/40.5/39.2. Fwd P/E 12.2 vs PDD 6.4, JD 6.4 | Chairman Tsai $20.7M and CEO Wu $5.0M (8/24–25), code P (ADR: coverage null) | Director Evans about $8.6M (6/29; Finviz shows $68M, an 8x ADS error) | 853 / 545. Adds: Kingstone, Norges. Sells: BMO $138M | 1.89%, 5.4d, 9/15 | -6.2% / -16.4%; 50>200 no; RS SPY -7.6/+11.9, XLY -0.9/+19.0; trend_down; gap failed | Sep-qtr print about 11/24 (est.); 11.11 | AI capex +75%, op income -57%, FCF negative, buyback cut 80%, $10.2B dilutive placement |

- Judgment (analyst call): prospect 4: AI cloud +45%; operating income -57% on capex; competition 4: fwd P/E 12.2 vs PDD 6.4; macro 2: EM 3 minus 1: negative FCF and a $10.2B placement; narrative 3: China AI outside the US themes.
- Avg target: 185.88 · https://stockanalysis.com/stocks/baba/forecast/ · 2026-09-24
- Revenue actual: 39640000000.0 · https://www.marketbeat.com/stocks/NYSE/BABA/earnings/ · 2026-09-24
- Guide: none · https://www.cnbc.com/2026/08/20/alibaba-cloud-revenue.html · 2026-09-24
- Revisions 90d: down · https://finance.yahoo.com/quote/BABA/analysis/ · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=BABA · 2026-09-24
- Holders up: 853 · https://www.marketbeat.com/stocks/NYSE/BABA/institutional-ownership/ · 2026-09-24
- Verdict: edge Discounted signal: the chairman and CEO bought $25.7M on the open market into the placement; China AI cloud +45%. Delivery fails on 90-day revisions down. Pre-mortem: Capex never earned its return and the placement was the top of management's confidence. Red team / strongest fact: not red-teamed: one-leg name; the probe's own strongest fact against: FCF -$11.4B and the buyback cut 80%.

### RDDT

Tier one_leg_missing; total 56; gates failed: insider.

Research row: | RDDT | 152.72 / 263.50-119.27 / -42.0% | Buy / 34 | 213.71 | 300/130 | +39.9 | Exane initiated Hold 180; D.A. Davidson target 200→185; Morgan Stanley 240→210; Guggenheim 255; Truist 275 | 7/30: rev $804.9M vs $731.0M; EPS $1.25 vs $0.95; guide held (Q3 $860-870M, below the current $872-886M consensus) | -20.99%, -9.18% | flat/up | $1.02B vs $0.87B (117%); SBC 12.2% | Logged-in users, ads and AI data licensing keep ~50% growth at a 45% EBITDA margin | META, PINS; GM 91.0-91.9%; fwd P/E 21.5 vs 22.9/7.8; EV/S 9.6 vs 8.8/2.3 | none | $50.1M; COO Wong $30.9M and CEO Huffman $18.2M, both 10b5-1 | 647/277; State St +8.7%, Amundi +21%, Styrax and Light Street new | 14.43%, 4.4, 9/15 | -4.7/-10.7; no; vs SPY -6.2/-7.8, vs XLC -6.7/-11.3; trend_down; not held | Q3 earnings ~10/29 (estimated) | Warning on search traffic from Google AI Overviews, US daily users fell to 53.2M, no new AI licensing deal; -21% on 7/31 |

- Judgment (analyst call): prospect 5: ads and licensing in the beat; Q3 guided below consensus; competition 4: GM ~91%; AI Overviews traffic risk; macro 2: internet platforms 4 minus 2: logged-in traffic risk plus SBC 12%; narrative 2: internet platforms fading.
- Avg target: 213.71 · https://stockanalysis.com/stocks/rddt/forecast/ · 2026-09-24
- Revenue actual: 804910000.0 · https://www.marketbeat.com/stocks/NYSE/RDDT/earnings/ · 2026-09-24
- Guide: held · https://seekingalpha.com/news/4622399-reddit-forecasts-q3-2026-revenue-of-860m-870m-with-45-percent-adjusted-ebitda-margin-midpoint · 2026-09-24
- Revisions 90d: up · https://www.zacks.com/stock/quote/RDDT/detailed-earning-estimates · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=RDDT · 2026-09-24
- Holders up: 647 · https://www.marketbeat.com/stocks/NYSE/RDDT/institutional-ownership/ · 2026-09-24
- Verdict: edge Beat with revisions up; the insider leg fails on $50.1M of planned CEO and COO sales. Pre-mortem: Search traffic loss compounded. Red team / strongest fact: not red-teamed: one-leg name; the probe's own strongest fact against: the Q3 guide sat below consensus.

### SPCX

Tier one_leg_missing; total 55; gates failed: insider.

Research row: | SPCX | $148.03 (9/24) / 225.64-104.83 / -34.4% | Buy / 36 (SA); MB Moderate Buy / 43, 7 sells | $222.42 (MB $218.28) | $450 / $140 | +50.3% | 4 downgrades on 8/7 (Citi Sell, RJ Strong Sell, Susq UP, RBC Hold). Since then 3 target raises, 3 cuts, 2 initiations (Pivotal Buy, DZ Sell $100), MS reiterated $300 on 9/21. First-wave initiations 7/7 (BofA $235, Stifel $190, Mizuho $200, Canaccord $246) | Q2 on 8/4, the first public print: rev $7.81B vs ~$6.85B, EPS -$0.09 vs -$0.26. No guidance | -13.6% / +16.6% | up / up (FY26 EPS -1.65 to 0.07) | FCF -$32.5B vs NI -$8.9B; SBC 10.6% | Starlink (12M subs, 38.6% margin) funds Starship and AI. Revenue ~$45B to ~$108B in FY27 | ASTS, RKLB. GM 44% to 55%, but not 4 consecutive quarters. Fwd P/E 103; EV/S 84 vs RKLB 54, ASTS 217 | none | Shotwell (COO) $52.5M on 9/22, 10b5-1 checked, sold only exercised shares | IPO 6/12, so first 13F cycle: 144 holders, all new, 0 sellers. SC US 122.5M, Darsana 101.5M, State St 10.9M, Dragoneer 8M | 7.73% (SA 9.10%), 1.86, date n/a | +9.2% / +3.4%; 50 slightly above 200. RS vs SPY +7.1 / -7.7; vs XLI +12.7 / +5.1. Base 105-155; gap reversed up (true) | Lock-ups 9/24, 10/9, 10/24 (328.4M each). Q3 print (date n/a) releases ~1.3B. 180-day expiry 12/8 (~800M) | Spiked to $225.64 in 4 sessions on a ~5% float, then fell below the $135 IPO price by late July. Demand faded, the focus moved to losses and capex, and chip stocks sold off (Bloomberg 7/17) |

- Judgment (analyst call): prospect 5: Starlink subscribers and margins are in the first print; Starship and AI capex are ahead; competition 6: launch and LEO broadband leader; EV/S 84; macro 1: long duration: FCF -$32.5B and lock-up supply; narrative 2: space lagging; lock-ups on 24 Sep, 9 Oct and 24 Oct.
- Avg target: 222.42 · https://stockanalysis.com/stocks/spcx/forecast/ · 2026-09-24
- Revenue actual: 7814000000.0 · https://www.sec.gov/Archives/edgar/data/1181412/000162828026052515/earningsreleaseq22608042.htm · 2026-08-04
- Guide: none · https://www.sec.gov/Archives/edgar/data/1181412/000162828026052515/earningsreleaseq22608042.htm · 2026-08-04
- Revisions 90d: up · https://finance.yahoo.com/quote/SPCX/analysis/ · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=SPCX · 2026-09-24
- Holders up: 144 · https://www.marketbeat.com/stocks/NASDAQ/SPCX/institutional-ownership/ · 2026-09-23
- Verdict: edge First-print beat, revisions up, 144 new holders in the first 13F cycle; the insider leg fails on the COO's $52.5M planned sale. Lock-up supply is the dated risk. Pre-mortem: Lock-up supply met a market with no appetite for $32B of negative FCF. Red team / strongest fact: not red-teamed: one-leg name; the probe's own strongest fact against: FCF -$32.5B and 328M shares unlocking on each of 24 Sep, 9 Oct and 24 Oct.

### GLW

Tier one_leg_missing; total 55; gates failed: upside.

Research row: | GLW | 154.15 / 271.78-77.05 / -43.3% | Strong Buy / 17 | 192.44 (MB 176.50) | 238 / 129 | 24.8 (MB 14.5) | Mizuho Buy 210→180; Truist Buy; Oppenheimer 200; Citi 220; JPM Hold | 07-28 BMO: rev 4.74B vs 4.63B, EPS 0.78 vs 0.755; held (EPS 0.85-0.89 vs 0.85; sales 4.9-5.0B vs 5.0B) | -12.1% / +11.5% | flat / up (3.28 / 3.27 / 3.18) | 2.40B vs 1.90B (1.26); 2.5% | Case: AI fiber (Optical +32% y/y); EPS 3.28 to 4.35 | COHR, LITE; GM 37.1→35.5→36.9→36.1; P/E 35.5 vs 20.7 / 27.4 | none | 2 sales, $3.5M, both without a plan (Steverson $2.0M, Gullo $1.5M) | 1446/903 (TTM); State Street +13.4% (41.1M sh) | 2.05%, 1.9d, 09-15 | +0.9% / +3.8%; yes (narrow); RS SPY +4.6/-36.9, XLK -2.4/-37.9; base; gap held | 10-27 Q3 (estimate) | -12% on 07-28 (as much as -20% intraday) on a slightly soft Q3 guide and slower optical growth (CNBC) |

- Judgment (analyst call): prospect 5: optical +32% y/y is reported; Q3 guide soft; competition 4: GM 37.1 to 36.1% flat; fwd P/E 35.5 above COHR and LITE; macro 3: AI networking archetype 1 plus 2: a dividend-paying industrial with 1.26x cash conversion is not long duration; narrative 2: AI networking and optics lagging and worsening.
- Avg target: 192.44 · https://stockanalysis.com/stocks/glw/forecast/ · 2026-09-24
- Revenue actual: 4740000000.0 · https://www.marketbeat.com/stocks/NYSE/GLW/earnings/ · 2026-09-24
- Guide: held · https://www.marketbeat.com/stocks/NYSE/GLW/earnings/ · 2026-07-28
- Revisions 90d: up · https://finance.yahoo.com/quote/GLW/analysis/ · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=GLW · 2026-09-24
- Holders up: 1446 · https://www.marketbeat.com/stocks/NYSE/GLW/institutional-ownership/ · 2026-09-24
- Verdict: edge Optical growth reported at 35x; the upside leg fails on the lower MarketBeat average. Pre-mortem: The optics theme kept de-rating. Red team / strongest fact: not red-teamed: one-leg name; the probe's own strongest fact against: AI networking and optics lagging and worsening.

### UUUU

Tier one_leg_missing; total 53; gates failed: delivery.

Research row: | UUUU | 11.32 / 27.90-10.69 / -59.4% | Strong Buy / 8 (8-0-0) | 24.15 | 32.5 / 16 | 113.3 | Cantor $33; HCW $29; BMO init $18; B. Riley 27→25; **Roth upgrade to Buy $16** | 08-05: rev $25.1M vs ~$30.8M (derived from Finviz), EPS -0.13 vs -0.04; guide **none** (volume guidance only) | +3.7% / +17.2% | flat (0/0) / down (60-day, Zacks article) | FCF -$120M vs NI -$82M; SBC 13.5% | US uranium plus rare-earth oxide producer; ASM deal (closed 08-28); revenue $132M→$262M | UEC, MP; GM 27.8→57.4% rising; EV/S 25.9 | CEO Bhappu 74,000 sh $968k (Form 4: P, not 10b5-1, +41% of holdings); director Hansen $51k | none | +18.87M; 210/146; 65/48; American Century +1315%, VanEck +25%, T. Rowe +56%, Norges new | 21.37%, 7.70, n/f | -14.5% / -34.4%; no; vs SPY -29/-26, vs XLE -30/-37; breakdown; gap held yes | Q3 early Nov (estimated) | Rare earths repriced on US-China thaw hopes; wider Q2 loss; estimates cut |

- Judgment (analyst call): prospect 3: rare-earth and uranium ramp; ASM deal closed; competition 3: GM 27.8 to 57.4% rising from a small base; macro 1: nuclear archetype 1; narrative 1: nuclear lagging and worsening.
- Avg target: 24.15 · https://stockanalysis.com/stocks/uuuu/forecast/ · 2026-09-24
- Revenue actual: 25110000.0 · https://www.marketbeat.com/stocks/NYSEAMERICAN/UUUU/earnings/ · 2026-09-24
- Guide: none · https://www.ad-hoc-news.de/boerse/news/nebenwerte/energy-fuels-stock-falls-3-10-percent-as-q2-loss-widens/70178417 · 2026-09-24
- Revisions 90d: down · https://finance.yahoo.com/markets/stocks/articles/energy-fuels-down-28-past-153400034.html · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=UUUU · 2026-09-24
- Holders up: 210 · https://api.nasdaq.com/api/company/UUUU/institutional-holdings?limit=15&type=TOTAL&sortColumn=marketValue · 2026-09-24
- Verdict: edge Discounted signal: the CEO bought $968k (+41% of holdings) at the lows; 13F adds by American Century and VanEck. Delivery fails on the revenue miss. Pre-mortem: Rare-earth scarcity premium collapsed on a trade deal. Red team / strongest fact: not red-teamed: one-leg name; the probe's own strongest fact against: short interest 21% and the chart in breakdown.

### CRDO

Tier one_leg_missing; total 53; gates failed: insider.

Research row: | CRDO | 195.97 (9/24) / 308.67–86.49 / -36.5% | Strong Buy / 19 (SA); MB Mod Buy 18 | 280.10 (MB 264.89) | 350 / 185 | +42.9 | 10 actions after the print. Four target cuts: MZ 290→245, EVR 325→292, JPM 335→310, BofA 340→275. Raises: Rosenblatt 215→235 (Neutral), TD Cowen 260→300 | 9/1: $479.0M vs $473.3M; $1.20 vs $1.17. Guide held: Q2 $525–535M, FY growth >85% reiterated | -20.0% / -22.4% | up / up (6.31 vs 6.15 vs 6.11) | FCF $439M vs NI $538M (0.81x); SBC 14.8% | AEC and optical DSP for AI clusters. FY27 revenue about $2.5B (+87%), optical >$600M | MRVL, ALAB. GM 67.6→68.5→68.2→64.5 (falling). Fwd P/E 20.3 vs MRVL 38.3 and ALAB 55.6 | none | $101.5M across 18 sales by 6 sellers. CTO $48.9M, COO $46.4M, CEO $2.5M. 15 of 18 marked 10b5-1 | Net not found. 12-month buyers/sellers 582/277. New/exit not found. Cuts: Wellington -61%, Manulife -54% | 5.04%, 0.8d, 9/15 (MB); Finviz 3.94% | -6.6% / +11.3%; 50>200 yes. RS vs XLK: 1m -20.6, 3m -32.4. Base. Gap held: no (gap down) | Q2 about 12/2 (estimate) | Photonics valuation reset in Jun–Jul, then -20% on the print as GAAP gross margin compressed and opex rose |

- Judgment (analyst call): prospect 6: AEC and optical DSP demand in the last print; FY >85% growth reiterated; competition 4: GM 68.5 to 64.5% compressing; fwd P/E 20.3 below MRVL 38 and ALAB 56; macro 1: AI networking archetype 1: long duration at 2.76% real yields; narrative 1: AI networking and optics lagging and worsening; crowd against tape.
- Avg target: 280.1 · https://stockanalysis.com/stocks/crdo/forecast/ · 2026-09-18
- Revenue actual: 479.0 · https://www.marketbeat.com/stocks/NASDAQ/CRDO/earnings/ · 2026-09-01
- Guide: held · https://seekingalpha.com/news/4639142-credo-technology-shares-fall-as-margin-pressure-overshadows-earnings-beat · 2026-09-01
- Revisions 90d: up · https://finance.yahoo.com/quote/CRDO/analysis/ · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=CRDO · 2026-09-24
- Holders up: 582 · https://www.marketbeat.com/stocks/NASDAQ/CRDO/institutional-ownership/ · 2026-09-24
- Verdict: edge Estimates up (14 up / 2 down) at 20x after a -20% print day; the insider leg fails on $101.5M of mostly planned sales. Pre-mortem: Margin compression was structural: switches and optics competition. Red team / strongest fact: not red-teamed: one-leg name; the probe's own strongest fact against: GM 68.5 to 64.5% and the theme lagging.

### OSCR

Tier one_leg_missing; total 50; gates failed: upside.

Research row: | OSCR | 28.87 / 34.48-10.69 / -16.3% | Hold / 11 | 34.60 (MB 33.90) | 49 / 26 | 19.9 | Target raises on 09-17 (Barclays 49, Raymond James 42, Goldman 34, Baird 33, BofA 30 Underperform); UBS 26 and Wells Fargo 27 in Aug; no rating changes | 08-06: rev 4.88B vs 4.73B; EPS 1.10 vs 0.40; guide raised (rev 18.7-19.0B, EOP 500-700M) | -11.9%, +2.2% | up / up (1.06→1.91; 8 up/0 down) | 4.38B vs 0.55B (float-driven, n/m) | Case: ACA exchange leader turning structurally profitable; ICHRA and AI extend margin | CNC, MOH; GM n/m; fwd P/E 16.6 vs 13.3/27.5; EV/S 0.35 vs 0.12/0.21 | none | about $25M discretionary: Schlosser 750k sh $22.8M (08-27/28, no plan), CFO Blackley $0.6M (no plan), Wittman $0.8M (plan), Schlosser $1.5M (plan); CEO Bertolini's $36M excluded as tax sell-to-cover | 204/94 (TTM); visible table mostly Q1-26 | 7.07% (MB 7.44%), 3.2d, 09-15 | -6.7%/+0.7%; 50>200; RS -6.8/-3.8 vs SPY, -3.6/-8.5 vs XLV; base (pulling back 16% from the 09-14 high); gap-down reversed | Q3 11-05/11-09 (estimates); ACA open enrolment 11-01 | n/a |

- Judgment (analyst call): prospect 6: EPS $1.10 vs $0.40; guide raised; competition 4: fwd P/E 16.6; macro 3: small cap 4 minus 1: ACA subsidy policy risk; narrative 3: outside the themes.
- Avg target: 34.6 · https://stockanalysis.com/stocks/oscr/forecast/ · 2026-09-24
- Revenue actual: 4880000000.0 · https://www.marketbeat.com/stocks/NYSE/OSCR/earnings/ · 2026-09-24
- Guide: raised · https://www.sec.gov/Archives/edgar/data/1568651/000156865126000066/oscarhealthsecondquarter20.htm · 2026-08-06
- Revisions 90d: up · https://finance.yahoo.com/quote/OSCR/analysis/ · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=OSCR · 2026-09-24
- Holders up: 204 · https://www.marketbeat.com/stocks/NYSE/OSCR/institutional-ownership/ · 2026-09-24
- Verdict: edge Beat and raise with 8 up / 0 down revisions; upside leg at 20%. Pre-mortem: Policy took the market away. Red team / strongest fact: not red-teamed: one-leg name; the probe's own strongest fact against: the co-founder sold $22.8M outside a plan in August.

### ACHR

Tier one_leg_missing; total 49; gates failed: delivery.

Research row: | ACHR | 5.71 / 14.62-4.30 / -60.9% | Buy / 9 (6-3-0) | 10.61 | 18 / 4.50 | 85.8 | GS Hold $8; Cantor $11; Canaccord $12; RJ Buy; Needham $9 | 08-10: rev $5.0M vs $1.9M beat, EPS -0.34 in line; guide n/f (EBITDA-loss guide only) | +8.5% / +1.0% | flat (0/0) / n/f | FCF -$660M vs NI -$800M; SBC ~4300% of revenue | Midnight in the UAE Restricted Type Certificate path; FAA Phase 3 of 4; revenue $15M→$143M | JOBY, BETA; GM 18.8→14.0%; EV/S 432 | none | $1.69M across 4 officers (Lentell $0.97M, Lyon $0.57M) | +14.98M; 262/238; 82/79; MS +55%, Vanguard +24%; cut ARK -15% | 14.65% (SA 14.97%), 2.84, n/f | +2.4% / -9.4%; no; vs SPY -4/+15, vs XLI +1/+28; base; gap held no | Q3 ~11-05 (estimated); piloted transition flight and UAE certificate (undated) | Dilution (shares +48% y/y), cash burn, still no certification; no dated news read |

- Judgment (analyst call): prospect 1: revenue depends on certification still ahead; competition 2: JOBY ahead on FAA stages; macro 0: pre-revenue, shares +48% y/y; narrative 1: outside any theme; eVTOL is a story.
- Avg target: 10.61 · https://stockanalysis.com/stocks/achr/forecast/ · 2026-09-24
- Revenue actual: 5000000.0 · https://www.marketbeat.com/stocks/NYSE/ACHR/earnings/ · 2026-09-24
- Guide: None · None · None
- Revisions 90d: None · None · None
- Insider coverage: True · https://finviz.com/quote.ashx?t=ACHR · 2026-09-24
- Holders up: 262 · https://api.nasdaq.com/api/company/ACHR/institutional-holdings?limit=15&type=TOTAL&sortColumn=marketValue · 2026-09-24
- Verdict: edge Story with 13F adds; delivery fails on no guidance and no certification. Pre-mortem: Certification slipped and dilution continued. Red team / strongest fact: not red-teamed: one-leg name; the probe's own strongest fact against: SBC about 4,300% of revenue; shares +48% y/y.

### IREN

Tier one_leg_missing; total 49; gates failed: delivery.

Research row: | IREN | 46.15 / 76.87-28.93 / -40.0% | Strong Buy / 17 | 79.03 (MB 81.47) | 131 / 43 | 71.3 | JPM upgrade to Buy 65; Northland init 99; Redburn init Hold 40; Bernstein 100; Cantor 99 | 8/27: rev $137.2M vs ~132M (Zacks $157M); EPS -0.25 vs -0.46 (normalized); ARR target raised to $4bn | -12.5% / +10.2% | down / down (-0.94→-3.42) | FCF -$2.23B vs NI -$0.70B; 29% | $4bn contracted ARR (Microsoft, a frontier lab); FY28 revenue $7.6B | NBIS, CRWV; GM 75.7/72.4/64.4/66.4 (rising); EV/S 28.6 | none (EDGAR: grants only) | none | 319 / 90 | 22.2%, 2.3d, 9/15 | +12.5% / +1.2%; 50<200; +9.2/-7.8; base; down gap reclaimed | Q1 about 11/5 (est.); Horizon 3-4 in Q4 | Revenue miss in the mining exit, $450M impairments, ATM dilution |

- Judgment (analyst call): prospect 4: $4bn contracted ARR from Microsoft and a frontier lab is guided; competition 3: GM 64.4 to 66.4% rising; EV/S 28.6; macro 1: long duration, FCF -$2.2B, converts and GPU debt at 9%; narrative 2: neoclouds lagging; crypto equities accelerating.
- Avg target: 79.03 · https://stockanalysis.com/stocks/iren/forecast/ · 2026-09-24
- Revenue actual: 137.2 · https://www.nasdaq.com/press-release/iren-reports-fy26-results-2026-08-27 · 2026-08-27
- Guide: raised · https://www.nasdaq.com/press-release/iren-reports-fy26-results-2026-08-27 · 2026-08-27
- Revisions 90d: down · https://finance.yahoo.com/quote/IREN/analysis/ · 2026-09-24
- Insider coverage: True · https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001878848&type=4&dateb=&owner=include&count=40 · 2026-09-24
- Holders up: 319 · https://www.marketbeat.com/stocks/NASDAQ/IREN/institutional-ownership/ · 2026-09-24
- Verdict: edge Contracted ARR $4bn; delivery fails on revenue miss and EPS cut -0.94 to -3.42. Pre-mortem: Financing at 9% met a 5% 10-year. Red team / strongest fact: not red-teamed: one-leg name; the probe's own strongest fact against: FCF -$2.23B and SBC 29% of revenue.

### AKAM

Tier one_leg_missing; total 49; gates failed: delivery.

Research row: | AKAM | 110.41 / 165.45–70.82 / -33.3% | Hold / 23; MB Hold 24 | 153.31 (MB 141.62) | 195 / 93 | +38.9 | 11 actions. GS Sell 93; Citi 160→122; Piper upgrade (140→125); JPM upgrade to Neutral 158; HSBC downgrade 171→123 | 8/6: $1,100M vs $1,090M; $1.59 vs $1.57. Guide cut: FY EPS top end $7.15→$7.05, margin 26%→25–26%, Q3 revenue below est | -6.8% / +5.4% | flat / flat (6.69 vs 6.70 vs 6.71) | FCF $956M vs NI $411M (2.3x); SBC 11.8% | Cloud and AI inference services. 2027 revenue +13% to $5.08B | NET, FSLY. GM 59.3→58.7→56.1→55.8 (falling). Fwd P/E 15.5 vs NET 214 and FSLY 42 | none | $0.72M across 2 sales by 1 officer. Both 10b5-1 | Net not found. 12-month buyers/sellers 392/247. Adds: Susquehanna Fund. +1541%, Tidal +329% | 13.39%, 5.9d, 9/15 | -2.6% / -0.5%; 50>200 yes. RS vs XLK: 1m -2.7, 3m -7.7. Base. Gap held: yes (recovered) | Q3 about 11/5 (estimate) | GAAP operating margin halved to 7.3% on AI compute and colocation costs; guide trimmed; GS Sell. Also -6.8% on 9/24, cause not found |

- Judgment (analyst call): prospect 3: AI inference services are a story; FY EPS guide trimmed; competition 3: GM 59.3 to 55.8% falling against NET and FSLY; macro 5: cash-flow value: FCF 2.3x NI, 15.5x forward earnings; narrative 3: outside any theme.
- Avg target: 153.31 · https://stockanalysis.com/stocks/akam/forecast/ · 2026-09-15
- Revenue actual: 1100.0 · https://www.marketbeat.com/stocks/NASDAQ/AKAM/earnings/ · 2026-08-06
- Guide: cut · https://www.sec.gov/Archives/edgar/data/0001086222/000108622226000083/exhibit991-q22026.htm · 2026-08-06
- Revisions 90d: flat · https://finance.yahoo.com/quote/AKAM/analysis/ · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=AKAM · 2026-09-24
- Holders up: 392 · https://www.marketbeat.com/stocks/NASDAQ/AKAM/institutional-ownership/ · 2026-09-24
- Verdict: edge Cash-flow value at 15.5x; delivery fails on the trimmed EPS guide. Pre-mortem: The AI pivot cost margin without growth. Red team / strongest fact: not red-teamed: one-leg name; the probe's own strongest fact against: GM 59.3 to 55.8% falling; Goldman Sell $93.

### RKLB

Tier one_leg_missing; total 48; gates failed: insider.

Research row: | RKLB | 73.61 / 151.00-37.57 / -51.3% | Buy / 20 (16-4-0) | 109.37 | 150 / 64 | 48.6 | Craig-Hallum Buy; **RJ init Buy $80; Berenberg init Buy $83**; BofA 115→110; BTIG Hold | 08-10: rev $234.1M vs $231.6M beat, EPS -0.08 vs -0.06 missed; Q3 guide $250-265M vs $236M (**raised**) | -0.0% / -1.1% | flat (0/0, 2 estimates) / n/f | FCF -$371M vs NI -$165M; SBC 10.6% | Electron plus Space Systems (backlog $2.36B), revenue +59%; Neutron adds medium lift | SPCX (SpaceX), Firefly; GM ~36-38% flat; EV/S 54.5 | none | CEO Beck trust $286.4M (07-06 to 07-08, 10b5-1 checked); CFO Spice $9.45M; COO Klein $5.55M; total $303.4M | +32.5M; 827/320; 329/79; Invesco +410%, GS +117%, JPM +29%; cut Baillie Gifford -44% | 7.70% (SA 8.15%), 2.39, 2026-08-31 | +6.1% / -9.1%; no; vs SPY +10/-13, vs XLI +15/-1; base; gap held no | Q3 ~11-09 (estimated); Neutron to pad Q4 (target) | Neutron slip toward 2027, CEO sales, new ATM |

- Judgment (analyst call): prospect 4: Space Systems backlog $2.36B and the raised Q3 guide; Neutron slipping toward 2027; competition 4: GM 36-38% flat; EV/S 54.5 vs SpaceX 84; macro 1: space archetype 1: long duration with a $1.94B ATM; narrative 1: space lagging and worsening.
- Avg target: 109.37 · https://stockanalysis.com/stocks/rklb/forecast/ · 2026-09-24
- Revenue actual: 234070000.0 · https://www.marketbeat.com/stocks/NASDAQ/RKLB/earnings/ · 2026-09-24
- Guide: raised · https://www.marketbeat.com/stocks/NASDAQ/RKLB/earnings/ · 2026-09-24
- Revisions 90d: None · None · None
- Insider coverage: True · https://finviz.com/quote.ashx?t=RKLB · 2026-09-24
- Holders up: 827 · https://api.nasdaq.com/api/company/RKLB/institutional-holdings?limit=15&type=TOTAL&sortColumn=marketValue · 2026-09-24
- Verdict: edge Backlog and raised guide; insider leg fails on the CEO trust's $286M planned sale and a $1.94B ATM. Pre-mortem: Neutron slipped and the ATM supplied the stock. Red team / strongest fact: not red-teamed: one-leg name; the probe's own strongest fact against: CEO trust sold $286M; space lagging and worsening.

### PLPC

Tier one_leg_missing; total 46; gates failed: upside.

Research row: | PLPC | 429.82 / 504.69–184.02 / -14.8% | not found (SA 404); MB "Buy" 2 | not found (MB $275 stale since 3/9; Finviz 480) | n/f | n/f | Freedom Capital upgrade to Strong Buy 8/4, no target shown | 7/29: $212.7M vs $193.0M; $4.49 vs $2.41. Guide none (does not guide as policy) | +30.0% / +62.5% | not found | FCF $34M vs NI $43M (0.80x); SBC 1.0% | Grid hardening and fiber build. Record Q2: GM 34.3%, EPS +75% | HUBB, ATKR. GM 29.7→29.8→31.3→34.3 (rising). Fwd P/E 30.1 vs HUBB 20.3 and ATKR 14.9 | none | $3.0M across 3 sales. 10% owner Ruhlman $2.1M; a director sold his whole holding. None marked 10b5-1 | Net not found. 12-month buyers/sellers 91/37. Adds: Metzler +285%, Tidal +138%, SIG +36% | 4.52%, 2.2d, 9/15 | +7.4% / +33.2%; 50>200 yes. RS vs XLI: 1m +9.5, 3m +14.4. Uptrend. Gap held: yes | Q3 about 10/28 (estimate) | n/a |

- Judgment (analyst call): prospect 6: record Q2: GM 34.3%, EPS +75%, grid hardening and fiber build; competition 5: GM 29.7 to 34.3% rising; fwd P/E 30 above HUBB and ATKR; macro 4: materials/industrials 4; narrative 4: grid theme improving; uncovered by the Street.
- Avg target: None · None · None
- Revenue actual: 212.68 · https://www.marketbeat.com/stocks/NASDAQ/PLPC/earnings/ · 2026-07-29
- Guide: none · https://www.prnewswire.com/news-releases/preformed-line-products-announces-record-second-quarter-2026-financial-results-302837970.html · 2026-07-29
- Revisions 90d: None · None · None
- Insider coverage: True · https://finviz.com/quote.ashx?t=PLPC · 2026-09-24
- Holders up: 91 · https://www.marketbeat.com/stocks/NASDAQ/PLPC/institutional-ownership/ · 2026-09-24
- Verdict: edge Record print, gross margin 29.7 to 34.3%; the upside leg fails because no current consensus exists. Pre-mortem: The record quarter was a pull-forward. Red team / strongest fact: not red-teamed: one-leg name; the probe's own strongest fact against: a director sold his entire holding outside a plan.

### WULF

Tier one_leg_missing; total 42; gates failed: delivery.

Research row: | WULF | 16.29 / 29.84-10.43 / -45.4% | Strong Buy / 22 | 34.30 (MB 33.33) | 62.5 / 15 | 110.6 | 3 initiations at Buy (WFC 30, UBS 24, Freedom 19); Redburn Hold 15; Bernstein 36 | 8/5: rev $44.8M vs 46.0M, EPS -1.94 vs -0.24 ($756M warrant charge); no guidance | -4.3% / -9.0% | down / down | FCF -$2.74B vs NI -$1.95B; 128% | Anthropic ~$19B/20y plus Fluidstack (Google backstop) | CIFR, APLD; GM 72.3/93.1/47.3/66.1; EV/S 65.4 | director Bucella $190K (3 buys) | $9.0M: CEO Prager (monthly), 2 directors | 289 / 103; Steamboat -86% | 34.7%, 3.65d, 9/15 | -3.6% / -9.8%; 50<200; -0.4/-42.0; trend_down; gap not held | Q3 about 11/9 (est.) | Q2 charge, $1.2B equity raised, CEO selling |

- Judgment (analyst call): prospect 3: Anthropic ~$19B lease contracted, build ahead; competition 2: GM volatile; SBC 128% of revenue; macro 0: the thesis needs the regime to change: $5.3B debt and a hostile rate tape; narrative 1: neoclouds lagging.
- Avg target: 34.3 · https://stockanalysis.com/stocks/wulf/forecast/ · 2026-09-24
- Revenue actual: 44.77 · https://www.marketbeat.com/stocks/NASDAQ/WULF/earnings/ · 2026-08-05
- Guide: none · https://investors.terawulf.com/news-events/press-releases/detail/144/terawulf-reports-second-quarter-2026-results · 2026-08-05
- Revisions 90d: down · https://finance.yahoo.com/quote/WULF/analysis/ · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=WULF · 2026-09-24
- Holders up: 289 · https://www.marketbeat.com/stocks/NASDAQ/WULF/institutional-ownership/ · 2026-09-24
- Verdict: edge Contracted Anthropic lease; delivery fails on EPS and revenue. Pre-mortem: Financing costs overwhelmed the contracted revenue. Red team / strongest fact: not red-teamed: one-leg name; the probe's own strongest fact against: SBC 128% of revenue, short 35%.

### EOSE

Tier one_leg_missing; total 41; gates failed: delivery.

Research row: | EOSE | 3.24 / 19.86-3.01 / -83.7% | Buy / 11 (4-7-0) | 6.61 | 10 / 4.00 | 104.0 | Needham cut 11→10; Stifel $9; Truist $7; Roth Hold 4→4.5; JPM Hold 6→5 | 08-05: rev $68.8M vs $68.3M beat, EPS -1.20 vs -0.19 missed; guide **cut** (to $300-350M from $300-400M) | -12.2% / -2.5% | down (0/2) / n/f | FCF -$420M vs NI -$529M; SBC 10.4% | Zinc long-duration storage scaled through the Cerberus Frontier Power JV; revenue $306M→$576M | FLNC, ESS; GM -111→-71% improving but negative; EV/S 10.2 | director Song 15,000 sh $59k | CEO Mastrangelo $1.55M; CCO Kroeker $0.95M; CAO Puri $0.46M; others (total $3.12M) | +28.0M; 218/152; 79/45; Hudson Bay new 13.7M, SIG +52%, BlackRock +13% | 33.65% (SA 31.19%), 4.13, 2026-09-15 | -14.3% / -58.0%; no; vs SPY -9/-51, vs XLI -3/-38; trend_down; gap held yes | Q3 ~11-04 (estimated) | Negative gross margins, EPS miss, top of guide cut, dilution |

- Judgment (analyst call): prospect 2: zinc storage scale-up via the JV; guide cut; competition 1: GM -111 to -71%, negative; macro 0: the thesis needs the regime to change: negative margins and dilution; narrative 2: AI power improving but the name is -84% from its high.
- Avg target: 6.61 · https://stockanalysis.com/stocks/eose/forecast/ · 2026-09-24
- Revenue actual: 68780000.0 · https://www.marketbeat.com/stocks/NASDAQ/EOSE/earnings/ · 2026-09-24
- Guide: cut · https://investors.eose.com/news-releases/news-release-details/eos-energy-enterprises-reports-second-quarter-2026-financial · 2026-09-24
- Revisions 90d: None · None · None
- Insider coverage: True · https://finviz.com/quote.ashx?t=EOSE · 2026-09-24
- Holders up: 218 · https://api.nasdaq.com/api/company/EOSE/institutional-holdings?limit=15&type=TOTAL&sortColumn=marketValue · 2026-09-24
- Verdict: edge Deep drawdown story; delivery fails on the guide cut. Pre-mortem: Negative margins and dilution. Red team / strongest fact: not red-teamed: one-leg name; the probe's own strongest fact against: gross margin -71%, short 34%.

### APP

Tier one_leg_missing; total 41; gates failed: delivery.

Research row: | APP | 312.47 / 745.61-297.50 / -58.1% | Buy / 33 | 498.37 | 790/325 | +59.5 | Evercore target 630→510; BTIG 408→396; Needham 500→475; Wells Fargo Hold 357→325; Piper Hold 325; Citi 600 | 8/5: rev $1.92B vs $1.94B; EPS $3.76 vs $3.76; guide labelled cut (Q3 about $2.07B vs $2.08B consensus) | -19.66%, -25.16% | flat/down | $4.53B vs $4.41B (103%); SBC 4.1% | The Axon ad engine extends into e-commerce and keeps 40%+ growth at 80%+ margins; the SEC probe closed with no action | TTD, U; GM 87.6-89.0%; fwd P/E 15.6 vs 49.8/37.9; EV/S 15.4 vs 1.6/9.1 | none | $1.6M, one director, 10b5-1 | 1204/689; State St +28%, Amundi +19.5%, Manulife +410% | 3.75%, 2.5, 9/15 | -9.7/-33.3; no; vs SPY +0.5/-34.4, vs XLK -6.5/-35.4; trend_down; not held | Q3 earnings ~11/4 (estimated) | Short-seller reports and an SEC probe early in 2026, then the first Q2 miss against its own guide, which also guided Q3 below consensus; shares fell 20% |

- Judgment (analyst call): prospect 4: Axon e-commerce extension is a story; Q3 guided below consensus; competition 5: GM 87.6-89.0%; fwd P/E 15.6 below TTD 49.8; macro 2: AI software 1 plus 1: FCF 103% of NI at 15x; narrative 2: AI applications fading; chart broken.
- Avg target: 498.37 · https://stockanalysis.com/stocks/app/forecast/ · 2026-09-24
- Revenue actual: 1920000000.0 · https://www.marketbeat.com/stocks/NASDAQ/APP/earnings/ · 2026-09-24
- Guide: cut · https://seekingalpha.com/news/4626587-applovin-craters-20-after-q2-revenue-falls-short-of-expectations · 2026-09-24
- Revisions 90d: down · https://www.zacks.com/stock/quote/APP/detailed-earning-estimates · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=APP · 2026-09-24
- Holders up: 1204 · https://www.marketbeat.com/stocks/NASDAQ/APP/institutional-ownership/ · 2026-09-24
- Verdict: edge 15.6x with FCF 103% of NI; delivery fails on a Q3 guide below consensus. Pre-mortem: The growth decelerated below the multiple. Red team / strongest fact: not red-teamed: one-leg name; the probe's own strongest fact against: the first miss against its own guide.

### ONDS

Tier one_leg_missing; total 40; gates failed: delivery.

Research row: | ONDS | 7.60 / 15.28-4.95 / -50.3% | Strong Buy / 9 | 19.42 | 25/13 | +155.5 | Ladenburg target 21.5→22.75; H.C. Wainwright 25; Roth 13; Needham and Lake Street 19 | 8/13: rev $83.8M vs $68.0M; EPS -$0.19 vs -$0.09; guide raised (FY26 $525-550M) | -8.80%, -14.23% | flat/down | -$172M vs +$168M (one-off gain); SBC 58% | Drones and counter-drone systems plus acquisitions take revenue to about $1B in 2027 on a $757M pro forma backlog | AVAV, KTOS; GM 26-49%; EV/S 17.7 vs 4.2/5.0 | none | $67K, one director, 10b5-1 | 214/41; RFG +57%, BNY new | 42.19%, 3.9, 9/15 | -4.8/-19.8; no; vs SPY -7.9/-5.5, vs XLK -14.9/-6.5; trend_down; not held | Q3 earnings ~11/12 (estimated) | Dilution (share count up about 259% in a year), Q2 EPS miss, short interest about 42% |

- Judgment (analyst call): prospect 3: revenue guide raised to $525-550M through acquisitions; competition 2: GM 26-49%; EV/S 17.7 vs AVAV 4.2; macro 0: the thesis needs the regime to change: 42% short, share count +259%; narrative 1: defense and drones fading.
- Avg target: 19.42 · https://stockanalysis.com/stocks/onds/forecast/ · 2026-09-24
- Revenue actual: 83770000.0 · https://www.marketbeat.com/stocks/NASDAQ/ONDS/earnings/ · 2026-09-24
- Guide: raised · https://ir.ondas.com/press-releases/detail/326/ondas-posts-record-q2-2026-revenue-of-83-8-million-on · 2026-09-24
- Revisions 90d: down · https://www.zacks.com/stock/quote/ONDS/detailed-earning-estimates · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=ONDS · 2026-09-24
- Holders up: 214 · https://www.marketbeat.com/stocks/NASDAQ/ONDS/institutional-ownership/ · 2026-09-24
- Verdict: edge Guide raised by acquisition; delivery fails on the EPS miss. Pre-mortem: Share count kept rising. Red team / strongest fact: not red-teamed: one-leg name; the probe's own strongest fact against: short 42%, share count +259% y/y.

### CIFR

Tier one_leg_missing; total 40; gates failed: delivery.

Research row: | CIFR | 18.10 / 30.14-11.01 / -40.0% | Strong Buy / 20 | 31.13 (MB 28.86) | 69 / 18 | 72.0 | MS raised to 54; WFC init 25; UBS init 23; Redburn and Freedom init Hold 18/22 | 8/4: rev $24.8M vs 31.9M, EPS -0.65 vs -0.25; no guidance | -15.7% / -28.8% | n/a (Yahoo error) | FCF -$1.50B vs NI -$1.12B; 47% | ~$11.4B contracted; 2027 EPS +0.18 | WULF, IREN; GM -131/-51/1/43 (collapsing); EV/S 64.2 | none | CEO Page $4.9M (July) | 260 / 82 | 18.1%, 2.3d, 9/15 | -0.6% / -1.5%; 50<200; +10.8/-34.0; base; gap not held | Q3 about 11/2 (est.) | Q2 miss as mining was decommissioned; -29% in the week after |

- Judgment (analyst call): prospect 3: ~$11.4B contracted; Q2 gross margin -131%; competition 2: GM collapsing in the transition; macro 0: the thesis needs the regime to change: $5.6B debt; narrative 1: neoclouds lagging.
- Avg target: 31.13 · https://stockanalysis.com/stocks/cifr/forecast/ · 2026-09-24
- Revenue actual: 24.84 · https://www.marketbeat.com/stocks/NASDAQ/CIFR/earnings/ · 2026-08-04
- Guide: none · https://www.sec.gov/Archives/edgar/data/0001819989/000181998926000038/q226_earningsxprxdraftxvf.htm · 2026-08-04
- Revisions 90d: None · None · None
- Insider coverage: True · https://finviz.com/quote.ashx?t=CIFR · 2026-09-24
- Holders up: 260 · https://www.marketbeat.com/stocks/NASDAQ/CIFR/institutional-ownership/ · 2026-09-24
- Verdict: edge Contracted $11.4B; delivery fails on the Q2 miss. Pre-mortem: The transition cost more than the contracts paid. Red team / strongest fact: not red-teamed: one-leg name; the probe's own strongest fact against: Q2 gross margin -131%.

### SOFI

Tier one_leg_missing; total 40; gates failed: upside.

Research row: | SOFI | 16.80 / 32.73–14.88 / -48.7% | Hold / 26 (MB 23, $22.53: alt) | $20.34 | $30 / $12 | +21.1 (MB +34.1) | 12 actions. Initiations: Piper OW $22, Scotia OP $25, Loop Hold $22. KBW Sell $16, MS UW $15. Mizuho cut 29 to 22 | 7/29: rev $1.21B vs $1.11B; EPS $0.12 vs $0.11. Raised FY adj. net revenue to $4.75–4.85B; EPS $0.60 held | -8.9% / +9.0% (the down gap filled) | flat / flat (Zacks 0.60 / 0.60 / 0.59) | FCF -$8.79B vs NI $636M (loan flows, not comparable); SBC 6.6% | Case: digital bank with members +35%, revenue +36%, EPS +60% / +37% | HOOD, LC. GM n/m. Fwd P/E 20.5 vs HOOD 41.5, LC 6.4 | none | 4 sales, 10b5-1, $0.89M (EVP, CTO) | 668 / 282. Adds: BlackRock, Norges, Vanguard, Two Sigma | 15.01%, 5.2d, 9/15 (Finviz 14.0%) | -4.5% / -12.8%; 50>200 no; RS SPY -11.8/-7.4, XLF -5.1/-4.9; trend_down; gap filled | Q3 print about 10/27 (est.) | Multiple compression, Muddy Waters short report (3/30), flat Q1 guide, lending-heavy mix, tech platform -27% |

- Judgment (analyst call): prospect 5: members +35% and a raised revenue guide; competition 3: bank-charter competition against HOOD and LC; macro 2: fintech 1 plus 1: profitable, but lending-heavy into a rising 2y; narrative 2: fintech fading.
- Avg target: 20.34 · https://stockanalysis.com/stocks/sofi/forecast/ · 2026-09-24
- Revenue actual: 1210000000.0 · https://www.marketbeat.com/stocks/NASDAQ/SOFI/earnings/ · 2026-09-24
- Guide: raised · https://www.benzinga.com/trading-ideas/movers/26/07/60758430/sofi-stock-falls-despite-q2-earnings-beat-and-raised-guidance-what-investors-need-to-know · 2026-09-24
- Revisions 90d: flat · https://www.zacks.com/stock/quote/SOFI/detailed-earning-estimates · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=SOFI · 2026-09-24
- Holders up: 668 · https://www.marketbeat.com/stocks/NASDAQ/SOFI/institutional-ownership/ · 2026-09-24
- Verdict: edge Members +35%, guide raised; the upside leg fails at 21% with a 34% MarketBeat range. Pre-mortem: The rate regime hit a lending-heavy mix. Red team / strongest fact: not red-teamed: one-leg name; the probe's own strongest fact against: fintech fading; short 15%.

### CAT

Tier no_runway; total 64; gates failed: none.

Research row: | CAT | 805.25 / 1073.46-459.58 / -25.0% | Buy / 28 | 975.61 (MB 994.38) | 1225 / 575 | 21.2 | Upgrades from Stifel and Freedom; President Capital initiated Buy 999; post-print target raises (UBS 925, Barclays 900, DA Davidson 882, RBC 897); no downgrades | 08-04: rev 20.54B vs 19.34B; EPS 8.17 vs 6.22; guide raised (FY sales growth mid-to-high teens; backlog $72B, +92%) | +5.6%, +1.6% | up / up (24.65→27.37) | 8.99B vs 10.84B (0.83) | Case: data-centre power drives the backlog, EPS +43% in 2026 and +19% in 2027 | DE, CNH; GM 28.9→26.0→30.0→33.6; fwd P/E 28.0 vs 33.1/24.4; EV/S 5.48 vs 5.11/2.27 | none | CEO Creed 08-28, 32,401 sh at $808.98 = $26.2M, exercise-and-sell, no plan | 2540/1817 (TTM); State Street +1.4M; Amundi -155k | 1.65% (MB 1.83%), 2.5d, 09-15 | -0.7%/-23.8%; 50>200; RS -0.9/-28.3 vs SPY, +4.6/-15.5 vs XLI; base; gap faded, price below pre-print level | Q3 10-28 (SA) or 11-04 (MB), both estimates | n/a (-25%) |

- Judgment (analyst call): prospect 7: data-center power backlog $72B, +92%, in the beat and raise; competition 6: GM 28.9 to 33.6% rising; macro 5: materials/industrials 4 plus 1: FCF and pricing; narrative 4: AI power improving.
- Avg target: 975.61 · https://stockanalysis.com/stocks/cat/forecast/ · 2026-09-24
- Revenue actual: 20540000000.0 · https://www.marketbeat.com/stocks/NYSE/CAT/earnings/ · 2026-09-24
- Guide: raised · https://www.bnnbloomberg.ca/business/company-news/2026/08/04/caterpillar-raises-2026-revenue-growth-target-after-quarterly-profit-beat/ · 2026-08-04
- Revisions 90d: up · https://www.zacks.com/stock/quote/CAT/detailed-earning-estimates · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=CAT · 2026-09-24
- Holders up: 2540 · https://www.marketbeat.com/stocks/NYSE/CAT/institutional-ownership/ · 2026-09-24

### ANET

Tier no_runway; total 64; gates failed: upside, insider.

Research row: | ANET | 205.70 / 214.89–114.52 / -4.3% | Strong Buy / 31; MB Buy 23 | 241.93 (MB 227.80) | 289 / 190 | +17.6 | 18 actions. 13 raises on 8/5, e.g. Barclays 195→289, UBS 187→259, Rosenblatt 210→280. DB initiated at 220 | 8/4: $3,036M vs $2,830M; $1.02 vs $0.886. Guide raised: FY26 to $12.6B (third raise); Q3 about $3.3B, EPS $1.06–1.08 | +3.6% / +10.5% | flat (26 up/0 down) / up (4.11 vs 4.11 vs 3.63) | FCF $5.16B vs NI $4.04B (1.28x); SBC 4.8% | AI Ethernet fabrics. 2026 revenue +40%; AI fabrics at least $3.5B | CSCO, NVDA. GM 64.6→62.9→61.9→62.9 (flat). Fwd P/E 39.4 vs CSCO 19.3 and NVDA 14.3 | none | $858M across 26 sales. CEO Ullal $433M, 10% owner Bechtolsheim $397M. 25 of 26 marked 10b5-1 | Net not found. 12-month buyers/sellers 1474/939. No reliable named adds (State Street row excluded) | 1.08%, 3.0d, 9/15 | +8.6% / +31.3%; 50>200 yes. RS vs XLK: 1m +0.6, 3m +18.8. Uptrend near a breakout. Gap held: yes | Q3 about 11/3 (estimate) | n/a |

- Judgment (analyst call): prospect 7: AI Ethernet fabrics in the third FY raise to $12.6B; competition 6: GM ~62-63% stable with share gains; fwd P/E 39.4 premium; macro 3: quality megacap 4 minus 1: 39x forward earnings; narrative 3: AI networking lagging, but the name itself is near highs; outside the basket's weakness.
- Avg target: 241.93 · https://stockanalysis.com/stocks/anet/forecast/ · 2026-08-31
- Revenue actual: 3036.0 · https://www.marketbeat.com/stocks/NYSE/ANET/earnings/ · 2026-08-04
- Guide: raised · https://www.gurufocus.com/news/9004375/arista-networks-inc-anet-q2-2026-earnings-call-highlights-record-3-billion-quarter-and-raised-2026-guidance-signal-strong-ai-momentum · 2026-08-04
- Revisions 90d: up · https://finance.yahoo.com/quote/ANET/analysis/ · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=ANET · 2026-09-24
- Holders up: 1474 · https://www.marketbeat.com/stocks/NYSE/ANET/institutional-ownership/ · 2026-09-24

### VIAV

Tier no_runway; total 59; gates failed: none.

Research row: | VIAV | 37.23 / 60.43–12.05 / -38.4% | Strong Buy / 8; MB Mod Buy 9 | 61.43 (MB 55.43) | 70 / 44 | +65.0 | 7 actions. Stifel 65; Rosenblatt 70. Post-print cuts: UBS 60→44 (Neutral), Needham 68→60, B.Riley 63→60 | 8/5: $443.1M vs $432.6M; $0.34 vs $0.298. Guide raised: Q1 FY27 $450–460M, EPS $0.40–0.42 vs $0.28 | +4.3% / +10.5% | flat / up (1.64 vs 1.64 vs 1.24) | FCF $83M vs NI -$30M; SBC 3.7% | Network and data-center test. FY27 revenue $1.89B (+25%), EPS $1.64 | KEYS, CIEN. GM 59.7→61.1→61.6→60.6 (flat). Fwd P/E 19.1 vs KEYS 26.1 and CIEN 30.4 | none | $8.4M across 7 sales by 5 sellers. Only 2 marked 10b5-1. CFO $2.0M and a director $3.3M not under a plan | Net not found. 12-month buyers/sellers 259/127. Add: UBS AM +39%. Cut: Wellington -30% | 4.65%, 2.4d, 9/15 | -2.0% / +3.2%; 50>200 yes. RS vs XLK: 1m -8.4, 3m -31.7. Base. Gap held: yes | Q1 FY27 about 10/28 (estimate) | -18% in 3 months despite growth: profit-taking, the 14-week quarter, dilution. UBS cut to $44 |

- Judgment (analyst call): prospect 5: network and data-center test in the raised Q1 FY27 guide; competition 4: GM ~60-61% flat; fwd P/E 19.1 below KEYS 26.1 and CIEN 30.4; macro 3: materials/industrials 4 minus 1: small cap with dilution; narrative 3: outside a basket; near the optics theme's weakness.
- Avg target: 61.43 · https://stockanalysis.com/stocks/viav/forecast/ · 2026-09-23
- Revenue actual: 443.1 · https://www.marketbeat.com/stocks/NASDAQ/VIAV/earnings/ · 2026-08-05
- Guide: raised · https://www.sec.gov/Archives/edgar/data/0000912093/000162828026053381/viavq4fy268-kex991.htm · 2026-08-05
- Revisions 90d: up · https://finance.yahoo.com/quote/VIAV/analysis/ · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=VIAV · 2026-09-24
- Holders up: 259 · https://www.marketbeat.com/stocks/NASDAQ/VIAV/institutional-ownership/ · 2026-09-24

### GEV

Tier no_runway; total 59; gates failed: none.

Research row: | GEV | 955.04 / 1195.94-530.16 / -20.1% | Buy / 37 (30-7-0) | 1237 | 1450 / 940 | 29.5 | Jefferies cut 1210→1185; MS $1350; BofA $1310; **GLJ init Sell $470**; Bernstein $1298 | 07-22: rev $11.10B vs $10.79B beat, EPS 2.47 vs 3.17 missed; guide **raised** (revenue +$1B to $45.5-46.5B; FCF to $11.5-12.5B) | -8.7% / -16.5% | down (1↑/2↓ Yahoo) / flat (30.77→30.78) | FCF $12.44B vs NI $9.53B | $176B backlog, 116 GW gas reservations, FCF $11.5-12.5B | Siemens Energy, MHI; GM 19.2→21.6%; fwd P/E 38.9, EV/S 5.9 | none | none (open-market) | +6.93M; 2025/1175; 500/134; Fisher new 3.56M, Cap World +17%, GS +42%; cut FMR -12% | 3.30%, 3.50, n/f | -2.0% / +5.1%; yes; vs SPY +3/-17, vs XLI +8/-4; base; gap held no | Q3 10-28 (confirmed, company events page) | n/a (-20%) |

- Judgment (analyst call): prospect 6: $176B backlog, FY revenue and FCF guides raised; competition 6: GM 19.2 to 21.6% rising; oligopoly with Siemens Energy and MHI; macro 5: cash-flow value archetype 5: FCF $12B; narrative 4: AI power improving.
- Avg target: 1237.0 · https://stockanalysis.com/stocks/gev/forecast/ · 2026-09-24
- Revenue actual: 11100000000.0 · https://www.marketbeat.com/stocks/NYSE/GEV/earnings/ · 2026-09-24
- Guide: raised · https://www.gevernova.com/news/press-releases/ge-vernova-reports-second-quarter-2026-financial-results-raises-2026-financial · 2026-09-24
- Revisions 90d: flat · https://finance.yahoo.com/quote/GEV/analysis/ · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=GEV · 2026-09-24
- Holders up: 2025 · https://api.nasdaq.com/api/company/GEV/institutional-holdings?limit=15&type=TOTAL&sortColumn=marketValue · 2026-09-24

### LITE

Tier no_runway; total 58; gates failed: upside, insider.

Research row: | LITE | 929.04 / 1085.68–144.52 / -14.4% | Buy / 26; MB Mod Buy 22 | 1,149 (MB 1,053.83) | 1,400 / 820 | +23.7 | 15 actions. Initiations: DB 1200, Evercore 1100. Post-print: JPM 1280, Mizuho 1140, MS 900→1000; BofA cut 1100→1000; UBS and TD Cowen at 820 | 8/11: $1,006M vs $987.7M; $3.23 vs $2.97. Guide raised: Q1 $1.225–1.275B, EPS $4.05–4.35 vs $3.63 consensus | +13.6% / +0.9% | up / up (21.67 vs 21.62 vs 18.13) | FCF $300M vs NI -$6.94B (non-cash $7.8B convert loss); SBC 5.7% | EML/CW lasers for AI. FY27 revenue $6.3B (+110%), EPS about $21.7 | COHR, AAOI. GM 37.7→39.0→46.6→49.3 (rising). Fwd P/E 27.4 vs COHR 20.7 | none | $63.1M across 31 sales by 4 sellers. 28 marked 10b5-1. $43M on 8/25 by GC and an officer | Net not found. 12-month buyers/sellers 670/290. Adds: NPS, Amundi +189%. Cuts: Styrax -36%, Wellington -28% | 7.29%, 1.6d, 9/15 | +8.7% / +27.9%; 50>200 yes. RS vs XLK: 1m -2.2, 3m +2.3. Uptrend. Gap held: yes, but only +0.9% | Q1 about 11/3 (estimate) | n/a |

- Judgment (analyst call): prospect 7: EML and CW lasers in the last two prints; Q1 EPS guide $4.05-4.35 vs $3.63; competition 6: GM 37.7 to 49.3% rising fast; share held; macro 2: AI networking 1 plus 1: earnings inflecting; narrative 1: AI networking and optics lagging and worsening.
- Avg target: 1149 · https://stockanalysis.com/stocks/lite/forecast/ · 2026-09-23
- Revenue actual: 1006.0 · https://www.marketbeat.com/stocks/NASDAQ/LITE/earnings/ · 2026-08-11
- Guide: raised · https://www.sec.gov/Archives/edgar/data/1633978/000162828026055726/lite_ex991xq4fy26.htm · 2026-08-11
- Revisions 90d: up · https://finance.yahoo.com/quote/LITE/analysis/ · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=LITE · 2026-09-24
- Holders up: 670 · https://www.marketbeat.com/stocks/NASDAQ/LITE/institutional-ownership/ · 2026-09-24

### ON

Tier no_runway; total 57; gates failed: none.

Research row: | ON | 73.15 / 134.92-44.56 / -45.8% | Buy / 29 (16 Hold) | 103.84 (MB 94.76) | 150 / 75 | 42.0 (MB 29.5) | Jefferies Buy 115; Seaport init Buy 100; Barclays Hold 100; Truist Hold 91→75; Craig-Hallum Hold | 08-03 AMC: rev 1.60B vs 1.59B, EPS 0.74 vs 0.715; raised (EPS 0.81-0.93 vs 0.83) | +0.5% / +0.9% | flat / up (Zacks 3.23 / 3.23 / 3.11) | 1.50B vs 0.63B (2.38); 2.4% | Case: auto/industrial recovery plus the Synaptics physical-AI platform; EPS 3.20 to 4.53 | NXPI, TXN; GM 37.9→38.1→38.5→39.3; P/E 16.3 vs 12.7 / 26.3 | none | none (verified: last Finviz row is 06-10) | 399/306 (TTM); Junto -60%, NPS -20%; Engineers Gate +570%; BlueCrest exited | 7.62%, 3.0d, 09-15 | -6.2% / -8.3%; yes; RS SPY +0.7/-42.9, XLK -6.3/-43.9; trend_down; gap held | 11-02 Q3 (estimate); Synaptics close expected mid-2027 | -23% on 06-26 on the all-stock $7B Synaptics deal (1.35 ON per SYNA), then the July semis sell-off (Motley Fool) |

- Judgment (analyst call): prospect 4: auto and industrial recovery is guided; the Synaptics deal adds execution risk; competition 4: GM 37.9 to 39.3% flat-up; fwd P/E 16.3 mid-peer; macro 4: quality megacap 4; cash conversion 2.4x; narrative 3: semis improving, auto and industrial outside the theme.
- Avg target: 103.84 · https://stockanalysis.com/stocks/on/forecast/ · 2026-09-24
- Revenue actual: 1600000000.0 · https://www.marketbeat.com/stocks/NASDAQ/ON/earnings/ · 2026-09-24
- Guide: raised · https://www.marketbeat.com/stocks/NASDAQ/ON/earnings/ · 2026-08-03
- Revisions 90d: up · https://www.zacks.com/stock/quote/ON/detailed-earning-estimates · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=ON · 2026-09-24
- Holders up: 399 · https://www.marketbeat.com/stocks/NASDAQ/ON/institutional-ownership/ · 2026-09-24

### SNDK

Tier no_runway; total 56; gates failed: insider.

Research row: | SNDK | 1753.62 / 2354.39-93.54 / -25.5% | Buy / 25 | 2137 | 3600 / 1000 | 21.9 | Rosenblatt init Buy 2400; Susquehanna 2745; Citi 2100; Bernstein 3000; Mizuho 1900→1875 | 08-05: rev 8.97B vs 8.42B*, EPS 39.25 vs 33.28; raised (EPS 44-46 vs 41.45; rev 10.3-10.8B vs 10.4B); $14B buyback | -6.8% / +13.2% | flat / up (213.9 vs 214.1 / 188.9) | 11.5B vs 11.4B (1.01); 1.2% | Case: AI eSSD keeps NAND tight; revenue 20.2B (FY26) to 49.0B (FY27) | MU, WDC; GM 29.8→50.9→78.4→84.6; fwd P/E 6.7 vs 6.8 / 13.7 | none | 9 sales, $121.4M, all 10b5-1; CEO Goeckeler $105M (Sep 14 and 17) | up/down 897/196 (TTM); no large named moves | 3.85%, 0.6d, 09-15 | +16.2% / +59.4%; yes; RS SPY +18.3/-29.4, XLK +11.3/-30.4; trend_up; gap held (recovered) | about 11-05 FQ1 (inferred from last year's 11-06 report date; no aggregator date found) | n/a |

- Judgment (analyst call): prospect 7: NAND tightness is in the beat and raise and a $14B buyback; competition 4: GM 29.8 to 84.6% cyclical; fwd P/E 6.7 at peak; macro 4: materials/industrials 4; narrative 5: memory improving; crowded among accounts.
- Avg target: 2137.0 · https://stockanalysis.com/stocks/sndk/forecast/ · 2026-09-24
- Revenue actual: 8970000000.0 · https://www.marketbeat.com/stocks/NASDAQ/SNDK/earnings/ · 2026-09-24
- Guide: raised · https://www.marketbeat.com/stocks/NASDAQ/SNDK/earnings/ · 2026-08-05
- Revisions 90d: up · https://finance.yahoo.com/quote/SNDK/analysis/ · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=SNDK · 2026-09-24
- Holders up: 897 · https://www.marketbeat.com/stocks/NASDAQ/SNDK/institutional-ownership/ · 2026-09-24

### SNOW

Tier no_runway; total 54; gates failed: insider.

Research row: | SNOW | 334.00 / 384.56-118.30 / -13.2% | Buy / 50 | 425.19 | 525/110 | +27.3 | 9/3-9/4 targets raised: Goldman 300→436, Raymond James 275→425, Mizuho 355→425, Argus 300→450; Morgan Stanley 470 | 9/2: rev $1.55B vs $1.48B; EPS $0.62 vs $0.45; guide raised (FY27 product revenue $6.07B from $5.84B, margin 14.5%, $3.7B buyback) | +16.55%, +7.57% | up/up | $1.20B vs -$1.09B; SBC 30.2% | AI data workloads lift product growth to 36-38% with margin expansion | DDOG, PLTR; GM 66.6-67.8% flat; fwd P/E 110 vs 87/84; EV/S 21.8 vs 22.3/73.7 | none | $555.8M, 9 sellers; Slootman $308M and Dageville $142M under 10b5-1; Garrett $17.5M and Beaulier $4.4M not under a plan | 889/503; Engineers Gate +434%, Styrax new, NPS +3.3% | 5.59%, 2.6, 9/15 | +5.8/+48.8; yes; vs SPY +5.2/+42.6, vs XLK -1.8/+41.6; trend_up; held | Q3 FY27 earnings ~12/2 (estimated) | n/a |

- Judgment (analyst call): prospect 7: product revenue guide raised to $6.07B with margin expansion; competition 4: GM ~67% flat; fwd P/E 110; macro 1: AI software archetype 1: SBC 30% of revenue; narrative 3: cloud and AI software fading.
- Avg target: 425.19 · https://stockanalysis.com/stocks/snow/forecast/ · 2026-09-24
- Revenue actual: 1550000000.0 · https://www.marketbeat.com/stocks/NYSE/SNOW/earnings/ · 2026-09-24
- Guide: raised · https://www.sec.gov/Archives/edgar/data/0001640147/000164014726000033/fy2027q2earnings.htm · 2026-09-24
- Revisions 90d: up · https://www.zacks.com/stock/quote/SNOW/detailed-earning-estimates · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=SNOW · 2026-09-24
- Holders up: 889 · https://www.marketbeat.com/stocks/NYSE/SNOW/institutional-ownership/ · 2026-09-24

### STLN

Tier no_runway; total 51; gates failed: none.

Research row: | STLN | $6.51 / 7.13-2.32 / -8.7% | Strong Buy / 5 | $9.00 | $11 / $7 | +38.2 | B. Riley $8→11, Needham $7 (8/7); BTIG $8→9 (7/16); Lake St init $10 (7/6) | 8/6: rev $161.3M vs $155.3M; EPS -0.08 vs -0.07; FY rev **raised** to $650-670M | +28.5%, +29.3% (held) | n/a | FCF TTM -$3.3M vs NI -$36M; H1 FCF positive. **Cash $41.1M; generating cash (FY FCF guide +$5-15M); debt $79.9M (OrbiMed)** | Case: value-based oncology plus specialty pharmacy; adj. EBITDA positive in Q2; capitation expanding beyond Florida | PRVA, AGL; GM 14.5%; EV/S 1.2 | 10% owner Chernett: $78K (8/14), $95K (7/21), $88K (7/10) | Director Hively $1.95M (8/21, about 42% of his stake); CMO Podnos $150K (exercise-and-sell) | TTM 74/22; adds State St 1.55M sh, Formula Growth 300k | 7.5% (Finviz 11.1%), DTC 7.4, 9/15 | +9.0% / +51%; 50>200; RS 1m +3.2 / 3m +22.7; trend_up; gap held | Q3 print about early Nov (est.); no binary events | n/a |

- Judgment (analyst call): prospect 5: value-based oncology; FY revenue raised to $650-670M; competition 3: GM 14.5%, EV/S 1.2; macro 3: small cap with OrbiMed debt; narrative 3: outside the themes.
- Avg target: 9.0 · https://stockanalysis.com/stocks/stln/forecast/ · 2026-09-24
- Revenue actual: 161.28 · https://www.marketbeat.com/stocks/NASDAQ/STLN/earnings/ · 2026-08-06
- Guide: raised · https://www.sec.gov/Archives/edgar/data/0001799191/000107997326001006/ex99x1.htm · 2026-08-06
- Revisions 90d: None · None · None
- Insider coverage: True · https://finviz.com/quote.ashx?t=STLN · 2026-09-24
- Holders up: 74 · https://www.marketbeat.com/stocks/NASDAQ/STLN/institutional-ownership/ · 2026-09-24

### ISRG

Tier no_runway; total 51; gates failed: upside.

Research row: | ISRG | 399.52 / 603.88-328.57 / -33.8% | Buy / 32 | 476.34 (MB 508.68) | 685 / 324 | 19.2 | Oppenheimer upgrade to Outperform 500; BNP upgrade; HSBC downgrade to Hold 391; UBS initiated Neutral 500; TD Cowen rating conflicts between sources | 07-16: rev 2.89B vs 2.83B; EPS 2.80 vs 2.48; guide held (procedure growth 13.5-15.5% not raised) | -14.2%, -16.1% | flat / up (10.47→10.74) | 3.22B vs 3.14B (1.03); SBC 7.5% | Case: da Vinci 5 cycle and low penetration (3.2M of about 9M procedures) keep mid-teens growth | MDT, SYK; GM 66.4→66.4→66.1→67.8; fwd P/E 35.4 vs 14.9/17.1; EV/S 12.3 vs 3.5/4.5 | none | $4.9M, every sale under a 10b5-1 plan (Guthart $4.0M, Brosius many small sales, Widman, Loeb, Ladd) | 1616/1003 (TTM); only small named holders visible | 2.31%, 2.7d, 09-15 | +7.4%/0.0%; 50<200; RS +7.3/-4.5 vs SPY, +10.5/-9.2 vs XLV; base; down-gap held for weeks, now +15.7% above the print-day close | Q3 10-20 (estimate) | Procedure growth slowed (GLP-1 cut bariatric cases), Medtronic Hugo cleared by FDA, Q2 beat without a guide raise |

- Judgment (analyst call): prospect 5: procedure growth held at 13.5-15.5%; not raised; competition 5: GM ~66-68% stable; Medtronic Hugo cleared; macro 3: long duration 1 plus 2: net cash, FCF 1.03x NI; narrative 4: AI health accelerating.
- Avg target: 476.34 · https://stockanalysis.com/stocks/isrg/forecast/ · 2026-09-24
- Revenue actual: 2890000000.0 · https://www.marketbeat.com/stocks/NASDAQ/ISRG/earnings/ · 2026-09-24
- Guide: held · https://www.fool.com/investing/2026/09/24/intuitive-surgical-stock-has-plunged-29-this-year/ · 2026-09-24
- Revisions 90d: up · https://www.zacks.com/stock/quote/ISRG/detailed-earning-estimates · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=ISRG · 2026-09-24
- Holders up: 1616 · https://www.marketbeat.com/stocks/NASDAQ/ISRG/institutional-ownership/ · 2026-09-24

### GOOGL

Tier no_runway; total 49; gates failed: none.

Research row: | GOOGL | 342.36 / 408.61-235.84 / -16.2% | Strong Buy / 62 | 428.41 | 515/340 | +25.1 | Evercore target 420→450; Tigress 415→485; Bernstein Hold 390→385; Morgan Stanley 400 | 7/22: rev $119.80B vs $117.07B; EPS $9.11 vs $2.89 (investment gains); guide none (company policy); 2026 capex raised to $195-205B | -7.13%, -2.46% | flat/up | $53.3B vs $244.2B; SBC 6.3% | Google Cloud (+82%, $514B backlog) and Gemini make money from AI while Search holds | MSFT, META; GM 59.6-62.5% rising; fwd P/E 22.6 vs 21.2/22.9; EV/S 9.1 vs 11.3/8.8 | none | $3.5M, 3 sellers, all 10b5-1 | 3756/3288; State St +5.6% | 0.81%, 3.5, 9/15 | -0.6/+1.3; yes; vs SPY -1.5/-4.9, vs XLC -2.1/-8.4; base; not held | Q3 earnings ~10/28 (estimated) | n/a |

- Judgment (analyst call): prospect 6: Cloud +82% with a $514B backlog in the last print; competition 6: GM 59.6 to 62.5% rising; fwd P/E 22.6; macro 4: quality megacap 4; narrative 5: Mag 7 accelerating; internet platforms fading.
- Avg target: 428.41 · https://stockanalysis.com/stocks/googl/forecast/ · 2026-09-24
- Revenue actual: 119800000000.0 · https://www.marketbeat.com/stocks/NASDAQ/GOOGL/earnings/ · 2026-09-24
- Guide: none · https://www.cnbc.com/2026/07/22/google-earnings-q2-goog-live-updates.html · 2026-09-24
- Revisions 90d: up · https://www.zacks.com/stock/quote/GOOGL/detailed-earning-estimates · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=GOOGL · 2026-09-24
- Holders up: 3756 · https://www.marketbeat.com/stocks/NASDAQ/GOOGL/institutional-ownership/ · 2026-09-24

### CRM

Tier no_runway; total 49; gates failed: upside.

Research row: | CRM | $238.22 (9/24) / 269.11-146.32 / -11.5% | Buy / 54 | $281.08 (MB $275.14) | $475 / $160 | +18.0% | Wolfe upgraded to Outperform (8/27). Target raises from Barclays, JPM, Truist, Argus, Guggenheim, Stifel, BMO, Canaccord, Mizuho, UBS, Wells. No downgrades | Q2 FY27 on 8/26: rev $11.35B vs $11.33B; non-GAAP EPS $5.90 vs $3.27 (inflated by investment gains). FY27 rev guide raised $200M to $46.1-46.4B | +22.6% / +28.6% | n/a / n/a (sources failed) | FCF $15.15B vs NI $9.66B; SBC n/a | Agentforce (ARR >$1.5B) keeps cRPO at ~14%, and the $25B ASR re-rates a 15x P/E | NOW, ADBE. GM 78.0% to 76.7%, drifting down. Fwd P/E 14.8 vs NOW 27.5, ADBE 8.6; EV/S 5.2 vs 9.9 / 3.6 | Dir Kirk $1.0M on 9/18 (P, not 10b5-1, EDGAR-verified; his 3rd buy since Dec-25) | Dir Conway $1.17M (9/4) | TTM: 2,003 up / 1,565 down. Andra +4,855% (small). Net n/a | 3.66%, 2.09, date n/a | +12.1% / +18.3%; 50 above 200. RS 1m +15.7 / +8.7; 3m +54.1 / +53.1. Trend up; gap held | ASR final settlement Oct-26. Q3 FY27 est. 12/2. Contentful and Fin deals closing | n/a |

- Judgment (analyst call): prospect 5: Agentforce and a guide raise; the EPS beat is investment gains; competition 4: GM drifting; fwd P/E 14.8; macro 5: quality megacap 4 plus 1: FCF 1.6x NI and a $25B ASR; narrative 3: cloud software fading.
- Avg target: 281.08 · https://stockanalysis.com/stocks/crm/forecast/ · 2026-09-18
- Revenue actual: 11350000000.0 · https://www.marketbeat.com/stocks/NYSE/CRM/earnings/ · 2026-09-24
- Guide: raised · https://www.salesforce.com/news/press-releases/2026/08/26/fy27-q2-earnings/ · 2026-08-26
- Revisions 90d: None · None · None
- Insider coverage: True · https://finviz.com/quote.ashx?t=CRM · 2026-09-24
- Holders up: 2003 · https://www.marketbeat.com/stocks/NYSE/CRM/institutional-ownership/ · 2026-09-23

### COHR

Tier no_runway; total 48; gates failed: none.

Research row: | COHR | 290.61 / 440.00–102.14 / -34.0% | Buy / 23; MB Mod Buy 22 | 415.36 (MB 397.63) | 500 / 280 | +42.9 | 11 actions. Post-print raises: Needham and Jefferies to 420, MS 330→375, B.Riley 309→345. DB initiated Buy 400; Oppenheimer upgrade (MB label) | 8/12: $2,046M vs $1,980M; $1.74 vs $1.43. Guide raised: Q1 FY27 midpoints about +7% revenue and +10% EPS vs consensus | -8.0% / -18.5% | flat / up (9.42 vs 9.41 vs 8.17) | FCF -$1.02B vs NI $770M (capex $1.1B); SBC 2.6% | AI datacom transceivers and lasers. FY27 revenue $10.6B (+49%), EPS $9.42 | LITE, AAOI. GM 36.6→37.0→37.7→38.5 (rising). Fwd P/E 20.7 vs LITE 27.4 and AAOI 18.2 | none | $8.5M across 9 sales by 6 sellers (directors, CFO, CTO). 6 marked 10b5-1 | 709/277 no: 709/359. Adds: NPS +2907%, Amundi +142%, UBS AM +65%. Cut: Wellington -34% | 5.22%, 1.7d, 9/15 | -2.0% / +1.8%; 50>200 yes. RS vs XLK: 1m -6.3, 3m -34.1. Base. Gap held: no | Q1 about 11/4 (estimate) | Sector reset (-11% on 7/28), then -18% in the 5 days after a beat-and-raise |

- Judgment (analyst call): prospect 6: datacom transceivers in the beat and raise; FY27 revenue +49% consensus; competition 5: GM 36.6 to 38.5% rising; fwd P/E 20.7 below LITE 27.4; macro 2: AI networking 1 plus 1: positive EPS at 20x softens the duration hit; narrative 1: AI networking and optics lagging and worsening.
- Avg target: 415.36 · https://stockanalysis.com/stocks/cohr/forecast/ · 2026-09-23
- Revenue actual: 2046.0 · https://www.marketbeat.com/stocks/NYSE/COHR/earnings/ · 2026-08-12
- Guide: raised · https://finance.biggo.com/news/08422f07-26d3-4da7-b252-6cc2c3b3b58d · 2026-08-12
- Revisions 90d: up · https://finance.yahoo.com/quote/COHR/analysis/ · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=COHR · 2026-09-24
- Holders up: 709 · https://www.marketbeat.com/stocks/NYSE/COHR/institutional-ownership/ · 2026-09-24

### CCJ

Tier no_runway; total 46; gates failed: insider, delivery.

Research row: | CCJ | 88.12 / 135.24-77.70 / -34.8% | Buy / 21 (19-2-0) | 127.77 | 170.86 / 83.99 | 45.0 | Jefferies init Buy $190; Truist 129→130; BofA cut 140→133; Scotia $125; Stifel $129 | 07-31: rev $573M vs $580M, EPS 0.13 vs 0.26 (both missed); guide **held** | -2.1% / +10.4% | flat (0/0) / n/f | FCF C$556M vs NI C$355M; SBC 0.3% | Term uranium near $90/lb plus Westinghouse new-build; EPS ~C$1.47→2.60 | Kazatomprom, NXE; GM 37→32% (volatile); fwd P/E 48.8, EV/S 15.3 | coverage unknown (SEDI filer) | coverage unknown | +5.12M; 525/461; 127/100; MFS +50%, BMO +23%, RBC +14%; cut FMR -14% | 2.00% (SA 1.87%), 2.71, n/f | -7.0% / -16.7%; no; vs SPY -18/-19, vs XLE -19/-31; trend_down; gap held yes | Q3 ~10-30 (estimated); Cigar Lake restart (no date) | Cigar Lake mill halt, McArthur River disruption, Westinghouse EBITDA $163M vs $352M, Q2 miss |

- Judgment (analyst call): prospect 4: term uranium near $90/lb; Cigar Lake halt is ahead of a restart; competition 4: GM 37 to 32% volatile; macro 1: nuclear archetype 1; narrative 1: nuclear lagging and worsening.
- Avg target: 127.77 · https://stockanalysis.com/stocks/ccj/forecast/ · 2026-09-24
- Revenue actual: 573060000.0 · https://www.marketbeat.com/stocks/NYSE/CCJ/earnings/ · 2026-09-24
- Guide: held · https://www.ad-hoc-news.de/boerse/news/nebenwerte/cameco-stock-falls-as-uranium-trade-cools-but-guidance-stays-intact/70018415 · 2026-09-24
- Revisions 90d: None · None · None
- Insider coverage: False · https://finviz.com/quote.ashx?t=CCJ · 2026-09-24
- Holders up: 525 · https://api.nasdaq.com/api/company/CCJ/institutional-holdings?limit=15&type=TOTAL&sortColumn=marketValue · 2026-09-24

### MU

Tier no_runway; total 46; gates failed: upside, insider.

Research row: | MU | 1080.53 (09-24) / 1255.00-154.65 / -13.9% | Strong Buy / 49 | 1515 (MB 1341.87) | 2200 / 361 | 40.2 (MB 24.2) | 09-23 to 24: Rosenblatt 1500, Wolfe 1500, UBS 1625, WFC 1525→1400, Citi 1150→1300 (all Buy) | 06-24: rev 41.46B vs 35.91B, EPS 25.11 vs 21.39; raised (FQ4 guide about $50B vs about 43.5B consensus) | +15.7% / -7.0% | up / up (FY27 column: 159.12 vs 155.80 30 days ago, 148.74 90 days ago) | 26.2B vs 50.5B (0.52); SBC 1.3% | Case: HBM/DRAM shortage keeps pricing at records; revenue 130B (FY26) to 248B (FY27) | SKHY, SNDK; GM 44.7→56.0→74.4→84.6; fwd P/E 6.8 vs 5.5 / 6.7; EV/S 13.3 vs 10.2 / 12.5 | none | 10 sales, $182.2M; CEO Mehrotra about $122M under 10b5-1; 4 sales without a plan (Sadana $14.0M, Dugle, Allen, Bjorlin) | quarter end 06-30; net n/a; up/down 2462/1246 (TTM); new/exit n/a; State Street trimmed 4.1% | 2.45%, 1.1d, 09-15 (Finviz 2.64%) | +15.3% / +64.5%; 50>200 yes; RS vs SPY +15.7/-15.4, vs XLK +8.7/-16.5; trend_up; gap not held | **09-30 FQ4 earnings, company-confirmed** (GlobeNewswire 08-26; call 2:30pm MT) | n/a (<30%) |

- Judgment (analyst call): prospect 7: HBM and DRAM pricing is in the last two prints: FQ3 beat by 15% on revenue, FQ4 guide ~$50B vs $43.5B; competition 5: GM 44.7 to 84.6% on pricing, cyclical not structural; fwd P/E 6.8 at peak margins; macro 4: materials/industrials 4; narrative 5: memory improving with attention heating into the 30 Sep print.
- Avg target: 1515.0 · https://stockanalysis.com/stocks/mu/forecast/ · 2026-09-24
- Revenue actual: 41460000000.0 · https://www.marketbeat.com/stocks/NASDAQ/MU/earnings/ · 2026-09-24
- Guide: raised · https://www.cnbc.com/2026/06/24/micron-mu-earnings-report-q3-2026.html · 2026-06-24
- Revisions 90d: up · https://finance.yahoo.com/quote/MU/analysis/ · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=MU · 2026-09-24
- Holders up: 2462 · https://www.marketbeat.com/stocks/NASDAQ/MU/institutional-ownership/ · 2026-09-24

### SKHY

Tier no_runway; total 46; gates failed: flow, insider, delivery.

Research row: | SKHY | $186.37 (9/24) / 199.87-124.80 / -6.8% | Strong Buy / 15 (ADR) | $248.43 (MB $253.22) | $355 / $152 | +33.3% | Wolfe raised to $250 (9/23), BofA to $268 (9/14), JPM initiated OW $245 (9/9), Citi upgraded (9/2), Needham raised to $220. 8/4 initiation wave: Rosenblatt $320, Cantor $300, Stifel $240, RBC $200 | Q2 on 7/29 (KRW): rev 79.32T vs 84T LSEG (miss); op profit 60.5T vs 64T. ADR EPS $8.76 vs $5.12 (MB). No numeric guide by policy | ADR -2.6% / +16.0% (low-confidence history); Seoul -9.6% | flat / up (KRW FY26 EPS +13.8% over 90d) | FCF $67.0B vs NI $104.6B (non-operating gains); SBC not disclosed | HBM3E/HBM4 leadership: revenue KRW 347T to 534T at ~5x fwd P/E | MU, SNDK (Samsung not US-listed). GM 57% to 83%. Fwd P/E 5.5 vs MU 6.8, SNDK 6.7 | n/a, foreign issuer | n/a, foreign issuer | No 13F yet: listed 7/10, after the Q2 quarter-end | 4.57% (SA), 0.84, date n/a | +14.2% / +13.7%; 50 marginally below 200. 1m RS +16.7 vs SPY, +9.7 vs XLK. Breakout (+23.6% on 9/21); gap held | Q3 results (date n/a). First 13F cycle by 11/16. HBM4 ramp in H2 | n/a |

- Judgment (analyst call): prospect 7: HBM3E/HBM4 leadership; revenue KRW 347T to 534T; competition 5: GM 57 to 83%; fwd P/E 5.5; macro 4: materials/industrials 4; narrative 5: memory improving.
- Avg target: 248.43 · https://stockanalysis.com/stocks/skhy/forecast/ · 2026-09-23
- Revenue actual: 79320000000000.0 · https://news.skhynix.com/en/q2-2026-business-results/ · 2026-07-29
- Guide: none · https://news.skhynix.com/en/q2-2026-business-results/ · 2026-07-29
- Revisions 90d: up · https://finance.yahoo.com/quote/000660.KS/analysis/ · 2026-09-24
- Insider coverage: None · None · None
- Holders up: None · None · None

### PYPL

Tier no_runway; total 46; gates failed: upside.

Research row: | PYPL | 52.60 / 79.21–38.46 / -33.6% | Hold / 43 (MB 47, $56.03) | $57.07 | $80 / $36 | +8.5 | 23 actions. Target raises after the print (to $57–70); cuts in late Aug (Mizuho 51, Truist 53, Loop 50). Jefferies up to Buy 7/28. Wells to $61 on 9/24 | 7/28: rev $8.68B vs $8.47B; EPS $1.38 vs $1.28. Raised FY EPS to about $5.38 and TM$ to about $15.6B | +4.0% / +4.4% | flat / flat (5.39 vs 5.38 vs 5.30; 36 up, 3 down) | FCF $6.59B vs NI $4.90B; SBC 2.9% | Case: turnaround at 9x EPS. TM$ growth returns, Venmo monetizes, about $6B FCF funds buybacks | XYZ, V. GM 39.6/40.3/41.4/40.7 (drifting down). Fwd P/E 9.1 vs XYZ 14.6, V 24.5 | none | 6 small 10b5-1 sales, $0.85M (CAO, two presidents) | 960 / 906. Adds: BlackRock, Norges, BofA. Sells: Amundi, Clearbridge, Coatue | 3.45%, 2.7d, 9/15 | -7.4% / +4.2%; 50>200 yes; RS SPY -15.7/+19.6, XLF -9.1/+22.1; base; gap held | Q3 print about 10/27 (est.) | Slowing growth and checkout competition; cautious Q1 outlook (-7.7% on 5/5) |

- Judgment (analyst call): prospect 4: turnaround at 9x EPS; guide raised; competition 4: GM 39.6 to 40.7% drifting; macro 5: cash-flow value: FCF 1.35x NI, buybacks; narrative 3: fintech fading.
- Avg target: 57.07 · https://stockanalysis.com/stocks/pypl/forecast/ · 2026-09-24
- Revenue actual: 8680000000.0 · https://www.marketbeat.com/stocks/NASDAQ/PYPL/earnings/ · 2026-09-24
- Guide: raised · https://finance.yahoo.com/markets/stocks/articles/paypal-q2-2026-earnings-beat-124337219.html · 2026-09-24
- Revisions 90d: flat · https://finance.yahoo.com/quote/PYPL/analysis/ · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=PYPL · 2026-09-24
- Holders up: 960 · https://www.marketbeat.com/stocks/NASDAQ/PYPL/institutional-ownership/ · 2026-09-24

### ALAB

Tier no_runway; total 46; gates failed: upside, insider.

Research row: | ALAB | $360.51 (9/24) / 499.48-97.89 / -27.8% | Buy / 26 | $389.95 (MB $348.33, stale 8/18) | $500 / $190 | +8.2% | Northland upgraded to OP $350 (8/17). Post-print raises: Citi $430, Evercore $452, RBC $500, Jefferies $450, Needham $425. TD Cowen cut to $375 (Hold). Susquehanna Neutral $310 (9/12) | Q2 on 8/4: rev $392.4M vs $360.9M, EPS $0.80 vs $0.69. Q3 guide $540-560M vs $410M: raised | -12.0% / -11.9% | n/a / up (derived: Q3 EPS $0.59 pre-print to $1.19 now) | FCF $277M vs NI $369M (0.75); SBC not found | Scorpio fabric switches plus retimers ride rack scale-up: revenue $1.9B to $3.0B | CRDO, MRVL (and AVGO). GM 76.3% to 73.3%, falling. Fwd P/E 56 vs CRDO 20, MRVL 38; EV/S 51 vs 23-24 | none | ~$210M from 5 insiders: Alba $132M (7/1, 9/1), CEO Mohan $30.8M, COO $30.8M (8/17), Dyckerhoff monthly, GC | TTM: 605 up / 257 down. NPS -20.6%. Net n/a | 6.33% (SA 5.79%), 2.04, date n/a | +18.5% / +53.2%; 50 above 200. RS 1m +27.4 / +20.4; 3m -13.9 / -14.9. Recovering (trend_up); down gap held (false) | Q3 est. 11/3 (unconfirmed) | n/a (<30%) |

- Judgment (analyst call): prospect 6: Q3 guide $540-560M vs $410M; competition 4: GM 76.3 to 73.3% falling; fwd P/E 56; macro 1: AI networking 1; narrative 1: AI networking lagging.
- Avg target: 389.95 · https://stockanalysis.com/stocks/alab/forecast/ · 2026-09-14
- Revenue actual: 392400000.0 · https://www.marketbeat.com/stocks/NASDAQ/ALAB/earnings/ · 2026-09-24
- Guide: raised · https://www.marketbeat.com/stocks/NASDAQ/ALAB/earnings/ · 2026-09-24
- Revisions 90d: up · https://www.marketbeat.com/stocks/NASDAQ/ALAB/earnings/ · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=ALAB · 2026-09-24
- Holders up: 605 · https://www.marketbeat.com/stocks/NASDAQ/ALAB/institutional-ownership/ · 2026-09-23

### ARM

Tier no_runway; total 46; gates failed: upside.

Research row: | ARM | 306.34 / 452.70-100.02 / -32.3% | Buy / 43 | 288.71 | 500 / 125 | -5.8 | MS Hold 212; Bernstein 500→480; Piper init Buy 320; RJ 244→272; Mizuho Buy 400 | 07-29: $1.29B vs $1.26B, $0.45 vs $0.40; guide raised (EPS $0.43-0.51 vs $0.39) | +7.4% / +27.5% | flat / up | FCF $1.51B vs NI $1.04B (1.44x); **SBC 22.4%** | The case: royalty uplift and data-center share; FY28 revenue $8.24B (+36%) | QCOM, INTC; GM ~97-98% flat; fwd P/E 99.9 vs 19.2 / 60.1; EV/S 62.8; RISC-V substitute | none | CFO Child 2 sales, $5.8M | MB 427 / 225 TTM; inst own 7.5% | 1.57% / 3.07d / n/f | +16.3% / +45.2%, yes; RS 1m +26.7 / +19.7, 3m -16.4 / -17.4; breakout (-7.9% on 09-24); gap held | Q2 ~11-04 (est.) | July -34%: semis selloff, HSBC cut to Hold (TSMC 3nm, valuation); 09-24 Oracle Jupiter force majeure plus profit-taking |

- Judgment (analyst call): prospect 5: royalty uplift is in the raised guide, data-center share is still a story; competition 3: GM flat ~97%; RISC-V substitute named; fwd P/E ~100 vs QCOM 19; macro 3: quality megacap 4, minus 1: ~100x forward earnings is long duration at 2.76% real yields; narrative 3: semis improving; the stock sits above its consensus target.
- Avg target: 288.71 · https://stockanalysis.com/stocks/arm/forecast/ · 2026-09-24
- Revenue actual: 1.29 · https://www.marketbeat.com/stocks/NASDAQ/ARM/earnings/ · 2026-07-29
- Guide: raised · https://www.marketbeat.com/stocks/NASDAQ/ARM/earnings/ · 2026-07-29
- Revisions 90d: up · https://finance.yahoo.com/quote/ARM/analysis/ · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=ARM · 2026-09-24
- Holders up: 427 · https://www.marketbeat.com/stocks/NASDAQ/ARM/institutional-ownership/ · 2026-09-24

### SE

Tier no_runway; total 43; gates failed: insider, delivery.

Research row: | SE | 100.73 / 193.48–77.05 / -47.9% | Strong Buy / 29 (MB 14, $149.40) | $157.11 | $195 / $105 | +56.0 | 11 actions. RBC and Arete upgraded (early Sep). Barclays, JPM, Benchmark raised targets. TD Cowen Hold $115 | 8/11: rev $7.79B vs $7.12B; EPS $0.70 vs $0.86 (miss). Held: GMV about +25%, Shopee about $1B EBITDA | +14.6% / +1.3% (gave back about 90%) | flat / down (Zacks, 2 estimates: 3.79 / 3.79 / 4.24) | FCF $4.21B vs NI $1.64B; SBC n/a | Case: Shopee +48%, Monee loans +62%, EPS +36% in 2027 | MELI, PDD. GM 45.6/44.3/43.8/43.4. Fwd P/E 21.2 vs MELI 32.4, PDD 6.4 | none seen | 94 sales, about $276M seen since 8/11: CEO Li $147M (the $137M on 8/11 was 10b5-1), COO $70M, CPO $32M, President $11M, CFO $5M | 89 / 44 (thin). Adds: OCBC, Norges, WCM | 1.79%, 3.2d, 9/15 | -9.3% / -2.9%; 50>200 yes; RS SPY -18.4/+8.7, XLY -11.8/+15.8; trend_down; gap barely held | Q3 print about 11/10 (est.); 11.11 | TikTok Shop share gains (Vietnam 52% vs 64%), reinvestment cuts, EPS misses, executive selling |

- Judgment (analyst call): prospect 5: Shopee +48% and Monee loans +62% are reported; EPS misses; competition 3: TikTok Shop taking share in Vietnam; macro 3: EM archetype 3; narrative 2: consumer lagging; heavy executive selling.
- Avg target: 157.11 · https://stockanalysis.com/stocks/se/forecast/ · 2026-09-24
- Revenue actual: 7790000000.0 · https://www.marketbeat.com/stocks/NYSE/SE/earnings/ · 2026-09-24
- Guide: held · https://www.investing.com/news/transcripts/earnings-call-transcript-sea-limited-tops-revenue-forecasts-in-q2-2026-93CH-4851797 · 2026-09-24
- Revisions 90d: down · https://www.zacks.com/stock/quote/SE/detailed-earning-estimates · 2026-09-24
- Insider coverage: None · None · None
- Holders up: 89 · https://www.marketbeat.com/stocks/NYSE/SE/institutional-ownership/ · 2026-09-24

### ABCL

Tier no_runway; total 43; gates failed: delivery.

Research row: | ABCL | $12.65 / 13.18-2.74 / -4.0% | Strong Buy / 9 | $17.13 | $30 / $9 | +35.4 | GS init Hold $13 (9/24); Truist Buy $30 (9/2); BMO $15 (8/18); JonesTrading $25 (8/10); Piper $12 (8/7) | 8/5: rev $4.05M vs $7.85M (miss); EPS -0.18 vs -0.16 (miss); no guide | +10.3%, +85% (ABCL635 data on 8/10) | n/a | FCF TTM -$120M vs NI -$165M; SBC 77%. **Cash $540M at 6/30 plus $200M gross offering; underlying burn about $41M/q; runway about 18q** | Case: single-dose ABCL635 met both Phase 2 VMS endpoints; TCE deals with Jazz ($84M) and Vertex ($28M) | Astellas Veozah, Bayer Lynkuet; EV/S 55 | none | none (Finviz table empty) | TTM 77/29; adds HighTower, Headlands; exit Alyeska -80% | 15.5% (Finviz 13.4%), DTC 9.6, 9/15 | +32% / +123%; 50>200; RS 1m +1.0 / 3m +85.5; trend_up; gap held | IMS full Phase 2 data 9/30-10/3 (confirmed); Q3 about 11/5 (est.); ABCL575 Phase 1 topline Q4-26. **Offering: $200M at $9.75 on 8/11** | n/a |

- Judgment (analyst call): prospect 3: ABCL635 Phase 2 hit; the IMS readout 30 Sep to 3 Oct is binary; competition 3: Veozah and Lynkuet already on market; macro 1: long duration; SBC 77% of revenue; narrative 3: the stock is +123% vs its 200-day on the data.
- Avg target: 17.13 · https://stockanalysis.com/stocks/abcl/forecast/ · 2026-09-24
- Revenue actual: 4.05 · https://www.marketbeat.com/stocks/NASDAQ/ABCL/earnings/ · 2026-08-05
- Guide: none · https://www.sec.gov/Archives/edgar/data/1703057/000170305726000044/q22026earningspressrelease.htm · 2026-08-05
- Revisions 90d: None · None · None
- Insider coverage: True · https://finviz.com/quote.ashx?t=ABCL · 2026-09-24
- Holders up: 77 · https://www.marketbeat.com/stocks/NASDAQ/ABCL/institutional-ownership/ · 2026-09-24

### GS

Tier no_runway; total 43; gates failed: none.

Research row: | GS | 923.29 / 1153.99–740.01 / -20.0% | Hold / 25 (MB 24, $1,055.71) | $1,142 | $1,325 / $730 | +23.7 | 8 actions. Citi cut 1,200 to 1,050 (9/23). HSBC upgrade (date conflicts between sources). Barclays $1,245, Jefferies $1,299 | 7/14: rev $20.34B vs $16.22B; EPS $20.98 vs $14.47. Guide: none (policy). CEO warned 9/16 of softer FICC and non-comp costs up more than $500M | +9.0% / +3.8% | flat / up (Zacks 69.64 / 68.89 / 59.99; Q3 cut this week) | FCF n/m (-$41.5B) vs NI $19.98B; SBC 5.1% | Case: record capital-markets cycle, FY26 EPS about $70 (+36%) | MS, JPM. GM n/m. Fwd P/E 12.6 vs MS 14.3, JPM 13.5 | none (GS-as-owner rows excluded) | CAO Leslie $1.09M (not 10b5-1) | 2,056 / 1,370. Adds: Kingstone, BlackRock. Sells: Dodge & Cox (small) | 2.39%, 3.9d, 9/15 | -9.8% / -3.7%; 50>200 yes; RS SPY -13.0/-17.8, XLF -6.3/-15.3; breakdown; gap held (faded) | Q3 print 10/13 BMO (Finviz, not confirmed) | n/a (<30%) |

- Judgment (analyst call): prospect 5: record capital markets in the last print; CEO warned on FICC; competition 5: fwd P/E 12.6 in line with MS and JPM; macro 3: banks 4 minus 1: bear-flattening curve; narrative 1: banks lagging and worsening; a corpus account is short.
- Avg target: 1142 · https://stockanalysis.com/stocks/gs/forecast/ · 2026-09-24
- Revenue actual: 20340000000.0 · https://www.marketbeat.com/stocks/NYSE/GS/earnings/ · 2026-09-24
- Guide: none · https://www.investing.com/news/stock-market-news/goldman-sachs-stock-falls-after-ceo-warns-of-softer-trading-4904361 · 2026-09-24
- Revisions 90d: up · https://www.zacks.com/stock/quote/GS/detailed-earning-estimates · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=GS · 2026-09-24
- Holders up: 2056 · https://www.marketbeat.com/stocks/NYSE/GS/institutional-ownership/ · 2026-09-24

### AMKR

Tier no_runway; total 39; gates failed: delivery.

Research row: | AMKR | 52.69 / 96.68-28.03 / -45.5% | Buy / 11 | 76.4 | 92 / 65 | +45.0 | BofA init Buy 70; B.Riley Hold 75→65; GS Hold 65; MS Hold 69→70; Needham Buy 90 | 07-27: $1.90B vs $1.81B, $0.70 vs $0.47; guide cut on revenue (Q3 $2.0-2.1B vs $2.1B; EPS guide above) | **-24.7%** / -8.0% | flat / up | FCF **-$172M** vs NI $555M; SBC n/f | The case: AI advanced packaging and Arizona campus | TSM, INTC; GM 14-17% volatile; fwd P/E 19.2 vs 20.6 / 60.1 | none | 9 sales, $4.0M, 5 sellers (small) | MB 324 / 153 TTM; exits Baird -95%, Tidal -81%, Engineers Gate -75% | **16.28%** / 1.97d / n/f | -0.6% / -7.6%, **no**; RS 1m +8.0 / +1.1, 3m -42.9 / -44.0; base; gap not held | Q3 ~10-26 (est.) | -25% on 07-28: revenue guide below consensus (HBM shortages, timing) with capex held at $2.5-3.0B |

- Judgment (analyst call): prospect 3: AI packaging and Arizona are still ahead; Q3 revenue guide below consensus and FCF negative; competition 2: GM 14-17% volatile against TSM in-house packaging; share not gaining; macro 3: materials 4 minus 1: negative FCF with $2.5-3.0B capex into a hostile rate regime; narrative 2: semis improving but the name broke down 25% on its print.
- Avg target: 76.4 · https://stockanalysis.com/stocks/amkr/forecast/ · 2026-09-24
- Revenue actual: 1.9 · https://www.marketbeat.com/stocks/NASDAQ/AMKR/earnings/ · 2026-07-27
- Guide: cut · https://www.marketbeat.com/stocks/NASDAQ/AMKR/earnings/ · 2026-07-27
- Revisions 90d: up · https://query2.finance.yahoo.com/v10/finance/quoteSummary/AMKR?modules=earningsTrend · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=AMKR · 2026-09-24
- Holders up: 324 · https://www.marketbeat.com/stocks/NASDAQ/AMKR/institutional-ownership/ · 2026-09-24

### ADUR

Tier no_runway; total 37; gates failed: insider, delivery.

Research row: | ADUR | 12.56 / 18.19-9.00 / -31.0% | Strong Buy / 4 | 26.98 (MB 29.25) | 32.32 / 21.38 | 114.8 | HCW reiterated Buy 22 (09-22); Roth initiated Buy 30 (07-27/31) | 08-31 (FY Q4): rev C$0 vs 0.24M; EPS -0.27 vs -0.08; guide none (pre-revenue) | -3.5%, -4.1% | down / down (-0.37→-0.40, 2 estimates) | -14.7M vs -26.8M CAD; SBC n/m | Case: low-temperature HCT recycles mixed plastics at about 89-91% yield; licensing via a first commercial plant | PCT, LYB; GM n/m; fwd P/E n/m vs n/m/7.9; EV/S n/m | coverage unknown: Form 4 does not apply (MJDS foreign private issuer, 40-F/6-K); SEDI not checked | coverage unknown (same reason) | 15/1 (TTM); holdings tiny | 12.96% (MB 8.68%), 6.7d (MB 9.3), 09-15 | -18.6%/-12.8%; 50<200; RS -18.8/-17.3 vs SPY, -13.2/-4.5 vs XLI; trend_down; gap not held | Q1 FY27 about 10-15 (estimate); first commercial plant design and start of work targeted in 2026 | June US$15.64M offering at $15.20 plus a C$9.16M placement; wider FY26 loss (C$26.8M) |

- Judgment (analyst call): prospect 1: commercial plant not before 2028; competition 2: pre-revenue technology; macro 0: pre-revenue and diluting; narrative 1: outside the themes.
- Avg target: 26.98 · https://stockanalysis.com/stocks/adur/forecast/ · 2026-09-24
- Revenue actual: 0 · https://investors.adurocleantech.com/press-releases/press-releases-details/2026/Aduro-Clean-Technologies-Reports-Fourth-Quarter-and-Fiscal-Year-2026-Results-and-Provides-Business-Update/default.aspx · 2026-09-01
- Guide: none · https://investors.adurocleantech.com/press-releases/press-releases-details/2026/Aduro-Clean-Technologies-Reports-Fourth-Quarter-and-Fiscal-Year-2026-Results-and-Provides-Business-Update/default.aspx · 2026-09-01
- Revisions 90d: down · https://www.zacks.com/stock/quote/ADUR/detailed-earning-estimates · 2026-09-24
- Insider coverage: None · None · None
- Holders up: 15 · https://www.marketbeat.com/stocks/NASDAQ/ADUR/institutional-ownership/ · 2026-09-24

### META

Tier no_runway; total 37; gates failed: upside, insider, delivery.

Research row: | META | 777.59 (9/24) / 763.90-520.26 / new high | Strong Buy / 62 | 761.01 | 1000/580 | -2.1 | 9/24: Raymond James target 650→860, Citizens JMP 770→885, Tigress 995; BMO Hold 580, Wedbush Hold 650; 9/21 Wells Fargo target 640→796 on the Muse AI agent | 7/29: rev $60.80B vs $60.22B; EPS $6.18 vs $7.19 (miss: $2.4B legal charge, higher tax rate); guide held (Q3 revenue $61-64B; costs, capex and tax rate raised) | -7.95%, +0.73% vs pre-print | down/down | $41.0B vs $68.1B (60%); SBC 11.0% | Muse and Meta AI agents plus AI ad ranking keep revenue growth above 20% and pay for $130-145B of capex | GOOGL, PINS; GM 81.4-82.0% flat; fwd P/E 22.9 vs 22.6/7.8; EV/S 8.8 vs 9.1/2.3 | none | $82.7M, 9 sellers; Cox (Chief Product Officer) $55.0M; all but $1.7M under 10b5-1 plans | Net n/a; buyers/sellers 3968/2687 over 12 months; named: State St +4%, NPS +3.3%, Darsana new | 1.41%, 1.6, 9/15 | +26.6/+24.2; 50<200; vs SPY +36.2/+38.8; breakout; gap held (yes) | Q3 earnings ~10/28 (estimated) | n/a |

- Judgment (analyst call): prospect 7: AI ad ranking visible in +22% revenue; costs and capex raised; competition 6: GM ~81-82% flat; fwd P/E 22.9 in line; macro 4: quality megacap 4; narrative 5: Mag 7 accelerating, the outlook's top Mag 7 pick, but at a new high with the most longs in the corpus.
- Avg target: 761.01 · https://stockanalysis.com/stocks/meta/forecast/ · 2026-09-24
- Revenue actual: 60800000000.0 · https://www.marketbeat.com/stocks/NASDAQ/META/earnings/ · 2026-09-24
- Guide: held · https://www.sec.gov/Archives/edgar/data/1326801/000162828026050596/meta-06302026xexhibit991.htm · 2026-09-24
- Revisions 90d: down · https://www.zacks.com/stock/quote/META/detailed-earning-estimates · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=META · 2026-09-24
- Holders up: 3968 · https://www.marketbeat.com/stocks/NASDAQ/META/institutional-ownership/ · 2026-09-24

### AAOI

Tier no_runway; total 36; gates failed: delivery.

Research row: | AAOI | 101.03 / 233.67–18.50 / -56.8% | Buy / 6 (targets last updated 8/19); MB Hold 6 | 163.40 (MB 139.40) | 220 / 109 | +61.7 | 5 actions. Northland 58→120 and B.Riley 94→109 (both Hold). RJ 151→178. Needham cut 220→190 | 8/6: $191.9M vs $190.5M; $0.06 vs $0.015. Guide held: Q3 revenue $255–290M (above est), EPS $0.11–0.26 (midpoint below est) | +9.2% / +21.0% | down / down (0.68 vs 0.89 vs 0.89) | FCF -$900M vs NI -$57M; SBC 2.6% | 800G/1.6T transceivers. 2026 revenue $1.04B, 2027 $2.66B | COHR, LITE. GM 28.0→31.2→29.1→27.7 (flat to down). Fwd P/E 18.2 (Finviz) vs SA 43.9 | none | $6.7M across 7 sales by 3 sellers. 1 not under a plan ($3.5M) | Net not found. 12-month buyers/sellers 197/54. Add: UBS AM +50% | 15.13%, 2.0d, 9/15 | -9.5% / -5.3%; 50>200 yes. RS vs XLK: 1m -17.9, 3m -32.6. Downtrend. Gap held: yes | Q3 about 11/5 (estimate); ATM sales continuing | Photonics reset (-13% 6/23, -17% 7/2), then a second $600M ATM. Share count +49% y/y |

- Judgment (analyst call): prospect 3: 800G/1.6T ramp guided, EPS consensus cut 0.89 to 0.68; competition 2: GM flat-down 28-31%; serial ATM dilution; macro 1: long duration with negative FCF; narrative 1: AI networking and optics lagging and worsening.
- Avg target: 163.4 · https://stockanalysis.com/stocks/aaoi/forecast/ · 2026-08-19
- Revenue actual: 191.92 · https://www.marketbeat.com/stocks/NASDAQ/AAOI/earnings/ · 2026-08-06
- Guide: held · https://investors.ao-inc.com/news-releases/news-release-details/applied-optoelectronics-reports-second-quarter-2026-results · 2026-08-06
- Revisions 90d: down · https://finance.yahoo.com/quote/AAOI/analysis/ · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=AAOI · 2026-09-24
- Holders up: 197 · https://www.marketbeat.com/stocks/NASDAQ/AAOI/institutional-ownership/ · 2026-09-24

### CRWV

Tier no_runway; total 36; gates failed: insider, delivery.

Research row: | CRWV | 90.13 / 153.20-60.55 / -41.2% | Buy / 40 | 140.81 (MB 138.78) | 317 / 39 | 56.2 | JPM upgrade to Buy 125; UBS init Buy 120; Redburn init Sell 54; Bernstein Sell 74; Barclays Hold 105 | 8/11: rev $2.575B vs ~2.555B, EPS -1.14 vs -1.52; guide raised (FY26 $12.4-13.2B) | +19.3% / +0.6% | up / down | FCF -$13.7B vs NI -$1.9B; 8.2% | Backlog ~$104B + >$25B; 2027 revenue $26B | NBIS, ORCL; GM 65.9/65.5/67.6/73.0 (falling); EV/S 12.7 vs NBIS 50.3, ORCL 7.8 | none | about $777M visible (Magnetar $479M, CEO $194M weekly, CDO $70M); coverage incomplete | 667 / 150; State Street +140% | 15.8%, 2.4d, 9/15 | +5.5% / -2.2%; 50<200; +2.2/-13.2; base; gap faded | Q3 about 11/9 (est.); $500M convert option by about 10/1 | Insider and Magnetar selling, $640M/qtr interest, serial converts |

- Judgment (analyst call): prospect 4: ~$104B backlog is contracted; the 2027 revenue path needs financing; competition 2: GM 73.0 to 65.9% falling; 10x debt to equity; macro 0: the thesis needs the regime to change: $51.6B debt, $640M/quarter interest; narrative 1: neoclouds lagging.
- Avg target: 140.81 · https://stockanalysis.com/stocks/crwv/forecast/ · 2026-09-24
- Revenue actual: 2575 · https://www.marketbeat.com/stocks/NASDAQ/CRWV/earnings/ · 2026-08-11
- Guide: raised · https://trendspider.com/blog/coreweave-stock-q2-earnings-guidance-2026/ · 2026-08-11
- Revisions 90d: down · https://finance.yahoo.com/quote/CRWV/analysis/ · 2026-09-24
- Insider coverage: False · https://finviz.com/quote.ashx?t=CRWV · 2026-09-24
- Holders up: 667 · https://www.marketbeat.com/stocks/NASDAQ/CRWV/institutional-ownership/ · 2026-09-24

### NKE

Tier no_runway; total 33; gates failed: delivery.

Research row: | NKE | 35.99 (09-24) / 76.97-35.35 / -53.2% | Hold / 42 | 47.32 (MB 48.41) | 94 / 23 | 31.5 | 3 downgrades (Baird, Citi, Truist), 1 upgrade to Hold (Benchmark), 8 target cuts (UBS 42, Stifel 40, Oppenheimer 52); BMO initiated Underperform $30 | 06-30: rev 10.97B vs 10.85B; EPS 0.20 ex-tariff (GAAP 0.72 incl. $0.52 IEEPA benefit) vs 0.11; guide held (Q1 FY27 revenue down low-to-mid single digits) | +4.9%, +4.2% | down / down (FY27 1.82→1.68; 1 up/5 down) | 2.18B vs 3.11B (0.70); SBC 1.5% | Case: the "win now" reset returns revenue growth and FY28 EPS +34% | DECK, ONON; GM 42.2→40.6→40.5→50.1 (Q4 includes ~900bp tariff recovery); fwd P/E 21.2 vs 10.3/16.6; EV/S 1.19 vs 1.72/2.30 | none | 8 small sales, $0.77M, 7 under 10b5-1 plans (Montagne $0.2M not) | 1170 buyers/1011 sellers (TTM); Wellington -42% (-16.1M sh); State Street +4.0M, Amundi +2.4M | 7.30% (MB 5.84%), 3.1d, 09-15; SI +13% | -9.7%/-27.5%; 50<200; RS vs SPY -9.0/-16.5, vs XLY -2.4/-9.3; trend_down; gap held at +5d, since fully given back | Q1 FY27 10-01 (confirmed) | Weak demand, China share loss, tariffs, a guide for falling revenue, September downgrades, removed from the S&P 100 on 09-21 |

- Judgment (analyst call): prospect 2: the reset is a story; revenue guided down; competition 2: losing share to ONON and in China; macro 3: consumer discretionary 4 minus 1: oil above $85 hurts consumer; narrative 1: consumer discretionary lagging.
- Avg target: 47.32 · https://stockanalysis.com/stocks/nke/forecast/ · 2026-09-24
- Revenue actual: 10970000000.0 · https://www.marketbeat.com/stocks/NYSE/NKE/earnings/ · 2026-09-24
- Guide: held · https://www.sec.gov/Archives/edgar/data/0000320187/000032018726000076/q4fy26exhibit991er.htm · 2026-06-30
- Revisions 90d: down · https://finance.yahoo.com/quote/NKE/analysis/ · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=NKE · 2026-09-24
- Holders up: 1170 · https://www.marketbeat.com/stocks/NYSE/NKE/institutional-ownership/ · 2026-09-24

### AI

Tier no_runway; total 31; gates failed: upside.

Research row: | AI | 10.76 / 20.22-7.68 / -46.8% | Sell / 13 | 8.30 | 12/6 | -22.9 | 9/3: BofA Sell 8, D.A. Davidson Sell 7, UBS Hold 12, Canaccord and Northland Hold 10; 9/18 Morgan Stanley Sell 7 | 9/2: rev $52.38M vs $52.06M; EPS -$0.20 vs -$0.26; guide held (FY27 $210-240M reiterated; Q2 $51-55M). Siebel CEO again since 5/8/26 | +3.61%, +0.19% | up/up | -$156M vs -$446M; SBC 111% | Siebel's return and the sales restructuring hold revenue steady; bookings +73% q/q; FCF positive; $651M cash | PLTR, SNOW; GM 17-40% volatile; EV/S 4.7 vs 73.7/21.8 | none | $16.9M; CEO Siebel $15.5M ($13.8M under 10b5-1, $1.8M not); CFO $0.8M; former CEO Ehikian $0.5M | 145/63; Engineers Gate new; BofA +55% (Q1 filing) | 32.88%, 6.9, 9/15 | +8.0/+3.5; no; vs SPY +9.7/+18.5, vs XLK +2.8/+17.5; base; held | Q2 FY27 earnings ~12/2 (estimated) | FY26 revenue fell 36% to $250M through the sales reorganisation and the founder's health disruption |

- Judgment (analyst call): prospect 2: restructuring under the returning founder; revenue fell 36%; competition 1: GM 17-40% volatile against PLTR and SNOW; macro 1: long duration, SBC 111% of revenue; narrative 2: AI applications fading.
- Avg target: 8.3 · https://stockanalysis.com/stocks/ai/forecast/ · 2026-09-24
- Revenue actual: 52380000.0 · https://www.marketbeat.com/stocks/NYSE/AI/earnings/ · 2026-09-24
- Guide: held · https://www.sec.gov/Archives/edgar/data/1577526/000157752626000119/ex991-fy27xq1earnings.htm · 2026-09-24
- Revisions 90d: up · https://www.zacks.com/stock/quote/AI/detailed-earning-estimates · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=AI · 2026-09-24
- Holders up: 145 · https://www.marketbeat.com/stocks/NYSE/AI/institutional-ownership/ · 2026-09-24

### ASTS

Tier no_runway; total 30; gates failed: delivery.

Research row: | ASTS | 61.06 / 133.86-47.50 / -54.4% | Hold / 14 (5-7-2) | 79.61 | 108 / 42.5 | 30.4 | Berenberg init Buy $92; DB cut 106→93; UBS cut 80→78; Clear Street $115; W. Blair Hold | 08-10: rev $31.5M vs $34.5M, EPS -0.77 vs -0.32 (both missed); FY rev guide $150-200M (direction n/f) | +4.2% / -2.5% | down (0↑/4↓) / down (-1.51→-2.28) | FCF -$1.64B vs NI -$619M; SBC 128% | Direct-to-phone satellite broadband; 13 in orbit, company target ~45 in 2026; revenue $169M→$651M | SPCX Starlink direct-to-cell, Globalstar/Apple; GM 62.6→25.2% falling; EV/S 217 | director Cisneros 10,822 sh $619k (Form 4: P, not 10b5-1) | CTO Yao $2.36M, COO Gupta $0.71M (09-16) | +9.36M; 560/243; 180/102; MS +129%, Marex +136%, Jane Street new; **Rakuten -15.5M (-50%)** | 34.17% (SA 24.07%), 6.93, 2026-08-31 | -2.6% / -25.2%; no; vs SPY -2/-11, vs XLC -2/-15; base; gap held no | Q3 ~11-09 (estimated); BlueBird 14-16 launch (undated) | $1B convertible in July (-13%), Q2 miss, estimate cuts |

- Judgment (analyst call): prospect 2: direct-to-phone service needs ~45 satellites; 13 in orbit; competition 2: GM 62.6 to 25.2% falling; SpaceX direct-to-cell substitute shipping; macro 0: the thesis needs the regime to change: $2B of converts, SBC 128%; narrative 1: space lagging and worsening.
- Avg target: 79.61 · https://stockanalysis.com/stocks/asts/forecast/ · 2026-09-24
- Revenue actual: 31520000.0 · https://www.marketbeat.com/stocks/NASDAQ/ASTS/earnings/ · 2026-09-24
- Guide: None · None · None
- Revisions 90d: down · https://finance.yahoo.com/quote/ASTS/analysis/ · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=ASTS · 2026-09-24
- Holders up: 560 · https://api.nasdaq.com/api/company/ASTS/institutional-holdings?limit=15&type=TOTAL&sortColumn=marketValue · 2026-09-24

### NBIS

Tier no_runway; total 30; gates failed: upside, delivery.

Research row: | NBIS | $243.48 (9/24) / 299.86-73.52 / -18.8% | Buy / 19 (SA); MB 19, 2 sells | $276.26 (MB $241.80, below close) | $415 / $84 | +13.5% (MB -0.7%) | BNP upgraded to OP $399 (9/24). Redburn initiated Sell $84 (9/21). Truist initiated Buy $355, Citi raised to $324, Baird to $340, Piper initiated Neutral $224, DA Davidson Neutral $175 | Q2 on 8/12: rev $582M vs $568M, EPS -$0.12 vs -$0.67. FY26 held: rev $3.0-3.4B, ARR $7-9B, capex $20-25B | +34.1% / +15.9% | flat / down (FY26 GAAP EPS -1.62 to -2.34) | FCF -$5.88B vs NI $42M | Prepaid multi-$B AI-cloud deals fund a 5 GW build. ARR $3B to $7-9B; FY27 revenue ~$12.3B | CRWV, IREN. GM 71% to 77% (SA); Finviz 18.8% conflicts. EV/S 50 vs CRWV 12.5, IREN 26 | none | 10 sales, ~$46M, 8 insiders: CEO $11.0M, Dir Ryan $13.3M, CIO $8.0M, CRO, CTO, CFO, Dir Boynton | TTM: 571 up / 199 down. State Street +16.2% to 4.07M. Trims: Andra -70%. Net n/a | 20.31% (SA 19.80%), 2.22, date n/a | +13.6% / +49.0%; 50 above 200. RS 1m +9.5 / +2.6; 3m -9.6 / -10.6. Rebound inside range; gap held but faded 13.6% | Q3 est. 11/10 (unconfirmed). Exit-2026 ARR test | n/a |

- Judgment (analyst call): prospect 4: ARR guide $7-9B held; GAAP losses widening; competition 3: EV/S 50 vs CRWV 12.5; macro 0: the thesis needs the regime to change: capex $20-25B; narrative 1: neoclouds lagging.
- Avg target: 276.26 · https://stockanalysis.com/stocks/nbis/forecast/ · 2026-09-24
- Revenue actual: 582300000.0 · https://www.marketbeat.com/stocks/NASDAQ/NBIS/earnings/ · 2026-09-24
- Guide: held · https://nebius.com/newsroom/nebius-reports-second-quarter-2026-financial-results · 2026-08-12
- Revisions 90d: down · https://finance.yahoo.com/quote/NBIS/analysis/ · 2026-09-24
- Insider coverage: True · https://finviz.com/quote.ashx?t=NBIS · 2026-09-24
- Holders up: 571 · https://www.marketbeat.com/stocks/NASDAQ/NBIS/institutional-ownership/ · 2026-09-23

### PSNL

Tier no_runway; total 29; gates failed: upside.

Research row: | PSNL | $16.57 / 18.89-4.95 / -12.3% | Buy / 5 (2B/3H) | $15.44 | $16.25 / $13 | -6.8 | Craig-Hallum downgrade to Hold $16 (8/24) | 8/4: rev $22.4M vs $16.7M; EPS -0.30 vs -0.26; no guide (deal pending) | 0.0%, +5.1% (not held) | n/a | FCF TTM -$101M vs NI -$107M; SBC 16%. **Cash $212.7M; burn about $28M/q; runway about 7.7q (moot if the deal closes)** | Case: merger arbitrage. Tempus pays $16.25 in stock (0.3356 max ratio); with TEM at $82.24 the value is fixed at $16.25 | NTRA, GH; GM 12.7%; EV/S 22.9 | none | CEO Hall $1.51M (7/9) + $1.32M (6/26); Pres Chen $1.52M (7/15); CFO $745K; 9/18 four-officer sell-to-cover of about $267K | TTM 64/35; adds BofA 1.82M sh, UBS | 8.2% (Finviz 11.5%), DTC 3.6, 9/15 | +9.8% / +61%; 50>200; RS 1m -4.1 / 3m +27.1; base; gap not held | HSR refiled 9/2 (waiting period ends about 10/2, derived); special meeting not set; close late 2026 or early 2027 (outside date 4/20/27); Q3 about 11/3 | n/a |

- Judgment (analyst call): prospect 1: merger arbitrage at a fixed $16.25; no standalone case; competition 3: NTRA and GH; macro 2: deal spread insensitive to rates; narrative 2: cash-out via TEM stock.
- Avg target: 15.44 · https://stockanalysis.com/stocks/psnl/forecast/ · 2026-09-24
- Revenue actual: 22.36 · https://www.marketbeat.com/stocks/NASDAQ/PSNL/earnings/ · 2026-08-04
- Guide: none · https://www.biospace.com/press-releases/personalis-reports-second-quarter-2026-results-and-recent-highlights · 2026-08-04
- Revisions 90d: None · None · None
- Insider coverage: True · https://finviz.com/quote.ashx?t=PSNL · 2026-09-24
- Holders up: 64 · https://www.marketbeat.com/stocks/NASDAQ/PSNL/institutional-ownership/ · 2026-09-24
