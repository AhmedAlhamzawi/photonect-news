#!/usr/bin/env python3
"""Generate the 22 non-face AI scenes for the 2026-06-10 slate via Nano Banana Pro (9:16, 2K).
Faces (Randy Bresnik -> artemis broll_1, Luca Parmitano -> artemis broll_3) are real photos fetched separately.
Every scene prompt MATCHES its target beat's text. Strong no-text/no-UI/no-screenshot/no-logo negatives
(KIE screenshot + triptych + brand-logo guard, critical for the WWDC slug). Bright/clean lighting to
clear engine luminance floors (deep-space artemis hero is intentionally dark and may warn)."""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

D = "2026-06-10"
GUARD = ("absolutely no text, no captions, no Instagram or app UI, no phone screen interface, no watermark, "
         "no logos, no brand marks, one single uncropped photograph, single continuous wide shot, one frame only, "
         "not a collage, not a grid, not split panels, photorealistic editorial photograph")

JOBS = [
    # 1. ARTEMIS III (hero/broll_2 generated; broll_1 = real Bresnik, broll_3 = real Parmitano)
    (f"{D}-artemis-3-moon-crew", "hero.jpg", f"A NASA Orion crew spacecraft with large deployed solar arrays orbiting high above the grey cratered surface of the Moon, a brilliant distant Sun flare, deep black starry space, the tiny blue Earth far in the distance, photorealistic cinematic space scene, no people, {GUARD}, {NEG}"),
    (f"{D}-artemis-3-moon-crew", "broll_2.jpg", f"Two sleek robotic lunar landing vehicles and a crew capsule performing a careful docking maneuver in bright lunar orbit above the Moon's cratered surface, sunlit modern spacecraft against deep black space, photorealistic cinematic wide shot, no people, {GUARD}, {NEG}"),
    # 2. BAGHDAD POWER CRISIS (all 4 generated, no faces)
    (f"{D}-baghdad-power-crisis", "hero.jpg", f"A wide cinematic skyline of Baghdad Iraq at dusk under a hazy hot orange sky, dense residential buildings mostly dark with only scattered window lights, rooftop water tanks and tangled overhead power cables, oppressive summer heat haze, photorealistic editorial establishing shot, no people, {GUARD}, {NEG}"),
    (f"{D}-baghdad-power-crisis", "broll_1.jpg", f"A dim Middle Eastern residential street at night during a power blackout, small private diesel generators humming on the sidewalk with bundles of cables strung between buildings, a few warm pools of light from shops, Baghdad documentary night scene, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-baghdad-power-crisis", "broll_2.jpg", f"A tight close-up of a dense cluster of old residential electricity meters and tangled wiring mounted on a concrete wall in an Arab city, a blurred electrical substation behind, harsh bright daylight, no people, photorealistic documentary shot, {GUARD}, {NEG}"),
    (f"{D}-baghdad-power-crisis", "broll_3.jpg", f"Tall high-voltage electricity transmission towers and power lines stretching across a flat arid Iraqi landscape under a blazing hazy sky at golden hour, sense of a strained national power grid, wide cinematic establishing shot, no people, {GUARD}, {NEG}"),
    # 3. LEBANON-ISRAEL CEASEFIRE (all 4 generated, neutral, no faces)
    (f"{D}-lebanon-israel-ceasefire", "hero.jpg", f"A convoy of olive-green Lebanese Army armored vehicles and soldiers deploying along a road through rugged southern Lebanon hill country under hazy daylight, a tense peacekeeping deployment, wide cinematic documentary shot, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-lebanon-israel-ceasefire", "broll_1.jpg", f"Three national flags standing upright on a long polished wooden negotiation table in a formal diplomatic meeting room, the flag of the United States, the flag of Lebanon and the flag of Israel, empty leather chairs, neutral cool window light, no people, wide cinematic shot, {GUARD}, {NEG}"),
    (f"{D}-lebanon-israel-ceasefire", "broll_2.jpg", f"Lebanese Army soldiers in olive-green uniforms manning a checkpoint at the entrance of a quiet stone village in south Lebanon, an armored personnel carrier parked nearby, hazy warm daylight, documentary wide shot, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-lebanon-israel-ceasefire", "broll_3.jpg", f"A quiet partly damaged hillside village in southern Lebanon at dusk, weathered stone buildings, rugged terrain and the distant silhouette of a medieval hilltop fortress, somber post-conflict atmosphere, wide cinematic shot, no people, {GUARD}, {NEG}"),
    # 4. OBESITY DRUG RETATRUTIDE (all 4 generated, no faces)
    (f"{D}-obesity-drug-retatrutide", "hero.jpg", f"A bright clean modern medical concept scene, a sleek digital bathroom weighing scale and a soft tape measure on a white clinical surface beside a glowing abstract human body silhouette on a screen, hopeful weight-loss research mood, soft daylight, shallow depth of field, no people, {GUARD}, {NEG}"),
    (f"{D}-obesity-drug-retatrutide", "broll_1.jpg", f"A close-up of a modern injectable medicine pen lying beside a digital weighing scale on a clean bright clinic counter, pharmaceutical weight-loss treatment concept, soft studio lighting, shallow depth of field, no people, {GUARD}, {NEG}"),
    (f"{D}-obesity-drug-retatrutide", "broll_2.jpg", f"A bright clinical illustration of a healthy human heart and metabolic system glowing on a large medical display screen in a modern research lab, clean hopeful atmosphere, soft daylight, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-obesity-drug-retatrutide", "broll_3.jpg", f"An extreme close-up of a single modern auto-injector pen beside a few white medication capsules on a reflective clean clinical surface, soft bright studio light, shallow depth of field, no people, {GUARD}, {NEG}"),
    # 5. SIRI AI WWDC (all 4 generated, NO logos/UI/text, no faces)
    (f"{D}-siri-ai-wwdc", "hero.jpg", f"A sleek modern circular glass technology campus building at dusk with warm interior lighting, a softly glowing abstract blue-and-white sphere of light floating above a clean minimalist stage, futuristic consumer-technology keynote atmosphere, no screens with interfaces, no brand marks, photorealistic cinematic wide shot, no people, {GUARD}, {NEG}"),
    (f"{D}-siri-ai-wwdc", "broll_1.jpg", f"A close-up of a generic frameless modern black smartphone lying on a clean reflective desk, a soft glowing colorful orb of light hovering just above its blank dark screen representing a voice assistant, no app interface, no icons, no logos, soft studio lighting, {GUARD}, {NEG}"),
    (f"{D}-siri-ai-wwdc", "broll_2.jpg", f"An abstract visualization of artificial intelligence, a flowing three-dimensional network of glowing blue and white nodes with a luminous sound waveform on a dark gradient background, sleek high-tech render, no text, no logos, {GUARD}, {NEG}"),
    (f"{D}-siri-ai-wwdc", "broll_3.jpg", f"A neat lineup of generic modern consumer devices on a clean light surface, a smartphone, a tablet, a thin laptop and a smartwatch, each blank screen emitting a soft uniform glow, minimalist product photography lighting, no logos, no icons, no interface, {GUARD}, {NEG}"),
    # 6. TONY AWARDS 2026 (all 4 generated, no readable text, no faces)
    (f"{D}-tony-awards-2026", "hero.jpg", f"A glamorous Broadway theatre district at night, warm glowing classic marquee bulbs and golden signage light with no readable letters, elegant evening crowd softly blurred, festive awards-night atmosphere, warm cinematic wide establishing shot, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-tony-awards-2026", "broll_1.jpg", f"The ornate facade of a historic Broadway theatre at night glowing with warm vintage marquee bulbs, a red carpet entrance, elegant evening atmosphere, no readable text on the signage, cinematic wide shot, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-tony-awards-2026", "broll_2.jpg", f"A grand empty theatre stage with rich red velvet curtains and a single dramatic spotlight beam, ornate gilded auditorium seats in soft focus, theatrical awards-night mood, cinematic wide shot, no people, {GUARD}, {NEG}"),
    (f"{D}-tony-awards-2026", "broll_3.jpg", f"A close-up of an elegant polished golden award trophy on a reflective stage podium under a warm spotlight, a blurred glamorous theatre interior behind, prestige awards-ceremony atmosphere, no readable text, shallow depth of field, {GUARD}, {NEG}"),
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
        if pending:
            print(f"  ... {len(pending)} pending", flush=True)
    ok = sum(1 for j in jobs if j.get("ok"))
    print(f"\n{ok}/{len(jobs)} scenes generated", flush=True)
    return 0 if ok == len(jobs) else 1


if __name__ == "__main__":
    sys.exit(main())
