#!/usr/bin/env python3
"""Generate the 20 scenes for the 2026-07-20 slate via Nano Banana Pro (KIE).

Human/object-led prompts only (no bare gov-building establishing shots -> fake UI),
upright-portrait pin, hardened anti-UI/anti-screenshot negatives. No phone-screen
scenes (they hallucinate fake app UI). See feedback_kie_fake_ui_govbuilding,
feedback_kie_no_screenshot, feedback_daily_render_gotchas.
"""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

D = "2026-07-20"

NEG = (
    "ultra-realistic editorial photojournalism, cinematic lighting, "
    "upright vertical 9:16 portrait orientation, correctly oriented, not rotated, not sideways, "
    "no on-screen text, no captions, no subtitles, no watermark, no logos, no signage text, "
    "no user interface, no app interface, no phone screenshot, no social media UI, "
    "no news ticker, no chyron, no lower third, no browser window, no arabic text, no garbled text"
)

JOBS = [
    # 1 — BUDGET / SALARY FREEZE (state finances reduced to salaries only)
    (f"{D}-budget-salary-freeze", "hero.jpg", f"A government paymaster's hands counting a thin stack of Iraqi dinar banknotes at a teller window, a long blurred queue of civil servants waiting behind, cold fluorescent light, tense documentary, {NEG}"),
    (f"{D}-budget-salary-freeze", "broll_1.jpg", f"A vast half-built public project site with idle cranes and exposed rebar and no workers, under a hazy pale sky, desolate wide shot, frozen construction, {NEG}"),
    (f"{D}-budget-salary-freeze", "broll_2.jpg", f"Close-up of a thick closed government budget ledger bound with a rubber band and a red official wax seal on a dark desk under a single lamp, deep shadows, {NEG}"),
    (f"{D}-budget-salary-freeze", "broll_3.jpg", f"An accountant's hands dividing a pile of cash into twelve small equal stacks on a desk under a lamp, overhead top-down shot, symbolic of rationed monthly spending, {NEG}"),
    # 2 — WAR / IRANIAN GAS CUT -> BLACKOUT
    (f"{D}-war-gas-blackout", "hero.jpg", f"A sprawling Middle Eastern city at night in near-total darkness, only scattered generator-lit windows glowing amber, hazy skyline, aerial cinematic wide shot, {NEG}"),
    (f"{D}-war-gas-blackout", "broll_1.jpg", f"A rusted gas pipeline pressure gauge and valves at a power plant under a blistering white sky, heat haze distorting the air, industrial close-up, {NEG}"),
    (f"{D}-war-gas-blackout", "broll_2.jpg", f"A family sweltering in a dim living room during a blackout, a still ceiling fan overhead, faces lit only by a battery lantern, sweat and heat, intimate documentary, {NEG}"),
    (f"{D}-war-gas-blackout", "broll_3.jpg", f"A row of small private diesel generators lined along an alley wall with tangled cables overhead and drifting exhaust smoke, gritty street documentary at dusk, {NEG}"),
    # 3 — GRAFT WHISTLEBLOWER REWARDS
    (f"{D}-graft-whistleblower", "hero.jpg", f"An anonymous hand dropping a sealed white envelope into a locked metal complaints box mounted on a government office wall, shallow focus, tense and furtive, dramatic side light, {NEG}"),
    (f"{D}-graft-whistleblower", "broll_1.jpg", f"Stacks of recovered banded hundred-dollar bills and gold bars laid on a table under a single hard light, evidence-room mood, still life, {NEG}"),
    (f"{D}-graft-whistleblower", "broll_2.jpg", f"An empty investigators' interview room with two metal chairs facing each other under a harsh overhead light, bare walls, long shadows, ominous, {NEG}"),
    (f"{D}-graft-whistleblower", "broll_3.jpg", f"A bundle of banknotes resting beside an official stamped certificate document on a wooden desk under a warm lamp, symbolic reward still life, shallow depth of field, {NEG}"),
    # 4 — BANIYAS OIL CORRIDOR (bypass Hormuz)
    (f"{D}-baniyas-oil-corridor", "hero.jpg", f"An oil pipeline stretching to the horizon across an empty desert at golden hour, strong converging perspective lines, epic cinematic wide shot, {NEG}"),
    (f"{D}-baniyas-oil-corridor", "broll_1.jpg", f"A Mediterranean coastal oil terminal with large white storage tanks and a tanker berthed at dusk, calm sea, wide establishing shot, {NEG}"),
    (f"{D}-baniyas-oil-corridor", "broll_2.jpg", f"Engineers in hard hats leaning over a large route map spread on a table at a construction site, only hands and torsos visible, planning mood, warm light, {NEG}"),
    (f"{D}-baniyas-oil-corridor", "broll_3.jpg", f"A crude oil tanker ship navigating a narrow sea strait at dusk with distant shore lights, tense maritime chokepoint mood, cinematic wide shot, {NEG}"),
    # 5 — DINAR / DOLLAR (market dollar edging down, still above official)
    (f"{D}-dinar-dollar-fall", "hero.jpg", f"A currency exchange shop counter at night, a hand stacking bundles of US dollars beside bundles of Iraqi dinars, warm neon glow, no readable numbers, documentary close-up, {NEG}"),
    (f"{D}-dinar-dollar-fall", "broll_1.jpg", f"Close-up of hands counting a fan of crisp US hundred-dollar bills over a glass counter, shallow focus, money-changer mood, {NEG}"),
    (f"{D}-dinar-dollar-fall", "broll_2.jpg", f"A bustling money-changer street in a Middle Eastern city at evening with shopfronts and people walking, no readable signage, wide documentary, {NEG}"),
    (f"{D}-dinar-dollar-fall", "broll_3.jpg", f"A brass balance scale on a desk with a small stack of US dollars on one pan and Iraqi dinar notes on the other, tilting slightly, symbolic still life under a lamp, {NEG}"),
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
                    print(f"  ✗ {j['slug']}/{j['file']} success but no url", file=sys.stderr, flush=True)
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
    ok = sum(1 for j in jobs if j.get("ok"))
    print(f"\n== Done: {ok}/{len(JOBS)} ==", flush=True)
    for j in jobs:
        if not j.get("ok"):
            print(f"  MISSING {j['slug']}/{j['file']}", flush=True)


if __name__ == "__main__":
    main()
