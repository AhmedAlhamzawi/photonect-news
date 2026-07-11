#!/usr/bin/env python3
"""Generate the 20 editorial scenes for the 2026-07-11 slate via KIE Nano Banana Pro
(9:16, 2K). All scene-based (no named-person faces). Reuses gen_2026_05_28 infra.
Each prompt is matched to THAT beat's Arabic text. No signage / on-screen text
(NEG enforces) to dodge garbled-Arabic + fake-UI hallucinations. Iraqi flags named
explicitly and kept minimal (KIE has hallucinated foreign flags before — Read-verify).
"""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

D = "2026-07-11"
JOBS = [
    # 1 · basra-oil-halliburton (P1 — US oil-services giant develops two Basra fields)
    (f"{D}-basra-oil-halliburton", "hero.jpg", f"A vast southern Iraqi oil field near Basra at golden hour, rows of pump jacks and a distillation tower on flat desert, warm dust haze, a sense of expanding production capacity, epic cinematic editorial wide shot, {NEG}"),
    (f"{D}-basra-oil-halliburton", "broll_1.jpg", f"Oil field engineers in hard hats and hi-vis vests inspecting valves and gauges at a modern Basra pumping station, international and local crews working together, bright daylight documentary, no readable text, {NEG}"),
    (f"{D}-basra-oil-halliburton", "broll_2.jpg", f"A cluster of pump jacks and a bright gas flare stack under a deep blue Iraqi sky, oil and associated gas production ramping up, industrial editorial mid shot, {NEG}"),
    (f"{D}-basra-oil-halliburton", "broll_3.jpg", f"A large crude oil tanker being loaded at a Basra Gulf export terminal at dusk, storage tanks and a jetty, calm water and orange sky, aerial industrial editorial shot, {NEG}"),
    # 2 · crude-opec-quota (P2 — Iraq presses OPEC for a higher quota, warns of exit)
    (f"{D}-crude-opec-quota", "hero.jpg", f"An Iraqi crude oil export terminal on the Gulf at golden hour with many large storage tanks and a docked tanker, a sense of capacity held back, industrial cinematic wide aerial shot, {NEG}"),
    (f"{D}-crude-opec-quota", "broll_1.jpg", f"Endless rows of pump jacks working across a southern Iraqi oil field under a bright sky, maximum production, industrial documentary aerial, {NEG}"),
    (f"{D}-crude-opec-quota", "broll_2.jpg", f"An empty formal international summit conference hall with a large round table, microphones and blank name placards, no readable text, high-stakes diplomacy mood, editorial, {NEG}"),
    (f"{D}-crude-opec-quota", "broll_3.jpg", f"A close editorial still of industrial oil pressure gauges and a red valve wheel on a pipeline, needles near maximum, moody backlight, no readable numbers, {NEG}"),
    # 3 · graft-second-wave (P1 — Operation Dawn 2nd wave, immunity lifted on MPs)
    (f"{D}-graft-second-wave", "hero.jpg", f"Elite Iraqi anti-corruption forces in black tactical gear at the steps of a courthouse before dawn, vehicle headlights cutting the blue darkness, backs and helmets only no faces, tense cinematic documentary, {NEG}"),
    (f"{D}-graft-second-wave", "broll_1.jpg", f"A judge's wooden gavel resting on a sound block beside thick closed legal case files on a dark bench in an empty courtroom, hard overhead light, justice and accountability, no readable text, {NEG}"),
    (f"{D}-graft-second-wave", "broll_2.jpg", f"An empty grand parliamentary debating chamber with rows of vacant seats and a raised speaker's rostrum, cold morning light, a sense of lifted immunity, editorial wide shot, no readable text, {NEG}"),
    (f"{D}-graft-second-wave", "broll_3.jpg", f"An editorial evidence still on a dark table — neat stacks of seized US hundred-dollar banknotes and gold bars under a hard police light, a corruption seizure, no logos, no readable text, {NEG}"),
    # 4 · hawr-marshlands-rizq (P3 — southern marshes drying, livelihoods & heritage)
    (f"{D}-hawr-marshlands-rizq", "hero.jpg", f"The southern Iraqi Mesopotamian marshes at golden hour, tall green reeds and a lone traditional mashoof canoe on a shrinking silver waterway, a water buffalo in the shallows, lyrical cinematic wide shot, {NEG}"),
    (f"{D}-hawr-marshlands-rizq", "broll_1.jpg", f"A Marsh Arab fisherman poling a slender wooden mashoof canoe through thinning reed beds at soft dawn, timeless documentary portrait from behind, warm reflective water, {NEG}"),
    (f"{D}-hawr-marshlands-rizq", "broll_2.jpg", f"A cracked, sun-baked dry marsh bed in southern Iraq with a stranded wooden boat and a lone water buffalo searching for water, stark parched earth to the horizon, somber climate documentary, {NEG}"),
    (f"{D}-hawr-marshlands-rizq", "broll_3.jpg", f"A traditional woven-reed Marsh Arab mudhif guesthouse beside a narrow channel with buffalo and drying nets, the fragile livelihood of the marshes, warm evening light, editorial documentary, {NEG}"),
    # 5 · kurdistan-salary-standoff (P1 — Erbil-Baghdad salary/oil standoff, US urges deal)
    (f"{D}-kurdistan-salary-standoff", "hero.jpg", f"The Erbil city skyline and the ancient citadel at dusk under a tense grey sky, a modern Kurdistan government district in the foreground, a quiet standoff mood, cinematic editorial wide shot, {NEG}"),
    (f"{D}-kurdistan-salary-standoff", "broll_1.jpg", f"A long orderly queue of ordinary Kurdish public-sector employees waiting outside a plain salary payout office, everyday clothes, a bare concrete wall, patient documentary photojournalism, no signage text, {NEG}"),
    (f"{D}-kurdistan-salary-standoff", "broll_2.jpg", f"A large crude oil pipeline crossing rugged northern Iraqi Kurdistan mountains toward the Turkish border, idle and still under an overcast sky, the oil-for-salary linkage, industrial editorial, {NEG}"),
    (f"{D}-kurdistan-salary-standoff", "broll_3.jpg", f"Two empty facing chairs at a bare negotiating table in a plain official room with soft window light, a stalled negotiation between two governments, minimalist editorial, no readable text, {NEG}"),
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
    print(f"\n== Done {ok}/{len(JOBS)} ==", flush=True)
    fails = [f"{j['slug']}/{j['file']}" for j in jobs if not j["ok"]]
    if fails:
        for f in fails:
            print(f"  FAIL: {f}", file=sys.stderr)
    return 0 if ok == len(JOBS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
