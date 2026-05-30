#!/usr/bin/env python3
"""Generate the 20 non-face AI scenes for 2026-05-30 via Nano Banana Pro (9:16, 2K).
Faces (Netanyahu/MBS/al-Sharaa/Isaacman) are real photos fetched separately into
each slug's broll_1.jpg. Every scene prompt MATCHES its target beat's text.
"""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

D = "2026-05-30"
# (slug, filename, prompt)
JOBS = [
    # 1. IRAQ WATER CRISIS (all 4 generated)
    (f"{D}-iraq-water-crisis", "hero.jpg", f"The cracked dry riverbed of the Euphrates in Iraq, deep fissures in the parched orange earth, a stranded wooden fishing boat resting on the cracked ground, scorching sun and heat haze, desolate, wide cinematic establishing shot, {NEG}"),
    (f"{D}-iraq-water-crisis", "broll_1.jpg", f"Aerial view of a dramatically shrunken Tigris river in Iraq winding through parched brown land, wide exposed sandbars and mudflats, very low water, drought, dramatic wide shot, {NEG}"),
    (f"{D}-iraq-water-crisis", "broll_2.jpg", f"A large concrete dam upstream holding back a reservoir while the riverbed downstream is nearly dry and cracked, arid mountains, water scarcity, daylight aerial wide shot, {NEG}"),
    (f"{D}-iraq-water-crisis", "broll_3.jpg", f"Iraqi residents in Basra collecting water from a parked tanker truck on a dusty street, filling yellow plastic jerricans, harsh midday sunlight, documentary photojournalism, {NEG}"),
    # 2. GAZA SEIZURE 70 (broll_1 = Netanyahu face)
    (f"{D}-gaza-seizure-70", "hero.jpg", f"Aerial view of a devastated Gaza cityscape, destroyed concrete buildings and grey rubble stretching to the horizon, overcast sky, somber documentary wide shot, {NEG}"),
    (f"{D}-gaza-seizure-70", "broll_2.jpg", f"Israeli military armored vehicles beside a fortified earthen berm marking a demarcation line cutting across a flattened Gaza neighborhood of rubble, tense, documentary photojournalism, {NEG}"),
    (f"{D}-gaza-seizure-70", "broll_3.jpg", f"Israeli soldiers in combat gear at a forward military position in Gaza at dusk, distant smoke rising on the horizon, tense, documentary photojournalism, {NEG}"),
    # 3. OIL WORST MONTH (all 4 generated)
    (f"{D}-oil-worst-month", "hero.jpg", f"A financial trading floor with huge wall screens showing a steeply falling crude oil price line chart glowing red, blurred traders in the foreground, tense market crash mood, {NEG}"),
    (f"{D}-oil-worst-month", "broll_1.jpg", f"Extreme close-up of a stock-market display board showing crude oil prices dropping sharply, red downward arrows and red candlestick charts, the number 92 visible, dramatic, {NEG}"),
    (f"{D}-oil-worst-month", "broll_2.jpg", f"Aerial wide shot of a giant crude oil supertanker crossing the calm Strait of Hormuz at dawn, golden light on steel-blue gulf water, hazy distant coastline, strategic tension, {NEG}"),
    (f"{D}-oil-worst-month", "broll_3.jpg", f"A single oil pumpjack and pipeline standing idle in the Arabian desert at dusk, burnt-orange sky, long shadows, sense of an oil-market slowdown, cinematic wide shot, {NEG}"),
    # 4. NEOM LINE HALT (broll_1 = MBS face)
    (f"{D}-neom-line-halt", "hero.jpg", f"A vast stalled megaproject construction site in the Saudi Arabian desert, idle tower cranes and unfinished concrete foundations stretching into the distance, abandoned scale, harsh daylight, wide cinematic, {NEG}"),
    (f"{D}-neom-line-halt", "broll_2.jpg", f"A futuristic mirrored linear skyscraper concept rising straight from the desert, only partially built, its glass walls reflecting orange dusk, dwarfing the empty landscape, conceptual cinematic, {NEG}"),
    (f"{D}-neom-line-halt", "broll_3.jpg", f"An industrial port and modern data-center complex on the Red Sea coast of Saudi Arabia, cranes, warehouses and solar arrays, practical infrastructure, aerial wide establishing shot, {NEG}"),
    # 5. SYRIA ENERGY DEAL (broll_1 = al-Sharaa face)
    (f"{D}-syria-energy-deal", "hero.jpg", f"Damascus Syria skyline at golden dusk, minarets and modern buildings, the distant Mount Qasioun behind, warm hazy light, wide aerial establishing shot, {NEG}"),
    (f"{D}-syria-energy-deal", "broll_2.jpg", f"A large natural-gas power plant with tall stacks beside a vast field of blue solar panels under a bright sky, high-voltage transmission lines, industrial energy infrastructure, wide aerial shot, {NEG}"),
    (f"{D}-syria-energy-deal", "broll_3.jpg", f"Construction cranes and workers rebuilding a war-damaged Syrian city, new concrete buildings rising beside scarred ruins, hopeful reconstruction, daytime documentary wide shot, {NEG}"),
    # 6. NASA MOONBASE (broll_1 = Isaacman face)
    (f"{D}-nasa-moonbase", "hero.jpg", f"A futuristic lunar base with a lander and silver habitat modules on the grey cratered surface of the Moon, the blue Earth rising in the black sky, ultra-realistic NASA-style space photography, {NEG}"),
    (f"{D}-nasa-moonbase", "broll_2.jpg", f"A robotic lunar lander descending toward the rugged shadowed terrain of the Moon's south pole, blue engine glow beneath it, sharp craters, stars, ultra-realistic space photography, {NEG}"),
    (f"{D}-nasa-moonbase", "broll_3.jpg", f"Two astronauts in white spacesuits walking on the grey lunar surface beside a landing craft, the blue Earth in the black sky behind them, Artemis program, ultra-realistic NASA-style photography, {NEG}"),
]


def main():
    jobs = []
    print(f"== Submitting {len(JOBS)} scene jobs ==", flush=True)
    for slug, fname, prompt in JOBS:
        out = IMG_ROOT / slug / fname
        try:
            tid = submit(prompt)
            jobs.append({"slug": slug, "file": fname, "out": out, "tid": tid, "ok": False})
            print(f"  + {slug}/{fname} tid={tid}", flush=True)
        except Exception as e:
            print(f"  ! submit {slug}/{fname}: {e}", file=sys.stderr, flush=True)
        time.sleep(0.5)
    pending = [j for j in jobs if j.get("tid")]
    print(f"\n== Polling {len(pending)} ==", flush=True)
    deadline = time.time() + 16 * 60
    while pending and time.time() < deadline:
        time.sleep(POLL_INTERVAL)
        still = []
        for j in pending:
            try:
                r = http_get(f"{STATUS_URL}?taskId={j['tid']}")
            except Exception:
                still.append(j); continue
            data = r.get("data") or {}
            st = data.get("state")
            if st == "success":
                url = first_image_url(data)
                if not url:
                    j["done"] = True; continue
                try:
                    info = download(url, j["out"]); j["ok"] = True
                    print(f"  ✓ {j['slug']}/{j['file']} {info}", flush=True)
                except Exception as e:
                    print(f"  ! dl {j['slug']}/{j['file']}: {e}", file=sys.stderr, flush=True)
            elif st == "fail":
                print(f"  ✗ {j['slug']}/{j['file']} FAIL {str(data)[:120]}", file=sys.stderr, flush=True)
            else:
                still.append(j)
        pending = still
        if pending:
            print(f"    ... {len(pending)} generating", flush=True)
    ok = sum(1 for j in jobs if j["ok"])
    print(f"\n== Done {ok}/{len(JOBS)} ==", flush=True)
    fails = [f"{j['slug']}/{j['file']}" for j in jobs if not j["ok"]]
    if fails:
        for f in fails:
            print(f"  FAIL: {f}", file=sys.stderr)
    return 0 if ok == len(JOBS) else 1


if __name__ == "__main__":
    sys.exit(main())
