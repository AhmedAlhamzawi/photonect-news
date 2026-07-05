#!/usr/bin/env python3
"""Cinematic KIE nano-banana-pro 9:16 2K scenes for the 2026-07-05 slate.
Throughline: external chokepoints/levers on Iraqi/Gulf money + a health register-break.
All 5 stories are scene-based (no single named person → no face slots)."""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

X = ("absolutely no on-screen text, no Arabic or English writing, no captions, no UI, no fake screenshots, "
     "no watermark, no logos, no brand marks, no garbled characters, no readable signage, no digits, no charts with numbers")

CEY = "2026-07-05-ceyhan-oil-deadline"
HOR = "2026-07-05-hormuz-transit-fees"
WAT = "2026-07-05-iraq-water-emergency"
PIF = "2026-07-05-saudi-pif-squeeze"
SIC = "2026-07-05-sickle-cell-cure"

JOBS = [
    # 1) CEYHAN OIL DEADLINE — Iraq-Turkey pipeline export lever
    (CEY, "hero.jpg",   f"A cinematic wide aerial at dusk of a massive steel crude-oil pipeline snaking across arid mountainous Iraq-Turkey border terrain toward the horizon, a lone pump station silhouette, burnt-orange sky, heavy geopolitical tension, immense scale of an oil export lifeline, {NEG}, {X}"),
    (CEY, "broll_1.jpg",f"A grand formal international negotiation hall with a long polished conference table ringed by empty leather chairs and plain unmarked flag stands, dramatic chandelier light, wood panelling, a cold diplomatic tension, no identifiable people, {NEG}, {X}"),
    (CEY, "broll_2.jpg",f"A cinematic wide aerial of a large Mediterranean oil export terminal at golden hour, rows of huge white crude storage tanks and long jetties, a supertanker berthed loading, calm sea, immense petroleum infrastructure, {NEG}, {X}"),
    (CEY, "broll_3.jpg",f"A moody cinematic shot of a lone oil pipeline pump-and-metering station at blue hour, large valves gauges and pipes, warm work-lights glowing, a sense of crude still flowing under uncertainty, no readable signage, {NEG}, {X}"),
    # 2) HORMUZ TRANSIT FEES — Iran strait chokepoint lever
    (HOR, "hero.jpg",   f"A dramatic cinematic aerial at dawn of the narrow Strait of Hormuz, a giant crude supertanker threading between rugged steep coastlines, steel-blue sea, hazy mountains, a tense sense of a strategic maritime chokepoint, {NEG}, {X}"),
    (HOR, "broll_1.jpg",f"Vertical portrait 9:16 photo, upright orientation, level horizon: a cinematic shot of a small fast military patrol boat cutting a white wake across a narrow strait close to a towering loaded oil tanker, overcast grey sky, tense maritime standoff mood, {NEG}, {X}"),
    (HOR, "broll_2.jpg",f"A cinematic high aerial of a convoy of several fully loaded crude oil supertankers riding low in calm blue water, immense scale of global oil trade at golden light, {NEG}, {X}"),
    (HOR, "broll_3.jpg",f"A moody cinematic shot of a single supertanker silhouetted at dusk waiting outside a narrow strait, brooding orange-grey sky, a heavy sense of uncertainty and waiting, {NEG}, {X}"),
    # 3) IRAQ WATER EMERGENCY — upstream-dam water lever
    (WAT, "hero.jpg",   f"A breathtaking cinematic aerial of a nearly empty Iraqi reservoir behind a dam, vast cracked mud flats where water once stood, only a thin shrinking channel remaining, harsh sun and heat haze, the scale of a historic drought, {NEG}, {X}"),
    (WAT, "broll_1.jpg",f"A cinematic wide shot of the cracked drought-stricken bed of the Euphrates river in Iraq, small wooden boats stranded on dry fractured earth, sparse dead reeds, blazing midday heat shimmer, {NEG}, {X}"),
    (WAT, "broll_2.jpg",f"A documentary wide shot of an abandoned Iraqi farm field, withered brown crops and a bone-dry cracked irrigation canal, a lone farmer figure far in the distance, dust and haze, dignified, no identifiable face, {NEG}, {X}"),
    (WAT, "broll_3.jpg",f"Vertical portrait 9:16 photo, upright orientation, level horizon: a gritty documentary shot of a water tanker truck filling plastic jerrycans for residents in a poor southern Iraqi neighbourhood under brutal summer sun, people standing and carrying containers, heat shimmer, faces not clearly identifiable, {NEG}, {X}"),
    # 4) SAUDI PIF SQUEEZE — Gulf oil-price fiscal lever
    (PIF, "hero.jpg",   f"A cinematic dusk aerial of the modern Riyadh skyline with gleaming skyscrapers and a distinctive tall tower, warm golden haze over a wealthy Gulf capital, a subtle sense of fiscal pressure, wide establishing shot, {NEG}, {X}"),
    (PIF, "broll_1.jpg",f"A moody cinematic interior of a grand Gulf finance-ministry hall with polished marble floors and tall columns, a lone official in a thobe walking away down the long empty space, dramatic overhead light, weight of a fiscal decision, no identifiable face, {NEG}, {X}"),
    (PIF, "broll_2.jpg",f"A cinematic wide aerial at dusk of a vast half-finished Gulf mega-project construction site, idle tower cranes and bare concrete tower skeletons, no workers, an eerie sense of a paused giga-project, {NEG}, {X}"),
    (PIF, "broll_3.jpg",f"A cinematic close silhouette of a desert oil pumpjack against a burnt-orange sunset with a single distant gas flare, heat haze, a heavy sense of oil-price pressure, {NEG}, {X}"),
    # 5) SICKLE-CELL GENE THERAPY — health register-break / hope
    (SIC, "hero.jpg",   f"A breathtaking cinematic macro of glowing blue DNA double-helix strands floating over a dark scientific background with soft red blood cells drifting past, a hopeful sense of a gene-therapy breakthrough, {NEG}, {X}"),
    (SIC, "broll_1.jpg",f"A pristine modern Gulf hospital research laboratory, scientists in white coats gloves and masks working at gleaming biotech equipment under cool blue light, advanced precision medicine, faces not clearly identifiable, {NEG}, {X}"),
    (SIC, "broll_2.jpg",f"An extreme cinematic macro of a gloved hand holding a small vial of faintly glowing cell suspension beside a laboratory microscope and coloured pipettes, shallow depth of field, precision biotech, {NEG}, {X}"),
    (SIC, "broll_3.jpg",f"A warm hopeful cinematic shot of an out-of-focus Middle Eastern family silhouette standing by a sunlit hospital window, gentle golden light, a tender sense of relief and hope, faces not clearly identifiable, {NEG}, {X}"),
]

def submit_retry(p, tries=5):
    last = None
    for i in range(tries):
        try: return submit(p)
        except Exception as e: last = e; time.sleep(3*(i+1))
    raise last

def main():
    jobs = []
    print(f"== Submitting {len(JOBS)} scene jobs ==", flush=True)
    for slug, fname, prompt in JOBS:
        out = IMG_ROOT / slug / fname
        if out.exists() and out.stat().st_size > 50_000:
            print(f"  = skip {slug}/{fname}"); continue
        try:
            tid = submit_retry(prompt)
            jobs.append({"slug": slug, "file": fname, "out": out, "tid": tid, "ok": False})
            print(f"  + {slug}/{fname} {tid}", flush=True)
        except Exception as e:
            print(f"  ! submit {slug}/{fname}: {e}", file=sys.stderr, flush=True)
        time.sleep(0.8)
    pending = [j for j in jobs if j.get("tid")]
    print(f"\n== Polling {len(pending)} ==", flush=True)
    deadline = time.time() + 20*60
    while pending and time.time() < deadline:
        time.sleep(POLL_INTERVAL)
        still = []
        for j in pending:
            try: r = http_get(f"{STATUS_URL}?taskId={j['tid']}")
            except Exception: still.append(j); continue
            data = r.get("data") or {}
            st = data.get("state")
            if st == "success":
                url = first_image_url(data)
                if not url: still.append(j); continue
                try: download(url, j["out"]); j["ok"] = True; print(f"  ✓ {j['slug']}/{j['file']}", flush=True)
                except Exception as e: print(f"  ! dl {j['slug']}/{j['file']}: {e}", file=sys.stderr); still.append(j)
            elif st == "fail":
                print(f"  ✗ {j['slug']}/{j['file']} FAIL {str(data)[:120]}", file=sys.stderr)
            else: still.append(j)
        pending = still
        print(f"  ... {len(pending)} pending", flush=True)
    ok = sum(1 for j in jobs if j["ok"])
    print(f"\n== DONE {ok}/{len(JOBS)} ==", flush=True)
    for j in jobs:
        if not j["ok"]: print(f"  MISSING {j['slug']}/{j['file']}")
    return 0 if ok == len(JOBS) else 1

if __name__ == "__main__":
    sys.exit(main())
