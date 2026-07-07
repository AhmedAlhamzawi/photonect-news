#!/usr/bin/env python3
"""Generate the 20 bespoke KIE nano-banana-pro 9:16 2K scenes for 2026-07-07.
All scene-based (no named-person portraits → no Commons faces). One still per beat.
Reuses gen_2026_05_28 infra. Hardened anti-UI + upright-portrait prompts.
"""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

D = "2026-07-07"
EXTRA = ("authentic Middle Eastern / Iraqi setting, correct upright vertical 9:16 orientation, "
         "no smartphone or app interface, no news-app screenshot, no ticker graphics, no text overlays, "
         "no readable writing, no garbled letters, no distorted faces, no extra limbs")

def N(x): return f"{x}, {NEG}, {EXTRA}"

# (slug, filename, prompt)
JOBS = [
    # 1. DEVELOPMENT ROAD / FAW — jobs & mega-project
    (f"{D}-development-road-jobs", "hero.jpg", N("Epic aerial establishing shot of a vast modern deep-water container port under construction on an artificial island in southern Iraq, giant orange gantry cranes, long concrete quays, cargo ships, turquoise Gulf water, golden-hour light, immense scale")),
    (f"{D}-development-road-jobs", "broll_1.jpg", N("A newly built double-track railway line stretching straight to the horizon across the flat southern Iraqi desert, fresh grey ballast and gleaming steel rails, construction machinery in the distance, clear pale sky, wide cinematic")),
    (f"{D}-development-road-jobs", "broll_2.jpg", N("Construction workers in orange hi-vis vests and white hard hats at a massive port container yard in Iraq, tall stacks of colorful shipping containers, gantry cranes overhead, busy industrial site, documentary photojournalism")),
    (f"{D}-development-road-jobs", "broll_3.jpg", N("A brand-new multi-lane highway and parallel rail corridor cutting through open desert with logistics warehouses and industrial hubs alongside, freight trucks, warm sunset haze, wide aerial establishing shot")),
    # 2. OPEC STANDOFF — oil / quota / Hormuz
    (f"{D}-iraq-opec-standoff", "hero.jpg", N("A giant crude oil supertanker riding low in the water crossing the Strait of Hormuz at dawn, calm steel-blue Persian Gulf, faint hazy coastline, strategic tension, wide aerial cinematic")),
    (f"{D}-iraq-opec-standoff", "broll_1.jpg", N("A formal international oil ministers conference hall, a long polished wooden table ringed with generic national flags of oil-producing nations, empty leather chairs, dramatic chandelier lighting, no identifiable people")),
    (f"{D}-iraq-opec-standoff", "broll_2.jpg", N("A sprawling crude oil export terminal in southern Iraq at dusk, webs of pipelines, rows of storage tanks, loading jetties reaching into the Gulf, faint gas-flare glow, wide industrial aerial nightscape")),
    (f"{D}-iraq-opec-standoff", "broll_3.jpg", N("Abstract glowing red and green financial candlestick chart of oil prices projected across a dark wall, blurred bokeh, tense market mood, no readable numbers, cinematic")),
    # 3. GULF POWER LINK — electricity interconnection
    (f"{D}-iraq-power-gulf-link", "hero.jpg", N("High-voltage lattice transmission towers and long 400kV power lines marching across the southern Iraqi desert at golden dusk, a substation glowing in the distance, new energy infrastructure, wide cinematic")),
    (f"{D}-iraq-power-gulf-link", "broll_1.jpg", N("A large modern electrical substation with transformers and switchgear at dusk near Basra Iraq, glowing insulators, orderly high-voltage grid infrastructure, wide clean shot")),
    (f"{D}-iraq-power-gulf-link", "broll_2.jpg", N("Long-distance overhead power transmission lines and steel lattice towers crossing arid borderland desert between the Gulf and Iraq at sunset, receding to the horizon, epic scale, wide aerial")),
    (f"{D}-iraq-power-gulf-link", "broll_3.jpg", N("An Iraqi family in a warmly lit living room at night with the lights on and a ceiling fan spinning, calm and normal, an idle unused private generator on the balcony outside, intimate documentary")),
    # 4. WORLD CUP RETURN — pride, scene-based, no player faces
    (f"{D}-iraq-worldcup-return", "hero.jpg", N("A packed floodlit football stadium at night filled with jubilant fans waving the flag of Iraq (red white and black horizontal bands with green Arabic script), bright green pitch, confetti in the air, electric atmosphere, wide cinematic sports photography, no identifiable faces")),
    (f"{D}-iraq-worldcup-return", "broll_1.jpg", N("Ecstatic football fans in red and white celebrating in packed stadium stands, waving Iraqi flags and scarves, joyous emotion, bright night stadium floodlights, documentary crowd photography, no single identifiable person")),
    (f"{D}-iraq-worldcup-return", "broll_2.jpg", N("A generic golden football world-championship trophy on a pedestal under stadium floodlights, confetti falling, blurred packed crowd behind, ultra-realistic sports photography, no logos")),
    (f"{D}-iraq-worldcup-return", "broll_3.jpg", N("A single football boot and a ball resting on a floodlit green pitch at night with an empty goal net behind, dramatic long shadows, bittersweet reflective mood, cinematic close-up")),
    # 5. PAYROLL / PRINTING — money, liquidity, salaries
    (f"{D}-payroll-printing", "hero.jpg", N("Close-up of thick stacks and bundles of generic Iraqi dinar banknotes on a dark surface, shallow depth of field, blurred so no text is legible, dramatic cinematic lighting, sense of a cash crunch")),
    (f"{D}-payroll-printing", "broll_1.jpg", N("A long orderly queue of Iraqi public-sector employees waiting outside a government salary pay office in summer heat, plain modern building, documentary photojournalism, authentic Iraqi street")),
    (f"{D}-payroll-printing", "broll_2.jpg", N("Extreme close-up of hands counting a thick stack of generic Iraqi dinar banknotes at a bank teller counter, shallow focus, blurred notes with no legible text, tension, documentary")),
    (f"{D}-payroll-printing", "broll_3.jpg", N("A stately modern central bank / finance ministry building in Baghdad Iraq at dusk, imposing columned architecture, the flag of Iraq on a pole, wide low-angle establishing shot")),
]

def main():
    only = set(sys.argv[1:])
    jobs = []
    print(f"== Submitting {len(JOBS)} scene jobs ==", flush=True)
    for slug, fname, prompt in JOBS:
        if only and slug not in only:
            continue
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
            data = (r.get("data") or {})
            state = data.get("state") or data.get("status") or ""
            url = first_image_url(data)
            if url:
                try:
                    info = download(url, j["out"])
                    j["ok"] = True
                    print(f"  ✓ {j['slug']}/{j['file']}  {info}", flush=True)
                except Exception as e:
                    print(f"  ! download {j['slug']}/{j['file']}: {e}", file=sys.stderr, flush=True)
            elif str(state).lower() in ("fail", "failed", "error"):
                print(f"  ✗ {j['slug']}/{j['file']} FAILED state={state}", file=sys.stderr, flush=True)
            else:
                still.append(j)
        pending = still
        print(f"    …{len(pending)} pending", flush=True)
    ok = sum(1 for j in jobs if j.get("ok"))
    print(f"\n== DONE {ok}/{len(jobs)} ok ==", flush=True)
    return 0 if ok == len(jobs) else 1

if __name__ == "__main__":
    sys.exit(main())
