#!/usr/bin/env python3
"""Generate the 21 non-face AI scenes for the 2026-07-03 slate via Nano Banana Pro.
Faces (LeBron / Giannis / MBS) are real Commons photos, fetched separately.
Reuses gen_2026_05_28 infrastructure (submit / poll / download).
"""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

D = "2026-07-03"
# Hardened anti-UI negatives for any scene with screens/maps/charts
NOUI = "no user interface, no app screenshot, no dashboard, no infographic, no readable text, no numbers, no gibberish letters, no logos, no watermark"

# (slug, filename, prompt)
JOBS = [
    # GLOBAL WILDFIRE RECORD (climate)
    (f"{D}-global-wildfire-record", "hero.jpg", f"A massive forest wildfire at night, towering walls of orange flame engulfing a hillside of pine trees, thick glowing smoke against a black sky, embers flying, apocalyptic scale, aerial wide shot, {NEG}"),
    (f"{D}-global-wildfire-record", "broll_1.jpg", f"Aerial view of a vast charred blackened landscape after a wildfire, smoldering scorched earth stretching to the horizon, thin smoke rising, bleak grey daylight, {NEG}"),
    (f"{D}-global-wildfire-record", "broll_2.jpg", f"A dense forest fire sweeping through a South Asian tropical forest, orange flames and heavy grey smoke among green foliage, dramatic documentary, {NEG}"),
    (f"{D}-global-wildfire-record", "broll_3.jpg", f"A parched cracked-earth riverbed in the Amazon rainforest during severe drought, bare dead trees, hazy smoke on the horizon, harsh sunlight, ominous climate wide shot, {NEG}"),
    # IRAQ BUDGET FREEZE (iraq_domestic)
    (f"{D}-iraq-budget-freeze", "hero.jpg", f"Interior of a modern Iraqi parliamentary chamber, curved rows of empty seats, the flag of Iraq (red white and black horizontal bands with green Arabic script) on the front wall, formal government assembly hall, dramatic overhead lighting, no people, {NEG}"),
    (f"{D}-iraq-budget-freeze", "broll_1.jpg", f"A stack of Iraqi dinar banknotes on a wooden desk beside a paper ledger and a calculator in a dim government office, a shaft of light, austere fiscal mood, still life, {NEG}, {NOUI}"),
    (f"{D}-iraq-budget-freeze", "broll_2.jpg", f"Close-up of Iraqi dinar banknotes and coins scattered on a dark surface under a single hard spotlight, deep shadows, sense of financial scarcity, macro photography, {NEG}, {NOUI}"),
    (f"{D}-iraq-budget-freeze", "broll_3.jpg", f"An unfinished public building project in an Iraqi city, idle tower cranes and bare grey concrete floors under a hazy sky, stalled development, wide aerial shot, {NEG}"),
    # MILKY WAY DARK MATTER (science)
    (f"{D}-milkyway-dark-matter", "hero.jpg", f"The glowing dense core of the Milky Way galaxy, brilliant golden star clouds and dark dust lanes, a faint spherical haze at the very center, deep space astrophotography, cinematic, {NEG}"),
    (f"{D}-milkyway-dark-matter", "broll_1.jpg", f"Abstract cosmic visualization of a faint spherical gamma-ray glow radiating from the center of a spiral galaxy, purple and gold energy haze against black space, scientific render, {NEG}, {NOUI}"),
    (f"{D}-milkyway-dark-matter", "broll_2.jpg", f"A dark astrophysics research room bathed in cool blue light, a large glowing abstract colorful all-sky heatmap projection on the wall, a silhouetted scientist studying it, {NEG}, {NOUI}"),
    (f"{D}-milkyway-dark-matter", "broll_3.jpg", f"Deep space filled with countless glowing pulsars and neutron stars, beams of radiation sweeping across a dense starfield near a bright galactic core, mysterious blue-violet haze, cinematic, {NEG}"),
    # NBA FREE AGENCY (sport) — hero + broll_2 only (broll_1=LeBron, broll_3=Giannis are faces)
    (f"{D}-nba-free-agency-quake", "hero.jpg", f"A dramatic empty indoor basketball arena at night, a single spotlight on the polished hardwood court, thousands of empty dark seats around it, moody cinematic wide shot, {NEG}, {NOUI}"),
    (f"{D}-nba-free-agency-quake", "broll_2.jpg", f"A lone orange basketball resting on a spotlit hardwood court in a dark arena, dramatic shadows, tense anticipation, ultra-realistic close-up, {NEG}, {NOUI}"),
    # QATAR FDI RECORD (gulf_regional)
    (f"{D}-qatar-fdi-record", "hero.jpg", f"Doha Qatar skyline at dusk, the distinctive cluster of modern skyscrapers along the West Bay corniche, calm Gulf water reflecting golden and blue light, wide aerial establishing shot, {NEG}"),
    (f"{D}-qatar-fdi-record", "broll_1.jpg", f"A gleaming modern financial district in Doha with glass towers and construction cranes at golden hour, sense of investment and rapid growth, wide shot, {NEG}"),
    (f"{D}-qatar-fdi-record", "broll_2.jpg", f"The national flags of the United Arab Emirates and Qatar flying side by side on tall poles against a clear blue sky in front of modern glass towers, low heroic angle, {NEG}"),
    (f"{D}-qatar-fdi-record", "broll_3.jpg", f"A cinematic dusk skyline of Gulf financial towers reflected on calm water, warm golden haze, a sense of capital and prosperity, wide establishing shot, {NEG}"),
    # SAUDI-LED AXIS (mena_geopolitics) — hero + broll_2/3 (broll_1=MBS face)
    (f"{D}-saudi-led-axis", "hero.jpg", f"The national flags of Saudi Arabia, Qatar, Turkey, Egypt and Pakistan flying together on a row of tall flagpoles against a dramatic cloudy dusk sky, low heroic angle, sense of a new alliance, {NEG}"),
    (f"{D}-saudi-led-axis", "broll_2.jpg", f"A large geopolitical map of the Middle East region on a dark table under a focused overhead light, small national flag pins clustered across the region, a strategy-room mood, {NEG}, {NOUI}"),
    (f"{D}-saudi-led-axis", "broll_3.jpg", f"The national flag of the United Arab Emirates flying alone on a tall pole set apart from a distant cluster of other flags, overcast dusk sky, sense of divergence and distance, cinematic, {NEG}"),
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
                    print(f"  OK {j['slug']}/{j['file']} {info}", flush=True)
                except Exception as e:
                    print(f"  ! dl {j['slug']}/{j['file']}: {e}", file=sys.stderr, flush=True)
            elif st == "fail":
                print(f"  x {j['slug']}/{j['file']} FAIL {str(data)[:120]}", file=sys.stderr, flush=True)
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
