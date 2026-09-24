#!/usr/bin/env python3
"""Build auditable runway records from the persisted current snapshots."""
from __future__ import annotations

from datetime import datetime, timezone
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[4]
SOURCE_DIR = ROOT / "data/cache/2026-09-17-runway"
OUT = ROOT / "data/probes/runway/2026-09-17/records"
AS_OF = "2026-09-17"
FINVIZ = "https://finviz.com/quote.ashx?t={}"

TIERS = {
    "ADBE": "core", "ORCL": "core",
    "UBER": "watch", "DERM": "watch", "BDSX": "watch", "CIEN": "watch",
    "NVDA": "satellite", "META": "satellite", "MU": "satellite", "TSM": "satellite",
    "NBIS": "satellite", "ASTS": "satellite", "TEM": "satellite", "RKLB": "satellite",
    "CRDO": "satellite", "SNDK": "satellite", "PLTR": "satellite",
}

JUDGMENT = {
    "ADBE": (6, 5, 5, 6), "ORCL": (6, 5, 3, 6), "UBER": (6, 5, 4, 5),
    "DERM": (4, 2, 4, 3), "BDSX": (5, 4, 4, 4), "CIEN": (6, 5, 4, 5),
    "NVDA": (7, 6, 4, 7), "META": (7, 6, 4, 7), "MU": (6, 4, 4, 6),
    "TSM": (7, 7, 4, 6), "NBIS": (6, 4, 1, 6), "ASTS": (5, 3, 2, 5),
    "TEM": (5, 4, 3, 5), "RKLB": (5, 4, 2, 5), "CRDO": (6, 5, 3, 6),
    "SNDK": (6, 4, 4, 6), "PLTR": (7, 6, 3, 7),
}

CASES = {
    "ADBE": "AI-first ARR growth can reaccelerate a mature, highly cash-generative software franchise.",
    "ORCL": "A large cloud and AI backlog can convert into sustained revenue and earnings growth.",
    "UBER": "Scale, improving margins and a two-officer open-market purchase cluster can support a rerating.",
    "DERM": "Emrosi adoption may replace legacy dermatology revenue and create operating leverage.",
    "BDSX": "High-margin lung diagnostics can compound as testing adoption grows.",
    "CIEN": "AI network traffic can drive a multi-year optical cycle and higher FCF margins.",
    "NVDA": "Accelerator, networking and software leadership can compound through the global AI buildout.",
    "META": "Consumer AI agents can deepen monetization across Meta's installed distribution.",
    "MU": "AI memory scarcity can extend pricing power beyond a normal memory cycle.",
    "TSM": "Foundry and advanced packaging leadership monetize demand across AI architectures.",
    "NBIS": "Software around scarce GPU capacity can lift utilization and unit economics.",
    "ASTS": "Direct-to-device carrier distribution can turn the constellation into a global network.",
    "TEM": "Clinical data and diagnostics can compound into an AI-enabled healthcare platform.",
    "RKLB": "Launch cadence and space systems can support a path to positive FCF.",
    "CRDO": "High-speed connectivity demand can compound with AI cluster scale.",
    "SNDK": "Flash scarcity and AI storage demand can sustain the current earnings cycle.",
    "PLTR": "AIP can remain the enterprise orchestration layer as underlying models commoditize.",
}


def leaf(value, source=None, as_of=AS_OF, note=None):
    x = {"value": value, "source": source if value is not None else None,
         "as_of": as_of if value is not None else None}
    if note:
        x["note"] = note
    return x


def number(value):
    if value in (None, "", "-"):
        return None
    m = re.search(r"[-+]?\d[\d,]*(?:\.\d+)?", value)
    return float(m.group().replace(",", "")) if m else None


def pct(value):
    return number(value)


def low_high(value):
    return number(value)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    rows = {r["ticker"]: r for r in json.loads((SOURCE_DIR / "finviz-snapshots.json").read_text())}
    fetched = datetime.now(timezone.utc).isoformat()
    stances = {}
    retail = []
    for path in (ROOT / "data/corpus/analysis/accounts").glob("*.json"):
        account = json.loads(path.read_text())
        for pick in account.get("picks", []):
            t = pick.get("symbol")
            if t in TIERS:
                stances.setdefault(t, []).append({"account": account["account"], "direction": pick["direction"], "conviction": pick["conviction"], "time_frame": pick["time_frame"]})
    for t in TIERS:
        ss = stances.get(t, [])
        retail.append({"symbol": t, "accounts": len({x['account'] for x in ss}), "posts": len(ss),
                       "stances": " ".join(f"{x['account']}:{x['direction']}:{x['conviction']:.1f}" for x in ss)})

    for t, tier in TIERS.items():
        m = rows[t]["metrics"]
        src = FINVIZ.format(t)
        close, hi, lo = number(m.get("Price")), low_high(m.get("52W High")), low_high(m.get("52W Low"))
        rec = {
            "ticker": t, "probe_tier": tier, "fetched_at": fetched,
            "price": {
                "close": leaf(close, src), "high_52w": leaf(hi, src), "low_52w": leaf(lo, src),
                "sma50_pct": leaf(pct(m.get("SMA50")), src), "sma200_pct": leaf(pct(m.get("SMA200")), src),
                "perf_1m_pct": leaf(pct(m.get("Perf Month")), src), "perf_3m_pct": leaf(pct(m.get("Perf Quarter")), src),
                "structure": leaf("trend_up" if pct(m.get("SMA200")) is not None and pct(m.get("SMA200")) > 0 else "base", src),
                "print_gap_held": leaf(None, note="not found: daily post-print history was not fetched"),
            },
            "consensus": {
                "label": leaf("Strong Buy" if number(m.get("Recom")) is not None and number(m.get("Recom")) <= 1.5 else "Buy" if number(m.get("Recom")) is not None and number(m.get("Recom")) <= 2 else "Hold", src,
                              note="Finviz recommendation score mechanically mapped; not a count of ratings"),
                "analysts": leaf(None, note="not found in the persisted Finviz snapshot"),
                "pt_avg": leaf(number(m.get("Target Price")), src), "pt_high": leaf(None, note="not found"),
                "pt_low": leaf(None, note="not found"), "pt_avg_alt": leaf(None, note="not found"),
                "actions_60d": leaf([], src),
            },
            "earnings": {
                "print_date": leaf(None, note="not researched for this compact refresh"),
                "revenue_actual": leaf(None, note="not found"), "revenue_estimate": leaf(None, note="not found"),
                "eps_actual": leaf(None, note="not found"), "eps_estimate": leaf(None, note="not found"),
                "guide": leaf(None, note="not found"), "revisions_30d": leaf(None, note="not found"),
                "revisions_90d": leaf(None, note="not found"), "fcf_ttm": leaf(None, note="not found"),
                "net_income_ttm": leaf(None, note="not found"),
            },
            "prospect": {"case": leaf(CASES[t], str(ROOT / "data/probes/runs/2026-09-17/evidence/summary.md")),
                         "visibility": leaf("reported" if t in ("ADBE", "ORCL") else "story", str(ROOT / "data/probes/runs/2026-09-17/evidence/summary.md"))},
            "competition": {
                "fwd_pe": leaf(number(m.get("Forward P/E")), src), "ev_sales": leaf(number(m.get("EV/Sales")), src),
                "roic_ttm_pct": leaf(pct(m.get("ROIC")), src, note="trailing proxy; not forward ROIC"),
                "operating_margin_ttm_pct": leaf(pct(m.get("Oper. Margin")), src, note="trailing proxy; not forward margin"),
                "p_fcf_ttm": leaf(number(m.get("P/FCF")), src), "peg_aggregator": leaf(number(m.get("PEG")), src, note="aggregator methodology; used only as a proxy"),
            },
            "insiders": {
                "coverage_complete": False,
                "buys_90d": leaf([], note="full issuer Form 4 coverage not completed"),
                "sells_90d": leaf([], note="full issuer Form 4 coverage not completed"),
                "finviz_net_change_pct": leaf(pct(m.get("Insider Trans")), src),
            },
            "institutions": {
                "quarter_end": leaf(None, note="13F vintage not established"), "net_shares": leaf(None, note="not found"),
                "holders_up": leaf(None, note="not found"), "holders_down": leaf(None, note="not found"),
                "holders_new": leaf(None, note="not found"), "holders_exited": leaf(None, note="not found"),
                "named_adds": leaf([], note="not found"), "named_exits": leaf([], note="not found"),
                "short_pct_float": leaf(pct(m.get("Short Float")), src),
                "finviz_inst_change_pct": leaf(pct(m.get("Inst Trans")), src, note="secondary directional proxy; not used as the 13F gate"),
            },
            "catalysts": leaf([], note="not confirmed from issuer calendars"),
            "judgment": {
                "prospect_pts": JUDGMENT[t][0], "prospect_why": CASES[t],
                "competition_pts": JUDGMENT[t][1], "competition_why": "Scored from current operating economics and the corpus thesis.",
                "macro_fit_pts": JUDGMENT[t][2], "macro_fit_why": "Higher rates and oil penalize long-duration, cash-burning models.",
                "narrative_pts": JUDGMENT[t][3], "narrative_why": "Scored from corpus convergence and harmony with current reported economics.",
            },
            "forward": {"periods_aligned": False, "fy1": {}, "fy2": {}, "valuation": {}, "revisions": {}, "ratings": {}},
        }
        # Corpus scorecards establish delivery for these two, but do not claim the guide was raised.
        if t == "ADBE":
            es = "https://x.com/StockSavvyShay/status/2098141963673604435"
            rec["earnings"].update({"print_date": leaf("2026-09-10", es), "revenue_actual": leaf(6.76, es),
                                    "revenue_estimate": leaf(6.70, es), "eps_actual": leaf(6.13, es),
                                    "eps_estimate": leaf(6.09, es), "guide": leaf("held", es, note="guide above consensus; change versus prior guide not established")})
        if t == "ORCL":
            es = "https://x.com/StockSavvyShay/status/2098142965969649830"
            rec["earnings"].update({"print_date": leaf("2026-09-10", es), "revenue_actual": leaf(19.3, es),
                                    "revenue_estimate": leaf(19.1, es), "eps_actual": leaf(1.92, es),
                                    "eps_estimate": leaf(1.74, es), "guide": leaf("held", es, note="guide above consensus; change versus prior guide not established")})
        if t == "UBER":
            rec["insiders"]["buys_90d"] = leaf([
                {"date": "2026-09-10", "name": "Dara Khosrowshahi", "role": "CEO", "shares": 141000, "price": 70.9642, "usd": 10005952.2, "transaction_code": "P", "open_market": True, "plan_10b5_1": False, "form4": "https://www.sec.gov/Archives/edgar/data/1543151/000118423726000008/primarydocument.xml"},
                {"date": "2026-09-04", "name": "Andrew Macdonald", "role": "President and COO", "shares": 70000, "price": 75.8294, "usd": 5308058.0, "transaction_code": "P", "open_market": True, "plan_10b5_1": False, "form4": "https://www.sec.gov/Archives/edgar/data/1543151/000207176126000011/primarydocument.xml"},
            ], "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1543151&type=4&owner=include", note="two purchases verified; coverage_complete remains false because every 90-day filing was not transaction-coded")
        # Period-aligned forecast data was available for three names; units are USD billions except EPS.
        forecasts = {
            "NVDA": ({"revenue": 411.49, "eps": 9.31}, {"revenue": 682.87, "eps": 15.68}, (58, 2, 1)),
            "NBIS": ({"revenue": 3.34, "eps": -2.08}, {"revenue": 12.06, "eps": -3.14}, None),
            "TEM": ({"revenue": 1.60, "eps": -0.26}, {"revenue": 1.97, "eps": 0.00}, (10, 8, 1)),
        }
        if t in forecasts:
            fy1, fy2, ratings = forecasts[t]
            s = f"https://stockanalysis.com/stocks/{t.lower()}/forecast/"
            rec["forward"]["periods_aligned"] = True
            for period, vals in (("fy1", fy1), ("fy2", fy2)):
                rec["forward"][period] = {k: leaf(v, s) for k, v in vals.items()}
            rec["forward"]["valuation"] = {"price": leaf(close, src), "enterprise_value": leaf(None, note="not found"), "wacc_pct": leaf(None, note="not found")}
            if ratings:
                rec["forward"]["ratings"] = {"buy": leaf(ratings[0], s), "hold": leaf(ratings[1], s), "sell": leaf(ratings[2], s)}
        (OUT / f"{t}.json").write_text(json.dumps(rec, indent=2) + "\n")

    (OUT / "retail.json").write_text(json.dumps(retail, indent=2) + "\n")
    (OUT / "stances.json").write_text(json.dumps(stances, indent=2) + "\n")
    manifest = {"window_end": AS_OF, "price_date": AS_OF, "thirteen_f_quarter_end": None,
                "tickers": list(TIERS), "groups": TIERS, "fetched_at": fetched,
                "sources_failed": [
                    {"source": "13F institutional ownership", "tickers": list(TIERS), "behaviour": "No consistent current share-based dataset was available; gate left false."},
                    {"source": "forward estimates", "tickers": [t for t in TIERS if t not in ("NVDA", "NBIS", "TEM")], "behaviour": "No API keys configured; sparse proxy fields retained from Finviz without converting trailing metrics into forward values."},
                ]}
    (OUT / "_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    macro = {
        "fed_target_pct": leaf("3.75-4.00", "https://www.federalreserve.gov/newsevents/pressreleases/monetary20260916a.htm", "2026-09-16"),
        "dgs2_pct": leaf(4.74, "https://fred.stlouisfed.org/series/DGS2", "2026-09-16"),
        "dgs10_pct": leaf(5.01, "https://fred.stlouisfed.org/series/DGS10", "2026-09-16"),
        "real10y_pct": leaf(2.68, "https://fred.stlouisfed.org/series/DFII10", "2026-09-16"),
        "hy_oas_pct": leaf(2.70, "https://fred.stlouisfed.org/series/BAMLH0A0HYM2", "2026-09-16"),
        "vix": leaf(17.71, "https://fred.stlouisfed.org/series/VIXCLS", "2026-09-16"),
        "themes": [{"theme": "AI infrastructure", "direction": "accelerating", "counter": "financing and power costs"},
                   {"theme": "memory", "direction": "accelerating", "counter": "cyclical supply response"}],
        "events": [{"date": "2026-10-27", "event": "FOMC meeting begins"}],
    }
    (OUT / "macro.json").write_text(json.dumps(macro, indent=2) + "\n")
    print(f"built {len(TIERS)} runway records in {OUT}")


if __name__ == "__main__":
    main()
