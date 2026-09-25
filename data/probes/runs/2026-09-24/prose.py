"""Prose for the 2026-09-24 runway page. Tickers in <span class="t">, figures in <span class="num">."""


def t(x):
    return f'<span class="t">{x}</span>'


def n(x):
    return f'<span class="num">{x}</span>'


TIERLABEL = {"runway": "runway", "one_leg_missing": "one leg", "no_runway": "no runway"}

LEDE = ("Which of the 123 stocks the fourteen accounts named since 7 July can still run over the next three to six "
        "months from today's price. The answer is short. One name passes every gate. The rest need a dated event first, "
        "because the Fed is hiking into an oil shock and the 10-year sits at 5.11%.")

RUNWAY = ["UNH"]
ONELEG = ["NVDA", "VST", "NU", "BABA", "CRDO", "WDC", "GRAB", "UBER", "UUUU", "KURA", "AMZN", "LRCX", "ASML",
          "AMAT", "NXPI", "APP", "AVGO", "CSCO", "OSCR", "GLW", "SOFI", "RDDT", "PLPC", "AKAM", "SPCX",
          "APLD", "ORCL", "IREN", "ACHR", "WULF", "RKLB", "CIFR", "ONDS", "EOSE"]
NORUN_CARD = ("TXN AMBA DAL RARE STIM GRRR WYFI META MU SNDK ARM AI PSNL ANET LITE SNOW CAT GEV GOOGL COHR "
              "ON VIAV GS ABCL SE CCJ CRWV SKHY NBIS ALAB PYPL CRM ISRG STLN AMKR AAOI NKE ASTS ADUR "
              "<br>plus 49 screened out on the Finviz pass")

BREAK = {
    "UNH": ("Kill if the 13 Oct Q3 print holds or cuts the FY26 range below its $19.75 midpoint, or reports a medical "
            "care ratio above guidance. Red team: revisions up is only +0.3% in 30 days, and the Optum CEO sold $661K "
            "outside a plan. Expected +6.9% in six months against an 8% bar."),
}

_ONE = {
    "NVDA": ("Insider fails: director Stevens sold $947M in September, plan status unverified.",
             "Everything else passes: Q3 guide raised to $105.8-110.2B, revisions 39 up and 1 down, 14.3x FY28 earnings or 24x FY27. The late-November print resolves it. Kill if the Q4 guide is below $118B. Expected +8.4%, the only name above the core bar. Core starter size."),
    "VST": ("Delivery fails: Q2 revenue $4.02B against $5.46B.",
            "The CEO bought three times on the open market near the low, $1.17M, and the fleet is the cash-flow shape this regime pays for. A new hyperscaler PPA or the early-November print reaffirming $6.8-7.6B EBITDA resolves it. Expected +11%."),
    "NU": ("Insider fails: the Form 4 record is not verified complete.",
           "ROE 33% at 12x forward earnings with revisions up. The 12 Nov print decides it. Kill on 90-day NPL above 7.5%. Expected +10%."),
    "BABA": ("Delivery fails: 90-day revisions down, 11 up and 17 down.",
             "The chairman and CEO bought $25.7M on the open market into the $10.2B placement. The late-November print must show cloud above 40% with capex paying back. Expected +10%, below the satellite bar."),
    "CRDO": ("Insider fails: $101.5M of sales, mostly planned.",
             "Revisions 14 up and 2 down at 20x after a -20% print day. The 2 Dec print resolves it if gross margin is back above 66%. Expected +10%."),
    "WDC": ("Upside fails on MarketBeat's $535 against StockAnalysis's $665.",
            "Estimates up after a beat and raise that fell 13%. The 29 Oct print resolves it. Expected +9%."),
    "GRAB": ("Moved down by the red team: base case misses the satellite bar.",
             "CEO Anthony Tan bought $29.9M on 21 Sep after a 53% drawdown, the largest insider buy in the set. Kill below the $2.74 low or on Q3 EBITDA implying less than $720M. Expected +9%."),
    "UBER": ("Delivery fails: Q2 revenue $14.19B against $14.24B.",
             "The CEO bought $10.0M and the COO $5.3M in September. Revisions 27 up and 2 down at 15.6x. The 3 Nov print resolves it; kill on bookings below $58.25B. Red team: an SVP sold $2.0M outside a plan the next day, and Cybercab is live in Austin. Expected +7.6%."),
    "UUUU": ("Delivery fails: Q2 revenue $25.1M against about $30.8M.",
             "The CEO bought $968K, lifting his holding 41%, and 13F holders added. Rare-earth pricing is the risk. Expected +7%."),
    "KURA": ("Moved down by the red team: base case misses the satellite bar.",
             "The CEO bought $2.35M on the open market in August. The Q4 update is Phase 1 data at an unconfirmed ASH venue. Kill on Q3 KOMZIFTI sales below $12M on about 3 Nov. Binary inside three months, so never core."),
    "AMZN": ("Insider fails: Bezos sold $346.5M under a plan.",
             "AWS re-accelerated to +37%. The 29 Oct print resolves it; kill on AWS below 30%. Expected +6.7%."),
    "LRCX": ("Insider fails: $58.3M of planned sales across five officers.",
             "Beat and raise, revisions up. The 21 Oct print resolves it."),
    "ASML": ("Insider fails: foreign issuer, no Form 4 coverage.",
             "Guide raised, revisions 28 up and 0 down. The 14 Oct print resolves it."),
    "AMAT": ("Insider fails: CEO Dickerson sold $55.6M on 29 and 30 June.",
             "Estimates up after a sell-the-news print. The 12 Nov print resolves it."),
    "NXPI": ("Moved down by the red team: estimates are flat, not up.",
             "15.3x FY26 earnings after a -10.8% post-print week. The 27 Oct print must guide Q4 at or above $3.7B."),
    "APP": ("Delivery fails: Q3 guided below consensus.",
            "15.6x with FCF equal to net income. The 4 Nov print resolves it."),
    "AVGO": ("Moved down by the red team: FY27 revisions 25 down and 11 up.",
             "A lagging label until estimates turn. The 9 Dec print resolves it; kill on FY27 EPS below 19.0."),
    "CSCO": ("Moved down by the red team: the FY27 guide midpoint sits below consensus.",
             "The FQ1 beat is timing inside the year. The 11 Nov print must hold gross margin above 63.5%."),
    "OSCR": ("Upside fails at 20%.", "Beat and raise with 8 up and 0 down revisions. ACA subsidy policy is the dated risk."),
    "GLW": ("Upside fails on MarketBeat's lower average.", "Optical growth at 35x in a lagging theme. The 27 Oct print resolves it."),
    "SOFI": ("Upside fails at 21% with a 34% range.", "Members +35%. The 27 Oct print resolves it."),
    "RDDT": ("Insider fails: $50.1M of planned CEO and COO sales.", "US logged-in users are the test at the 29 Oct print."),
    "PLPC": ("Upside fails: no current consensus exists.", "Record Q2 with margin 29.7% to 34.3%. The 28 Oct print resolves it."),
    "AKAM": ("Delivery fails: the FY EPS guide was trimmed.", "Cash-flow value at 15.5x. The 5 Nov print resolves it."),
    "SPCX": ("Insider fails: the COO sold $52.5M under a plan.",
             "Lock-up tranches of 328M shares open on 24 Sep, 9 Oct and 24 Oct, then about 800M on 8 Dec. Kill below the $135 IPO price after 24 Oct."),
    "APLD": ("Moved down by the red team: the consensus is stale.", "Newest targets average about $33 against $66. Pass."),
    "ORCL": ("Moved down by the red team: the balance sheet needs the regime to change.", "FCF -$28.7B against $169B of debt. Pass."),
    "IREN": ("Delivery fails: FY27 EPS cut from -0.94 to -3.42 in 30 days.", "Pass until the 10-year is below 4.75%."),
    "ACHR": ("Delivery fails: no certification, no guide.", "Pass."),
    "WULF": ("Delivery fails.", "SBC 128% of revenue, short 35%. Pass."),
    "RKLB": ("Insider fails: the CEO's trust sold $286M, and a $1.94B ATM is open.", "Neutron slipping toward 2027. Pass."),
    "CIFR": ("Delivery fails: Q2 gross margin -131%.", "Pass."),
    "ONDS": ("Delivery fails.", "Short 42%, share count +259% in a year. Pass."),
    "EOSE": ("Delivery fails: revenue guide cut.", "Gross margin -71%. Pass."),
}
ONELEG_DL = "\n".join(f'    <dt>{k}</dt><dd><b>{a}</b> {b}</dd>' for k, (a, b) in ((k, _ONE[k]) for k in ONELEG))

NORUN_UL = "\n".join(f"    <li>{x}</li>" for x in [
    f"<b>Moved down by the red team.</b> {t('TXN')} base case +5% below the bar. {t('AMBA')} has no edge. {t('DAL')} consensus fell below its own guide on fuel. {t('RARE')} failed its Angelman Phase 3 on 2 Sep. {t('STIM')} carries a going-concern flag. {t('GRRR')} and {t('WYFI')} are dilution and financing stories.",
    f"<b>At or above consensus.</b> {t('META')} at a new high, {n('-2%')} to target. {t('ARM')} {n('-6%')}, {t('AI')} {n('-23%')} with a Sell consensus, {t('PSNL')} trades above the $16.25 Tempus deal value. {t('ALAB')}, {t('NBIS')}, {t('PYPL')}, {t('ANET')}, {t('CRM')} and {t('ISRG')} sit under 20%.",
    f"<b>Upside against insider selling.</b> {t('MU')} officers sold $182M, the CEO $122M under a plan, into the 30 Sep print. {t('SNDK')} $121M, {t('LITE')} $63M, {t('SNOW')} $556M. Memory has the best estimate momentum in the set; the price already has it.",
    f"<b>Reward does not cover the stop.</b> {t('CAT')}, {t('GEV')}, {t('GOOGL')}, {t('COHR')}, {t('VIAV')}, {t('ON')}, {t('STLN')}, {t('GS')}, {t('AMKR')}, {t('AAOI')}, {t('NKE')} and {t('ASTS')} all score R:R below 1.5 because the nearest real anchor is the low target or the 52-week low. {t('ABCL')} has a binary readout on 30 Sep to 3 Oct.",
    f"<b>Two legs missing.</b> {t('SE')}, whose executives sold about $276M since the print. {t('CCJ')}, {t('CRWV')}, {t('ADUR')} and {t('SKHY')}, where insider coverage is unknown and delivery failed.",
    "<b>Screened out on the Finviz pass.</b> 40 names at or within 20% of the Finviz mean target, including "
    + " ".join(t(x) for x in "MSFT AAPL AMD TSLA PLTR CRWD NET ZS PANW OKTA NOW LLY NVO HOOD COIN DELL MRVL INTC TEM HIMS ZETA".split())
    + ", and 9 with two proxy gates failing: " + " ".join(t(x) for x in "TSM VRT CEG GNRC IONQ NFLX MCD NOK AEHR".split()) + ".",
])

FIT = f"""  <p>{t('UNH')} is the only name that fits: drawdown {n('19%')}, short interest {n('1.5%')}, beta {n('0.61')}, no binary event, macro fit neutral. Its edge is timing. Estimates rise while the price has fallen for three months. The scenario tree gives {n('+6.9%')} over six months against an {n('8%')} bar built from a single-A yield near {n('5.6%')}. So it is a half position now and a full one if the 13 Oct print raises the range again.</p>
  <p>{t('NVDA')} is the other core starter. It clears the bar at {n('+8.4%')}, but its insider leg fails, and it is the loudest name in the corpus, with 259 posts from 10 accounts. Add after the late-November guide holds.</p>
  <p>Everything else waits for its date. The strongest insider-backed setups are {t('GRAB')}, {t('UBER')}, {t('BABA')}, {t('VST')}, {t('KURA')} and {t('UUUU')}, where officers bought with their own money after drawdowns. None clears the {n('20%')} satellite bar on its own tree today. The neoclouds, space, nuclear and speculative names are passes while real yields sit at {n('2.76%')}. The book stays at the outlook's {n('60%')} gross, with T-bills paying about {n('2.4%')} for the six months as the hurdle's floor.</p>"""

APPX_SRC = ('<p class="src">Tier is this probe\'s final placement after the red team; "screened" names were ranked on the Finviz snapshot only. '
            "Flow is MarketBeat's trailing-twelve-month buyer and seller counts, not a quarter-on-quarter 13F change. "
            "SI is short interest as a percent of float. The number after the consensus label is the 100-point score. "
            "(est.) marks an aggregator date the company has not confirmed.</p>")

LIMITS = f"""<div class="callout warn">
    The 13F figures describe 30 June 2026 and are twelve weeks stale. Fintel is blocked, so net share changes and new or exited holder counts are missing for every name, and the flow gate rests on MarketBeat's twelve-month counts. Yahoo's analysis page failed for most names, so revisions come from Zacks and StockAnalysis levels. Forward EBIT, cash flow and capex for FY2 sit behind paywalls, so operating-margin, FCF-growth and return-on-capital checks are uncovered. Almost every earnings date is an aggregator estimate; Micron on 30 Sep, Nike on 1 Oct, UNH on 13 Oct and GE Vernova on 28 Oct are confirmed. Chart reads come from moving-average distances, not a full price series. Prospect, competition, macro fit and narrative are analyst judgments and are written as such. The 49 screened-out names were judged on the Finviz mean target alone. Calibration: of the September verdicts still priced, {t('IONQ')} is {n('+14%')} against an expected {n('+2%')} and {t('QCOM')}, called no runway, is {n('+15%')}. Two names is too few to adjust on, but both errors ran the same way, too cautious.
  </div>
  <p>Three things would sharpen the next probe: a quarter-on-quarter 13F source to replace Fintel; opening every Form 4 above $10M to confirm its plan box; and rerunning this page after Micron on 30 Sep and CPI on 14 Oct, which decide the memory and duration calls.</p>"""

FOOT = ('<div class="foot">Sources are Finviz, StockAnalysis (S&amp;P Global), MarketBeat, Yahoo, Zacks, Nasdaq, SEC EDGAR and company releases, '
        "as fetched on 24 Sep 2026, read against the account analyses in data/corpus/analysis/accounts and the macro regime of 24 Sep. "
        "Every figure's URL and date is in data/probes/runway/2026-09-24/records; the scorecard and verdicts are in "
        "data/probes/runway/2026-09-24/evidence.md. Nothing here is investment advice.</div>")
