#!/usr/bin/env python3
"""Generate the 2026-08-31 slate scenes via KIE Nano Banana Pro (9:16 2K).

Prompt shape carried over from 2026-08-17/19/27: lead with IRAQ / MIDDLE EAST,
name the architecture, name the dress, demand completely blank surfaces, add
explicit negatives against Western / East-Asian / South-Asian defaults and
winter clothing.

EDITORIAL CONSTRAINT (2026-08-31): slug A names two men who are ACCUSED AND
DETAINED, not convicted, and V11 renders no «صورة توضيحية» AI chip. Slug A
therefore carries NO depictive imagery of the alleged offence — no cash, no
gold, no handcuffs, no stamps, no safes, no property. Institutions only.
Slug C likewise stages no protest and no crowd: the Basra sit-in is real, but a
synthetic crowd would read as documentary footage of it.

Scenes only. No real named individual is ever depicted.
"""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, http_get, first_image_url, download, submit  # type: ignore

D = "2026-08-31"

LEAD = "IRAQ, MIDDLE EAST."
NOUI = ("absolutely no user-interface, no app screens, no news graphics, no readable text "
        "on any screen, no phone or tablet UI, no burned-in captions")
UP = "upright vertical portrait orientation, level horizon, not rotated, not tilted"
NOFACE = ("no recognisable famous person, anonymous ordinary people, faces turned away or "
          "partially obscured")
BLANK = "all signage and surfaces completely blank, no lettering of any alphabet anywhere"
NOTWEST = ("not American, not European, not East Asian, not South Asian, no Western living rooms, "
           "no Latin-script books or signage, peak summer clothing only, no winter coats, "
           "no scarves, no jackets")
NOTE_EDGE = ("banknotes stacked edge-on and out of focus so that no denomination, portrait or "
             "lettering is legible anywhere")

JOBS: list[tuple[str, str, str]] = []

# ── A · القضاء يضبط أموالاً وعقارات بقضية الجميلي (P1 · فساد · 18:00 LEAD) ──
# Institutions only. Nothing that re-enacts the alleged offence.
s = f"{D}-a-jumaili-office-seizure"
JOBS += [
    (s, "hero.jpg",
     f"{LEAD} Wide editorial photojournalism shot of the exterior of a plain modern Iraqi courthouse and "
     f"judicial complex in Baghdad seen from across a quiet forecourt in hard late-morning sun, "
     f"sand-coloured stone facade with a deep shaded colonnade, concrete blast barriers along the kerb, "
     f"a single bare flagpole, austere institutional architecture, no people in frame, {UP}, {BLANK}, "
     f"{NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_1.jpg",
     f"{LEAD} Interior of an empty formal Iraqi courtroom, a raised wooden judge's bench facing rows of "
     f"plain empty wooden benches, pale institutional walls, cool even daylight from high windows, "
     f"completely deserted, no people at all, wide symmetrical editorial shot, {UP}, {BLANK}, {NOTWEST}, "
     f"{NOUI}, {NEG}"),
    (s, "broll_2.jpg",
     f"{LEAD} Exterior of a large plain government ministry tower in Baghdad photographed from street "
     f"level across a wide empty avenue at midday, repetitive rows of identical windows in a "
     f"sand-coloured concrete facade, dusty palm trees along the kerb, security barriers, austere "
     f"bureaucratic architecture, no people, {UP}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_3.jpg",
     f"{LEAD} Close-up of a tall stack of plain bound paper case folders tied shut with cotton cord "
     f"resting on a worn wooden desk in a dim government office, soft window light from one side, "
     f"shallow depth of field, no hands and no people in frame, absolutely no writing or labels on any "
     f"folder, {BLANK}, {NOUI}, {NEG}"),
]

# ── B · الدولار ثابت لليوم الثاني (P1 · دولار · 19:45) ──
s = f"{D}-b-dollar-flat-second-day"
JOBS += [
    (s, "hero.jpg",
     f"{LEAD} Wide editorial photojournalism shot of a currency exchange shop window in Baghdad seen "
     f"from the customer's side, the money changer's hands resting still on the counter beside two neat "
     f"untouched stacks of banknotes with no customer at the grille, harsh bright summer daylight on the "
     f"glass, short-sleeved summer shirt, a quiet unmoving mood, documentary reportage, {UP}, {NOFACE}, "
     f"{NOTE_EDGE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_1.jpg",
     f"{LEAD} Interior of a small family grocery shop in a Baghdad neighbourhood, the shopkeeper's hands "
     f"arranging tins and packets of imported food on plain metal shelves, completely unlabelled "
     f"packaging, warm afternoon light through the open shopfront, no face in frame, documentary "
     f"reportage, {UP}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_2.jpg",
     f"{LEAD} A small currency exchange kiosk on a clean modern street in Erbil in the Kurdistan Region "
     f"of Iraq, a trader in a light summer shirt seated behind the open window, low-rise city buildings "
     f"and young trees behind, warm late-afternoon sun, wide documentary editorial shot, {UP}, {NOFACE}, "
     f"{NOTE_EDGE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_3.jpg",
     f"{LEAD} A crowded informal currency trading street in central Baghdad in the late morning, dense "
     f"crowd of male traders in short-sleeved shirts standing and talking, low concrete commercial "
     f"buildings with plain blank frontages behind, hot white summer light and dust haze, wide "
     f"documentary editorial shot, {UP}, {NOFACE}, {NOTE_EDGE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
]

# ── C · رواتب آب لم تصل بآخر يوم من الشهر (P1 · مجتمع · 21:15) ──
# No staged protest and no placards: the Basra sit-in is real and a synthetic
# crowd would be read as footage of it.
s = f"{D}-c-salaries-august-last-day"
JOBS += [
    (s, "hero.jpg",
     f"{LEAD} Wide editorial photojournalism shot of a long queue of ordinary Iraqi people waiting on "
     f"the pavement outside a plain bank cash-withdrawal booth in an Iraqi city in hard summer sun, men "
     f"in short-sleeved shirts and women in dark abayas standing patiently in a line that stretches out "
     f"of frame, dusty street and a plain concrete facade behind, {UP}, {NOFACE}, {BLANK}, {NOTWEST}, "
     f"{NOUI}, {NEG}"),
    (s, "broll_1.jpg",
     f"{LEAD} Exterior of a plain Iraqi public university administration building on a river corniche in "
     f"Basra photographed in bright morning light, low modern concrete blocks with rows of shuttered "
     f"windows, dusty palm trees and an empty paved forecourt, wide documentary editorial shot, no "
     f"people, {UP}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_2.jpg",
     f"{LEAD} A family shopping at a busy open-air vegetable and fruit market in Baghdad in the late "
     f"afternoon, a woman in a dark abaya and a man in a short-sleeved shirt choosing produce from piled "
     f"wooden crates, warm low sun and dust in the air, faces turned away from the camera, documentary "
     f"reportage, {UP}, {NOFACE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_3.jpg",
     f"{LEAD} Exterior of a large plain finance ministry office building in Baghdad seen from a wide "
     f"empty avenue in flat midday light, sand-coloured stone and glass, security barriers along the "
     f"forecourt, a bare flagpole, austere institutional architecture, no people, {UP}, {BLANK}, "
     f"{NOTWEST}, {NOUI}, {NEG}"),
]

# ── D · الدين الداخلي 106 تريليون دينار (P1 · اقتصاد كلي · 22:30 · V10.1 SILENT CONTROL) ──
s = f"{D}-d-internal-debt-106"
JOBS += [
    (s, "hero.jpg",
     f"{LEAD} Exterior of a plain modern central bank headquarters tower in Baghdad seen from across a "
     f"wide empty avenue at hard midday sun, sand-coloured stone and glass facade with rows of identical "
     f"windows, concrete blast barriers along the forecourt, a single unmarked flagpole, austere "
     f"institutional architecture, wide editorial shot, no people, {UP}, {BLANK}, {NOTWEST}, {NOUI}, "
     f"{NEG}"),
    (s, "broll_1.jpg",
     f"{LEAD} Interior of a large plain Iraqi commercial bank branch hall in the middle of the day, a "
     f"long row of teller windows behind glass with only one or two distant customers, rows of empty "
     f"steel chairs in the foreground, polished tiled floor, cold fluorescent ceiling light, {UP}, "
     f"{NOFACE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_2.jpg",
     f"{LEAD} Wide aerial establishing shot of central Baghdad along the Tigris river in flat hazy "
     f"daylight, dense low-rise sand-coloured buildings, the river curving through the city, distant "
     f"bridges, heat haze on the horizon, {UP}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_3.jpg",
     f"{LEAD} A stalled unfinished public construction project on the edge of an Iraqi city, a bare grey "
     f"concrete frame of several storeys standing open to the sky with no workers and no machinery, "
     f"weeds growing at the base, rebar protruding from the top floor, flat arid horizon behind, hard "
     f"midday light, wide documentary editorial shot, {UP}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
]

# ── E · ضربة لارك وقفزة النفط وأجواء العراق (P2 · 23:45) ──
# No military hardware of any kind: no warships, no jets, no missiles.
s = f"{D}-e-oil-larak-airspace"
JOBS += [
    (s, "hero.jpg",
     f"{LEAD} Wide cinematic aerial editorial shot of a narrow sea strait between two arid rocky "
     f"coastlines at dawn, deep blue open water, pale barren headlands on both sides, two distant "
     f"cargo vessels as small silhouettes far out in the channel, soft golden haze on the horizon, "
     f"no military vessels of any kind, {UP}, {BLANK}, {NOUI}, {NEG}"),
    (s, "broll_1.jpg",
     f"{LEAD} Wide aerial editorial shot of a single laden crude oil supertanker under way alone in open "
     f"blue water far from any coast, long red and black hull, white deck pipework, a wake trailing "
     f"behind, hard high sun, no other vessels in frame, no military vessels, {UP}, {BLANK}, {NOUI}, "
     f"{NEG}"),
    (s, "broll_2.jpg",
     f"{LEAD} An air traffic control tower at a civilian airport silhouetted against a deep blue "
     f"pre-dawn sky, the glazed control cab lit warmly from inside, empty floodlit apron below with a "
     f"single parked civilian passenger aircraft, quiet and still, completely plain unmarked aircraft "
     f"livery, {UP}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_3.jpg",
     f"{LEAD} Wide editorial shot of a large crude oil storage tank farm and refinery in southern Iraq "
     f"at dusk, rows of identical white cylindrical tanks, pipework and flare stacks behind, flat desert "
     f"horizon and a deep orange sky, no people, {UP}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
]


def main() -> int:
    only = set(sys.argv[1:])
    todo = [(s, f, p) for (s, f, p) in JOBS if not only or s in only]
    jobs = []
    print(f"== Submitting {len(todo)} scene jobs (KIE nano-banana-pro 9:16 2K) ==", flush=True)
    for slug, fname, prompt in todo:
        out = IMG_ROOT / slug / fname
        out.parent.mkdir(parents=True, exist_ok=True)
        try:
            tid = submit(prompt)
            jobs.append({"slug": slug, "file": fname, "out": out, "tid": tid, "ok": False})
            print(f"  + {slug}/{fname} tid={tid}", flush=True)
        except Exception as e:
            print(f"  ! submit {slug}/{fname}: {e}", file=sys.stderr, flush=True)
        time.sleep(0.4)

    pending = [j for j in jobs if j.get("tid")]
    print(f"== Polling {len(pending)} jobs ==", flush=True)
    deadline = time.time() + 14 * 60
    while pending and time.time() < deadline:
        time.sleep(POLL_INTERVAL)
        still = []
        for j in pending:
            try:
                r = http_get(f"{STATUS_URL}?taskId={j['tid']}")
                data = (r or {}).get("data") or {}
                st = str(data.get("state") or "").lower()
                if st == "success":
                    url = first_image_url(data)
                    if url:
                        info = download(url, j["out"])
                        j["ok"] = True
                        print(f"  OK  {j['slug']}/{j['file']}  {info}", flush=True)
                        continue
                    print(f"  ?   {j['slug']}/{j['file']}: success but no url", flush=True)
                    continue
                if st in ("fail", "failed", "error"):
                    print(f"  XX  {j['slug']}/{j['file']} FAILED: {str(data)[:200]}", flush=True)
                    continue
                still.append(j)
            except Exception as e:
                print(f"  ?   {j['slug']}/{j['file']}: {e}", flush=True)
                still.append(j)
        pending = still
        if pending:
            print(f"    ({len(pending)} still generating)", flush=True)

    done = sum(1 for j in jobs if j["ok"])
    print(f"== DONE {done}/{len(jobs)} ==", flush=True)
    for j in jobs:
        if not j["ok"]:
            print(f"   MISSING {j['slug']}/{j['file']}", flush=True)
    return 0 if done == len(jobs) else 1


if __name__ == "__main__":
    raise SystemExit(main())
