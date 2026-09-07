---
name: runway-probe
description: Produce a Runway Probe - rank the names from a Corpus Probe by their chance of further gain from today's price. Reads twelve signals in four groups (fundamentals, flows and positioning, price and chart, context) from the corpus and the web, scores them on a fixed rubric, and publishes in the fixed Runway Probe format. Use when asked "which of these have runway", "which have the higher chance of gain from here", or to check earnings, analyst comment, insider and institutional activity, chart, macro fit or competition on a list of tickers.
argument-hint: "[path to the corpus probe html, default: newest in data/analysis/probes] [--mandate '...'] [--tickers A,B,C to override the list]"
---

# Runway Probe

## The problem, and how it is solved

The corpus probe tiers names on what the accounts said over a window that ended days or
weeks ago, with no price layer. It cannot say whether a name still has room from today's
price, whether the business is actually delivering, whether the people with the most
information are buying or selling, whether the chart agrees, or whether the macro
climate and the market's current narrative favour the name. The runway probe answers
all of that with a fixed set of twelve signals, gathered once per name, scored on one
rubric, and written into the same page structure every time so probes from different
windows read side by side.

The signals, in four groups:

| Group | Signal | Answers |
|---|---|---|
| Fundamentals | Earnings | Is the business delivering, and are estimates moving up or down? |
| | Prospect | What has to happen over 12 months for the stock to work, and how likely is it? |
| | Competition | Does the company have a moat, or is share moving against it? |
| Flows and positioning | Insider activity | Are officers and directors buying with their own money, or selling? |
| | Institutional flow | Are 13F filers net adding or cutting, and who? Short interest? |
| | Retail interest | How crowded is the name among the corpus accounts and their audiences? |
| Price and chart | Current price and upside | Where is it against consensus, its highs and lows? |
| | Risk : reward | How much can be made against how much can be lost to the nearest anchor? |
| | Daily chart | Trend, moving averages, base or breakdown, relative strength, volume on the print. |
| Context | Macro climate | Rates, dollar, credit, oil, Fed path, factor leadership, and whether the name's shape fits. |
| | Narrative harmony | Does the name sit inside the market's live themes, and is that theme accelerating or fading? |
| | Catalysts | Dated events in 3 months that resolve the thesis either way. |

Each signal has a definition, a source, an interpretation rule and a score in
`scorecard.md`. The interpretation rules are the durable findings of the empirical
literature and practitioner experience: post-earnings-announcement drift and estimate
revision momentum, insider cluster buying, the contrarian value of crowding, trend
persistence and the 200-day line, duration sensitivity to the rate regime. They are
written down so every probe applies them the same way.

Reference output: `analysis_output/2026-09-06-runway-probe.html`. The page format does
not change. The richer signal set changes what goes *into* the cells and the ranking,
and is preserved in full in a companion evidence file beside the page.

## Inputs

| Input | Where | If missing |
|---|---|---|
| Ticker list with the tier each name held | tier cards of the newest `data/analysis/probes/<date>-probe.html` | `--tickers` overrides; otherwise run `/corpus-probe` first |
| Mandate | the corpus probe's meta strip, or `--mandate` | default `high return, medium-to-low risk, 1 to 3 years` |
| Corpus stance and retail interest | `pnpm q retail-interest --symbols "A,B,C"`, `scripts/mine-corpus-signals.py`, `data/analysis/accounts/*.json` | run `/fetch` for the window |
| Corpus regime facts | the macro accounts' posts in `data/_session/*.posts.jsonl` and the corpus probe's "lens" section | `pnpm task:session-dump` regenerates the bundles |
| Outside data | WebFetch of the pinned pages in `sources.md`, via subagents; WebSearch only as the registry's fallback | none; this probe cannot run offline |
| Per-name records | `analysis_output/<window_end>-runway-data/<TICKER>.json` in the shape of `record.schema.md` | the research subagents write them in step 3 |
| Price history | not in the repo; from the web per name | say so in the caveats; never compute a return the corpus could later contradict |

## Data sourcing discipline

The probe has no market-data layer yet, so determinism comes from procedure:

- **One page per field.** `sources.md` names the primary, secondary and tertiary URL for
  every field group, per ticker and for the macro brief. Subagents WebFetch the pinned
  page first and fall back in order. WebSearch is allowed only for "why it fell", the
  live themes, and pages the registry does not cover. The URL actually read is recorded
  on every value.
- **Records, not prose.** Each ticker's evidence is a JSON file in the shape of
  `record.schema.md`, every leaf `{value, source, as_of}`, under
  `analysis_output/<window_end>-runway-data/`. The corpus-side inputs (`retail.json`,
  `stances.json`) and the macro brief (`macro.json`) sit beside them, with a
  `_manifest.json` naming the price date, the 13F quarter-end, the tickers, and every
  source that failed.
- **Mechanical points are computed, not judged.** `scripts/build-scorecard.py` reads the
  records and derives upside, drawdown, the downside anchor, risk : reward, the four
  gates, the tier, and the points for earnings, insider, institutional, retail, upside,
  risk : reward and chart, exactly as `scorecard.md` states them. Two runs over the same
  records give the same numbers.
- **Judgment is separate and labelled.** Prospect, competition, macro fit and narrative
  harmony are filled by the main agent into each record's `judgment` block with a
  one-line reason, after the macro brief and the corpus read. The script adds them
  without modification and lists any ticker whose judgment block is incomplete.
- **Failures are logged forward.** A source that blocks or changes shape goes into the
  manifest and into the failure log at the foot of `sources.md`, so the next run does
  not rediscover it.

## The chain

```
mandate + hurdle ─┐
corpus context ───┼─► evidence records ─► scorecard ─► perception ─► scenarios ─► red team ─► verdict + size ─► publish ─► ledger
macro regime ─────┘        (subagents)      (script)    (doctrine)   (doctrine §4)  (subagent)                                 (script)
```

Gathering is parallel and deterministic; perceiving and deciding are sequential and
follow `doctrine.md`, which says what each data point means, what it does not mean, its
base rate, its traps, and how the signals interact. Read the doctrine before step 4.

## Process

Steps 1 to 3 are independent. Run them in one message where the tool allows it.

### 1. Corpus side, in the main context

```bash
mkdir -p analysis_output/<window_end>-runway-data
python3 .claude/skills/runway-probe/scripts/mine-corpus-signals.py <TICKERS>
pnpm -s q retail-interest --symbols "<TICKERS>" --json > analysis_output/<window_end>-runway-data/retail.json
```

Write `stances.json` from the analysis JSONs (per ticker: account, direction,
conviction, time_frame) and start `_manifest.json` with the window, tickers and groups.

The first prints every corpus post that pairs a ticker with an analyst or institutional
keyword. Most "PTs" in it are commentators' own; the real broker relays and insider
filings are the corpus-side evidence. The second gives, per ticker, how many accounts
mentioned it, on how many days, with what engagement, and every formal stance with its
conviction. From the analysis JSONs, note each name's sponsoring account and what the
corpus probe said about that account's reliability.

### 2. Macro climate, one subagent

Launch one `general-purpose` subagent with `macro-brief.md`. It returns the current
regime in a fixed shape: policy rate and the priced path, the 2s10s and 10-year level,
IG and HY spreads, the dollar, oil, VIX, the last payrolls and CPI prints, factor and
sector leadership over 1 and 3 months, and the dated macro events in the next 3 months.
Merge it with the corpus's own regime facts (the rates-and-credit account's posts are
usually sharper than the aggregators). The macro section of the scorecard is applied
from this one brief to every name, so it is gathered once.

### 3. Per-name evidence, one subagent per group of at most eight tickers

Split the list into groups of at most eight, launch one `general-purpose` subagent per
group in a single message, each with `research-brief.md` and its tickers. The brief
fixes twenty columns so the group tables merge unedited. Budget is 4 to 6 searches per
name. Known source behaviour, so the write-up can say what was not verifiable:

- Fintel, WhaleWisdom, OpenInsider and Nasdaq holdings pages often return 403 or time
  out. Finviz is the working substitute for insider tables and moving-average distances;
  StockAnalysis and MarketBeat for targets, estimates and revision history.
- MarketBeat institutional pages carry a recurring CalSTRS row showing implausible
  multi-thousand-percent increases. Exclude it; use holder counts, not dollar totals, on
  any name where it appears.
- MarketBeat averages lag target cuts; StockAnalysis (S&P Global) reflects them faster.
  Where they disagree by more than ten points, show both as a range.
- "BlackRock / Norges / BNY new multibillion position" alerts are filer-entity changes.
- Earnings dates from aggregators are estimates until the company confirms.

### 4. Score every name on the rubric

When the records are in, fill the `judgment` block of every record (prospect,
competition, macro fit, narrative harmony, each with points from `scorecard.md` and a
one-line reason), then run:

```bash
python3 .claude/skills/runway-probe/scripts/build-scorecard.py analysis_output/<window_end>-runway-data
```

It writes `scorecard.json` and `scorecard.md` beside the records: derived numbers,
points per signal, the four gates, the tier and the total, sorted by tier then score.
It names any ticker whose judgment block is incomplete; finish those and rerun. Read
the `why` strings; if one looks wrong, fix the record, never the script's output. The
gates decide the tier; the score decides the order inside a tier.

| Tier | Gate |
|---|---|
| **Runway** | all four gates pass: upside gate, flow gate, insider gate, delivery gate; and risk : reward at or above 2 : 1 |
| **One leg missing** | exactly one gate fails, and the failure has a dated resolution |
| **No runway on the numbers** | two or more gates fail, or price is at or above consensus, or R : R below 1.5 : 1 |

A name with a 90-point score and a failed delivery gate (guidance cut, negative
revisions) is still One leg missing. The gates exist so that a great story cannot
out-score a deteriorating business.

### 4b. Perceive, then decide

Follow `doctrine.md` section 2 for every Runway and One-leg-missing name: the
second-order reads and the interaction table are where the verdict comes from, not the
total. Then section 4: state the edge, build the bull, base and bear scenario tree with
probabilities and conditions, compute the expected return, compare it to the hurdle
from the macro brief, write the kill criterion with a number and a date, and run the
pre-mortem. Read `analysis_output/verdicts.jsonl` first for any earlier verdict on the
same ticker and say whether it has held.

### 4c. Red team

Launch one `general-purpose` subagent with `redteam-brief.md` and the top Runway names.
It argues the bear case from the same records and must name the single strongest fact
against each verdict. Its answer goes into the "What can break it" cell, and a verdict
it breaks moves down a tier.

### 5. Fit to the mandate

From the Runway tier, name the subset that fits the mandate's risk (for medium-to-low
risk: drawdown from high under about 30%, short interest under 10% of float, beta or
implied volatility not in the top decile, no binary event inside three months, macro fit
not negative). The rest is a capped satellite sleeve. Say so.

### 6. Write, then publish

Copy `template.html` to `analysis_output/<window_end>-runway-probe.html`, fill every
section in the fixed order below, and publish with the Artifact tool. Title is
`<Month> Runway Probe`. Favicon is 🛫 on first publish; omit it when republishing the
same file. Description names the count of names and the signal groups.

Then write `verdicts.json` in the data directory (shape in
`scripts/register-verdicts.py`) and register it:

```bash
python3 .claude/skills/runway-probe/scripts/register-verdicts.py analysis_output/<window_end>-runway-data
```

That appends every verdict with its close, date, scenario tree, expected return, kill
criterion and size to `analysis_output/verdicts.jsonl`. The next probe reads it to score
this one; the calibration note goes in "What this probe cannot tell you".

Write the companion `analysis_output/<window_end>-runway-evidence.md` at the same time:
the manifest summary (price date, 13F vintage, sources failed), the macro brief table,
the generated `scorecard.md` table, then one block per ticker holding the twenty-column
summary row, the judgment reasons, and the source URL and date of every figure that
decided a gate. The records directory stays beside it as the raw evidence. The page is
the reading surface; the evidence file and the records are where the next probe, or a
reader who doubts a cell, goes to check.

## Where each signal lands on the page

The page keeps its ten sections and its columns. The signals map onto them like this:

| Section | Carries |
|---|---|
| Meta strip | mandate, names probed, the four signal groups, 13F vintage, price date |
| Tier cards | the gate outcomes; the small line states the gate rule |
| How the signals were read | one bullet per group (four bullets), then the reading-rule callout naming the gates |
| Runway table | Upside cell also carries the R : R as `+46% · 3.1:1`; Consensus cell adds the 90-day revision direction; Institutional cell adds short interest; Insider cell keeps buys and sells; What can break it carries the kill criterion with its date and the red team's strongest fact |
| One leg missing | the failed gate first, then the dated event that resolves it |
| No runway | grouped by the failing reason; add "Chart broken" and "Macro shape wrong" to the reasons where they apply |
| Fit to the mandate | the risk tests above, plus macro fit; each fit name's edge in one clause and its expected return against the hurdle, as words not a table |
| All N names | Institutional column also carries short interest; Insiders as before; Next dated event as before; Consensus cell carries the score in mono, e.g. `Strong Buy, 20 · 82` |
| What this probe cannot tell you | 13F vintage, blocked sources, unconfirmed dates, that chart reads are from aggregator moving-average distances not a full price series, that competition and prospect are judgment calls stated as such |
| Footer | sources with fetch date, and the evidence file name |

## Rules

- **Every number carries its source and date**, on the page in the cell or `.src` line
  and in the evidence file in full.
- **Upside is target divided by close, nothing else.** No corpus-based return is ever
  computed here.
- **Selling is evidence.** An insider cell that says "None" when the CEO sold nine
  figures is wrong. Write the sale.
- **Crowding is contrarian at the extremes.** A retail-interest score is high when the
  name is quiet with fundamentals, not when it is loud.
- **Show disagreement as a range**, never the friendlier number.
- **"Not found" is an answer.** A blank cell is not.
- **Judgment is labelled.** Prospect, competition and narrative harmony are analyst
  calls. Write them as "the case is", not as facts.
- **Every verdict is falsifiable.** A kill criterion has an observation, a number and
  a date. A verdict without one does not get published.
- **The probe keeps score.** Every Runway and One-leg-missing verdict is registered in
  the ledger, and the next probe reports how the earlier ones did.
- **Prose style.** Short sentences. No em dashes, no parentheticals, no arrows.
  Tickers in `<span class="t">`, figures in `<span class="num">`, upside bars capped
  at 100%.
- **Do not change the template CSS or section order.**

## Done when

- every ticker from the input list is in exactly one tier card and one appendix row
- every ticker has a record under `analysis_output/<window_end>-runway-data/` with every
  leaf carrying a source URL and date or a "not found" note, a filled judgment block,
  and a row in the generated `scorecard.json`
- `_manifest.json` lists every source that failed, and `sources.md`'s failure log has
  a line for any new behaviour
- every Runway row has all cells filled with a source
- every Runway and One-leg-missing name has a scenario tree, an expected return against
  the hurdle, a kill criterion with a date, a pre-mortem line and a red-team fact, and is
  registered in `analysis_output/verdicts.jsonl`
- the page and the evidence file exist under `analysis_output/` and the artifact URL is
  in the final message
