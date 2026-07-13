#!/usr/bin/env python3
"""Generate the 20 editorial scenes for the 2026-07-13 slate via KIE Nano Banana Pro
(9:16, 2K). All scene-based (no named-person faces — the officials here are new 2026
figures with no reliable Commons portrait; scene-based avoids wrong-face + fake-face
risk, matching the 2026-07-11/12 precedent). Each prompt is matched to THAT beat's
Arabic text. Hardened anti-UI / anti-text negatives (see feedback_kie_fake_ui_govbuilding).
Read-verify every image before accept.

Slate:
  1 · basra-water-rationing   (P1 services)   — drought / water rationing
  2 · congo-fever-outbreak    (P3 health)     — CCHF livestock fever
  3 · graft-oil-two-trillion  (P1, V11)       — oil corruption seizures
  4 · gulf-energy-fund-iraq   (P2 Gulf-Iraq)  — Gulf energy investment
  5 · iraq-turkey-pipeline-clock (P1, V11)    — ITP treaty expiry
"""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

# Extra-hard negatives for any shot at risk of hallucinated UI / gauges / labels / maps.
HARD = "absolutely no readable text, no numbers, no letters, no user interface, no app screen, no news graphics, no maps with labels, no watermark, no logos"

D = "2026-07-13"
JOBS = [
    # 1 · basra-water-rationing (P1 — driest since 1933, Basra on water tankers, Turkey dams)
    (f"{D}-basra-water-rationing", "hero.jpg", f"A vast cracked dry riverbed under a harsh white sun, deep fissures in the parched clay, a couple of small wooden fishing boats stranded on the baked earth where a river once flowed, severe drought in southern Iraq, cinematic editorial wide shot, {HARD}, {NEG}"),
    (f"{D}-basra-water-rationing", "broll_1.jpg", f"A high aerial view of a severely shrunken river snaking through parched brown land with wide exposed sandbars, low water level, sun-baked landscape, drought documentary aerial shot, {HARD}, {NEG}"),
    (f"{D}-basra-water-rationing", "broll_2.jpg", f"A blue water tanker truck filling household plastic water containers on a dusty residential street in Basra, people carrying jugs from behind with no clear faces, daily water delivery in a water-scarce city, gritty documentary photojournalism, no faces visible, {HARD}, {NEG}"),
    (f"{D}-basra-water-rationing", "broll_3.jpg", f"A large upstream concrete hydroelectric dam holding back a big reservoir in a rugged mountainous region, controlled water release through the spillway, upstream control of river flow, industrial editorial wide shot, {HARD}, {NEG}"),
    # 2 · congo-fever-outbreak (P3 — CCHF 145 cases, livestock/tick vector, slaughter-season inspection)
    (f"{D}-congo-fever-outbreak", "hero.jpg", f"A calm warm-toned hospital isolation ward, a masked medical worker in full PPE and gloves standing beside an empty patient bed with soft window light, seasonal viral fever care, tender medical editorial, no faces clearly visible, {HARD}, {NEG}"),
    (f"{D}-congo-fever-outbreak", "broll_1.jpg", f"A modern clinical laboratory, a gloved technician in PPE holding up a small blood sample vial under cool clinical light, disease surveillance and testing, cinematic medical editorial, no readable text, {NEG}"),
    (f"{D}-congo-fever-outbreak", "broll_2.jpg", f"A rural livestock pen in southern Iraq under hot hazy sun with sheep and cattle crowded together, a herder seen from behind among the animals with no visible face, the animal-to-human disease vector, documentary photojournalism, no faces visible, {HARD}, {NEG}"),
    (f"{D}-congo-fever-outbreak", "broll_3.jpg", f"A clean meat-inspection scene at a slaughterhouse, a health inspector in a white coat and gloves examining hanging carcasses under bright hygienic light, food-safety control during the slaughter season, documentary editorial, no faces clearly visible, {HARD}, {NEG}"),
    # 3 · graft-oil-two-trillion (P1, V11 — 3rd oil official arrest, $20M in water bottles, $2T lost)
    (f"{D}-graft-oil-two-trillion", "hero.jpg", f"An editorial evidence still on a dark table, neat tall stacks of seized US hundred-dollar banknotes and a few gold bars under a hard police spotlight, a major state oil-corruption seizure, {HARD}, {NEG}"),
    (f"{D}-graft-oil-two-trillion", "broll_1.jpg", f"Elite anti-corruption officers in dark tactical gear escorting a detained official out of a government building at dawn, the suspect faceless from behind with hands held behind the back, tense documentary photojournalism, no faces visible, {HARD}, {NEG}"),
    (f"{D}-graft-oil-two-trillion", "broll_2.jpg", f"A police evidence table with US dollar banknotes rolled and stuffed inside clear unlabeled plastic water bottles, an unusual cash-concealment seizure, hard evidence-photo lighting, blank bottles with no readable labels, {HARD}, {NEG}"),
    (f"{D}-graft-oil-two-trillion", "broll_3.jpg", f"A large oil refinery with distillation towers and a bright gas flare at dusk under a somber sky, national oil wealth shadowed by graft, industrial editorial wide shot, {HARD}, {NEG}"),
    # 4 · gulf-energy-fund-iraq (P2 — Gulf energy fund, Chevron+UCC pipeline, export terminals)
    (f"{D}-gulf-energy-fund-iraq", "hero.jpg", f"A gleaming Gulf financial-district skyline of modern glass towers at golden hour, an Iraqi flag on a tall pole in the foreground, a regional investment mood, cinematic editorial wide shot, {HARD}, {NEG}"),
    (f"{D}-gulf-energy-fund-iraq", "broll_1.jpg", f"A formal high-level investment signing room, two business delegations seated across a long polished table with flags standing behind them, figures seen from behind and the side with no clear faces, sovereign-fund diplomacy, editorial, {HARD}, {NEG}"),
    (f"{D}-gulf-energy-fund-iraq", "broll_2.jpg", f"A large crude-oil pipeline under construction stretching across open desert with heavy machinery and distant workers, new energy-export infrastructure, industrial editorial wide shot, no faces visible, {HARD}, {NEG}"),
    (f"{D}-gulf-energy-fund-iraq", "broll_3.jpg", f"An oil export marine terminal with rows of large storage tanks and a moored crude tanker loading at a coastal port at dusk, a diversified export outlet, industrial editorial aerial shot, {HARD}, {NEG}"),
    # 5 · iraq-turkey-pipeline-clock (P1, V11 — ITP treaty ends Jul 27, Ceyhan protocol, halted north exports)
    (f"{D}-iraq-turkey-pipeline-clock", "hero.jpg", f"A massive crude-oil pipeline stretching across a rugged border landscape toward the horizon under a tense dusk sky, a critical cross-border export artery, cinematic editorial wide shot, {HARD}, {NEG}"),
    (f"{D}-iraq-turkey-pipeline-clock", "broll_1.jpg", f"Two empty facing chairs at a bare diplomatic negotiating table in a plain official room with soft grey window light, a stalled treaty negotiation between two states, minimalist editorial still, {HARD}, {NEG}"),
    (f"{D}-iraq-turkey-pipeline-clock", "broll_2.jpg", f"A large Mediterranean oil export port at dusk with rows of storage tanks and a moored crude tanker loading at the jetty, a pipeline terminus by the sea, industrial editorial aerial shot, {HARD}, {NEG}"),
    (f"{D}-iraq-turkey-pipeline-clock", "broll_3.jpg", f"A pipeline pumping and valve station in a desert with large idle shut-off valves and pipework under a grey overcast sky, halted crude flow, industrial documentary mid shot, {HARD}, {NEG}"),
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
    deadline = time.time() + 20 * 60
    while pending and time.time() < deadline:
        time.sleep(POLL_INTERVAL)
        still = []
        for j in pending:
            try:
                r = http_get(f"{STATUS_URL}?taskId={j['tid']}")
            except Exception as e:
                msg = str(e)
                if "402" in msg:
                    print("  !! KIE 402 out-of-credits — aborting, fall back to Pexels/Commons", file=sys.stderr, flush=True)
                    return 2
                still.append(j); continue
            data = r.get("data") or {}
            st = data.get("state")
            if st == "success":
                url = first_image_url(data)
                if not url:
                    print(f"  ? {j['slug']}/{j['file']}: success but no url", file=sys.stderr, flush=True)
                    continue
                try:
                    info = download(url, j["out"])
                    j["ok"] = True
                    print(f"  OK {j['slug']}/{j['file']}  {info}", flush=True)
                except Exception as e:
                    print(f"  ! download {j['slug']}/{j['file']}: {e}", file=sys.stderr, flush=True)
            elif st == "fail":
                print(f"  X {j['slug']}/{j['file']}: fail — {data.get('failMsg','?')}", file=sys.stderr, flush=True)
            else:
                still.append(j)
        pending = still
    ok = sum(1 for j in jobs if j["ok"])
    print(f"\n== Done: {ok}/{len(JOBS)} images ==", flush=True)
    return 0 if ok == len(JOBS) else 1


if __name__ == "__main__":
    sys.exit(main())
