#!/usr/bin/env python3
"""Generate the 20 editorial scenes for the 2026-07-10 slate via KIE Nano Banana Pro
(9:16, 2K). All scene-based (no named-person faces). Reuses gen_2026_05_28 infra.
Each prompt is matched to THAT beat's Arabic text. No signage / no on-screen text
(NEG enforces) to dodge garbled-Arabic + fake-UI hallucinations.
"""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

D = "2026-07-10"
JOBS = [
    # 1 · budget-salary-clock (P1 — no budget 2 years, salaries, 2027 draft)
    (f"{D}-budget-salary-clock", "hero.jpg", f"A grand Iraqi government finance ministry building in Baghdad at dawn, pale marble facade and columns, a national flag, quiet empty official plaza, solemn sense of a stalled bureaucracy, wide cinematic editorial shot, {NEG}"),
    (f"{D}-budget-salary-clock", "broll_1.jpg", f"A clean editorial still life on a wooden desk — a thick closed official ledger, a fountain pen and a calculator beside a small national flag, soft window light, the drafting of a budget, no readable fine text, {NEG}"),
    (f"{D}-budget-salary-clock", "broll_2.jpg", f"A long orderly queue of ordinary Iraqi public-sector employees waiting outside a plain government salary office, everyday clothes, a bare concrete wall, patient documentary photojournalism, no signage text, {NEG}"),
    (f"{D}-budget-salary-clock", "broll_3.jpg", f"A modern Iraqi government meeting room where officials in suits review abstract financial bar charts on a large wall screen, professional editorial atmosphere, soft daylight, no readable text, {NEG}"),
    # 2 · crude-pipeline-clock (P2 — Iraq-Turkey pipeline treaty expiring)
    (f"{D}-crude-pipeline-clock", "hero.jpg", f"A vast crude-oil pipeline stretching across arid northern Iraqi mountains toward the horizon at golden hour, a pump station in the distance, epic industrial cinematic wide shot, {NEG}"),
    (f"{D}-crude-pipeline-clock", "broll_1.jpg", f"An aerial view of a large oil export pipeline crossing rugged terrain near the Iraq-Turkey border region, dramatic dusk light and long shadows, editorial documentary, {NEG}"),
    (f"{D}-crude-pipeline-clock", "broll_2.jpg", f"A Mediterranean oil export terminal at dusk with rows of large storage tanks and a docked crude tanker at a jetty, calm sea and orange sky, industrial editorial aerial shot, {NEG}"),
    (f"{D}-crude-pipeline-clock", "broll_3.jpg", f"A dormant idle oil pipeline valve station with closed red valves and gauges under a grey overcast sky, still and rusting, somber industrial documentary, no readable text, {NEG}"),
    # 3 · graft-oil-sector (P1 — Operation Dawn, $250M seized, reaching oil)
    (f"{D}-graft-oil-sector", "hero.jpg", f"Elite Iraqi anti-corruption forces in black tactical gear conducting a pre-dawn operation outside an official government building, vehicle headlights cutting the darkness, backs and helmets only no faces, tense cinematic documentary, {NEG}"),
    (f"{D}-graft-oil-sector", "broll_1.jpg", f"An editorial evidence still life on a dark table — neat stacks of seized US hundred-dollar banknotes and a few gold bars under a hard overhead light, a police seizure, no logos, no readable text, {NEG}"),
    (f"{D}-graft-oil-sector", "broll_2.jpg", f"An Iraqi oil refinery at dusk with distillation towers and a single flare stack silhouetted against a deep orange sky, ominous industrial wide shot, {NEG}"),
    (f"{D}-graft-oil-sector", "broll_3.jpg", f"An empty ornate Iraqi government hall with a long polished marble corridor, a single distant figure walking away in shadow, a sense of scale and accountability, cinematic editorial, {NEG}"),
    # 4 · gulf-billions-iraq (P2 — Gulf funds + jobs)
    (f"{D}-gulf-billions-iraq", "hero.jpg", f"A gleaming Gulf financial-district skyline of modern glass towers at golden hour beside distant construction cranes, a sense of sovereign-wealth capital and investment, optimistic cinematic editorial wide shot, {NEG}"),
    (f"{D}-gulf-billions-iraq", "broll_1.jpg", f"A modern Gulf sovereign wealth fund headquarters tower with reflective blue glass and a bright corporate plaza, luxury financial architecture, clean daylight editorial, no readable text, {NEG}"),
    (f"{D}-gulf-billions-iraq", "broll_2.jpg", f"A busy modern Iraqi construction and industrial site with tower cranes and workers in hard hats and hi-vis vests building new infrastructure, bright daylight, optimistic documentary, {NEG}"),
    (f"{D}-gulf-billions-iraq", "broll_3.jpg", f"Young Iraqi professionals in business attire, men and women of varied ages, walking into a modern office building in Baghdad in hopeful morning light, editorial documentary, {NEG}"),
    # 5 · heat-record-world (P3 — heatwave, water 8%, grid strain)
    (f"{D}-heat-record-world", "hero.jpg", f"Blazing Iraqi summer sun over a Baghdad street at midday, intense heat haze shimmering off the empty asphalt, a lone figure shielding their eyes from the glare, cinematic documentary, {NEG}"),
    (f"{D}-heat-record-world", "broll_1.jpg", f"A deserted Iraqi city street at noon under a scorching white sun, shuttered shopfronts and empty pavements during a heat holiday, harsh light and visible heat shimmer, documentary, no readable text, {NEG}"),
    (f"{D}-heat-record-world", "broll_2.jpg", f"A cracked dried-up riverbed in southern Iraq under a harsh sun, parched fissured earth stretching to the horizon with only a thin trickle of water, stark climate documentary, {NEG}"),
    (f"{D}-heat-record-world", "broll_3.jpg", f"Iraqi high-voltage transmission towers and sagging power lines under a hazy scorching sky above a dense low-rise neighborhood bristling with air-conditioner units, heat distortion, documentary editorial, {NEG}"),
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
