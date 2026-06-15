#!/usr/bin/env python3
"""Generate the AI scenes for the 2026-06-15 slate via Nano Banana Pro (9:16, 2K).
One still per beat, each prompt MATCHED to its target beat's text. Strong
no-text/no-UI/no-screenshot/no-logo negatives. NO real-face slots this slate
(no single-person-centric story; the Iran deal is treated neutrally with flags/strait).
Bright/clean lighting to clear engine luminance floors; space scenes kept luminous, not pitch black."""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

D = "2026-06-15"
GUARD = ("absolutely no text, no captions, no Instagram or app UI, no phone screen interface, no watermark, "
         "no logos, no brand marks, no jersey numbers, no scoreboard numbers, one single uncropped photograph, "
         "single continuous wide shot, one frame only, not a collage, not a grid, not split panels, "
         "photorealistic editorial photograph")

JOBS = [
    # 1. US-IRAN WAR-ENDING DEAL (geopolitics; strictly neutral: flags, table, strait, signing hall)
    (f"{D}-iran-us-war-deal", "hero.jpg", f"A solemn neutral diplomacy scene, two unmarked national flagpoles flanking a long polished negotiation table in a bright modern conference hall with tall windows, a sense of a historic agreement to end a war, photorealistic editorial wide establishing shot, no people, no readable text, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-iran-us-war-deal", "broll_1.jpg", f"A bright formal international signing room in Switzerland with a long table, neat chairs, a carafe of water and folders, soft daylight through large windows and distant alpine mountains outside, an atmosphere of an imminent peace agreement, photorealistic wide interior shot, no people, no readable text, no logos, {GUARD}, {NEG}"),
    (f"{D}-iran-us-war-deal", "broll_2.jpg", f"A wide daytime aerial view of the Strait of Hormuz, a narrow blue sea channel between rugged coastlines with a large oil tanker sailing through calm water under clear sky, a sense of reopened shipping lanes, photorealistic editorial aerial shot, no readable text, no logos, {GUARD}, {NEG}"),
    (f"{D}-iran-us-war-deal", "broll_3.jpg", f"A low-angle upright vertical view of a row of plain unmarked national flags on tall flagpoles fluttering against a bright clear blue sky outside a grand modern diplomatic building, an atmosphere of an international welcome to a major agreement, photorealistic editorial portrait-orientation shot, no people, no readable text, no logos, no recognizable flag emblems, {GUARD}, {NEG}"),
    # 2. LE MANS 24h (sport; race cars, track, podium, no logos/numbers/faces)
    (f"{D}-le-mans-toyota-win", "hero.jpg", f"A sleek unmarked white-and-red endurance prototype race car blasting down a sunlit racetrack straight with strong motion blur, grandstands behind, a triumphant finish-line atmosphere, photorealistic dynamic motorsport shot, no jersey numbers, no sponsor logos, no readable text, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-le-mans-toyota-win", "broll_1.jpg", f"Two unmarked endurance prototype race cars side by side cornering closely on a daylight circuit, intense wheel-to-wheel battle, a razor-thin margin atmosphere, photorealistic motorsport action shot, no numbers, no logos, no readable text, no faces, {GUARD}, {NEG}"),
    (f"{D}-le-mans-toyota-win", "broll_2.jpg", f"A long curving racetrack at golden hour with a single plain prototype race car in motion and empty pit garages in the background, a sense of a historic 24-hour endurance victory, photorealistic wide motorsport shot, no logos, no numbers, no readable text, no faces, {GUARD}, {NEG}"),
    (f"{D}-le-mans-toyota-win", "broll_3.jpg", f"A gleaming silver motorsport championship trophy on a draped podium under bright daylight with confetti beginning to fall and an empty grandstand behind, a celebratory victory atmosphere, photorealistic shot, no readable text, no engraving text, no logos, no faces, {GUARD}, {NEG}"),
    # 3. IRAQ WATER CRISIS (iraq; drought, cracked riverbed, dried marshes, reservoir, heat)
    (f"{D}-iraq-water-crisis", "hero.jpg", f"A vast cracked dry riverbed under a harsh bright Iraqi summer sun, parched fissured earth stretching to the horizon with a thin trickle of water, a few date palms wilting, an oppressive heat-haze atmosphere, photorealistic editorial wide establishing shot, no people, no readable text, {GUARD}, {NEG}"),
    (f"{D}-iraq-water-crisis", "broll_1.jpg", f"A drained reservoir behind a concrete dam in northern Iraq showing dramatic white bathtub-ring water marks far above the shrunken water line, bright daylight, a sense of record-low water storage, photorealistic editorial wide shot, no people, no readable text, no logos, {GUARD}, {NEG}"),
    (f"{D}-iraq-water-crisis", "broll_2.jpg", f"The drying southern marshes of Iraq, cracked salt-crusted mudflats where wetlands once stood, a stranded narrow wooden canoe on dry ground and dead reeds under hazy bright light, a desolate environmental atmosphere, photorealistic documentary wide shot, no people, no readable text, {GUARD}, {NEG}"),
    (f"{D}-iraq-water-crisis", "broll_3.jpg", f"A modern water desalination and treatment plant with rows of pipes and tanks under bright daylight near a coastline in southern Iraq, a sense of an engineered response to water scarcity, photorealistic industrial wide shot, no people, no readable text, no logos, {GUARD}, {NEG}"),
    # 4. KECK PLANET SPINS (science; observatory + giant planets, keep luminous)
    (f"{D}-keck-planet-spins", "hero.jpg", f"A breathtaking luminous deep-space scene of several giant gas planets and a glowing brown dwarf spinning around distant bright stars, vivid swirling cloud bands of gold, amber and blue, awe-inspiring cosmic scale with bright glowing highlights, photorealistic astronomical render, no readable text, no logos, {GUARD}, {NEG}"),
    (f"{D}-keck-planet-spins", "broll_1.jpg", f"Twin large white domed astronomical observatories on a high volcanic mountain summit in Hawaii at golden dusk under a brilliant starry sky, a sense of precision astronomy, photorealistic editorial wide shot, no readable text, no logos, {GUARD}, {NEG}"),
    (f"{D}-keck-planet-spins", "broll_2.jpg", f"A close luminous view of a fast-spinning banded giant gas planet with vivid swirling storm clouds and a soft motion blur suggesting rapid rotation, set against a bright star field, photorealistic astronomical render, vivid glow, no readable text, no logos, {GUARD}, {NEG}"),
    (f"{D}-keck-planet-spins", "broll_3.jpg", f"The interior of a large astronomical observatory dome with a giant telescope mirror assembly gleaming under soft light and the dome slit open to a luminous night sky, a sense of giant precision optics, photorealistic wide interior shot, no readable text, no logos, no faces, {GUARD}, {NEG}"),
    # 5. MARKETS / HORMUZ REOPEN (economy; trading floor, oil, tanker, bright clean)
    (f"{D}-markets-hormuz-reopen", "hero.jpg", f"A bright modern financial trading floor with large glowing abstract market display walls showing rising green and falling red charts in soft focus, dynamic energetic atmosphere, photorealistic editorial wide shot, no readable numbers, no readable text, no logos, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-markets-hormuz-reopen", "broll_1.jpg", f"A clean abstract financial visualization of a steeply falling oil-price line over a soft background of oil barrels and a refinery silhouette at bright dawn, a sense of plunging crude prices, photorealistic editorial render, no readable numbers, no readable text, no logos, {GUARD}, {NEG}"),
    (f"{D}-markets-hormuz-reopen", "broll_2.jpg", f"A bright abstract stock-market scene of soaring green upward arrows and rising candlestick bars over a luminous Asian city skyline at dawn, an optimistic market-rally atmosphere, photorealistic editorial render, no readable numbers, no readable text, no logos, {GUARD}, {NEG}"),
    (f"{D}-markets-hormuz-reopen", "broll_3.jpg", f"A large oil tanker sailing through the narrow blue Strait of Hormuz between rugged coastlines under bright clear daylight, a sense of reopened global oil shipping lanes, photorealistic editorial aerial shot, no readable text, no logos, {GUARD}, {NEG}"),
    # 6. CYTISINICLINE / QUIT SMOKING (health; clinic, pills, broken cigarette, no faces)
    (f"{D}-smoking-drug-cytisinicline", "hero.jpg", f"A bright clean medical close-up of a small white pill blister pack and a single snapped cigarette on a light clinical surface, soft daylight, a hopeful quit-smoking-breakthrough atmosphere, shallow depth of field, no readable text, no logos, no faces, {GUARD}, {NEG}"),
    (f"{D}-smoking-drug-cytisinicline", "broll_1.jpg", f"A bright modern pharmacy or clinic interior with neat shelves and a clean counter under soft daylight, a sense of an approved new medication, photorealistic wide interior shot, no readable text, no logos, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-smoking-drug-cytisinicline", "broll_2.jpg", f"A bright pharmaceutical research laboratory with clean glassware, a green plant leaf motif beside small white tablets symbolizing a plant-based compound, soft clinical light, photorealistic editorial shot, no readable text, no logos, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-smoking-drug-cytisinicline", "broll_3.jpg", f"A symbolic health scene of a hand crushing a cigarette beside a disposable vaping device on a bright clean surface, a sense of breaking nicotine addiction, photorealistic editorial shot, shallow depth of field, no readable text, no logos, no recognizable faces, {GUARD}, {NEG}"),
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
