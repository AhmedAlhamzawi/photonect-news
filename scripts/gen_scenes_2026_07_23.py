#!/usr/bin/env python3
"""Generate the 2026-07-23 slate scenes via KIE Nano Banana Pro (9:16 2K).
5 slugs x 4 images each (hero + broll_1/2/3), each matched to its beat.
Scenes only (no named-person faces on this slate). Hardened anti-UI/anti-text
negatives, especially for the AI-chips story. Submit-all-then-poll-all.
"""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, http_get, first_image_url, download, submit  # type: ignore

D = "2026-07-23"
NOUI = "absolutely no user-interface, no app screens, no news graphics, no readable text on any screen, no phone or tablet UI"

JOBS = [
    # 1 — GRAFT SPREADS: aviation + borders + Saladin (integrity enforcement)
    (f"{D}-graft-saladin-airways", "hero.jpg", f"Wide editorial shot of Iraqi integrity-commission investigators in formal attire walking into a government ministry building carrying document folders, a serious accountability operation, daylight, documentary photojournalism, {NEG}"),
    (f"{D}-graft-saladin-airways", "broll_1.jpg", f"A row of thick official case files and sealed legal document folders stacked on an investigator's wooden desk beside a small Iraqi flag, symbolizing multiple corruption cases, shallow depth of field, dramatic side light, {NEG}"),
    (f"{D}-graft-saladin-airways", "broll_2.jpg", f"Exterior of a parked Iraqi Airways passenger jet on the tarmac at an Iraqi airport under overcast sky, ground crew and stairs nearby, editorial aviation documentary shot, {NEG}"),
    (f"{D}-graft-saladin-airways", "broll_3.jpg", f"Close-up of an official's hands pressing a red ink stamp onto an Arabic arrest-warrant document at a provincial courtroom desk, rule of law and accountability, dramatic side light, shallow depth of field, {NEG}"),
    # 2 — JULY SALARIES LATE (ATM queue / delayed pay / finance ministry)
    (f"{D}-salaries-run-late", "hero.jpg", f"A long queue of ordinary Iraqi public-sector employees waiting to withdraw wages at a bank counter and ATM on a Baghdad street, worried expressions, folders in hand, overcast daylight, documentary photojournalism, {NEG}"),
    (f"{D}-salaries-run-late", "broll_1.jpg", f"Close-up of a worried man's hand holding a bank card in front of a glowing ATM machine in a dim bank vestibule, sense of waiting for a delayed salary, {NOUI}, shallow depth of field, {NEG}"),
    (f"{D}-salaries-run-late", "broll_2.jpg", f"Interior of an Iraqi finance ministry electronic-payments operations room, staff at computer terminals handling bank transfers, cool blue light, documentary, {NOUI}, {NEG}"),
    (f"{D}-salaries-run-late", "broll_3.jpg", f"Neat bundles of Iraqi dinar banknotes beside official government budget documents and a calculator on a desk in a finance office, cold clinical light, shallow depth of field, {NEG}"),
    # 3 — IRAQI SPRINT RECORD (generic athlete, no specific face)
    (f"{D}-iraq-sprint-national-record", "hero.jpg", f"A male sprinter in mid-stride bursting across the finish line on a blue running track in a packed floodlit stadium at night, motion blur, triumphant, cinematic sports photojournalism, {NEG}"),
    (f"{D}-iraq-sprint-national-record", "broll_1.jpg", f"Dynamic low-angle shot of a sprinter's spiked running shoes exploding off the starting blocks on a red athletics track, powerful motion, stadium background, sports photography, {NEG}"),
    (f"{D}-iraq-sprint-national-record", "broll_2.jpg", f"Two sprinters neck and neck lunging at the finish tape on an athletics track under bright floodlights, extreme motion blur, dramatic razor-thin margin, sports photojournalism, {NEG}"),
    (f"{D}-iraq-sprint-national-record", "broll_3.jpg", f"A victorious young athlete draped in the flag of Iraq raising both arms on a stadium running track at night, floodlights, emotional cinematic celebration, {NEG}"),
    # 4 — US OPENS AI CHIPS TO UAE (data center / chips / flags — hardened no-UI)
    (f"{D}-uae-us-ai-chips-greenlight", "hero.jpg", f"Aerial exterior of a vast modern AI data-center campus in the desert of the United Arab Emirates at dusk, sleek white buildings and cooling towers, warm sky, cinematic architectural photography, {NEG}"),
    (f"{D}-uae-us-ai-chips-greenlight", "broll_1.jpg", f"Extreme macro close-up of an advanced AI accelerator computer chip on a green circuit board, glowing gold contacts and intricate silicon detail, cold blue tech lighting, {NOUI}, {NEG}"),
    (f"{D}-uae-us-ai-chips-greenlight", "broll_2.jpg", f"Interior of a state-of-the-art data-center hall with long rows of illuminated server racks in blue-white light, an engineer in business attire walking the aisle, high-tech clean environment, {NOUI}, {NEG}"),
    (f"{D}-uae-us-ai-chips-greenlight", "broll_3.jpg", f"The flag of the United States and the flag of the United Arab Emirates on flagpoles side by side against a clear blue sky, diplomatic setting, wide establishing shot, {NEG}"),
    # 5 — IRAQ PROJECTS BOOM (construction cranes / megaproject / port)
    (f"{D}-iraq-projects-boom-despite-war", "hero.jpg", f"Wide aerial shot of a massive active construction site with many tall tower cranes and half-built high-rise towers in a modern Iraqi city under a golden dusk sky, sense of a building boom, cinematic, {NEG}"),
    (f"{D}-iraq-projects-boom-despite-war", "broll_1.jpg", f"A skyline of construction tower cranes silhouetted against a dramatic orange dusk sky over a growing Iraqi city, infrastructure boom, wide cinematic shot, {NEG}"),
    (f"{D}-iraq-projects-boom-despite-war", "broll_2.jpg", f"Iraqi construction workers in hard hats and hi-vis vests working on a large highway megaproject at sunrise, heavy machinery and earthmovers, hopeful industrious mood, documentary photojournalism, {NEG}"),
    (f"{D}-iraq-projects-boom-despite-war", "broll_3.jpg", f"Aerial view of a large modern container port under construction on the Iraqi coast with tall gantry cranes and cargo ships, Grand Faw port scale, calm blue sea, cinematic, {NEG}"),
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
    deadline = time.time() + 20 * 60
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
