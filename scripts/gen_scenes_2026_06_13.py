#!/usr/bin/env python3
"""Generate the AI scenes for the 2026-06-13 slate via Nano Banana Pro (9:16, 2K).
One still per beat, each prompt MATCHED to its target beat's text. Strong
no-text/no-UI/no-screenshot/no-logo negatives. Three slots are neutral fallbacks that may
be overwritten by real Commons portraits via fetch_faces_2026_06_13.py:
  iraq broll_1 (PM Zaidi), stanford broll_3 (Helen Blau), nba broll_3 (Jalen Brunson).
Bright/clean lighting to clear engine luminance floors (gaza scenes daylight, not dark)."""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

D = "2026-06-13"
GUARD = ("absolutely no text, no captions, no Instagram or app UI, no phone screen interface, no watermark, "
         "no logos, no brand marks, no jersey numbers, one single uncropped photograph, single continuous wide shot, "
         "one frame only, not a collage, not a grid, not split panels, photorealistic editorial photograph")

JOBS = [
    # 1. IRAQ KURDISTAN OIL RESTART (broll_1 = PM Zaidi face if fetched; neutral fallback here)
    (f"{D}-iraq-kurdistan-oil-restart", "hero.jpg", f"A large modern oil export terminal in Iraq under bright clear blue sky, rows of huge cylindrical crude storage tanks and steel pipelines, a sense of resumed production and energy, photorealistic editorial wide establishing shot, no people, {GUARD}, {NEG}"),
    (f"{D}-iraq-kurdistan-oil-restart", "broll_1.jpg", f"A formal Iraqi government setting, the Iraqi national flag with green white black and red on a flagpole in front of a sand-colored official government building in Baghdad under bright daylight, a sense of state authority, photorealistic editorial wide shot, no people, {GUARD}, {NEG}"),
    (f"{D}-iraq-kurdistan-oil-restart", "broll_2.jpg", f"A long steel oil pipeline stretching across a sunlit northern Iraqi landscape toward distant mountains on the Turkish border, pressure valves and pump stations along the route, bright daylight, photorealistic documentary wide shot, no people, {GUARD}, {NEG}"),
    (f"{D}-iraq-kurdistan-oil-restart", "broll_3.jpg", f"A new oil pipeline under construction across a vast Iraqi desert, large sections of green-coated steel pipe laid out in a long line ready to be joined, heavy machinery, bright hazy daylight, photorealistic documentary wide shot, no recognizable faces, {GUARD}, {NEG}"),
    # 2. GAZA PHASE TWO (neutral, sensitive, no faces, daylight not dark)
    (f"{D}-gaza-phase-two", "hero.jpg", f"A wide view of a damaged Middle Eastern city skyline under bright hazy daylight, distant tall construction cranes beginning reconstruction among partly ruined concrete buildings, a somber but hopeful rebuilding atmosphere, cinematic editorial establishing shot, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-gaza-phase-two", "broll_1.jpg", f"A neutral formal diplomacy scene, an empty polished negotiation table with rows of empty chairs in a bright modern conference room, soft daylight through tall windows, an international mediation atmosphere, no flags, no logos, no readable text, no people, wide cinematic interior shot, {GUARD}, {NEG}"),
    (f"{D}-gaza-phase-two", "broll_2.jpg", f"A high aerial daytime view of a divided urban area split by a long cleared boundary line and concrete barriers running through it, bright daylight, a separation and partial-withdrawal concept, photorealistic wide overhead shot, no recognizable faces, no readable text, {GUARD}, {NEG}"),
    (f"{D}-gaza-phase-two", "broll_3.jpg", f"A large urban reconstruction site under bright daylight, tall tower cranes lifting materials, stacks of concrete blocks and rebar, rebuilding after destruction, a hopeful recovery atmosphere, photorealistic documentary wide shot, no recognizable faces, {GUARD}, {NEG}"),
    # 3. SAUDI VISION 2030 (economy / society, bright, no faces, no readable text)
    (f"{D}-saudi-vision2030-nextphase", "hero.jpg", f"A gleaming modern Riyadh skyline of glass skyscrapers at golden hour under a clear sky, a prosperous Gulf metropolis, a sense of economic transformation, photorealistic cinematic wide establishing shot, no readable text, no logos, no people, {GUARD}, {NEG}"),
    (f"{D}-saudi-vision2030-nextphase", "broll_1.jpg", f"A sleek modern Saudi financial and business district with mirrored office towers and palm-lined boulevards under bright daylight, a thriving non-oil economy atmosphere, photorealistic wide shot, no readable text, no logos, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-saudi-vision2030-nextphase", "broll_2.jpg", f"A vast bright modern airport terminal in Saudi Arabia with soaring architecture and many distant travelers with luggage, a booming tourism and travel atmosphere, photorealistic wide interior shot, no readable signage text, no logos, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-saudi-vision2030-nextphase", "broll_3.jpg", f"A futuristic Saudi giga-project of sleek curved modern architecture rising from the desert at dusk, ambitious visionary design, soft warm glow, photorealistic architectural render, no readable text, no logos, no people, {GUARD}, {NEG}"),
    # 4. JUNO NEUTRINO (science / physics, awe, well-lit hero)
    (f"{D}-juno-neutrino-result", "hero.jpg", f"The interior of a gigantic spherical particle physics detector, the vast curved inner wall covered with thousands of golden and bronze photomultiplier orbs glowing softly, an awe-inspiring high-tech cathedral of science, photorealistic wide shot, no people, no readable text, {GUARD}, {NEG}"),
    (f"{D}-juno-neutrino-result", "broll_1.jpg", f"An abstract scientific visualization of glowing particle tracks and oscillating wave patterns in luminous blue and gold against a dark gradient, a neutrino physics concept, sleek high-tech render, no readable text, no logos, {GUARD}, {NEG}"),
    (f"{D}-juno-neutrino-result", "broll_2.jpg", f"A vast underground physics laboratory deep beneath the earth, an enormous spherical detector surrounded by steel scaffolding and bright work lights, a monumental engineering scene, photorealistic wide shot, no recognizable faces, no readable text, {GUARD}, {NEG}"),
    (f"{D}-juno-neutrino-result", "broll_3.jpg", f"An ethereal abstract visualization of three glowing luminous spheres of different sizes representing neutrino mass states, floating in deep blue space with delicate light filaments, sleek scientific render, no readable text, no logos, {GUARD}, {NEG}"),
    # 5. STANFORD CARTILAGE (health, bright, hopeful; broll_3 = Helen Blau face if fetched)
    (f"{D}-stanford-cartilage-regrow", "hero.jpg", f"A bright modern medical research laboratory, a glowing clean three-dimensional illustration of a human knee joint with healthy cartilage on a large display screen, a hopeful regenerative-medicine atmosphere, soft daylight, shallow depth of field, no readable text, no people, {GUARD}, {NEG}"),
    (f"{D}-stanford-cartilage-regrow", "broll_1.jpg", f"A clean bright three-dimensional medical illustration of a human knee joint showing smooth glistening cartilage on the bone surfaces, a regenerative-biology concept, sleek polished render against a soft light background, no readable text, no logos, {GUARD}, {NEG}"),
    (f"{D}-stanford-cartilage-regrow", "broll_2.jpg", f"A bright clinical laboratory bench with a microscope and small petri dishes containing tissue samples, soft clean daylight, a biomedical research atmosphere, shallow depth of field, no readable text, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-stanford-cartilage-regrow", "broll_3.jpg", f"A scientist in a white coat holding up a small clear vial in a bright modern laboratory, seen from behind so the face is not visible, a medical-breakthrough atmosphere, soft daylight, shallow depth of field, no readable text, {GUARD}, {NEG}"),
    # 6. NBA FINALS (sport, festive; broll_3 = Jalen Brunson face if fetched; no logos/numbers/faces in generated)
    (f"{D}-nba-finals-knicks", "hero.jpg", f"A packed indoor basketball arena during a championship finals game at night, brilliant spotlights on a glossy hardwood court, a euphoric sea of fans in the stands, an electric big-game atmosphere, photorealistic cinematic wide establishing shot, no readable text, no logos, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-nba-finals-knicks", "broll_1.jpg", f"A dramatic high view of a glossy hardwood basketball court inside a sold-out arena under bright spotlights, vast crowd around it, a finals-night atmosphere, photorealistic wide shot, no readable text, no scoreboard numbers, no logos, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-nba-finals-knicks", "broll_2.jpg", f"A jubilant arena crowd erupting in celebration with golden confetti falling under bright spotlights at a basketball championship, pure euphoria, photorealistic cinematic shot, no readable text, no logos, no recognizable faces, {GUARD}, {NEG}"),
    (f"{D}-nba-finals-knicks", "broll_3.jpg", f"A lone basketball player in a plain unmarked uniform dribbling under a dramatic spotlight on a darkened arena court, dynamic silhouette-like lighting, photorealistic sports shot, no jersey numbers, no logos, no readable text, no recognizable face, {GUARD}, {NEG}"),
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
