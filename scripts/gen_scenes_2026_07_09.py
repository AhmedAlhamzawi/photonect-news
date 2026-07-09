#!/usr/bin/env python3
"""Generate the 20 editorial scenes for the 2026-07-09 slate via KIE Nano Banana Pro
(9:16, 2K). All scene-based (no named-person faces). Reuses gen_2026_05_28 infra.
Each prompt is matched to THAT beat's Arabic text. No signage / no on-screen text
(NEG enforces) to dodge garbled-Arabic + fake-UI hallucinations.
"""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

D = "2026-07-09"
JOBS = [
    # 1 · american-hospital (health + money, keep spend home)
    (f"{D}-american-hospital", "hero.jpg", f"Interior of a gleaming state-of-the-art modern hospital lobby with clean white and glass architecture, advanced medical equipment visible, bright natural light, a sense of world-class healthcare, wide cinematic shot, {NEG}"),
    (f"{D}-american-hospital", "broll_1.jpg", f"A middle-aged Iraqi patient with a suitcase and a folder of medical scans waiting in an airport departure hall, about to travel abroad for treatment, tired anxious expression, soft overcast window light, documentary photojournalism, {NEG}"),
    (f"{D}-american-hospital", "broll_2.jpg", f"A clean editorial still life on a dark surface — a stethoscope, a fan of US hundred-dollar bills, a passport and an X-ray film, symbolizing the cost of medical travel abroad, dramatic side light, {NEG}"),
    (f"{D}-american-hospital", "broll_3.jpg", f"Doctors and nurses in scrubs walking through a bright modern hospital corridor with advanced imaging machines, a newly built advanced medical facility, hopeful professional atmosphere, wide documentary shot, {NEG}"),
    # 2 · electricity-graft (corruption reaching the grid)
    (f"{D}-electricity-graft", "hero.jpg", f"A high-voltage electrical substation and transmission towers silhouetted against a dark dusk sky over a mostly blacked-out Iraqi city skyline, only a few scattered lights, ominous tense mood, wide cinematic shot, {NEG}"),
    (f"{D}-electricity-graft", "broll_1.jpg", f"An empty administrative office in a government building with vacated desks and chairs, papers left behind and open filing drawers, the aftermath of officials being removed, cold fluorescent light, documentary, {NEG}"),
    (f"{D}-electricity-graft", "broll_2.jpg", f"An editorial still life — thick stacks of Iraqi dinar banknotes, a household electricity meter and a paper ledger on a worn desk, money quietly disappearing from bill collections, moody dramatic side light, {NEG}"),
    (f"{D}-electricity-graft", "broll_3.jpg", f"Elite Iraqi anti-corruption forces in black tactical gear conducting a pre-dawn operation, vehicle headlights and flashlight beams cutting darkness, backs and helmets only no faces, tense cinematic documentary, {NEG}"),
    # 3 · iran-deal-collapse (Hormuz under fire, Iraq oil lifeline)
    (f"{D}-iran-deal-collapse", "hero.jpg", f"A massive crude-oil supertanker in the narrow Strait of Hormuz at dusk with a distant grey warship silhouette on the horizon, tense hazy strategic standoff, deep orange and steel-blue sky, wide cinematic aerial shot, {NEG}"),
    (f"{D}-iran-deal-collapse", "broll_1.jpg", f"An abandoned formal diplomatic negotiation table in a grand empty hall, two blank national flags on stands, empty leather chairs and scattered papers, a collapsed agreement, cold dramatic light no identifiable people, {NEG}"),
    (f"{D}-iran-deal-collapse", "broll_2.jpg", f"Several large commercial cargo and oil ships anchored and stranded in the Persian Gulf at dusk, a lone silhouetted seafarer standing on a deck looking out, waiting and uncertainty, moody wide shot, {NEG}"),
    (f"{D}-iran-deal-collapse", "broll_3.jpg", f"An Iraqi oil export terminal at Basra with a large tanker loading at a jetty, pipelines and storage tanks along the Gulf shore at golden hour, Iraq's export lifeline, wide aerial shot, {NEG}"),
    # 4 · land-plots-million (housing / who gets a plot)
    (f"{D}-land-plots-million", "hero.jpg", f"A vast aerial view of newly surveyed empty residential land plots on the outskirts of an Iraqi city, a grid of dirt roads and utility poles across arid ground, early morning light, sense of a huge housing project, wide drone shot, {NEG}"),
    (f"{D}-land-plots-million", "broll_1.jpg", f"An aerial shot of gridded empty land plots with freshly laid asphalt roads, concrete boundary markers and rows of new electricity poles, infrastructure being installed across bare land, bright daylight, {NEG}"),
    (f"{D}-land-plots-million", "broll_2.jpg", f"An ordinary Iraqi family standing hopefully on a bare plot of land in front of a half-built modest concrete house, gesturing at their future home, warm afternoon light, intimate documentary, {NEG}"),
    (f"{D}-land-plots-million", "broll_3.jpg", f"A long orderly queue of ordinary Iraqi citizens holding paperwork outside a government housing registration office, waiting to claim land, mixed emotions of hope and worry, overcast daylight documentary, {NEG}"),
    # 5 · washington-dollar (PM to Washington, investment vs weapons)
    (f"{D}-washington-dollar", "hero.jpg", f"The White House in Washington viewed across the lawn at golden hour with two flagpoles flying an American flag and the national flag of Iraq (red white black horizontal bands with green Arabic script) side by side, diplomatic gravitas, wide cinematic shot, {NEG}"),
    (f"{D}-washington-dollar", "broll_1.jpg", f"A delegation of Iraqi businessmen in dark suits carrying briefcases walking across an airport tarmac toward a waiting government aircraft at dawn, a high-level economic mission, crisp editorial photojournalism, {NEG}"),
    (f"{D}-washington-dollar", "broll_2.jpg", f"A bustling modern Iraqi construction and industrial site with cranes, new steel-frame buildings and workers in hard hats, private-sector investment and job creation, hopeful bright daylight, wide shot, {NEG}"),
    (f"{D}-washington-dollar", "broll_3.jpg", f"Iraqi soldiers standing in disciplined formation beneath a large national flag of Iraq (red white black horizontal bands with green Arabic takbir script) at a state ceremony, weapons under state authority, low heroic angle, {NEG}"),
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
    sys.exit(main())
