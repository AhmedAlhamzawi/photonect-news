#!/usr/bin/env python3
"""Generate the AI scenes for the 2026-06-18 slate via Nano Banana Pro (9:16, 2K).
One still per beat, each prompt MATCHED to its target beat's text. Strong
no-text/no-UI/no-screenshot/no-logo negatives. No real-face slot this slate —
no story is centrally about a single named individual, so all 24 are scenes."""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

D = "2026-06-18"
GUARD = ("absolutely no text, no captions, no Instagram or app UI, no phone screen interface, no watermark, "
         "no logos, no brand marks, no registration codes, no readable signage, no labels, no numbers, "
         "one single uncropped photograph, single continuous wide shot, one frame only, not a collage, "
         "not a grid, not split panels, photorealistic editorial photograph")

JOBS = [
    # 1. MOSUL CULTURAL MUSEUM (iraq_domestic, C) — reopening, restoration, heritage revival
    (f"{D}-iraq-mosul-museum", "hero.jpg", f"A grand restored museum gallery interior with tall pale stone walls and soft warm spotlighting, ancient Mesopotamian Assyrian stone reliefs and statues on display, a sense of cultural revival and a museum reopening after long closure, photorealistic editorial wide shot, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-iraq-mosul-museum", "broll_1.jpg", f"A weathered honey-colored stone museum facade in an old Middle Eastern city partly covered in restoration scaffolding under warm golden afternoon light, half-repaired walls, a sense of a long closure finally ending, photorealistic editorial wide shot, no people, {GUARD}, {NEG}"),
    (f"{D}-iraq-mosul-museum", "broll_2.jpg", f"Close-up of gloved conservator hands carefully restoring a damaged ancient carved stone relief with fine tools under soft warm museum lighting, focused craftsmanship, shallow depth of field, photorealistic documentary shot, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-iraq-mosul-museum", "broll_3.jpg", f"A majestic ancient Assyrian winged-bull lamassu stone sculpture standing dignified in a softly lit museum hall, monumental scale, a sense of heritage restored and standing tall again, photorealistic editorial shot, no people, {GUARD}, {NEG}"),
    # 2. IRAN-US DEAL SIGNING (mena_geopolitics, A) — Swiss diplomacy, peace talks, recovery
    (f"{D}-iran-us-deal-signing", "hero.jpg", f"An elegant formal diplomatic conference hall beside a calm lake with snow-capped Alps through tall windows, a long polished negotiation table and plain unmarked flags on poles, soft daylight, a solemn high-stakes atmosphere of peace talks, photorealistic editorial wide shot, no people, no emblems, {GUARD}, {NEG}"),
    (f"{D}-iran-us-deal-signing", "broll_1.jpg", f"A stately Swiss diplomatic room with a single ornate desk holding a closed leather folder and a pen, tall windows showing a serene alpine lake, a historic solemn calm before a signing, photorealistic editorial shot, no people, no readable documents, no emblems, {GUARD}, {NEG}"),
    (f"{D}-iran-us-deal-signing", "broll_2.jpg", f"A hopeful golden sunrise over a modern Middle Eastern city skyline with construction cranes and rebuilding, warm optimistic light symbolizing economic recovery and reopening, photorealistic editorial wide shot, no people, no readable signage, {GUARD}, {NEG}"),
    (f"{D}-iran-us-deal-signing", "broll_3.jpg", f"Two facing rows of empty chairs across a long negotiation table with plain unmarked flags in a formal hall, soft window light, a tense uncertain calm awaiting talks, photorealistic editorial wide shot, no people, no emblems, {GUARD}, {NEG}"),
    # 3. MAMMAL REGENERATION (wildcard/science, B) — abstract bio-regeneration, lab, genetic switch
    (f"{D}-mammal-regeneration", "hero.jpg", f"A glowing abstract scientific visualization of biological tissue regenerating, luminous cells and DNA strands knitting together, deep blue and teal tones, a sense of healing and renewal, photorealistic 3D render, {GUARD}, {NEG}"),
    (f"{D}-mammal-regeneration", "broll_1.jpg", f"A clean modern molecular-biology laboratory with a glowing blue DNA double-helix model and gloved hands near a microscope, cool scientific lighting, a sense of discovery, photorealistic editorial shot, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-mammal-regeneration", "broll_2.jpg", f"An abstract microscopic visualization of a glowing genetic switch toggling on among luminous gene strands and floating oxygen molecules, teal and gold tones, a clean elegant scientific render, {GUARD}, {NEG}"),
    (f"{D}-mammal-regeneration", "broll_3.jpg", f"A clean abstract scientific render of new tissue forming and filling a gap, glowing fresh cells multiplying, soft blue-green tones, a hopeful regenerative-medicine atmosphere, photorealistic 3D render, {GUARD}, {NEG}"),
    # 4. SAUDI SEHA VIRTUAL HOSPITAL (gulf_regional, A) — telemedicine command center, network, hospital
    (f"{D}-saudi-seha-hospital", "hero.jpg", f"A sleek futuristic medical command center with a vast wall of glowing blue screens showing abstract health graphics and a softly glowing connectivity map, modern clinician workstations, a sense of the world's largest virtual hospital, photorealistic editorial wide shot, no readable text, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-saudi-seha-hospital", "broll_1.jpg", f"A luminous abstract network of glowing connection lines spreading across a dark map-like surface linking many bright nodes, cool blue and white tones, a sense of a vast unified medical network across a country, photorealistic render, no readable text, {GUARD}, {NEG}"),
    (f"{D}-saudi-seha-hospital", "broll_2.jpg", f"Seen over the shoulder of a clinician in a modern telemedicine studio facing a large glowing monitor during a virtual consultation, clean clinical setting, soft blue light, professional, photorealistic editorial shot, no readable text on screen, face not visible, {GUARD}, {NEG}"),
    (f"{D}-saudi-seha-hospital", "broll_3.jpg", f"A modern gleaming hospital building in a Gulf city at golden hour with sleek glass architecture and palm trees, a thriving advanced-healthcare atmosphere, photorealistic editorial wide shot, no readable signage, no logos, {GUARD}, {NEG}"),
    # 5. JWST EXOPLANET HD 80606 b (wildcard/space, B) — roasted gas giant, elliptical orbit, spectrum
    (f"{D}-jwst-exoplanet-roasted", "hero.jpg", f"A dramatic deep-space scene of a large banded gas-giant exoplanet glowing red-hot on one side as it swings close to a brilliant sun-like star, swirling stormy atmosphere, cinematic photorealistic astronomical render, {GUARD}, {NEG}"),
    (f"{D}-jwst-exoplanet-roasted", "broll_1.jpg", f"A massive banded gas-giant planet in deep space with a highly elongated glowing elliptical orbital arc sweeping toward a bright distant star, cinematic astronomical render, no labels, {GUARD}, {NEG}"),
    (f"{D}-jwst-exoplanet-roasted", "broll_2.jpg", f"A gas-giant planet half-scorched and glowing orange from intense stellar heat with shimmering atmospheric distortion, a blazing sun-like star nearby, dramatic deep-space render, {GUARD}, {NEG}"),
    (f"{D}-jwst-exoplanet-roasted", "broll_3.jpg", f"An abstract elegant visualization of starlight passing through a planet's glowing thin atmosphere against a deep-space backdrop, faint soft colored light bands, a scientific spectroscopy mood, photorealistic render, no text, no numbers, {GUARD}, {NEG}"),
    # 6. SUPERCONDUCTOR LEAP (tech_ai/physics, C) — levitating film, nanostructure, quantum chip
    (f"{D}-superconductor-leap", "hero.jpg", f"A sleek abstract physics render of a glowing ultrathin blue crystalline film hovering above a finely sculpted nanostructured surface with luminous magnetic field lines curving around it, dark elegant background, advanced-science atmosphere, photorealistic 3D render, {GUARD}, {NEG}"),
    (f"{D}-superconductor-leap", "broll_1.jpg", f"A macro abstract render of a nanostructured surface covered in tiny parallel ridges and valleys beneath a glowing ultrathin superconducting layer, blue and gold luminescence, dark background, scientific, {GUARD}, {NEG}"),
    (f"{D}-superconductor-leap", "broll_2.jpg", f"An extreme abstract macro render of atomic layers stacked in a glowing crystalline lattice, an impossibly thin luminous film catching cool blue light, dark elegant background, photorealistic 3D render, {GUARD}, {NEG}"),
    (f"{D}-superconductor-leap", "broll_3.jpg", f"A sleek abstract render of a glowing quantum computing chip with luminous circuit pathways and cool blue energy flowing efficiently across it, dark elegant futuristic-technology background, photorealistic 3D render, no readable text, no logos, {GUARD}, {NEG}"),
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
    deadline = time.time() + 20 * 60
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
