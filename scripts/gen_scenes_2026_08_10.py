#!/usr/bin/env python3
"""Generate the 2026-08-10 slate scenes via KIE Nano Banana Pro (9:16 2K).
5 slugs x 4 images each (hero + broll_1/2/3), each matched to its beat.
Scenes only — no real named individuals are depicted. Hardened anti-UI negatives.
Submit-all-then-poll-all.
"""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, http_get, first_image_url, download, submit  # type: ignore

D = "2026-08-10"
NOUI = "absolutely no user-interface, no app screens, no news graphics, no readable text on any screen, no phone or tablet UI"
UP = "upright vertical portrait orientation, correct horizon, not rotated"
NOFACE = "no recognisable famous person, anonymous ordinary people, faces turned away or partially obscured"

JOBS = [
    # 1 — POWER PROTEST + WHO COLLECTS THE BILL  (P1 services/governance · LEAD)
    (f"{D}-blackout-bill-provinces", "hero.jpg", f"Wide editorial photojournalism shot of a rural road in southern Iraq blocked by burning car tyres sending thick black smoke into a hazy late-afternoon sky, a few anonymous protesters standing back in silhouette, flat marshland horizon behind, documentary reportage, {UP}, {NOFACE}, {NOUI}, {NEG}"),
    (f"{D}-blackout-bill-provinces", "broll_1.jpg", f"Close-up of a bank of old analogue electricity meters bolted to a weathered concrete wall with a tangle of wires running between them, dust and heat haze, harsh midday sun, documentary detail shot, {NOUI}, {NEG}"),
    (f"{D}-blackout-bill-provinces", "broll_2.jpg", f"An electricity collection clerk in plain clothes standing at a residential doorway writing in a paper receipt book while a resident hands over banknotes, small local bill-collection scene, warm afternoon light, intimate documentary photojournalism, {NOFACE}, {NOUI}, {NEG}"),
    (f"{D}-blackout-bill-provinces", "broll_3.jpg", f"An Iraqi family sitting in a dim sweltering living room during a power cut, a motionless ceiling fan above and a single battery lantern glowing on the floor, extreme summer heat, intimate documentary photojournalism, {NOFACE}, {NOUI}, {NEG}"),
    # 2 — DOLLAR AT THE SHOPS CROSSES 153,000  (P1 dinar · daily anchor · 19:45)
    (f"{D}-dollar-shops-153", "hero.jpg", f"Wide editorial shot of a busy currency exchange shopfront on a Baghdad street, customers queuing at the counter window in bright harsh sunlight, bundles of banknotes changing hands, energetic informal money market, documentary photojournalism, {UP}, {NOFACE}, {NOUI}, {NEG}"),
    (f"{D}-dollar-shops-153", "broll_1.jpg", f"Extreme close-up of two hands holding a thick fan of Iraqi dinar banknotes in one hand and a fan of US one-hundred-dollar bills in the other, direct side-by-side comparison, dark background, dramatic rim light, shallow depth of field, {NOUI}, {NEG}"),
    (f"{D}-dollar-shops-153", "broll_2.jpg", f"A currency exchange street in Erbil in the Kurdistan Region at golden hour, small exchange booths with shuttered fronts and traders standing outside, low warm sun, wide documentary editorial shot, {UP}, {NOFACE}, {NOUI}, {NEG}"),
    (f"{D}-dollar-shops-153", "broll_3.jpg", f"A woman paying with dinar banknotes at a crowded open-air vegetable and grocery stall, produce piled high in crates, everyday cost of living, warm late afternoon light, intimate documentary photojournalism, {NOFACE}, {NOUI}, {NEG}"),
    # 3 — NASIRIYA LAND FILES / ARREST WARRANTS  (P1 corruption · 21:15)
    (f"{D}-land-files-nasiriya", "hero.jpg", f"Wide editorial shot of anti-corruption investigators in plain dark clothing examining tall stacks of seized property deed folders spread across a long table in a bare government office, evidence boxes on the floor, cold overhead light, serious forensic atmosphere, documentary photojournalism, {UP}, {NOFACE}, {NOUI}, {NEG}"),
    (f"{D}-land-files-nasiriya", "broll_1.jpg", f"Extreme close-up of a tall disordered stack of old paper property deed documents bound with string, official rubber ink stamps and a scattered set of stamp seals on a desk beside them, dramatic side light, shallow depth of field, {NOUI}, {NEG}"),
    (f"{D}-land-files-nasiriya", "broll_2.jpg", f"Exterior of a plain modern Iraqi courthouse building with a flat facade and a flagpole in front, empty forecourt, hard midday sun casting sharp shadows, austere institutional architecture, wide editorial shot, {UP}, {NOUI}, {NEG}"),
    (f"{D}-land-files-nasiriya", "broll_3.jpg", f"Aerial view of a grid of empty unbuilt residential land plots on the edge of a southern Iraqi city, boundary markers and dirt access roads dividing bare sandy lots, some half-built houses at the edge, harsh daylight, drone editorial photography, {NOUI}, {NEG}"),
    # 4 — TURKISH GRAIN & PASTA / THE FOOD BASKET  (P2 trade-food · 22:30)
    (f"{D}-pasta-turkey-imports", "hero.jpg", f"Wide editorial shot of an Iraqi grocery market aisle stacked high with open burlap sacks of lentils, chickpeas, rice and bulgur with metal scoops resting in them, rich earthy colours, warm market light, documentary photojournalism, {UP}, {NOFACE}, {NOUI}, {NEG}"),
    (f"{D}-pasta-turkey-imports", "broll_1.jpg", f"Close-up of dense rows of packaged dried pasta and bottles of vegetable cooking oil filling a grocery shelf from top to bottom, plain unbranded packaging with no readable text, supermarket interior light, shallow depth of field, {NOUI}, {NEG}"),
    (f"{D}-pasta-turkey-imports", "broll_2.jpg", f"A long queue of heavy cargo lorries waiting nose to tail at a land border crossing between arid hills, customs canopy ahead, dust and heat shimmer, wide editorial documentary shot, {UP}, {NOUI}, {NEG}"),
    (f"{D}-pasta-turkey-imports", "broll_3.jpg", f"A woman filling a shopping bag with dry goods at a neighbourhood grocery while the shopkeeper weighs pulses on a hanging scale, everyday household food shopping, warm interior light, intimate documentary photojournalism, {NOFACE}, {NOUI}, {NEG}"),
    # 5 — NEW EXPORT ROUTES: FISHKHABOUR + BANIYAS  (P2 oil · SILENT V10.1 CONTROL · 23:45)
    (f"{D}-route-baniyas-oil", "hero.jpg", f"Wide cinematic aerial shot of a large-diameter crude oil pipeline running in a dead straight line across empty arid desert toward a distant mountain ridge, service track alongside, clear hard daylight, editorial infrastructure photography, {UP}, {NOUI}, {NEG}"),
    (f"{D}-route-baniyas-oil", "broll_1.jpg", f"A Mediterranean coastal oil export terminal at golden hour, storage tank farm in the foreground and a jetty with loading arms reaching into calm blue sea, wide cinematic aerial editorial shot, {UP}, {NOUI}, {NEG}"),
    (f"{D}-route-baniyas-oil", "broll_2.jpg", f"Close-up of a cluster of large red and steel manifold valves and pressure gauges at a crude oil pumping station, weathered paint and pipework, hard directional sunlight, industrial detail photography, {NOUI}, {NEG}"),
    (f"{D}-route-baniyas-oil", "broll_3.jpg", f"A fully laden crude oil supertanker under way on open sea at dawn seen from the air, long wake behind it, steel-blue water and pale sky, cinematic wide aerial shot, {NOUI}, {NEG}"),
]


def main() -> int:
    only = set(sys.argv[1:])
    jobs = []
    todo = [(s, f, p) for (s, f, p) in JOBS if not only or s in only]
    print(f"== Submitting {len(todo)} scene jobs ==", flush=True)
    for slug, fname, prompt in todo:
        out = IMG_ROOT / slug / fname
        out.parent.mkdir(parents=True, exist_ok=True)
        try:
            tid = submit(prompt)
            jobs.append({"slug": slug, "file": fname, "out": out, "tid": tid, "ok": False})
            print(f"  + {slug}/{fname} tid={tid}", flush=True)
        except Exception as e:
            print(f"  ! submit {slug}/{fname}: {e}", file=sys.stderr, flush=True)
        time.sleep(0.5)

    pending = [j for j in jobs if j.get("tid")]
    print(f"== Polling {len(pending)} jobs ==", flush=True)
    deadline = time.time() + 14 * 60
    while pending and time.time() < deadline:
        time.sleep(POLL_INTERVAL)
        still = []
        for j in pending:
            try:
                info = http_get(f"{STATUS_URL}?taskId={j['tid']}")
                url = first_image_url(info)
                if url:
                    download(url, j["out"])
                    j["ok"] = True
                    print(f"  ✓ {j['slug']}/{j['file']}", flush=True)
                    continue
                data = (info or {}).get("data") or {}
                state = str(data.get("state") or data.get("status") or "").lower()
                if state in ("fail", "failed", "error"):
                    print(f"  ✗ {j['slug']}/{j['file']} FAILED: {data.get('failMsg')}", flush=True)
                    continue
                still.append(j)
            except Exception as e:
                print(f"  ? {j['slug']}/{j['file']}: {e}", flush=True)
                still.append(j)
        pending = still
        print(f"    ({len(pending)} still pending)", flush=True)

    done = sum(1 for j in jobs if j["ok"])
    print(f"== DONE {done}/{len(jobs)} ==", flush=True)
    for j in jobs:
        if not j["ok"]:
            print(f"   MISSING {j['slug']}/{j['file']}", flush=True)
    return 0 if done == len(jobs) else 1


if __name__ == "__main__":
    raise SystemExit(main())
