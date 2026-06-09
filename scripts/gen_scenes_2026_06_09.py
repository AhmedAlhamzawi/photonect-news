#!/usr/bin/env python3
"""Generate the 22 non-face AI scenes for the 2026-06-09 slate via Nano Banana Pro (9:16, 2K).
Faces (Ayman Hussein -> iraq broll_2, Abbas Araghchi -> iran hero) are real photos fetched separately.
Every scene prompt MATCHES its target beat's text. Strong no-text/no-UI/single-frame negatives
(KIE screenshot + triptych guard). Bright/clean lighting to clear engine luminance floors."""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

D = "2026-06-09"
GUARD = ("absolutely no text, no captions, no Instagram or app UI, no phone screen, no watermark, "
         "no logos, one single uncropped photograph, single continuous wide shot, one frame only, "
         "not a collage, not a grid, not split panels, photorealistic editorial photograph")

JOBS = [
    # 1. IRAQ WORLD CUP (hero/broll_1/broll_3 generated; broll_2 = real Ayman Hussein)
    (f"{D}-iraq-worldcup-2026", "hero.jpg", f"A jubilant crowd of Iraqi football supporters celebrating a World Cup qualification inside a packed stadium at night, a huge flag of Iraq (red white black horizontal bands with green Arabic script in the white band) waving above the crowd, green floodlit pitch below, bursts of fireworks, ecstatic emotional national celebration, wide cinematic establishing shot, no recognizable individual faces, {GUARD}, {NEG}"),
    (f"{D}-iraq-worldcup-2026", "broll_1.jpg", f"A sea of Iraqi football fans in green national-team jerseys celebrating in a city square at night, waving many flags of Iraq, joyous emotional crowd, warm city lights and confetti, energetic documentary wide shot, no recognizable individual faces, {GUARD}, {NEG}"),
    (f"{D}-iraq-worldcup-2026", "broll_3.jpg", f"A grand modern World Cup football stadium at night, packed tiers of fans under bright white floodlights, pristine green pitch, electric pre-match atmosphere, wide cinematic establishing aerial shot, no recognizable faces, {GUARD}, {NEG}"),
    # 2. IRAN NUCLEAR (broll_1/2/3 generated; hero = real Araghchi)
    (f"{D}-iran-nuclear-deadlock", "broll_1.jpg", f"A formal diplomatic negotiation room, a long polished wooden table with the flag of the United States and the flag of Iran standing upright facing each other, empty leather chairs, neutral mediator setting, soft cool window light, no people, wide cinematic shot, {GUARD}, {NEG}"),
    (f"{D}-iran-nuclear-deadlock", "broll_2.jpg", f"Interior of a uranium enrichment facility, a long clean industrial hall lined with rows of tall metallic gas centrifuge cascades, cool technical lighting, sense of nuclear capability, no people, wide cinematic shot, {GUARD}, {NEG}"),
    (f"{D}-iran-nuclear-deadlock", "broll_3.jpg", f"Aerial view of a massive crude oil supertanker crossing the narrow Strait of Hormuz at dawn, calm steel-blue Persian Gulf water, faint hazy mountainous coastline, strategic maritime chokepoint, cinematic wide shot, {GUARD}, {NEG}"),
    # 3. KIDNEY-HEART DRUG (all 4 generated, no faces)
    (f"{D}-kidney-heart-drug", "hero.jpg", f"A clean bright modern medical research setting, a glowing 3D anatomical illustration of healthy human kidneys and a heart on a large screen beside polished lab equipment, hopeful clinical atmosphere, soft daylight, shallow depth of field, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-kidney-heart-drug", "broll_1.jpg", f"A clean tightly-framed vertical close-up of a gloved hand holding a single small labelled glass medical vial up to soft daylight, blurred modern laboratory instruments behind, shallow depth of field, clinical trial research mood, upright vertical portrait orientation, level horizon, not rotated, not sideways, no recognizable face, {GUARD}, {NEG}"),
    (f"{D}-kidney-heart-drug", "broll_2.jpg", f"Extreme close-up of a single medication blister pack and a few round white tablets resting on a clean reflective clinic surface beside a stethoscope, soft bright studio lighting, shallow depth of field, no people, {GUARD}, {NEG}"),
    (f"{D}-kidney-heart-drug", "broll_3.jpg", f"A sleek modern pharmaceutical corporate boardroom with a wide bright window, an abstract clinical-data line chart glowing on a large wall screen, professional regulatory medical mood, no recognizable faces, wide cinematic shot, {GUARD}, {NEG}"),
    # 4. QATAR-EGYPT MEGAPROJECT (all 4 generated, no faces)
    (f"{D}-qatar-egypt-megaproject", "hero.jpg", f"Aerial view of a vast luxury Mediterranean coastal resort city under bright daylight, turquoise sea meeting a long golden sandy beach, modern white hotels, marinas and palm-lined promenades along the shoreline, large-scale tourism development, wide cinematic establishing shot, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-qatar-egypt-megaproject", "broll_1.jpg", f"Aerial wide shot of an Egyptian North Coast Mediterranean shoreline, turquoise water and pale sand, the early large-scale framework of a new coastal city development with cranes and laid-out roads, bright clear daylight, {GUARD}, {NEG}"),
    (f"{D}-qatar-egypt-megaproject", "broll_2.jpg", f"A sweeping modern beachfront resort with rows of white luxury hotel buildings, palm-lined promenades and a long crowded golden beach beside calm blue Mediterranean sea, vibrant summer tourism scene, wide aerial shot, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-qatar-egypt-megaproject", "broll_3.jpg", f"Doha Qatar skyline at golden dusk, the distinctive modern towers of the West Bay financial district reflecting on the calm bay, sense of Gulf sovereign capital and investment, wide aerial establishing shot, {GUARD}, {NEG}"),
    # 5. TIANWEN-2 ASTEROID (all 4 generated, no faces)
    (f"{D}-tianwen2-asteroid", "hero.jpg", f"A sleek robotic space probe with large golden solar panels approaching a small dark-grey rocky near-Earth asteroid in deep black space, a distant bright Sun flare, the tiny blue-and-white Earth far in the background, photorealistic cinematic space scene, {GUARD}, {NEG}"),
    (f"{D}-tianwen2-asteroid", "broll_1.jpg", f"A spacecraft slowly orbiting a small irregular rocky asteroid against the black starfield of deep space, raking sunlight across the cratered grey surface, photorealistic, wide cinematic shot, {GUARD}, {NEG}"),
    (f"{D}-tianwen2-asteroid", "broll_2.jpg", f"Close-up of a robotic spacecraft sampling arm touching down on the rocky regolith surface of a small asteroid, fine dust particles drifting in microgravity, harsh sunlit grey rock, deep space behind, photorealistic space scene, {GUARD}, {NEG}"),
    (f"{D}-tianwen2-asteroid", "broll_3.jpg", f"A small rocky asteroid in the foreground with the distant blue crescent of Earth and the pale Moon together in deep black space, soft sunlight, scientific cosmic atmosphere, photorealistic wide shot, {GUARD}, {NEG}"),
    # 6. ARAB REGION HEAT (all 4 generated, no faces)
    (f"{D}-arab-region-heat", "hero.jpg", f"A Middle Eastern city skyline shimmering under a brutal blazing midday sun and heavy heat haze, pale washed-out sky, oppressive summer heatwave atmosphere, wide cinematic establishing shot, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-arab-region-heat", "broll_1.jpg", f"A vast expanse of sun-scorched deeply cracked dry desert earth under a fierce white sun and shimmering heat distortion, a distant Arab city skyline on the hazy horizon, brutal drought, wide cinematic shot, no people, {GUARD}, {NEG}"),
    (f"{D}-arab-region-heat", "broll_2.jpg", f"A hazy Middle Eastern urban street under extreme heat with visibly shimmering distorted air, a lone figure seen from behind shielding from the harsh bright sun, oppressive heatwave, documentary wide shot, no recognizable face, {GUARD}, {NEG}"),
    (f"{D}-arab-region-heat", "broll_3.jpg", f"A blazing white sun over rippling arid sand dunes with a distant modern Gulf city skyline in heavy heat haze, sense of extreme dangerous heat, wide cinematic establishing shot, no people, {GUARD}, {NEG}"),
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
            print(f"    ... {len(pending)} generating", flush=True)
    ok = sum(1 for j in jobs if j["ok"])
    print(f"\n== Done {ok}/{len(sel)} ==", flush=True)
    fails = [f"{j['slug']}/{j['file']}" for j in jobs if not j["ok"]]
    if fails:
        for f in fails:
            print(f"  FAIL: {f}", file=sys.stderr)
    return 0 if ok == len(sel) else 1


if __name__ == "__main__":
    sys.exit(main())
