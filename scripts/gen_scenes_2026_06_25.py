#!/usr/bin/env python3
"""Generate AI scenes for the 2026-06-25 slate via Nano Banana Pro 9:16 2K.
One still per beat — no cycling. The only real face (Giannis Antetokounmpo)
is fetched separately into giannis-heat-trade/broll_1.jpg.
"""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

D = "2026-06-25"
X = "absolutely no on-screen text, no Arabic or English writing, no captions, no Instagram or app UI, no fake screenshots, no scoreboard graphics, no watermark, no logos, no brand marks, no garbled characters"

JOBS = [
    # 1. IRAQ POWER GRID CRISIS — blackout, heat, gas plants
    (f"{D}-iraq-power-grid-crisis", "hero.jpg", f"A sprawling Iraqi city skyline at dusk under a hazy orange sky during a power blackout, most buildings dark with only scattered lights, distant electricity transmission towers silhouetted, oppressive summer heat haze, wide cinematic establishing shot, {NEG}, {X}"),
    (f"{D}-iraq-power-grid-crisis", "broll_1.jpg", f"Tall high-voltage electricity transmission pylons and sagging power lines stretching across an arid sun-baked Iraqi landscape under a blazing white sky, heat shimmer rising, documentary wide shot, {NEG}, {X}"),
    (f"{D}-iraq-power-grid-crisis", "broll_2.jpg", f"A natural-gas power plant with tall cooling towers and pipelines in Iraq under harsh daylight, partly idle industrial energy infrastructure, wide documentary shot, {NEG}, {X}"),
    (f"{D}-iraq-power-grid-crisis", "broll_3.jpg", f"A crowded Iraqi street at night during a blackout lit only by a few private diesel generators and car headlights, people in the heat, tense documentary mood, {NEG}, {X}"),
    # 2. GIANNIS HEAT TRADE — arena scenes (broll_1 = real Giannis face, fetched separately)
    (f"{D}-giannis-heat-trade", "hero.jpg", f"A dramatic empty professional basketball arena interior with a glossy hardwood court and a single hoop lit by a bright spotlight, empty tiered seats fading into shadow, cinematic sports atmosphere, {NEG}, {X}"),
    (f"{D}-giannis-heat-trade", "broll_2.jpg", f"The Miami waterfront skyline at golden dusk with modern glass skyscrapers along the bay, palm trees, warm tropical light, wide aerial establishing shot, {NEG}, {X}"),
    (f"{D}-giannis-heat-trade", "broll_3.jpg", f"An empty basketball arena at night with rows of vacant seats and a dim spotlit hardwood court, a quiet contemplative end-of-an-era mood, cinematic wide shot, {NEG}, {X}"),
    # 3. LEBANON ISRAEL TALKS — diplomacy + somber landscape
    (f"{D}-lebanon-israel-talks", "hero.jpg", f"A formal diplomatic negotiation hall with a long polished wooden table, plain flags on stands, empty leather chairs facing each other, soft daylight through tall windows, no people, cinematic establishing shot, {NEG}, {X}"),
    (f"{D}-lebanon-israel-talks", "broll_1.jpg", f"An empty diplomatic meeting room with two seating sections facing each other across a long table set with microphones and water glasses, neutral mediation setting, soft light, no people, {NEG}, {X}"),
    (f"{D}-lebanon-israel-talks", "broll_2.jpg", f"A quiet southern Lebanese village landscape at dawn with weathered stone buildings and olive trees on rolling green hills, calm somber documentary mood, wide shot, {NEG}, {X}"),
    (f"{D}-lebanon-israel-talks", "broll_3.jpg", f"A solemn candlelit memorial at dusk with many small glowing flames in soft focus, mournful respectful peaceful mood, no people, {NEG}, {X}"),
    # 4. MRNA CANCER VACCINE — clean biomedical, no readable text
    (f"{D}-mrna-cancer-vaccine", "hero.jpg", f"A clean modern biomedical research laboratory with a glowing abstract blue double-helix DNA strand of light floating above lab benches, cool blue and white scientific aesthetic, {NEG}, {X}"),
    (f"{D}-mrna-cancer-vaccine", "broll_1.jpg", f"A close macro shot of gloved scientist hands holding a small glass vaccine vial filled with glowing blue liquid in a sterile lab, soft bokeh, cool clinical light, no readable text, {NEG}, {X}"),
    (f"{D}-mrna-cancer-vaccine", "broll_2.jpg", f"An abstract glowing 3D visualization of mRNA strands and bright immune cells targeting a cancer cell, deep blue and teal scientific render, {NEG}, {X}"),
    (f"{D}-mrna-cancer-vaccine", "broll_3.jpg", f"A hopeful backlit silhouette of a person standing by a bright hospital window at sunrise, soft warm golden light, gentle optimistic documentary mood, face not visible, {NEG}, {X}"),
    # 5. GULF NON-OIL GROWTH — skylines + non-oil trade
    (f"{D}-gulf-nonoil-growth", "hero.jpg", f"The Riyadh Saudi Arabia financial district skyline at golden dusk with the distinctive Kingdom Centre tower and modern skyscrapers, warm desert haze, wide aerial establishing shot, {NEG}, {X}"),
    (f"{D}-gulf-nonoil-growth", "broll_1.jpg", f"A bustling modern Gulf logistics port in daytime with stacked colorful shipping containers and tall cranes under a clear blue sky, non-oil trade and commerce, wide aerial shot, {NEG}, {X}"),
    (f"{D}-gulf-nonoil-growth", "broll_2.jpg", f"The Dubai UAE skyline along the water at dusk with sleek illuminated glass towers, modern diversified economy, wide aerial establishing shot, {NEG}, {X}"),
    (f"{D}-gulf-nonoil-growth", "broll_3.jpg", f"A bright modern Gulf business district in daytime with people walking past contemporary glass office towers and green landscaping, prosperous non-oil economy mood, {NEG}, {X}"),
    # 6. EL NINO CLIMATE DRIVER — ocean + weather extremes
    (f"{D}-elnino-climate-driver", "hero.jpg", f"A dramatic satellite-style view of the Pacific Ocean with swirling warm ocean currents glowing in deep blues and warm tones, conceptual climate visualization, cinematic, no labels, {NEG}, {X}"),
    (f"{D}-elnino-climate-driver", "broll_1.jpg", f"Vast open ocean waves under a dramatic shifting sky with warm and cool light mixing, conceptual climate-change mood, wide cinematic seascape, {NEG}, {X}"),
    (f"{D}-elnino-climate-driver", "broll_2.jpg", f"A split-mood landscape showing parched cracked dry earth on one side and dark rain clouds with rainfall on the other, conceptual weather-extremes visualization, cinematic, {NEG}, {X}"),
    (f"{D}-elnino-climate-driver", "broll_3.jpg", f"Heavy storm clouds gathering over an arid Middle Eastern landscape with date palms, dramatic light breaking through, anticipation of seasonal rain, wide cinematic shot, {NEG}, {X}"),
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
