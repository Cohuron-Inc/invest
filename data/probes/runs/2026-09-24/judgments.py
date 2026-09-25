#!/usr/bin/env python3
"""Main-agent judgment for the 2026-09-24 runway probe: prospect, competition, macro fit,
narrative harmony, per scorecard.md, each with a one-line reason. Macro fit starts from
records/macro.json macro_regime.runway_macro_fit_pts for the name's archetype
(long_duration_growth 1, quality_megacap 4, cash_flow_value 5, materials_industrials 4,
small_caps 4, banks 4, em_international 3, crypto_high_beta 4, defensives 2) and moves at
most one point with a reason. Narrative takes theme direction from
research/2026-09-24/themes/themes.json. These are analyst calls, labelled as such."""
import json
from pathlib import Path

REC = Path(__file__).resolve().parents[3] / "probes/runway/2026-09-24/records"

J = {
# ticker: (prospect, why, competition, why, macro, why, narrative, why)
"NVDA": (7, "the case is in the last two prints: Q2 beat and Q3 guide raised to $105.8-110.2B; FY28 revenue consensus $683B", 6, "GM 73.4 to 75.0% rising with share held; fwd P/E 14.3 below AMD 39.6 and AVGO 18.2", 4, "quality megacap archetype 4; self-funding, net cash", 5, "Mag 7 accelerating but semis only improving; loudest name in the corpus"),
"AVGO": (5, "AI revenue path of ~$115B FY27 is CEO guidance; Q4 guide sat just under consensus", 4, "GM 76.6 to 74.2% diluting on AI mix; fwd P/E 18.2 mid-peer", 4, "quality megacap archetype 4", 3, "semis improving, but FY2 estimates cut 25 down / 11 up and the chart is below both lines"),
"ARM": (5, "royalty uplift is in the raised guide, data-center share is still a story", 3, "GM flat ~97%; RISC-V substitute named; fwd P/E ~100 vs QCOM 19", 3, "quality megacap 4, minus 1: ~100x forward earnings is long duration at 2.76% real yields", 3, "semis improving; the stock sits above its consensus target"),
"AMAT": (6, "WFE upcycle visible in the raised Q4 guide; FY27 revenue +35% is consensus", 5, "GM 48.0 to 50.3% rising; fwd P/E 25.3 in line with LRCX and ASML; China share falling", 4, "materials/industrials archetype 4", 2, "semicap basket lagging and worsening, -24pp vs SPY over 3m"),
"LRCX": (6, "memory and GAA etch in the raised Q1 guide; FY27 revenue +50% consensus", 5, "GM 49.6 to 51.8% rising; valuation in line with peers", 4, "materials/industrials archetype 4", 2, "semicap basket lagging and worsening"),
"ASML": (6, "EUV and High-NA demand in the raised Q3 guide", 7, "EUV monopoly; GM 51.6 to 54.0% rising; fwd P/E 28.4 near peers", 4, "quality megacap archetype 4", 3, "semis improving, semicap lagging; mixed"),
"AMKR": (3, "AI packaging and Arizona are still ahead; Q3 revenue guide below consensus and FCF negative", 2, "GM 14-17% volatile against TSM in-house packaging; share not gaining", 3, "materials 4 minus 1: negative FCF with $2.5-3.0B capex into a hostile rate regime", 2, "semis improving but the name broke down 25% on its print"),
"TXN": (6, "analog recovery visible in the raised Q3 guide; capex roll-off lifts FCF", 5, "GM 57.4 to 61.4% rising; fwd P/E 26.3 above NXPI 12.7 and ON 16.3", 5, "quality megacap 4 plus 1: FCF 0.88x NI and a dividend fit a cash-flow regime", 3, "semis improving; analog outside the AI narrative"),
"MU": (7, "HBM and DRAM pricing is in the last two prints: FQ3 beat by 15% on revenue, FQ4 guide ~$50B vs $43.5B", 5, "GM 44.7 to 84.6% on pricing, cyclical not structural; fwd P/E 6.8 at peak margins", 4, "materials/industrials 4", 5, "memory improving with attention heating into the 30 Sep print"),
"SNDK": (7, "NAND tightness is in the beat and raise and a $14B buyback", 4, "GM 29.8 to 84.6% cyclical; fwd P/E 6.7 at peak", 4, "materials/industrials 4", 5, "memory improving; crowded among accounts"),
"WDC": (6, "HDD exabyte growth and pricing in the beat and above-consensus guide", 5, "duopoly with STX; GM 43.5 to 54.1% rising", 4, "materials/industrials 4", 4, "memory and storage improving, but the stock fell 13% on the beat"),
"ON": (4, "auto and industrial recovery is guided; the Synaptics deal adds execution risk", 4, "GM 37.9 to 39.3% flat-up; fwd P/E 16.3 mid-peer", 4, "quality megacap 4; cash conversion 2.4x", 3, "semis improving, auto and industrial outside the theme"),
"NXPI": (5, "auto upcycle in the raised Q3 guide; 2030 EPS doubling is a story", 5, "GM 56.3 to 57.3% stable; fwd P/E 12.7 cheapest in analog", 5, "quality megacap 4 plus 1: 12.7x forward earnings with 0.94x cash conversion suits the plateau", 3, "semis improving; auto outside the AI theme"),
"AMBA": (4, "edge-AI SoC growth guided; EPS 0.80 to 1.12 is consensus", 3, "GM 59.6 to 57.7% falling; fwd P/E 66", 2, "small cap and GAAP loss-making with SBC 22% of revenue: long duration", 3, "edge AI is outside the main themes"),
"GLW": (5, "optical +32% y/y is reported; Q3 guide soft", 4, "GM 37.1 to 36.1% flat; fwd P/E 35.5 above COHR and LITE", 3, "AI networking archetype 1 plus 2: a dividend-paying industrial with 1.26x cash conversion is not long duration", 2, "AI networking and optics lagging and worsening"),
"CSCO": (5, "hyperscaler AI orders $9.3B FY26; FQ1 guide raised above consensus", 4, "GM 65.5 to 64.1% drifting; fwd P/E 19.3 vs ANET 39.4", 5, "cash-flow value shape: 0.96x conversion, dividend, 19x", 3, "outside the AI networking basket's direction; mixed"),
"CRDO": (6, "AEC and optical DSP demand in the last print; FY >85% growth reiterated", 4, "GM 68.5 to 64.5% compressing; fwd P/E 20.3 below MRVL 38 and ALAB 56", 1, "AI networking archetype 1: long duration at 2.76% real yields", 1, "AI networking and optics lagging and worsening; crowd against tape"),
"COHR": (6, "datacom transceivers in the beat and raise; FY27 revenue +49% consensus", 5, "GM 36.6 to 38.5% rising; fwd P/E 20.7 below LITE 27.4", 2, "AI networking 1 plus 1: positive EPS at 20x softens the duration hit", 1, "AI networking and optics lagging and worsening"),
"LITE": (7, "EML and CW lasers in the last two prints; Q1 EPS guide $4.05-4.35 vs $3.63", 6, "GM 37.7 to 49.3% rising fast; share held", 2, "AI networking 1 plus 1: earnings inflecting", 1, "AI networking and optics lagging and worsening"),
"AAOI": (3, "800G/1.6T ramp guided, EPS consensus cut 0.89 to 0.68", 2, "GM flat-down 28-31%; serial ATM dilution", 1, "long duration with negative FCF", 1, "AI networking and optics lagging and worsening"),
"ANET": (7, "AI Ethernet fabrics in the third FY raise to $12.6B", 6, "GM ~62-63% stable with share gains; fwd P/E 39.4 premium", 3, "quality megacap 4 minus 1: 39x forward earnings", 3, "AI networking lagging, but the name itself is near highs; outside the basket's weakness"),
"VIAV": (5, "network and data-center test in the raised Q1 FY27 guide", 4, "GM ~60-61% flat; fwd P/E 19.1 below KEYS 26.1 and CIEN 30.4", 3, "materials/industrials 4 minus 1: small cap with dilution", 3, "outside a basket; near the optics theme's weakness"),
"AKAM": (3, "AI inference services are a story; FY EPS guide trimmed", 3, "GM 59.3 to 55.8% falling against NET and FSLY", 5, "cash-flow value: FCF 2.3x NI, 15.5x forward earnings", 3, "outside any theme"),
"PLPC": (6, "record Q2: GM 34.3%, EPS +75%, grid hardening and fiber build", 5, "GM 29.7 to 34.3% rising; fwd P/E 30 above HUBB and ATKR", 4, "materials/industrials 4", 4, "grid theme improving; uncovered by the Street"),
"ORCL": (5, "RPO of $664B is contracted; conversion to OCI revenue is ahead", 4, "GM 60.0 to 66.5% volatile; fwd P/E 12.7-16.4 below MSFT and AMZN", 1, "neocloud archetype 1: $169B debt, FCF -$28.7B, $20B ATM at 2.76% real yields; the thesis needs the regime to change", 1, "neocloud and data centers lagging; the corpus macro account is short"),
"CRWV": (4, "~$104B backlog is contracted; the 2027 revenue path needs financing", 2, "GM 73.0 to 65.9% falling; 10x debt to equity", 0, "the thesis needs the regime to change: $51.6B debt, $640M/quarter interest", 1, "neoclouds lagging"),
"IREN": (4, "$4bn contracted ARR from Microsoft and a frontier lab is guided", 3, "GM 64.4 to 66.4% rising; EV/S 28.6", 1, "long duration, FCF -$2.2B, converts and GPU debt at 9%", 2, "neoclouds lagging; crypto equities accelerating"),
"APLD": (4, "$36.2B take-or-pay leases contracted; delivery ahead", 3, "GM volatile 13-43%; EV/S 18.7 below CIFR and WULF", 1, "long duration with project debt at 7-9.25%", 1, "neoclouds lagging"),
"WULF": (3, "Anthropic ~$19B lease contracted, build ahead", 2, "GM volatile; SBC 128% of revenue", 0, "the thesis needs the regime to change: $5.3B debt and a hostile rate tape", 1, "neoclouds lagging"),
"CIFR": (3, "~$11.4B contracted; Q2 gross margin -131%", 2, "GM collapsing in the transition", 0, "the thesis needs the regime to change: $5.6B debt", 1, "neoclouds lagging"),
"WYFI": (2, "NC-1 $865M lease contracted; financing not closed", 2, "tiny float, 50% short, FY27 estimates cut 0.52 to 0.15", 0, "long duration, fresh 5% converts", 1, "neoclouds lagging"),
"GRRR": (2, "Yotta and Supermicro programmes; FY27 guide below consensus", 2, "GM volatile; share count +63% y/y", 1, "long duration small cap with a shelf", 2, "outside any basket; AI infrastructure financing trade fading"),
"VST": (4, "EBITDA guide held after a large Q2 revenue miss; PPAs are the story", 5, "nuclear and gas fleet; fwd P/E 13.6 below CEG 19.7", 5, "cash-flow value archetype 5: FCF equals net income, buybacks", 4, "AI power improving from a low base; quiet improvement"),
"GEV": (6, "$176B backlog, FY revenue and FCF guides raised", 6, "GM 19.2 to 21.6% rising; oligopoly with Siemens Energy and MHI", 5, "cash-flow value archetype 5: FCF $12B", 4, "AI power improving"),
"CCJ": (4, "term uranium near $90/lb; Cigar Lake halt is ahead of a restart", 4, "GM 37 to 32% volatile", 1, "nuclear archetype 1", 1, "nuclear lagging and worsening"),
"UUUU": (3, "rare-earth and uranium ramp; ASM deal closed", 3, "GM 27.8 to 57.4% rising from a small base", 1, "nuclear archetype 1", 1, "nuclear lagging and worsening"),
"EOSE": (2, "zinc storage scale-up via the JV; guide cut", 1, "GM -111 to -71%, negative", 0, "the thesis needs the regime to change: negative margins and dilution", 2, "AI power improving but the name is -84% from its high"),
"RKLB": (4, "Space Systems backlog $2.36B and the raised Q3 guide; Neutron slipping toward 2027", 4, "GM 36-38% flat; EV/S 54.5 vs SpaceX 84", 1, "space archetype 1: long duration with a $1.94B ATM", 1, "space lagging and worsening"),
"ASTS": (2, "direct-to-phone service needs ~45 satellites; 13 in orbit", 2, "GM 62.6 to 25.2% falling; SpaceX direct-to-cell substitute shipping", 0, "the thesis needs the regime to change: $2B of converts, SBC 128%", 1, "space lagging and worsening"),
"ACHR": (1, "revenue depends on certification still ahead", 2, "JOBY ahead on FAA stages", 0, "pre-revenue, shares +48% y/y", 1, "outside any theme; eVTOL is a story"),
"SPCX": (5, "Starlink subscribers and margins are in the first print; Starship and AI capex are ahead", 6, "launch and LEO broadband leader; EV/S 84", 1, "long duration: FCF -$32.5B and lock-up supply", 2, "space lagging; lock-ups on 24 Sep, 9 Oct and 24 Oct"),
"META": (7, "AI ad ranking visible in +22% revenue; costs and capex raised", 6, "GM ~81-82% flat; fwd P/E 22.9 in line", 4, "quality megacap 4", 5, "Mag 7 accelerating, the outlook's top Mag 7 pick, but at a new high with the most longs in the corpus"),
"AMZN": (6, "AWS re-accelerated to +37% in the last print", 6, "GM 48.5 to 52.3% rising", 4, "quality megacap 4", 6, "Mag 7 accelerating"),
"GOOGL": (6, "Cloud +82% with a $514B backlog in the last print", 6, "GM 59.6 to 62.5% rising; fwd P/E 22.6", 4, "quality megacap 4", 5, "Mag 7 accelerating; internet platforms fading"),
"SNOW": (7, "product revenue guide raised to $6.07B with margin expansion", 4, "GM ~67% flat; fwd P/E 110", 1, "AI software archetype 1: SBC 30% of revenue", 3, "cloud and AI software fading"),
"APP": (4, "Axon e-commerce extension is a story; Q3 guided below consensus", 5, "GM 87.6-89.0%; fwd P/E 15.6 below TTD 49.8", 2, "AI software 1 plus 1: FCF 103% of NI at 15x", 2, "AI applications fading; chart broken"),
"RDDT": (5, "ads and licensing in the beat; Q3 guided below consensus", 4, "GM ~91%; AI Overviews traffic risk", 2, "internet platforms 4 minus 2: logged-in traffic risk plus SBC 12%", 2, "internet platforms fading"),
"AI": (2, "restructuring under the returning founder; revenue fell 36%", 1, "GM 17-40% volatile against PLTR and SNOW", 1, "long duration, SBC 111% of revenue", 2, "AI applications fading"),
"ONDS": (3, "revenue guide raised to $525-550M through acquisitions", 2, "GM 26-49%; EV/S 17.7 vs AVAV 4.2", 0, "the thesis needs the regime to change: 42% short, share count +259%", 1, "defense and drones fading"),
"UBER": (6, "bookings +18-22% and EPS growth in the last prints", 5, "GM ~39% stable; fwd P/E 15.6 vs DASH 39.9; the AV partner fear is a story", 5, "cash-flow value shape: FCF $10.1B at 15.6x", 3, "internet platforms fading; robotaxi fear"),
"PYPL": (4, "turnaround at 9x EPS; guide raised", 4, "GM 39.6 to 40.7% drifting", 5, "cash-flow value: FCF 1.35x NI, buybacks", 3, "fintech fading"),
"SOFI": (5, "members +35% and a raised revenue guide", 3, "bank-charter competition against HOOD and LC", 2, "fintech 1 plus 1: profitable, but lending-heavy into a rising 2y", 2, "fintech fading"),
"NU": (6, "139M customers, ROE 33% reported", 5, "fwd P/E 12.1 vs MELI 32.4", 3, "EM archetype 3", 3, "fintech fading"),
"GS": (5, "record capital markets in the last print; CEO warned on FICC", 5, "fwd P/E 12.6 in line with MS and JPM", 3, "banks 4 minus 1: bear-flattening curve", 1, "banks lagging and worsening; a corpus account is short"),
"BABA": (4, "AI cloud +45%; operating income -57% on capex", 4, "fwd P/E 12.2 vs PDD 6.4", 2, "EM 3 minus 1: negative FCF and a $10.2B placement", 3, "China AI outside the US themes"),
"SE": (5, "Shopee +48% and Monee loans +62% are reported; EPS misses", 3, "TikTok Shop taking share in Vietnam", 3, "EM archetype 3", 2, "consumer lagging; heavy executive selling"),
"GRAB": (5, "adj. EBITDA +54% and the FY guide raised", 4, "fwd P/E 18.0 vs UBER 15.6", 3, "EM archetype 3", 2, "outside the themes; the Atome deal clouds it"),
"NKE": (2, "the reset is a story; revenue guided down", 2, "losing share to ONON and in China", 3, "consumer discretionary 4 minus 1: oil above $85 hurts consumer", 1, "consumer discretionary lagging"),
"DAL": (4, "premium revenue in the last print; consensus below its own guide on fuel", 4, "fwd P/E 10.7 vs UAL 9.2", 2, "oil shock is the direct headwind for an airline", 2, "consumer and travel lagging"),
"CAT": (7, "data-center power backlog $72B, +92%, in the beat and raise", 6, "GM 28.9 to 33.6% rising", 5, "materials/industrials 4 plus 1: FCF and pricing", 4, "AI power improving"),
"ISRG": (5, "procedure growth held at 13.5-15.5%; not raised", 5, "GM ~66-68% stable; Medtronic Hugo cleared", 3, "long duration 1 plus 2: net cash, FCF 1.03x NI", 4, "AI health accelerating"),
"UNH": (6, "repricing in the beat and raise to $19.50-20.00", 5, "fwd P/E 17.6 vs ELV 14.7", 5, "defensive with FCF 1.67x NI: plateau-tolerant", 3, "managed care outside the themes"),
"OSCR": (6, "EPS $1.10 vs $0.40; guide raised", 4, "fwd P/E 16.6", 3, "small cap 4 minus 1: ACA subsidy policy risk", 3, "outside the themes"),
"ADUR": (1, "commercial plant not before 2028", 2, "pre-revenue technology", 0, "pre-revenue and diluting", 1, "outside the themes"),
"KURA": (5, "KOMZIFTI launch ramp +57% q/q is reported; the frontline combination data is ahead", 4, "menin class against SNDX; GM 97.6%", 1, "SMID biotech: long duration", 2, "SMID biotech fading"),
"RARE": (3, "two approvals landed; the Angelman Phase 3 failed", 3, "BMRN and SRPT; EV/S 3.3", 1, "long duration with about 4.4 quarters of cash", 1, "SMID biotech fading"),
"ABCL": (3, "ABCL635 Phase 2 hit; the IMS readout 30 Sep to 3 Oct is binary", 3, "Veozah and Lynkuet already on market", 1, "long duration; SBC 77% of revenue", 3, "the stock is +123% vs its 200-day on the data"),
"PSNL": (1, "merger arbitrage at a fixed $16.25; no standalone case", 3, "NTRA and GH", 2, "deal spread insensitive to rates", 2, "cash-out via TEM stock"),
"STLN": (5, "value-based oncology; FY revenue raised to $650-670M", 3, "GM 14.5%, EV/S 1.2", 3, "small cap with OrbiMed debt", 3, "outside the themes"),
"STIM": (3, "adj. EBITDA positive but a going-concern flag", 2, "GM 51%", 0, "a covenant breach it expects on 31 Mar 2027", 1, "psychedelics and CNS lagging and worsening"),
"SKHY": (7, "HBM3E/HBM4 leadership; revenue KRW 347T to 534T", 5, "GM 57 to 83%; fwd P/E 5.5", 4, "materials/industrials 4", 5, "memory improving"),
"NBIS": (4, "ARR guide $7-9B held; GAAP losses widening", 3, "EV/S 50 vs CRWV 12.5", 0, "the thesis needs the regime to change: capex $20-25B", 1, "neoclouds lagging"),
"ALAB": (6, "Q3 guide $540-560M vs $410M", 4, "GM 76.3 to 73.3% falling; fwd P/E 56", 1, "AI networking 1", 1, "AI networking lagging"),
"CRM": (5, "Agentforce and a guide raise; the EPS beat is investment gains", 4, "GM drifting; fwd P/E 14.8", 5, "quality megacap 4 plus 1: FCF 1.6x NI and a $25B ASR", 3, "cloud software fading"),
}


def main():
    n = 0
    for t, (p, pw, c, cw, m, mw, nn, nw) in J.items():
        path = REC / f"{t}.json"
        rec = json.loads(path.read_text())
        rec["judgment"] = {"prospect_pts": p, "prospect_why": pw, "competition_pts": c, "competition_why": cw,
                           "macro_fit_pts": m, "macro_fit_why": mw, "narrative_pts": nn, "narrative_why": nw,
                           "by": "main agent, 2026-09-24", "label": "analyst judgment, not measured"}
        path.write_text(json.dumps(rec, indent=1) + "\n")
        n += 1
    print(f"judgment written for {n} records")


if __name__ == "__main__":
    main()
