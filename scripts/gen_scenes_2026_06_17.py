#!/usr/bin/env python3
"""Generate the AI scenes for the 2026-06-17 slate via Nano Banana Pro (9:16, 2K).
One still per beat, each prompt MATCHED to its target beat's text. Strong
no-text/no-UI/no-screenshot/no-logo negatives.

Real-face slot this slate: worldcup-messi-hattrick/broll_1 is OVERWRITTEN by a
real Lionel Messi Commons portrait (see fetch_faces_2026_06_17.py) — the
celebration scene generated here is only a fallback if that fetch fails.
All other slots are scene-only (no centrally-named single individual)."""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

D = "2026-06-17"
GUARD = ("absolutely no text, no captions, no Instagram or app UI, no phone screen interface, no watermark, "
         "no logos, no brand marks, no jersey numbers, no scoreboard numbers, no registration codes, "
         "one single uncropped photograph, single continuous wide shot, one frame only, not a collage, "
         "not a grid, not split panels, photorealistic editorial photograph")

JOBS = [
    # 1. IRAQ POWER / BLACKOUT SUMMER (iraq_domestic, A) — grid, dark city, heat, gas, solar
    (f"{D}-iraq-power-summer", "hero.jpg", f"A sprawling Middle Eastern capital city at dusk under a hazy blazing orange heat-sky, large dark patches where whole neighborhoods sit without power, only scattered lights glowing, tall electricity transmission pylons in the foreground, an oppressive summer-heat atmosphere, photorealistic editorial aerial wide shot, no readable text, no logos, {GUARD}, {NEG}"),
    (f"{D}-iraq-power-summer", "broll_1.jpg", f"A dense Baghdad-like residential street at night mostly in darkness during a blackout, a few windows lit by small private generators, tangled web of low-hanging neighborhood power cables overhead, warm dim glow, photorealistic documentary night shot, no readable text, no logos, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-iraq-power-summer", "broll_2.jpg", f"A large power station with tall chimneys and a bright orange gas flare burning against a dusty twilight sky in an arid landscape, heavy industrial energy infrastructure, a sense of strained supply, photorealistic editorial wide shot, no readable text, no logos, {GUARD}, {NEG}"),
    (f"{D}-iraq-power-summer", "broll_3.jpg", f"A vast field of modern blue solar photovoltaic panels stretching across a sunny southern Iraqi desert under a brilliant clear sky, distant palm trees, a sense of a hopeful clean-energy alternative, photorealistic editorial wide aerial shot, no readable text, no logos, {GUARD}, {NEG}"),
    # 2. WORLD CUP — MESSI HAT-TRICK (wildcard/sport, C) — stadium, celebration, ball; broll_1 -> real Messi face
    (f"{D}-worldcup-messi-hattrick", "hero.jpg", f"A euphoric packed World Cup football stadium at night under brilliant floodlights, a vast sea of fans in sky-blue and white celebrating wildly, confetti drifting in the air, an electric moment of triumph, photorealistic editorial wide shot, no readable text, no logos, no jersey numbers, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-worldcup-messi-hattrick", "broll_1.jpg", f"A lone football player in a plain unmarked sky-blue shirt celebrating a goal with arms spread wide before a roaring packed stadium crowd, joyful triumphant body language, seen from behind so the face is not visible, photorealistic sports action shot, no jersey numbers, no logos, no readable text, {GUARD}, {NEG}"),
    (f"{D}-worldcup-messi-hattrick", "broll_2.jpg", f"A football frozen mid-flight bulging into the back of a white goal net under bright stadium floodlights, water droplets and net detail crisp, a decisive goal-scoring moment, photorealistic high-speed sports shot, no logos, no numbers, no readable text, {GUARD}, {NEG}"),
    (f"{D}-worldcup-messi-hattrick", "broll_3.jpg", f"A gleaming golden football trophy on a plinth glowing under dramatic stadium spotlights at night with a softly blurred packed crowd behind, a sense of glory and destiny, photorealistic editorial shot, no readable text, no logos, {GUARD}, {NEG}"),
    # 3. LEBANON CEASEFIRE / RETURN (mena_geopolitics, A) — south Lebanon, returning families, flags, border
    (f"{D}-lebanon-ceasefire-return", "hero.jpg", f"A quiet southern Lebanese hillside village at golden dawn with weathered and partly damaged stone houses among olive groves, soft hopeful morning light, a calm after-conflict stillness, photorealistic editorial wide shot, no people, no readable text, no logos, {GUARD}, {NEG}"),
    (f"{D}-lebanon-ceasefire-return", "broll_1.jpg", f"A line of cars loaded with household belongings driving along a rural road back toward a southern Lebanese village under soft daylight, distant anonymous silhouetted figures, a sense of families returning home, photorealistic documentary wide shot, no recognizable faces, no readable text, no logos, no license plates, {GUARD}, {NEG}"),
    (f"{D}-lebanon-ceasefire-return", "broll_2.jpg", f"A row of plain unmarked flags on tall poles fluttering against a pale sky in front of a modern diplomatic building, a neutral atmosphere of negotiation, photorealistic editorial wide shot, no people, no emblems, no readable text, no logos, {GUARD}, {NEG}"),
    (f"{D}-lebanon-ceasefire-return", "broll_3.jpg", f"A still hilly border landscape in southern Lebanon at dusk with cypress and olive trees and a winding empty road, distant hazy hills, a fragile uncertain calm, photorealistic editorial landscape, no people, no readable text, no logos, {GUARD}, {NEG}"),
    # 4. WMO CLIMATE / 1.5C (wildcard/climate, B) — heat, glowing earth, ice melt, drought
    (f"{D}-wmo-climate-15c", "hero.jpg", f"A blistering sun hanging huge and orange over a heat-shimmering cracked dry landscape, distorted rippling air from extreme heat, a vast empty parched plain, an ominous record-heat atmosphere, photorealistic editorial wide shot, no readable text, no logos, {GUARD}, {NEG}"),
    (f"{D}-wmo-climate-15c", "broll_1.jpg", f"A glowing visualization of planet Earth seen from space flushed in deep reds and oranges indicating extreme warmth, swirling atmosphere, dramatic and clean, photorealistic render, no readable text, no labels, no country borders, no logos, {GUARD}, {NEG}"),
    (f"{D}-wmo-climate-15c", "broll_2.jpg", f"A dramatic Arctic scene of a vast pale blue glacier calving and melting into dark ocean water with meltwater streams, a sense of accelerating change, photorealistic editorial wide shot, no people, no readable text, no logos, {GUARD}, {NEG}"),
    (f"{D}-wmo-climate-15c", "broll_3.jpg", f"A deeply cracked dry lakebed under a harsh white sky with a few withered shrubs, severe drought, heat haze on the horizon, photorealistic editorial wide shot, no people, no readable text, no logos, {GUARD}, {NEG}"),
    # 5. AI LABS GO PUBLIC (tech_ai, B) — neural glow + rising chart, server HQ, abstract exchange
    (f"{D}-ai-labs-go-public", "hero.jpg", f"A sleek abstract visualization of a glowing blue-and-gold neural network merging into a steeply rising luminous financial growth curve, dark elegant background, a sense of an AI industry surging onto markets, photorealistic 3D render, no readable text, no numbers, no logos, {GUARD}, {NEG}"),
    (f"{D}-ai-labs-go-public", "broll_1.jpg", f"A vast modern AI data center with endless symmetrical rows of tall black server racks glowing with cool blue indicator lights, polished reflective floor, dramatic vanishing-point perspective, immense scale, photorealistic editorial wide shot, no readable text, no logos, {GUARD}, {NEG}"),
    (f"{D}-ai-labs-go-public", "broll_2.jpg", f"An abstract modern stock-exchange atmosphere with luminous green upward-rising arcs and glowing candlestick-like bars of light soaring across a dark elegant trading hall, a sense of a historic market debut, photorealistic render, no readable text, no numbers, no logos, {GUARD}, {NEG}"),
    (f"{D}-ai-labs-go-public", "broll_3.jpg", f"A glowing abstract digital human brain made of luminous circuitry and flowing data streams rising upward against a dark background, a sense of powerful artificial intelligence and momentum, photorealistic render, no readable text, no logos, {GUARD}, {NEG}"),
    # 6. FENTANYL OVERDOSE VACCINE (wildcard/health, A) — vial, antibodies, lab
    (f"{D}-fentanyl-overdose-vaccine", "hero.jpg", f"A bright clean medical macro close-up of a single clear glass vaccine vial with a metallic cap on a soft-lit clinical surface, a faint blue glow, a hopeful breakthrough-medicine atmosphere, shallow depth of field, photorealistic shot, no readable text, no logos, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-fentanyl-overdose-vaccine", "broll_1.jpg", f"A clear glass medical vial beside a fine syringe on a bright clinical white surface with soft daylight, a clean modern pharmaceutical look, photorealistic macro shot, no readable text, no logos, no faces, {GUARD}, {NEG}"),
    (f"{D}-fentanyl-overdose-vaccine", "broll_2.jpg", f"A clean abstract scientific render of glowing Y-shaped antibody molecules binding to and surrounding a small drug molecule in a bloodstream, blue and teal tones, intercepting it before it spreads, photorealistic microscopic visualization, no readable text, no logos, {GUARD}, {NEG}"),
    (f"{D}-fentanyl-overdose-vaccine", "broll_3.jpg", f"A bright modern biomedical research laboratory with clean glassware, pipettes and a rack of small vials under soft clinical light, a sense of active vaccine development, photorealistic editorial wide shot, no readable text, no logos, no recognizable faces, {GUARD}, {NEG}"),
]


def main():
    only = set(sys.argv[1:])
    sel = [(s, f, p) for (s, f, p) in JOBS if not only or f"{s}/{f}" in only or s in only]
    print(f"== Submitting {len(sel)} scene jobs ==", flush=True)
    jobs = []
    for slug, fname, prompt in sel:
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
    deadline = time.time() + 18 * 60
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
        print(f"  .. {len(pending)} pending", flush=True)
    ok = sum(1 for j in jobs if j.get("ok"))
    print(f"\n== Done: {ok}/{len(jobs)} images ==", flush=True)
    return 0 if ok == len(jobs) else 1


if __name__ == "__main__":
    sys.exit(main())
