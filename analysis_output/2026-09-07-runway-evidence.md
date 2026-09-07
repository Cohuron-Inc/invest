# September Runway Probe — evidence

Companion to `analysis_output/2026-09-07-runway-probe.html`. Raw records are in
`analysis_output/2026-09-07-runway-data/`, one JSON per ticker, every leaf carrying its
source URL and the date the page stated.

## Manifest summary

| Item | Value |
|---|---|
| Window end | 2026-09-07 |
| Price date | 2026-09-04 close, every name |
| 13F vintage | 2026-06-30 inferred; see the caveat below, none of these are a clean quarter-over-quarter holders table |
| Short interest settlement | 2026-08-14 |
| Names | PLPC, AMKR, IONQ, TEM, QCOM, RKT, TPL, GLD |
| Mandate | high return, medium-to-low risk, 1 to 3 years |
| Hurdle | 5.37%, ICE BofA single-A US corporate effective yield, 2026-09-03 |
| Source of the list | the user, not a corpus probe tier card, so `probe_tier` is null on every record |

Ticker resolution: the request named "TEMPUS", which is TEM, Tempus AI; and "QUALCOM
STOCK", which is QCOM, Qualcomm. GLD is a commodity trust and not an operating company,
and the four gates do not apply to it.

### Sources that failed

- `finance.yahoo.com/quote/TICKER/analysis/` returned a load error or empty EPS Revisions
  and EPS Trend tables on five of eight names. This is the pinned primary for estimate
  revisions, so the 30-day direction is missing on most of the list.
- `stockanalysis.com/stocks/TICKER/forecast/` publishes no estimate-trend table at all,
  so it cannot serve as the revisions secondary. For IONQ and TEM the 90-day direction
  was derived instead from the pre-print consensus against the current consensus, and the
  derivation is written into the record note. Both are marked derived on the page.
- `stockanalysis.com/stocks/PLPC/forecast/` is a 404. PLPC's coverage is too thin for the
  consensus product, so no live average target exists.
- MarketBeat's institutional pages still carry the CalSTRS row with multi-thousand-percent
  increases. On TPL that row's share count exceeds total shares outstanding, which
  confirms the corruption. Dollar totals were excluded on every affected name and holder
  counts used instead.
- MarketBeat's buyer and seller counts are trailing-twelve-month, not a quarter-over-quarter
  13F holders table. They were used as the closest available proxy for the flow gate and
  that is flagged per ticker in the records.
- Short interest disagrees materially between aggregators on three names because the float
  denominators differ: TEM 27.75% (Finviz) against 21.86% (MarketBeat), AMKR 15.96%
  against 5.27%, RKT 5.50% against 8.56%. Both are recorded; MarketBeat is used as primary
  where it states a settlement date.
- Print-day and five-day reaction was not fetched for IONQ, TEM, RKT and TPL, so
  `print_gap_held` is null for those four.
- Macro side: CME FedWatch timed out twice, Barchart's breadth pages returned empty
  content, the StockAnalysis ETF pages surface only one-year return through WebFetch, and
  FRED's CSV endpoint returns rows from 2008 to 2012 unless explicit date parameters are
  passed. Substitutes are named in `macro.json`.

### Rubric behaviour that distorted this run

Four artifacts are recorded in `_manifest.json` under `rubric_artifacts` and in the
registry's new "Rubric behaviour to fix" table. They matter for reading the scorecard:

1. **Risk to reward explodes when the downside anchor sits on top of the close.** QCOM's
   200-day line is 0.54% below its close, giving 26.9 : 1. RKT's low consensus target of
   $14.00 is 0.4% below its $14.06 close, giving 60.7 : 1. Both numbers are arithmetic,
   not analysis. Neither was allowed to drive a verdict.
2. **The delivery gate cannot be passed by a company that does not guide.** PLPC beat EPS
   by 86% and rose 30% on the day, and still fails the gate because it issues no guidance.
   TPL does not guide either. This did not change either tier, since both also fail a
   second gate, but it is why their delivery column reads as a failure.
3. **Zero corpus coverage scores as "quiet with fundamentals".** Five of eight names have
   no corpus mentions at all, and the rubric awards them 6 or 9 contrarian points for
   silence. Their totals are inflated by roughly that much and are not comparable with a
   name the corpus actually covers.
4. **GLD is scored against equity gates it cannot meet.** It takes 3 points for having no
   insiders and 0 for having no earnings print. Its total of 29 is meaningless.

## Macro brief

| Item | Value (date) | Source | Read |
|---|---|---|---|
| Fed funds target | 3.50-3.75%, held 2026-07-29, vote 9-3 with three dissents for a hike | federalreserve.gov statement | The majority is on hold and the dissent bloc wants to tighten |
| Priced path | ~56% hike at the 16 Sep meeting, ~67% cumulative by 28 Oct, year-end implied 3.99% (2026-09-04) | centralbank.watch (FedWatch timed out) | The market has flipped from pricing cuts to pricing about 1.5 hikes by December |
| 2y / 10y / 2s10s / 10y real | 4.34% / 4.77% / +0.41 / 2.42% (2026-09-03/04) | FRED DGS2, DGS10, T10Y2Y, DFII10 | A genuine tightening of financial conditions |
| IG / HY OAS | 0.81% (+3bp) / 2.65% (-10bp) (2026-09-03) | FRED BAMLC0A0CM, BAMLH0A0HYM2 | Credit is calm and is not confirming the rate scare |
| Dollar index | 118.75, -1.55% over a month (2026-08-28) | FRED DTWEXBGS | Weaker dollar even as yields rose |
| WTI | $91.48, +11.6% over a month (2026-09-01) | FRED DCOILWTICO | The Iran escalation is a live inflation risk |
| VIX | 14.32, one-month range 14.25 to 16.34 (2026-09-03) | FRED VIXCLS | Calm to the point of complacency |
| Payrolls / unemployment | +162K against +53K consensus; 4.1% (Aug, released 2026-09-04) | BLS | A large beat that argues for a hike, not a cut |
| CPI / core | 3.4% / 2.5% year over year (Jul, released 2026-08-12) | BLS | Still above target; the August print lands 11 Sep |
| SPY / QQQ | +0.21% / +4.43% and +0.60% / +1.97% over 1m / 3m (2026-09-04) | Finviz | Index gains have stalled over the last month |
| Factors 1m | Value +4.75% and high beta +1.92% led; momentum -1.07% and quality -1.06% lagged | Finviz MTUM, VLUE, QUAL, IWM, SPHB, SPLV | Rotation out of crowded momentum into cyclical value |
| Sectors 1m | Top: energy +2.26%, technology +1.36%, utilities +0.84%. Bottom: consumer cyclical -1.92%, real estate -1.23%, materials -1.11% | Finviz groups | The oil trade is already being played |
| Breadth | Over 70% above the 200-day, only 54% above the 50-day (week of 2026-08-28) | StockCharts (Barchart empty) | Long-term breadth healthy, short-term participation thinning |
| Hurdle | 5.37% (2026-09-03) | FRED BAMLC0A3CAEY | The bar an equity has to clear against safe corporate credit |

Live themes, with direction and counter-narrative: the **Fed hawkish pivot** is
accelerating, countered by a soft August CPI on 11 September deflating hike odds. The
**Iran and oil shock** is accelerating, countered by the fact that prior 2026 spikes
unwound once fighting paused and Hormuz has not actually closed. **AI capex** is stable
rather than accelerating, with a building counter-narrative in capex fatigue and top-ten
S&P concentration at 35%, above the dot-com peak of 25%. **Narrowing breadth** is
accelerating. **Fiscal cliff risk** is fading, with the CR funding the government to
11 December.

Dated macro events in three months: CPI 11 Sep, FOMC 15-16 Sep, payrolls 2 Oct, CPI
14 Oct, FOMC 27-28 Oct, quarterly refunding around 2-4 Nov, payrolls 6 Nov, CPI 10 Nov,
payrolls 4 Dec, FOMC 8-9 Dec, CPI 10 Dec, funding deadline 11 Dec.

The corpus's own macro account, deerpointmacro, put 30-year single-A industrial paper at
6.02% on 5 September, against the 5.37% index-level single-A yield used as the hurdle
here. Both say the same thing: an equity in this regime needs a visible free-cash-flow
yield or a demonstrated earnings inflection.

## Scorecard

| # | Ticker | Tier | Close | Upside | R:R | Earn | Prosp | Comp | Insd | Inst | Retail | Up | RR | Chart | Macro | Narr | Total | Gates failed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | IONQ | runway | 39.52 | 71% | 2.1 | 14 | 2 | 2 | 0 | 7 | 9 | 10 | 7 | 2 | 1 | 2 | 56 | none |
| 2 | RKT | one_leg_missing | 14.06 | 26% | 60.7 | 3 | 3 | 3 | 3 | 7 | 6 | 6 | 10 | 0 | 1 | 2 | 44 | delivery |
| 3 | TPL | no_runway | 362.42 | 22% | 0.9 | 6 | 6 | 5 | 4 | 7 | 6 | 6 | 1 | 0 | 7 | 6 | 54 | delivery |
| 4 | QCOM | no_runway | 168.74 | 14% | 26.9 | 3 | 4 | 3 | 0 | 7 | 6 | 3 | 10 | 3 | 6 | 4 | 49 | upside, delivery |
| 5 | PLPC | no_runway | 398.45 | n/f% | n/f | 6 | 7 | 6 | 2 | 7 | 6 | 0 | 0 | 5 | 5 | 5 | 49 | upside, delivery |
| 6 | TEM | no_runway | 64.62 | 2% | 0.1 | 10 | 5 | 4 | 0 | 7 | 9 | 1 | 1 | 3 | 3 | 5 | 48 | upside |
| 7 | AMKR | no_runway | 47.77 | 60% | 1.2 | 3 | 5 | 3 | 0 | 9 | 6 | 10 | 1 | 0 | 3 | 4 | 44 | delivery |
| 8 | GLD | no_runway | 406.77 | n/f% | n/f | 0 | 5 | 2 | 3 | 3 | 6 | 0 | 0 | 2 | 4 | 4 | 29 | upside, flow, delivery |

Why, per mechanical signal:

- **IONQ** earnings: beat both, guide raised, revisions up; insider: clustered or CEO selling $513,216, no buys; institutional: net adds or holders up 527 vs down 143; retail: quiet with fundamentals: 0 posts, 0 accounts; chart: below the 200 (-10.6%) in a base
- **RKT** earnings: miss, guide cut, or revisions down; cash conversion below 70% caps at 6; insider: no insider activity found; institutional: net adds or holders up 536 vs down 134; retail: moderate: 0 posts, 0 accounts; chart: below both (-0.7% / -13.0%), structure trend_up
- **TPL** earnings: mixed print; insider: small buys $1,528; institutional: net adds or holders up 648 vs down 218; retail: moderate: 0 posts, 0 accounts; chart: below both (-6.6% / -7.5%), structure breakdown
- **QCOM** earnings: miss, guide cut, or revisions down; insider: clustered or CEO selling $1,467,842, no buys; institutional: net adds or holders up 1863 vs down 1510; retail: moderate: 2 posts, 2 accounts; chart: above the 200 (+0.5%) or breaking out; RS 3m -25.73
- **PLPC** earnings: mixed print; insider: no buys; sells $5,361,640; institutional: net adds or holders up 89 vs down 35; retail: moderate: 0 posts, 0 accounts; chart: above both averages, RS 3m 9.129999999999999
- **TEM** earnings: beat, guide held or raised, revisions not down; insider: clustered or CEO selling $18,274,074, no buys; institutional: net adds or holders up 283 vs down 127; retail: quiet with fundamentals: 11 posts, 2 accounts; chart: above the 200 (+14.6%) or breaking out; RS 3m 27.13
- **AMKR** earnings: miss, guide cut, or revisions down; cash conversion below 70% caps at 6; insider: clustered or CEO selling $2,146,287, no buys; institutional: net +35,100,000 sh, new None vs exited None, named adds; retail: moderate: 3 posts, 2 accounts; chart: below both (-18.8% / -14.9%), structure breakdown
- **GLD** earnings: no print found; insider: no insider activity found; institutional: not cleanly measurable; retail: moderate: 0 posts, 0 accounts; chart: below the 200 (-2.1%) in a base

## Corpus side

`pnpm q retail-interest` over the 7 Jul to 7 Sep window, six accounts, 4,551 posts:

| Ticker | Accounts | Posts | Days | Posts last 14d | Likes | Impressions | Formal stance |
|---|---|---|---|---|---|---|---|
| TEM | 2 | 11 | 7 | 1 | 735 | 104,562 | LogicalThesis long, conviction 0.60, position |
| AMKR | 2 | 3 | 3 | 0 | 698 | 129,577 | stocktalkweekly long, conviction 0.60, position |
| QCOM | 2 | 2 | 2 | 1 | 1,638 | 170,123 | none |
| PLPC | 0 | 0 | 0 | 0 | — | — | none |
| IONQ | 0 | 0 | 0 | 0 | — | — | none |
| RKT | 0 | 0 | 0 | 0 | — | — | none |
| GLD | 0 | 0 | 0 | 0 | — | — | none |
| TPL | 0 | 0 | 0 | 0 | — | — | none |

Three corpus posts pair one of these tickers with an analyst or institutional keyword.
Only one is evidence rather than commentary:

- **AMKR**, CEOStockWatcher, 2026-08-10, post 2086852102492389491: "A director at Amkor
  $AMKR just sold $2.75m (their 2nd largest sale, out of 53)." This is a Form 4 relay and
  it corroborates the clustered selling in the record.
- **TEM**, LogicalThesis, 2026-07-14: an argument about PSNL taking on NTRA with TEM's
  help, not a stance on TEM.
- **QCOM**, TheLongInvest, 2026-07-29: a macro post that lists QCOM among companies
  reporting that day. Not a stance.

The two formal stances, from `data/analysis/accounts/`:

- **stocktalkweekly on AMKR**, long, 0.60: "A long-held name he says he has been loud
  about since well before the window. The bull case is that the prepayment and roadmap
  alignment with the dominant AI chip vendor are enormous relative to the company's market
  capitalisation and revenue base, effectively locking in the U.S. advanced-packaging
  capacity build."
- **LogicalThesis on TEM**, long, 0.60: "TEM bought the MRD asset he had been pounding the
  table on at what he considered a steal, giving it a legitimate shot at a duopoly with
  NTRA. On 7/17 he had cut the position because a competing bid looked bad for TEM; the
  deal terms three days later reversed his view entirely."

Read as positioning rather than fact, per the doctrine: corpus commentary is the cheapest
evidence in the set. Neither stance is high conviction, and neither account is a
counterweight to the filings.

## Per name

### PLPC — Preformed Line Products, no runway on the numbers, 49/100

| Field | Value | Source, date |
|---|---|---|
| Close | $398.45, 52w $504.69 to $184.02, 21.1% off the high | finviz.com/quote.ashx?t=PLPC, 2026-09-04 |
| Consensus | Strong Buy, 2 analysts. **No live average target.** | marketbeat.com/stocks/NASDAQ/PLPC/forecast/, 2026-09-07 |
| Only published target | $275, set by Loop Capital 2026-03-09, before the Q2 beat and the rally. MarketBeat shows it as 31.0% *downside*. Treated as stale, not as a live target. | same |
| Analyst actions 60d | Freedom Capital upgrade to Strong Buy, 2026-08-04. Weiss excluded per brief. | same |
| Last print | 2026-07-29. Revenue $212.7M vs $193M, EPS $4.49 vs $2.41. No guidance issued. | marketbeat.com/stocks/NASDAQ/PLPC/earnings/ |
| Print reaction | **+30.0% on the day, +66.2% at five sessions.** The gap held. | record, price block |
| Revisions | Not found, no estimate tables published | — |
| FCF vs NI | $34.4M against $43.1M, 0.80x conversion. SBC 1.0% of revenue. | stockanalysis.com cash-flow statement |
| Competition | HUBB at 21.2x forward and 4.7x EV/sales; MacLean Power private. **Gross margin 29.7% to 34.3% rising over four quarters.** | stockanalysis.com ratios |
| Insiders 90d | No buys. Ruhlman $4.4M and Corlett $0.9M sold, $5.36M total. 10b5-1 status not stated by the source. | finviz.com/quote.ashx?t=PLPC |
| Institutions | Holders up 89, down 35. Adds Wasatch and Millennium; exits Renaissance, HSBC, Dimensional. CalSTRS excluded. | marketbeat institutional-ownership |
| Short interest | 5.03% of float, 1.3 days to cover | marketbeat short-interest, 2026-08-14 |
| Chart | +2.95% above the 50-day, +28.9% above the 200-day, 50 above 200. RS 3m +9.1pp against SPY, 1m -13.7pp. In a base. | finviz |
| Catalyst | Q3 earnings around 2026-10-28, aggregator estimate | marketbeat |

Judgment: prospect 7, the driver is in the reported print and the margin trend, not in a
story. Competition 6, widening gross margin is the cleanest moat evidence in the probe.
Macro fit 5, cash-generative industrial but a small cap in a month when small caps
trailed. Narrative 5, grid buildout adjacency but no theme sponsorship.

Gates: **upside fails** because no live target exists; **delivery fails** because the
company issues no guidance and the gate requires a held or raised guide. Both are
recorded, and the second is a rubric artifact rather than a business fact.

### AMKR — Amkor Technology, no runway on the numbers, 44/100

| Field | Value | Source, date |
|---|---|---|
| Close | $47.77, 52w $96.68 to $23.38, 50.6% off the high | finviz, 2026-09-04 |
| Consensus | Moderate Buy, 11 analysts. Average $76.40, high $92, low $65. **+59.9% upside.** Alt $68.33 (MarketBeat). | stockanalysis.com/stocks/amkr/forecast/ |
| Analyst actions 60d | BofA initiation 2026-08-27; Morgan Stanley, Goldman and B. Riley at hold; Needham buy 2026-07-28 | same |
| Last print | 2026-07-27. Revenue $1.90B vs $1.81B beat, EPS $0.70 vs $0.47 beat. **Guide cut** on the communications segment. | marketbeat earnings |
| Print reaction | **-24.7% on the day, -17.9% at five sessions.** The gap held, unfilled. | record |
| Revisions | 30d down, 90d up. The source's own count table conflicts with its trend numbers; both recorded. | yahoo analysis |
| FCF vs NI | **-$172.4M against $555.5M.** SBC 0.3% of revenue. Cash conversion caps the earnings score at 6. | stockanalysis |
| Competition | ASX at 26.6x forward, 4.2x EV/sales; JCET China-listed and unreachable. Gross margin range-bound 14-17%. | stockanalysis |
| Insiders 90d | No buys. Rogers, Faust, Alexander, Rutten and Engel sold, about $2.1M total. **Corroborated by the corpus:** CEOStockWatcher, 10 Aug, a director's $2.75M sale, their second largest of 53. | finviz; corpus post 2086852102492389491 |
| Institutions | Net +35.1M shares. Holders up 322, down 151. Adds TD Waterhouse, Corient; exits Amundi, Fortitude, Oliver Luxxe. | marketbeat |
| Short interest | 5.27% of float (MarketBeat) against 15.96% (Finviz), different denominators | 2026-08-14 |
| Chart | -18.8% below the 50-day, -14.9% below the 200-day, 50 below 200. Relative strength badly negative on both spans. **Breakdown.** | finviz |
| Catalyst | Q3 earnings around 2026-10-26, aggregator estimate | marketbeat |

Judgment: prospect 5, the advanced-packaging case is in announced capex and backlog, not
in the last two prints. Competition 3, flat gross margin and the highest-value packaging
being taken in-house by the foundry. Macro fit 3, a capital-intensive cyclical with
negative free cash flow committing to a $7B campus at a 4.77% ten-year. Narrative 4,
inside a theme the macro brief rates stable with a capex-fatigue counter building.

Gates: **delivery fails** on the guide cut. Risk to reward is 1.17 : 1 against the
52-week low, below the 1.5 floor, which is what drops it out of "one leg missing".

### IONQ — IonQ, RUNWAY on all four gates, 56/100

| Field | Value | Source, date |
|---|---|---|
| Close | $39.52, 52w $84.64 to $25.89, 53.3% off the high | finviz, 2026-09-04 |
| Consensus | Strong Buy, 13 analysts. Average $67.68, high $100, low $44.78. **+71.3% upside.** | stockanalysis.com/stocks/ionq/forecast/ |
| Analyst actions 60d | Northland, Wedbush, Mizuho, Cantor reiterate or maintain 6-19 Aug; Morgan Stanley hold, the outlier | same |
| Last print | 2026-08-05. Revenue $80.1M vs $66.5M beat, +286.7% y/y. EPS -$0.33 vs -$0.56 beat. **FY26 guide raised to $280-290M against $268.2M consensus.** | marketbeat earnings |
| Also guided | **FY26 adjusted EBITDA loss guided to widen to $310-330M.** | fool.com coverage of the print |
| Revisions 90d | **Up, derived.** FY26 revenue consensus moved $268.2M at the 5 Aug print to $287.17M by 19 Aug, +7.1%. No estimate-trend table exists for this name on either pinned source. | marketbeat earnings against stockanalysis forecast, 2026-08-19 |
| FCF vs NI | **-$483.9M** against -$1,365.0M. GAAP net income is distorted by non-cash warrant swings of +$805M and -$1,868M in consecutive quarters. **SBC is 182.6% of revenue.** | stockanalysis cash-flow statement |
| Competition | RGTI at 351x EV/sales, QBTS at 457x; IONQ around 52x forward sales. **Gross margin fell 48.0% to 26.3% over four quarters.** New entrant IQM. | stockanalysis |
| Insiders 90d | No buys. Toledano, Chou and Raymond all sold on 2026-06-18, about $513K total. | finviz |
| Institutions | Holders up 527, down 143. Adds UBS AM, Amundi; exits Wellington, GTS, Van Eck. | marketbeat |
| Short interest | 11.18% of float, 1.9 days to cover | 2026-08-14 |
| Chart | -4.1% below the 50-day, -10.6% below the 200-day. RS 3m -34.8pp against SPY. In a base. | finviz |
| Catalyst | Q3 earnings around 2026-11-04, aggregator estimate | marketbeat |

Judgment: prospect 2, real revenue growth but the path to the target is commercial quantum
advantage years out. Competition 2, margin collapsing while revenue grows is buying share,
against far better-capitalised architectures. Macro fit 1, the thesis needs the rate regime
to change. Narrative 2, a name that is mostly narrative, and its factor proxy was the worst
performer of the month.

Gates: **all four pass.** Upside +71.3%, holders up 527 against 143, no insider selling
cluster above the dollar threshold, and a revenue beat with a raised guide and up
revisions. Risk to reward 2.07 : 1 against the 52-week low.

This is the probe's most important result and it is a warning, not a recommendation. The
gates are blind to cash burn, to stock compensation, and to gross-margin collapse. See the
verdict below.

### TEM — Tempus AI, no runway on the numbers, 48/100

| Field | Value | Source, date |
|---|---|---|
| Close | $64.62, 52w $104.32 to $40.77, 38.1% off the high | finviz, 2026-09-04 |
| Consensus | Buy, 16 analysts. Average $65.79, high $100, low $35. **+1.8% upside.** | stockanalysis.com/stocks/tem/forecast/, 2026-09-02 |
| Analyst actions 60d | Cantor initiation; Canaccord, Piper and BTIG raises 20 Aug to 2 Sep; JPMorgan cut 2026-08-05 | same |
| Last print | 2026-07-30. Revenue $382.5M vs $379.7M beat, EPS -$0.04 vs -$0.14 beat. **Guide held** at about $1.6B FY26. | marketbeat earnings |
| Revisions 90d | **Flat, derived.** Guide held at about $1.6B and consensus sits at $1.60B, so consensus has not moved against the guide. No estimate-trend table exists. | stockanalysis forecast, 2026-09-02 |
| FCF vs NI | -$263.2M against -$254.4M. SBC 13.0% of revenue, above the 10% flag. | stockanalysis |
| Competition | GH at 18.9x EV/sales, NTRA at 17.2x. Gross margin stable 63-65%. | stockanalysis |
| Insiders 90d | No buys. **CEO Eric Lefkofsky sold $16.3M**, Kubo $1.9M, Doudna $0.04M. $18.2M total. | finviz |
| Institutions | Holders up 283, down 127. Adds Leonteq, Assetmark, Hollencrest on small bases; exits H&H, Dimensional, BofA. Page implies a 2026-03-31 quarter end, which trails its own Q2 print. | marketbeat |
| Short interest | **21.86% of float (MarketBeat) against 27.75% (Finviz)**, 7.3 days to cover. One source cites a peak near 30.5% earlier in 2026. | 2026-08-14 |
| Chart | +16.0% above the 50-day, +14.6% above the 200-day, 50 above 200. **RS 1m +35.9pp and 3m +34.8pp against SPY.** Trending up. | finviz |
| Catalysts | Q3 earnings around 2026-11-03, aggregator estimate. Shareholder litigation ongoing. | marketbeat |

Judgment: prospect 5, guided visibility with a real path to first GAAP profit. Competition
4, stable margin and a shot at an MRD duopoly, but Natera is the stronger franchise. Macro
fit 3, still-unprofitable growth healthcare carries duration, though breakeven is a year
out rather than several. Narrative 5, inside the AI theme with revenue underneath it, but
carrying a Spruce Point short report and 22% to 28% short interest.

Gates: **upside fails** at +1.8%. Risk to reward is 0.14 : 1. The name has already run:
the strongest relative strength in the probe over both spans, with the CEO selling $16.3M
into it. That pairing is the doctrine's distribution read.

### QCOM — Qualcomm, no runway on the numbers, 49/100

| Field | Value | Source, date |
|---|---|---|
| Close | $168.74, 52w $259.92 to $121.99, 35.1% off the high | finviz, 2026-09-04 |
| Consensus | Hold, 37 analysts. Average $193.10, high $400, low $100. **+14.4% upside.** Alt $203.76 (MarketBeat), +20.8%. | stockanalysis.com/stocks/QCOM/forecast/ |
| Analyst actions 60d | Citi hold $175 (8/25); BofA sell $180 (8/11); Freedom Capital upgrade to buy $200 (8/7); JPMorgan neutral $215 (8/5); Argus buy $220 (7/31) | same |
| Last print | 2026-07-29. Revenue $9.95B vs $9.69B beat, EPS $2.21 vs $2.23 **miss**. **Q4 guide cut** to $2.05-2.25 against $2.23 consensus. | marketbeat earnings |
| Print reaction | -2.6% on the day, +3.0% at five sessions | record |
| FCF vs NI | $9,979M against $13,377M, 0.75x conversion. SBC 7.8%, below the flag. The overview page states TTM net income of $9.26B against the cash-flow statement's $13,377M; the conflict is recorded. | stockanalysis |
| Competition | AVGO at 18.6x forward, MRVL at 33.0x, QCOM at **16.6x, the cheapest**. **Gross margin narrowed 55.3% to 53.1% over four quarters.** | stockanalysis, finviz |
| Insiders 90d | No buys. Five routine officer sales, $35K to $470K, $1.47M total. Plan status not stated. | finviz |
| Institutions | Holders up 1,863, down 1,510. Amundi +94.1% named add. CalSTRS row (+18,251.8%) excluded. | marketbeat |
| Short interest | 3.17% of float, 3.6 days to cover | 2026-08-14 |
| Chart | -0.34% below the 50-day, +0.54% above the 200-day, the two lines are on top of each other. RS 1m +4.2pp against SPY and +1.1pp against XLK; **3m -25.7pp**. In a base. Print gap did not hold as a gap, though price recovered above the pre-print level. | finviz |
| Catalyst | Q4 FY26 earnings around 2026-11-04, aggregator estimate | marketbeat |
| Why it fell | Handset revenue -20% y/y on OEM inventory drawdown and memory cost inflation, and Apple's in-house modem transition taking QCOM's iPhone share from about 20% toward zero by 2027 | record |

Judgment: prospect 4, the auto and IoT offset is guided but the Apple loss is contractual
and dated, so the negative is more certain than the positive. Competition 3, narrowing
margin while the largest customer designs it out, offset by the cheapest multiple in the
peer set. Macro fit 6, the regime's preferred shape, with a free-cash-flow yield that
clears the 5.37% hurdle. Narrative 4, outside the accelerating themes.

Gates: **upside fails** at +14.4% against the 20% bar, and the two aggregators agree
within ten points so the alternative 25% test does not apply. **Delivery fails** on the
guide cut. The 26.9 : 1 risk to reward is the anchor artifact described above and was
ignored.

### RKT — Rocket Companies, one leg missing, 44/100

| Field | Value | Source, date |
|---|---|---|
| Close | $14.06, 52w $24.36 to $12.17, 42.3% off the high | finviz, 2026-09-04 |
| Consensus | Buy, 17 analysts. Average $17.70, high $21, low $14. **+25.9% upside.** | stockanalysis.com/stocks/RKT/forecast/ |
| Analyst actions 60d | RBC hold $16 (8/28); JPMorgan hold, cut $16 to $14 (8/11); KBW buy, cut $20 to $19 (8/10); BTIG hold (8/10); Morgan Stanley buy $19 (8/7). **Three of five cut.** | same |
| Last print | 2026-08-06. Revenue $2.76B vs $2.81B **miss**, EPS $0.16 vs $0.164 **miss**. **Q3 guide cut** to $2.5-2.7B against $2.9B consensus. | marketbeat earnings |
| FCF vs NI | **-$774M against +$471M.** SBC 4.7%. Cash conversion caps the earnings score. | stockanalysis |
| Competition | UWMC at 4.2x forward, PFSI at 6.7x, **RKT at 15.9x**. Mr. Cooper and Redfin are no longer independent peers, both acquired by RKT. | stockanalysis, finviz |
| Insiders 90d | **None either way.** The only visible rows pre-date the window. | finviz |
| Institutions | Holders up 536, down 134. Adds Amundi, Wellington, Atreides. | marketbeat |
| Short interest | 8.56% of float (MarketBeat) against 5.50% (Finviz), 3.5 days to cover | 2026-08-14 |
| Share basis | The consensus target and short interest are against the roughly 968M-share Class A public float, not the roughly 2.83B total shares across all classes; Class D is controlled by Rock Holdings. | record note |
| Chart | -0.69% below the 50-day, -13.0% below the 200-day. RS 1m +6.1pp and 3m +6.7pp against SPY. Trending up inside a larger downtrend. | finviz |
| Catalyst | Q3 earnings around 2026-10-29, aggregator estimate | marketbeat |

Judgment: prospect 3, the $500M synergy target depends on execution and on rate relief,
and the last print missed and cut. Competition 3, consolidating the industry but at a
roughly threefold multiple premium to UWMC and PFSI. Macro fit 1, the worst in the probe;
a mortgage originator with -$774M of free cash flow needs falling rates and the market has
flipped to pricing hikes. Narrative 2, its only theme is rate relief, moving the wrong way.

Gates: **delivery fails** on the miss and the guide cut. It reaches "one leg missing" only
because the 60.7 : 1 risk to reward clears the 1.5 floor, and that number is the artifact
described above: the low consensus target of $14.00 sits six cents below the close.
Corrected against the 52-week low of $12.17, reward to risk is 1.93 : 1.

### TPL — Texas Pacific Land, no runway on the numbers, 54/100

| Field | Value | Source, date |
|---|---|---|
| Close | $362.42, 52w $547.20 to $269.23, 33.8% off the high | finviz, 2026-09-04 |
| Consensus | Hold, **2 analysts only**. Average $442, high $639, low $245. **+22.0% upside.** Alt $441.33. | stockanalysis.com/stocks/TPL/forecast/ |
| Analyst actions 60d | KeyBanc buy $639, 2026-06-04, which is about 92 days old. No more recent action exists. | same |
| Last print | 2026-08-05. Revenue $246.1M vs $249.5M **miss**, EPS $2.23 vs $2.18 beat. No guidance issued, as a matter of policy. | marketbeat earnings |
| FCF vs NI | **$526.7M against $541.4M, 97% conversion.** SBC 1.8%. | stockanalysis |
| Competition | VNOM at 18.7x forward, KRP at 16.4x, **TPL at 37.1x, about twice the peer group**. **Gross margin 91.9% to 95.3% rising.** | stockanalysis |
| Revenue mix | First half 2026: land and royalty $317.4M against water $165.5M, about 66 to 34. | record |
| Insiders 90d | One director buy, Peter Doyle, 4 shares, $1,528. **Horizon Kinetics' three 1-share daily purchases were excluded** as a routine automatic program, not a discretionary buy; they are kept in the record under `routine_programs_excluded`. **Selling:** CFO Chris Steddum sold $1.27M on 2026-06-05, four days outside the window. | finviz |
| Institutions | Holders up 648, down 218. Adds UBS, VanEck. CalSTRS row excluded; its share count exceeded total shares outstanding. | marketbeat |
| Short interest | 6.78% of float, 9.6 days to cover | 2026-08-14 |
| Chart | -6.6% below the 50-day, -7.5% below the 200-day. RS 1m +1.7pp, **3m -11.5pp** against SPY. **Breakdown.** | finviz |
| Index | In the S&P 500 since November 2024, no removal to date | record |
| Catalyst | Q3 earnings around 2026-11-04, aggregator estimate | marketbeat |

Judgment: prospect 6, a third of first-half revenue is already water and surface, so part
of the re-rating case is reported rather than promised. Competition 5, widening gross
margin and a zero-capex royalty structure, but at twice the peer multiple. Macro fit 7,
**the best in the probe**: a debt-free royalty with 97% cash conversion in a plateau-or-higher
rate regime, with WTI up 11.6% in a month and energy the top sector. Narrative 6, inside
the accelerating oil shock with its own cash flow underneath it.

Gates: **delivery fails** on the revenue miss, compounded by the no-guidance artifact.
Risk to reward is 0.85 : 1 because the nearest anchor, the 52-week low, is 25.7% below the
close. That is the honest reason this name is not in the top tier: the business is the
best here, the entry price is not.

### GLD — SPDR Gold Shares, not scoreable on this rubric, 29/100

GLD is a commodity trust. It has no earnings, no guidance, no insiders and no sell-side
price targets, so three of the four gates cannot be passed and the total is meaningless.
What was gathered:

| Field | Value | Source, date |
|---|---|---|
| Close | $406.77, 52w $509.70 to $325.35, 20.2% off the high | finviz, 2026-09-04 |
| Spot gold | about $4,420, down 1.3% on 2026-09-04 after the strong August jobs report revived hike bets | USAGold |
| AUM, fee, holdings | $149.29B, 0.40% expense ratio, about 1,056.6 tonnes held (2026-09-02) | stockanalysis.com/etf/GLD/ |
| Flows | Directionally positive in August, +$3.38B in the week of 8/21. No clean 1m or 3m total found. | record |
| Bank forecasts | Goldman $4,900 end-2026 and $5,400-5,600 for 2027; JPMorgan and UBS $5,400 end-2027; Morgan Stanley $4,800 Q4 2026. Not converted to a GLD basis: the targets are calendar-year-end points, not rolling twelve-month, and a forced conversion would have been invented precision. | record |
| Central banks | Buying roughly 60 tonnes a month per Goldman | record |
| Chart | **+4.6% above the 50-day, -2.1% below the 200-day.** RS 1m +4.2pp, 3m -1.8pp against SPY. In a base. | finviz |
| Catalyst | **FOMC 2026-09-16, company-confirmed date.** The single event that matters for it in the window. | federalreserve.gov |

Judgment: prospect 5, central-bank buying is observed rather than forecast. Competition 2,
scored as substitution to this vehicle rather than to the metal: GLD charges 0.40% against
GLDM at 0.10% and IAU at 0.25% for the same exposure, so the incumbent steadily loses flow
to its own cheaper clones. Macro fit 4, genuinely two-sided and the hawkish side is
currently winning. Narrative 4, the debasement and geopolitics story is live but its
counter-narrative is the fastest-accelerating theme in the macro brief.

## Verdicts, after the red team

No ledger existed before this probe, so `analysis_output/verdicts.jsonl` starts here and
no calibration against earlier verdicts is possible. That is the first thing the next
probe should do.

The red team was run on the four names carrying verdicts and it changed three of them. Its
strongest general finding: **every kill criterion was anchored to an aggregator earnings
date marked `confirmed: false`**, so none of them was reliably measurable on the date
stated. All four were rewritten to be measurable without a confirmed date.

### IONQ — pass, despite passing all four gates

**Edge.** Weak. The one real signal is the doctrine's "estimates up, price down" setup:
FY26 revenue consensus moved from $268.2M at the 5 August print to $287.17M by 19 August,
+7.1%, while the stock sits 53.3% below its high. Everything else is against it.

**Scenario tree**, twelve months, from $39.52:

| Case | Price | p | Condition |
|---|---|---|---|
| Bull | $70 | 0.28 | FY26 revenue at the top of the $280-290M guide, FY27 consensus of $407M holds, a named contract of scale lands, and real yields fall |
| Base | $38 | 0.38 | Revenue delivers as guided and the multiple compresses against the burn |
| Bear | $18 | 0.34 | The $310-330M FY26 adjusted EBITDA loss forces an equity or convertible raise into a hawkish tape, and the quantum de-rating continues |

**Expected return +1.6%** against a 5.37% hurdle. Bear-case loss 54%.

**Red team's strongest fact against the verdict:** IONQ trades at 64.96x EV/sales against
RGTI at 351.03x and QBTS at 456.90x, and is described as having the most revenue, deepest
cash and fullest catalyst slate of the pure-play group. It also pointed out that
institutions added into exactly the drawdown the verdict treats as disqualifying: holders
up 527 against 143, with UBS AM adding 45% and Amundi 15.5%. That argument moved the bull
probability from 0.25 to 0.28 and the expected return from -1.3% to +1.6%. It still does
not clear the hurdle, and it does not touch the burn.

**Pre-mortem.** Twelve months on, down 40%: the company financed a $310-330M EBITDA loss
with equity into a falling tape, and dilution on top of stock compensation already running
at 182.6% of revenue did the rest.

**Kill criterion**, rewritten to be date-independent: **any FY26 revenue guidance update
showing below $280M, or any equity or convertible raise announced, before 31 December
2026.**

**Size: pass.** If it is held anyway, it is a sleeve position with that kill date written
down, never core. It fails every one of the mandate's risk tests.

### RKT — pass, but closer than the first read

**Edge.** Originally written as "none, beta on a rate cut". The red team showed that is
wrong, and the verdict was corrected.

**Scenario tree**, twelve months, from $14.06:

| Case | Price | p | Condition |
|---|---|---|---|
| Bull | $19 | 0.22 | Soft September CPI, the hike priced out, the ten-year back toward 4.2%, volumes recover and the $500M synergy target gets credit |
| Base | $15.50 | 0.45 | Rates plateau, Q3 lands inside the cut guide, and synergy delivery continues at the pace already disclosed |
| Bear | $9.50 | 0.33 | The Fed hikes in September and again by December, the ten-year goes above 5%, volumes fall further and -$774M free cash flow forces balance-sheet attention |

**Expected return +1.6%** against a 5.37% hurdle. Bear-case loss 32%.

**Red team's strongest fact against the verdict:** Amundi added 152.1%, or 13.7M shares,
Wellington 64.5%, or 9.0M shares, and Atreides 69.7%, or 6.1M shares, **after** the Q2 miss
and the Q3 guide cut. Real money bought the bad print. It also named an idiosyncratic path
the original tree omitted entirely: the Redfin-sourced mortgage attach rate is already at
47%, home-equity volume has doubled year over year, and $100M of the $500M synergy target
was realised in Q2, so there is a route that pays without the Fed reversing. The base case
was raised from $13.50 to $15.50 to carry it, and the expected return moved from -6.1% to
+1.6%.

**Pre-mortem.** Down 40%: rates went up rather than down, and the synergy story was not
large enough to matter against origination volume.

**Kill criterion**, with the red team's buffer: **the 16 September FOMC delivers a hike, or
no Q3 print with revenue at or above $2.5B has appeared by 15 November 2026.**

**Size: pass.** Macro fit is the worst in the probe. A name whose primary driver is the one
variable the regime is moving against does not belong in a medium-to-low-risk book,
whatever the institutional flow says.

### TPL — the best business here, and not at this price

**Edge.** Real, and of the disagreement kind. The market prices TPL as an oil royalty at
37.1x forward. Water and surface was $165.5M of $482.9M of first-half revenue, about 34%,
and that half is contracted infrastructure that does not deserve a royalty multiple.

**Scenario tree**, twelve months, from $362.42:

| Case | Price | p | Condition |
|---|---|---|---|
| Bull | $500 | 0.27 | Water and surface keeps compounding above 30% of the mix, Chevron Kilby volumes ramp, WTI holds above $85, and the non-oil half re-rates |
| Base | $400 | 0.40 | Royalty revenue tracks Permian volumes flat, water grows, 97% cash conversion continues, modest re-rating |
| Bear | $270 | 0.33 | The Iran premium unwinds and WTI returns to $70, **or** expenses keep outgrowing revenue as they did in Q1, and the 37.1x multiple compresses toward the VNOM 18.7x and KRP 16.4x peer group |

**Expected return +6.0%** against a 5.37% hurdle. Bear-case loss 25.5%.

**Red team's strongest fact against the verdict:** Q1 2026 adjusted EBITDA missed by 11%
"as expenses outgrew revenue" — a cost-discipline problem entirely uncorrelated with the
oil and water framework the whole tree was built on. It also noted that with two analysts
and a $245 to $639 target range, the risk-to-reward arithmetic rests on very thin, very
dispersed consensus. That raised the bear probability from 0.25 to 0.33 and cut the
expected return from +9.7% to +6.0%.

**This is what demotes TPL.** A 6.0% expected return against a 5.37% credit hurdle is a
premium of about sixty basis points for taking oil beta, a 25.5% bear case and a
two-analyst consensus. That is not compensation. The business is the best in the probe and
the price is wrong.

**Pre-mortem.** Down 40%: the Hormuz premium unwound, and a 37x multiple on a royalty
stream had no support once the commodity rolled over.

**Kill criterion**, with the red team's filing fix: **WTI closes below $75 for ten
consecutive sessions, or the Q3 10-Q, expected mid-to-late November 2026, shows water and
surface revenue below 30% of total.**

**Size: pass at $362.** It becomes interesting nearer the $269 anchor, where the same tree
would give roughly 2 : 1 to the base case.

### QCOM — hold what you own, do not add

**Edge.** Timing and valuation. 16.6x forward with $9,979M of TTM free cash flow, the
cheapest in its peer set, with the Apple modem loss now largely in consensus.

**Scenario tree**, twelve months, from $168.74:

| Case | Price | p | Condition |
|---|---|---|---|
| Bull | $210 | 0.24 | The auto exit-rate reaches $6B and a data-centre design win is announced, and the market pays a cash-flow multiple for the diversified half |
| Base | $190 | 0.44 | Automotive alone sustains its disclosed ~38% year-over-year growth and gross margin stabilises near 53%, re-rating the stock off a 16.6x multiple with no new catalyst required |
| Bear | $130 | 0.32 | Handset weakness deepens with the Apple loss, gross margin slides below 53%, and the multiple compresses to 12x |

**Expected return +4.1%** against a 5.37% hurdle. Bear-case loss 23%.

**Red team's strongest fact against the verdict:** the stock gapped down to $147.61 after
the 29 July print and had recovered to $168.74 by 4 September, **above the $155.68
pre-print close**. The market has already re-absorbed the news the bear case leans on. It
also replaced the conjunctive bull case with a lower bar: automotive continuing a trend
already in the data, with margin merely stabilising, gets to $190-200 without a new event.
That became the base case, and the expected return moved from +1.6% to +4.1%.

**Pre-mortem.** Down 40%: the Apple modem loss turned out to be the start of a share-loss
cycle rather than a one-off, and the cheap multiple got cheaper.

**Kill criterion**, with the red team's correction that Qualcomm guides the next quarter
rather than the full year at its Q4 call: **gross margin prints below 52%, or the Q1 FY27
revenue guidance issued at the Q4 FY26 report comes in below the current $9.7-10.5B
run-rate.**

**Size: hold, do not add.** It is the right shape for the regime and the wrong price for a
20% upside gate. It becomes a buy nearer $150, where the same tree clears the hurdle with a
proper premium.

## Fit to the mandate

The mandate is high return at medium-to-low risk over one to three years. The risk tests
are: drawdown from the high under about 30%, short interest under 10% of float, volatility
not in the top decile, no binary event inside three months, and macro fit not negative.

**No name in the Runway tier fits the mandate.** IONQ is the only name that passes all four
gates and it fails every risk test: 53.3% off its high, 11.18% short interest, top-decile
volatility, and the worst macro fit in the probe bar RKT.

Against the risk screen alone:

- **PLPC passes every test**: 21.1% off its high, 5.03% short interest, a small-cap
  industrial with widening margins, no binary event, macro fit neutral. It fails the
  probe's upside gate only because two analysts cover it and neither has published a target
  since March. That is an absence of coverage, not an absence of upside, and it is the one
  name here where the probe's machinery and the mandate genuinely disagree.
- **QCOM fails on drawdown** at 35.1% and on nothing else. Right shape, wrong price.
- **TPL fails on drawdown** at 33.8% and on nothing else. Right shape, right business,
  wrong price.
- **TEM, AMKR, IONQ and RKT** each fail two or more.
- **GLD** is not scoreable against these tests; it is a macro instrument, sized as one.

The honest conclusion for a medium-to-low-risk book: **nothing on this list is a core buy
at these prices.** Two names, TPL and QCOM, are the right shape and are waiting on price.
One name, PLPC, passes the risk screen and cannot be measured for upside. The rest fail on
the business, the regime, or both.
