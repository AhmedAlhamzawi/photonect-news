#!/usr/bin/env python3
"""Generate the 2026-09-01 slate scenes via KIE Nano Banana Pro (9:16 2K).

Prompt shape carried over from 2026-08-17/19/27/31: lead with IRAQ / MIDDLE EAST,
name the architecture, name the dress, demand completely blank surfaces, add
explicit negatives against Western / East-Asian / South-Asian defaults and
winter clothing.

EDITORIAL CONSTRAINTS (2026-09-01):

* Slug D names two men who have now been SENTENCED (7 years each, Federal
  Integrity Commission, announced Sun 30 Aug).  Conviction is established, but
  V11 still renders no «صورة توضيحية» AI chip, so the slug carries NO depictive
  re-enactment of the offence attached to the named men — no cash piles, no
  gold, no handcuffs, no seized villas.  Institutions only.
* Slug A is a PROPOSED foreign military sale notified to Congress, not a
  delivered aircraft.  No Iraqi-marked helicopter in flight, nothing that reads
  as documentary footage of an aircraft Iraq does not yet own.  Generic
  airframes on the ground, hangars, institutions.
* Slug E must not stage a protest, a salary queue with legible signage, or any
  crowd that would read as documentary footage of a real event.
* Money frames: banknotes edge-on and out of focus ONLY.  Two separate reels
  have previously shipped fabricated / foreign currency (Indian rupees, a
  Saddam-era note).  No denomination, portrait, or lettering may be legible.

Scenes only.  No real named individual is ever depicted.
"""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, http_get, first_image_url, download, submit  # type: ignore

D = "2026-09-01"

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
             "lettering is legible anywhere, no coat of arms, no national emblem, no face on any note")
NOMARK = ("no national roundel, no tail number, no unit insignia, no painted markings of any kind "
          "on any aircraft or vehicle")

JOBS: list[tuple[str, str, str]] = []

# ── A · واشنطن توافق على بيع مروحيات بـ800 مليون دولار (P2 · 18:00 LEAD) ──
# Proposed sale, not delivered aircraft. Ground, hangars, institutions only.
s = f"{D}-a-helicopters-800-million"
JOBS += [
    (s, "hero.jpg",
     f"{LEAD} Wide editorial photojournalism shot of a plain unmarked twin-engine utility helicopter "
     f"parked and powered down on a hot concrete airbase apron in the Iraqi desert at first light, "
     f"rotor blades tied down and drooping, wheel chocks in place, low sand-coloured hangars far "
     f"behind, empty apron, heat haze on the concrete, no people in frame, {UP}, {NOMARK}, {BLANK}, "
     f"{NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_1.jpg",
     f"{LEAD} Interior of a large military maintenance hangar in the Iraqi desert, an unmarked utility "
     f"helicopter with its engine cowlings opened for servicing, a rolling toolbox and a wheeled "
     f"maintenance ladder beside it, shafts of dusty daylight through high windows, cool shadowed "
     f"cavernous space, no people in frame, {UP}, {NOMARK}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_2.jpg",
     f"{LEAD} An older Soviet-era style transport helicopter sitting long-disused at the edge of a "
     f"desert airfield in Iraq, faded weathered paint, dust drifted against the tyres, rotor blades "
     f"tied, scrub grass growing at the wheels, harsh flat midday sun, a mood of obsolescence, "
     f"no people, {UP}, {NOMARK}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_3.jpg",
     f"{LEAD} Exterior of a plain austere government defence ministry building in Baghdad photographed "
     f"from street level across an empty avenue in hard afternoon sun, sand-coloured concrete facade, "
     f"concrete blast barriers along the kerb, a single bare flagpole, dusty palm trees, no people, "
     f"{UP}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
]

# ── B · الدولار يعاود الارتفاع فوق 154 ألفاً (P1 · دولار · 19:45) ──
s = f"{D}-b-dollar-back-above-154"
JOBS += [
    (s, "hero.jpg",
     f"{LEAD} Wide editorial photojournalism shot of a currency exchange shop in Baghdad seen from the "
     f"customer's side of the grille, the money changer's hands counting a fanned bundle held edge-on, "
     f"a second customer waiting behind, harsh bright summer daylight through the shopfront glass, "
     f"short-sleeved summer shirts, busy documentary reportage mood, {UP}, {NOFACE}, {NOTE_EDGE}, "
     f"{BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_1.jpg",
     f"{LEAD} Tight editorial shot of a crowded currency trading street in central Baghdad in hard "
     f"morning sun, men in short-sleeved summer shirts standing in small clusters along a row of small "
     f"exchange booths with completely blank fascias, a dense busy kerbside market mood, faces turned "
     f"away from camera, {UP}, {NOFACE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_2.jpg",
     f"{LEAD} A currency exchange counter in a modern shopping arcade in Erbil, Kurdistan Region of "
     f"Iraq, clean bright interior with polished stone floor, a single teller's hands resting beside "
     f"two neat stacks of banknotes turned edge-on, cool even indoor lighting, calm and orderly mood, "
     f"contrast with a crowded street market, no face in frame, {UP}, {NOFACE}, {NOTE_EDGE}, {BLANK}, "
     f"{NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_3.jpg",
     f"{LEAD} Extreme close-up of a pair of hands passing a thin folded bundle of banknotes across a "
     f"worn wooden counter, the notes held tightly edge-on and heavily out of focus, warm shallow "
     f"depth of field, dim interior light, no faces, no legible currency detail whatsoever, "
     f"{NOTE_EDGE}, {BLANK}, {NOUI}, {NEG}"),
]

# ── C · الصادرات اليابانية إلى العراق (P3 · V10.1 SILENT CONTROL · 21:15) ──
s = f"{D}-c-japan-exports-83-million"
JOBS += [
    (s, "hero.jpg",
     f"{LEAD} Wide editorial photojournalism shot of a large open-air imported car lot on the outskirts "
     f"of Baghdad, long neat rows of identical plain silver and white saloon cars parked nose-to-tail "
     f"under a hazy white summer sky, dusty gravel ground, a low breeze-block wall behind, no people, "
     f"absolutely no badges, no emblems, no number plates and no manufacturer marks on any vehicle, "
     f"{UP}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_1.jpg",
     f"{LEAD} Wide shot of a container terminal at Umm Qasr port in southern Iraq, stacks of plain "
     f"unmarked shipping containers in faded red and blue, a tall gantry crane above the quay, flat "
     f"grey Gulf water beyond, hazy humid light, industrial scale, no people, absolutely no shipping "
     f"line names or lettering on any container, {UP}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_2.jpg",
     f"{LEAD} A car transporter truck loaded with a double deck of plain unmarked saloon cars driving "
     f"along a dusty desert highway in Iraq under a bleached midday sky, flat scrub desert either side, "
     f"heat shimmer on the tarmac, editorial documentary shot from the roadside, no badges, no number "
     f"plates, no lettering on the truck, {UP}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_3.jpg",
     f"{LEAD} Interior of a spare-parts warehouse in Baghdad, tall steel racking filled with stacked "
     f"black rubber tyres and plain cardboard boxes of unlabelled automotive parts, a concrete floor, "
     f"cool fluorescent light from above, one worker in a short-sleeved shirt seen from behind at the "
     f"far end of the aisle, {UP}, {NOFACE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
]

# ── D · السجن 7 سنوات بقضية الكسب غير المشروع (P1 · فساد · 22:30) ──
# Sentenced, but institutions only: no re-enactment of the offence.
s = f"{D}-d-graft-seven-years"
JOBS += [
    (s, "hero.jpg",
     f"{LEAD} Wide editorial photojournalism shot of the exterior of a plain modern Iraqi courthouse in "
     f"Baghdad seen from across a quiet forecourt in hard late-afternoon sun, sand-coloured stone "
     f"facade with a deep shaded colonnade, concrete blast barriers along the kerb, long raking "
     f"shadows, austere institutional architecture, no people in frame, {UP}, {BLANK}, {NOTWEST}, "
     f"{NOUI}, {NEG}"),
    (s, "broll_1.jpg",
     f"{LEAD} Interior of an empty formal Iraqi courtroom, a raised wooden judge's bench facing rows of "
     f"plain empty wooden benches, pale institutional walls, cool even daylight from high windows, "
     f"completely deserted, no people at all, wide symmetrical editorial shot, {UP}, {BLANK}, "
     f"{NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_2.jpg",
     f"{LEAD} A single empty steel-framed chair standing alone inside a bare institutional holding room "
     f"with pale painted walls and a polished concrete floor, one high barred window casting a hard "
     f"rectangle of light across the floor, stark and austere, absolutely no people, {UP}, {BLANK}, "
     f"{NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_3.jpg",
     f"{LEAD} Close-up of a tall stack of plain bound paper case folders tied shut with cotton cord "
     f"resting on a worn wooden desk in a dim government office, soft window light from one side, "
     f"shallow depth of field, no hands and no people in frame, absolutely no writing or labels on any "
     f"folder, {BLANK}, {NOUI}, {NEG}"),
]

# ── E · خاما البصرة يقفزان فوق 80 دولاراً (P1 · نفط ورواتب · 23:45) ──
s = f"{D}-e-basra-crude-above-80"
JOBS += [
    (s, "hero.jpg",
     f"{LEAD} Wide aerial editorial shot of an offshore crude oil loading terminal in the northern "
     f"Arabian Gulf off Basra at dawn, a long steel jetty and mooring buoys reaching into calm "
     f"steel-blue water, a single large tanker made fast alongside, pale gold horizon haze, industrial "
     f"scale, no people, no lettering on the hull, {UP}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_1.jpg",
     f"{LEAD} Rows of large crude oil storage tanks and a lattice of pipework in the flat desert of "
     f"southern Iraq under a bleached white midday sky, dusty haze, heat shimmer, austere industrial "
     f"geometry, no people, absolutely no lettering or numbering on any tank, {UP}, {BLANK}, "
     f"{NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_2.jpg",
     f"{LEAD} Extreme close-up of a heavy rusted red pipeline valve wheel and flange assembly at an "
     f"oil facility in southern Iraq, peeling paint and desert dust caught in the threads, hard "
     f"directional afternoon sun, shallow depth of field, no people, no lettering or gauges with "
     f"readable numbers, {UP}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_3.jpg",
     f"{LEAD} Interior of a quiet Iraqi bank branch in Baghdad, a row of empty teller windows with "
     f"blank fascias, worn tiled floor, a few plastic waiting chairs standing empty, cool fluorescent "
     f"light, an air of waiting with almost nobody there, one person seen from behind at the far "
     f"counter, {UP}, {NOFACE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
]


def main() -> int:
    only = set(sys.argv[1:])
    jobs = [j for j in JOBS if not only or j[0] in only or f"{j[0]}/{j[1]}" in only]
    print(f"submitting {len(jobs)} jobs")
    live: list[tuple[str, str, str]] = []
    for slug, name, prompt in jobs:
        try:
            tid = submit(prompt)
            live.append((slug, name, tid))
            print(f"  + {slug}/{name} -> {tid}")
        except Exception as e:  # noqa: BLE001
            print(f"  ! {slug}/{name} submit FAILED: {e}")
        time.sleep(0.6)

    pending = dict(((s, n), t) for s, n, t in live)
    done: dict[tuple[str, str], str] = {}
    deadline = time.time() + 16 * 60
    while pending and time.time() < deadline:
        time.sleep(POLL_INTERVAL)
        for key in list(pending):
            tid = pending[key]
            try:
                r = http_get(f"{STATUS_URL}?taskId={tid}")
            except Exception:
                continue
            data = r.get("data") or {}
            state = (data.get("state") or data.get("status") or "").lower()
            if state in ("success", "succeeded", "completed"):
                url = first_image_url(data)
                if not url:
                    print(f"  ! {key} success but no url")
                    pending.pop(key, None)
                    continue
                slug, name = key
                out = IMG_ROOT / slug / name
                out.parent.mkdir(parents=True, exist_ok=True)
                try:
                    info = download(url, out)
                    done[key] = info
                    print(f"  ok {slug}/{name} {info}")
                except Exception as e:  # noqa: BLE001
                    print(f"  ! {key} download failed: {e}")
                pending.pop(key, None)
            elif state in ("fail", "failed", "error"):
                print(f"  ! {key} FAILED: {data.get('failMsg') or data}")
                pending.pop(key, None)
        print(f"  ... {len(pending)} pending, {len(done)} done")

    print(f"\ndone={len(done)} pending={len(pending)} of {len(jobs)}")
    for key in pending:
        print(f"  TIMEOUT {key}")
    return 0 if not pending else 1


if __name__ == "__main__":
    raise SystemExit(main())
