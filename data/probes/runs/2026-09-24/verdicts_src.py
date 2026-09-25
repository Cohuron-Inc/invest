#!/usr/bin/env python3
"""Verdicts for the 2026-09-24 runway probe. Horizon 6 months (operator asked for 3-6 month runway).
Hurdle: 2y 4.85% + IG OAS 77bp = single-A about 5.6% a year, 2.8% over six months;
equity bar +8% expected over 6 months for core, +20% for satellite. Writes records/verdicts.json."""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parents[3] / "probes/runway/2026-09-24/records/verdicts.json"
H = 6


def v(edge, bull, base, bear, kill, by, pre, red, size, tier_override=None):
    d = {"edge": edge,
         "bull": {"price": bull[0], "p": bull[1], "if": bull[2]},
         "base": {"price": base[0], "p": base[1], "if": base[2]},
         "bear": {"price": bear[0], "p": bear[1], "if": bear[2]},
         "kill": {"observation": kill, "by": by}, "premortem": pre, "redteam_fact": red,
         "size": size, "horizon_months": H}
    if tier_override:
        d["tier_override"] = tier_override
    assert abs(bull[1] + base[1] + bear[1] - 1) < 1e-9
    return d


NR = "not red-teamed: one-leg name; the probe's own strongest fact against"
V = {
# ---------------- one leg missing ----------------
"UBER": v("Discounted signal: the CEO bought $10.0M and the COO $5.3M on the open market in September after a 32% drawdown, while 30-day revisions run 27 up / 2 down. The delivery leg failed on a $50M revenue miss.",
    (92, .25, "Q3 on about 3 Nov shows bookings at the top of $58.25-60.25B and AV partnerships read as supply, not substitution"),
    (78, .40, "bookings in range, EPS $0.84-0.88, the robotaxi fear stays a multiple cap"),
    (58, .35, "Tesla Cybercab expansion and Waymo's own app take share of mind; bookings guide cut"),
    "Q3 gross bookings below $58.25B on about 3 Nov, or a close below the $65.41 52-week low", "2026-11-15",
    "Robotaxi disintermediation became a numbers story, not a fear story.", "An SVP sold $2.0M outside a plan the day after the CEO bought; Tesla Cybercab is live in Austin about 30% below Uber's prices.", "core"),
"TXN": v("Timing: analog recovery with 25 up / 0 down revisions and a gross margin back at 61%, priced at exactly the 20% upside line.",
    (320, .25, "Q3 on 27 Oct beats and guides Q4 above seasonal"), (288, .50, "recovery continues at consensus pace"), (240, .25, "the analog recovery stalls on auto and China"),
    "Q4 revenue guide midpoint below $6.0B, or gross margin below 60%, at the 27 Oct print", "2026-10-31",
    "The recovery was priced; 26x forward earnings de-rated under a 5% 10-year.", "Upside is 19.97% and the base case +5.3% sits below the 8% core hurdle at 26.3x against NXPI 12.7x.", "pass", "no_runway"),
"ASML": v("Quality with guide raised and revisions 28 up / 0 down; the insider leg fails only because a foreign issuer files no Form 4.",
    (2100, .30, "the 14 Oct print lifts 2027 toward the top of the EUR 54.6B consensus"), (1850, .45, "orders in line"), (1450, .25, "China export rules tighten, 2027 orders slip"),
    "Q3 bookings below EUR 5B on 14 Oct, or 2027 revenue commentary below EUR 50B", "2026-10-20",
    "Semicap de-rated as memory capex paused after the pricing peak.", NR + ": the semicap basket is lagging and worsening, -24pp vs SPY over 3 months.", "core"),
"WDC": v("Estimates up after a beat-and-raise met with a -13% print day; the upside leg fails only on MarketBeat's lagging average.",
    (600, .30, "the 29 Oct print confirms exabyte pricing"), (500, .40, "in line"), (370, .30, "the memory cycle turns; HDD pricing discipline breaks"),
    "FQ1 revenue below $4.0B or gross margin below 50% on 29 Oct", "2026-11-05",
    "The storage cycle peaked with memory.", NR + ": cash conversion 0.37x on GAAP gains.", "sleeve"),
"AMAT": v("Estimates up (29 up / 1 down) after a sell-the-news print; the insider leg fails on the CEO's $55.6M sale.",
    (600, .30, "the 12 Nov print guides FY27 WFE up 30%+"), (510, .40, "in line"), (390, .30, "China share keeps falling; WFE digestion"),
    "FQ4 revenue guide below $9.8B, or China below 25% with total down q/q", "2026-11-20",
    "The CEO sold near the top for a reason: WFE digested in 2027.", NR + ": CEO Dickerson sold $55.6M on 29-30 June.", "sleeve"),
"NVDA": v("Earnings momentum at 14.3x forward: guide raised to $105.8-110.2B and revisions 39 up / 1 down. Insider leg fails on director Stevens' $947M sale.",
    (290, .30, "the 25 Nov print beats and guides above $120B"), (245, .45, "in line; the multiple holds"), (185, .25, "a hyperscaler capex cut or long-end tantrum de-rates AI"),
    "Q4 FY27 revenue guide below $118B at the November print, or FY28 EPS consensus below 15.0 on 15 Dec", "2026-12-15",
    "AI capex digested and the loudest name in the corpus had no marginal buyer.", "On FY27 EPS the multiple is 24x, not 14x; FCF is 0.66x net income; the corpus has 259 posts from 10 accounts on it.", "core"),
"LRCX": v("Beat-and-raise with estimates up; the insider leg fails on 10b5-1 sales totalling $58M.",
    (390, .30, "the 21 Oct print guides December quarter above $8.5B"), (335, .40, "in line"), (255, .30, "memory capex pause"),
    "December-quarter revenue guide below $7.7B on 21 Oct", "2026-10-31",
    "Memory makers cut capex after the pricing peak.", NR + ": the semicap basket is lagging and worsening.", "sleeve"),
"NU": v("ROE 33% at 12x forward earnings; the insider leg fails because the Form 4 record is not verified complete.",
    (18, .30, "the 12 Nov print holds 33% ROE and credit quality"), (15, .45, "in line"), (11, .25, "Brazil credit deteriorates"),
    "90-day NPL above 7.5% or ROE below 28% at the Q3 print", "2026-11-20",
    "Brazilian credit turned while the dollar strengthened.", NR + ": fintech fading; the chart below both averages.", "sleeve"),
"AMZN": v("AWS re-acceleration to +37% at 23.5x; the insider leg fails on Bezos's $346.5M planned sale.",
    (310, .30, "Q3 on 29 Oct shows AWS above 35%"), (265, .45, "in line"), (215, .25, "capex overwhelms FCF; retail margin squeezed by oil"),
    "AWS growth below 30% in the Q3 print", "2026-11-05",
    "FCF turned negative and the market repriced the capex.", NR + ": FY1 FCF consensus -$34.2B.", "core"),
"VST": v("Discounted signal: CEO Burke made 3 open-market buys ($1.17M) near the 52-week low; cash-flow shape the regime rewards. Delivery fails on the Q2 revenue miss.",
    (190, .30, "a hyperscaler PPA lands and the Q3 print on about 5 Nov reaffirms EBITDA"), (150, .45, "EBITDA guide held, ERCOT soft"), (115, .25, "ERCOT forward prices keep falling"),
    "EBITDA guide cut below $6.8B, or no new PPA announced", "2026-12-31",
    "Batteries flattened the ERCOT curve faster than PPAs arrived.", NR + ": revisions 0 up / 2 down.", "sleeve"),
"BABA": v("Discounted signal: the chairman and CEO bought $25.7M on the open market into the placement; China AI cloud +45%. Delivery fails on 90-day revisions down.",
    (160, .30, "cloud growth above 40% and capex payback visible at the late-November print"), (120, .40, "in line"), (85, .30, "capex keeps op income falling; US-China escalation"),
    "operating income down more than 50% y/y again at the late-November print", "2026-12-15",
    "Capex never earned its return and the placement was the top of management's confidence.", NR + ": FCF -$11.4B and the buyback cut 80%.", "sleeve"),
"RDDT": v("Beat with revisions up; the insider leg fails on $50.1M of planned CEO and COO sales.",
    (200, .25, "the 29 Oct print shows US DAU stabilising"), (160, .45, "in line"), (115, .30, "AI Overviews erode traffic further"),
    "US logged-in DAU below 52M at the Q3 print", "2026-11-05",
    "Search traffic loss compounded.", NR + ": the Q3 guide sat below consensus.", "sleeve"),
"SPCX": v("First-print beat, revisions up, 144 new holders in the first 13F cycle; the insider leg fails on the COO's $52.5M planned sale. Lock-up supply is the dated risk.",
    (210, .25, "lock-ups absorbed, the Q3 print shows Starlink margin expansion"), (150, .40, "supply absorbed at a flat price"), (105, .35, "about 1.3-2.1B shares unlock into a hostile duration tape"),
    "price below the $135 IPO after the 24 Oct lock-up tranche", "2026-11-15",
    "Lock-up supply met a market with no appetite for $32B of negative FCF.", NR + ": FCF -$32.5B and 328M shares unlocking on each of 24 Sep, 9 Oct and 24 Oct.", "sleeve"),
"GLW": v("Optical growth reported at 35x; the upside leg fails on the lower MarketBeat average.",
    (190, .25, "Q3 on 27 Oct shows optical acceleration"), (160, .45, "in line"), (130, .30, "AI optics de-rating continues"),
    "Q4 core EPS guide below $0.85 on 27 Oct", "2026-11-05",
    "The optics theme kept de-rating.", NR + ": AI networking and optics lagging and worsening.", "sleeve"),
"UUUU": v("Discounted signal: the CEO bought $968k (+41% of holdings) at the lows; 13F adds by American Century and VanEck. Delivery fails on the revenue miss.",
    (18, .25, "rare-earth oxide sales and uranium volumes beat in November"), (12, .40, "flat"), (8, .35, "rare earths reprice lower on a US-China thaw"),
    "Q3 revenue below $30M, or another equity raise", "2026-12-31",
    "Rare-earth scarcity premium collapsed on a trade deal.", NR + ": short interest 21% and the chart in breakdown.", "sleeve"),
"CRDO": v("Estimates up (14 up / 2 down) at 20x after a -20% print day; the insider leg fails on $101.5M of mostly planned sales.",
    (270, .30, "the 2 Dec print shows optical DSP ramp and gross margin back above 66%"), (215, .40, "in line"), (160, .30, "the optics theme keeps de-rating, margins compress"),
    "FQ2 gross margin below 63% or revenue below $525M", "2026-12-10",
    "Margin compression was structural: switches and optics competition.", NR + ": GM 68.5 to 64.5% and the theme lagging.", "sleeve"),
"OSCR": v("Beat and raise with 8 up / 0 down revisions; upside leg at 20%.",
    (38, .30, "ACA open enrolment from 1 Nov goes well and subsidies extended"), (30, .40, "in line"), (21, .30, "subsidy expiry shrinks the exchange market"),
    "enhanced ACA subsidies not extended, or Q3 medical loss ratio above 82%", "2026-12-31",
    "Policy took the market away.", NR + ": the co-founder sold $22.8M outside a plan in August.", "sleeve"),
"ACHR": v("Story with 13F adds; delivery fails on no guidance and no certification.",
    (9, .20, "UAE certificate and piloted transition flight"), (5.5, .45, "delays"), (3.5, .35, "dilution continues"),
    "no piloted transition flight or UAE certificate", "2027-03-31",
    "Certification slipped and dilution continued.", NR + ": SBC about 4,300% of revenue; shares +48% y/y.", "pass"),
"IREN": v("Contracted ARR $4bn; delivery fails on revenue miss and EPS cut -0.94 to -3.42.",
    (70, .25, "Horizon 3-4 energised on time and a third hyperscaler contract"), (45, .40, "in line"), (28, .35, "financing costs and long-end tantrum"),
    "FY27 EPS consensus below -4.00, or a new equity or convert raise above $1B", "2026-12-31",
    "Financing at 9% met a 5% 10-year.", NR + ": FCF -$2.23B and SBC 29% of revenue.", "pass"),
"AKAM": v("Cash-flow value at 15.5x; delivery fails on the trimmed EPS guide.",
    (140, .25, "AI inference revenue beats at the 5 Nov print"), (112, .45, "in line"), (90, .30, "margin keeps compressing"),
    "FY EPS guide below $6.90 on about 5 Nov", "2026-11-15",
    "The AI pivot cost margin without growth.", NR + ": GM 59.3 to 55.8% falling; Goldman Sell $93.", "sleeve"),
"RKLB": v("Backlog and raised guide; insider leg fails on the CEO trust's $286M planned sale and a $1.94B ATM.",
    (105, .20, "Neutron flies in Q4"), (72, .45, "Neutron slips to 2027"), (48, .35, "ATM issuance into a lagging space tape"),
    "Neutron first launch not on the pad by 31 Dec", "2026-12-31",
    "Neutron slipped and the ATM supplied the stock.", NR + ": CEO trust sold $286M; space lagging and worsening.", "pass"),
"PLPC": v("Record print, gross margin 29.7 to 34.3%; the upside leg fails because no current consensus exists.",
    (500, .30, "Q3 on about 28 Oct shows grid order momentum"), (440, .45, "in line"), (360, .25, "utility capex pause"),
    "Q3 gross margin below 31% or revenue below $200M", "2026-11-10",
    "The record quarter was a pull-forward.", NR + ": a director sold his entire holding outside a plan.", "sleeve"),
"WULF": v("Contracted Anthropic lease; delivery fails on EPS and revenue.", (28, .20, "Fluidstack sites deliver"), (16, .40, "in line"), (9, .40, "financing stress"),
    "any new equity or convert raise, or Q3 revenue below $50M", "2026-12-31", "Financing costs overwhelmed the contracted revenue.", NR + ": SBC 128% of revenue, short 35%.", "pass"),
"EOSE": v("Deep drawdown story; delivery fails on the guide cut.", (6, .15, "gross margin turns positive"), (3.2, .40, "flat"), (1.5, .45, "more dilution"),
    "Q3 gross margin below -50%", "2026-11-15", "Negative margins and dilution.", NR + ": gross margin -71%, short 34%.", "pass"),
"APP": v("15.6x with FCF 103% of NI; delivery fails on a Q3 guide below consensus.", (450, .25, "e-commerce ads re-accelerate at the 4 Nov print"), (320, .40, "in line"), (240, .35, "growth decelerates further"),
    "Q4 revenue guide below $2.1B on about 4 Nov", "2026-11-15", "The growth decelerated below the multiple.", NR + ": the first miss against its own guide.", "sleeve"),
"ONDS": v("Guide raised by acquisition; delivery fails on the EPS miss.", (14, .15, "organic backlog converts"), (7.5, .40, "flat"), (4, .45, "dilution continues"),
    "any new equity raise", "2026-12-31", "Share count kept rising.", NR + ": short 42%, share count +259% y/y.", "pass"),
"CIFR": v("Contracted $11.4B; delivery fails on the Q2 miss.", (28, .20, "HPC sites energise on schedule"), (18, .40, "in line"), (11, .40, "financing stress"),
    "Q3 gross margin below 0%", "2026-11-15", "The transition cost more than the contracts paid.", NR + ": Q2 gross margin -131%.", "pass"),
"SOFI": v("Members +35%, guide raised; the upside leg fails at 21% with a 34% MarketBeat range.", (24, .25, "Q3 on 27 Oct beats and raises"), (17, .45, "in line"), (12, .30, "credit and funding costs rise with the 2y"),
    "FY adjusted net revenue guide below $4.75B", "2026-11-05", "The rate regime hit a lending-heavy mix.", NR + ": fintech fading; short 15%.", "sleeve"),
}

if __name__ == "__main__":
    import runway_verdicts  # noqa: F401  (Runway-tier verdicts, written after the red team)
    V.update(runway_verdicts.V)
    OUT.write_text(json.dumps(V, indent=1) + "\n")
    print(f"{len(V)} verdicts -> {OUT}")

# Sizing rule applied after the red team (see the main-agent step in the session): expected return
# over 6 months against the hurdle, +8% core, +20% satellite. Only UNH (runway, +6.9%, 1pp under)
# and NVDA (+8.4%, insider leg failed) take core-starter size; other live setups are "watch".
