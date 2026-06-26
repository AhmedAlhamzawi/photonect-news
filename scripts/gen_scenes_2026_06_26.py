#!/usr/bin/env python3
"""Generate AI scenes for the 2026-06-26 slate via Nano Banana Pro 9:16 2K.
One still per beat — no cycling. The only real face (Rafael Grossi) is fetched
separately into iran-iaea-inspections/broll_1.jpg."""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

D = "2026-06-26"
X = "absolutely no on-screen text, no Arabic or English writing, no captions, no Instagram or app UI, no fake screenshots, no scoreboard graphics, no watermark, no logos, no brand marks, no garbled characters"

JOBS = [
    # 1. TELESURGERY — operating room + robotic console + fiber link + reach
    (f"{D}-telesurgery-athens-wuhan", "hero.jpg", f"Upright vertical portrait photo, correct orientation not rotated. A high-tech modern operating room seen from a normal eye-level standing viewpoint, a multi-armed robotic surgical system over a draped patient, surgical team in blue scrubs standing upright around the table, cool clinical blue light, sterile and precise, wide cinematic establishing shot, {NEG}, {X}"),
    (f"{D}-telesurgery-athens-wuhan", "broll_1.jpg", f"A surgeon seated at a robotic surgery control console gripping hand controllers and looking into a viewer, focused expression, glowing monitors behind in a dim control room, cinematic close shot, no readable text on screens, {NEG}, {X}"),
    (f"{D}-telesurgery-athens-wuhan", "broll_2.jpg", f"An abstract glowing visualization of fast fiber-optic light streams arcing between two distant points across a dark blue stylized globe, instant data transmission concept, deep blue and teal tech aesthetic, no labels, {NEG}, {X}"),
    (f"{D}-telesurgery-athens-wuhan", "broll_3.jpg", f"A sleek modern hospital building exterior at twilight with warm lit windows and a calm clean plaza, healthcare reaching far, wide cinematic establishing shot, {NEG}, {X}"),
    # 2. IRAQ FISCAL CRISIS — central bank, budget hall, banknotes, money market
    (f"{D}-iraq-fiscal-crisis", "hero.jpg", f"A modern central bank tower and government financial district in Baghdad Iraq under a tense overcast sky, austere institutional architecture, wide documentary establishing shot, {NEG}, {X}"),
    (f"{D}-iraq-fiscal-crisis", "broll_1.jpg", f"An austere empty government finance hall in Iraq with rows of seats and a long official table, dim solemn light, sense of fiscal stalemate, wide documentary shot, {NEG}, {X}"),
    (f"{D}-iraq-fiscal-crisis", "broll_2.jpg", f"A close macro shot of dense stacks of blank illegible banknotes piling up under cool light, currency printing and cash liquidity concept, shallow depth of field, no readable text on the notes, {NEG}, {X}"),
    (f"{D}-iraq-fiscal-crisis", "broll_3.jpg", f"A busy Middle Eastern currency exchange money-changer street stall with bundles of cash and a tense customer, declining-currency mood, documentary wide shot, no readable text, {NEG}, {X}"),
    # 3. WORLD CUP ARAB TEAMS — stadium, fans, two match moments
    (f"{D}-worldcup-arab-teams", "hero.jpg", f"A packed football stadium at night under bright floodlights with a vast sea of cheering fans and waving flags, electric celebratory atmosphere, wide cinematic establishing shot, {NEG}, {X}"),
    (f"{D}-worldcup-arab-teams", "broll_1.jpg", f"Jubilant football supporters in stadium stands waving plain colorful scarves and flags, faces lit with joy, vibrant crowd energy, dynamic wide shot, no specific team logos, {NEG}, {X}"),
    (f"{D}-worldcup-arab-teams", "broll_2.jpg", f"Footballers in plain red kit celebrating a goal on a floodlit green pitch, arms raised in triumph, dynamic action sports photography, motion energy, no logos, {NEG}, {X}"),
    (f"{D}-worldcup-arab-teams", "broll_3.jpg", f"A tense football match moment under bright floodlights, a player in plain green kit striking the ball toward goal, grass flying, dramatic sports action shot, no logos, {NEG}, {X}"),
    # 4. IRAN IAEA INSPECTIONS — podium, diplomatic room, nuclear facility (broll_1 = real Grossi, fetched)
    (f"{D}-iran-iaea-inspections", "hero.jpg", f"A formal international press-conference podium lined with microphones and plain unmarked flags on stands, empty institutional hall, soft cool daylight, no people, cinematic establishing shot, no readable text, {NEG}, {X}"),
    (f"{D}-iran-iaea-inspections", "broll_2.jpg", f"An elegant empty international conference room with a long polished wooden table, neutral unmarked flags on stands, rows of chairs, soft daylight through tall windows, calm institutional diplomatic setting, no people, no readable text, {NEG}, {X}"),
    (f"{D}-iran-iaea-inspections", "broll_3.jpg", f"A distant view of a large nuclear power facility with tall cooling towers and a containment dome under a grey overcast sky, neutral documentary wide shot, no labels, {NEG}, {X}"),
    # 5. CARMEL CAVE PREHISTORY — cave, tools, dig, ancient era
    (f"{D}-carmel-cave-prehistory", "hero.jpg", f"A dramatic prehistoric limestone cave interior with shafts of daylight streaming through a collapsed roof opening, floating dust motes, rugged stone walls, cinematic archaeological atmosphere, {NEG}, {X}"),
    (f"{D}-carmel-cave-prehistory", "broll_1.jpg", f"A close detailed shot of ancient stone hand-axe tools and weathered animal bones resting on a dusty cave floor, warm excavation light, archaeological discovery mood, {NEG}, {X}"),
    (f"{D}-carmel-cave-prehistory", "broll_2.jpg", f"An archaeological excavation in progress with a measured grid, sorted stone artifacts and bone fragments laid out on cloth, brushes and tools, documentary overhead light, no readable text, {NEG}, {X}"),
    (f"{D}-carmel-cave-prehistory", "broll_3.jpg", f"A small prehistoric campfire glowing warmly at dusk in a rocky Levantine hill landscape, early human era atmosphere, no visible faces, cinematic wide shot, {NEG}, {X}"),
    # 6. RIYADH AIR LAUNCH — purple-tail jet, gate, apron, hub
    (f"{D}-riyadh-air-launch", "hero.jpg", f"A sleek modern twin-engine widebody jet airliner with a deep purple tail climbing against a golden sunset sky, clean elegant aviation photography, dynamic wide shot, no airline logos or text, {NEG}, {X}"),
    (f"{D}-riyadh-air-launch", "broll_1.jpg", f"A modern widebody jet airliner parked at an airport gate at dawn with a jet bridge connected and a gleaming glass terminal behind, departure mood, wide establishing shot, no logos or text, {NEG}, {X}"),
    (f"{D}-riyadh-air-launch", "broll_2.jpg", f"A modern airport apron in clear daylight with a widebody Dreamliner-style aircraft being serviced by ground crew and equipment, busy aviation operations, wide documentary shot, no logos or text, {NEG}, {X}"),
    (f"{D}-riyadh-air-launch", "broll_3.jpg", f"A gleaming modern airport terminal interior in Riyadh with travelers walking through bright contemporary architecture, global aviation hub mood, wide shot, no readable text, {NEG}, {X}"),
]


def submit_retry(prompt, tries=5):
    last = None
    for i in range(tries):
        try:
            return submit(prompt)
        except Exception as e:
            last = e
            time.sleep(3 * (i + 1))
    raise last


def main():
    jobs = []
    print(f"== Submitting {len(JOBS)} scene jobs (skip existing) ==", flush=True)
    for slug, fname, prompt in JOBS:
        out = IMG_ROOT / slug / fname
        if out.exists() and out.stat().st_size > 50_000:
            print(f"  = skip {slug}/{fname} (already on disk)", flush=True)
            continue
        try:
            tid = submit_retry(prompt)
            jobs.append({"slug": slug, "file": fname, "out": out, "tid": tid, "ok": False})
            print(f"  + {slug}/{fname} tid={tid}", flush=True)
        except Exception as e:
            print(f"  ! submit {slug}/{fname}: {e}", file=sys.stderr, flush=True)
        time.sleep(0.8)
    if not jobs:
        print("== nothing to generate; all on disk ==", flush=True)
        return 0
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
            data = r.get("data") or {}
            st = data.get("state")
            if st == "success":
                url = first_image_url(data)
                if not url:
                    continue
                try:
                    info = download(url, j["out"]); j["ok"] = True
                    print(f"  ✓ {j['slug']}/{j['file']} {info}", flush=True)
                except Exception as e:
                    print(f"  ! dl retry {j['slug']}/{j['file']}: {e}", file=sys.stderr, flush=True)
                    still.append(j)
            elif st == "fail":
                print(f"  ✗ {j['slug']}/{j['file']} FAIL {str(data)[:160]}", file=sys.stderr, flush=True)
            else:
                still.append(j)
        pending = still
        print(f"  ... {len(pending)} pending", flush=True)
    ok = sum(1 for j in jobs if j["ok"])
    print(f"\n== DONE {ok}/{len(JOBS)} scenes ==", flush=True)
    for j in jobs:
        if not j["ok"]:
            print(f"  MISSING {j['slug']}/{j['file']}", flush=True)
    return 0 if ok == len(JOBS) else 1


if __name__ == "__main__":
    sys.exit(main())
