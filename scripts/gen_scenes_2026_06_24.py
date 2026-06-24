#!/usr/bin/env python3
"""Generate AI scenes for the 2026-06-24 slate via Nano Banana Pro 9:16 2K.
One still per beat — no cycling. Faces (Rubio, MBS) fetched separately.
For rubio-gulf-tour and saudi-pif-sports-pivot, broll_1 is a real Commons face — not generated here.
"""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

D = "2026-06-24"
X = "absolutely no on-screen text, no Arabic or English writing, no captions, no Instagram or app UI, no fake screenshots, no scoreboard graphics, no watermark, no logos, no garbled characters"

JOBS = [
    # 1. IRAQ RICE REBOUND — hopeful green agriculture, water returning
    (f"{D}-iraq-rice-rebound", "hero.jpg", f"Lush green flooded rice paddy fields in southern Iraq at golden sunrise, still water mirroring a soft sky, date palms on the horizon, a farmer's distant silhouette, hopeful documentary agriculture photography, {NEG}, {X}"),
    (f"{D}-iraq-rice-rebound", "broll_1.jpg", f"A large reservoir behind a concrete dam in Iraq brimming with turquoise water, arid tan hills around it, abundant water after drought, bright daylight aerial wide shot, {NEG}, {X}"),
    (f"{D}-iraq-rice-rebound", "broll_2.jpg", f"Close documentary shot of Iraqi farmers in light clothing wading in a flooded rice paddy planting bright green rice seedlings, water reflections, warm morning light, {NEG}, {X}"),
    (f"{D}-iraq-rice-rebound", "broll_3.jpg", f"The Tigris river winding through an arid Iraqi landscape lined with date palms, calm brown-green water, hazy daylight, wide aerial documentary shot, {NEG}, {X}"),
    # 2. RUBIO GULF TOUR — hero + Gulf scenes (broll_1 = real Rubio face, fetched separately)
    (f"{D}-rubio-gulf-tour", "hero.jpg", f"A formal diplomatic meeting hall in a Gulf state, a long polished table with the flag of the United States and the flags of Gulf states standing upright, empty leather chairs, soft daylight, no people, {NEG}, {X}"),
    (f"{D}-rubio-gulf-tour", "broll_2.jpg", f"Aerial view of a massive crude oil supertanker crossing the calm steel-blue waters of the Strait of Hormuz at dawn, faint hazy coastline, strategic maritime passage, cinematic wide shot, {NEG}, {X}"),
    (f"{D}-rubio-gulf-tour", "broll_3.jpg", f"The Manama Bahrain skyline at dusk along the Gulf waterfront, modern glass towers glowing, calm sea in front, wide aerial establishing shot, {NEG}, {X}"),
    # 3. EUROPE HEAT DOME — oppressive heat, drought
    (f"{D}-europe-heat-dome", "hero.jpg", f"A blazing white-hot sun hanging over a European city skyline through a thick shimmering heat haze, oppressive summer heat, washed-out pale sky, wide cinematic shot, {NEG}, {X}"),
    (f"{D}-europe-heat-dome", "broll_1.jpg", f"A sun-scorched European city plaza at midday in extreme heat, a few people seeking shade under sparse trees, shimmering heat haze rising off the pavement, harsh light, {NEG}, {X}"),
    (f"{D}-europe-heat-dome", "broll_2.jpg", f"Cracked dry parched earth and a withered golden field under a harsh sun, faint wildfire smoke on the distant horizon, severe drought documentary photography, {NEG}, {X}"),
    (f"{D}-europe-heat-dome", "broll_3.jpg", f"A glowing red outdoor thermometer rising high against a sweltering deep-orange sky over a parched landscape, climate-warning mood, conceptual cinematic, {NEG}, {X}"),
    # 4. CLINICAL AI BENCHMARK — clean medical tech, no readable text
    (f"{D}-clinical-ai-benchmark", "hero.jpg", f"An abstract glowing blue digital brain made of a neural network of light hovering above a clean modern hospital corridor, cool blue and white medical-tech aesthetic, {NEG}, {X}"),
    (f"{D}-clinical-ai-benchmark", "broll_1.jpg", f"A doctor in a white coat consulting a glowing translucent holographic medical interface with abstract glowing icons, cool blue lighting, modern clinic, no readable text on the screen, {NEG}, {X}"),
    (f"{D}-clinical-ai-benchmark", "broll_2.jpg", f"A clinician reviewing abstract glowing data charts on several monitors with a stethoscope resting on the desk, modern hospital office, cool light, no readable numbers or text on screens, {NEG}, {X}"),
    (f"{D}-clinical-ai-benchmark", "broll_3.jpg", f"A conceptual balanced scale with a glowing AI microchip on one side and a glowing medical cross on the other, clean blue gradient background, symbolic, no text, {NEG}, {X}"),
    # 5. METEORITE LOST WORLD — desert specimen + deep space
    (f"{D}-meteorite-lost-world", "hero.jpg", f"A dark fist-sized meteorite rock resting on rippled golden Sahara desert sand under a deep blue starry twilight sky, dramatic low light, scientific specimen, cinematic, {NEG}, {X}"),
    (f"{D}-meteorite-lost-world", "broll_1.jpg", f"Cinematic space art of a glowing rocky moon-sized protoplanet orbiting the young bright Sun in the early solar system, swirling debris and dust, deep space, {NEG}, {X}"),
    (f"{D}-meteorite-lost-world", "broll_2.jpg", f"A deep-space comparison scene of a grey rocky moon-sized world beside a larger reddish Mars-like planet against a dense starfield, cinematic astronomy art, no text, {NEG}, {X}"),
    (f"{D}-meteorite-lost-world", "broll_3.jpg", f"A scientist in a lab examining a small dark meteorite fragment under a microscope, a glowing colorful mineral cross-section visible on a nearby screen, cool blue lab light, no readable text, {NEG}, {X}"),
    # 6. SAUDI PIF PIVOT — Riyadh + paused stadium + heritage tourism (broll_1 = real MBS face, fetched separately)
    (f"{D}-saudi-pif-sports-pivot", "hero.jpg", f"The Riyadh Saudi Arabia skyline at golden dusk with the distinctive Kingdom Centre tower and modern financial-district skyscrapers, warm desert haze, wide aerial establishing shot, {NEG}, {X}"),
    (f"{D}-saudi-pif-sports-pivot", "broll_2.jpg", f"A vast empty modern football stadium under bright floodlights at night with no crowd, rows of empty seats, a quiet sense of paused ambition, cinematic wide shot, {NEG}, {X}"),
    (f"{D}-saudi-pif-sports-pivot", "broll_3.jpg", f"A vibrant Saudi heritage tourism scene at night, the illuminated mud-brick old town of Diriyah with warm golden lights and visitors strolling narrow lanes, cultural tourism photography, {NEG}, {X}"),
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
                    continue
                try:
                    info = download(url, j["out"]); j["ok"] = True
                    print(f"  ✓ {j['slug']}/{j['file']} {info}", flush=True)
                except Exception as e:
                    print(f"  ! dl {j['slug']}/{j['file']}: {e}", file=sys.stderr, flush=True)
            elif st == "fail":
                print(f"  ✗ {j['slug']}/{j['file']} FAIL {str(data)[:160]}", file=sys.stderr, flush=True)
            else:
                still.append(j)
        pending = still
        print(f"  ... {len(pending)} pending", flush=True)
    ok = sum(1 for j in jobs if j["ok"])
    print(f"\n== DONE {ok}/{len(JOBS)} scenes ==", flush=True)
    for j in jobs:
        if not j["ok"]:
            print(f"  MISSING {j['slug']}/{j['file']}", flush=True)
    return 0 if ok == len(JOBS) else 1


if __name__ == "__main__":
    sys.exit(main())
