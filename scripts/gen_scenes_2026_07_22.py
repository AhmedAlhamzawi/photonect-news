#!/usr/bin/env python3
"""Generate the 2026-07-22 slate scenes via KIE Nano Banana Pro (9:16 2K).
5 slugs x 4 images each (hero + broll_1/2/3), each matched to its beat.
No named-person faces (alt-scenario / crowd / scene framing) -> scenes only.
Reuses gen_2026_05_28 infra. Submit-all-then-poll-all.
"""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, http_get, first_image_url, download, submit  # type: ignore

D = "2026-07-22"

JOBS = [
    # 1 — TRAVEL DOLLAR CUT (airport / exchange / limited cash)
    (f"{D}-travel-dollar-2000", "hero.jpg", f"Close-up of a traveler's hands counting a modest stack of US hundred-dollar bills at an airport currency-exchange counter, an Iraqi passport and a suitcase beside them, warm terminal light, shallow depth of field, {NEG}"),
    (f"{D}-travel-dollar-2000", "broll_1.jpg", f"A neat but limited stack of US hundred-dollar banknotes lying next to a dark passport on a bank teller counter, a teller's hands sliding the cash across, cold clinical bank light, {NEG}"),
    (f"{D}-travel-dollar-2000", "broll_2.jpg", f"A money changer handing US dollar notes across the counter to a customer inside a bustling Baghdad exchange bureau, stacks of Iraqi dinar and dollar bundles, documentary photojournalism, {NEG}"),
    (f"{D}-travel-dollar-2000", "broll_3.jpg", f"Interior of a modern Iraqi airport departure hall, travelers pulling wheeled suitcases toward the gates, a small currency-exchange booth to one side, warm ambient light, wide documentary shot, {NEG}"),
    # 2 — KURDISTAN SALARY STANDOFF (queue / negotiation / pay office)
    (f"{D}-kurdistan-salary-standoff", "hero.jpg", f"A long anxious queue of Kurdish public-sector employees waiting outside a government salary office in Erbil, worried faces, folders in hand, overcast daylight, documentary photojournalism, {NEG}"),
    (f"{D}-kurdistan-salary-standoff", "broll_1.jpg", f"Two delegations of officials in suits seated across a long negotiation table in a formal government meeting room, the flag of Iraq and the flag of the Kurdistan Region on stands, tense atmosphere, wide editorial shot, {NEG}"),
    (f"{D}-kurdistan-salary-standoff", "broll_2.jpg", f"A crowded government pay office in Erbil, employees holding paperwork pressed against a service counter under cold fluorescent light, sense of waiting for wages, documentary, {NEG}"),
    (f"{D}-kurdistan-salary-standoff", "broll_3.jpg", f"Close-up of hands over stacks of official financial documents and a fountain pen on a polished desk, blurred Iraqi and Kurdistan flags in the background, high-stakes negotiation, shallow depth of field, {NEG}"),
    # 3 — ARBAEEN ECONOMY (pilgrims / mawakib / Karbala night)
    (f"{D}-arbaeen-economy", "hero.jpg", f"Aerial wide shot of a vast sea of millions of pilgrims dressed in black walking toward the golden-domed shrine of Imam Hussain in Karbala at dusk, immense scale, respectful cinematic photojournalism, {NEG}"),
    (f"{D}-arbaeen-economy", "broll_1.jpg", f"An endless river of pilgrims walking the long highway toward Karbala under the sun, green and black banners overhead, heat haze, wide documentary photojournalism, {NEG}"),
    (f"{D}-arbaeen-economy", "broll_2.jpg", f"A roadside mawkib service tent where volunteers ladle free food and hand water to passing pilgrims, steam rising from huge cooking pots, warm generous atmosphere, documentary, {NEG}"),
    (f"{D}-arbaeen-economy", "broll_3.jpg", f"A Karbala city street at night packed with pilgrims, strung festival lights overhead, vendors and service workers, sense of huge logistics and crowd, documentary photojournalism, {NEG}"),
    # 4 — OPEC PRICE SQUEEZE (tanker / oilfield / flag) [V10 control]
    (f"{D}-opec-price-squeeze", "hero.jpg", f"Aerial wide shot of a giant crude oil supertanker loading at a Gulf offshore export terminal at dawn, pipelines and mooring buoys on a calm steel-blue sea, cinematic, {NEG}"),
    (f"{D}-opec-price-squeeze", "broll_1.jpg", f"Rows of oil-well pumpjacks and tall gas flare stacks operating across a southern Iraqi desert oilfield at dusk, burnt-orange sky, heat haze, wide cinematic shot, {NEG}"),
    (f"{D}-opec-price-squeeze", "broll_2.jpg", f"A lone oil worker in a hard hat and overalls standing on a gantry overlooking a vast crude storage tank farm at golden hour, contemplative mood, industrial documentary, {NEG}"),
    (f"{D}-opec-price-squeeze", "broll_3.jpg", f"A large flag of Iraq flying on a tall pole against a dramatic dusk sky over the Baghdad skyline, wide establishing shot, sombre national mood, {NEG}"),
    # 5 — GRAFT CONCEALMENT (evidence / raid / hidden cash / gavel)
    (f"{D}-graft-concealment", "hero.jpg", f"Overhead shot of neat stacks of US hundred-dollar bills and gold bars and jewellery laid out as seized evidence on a dark table with paper evidence tags, dramatic investigative mood, {NEG}"),
    (f"{D}-graft-concealment", "broll_1.jpg", f"Elite Iraqi counter-terrorism officers in black tactical gear and body armor conducting a pre-dawn raid on an official villa, flashlight beams, tense documentary photojournalism, {NEG}"),
    (f"{D}-graft-concealment", "broll_2.jpg", f"Bundles of US dollar banknotes stuffed inside cut-open clear plastic water bottles arranged on a table as seized evidence, gritty investigative close-up, harsh light, {NEG}"),
    (f"{D}-graft-concealment", "broll_3.jpg", f"A wooden judge's gavel resting on formal Arabic legal documents on a courtroom bench, blurred scales of justice behind, accountability and rule of law, shallow depth of field, {NEG}"),
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
            url = first_image_url(data)
            state = str(data.get("state") or data.get("status") or "").lower()
            if url:
                try:
                    info = download(url, j["out"])
                    j["ok"] = True
                    print(f"  ✓ {j['slug']}/{j['file']}  {info}", flush=True)
                except Exception as e:
                    print(f"  ! download {j['slug']}/{j['file']}: {e}", file=sys.stderr, flush=True)
                    still.append(j)
            elif state in ("fail", "failed", "error"):
                print(f"  ✗ {j['slug']}/{j['file']} FAILED state={state}", file=sys.stderr, flush=True)
            else:
                still.append(j)
        pending = still
        print(f"    … {len(pending)} pending", flush=True)
    ok = sum(1 for j in jobs if j["ok"])
    print(f"\n== Done: {ok}/{len(jobs)} downloaded ==", flush=True)
    return 0 if ok == len(jobs) else 1


if __name__ == "__main__":
    raise SystemExit(main())
