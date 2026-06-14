#!/usr/bin/env python3
"""Generate the AI scenes for the 2026-06-14 slate via Nano Banana Pro (9:16, 2K).
One still per beat, each prompt MATCHED to its target beat's text. Strong
no-text/no-UI/no-screenshot/no-logo negatives. Three slots are neutral fallbacks that may
be overwritten by real Commons portraits via fetch_faces_2026_06_14.py:
  iraq broll_1 (PM Ali al-Zaidi), hiv broll_1 (Pres. Cyril Ramaphosa), syria broll_3 (Pres. Ahmad al-Sharaa).
Bright/clean lighting to clear engine luminance floors; space scenes kept luminous, not pitch black."""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

D = "2026-06-14"
GUARD = ("absolutely no text, no captions, no Instagram or app UI, no phone screen interface, no watermark, "
         "no logos, no brand marks, no jersey numbers, no scoreboard numbers, one single uncropped photograph, "
         "single continuous wide shot, one frame only, not a collage, not a grid, not split panels, "
         "photorealistic editorial photograph")

JOBS = [
    # 1. IRAQ GOVERNMENT / CABINET (politics; broll_1 = PM Zaidi face if fetched; neutral fallback here)
    (f"{D}-iraq-government-cabinet", "hero.jpg", f"A grand formal Iraqi parliament chamber in Baghdad with tiered wooden seats and a raised speaker's podium under bright warm interior light, an empty solemn legislative hall, a sense of governance and statecraft, photorealistic editorial wide establishing shot, no people, no readable text, {GUARD}, {NEG}"),
    (f"{D}-iraq-government-cabinet", "broll_1.jpg", f"A formal Iraqi government setting, the Iraqi national flag with green white black and a red triangle on a polished flagpole inside a bright official government hall in Baghdad, marble columns, a sense of state authority, photorealistic editorial wide shot, no people, no readable text, {GUARD}, {NEG}"),
    (f"{D}-iraq-government-cabinet", "broll_2.jpg", f"A formal government cabinet meeting room with a long polished table and many empty leather chairs, two chairs conspicuously empty at the head, bright daylight through tall windows, a sense of unfinished government formation, photorealistic interior wide shot, no people, no readable text, {GUARD}, {NEG}"),
    (f"{D}-iraq-government-cabinet", "broll_3.jpg", f"A modern Baghdad cityscape at bright daytime with government ministry buildings and the Tigris river, a sense of a nation weighing its budget and finances, photorealistic editorial wide establishing shot, no people, no readable text, {GUARD}, {NEG}"),
    # 2. LENACAPAVIR HIV SHOT (health; broll_1 = Ramaphosa face if fetched; neutral fallback here)
    (f"{D}-lenacapavir-hiv-shot", "hero.jpg", f"A bright modern medical clinic close-up of a gloved hand holding a single clear glass vial and a syringe of clear liquid, soft clean daylight, a hopeful public-health-breakthrough atmosphere, shallow depth of field, no readable text, no logos, no faces, {GUARD}, {NEG}"),
    (f"{D}-lenacapavir-hiv-shot", "broll_1.jpg", f"A bright official podium at a public health launch event with a microphone and soft stage lighting in front of an empty modern auditorium, a national campaign atmosphere, photorealistic wide shot, no people, no readable text, no logos, {GUARD}, {NEG}"),
    (f"{D}-lenacapavir-hiv-shot", "broll_2.jpg", f"A bright welcoming community health clinic interior in South Africa with clean examination beds and medical supplies, sunlight through windows, a sense of accessible care, photorealistic documentary wide shot, no recognizable faces, no readable text, no logos, {GUARD}, {NEG}"),
    (f"{D}-lenacapavir-hiv-shot", "broll_3.jpg", f"A symbolic public-health scene, a large red awareness ribbon motif and gloved hands preparing a medical injection in a bright clinical setting, a sense of hope against an epidemic, photorealistic editorial shot, no recognizable faces, no readable text, no logos, {GUARD}, {NEG}"),
    # 3. SYRIA RECONSTRUCTION (geopolitics; broll_3 = al-Sharaa face if fetched; neutral fallback here)
    (f"{D}-syria-reconstruction", "hero.jpg", f"A wide view of the Damascus city skyline under bright clear daylight with tall construction cranes rising among rebuilt sand-colored buildings and minarets, a hopeful reconstruction atmosphere, cinematic editorial establishing shot, no recognizable faces, no readable text, {GUARD}, {NEG}"),
    (f"{D}-syria-reconstruction", "broll_1.jpg", f"A neutral formal European diplomacy scene, a bright modern conference hall with rows of empty chairs and a long table, soft daylight through tall glass, an international agreement atmosphere, no flags with readable text, no logos, no people, photorealistic wide interior shot, {GUARD}, {NEG}"),
    (f"{D}-syria-reconstruction", "broll_2.jpg", f"A large Syrian urban reconstruction site under bright daylight, tall tower cranes lifting concrete sections, stacks of rebar and building materials, partly rebuilt apartment blocks, a hopeful rebuilding atmosphere, photorealistic documentary wide shot, no recognizable faces, no readable text, {GUARD}, {NEG}"),
    (f"{D}-syria-reconstruction", "broll_3.jpg", f"A Syrian displacement camp of orderly white tents on dusty ground under bright hazy daylight, distant hills, a somber humanitarian atmosphere, photorealistic documentary wide shot, no recognizable faces, no readable text, {GUARD}, {NEG}"),
    # 4. JWST SLEEPING GIANT BLACK HOLE (science; keep luminous, not pitch black)
    (f"{D}-jwst-sleeping-giant", "hero.jpg", f"A breathtaking deep-space scene of a dormant supermassive black hole, a faint warm golden glow of a quiet accretion ring around a dark sphere set against a luminous field of distant stars and a soft nebula, awe-inspiring cosmic scale, photorealistic astronomical render, bright glowing highlights, no readable text, no logos, {GUARD}, {NEG}"),
    (f"{D}-jwst-sleeping-giant", "broll_1.jpg", f"The James Webb Space Telescope golden hexagonal mirror segments gleaming in space with a bright star field behind, brilliant gold reflections, a sense of precision astronomy, photorealistic space render, no readable text, no logos, {GUARD}, {NEG}"),
    (f"{D}-jwst-sleeping-giant", "broll_2.jpg", f"A luminous distant spiral galaxy with bright swirling star streams and glowing core against deep space, a sense of stars moving in orbit, vivid cosmic colors of gold and blue, photorealistic astronomical render, no readable text, no logos, {GUARD}, {NEG}"),
    (f"{D}-jwst-sleeping-giant", "broll_3.jpg", f"A quiet ancient elliptical galaxy glowing softly with a calm dormant supermassive black hole hinted at its luminous center, a peaceful early-universe deep-field scene with many faint distant galaxies, photorealistic astronomical render, gentle glow, no readable text, no logos, {GUARD}, {NEG}"),
    # 5. GCC UNIFIED VISA (gulf travel; bright, aspirational, no readable text)
    (f"{D}-gcc-unified-visa", "hero.jpg", f"A dazzling Gulf metropolis skyline of glass skyscrapers at golden hour with a clear sky and palm-lined waterfront, a prosperous seamless-travel atmosphere, photorealistic cinematic wide establishing shot, no readable text, no logos, no people, {GUARD}, {NEG}"),
    (f"{D}-gcc-unified-visa", "broll_1.jpg", f"A sleek bright modern Gulf international airport interior with soaring architecture and travelers walking with luggage in soft motion, a welcoming gateway atmosphere, photorealistic wide interior shot, no readable signage text, no logos, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-gcc-unified-visa", "broll_2.jpg", f"A traveler's hand holding a passport and a small rolling suitcase beside a bright airport departure window with planes outside, a sense of easy regional travel, shallow depth of field, photorealistic editorial shot, no readable text, no logos, no recognizable face, {GUARD}, {NEG}"),
    (f"{D}-gcc-unified-visa", "broll_3.jpg", f"A montage-feel panoramic of iconic Gulf city skylines together at golden hour, a tall slender tower, domed modern buildings and a curved skyline along the water, a single-region travel-zone feeling, photorealistic cinematic wide shot, no readable text, no logos, no people, {GUARD}, {NEG}"),
    # 6. NHL STANLEY CUP FINAL (sport; festive arena, no logos/numbers/faces)
    (f"{D}-nhl-stanley-cup-final", "hero.jpg", f"A packed indoor ice hockey arena during a championship final game at night, brilliant spotlights reflecting on the glossy white ice rink, a euphoric sea of fans in the stands, an electric big-game atmosphere, photorealistic cinematic wide establishing shot, no readable text, no logos, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-nhl-stanley-cup-final", "broll_1.jpg", f"A dramatic high overhead view of a glossy white ice hockey rink inside a sold-out arena under bright spotlights, distant skaters in plain unmarked uniforms, a finals-night atmosphere, photorealistic wide shot, no readable text, no scoreboard numbers, no logos, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-nhl-stanley-cup-final", "broll_2.jpg", f"A dynamic action shot of an ice hockey player in a plain unmarked uniform skating fast with a stick and spraying ice under bright arena spotlights, motion energy, photorealistic sports shot, no jersey numbers, no logos, no readable text, no recognizable face, {GUARD}, {NEG}"),
    (f"{D}-nhl-stanley-cup-final", "broll_3.jpg", f"A gleaming silver championship trophy standing on a draped table at center ice under a single dramatic spotlight in a darkened arena, golden confetti beginning to fall, a sense of imminent triumph, photorealistic cinematic shot, no readable text, no logos, no engraving text, {GUARD}, {NEG}"),
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
