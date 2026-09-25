#!/usr/bin/env python3
"""Stage-one screen of the whole corpus universe from the Finviz snapshots.

Deterministic: reads data/cache/2026-09-24-runway/finviz/finviz-snapshots.json and the
ticker-universe query output, applies Finviz proxies of the four runway gates, and
writes screen.json beside this script. It never replaces the full scorecard: it only
decides which names get the stage-two deep research. Proxies:
  upside   Finviz mean target / price - 1 >= 20%
  flow     Inst Trans (3-month change in institutional shares) >= 0
  insider  Insider Own x Insider Trans (6-month change) > -1% of shares outstanding
  delivery last-quarter sales surprise >= 0 and EPS next-year growth > 0
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SNAP = ROOT / "data/cache/2026-09-24-runway/finviz/finviz-snapshots.json"
UNIV = HERE / "universe.json"
# Non-operating instruments that the universe query cannot tell apart from stocks.
NON_OPERATING = {"DRAM": "Roundhill Memory ETF", "AOTG": "AOT Growth and Innovation ETF"}
# Main-agent overrides, each with its reason. Proxies that do not fit the name are not gate failures.
OVERRIDE_DEEP = {
    "SPCX": "listed 2026: Inst Trans and EPS-next-Y proxies are undefined for a fresh listing; 6 accounts, 82 posts",
    "SKHY": "ADR: Finviz flow and estimate fields do not cover the Korean listing; 5 accounts, 112 posts",
    "NBIS": "Finviz upside 19.4%, within a point of the gate; 7 accounts, 163 posts; the full gate uses StockAnalysis",
    "ALAB": "Finviz upside 17%, near the gate; 4 accounts and a 0.85 formal long",
    "CRM": "Finviz upside 19%, within a point of the gate; 4 accounts",
}
OPERATOR = "AI ABCL PSNL AKAM META UBER PYPL SOFI ARM PLPC KURA CRDO RARE ASTS RKLB".split()


def num(x):
    try:
        return float(str(x).split()[0].replace("%", "").replace(",", ""))
    except (ValueError, IndexError):
        return None


def main():
    snaps = json.loads(SNAP.read_text())
    univ = {r["symbol"]: r for r in json.loads(UNIV.read_text())}
    out = []
    for s in snaps:
        m, t = s["metrics"], s["ticker"]
        px, tgt = num(m.get("Price")), num(m.get("Target Price"))
        surpr = (m.get("EPS/Sales Surpr.") or "").split()
        eps_s = num(surpr[0]) if surpr else None
        sal_s = num(surpr[1]) if len(surpr) > 1 else None
        hi = (m.get("52W High") or "").split()
        ins_own, ins_tr = num(m.get("Insider Own")), num(m.get("Insider Trans"))
        ins_float = (ins_own * ins_tr / 100) if ins_own is not None and ins_tr is not None else None
        eny = num(m.get("EPS next Y"))
        r = {
            "ticker": t, "name": s["title"].split(" Stock")[0], "source": s["source"], "as_of": s["fetched_at"][:10],
            "price": px, "target": tgt, "upside_pct": round((tgt / px - 1) * 100, 1) if px and tgt else None,
            "high_52w": num(hi[0]) if hi else None, "from_high_pct": num(hi[1]) if len(hi) > 1 else None,
            "sma50_pct": num(m.get("SMA50")), "sma200_pct": num(m.get("SMA200")),
            "perf_q_pct": num(m.get("Perf Quarter")), "perf_m_pct": num(m.get("Perf Month")),
            "eps_surprise_pct": eps_s, "sales_surprise_pct": sal_s, "sales_qq_pct": num(m.get("Sales Q/Q")),
            "eps_next_y_pct": eny, "fwd_pe": num(m.get("Forward P/E")), "p_fcf": num(m.get("P/FCF")),
            "insider_trans_pct": ins_tr, "insider_sell_pct_shares": round(ins_float, 2) if ins_float is not None else None,
            "inst_trans_pct": num(m.get("Inst Trans")), "short_float_pct": num(m.get("Short Float")),
            "beta": num(m.get("Beta")), "recom": num(m.get("Recom")), "earnings": m.get("Earnings"),
            "market_cap": m.get("Market Cap"), "oper_margin_pct": num(m.get("Oper. Margin")),
            "corpus": {k: univ.get(t, {}).get(k) for k in ("accounts", "posts", "days", "last_day", "authors")},
            "operator_added": t in OPERATOR,
        }
        g = {
            "upside": r["upside_pct"] is not None and r["upside_pct"] >= 20,
            "flow": r["inst_trans_pct"] is not None and r["inst_trans_pct"] >= 0,
            "insider": ins_float is None or ins_float > -1.0,
            "delivery": sal_s is not None and sal_s >= 0 and eny is not None and eny > 0,
        }
        r["gates"] = g
        r["gates_failed"] = [k for k, ok in g.items() if not ok]
        r["above_200d"] = (r["sma200_pct"] or -1) > 0
        n = len(r["gates_failed"])
        r["override"] = OVERRIDE_DEEP.get(t)
        r["screen"] = ("non_operating" if t in NON_OPERATING else
                       "deep" if (g["upside"] and n <= 1) or t in OPERATOR or t in OVERRIDE_DEEP else
                       "no_runway_price_at_consensus" if not g["upside"] else "screened_out_two_legs")
        out.append(r)
    out.sort(key=lambda r: ({"deep": 0}.get(r["screen"], 1), len(r["gates_failed"]), -(r["upside_pct"] or -99)))
    (HERE / "screen.json").write_text(json.dumps(out, indent=1) + "\n")
    for r in out:
        print(f"{r['screen'][:10]:11}{r['ticker']:6}{'*' if r['operator_added'] else ' '} up={r['upside_pct']} fail={','.join(r['gates_failed'])} 200d={r['sma200_pct']} acc={r['corpus']['accounts']} posts={r['corpus']['posts']}")


if __name__ == "__main__":
    main()
