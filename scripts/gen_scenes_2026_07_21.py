#!/usr/bin/env python3
"""Generate the 2026-07-21 slate scenes via KIE Nano Banana Pro (9:16 2K).
5 slugs x 4 images each (hero + broll_1/2/3), each matched to its beat.
No named-person faces this slate (all alt-scenario Iraqi officials) -> scenes only.
Reuses gen_2026_05_28 infra. Submit-all-then-poll-all.
"""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, http_get, first_image_url, download, submit  # type: ignore

D = "2026-07-21"

JOBS = [
    # 1 — GRAFT / OIL-MINISTRY UNDERSECRETARY ($86M seizure, Operation Fajr)
    (f"{D}-graft-oil-undersecretary", "hero.jpg", f"Neat stacks of hundred-dollar bills and gold jewellery laid out on a dark table as seized evidence in an anti-corruption raid, evidence tags, dramatic overhead shot, tense investigative mood, {NEG}"),
    (f"{D}-graft-oil-undersecretary", "broll_1.jpg", f"Elite Iraqi counter-terrorism officers in black tactical gear and body armor conducting a pre-dawn raid on an official villa in Baghdad's Green Zone, flashlights, tense documentary photojournalism, {NEG}"),
    (f"{D}-graft-oil-undersecretary", "broll_2.jpg", f"A large modern Iraqi government ministry building at dusk with the flag of Iraq flying on a tall pole out front, official state architecture, sombre wide establishing shot, {NEG}"),
    (f"{D}-graft-oil-undersecretary", "broll_3.jpg", f"A wooden judge's gavel resting on formal Arabic legal documents on a courtroom bench, scales of justice blurred behind, accountability and rule of law, shallow depth of field, {NEG}"),
    # 2 — ELECTRICITY CABLE THEFT (Integrity Commission, blackout, your bill)
    (f"{D}-electricity-cable-theft", "hero.jpg", f"Huge coils of thick stolen high-voltage copper power cables piled up in a warehouse as seized evidence, harsh overhead light, gritty investigative documentary, {NEG}"),
    (f"{D}-electricity-cable-theft", "broll_1.jpg", f"Interior of a dim electricity-distribution warehouse in Baghdad, rows of cable spools and grey power transformers on shelves, cold fluorescent light, {NEG}"),
    (f"{D}-electricity-cable-theft", "broll_2.jpg", f"An Iraqi family sitting in a dim living room during a summer power blackout, lit only by a battery lantern and phone screens, sweltering Baghdad night, intimate documentary, {NEG}"),
    (f"{D}-electricity-cable-theft", "broll_3.jpg", f"Close-up of a worn residential electricity meter on a cracked apartment wall in Iraq, dials and wiring, a hand reaching toward it, harsh daylight, {NEG}"),
    # 3 — OIL EXPORTS RESTART (southern fields, Basra terminals, tankers)
    (f"{D}-oil-exports-restart", "hero.jpg", f"Aerial wide shot of a giant crude oil supertanker loading at Basra's offshore export terminal at dawn, calm steel-blue Persian Gulf, pipelines and mooring buoys, cinematic, {NEG}"),
    (f"{D}-oil-exports-restart", "broll_1.jpg", f"Oil field pumpjacks and tall gas flare stacks operating at full tilt in the southern Iraqi desert at dusk, burnt-orange sky, heat haze, sense of restored production, wide cinematic shot, {NEG}"),
    (f"{D}-oil-exports-restart", "broll_2.jpg", f"A sprawling Basra oil terminal at golden hour, huge white crude storage tanks and a maze of silver pipelines, a worker in a hard hat walking, industrial documentary, {NEG}"),
    (f"{D}-oil-exports-restart", "broll_3.jpg", f"Thick black crude oil gushing and swirling into a large steel storage tank, glistening surface, extreme close-up, dramatic industrial photography, {NEG}"),
    # 4 — FAW PORT LIFELINE (Grand Faw Port, cranes, Development Road)
    (f"{D}-faw-port-lifeline", "hero.jpg", f"Aerial wide shot of a vast new mega container port under construction on Iraq's southern Gulf coast at dawn, rows of towering ship-to-shore cranes and long new concrete berths beside calm sea, immense scale, cinematic, {NEG}"),
    (f"{D}-faw-port-lifeline", "broll_1.jpg", f"A line of enormous blue ship-to-shore container gantry cranes towering over thousands of stacked colourful shipping containers at a modern port, low heroic angle, golden light, {NEG}"),
    (f"{D}-faw-port-lifeline", "broll_2.jpg", f"A brand-new multi-lane highway and parallel high-speed rail corridor cutting straight through the flat Iraqi desert toward the horizon, cargo trucks, heat shimmer, wide aerial shot, {NEG}"),
    (f"{D}-faw-port-lifeline", "broll_3.jpg", f"A massive container cargo ship being guided by tugboats to dock at a gleaming new port berth, gantry cranes reaching over the deck, calm Gulf water, wide cinematic shot, {NEG}"),
    # 5 — IRAQ-US WASHINGTON DEALS (flags, summit, Kirkuk-Baniyas pipeline) [V10 control]
    (f"{D}-iraq-us-deals", "hero.jpg", f"The national flag of the United States and the flag of Iraq (red white black bands with green Arabic script) standing side by side on polished poles inside a grand marble Washington summit hall, formal diplomacy, warm light, {NEG}"),
    (f"{D}-iraq-us-deals", "broll_1.jpg", f"A formal business-summit signing table with the US and Iraqi flags, rows of empty leather chairs and folders of contracts, blurred suited delegates in the background, corporate diplomacy, {NEG}"),
    (f"{D}-iraq-us-deals", "broll_2.jpg", f"A long steel crude-oil pipeline stretching across arid desert terrain toward distant mountains, pump station, sense of a strategic export route, wide cinematic shot, {NEG}"),
    (f"{D}-iraq-us-deals", "broll_3.jpg", f"An oil pipeline arriving at a Mediterranean coastal export terminal at dusk, storage tanks and a moored tanker on a calm sea, warm horizon, wide establishing shot, {NEG}"),
]


def main() -> int:
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
    deadline = time.time() + 16 * 60
    while pending and time.time() < deadline:
        time.sleep(POLL_INTERVAL)
        still = []
        for j in pending:
            try:
                r = http_get(f"{STATUS_URL}?taskId={j['tid']}")
            except Exception:
                still.append(j); continue
            data = (r.get("data") or {})
            state = str(data.get("state") or data.get("status") or "").lower()
            url = first_image_url(data)
            if url:
                try:
                    info = download(url, j["out"])
                    j["ok"] = True
                    print(f"  ✓ {j['slug']}/{j['file']}  {info}", flush=True)
                except Exception as e:
                    print(f"  ! download {j['slug']}/{j['file']}: {e}", file=sys.stderr, flush=True)
                    still.append(j)
            elif state in ("fail", "failed", "error"):
                print(f"  ✗ FAILED {j['slug']}/{j['file']}: {data.get('failMsg') or data}", file=sys.stderr, flush=True)
            else:
                still.append(j)
        pending = still
        print(f"    ... {len(pending)} pending", flush=True)
    ok = sum(1 for j in jobs if j.get("ok"))
    print(f"\n== Done: {ok}/{len(jobs)} succeeded ==", flush=True)
    for j in jobs:
        if not j.get("ok"):
            print(f"   MISSING: {j['slug']}/{j['file']}", flush=True)
    return 0 if ok == len(jobs) else 1


if __name__ == "__main__":
    raise SystemExit(main())
