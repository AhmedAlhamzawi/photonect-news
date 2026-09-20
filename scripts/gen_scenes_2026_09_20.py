#!/usr/bin/env python3
"""Generate the 2026-09-20 slate scenes via KIE Nano Banana Pro (9:16 2K).

Prompt shape carried over from 2026-08-17/19/27/31 and 2026-09-01: lead with
IRAQ / MIDDLE EAST, name the architecture, name the dress, demand completely
blank surfaces, add explicit negatives against Western / East-Asian /
South-Asian defaults.

EDITORIAL CONSTRAINTS (2026-09-20):

* Seasonal: 20 Sep, 964 reports 30-something highs and "autumnal" air. Light
  long sleeves at most. NO winter coats, NO scarves, NO heavy jackets.
* Slug A is an EMBASSY TRAVEL ADVISORY about *possible* disruption — not a
  reported cancellation. No departure boards (they would need legible text),
  no stranded-crowd tableaux that read as documentary footage of a real
  cancellation event, no aircraft wreckage, no missiles, no military action.
* Slug B money frames: banknotes edge-on and out of focus ONLY. No
  denomination, portrait, emblem or lettering legible anywhere.
* Slug C is a forecast by an observatory, not a storm happening today. Dust
  and desertification landscapes are fine; no casualty or rescue imagery.
* Slug D is a consumer loan product. Rooftop solar and neighbourhood
  generators; no bank-branded signage, no legible rates.
* Slug E is macro debt data. Institutions and ledgers only; no named person,
  no handcuffs, no seized-cash tableau (nobody is accused of anything).

Scenes only.  No real named individual is ever depicted.
"""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, http_get, first_image_url, download, submit  # type: ignore

D = "2026-09-20"

LEAD = "IRAQ, MIDDLE EAST."
NOUI = ("absolutely no user-interface, no app screens, no news graphics, no readable text "
        "on any screen, no phone or tablet UI, no burned-in captions, no departure boards")
UP = "upright vertical portrait orientation, level horizon, not rotated, not tilted"
NOFACE = ("no recognisable famous person, anonymous ordinary people, faces turned away or "
          "partially obscured")
BLANK = "all signage and surfaces completely blank, no lettering of any alphabet anywhere"
NOTWEST = ("not American, not European, not East Asian, not South Asian, no Western living rooms, "
           "no Latin-script books or signage, warm late-summer early-autumn clothing, short or "
           "light long sleeves, no winter coats, no scarves, no heavy jackets")
NOTE_EDGE = ("banknotes stacked edge-on and out of focus so that no denomination, portrait or "
             "lettering is legible anywhere, no coat of arms, no national emblem, no face on any note")
NOMARK = ("no airline livery, no tail number, no company logo, no painted markings of any kind "
          "on any aircraft or vehicle")

JOBS: list[tuple[str, str, str]] = []

# ── A · تحذير أميركي: احتمال إلغاء رحلات واضطراب سفر (P2 · 18:00 LEAD) ──
s = f"{D}-a-us-warning-flights"
JOBS += [
    (s, "hero.jpg",
     f"{LEAD} Wide editorial photojournalism shot of a quiet airport departures hall in Baghdad in "
     f"hard late-morning light, a handful of travellers with wheeled suitcases spread far apart across "
     f"a polished floor, tall plain glass curtain wall, empty check-in desks with completely blank "
     f"fascias, a mood of uncertainty and waiting, {UP}, {NOFACE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_1.jpg",
     f"{LEAD} A single unmarked white narrow-body passenger jet parked and powered down at a remote "
     f"stand on a hot concrete apron in Iraq, boarding stairs withdrawn, no ground crew, heat haze "
     f"rising off the concrete, flat empty apron stretching away, {UP}, {NOMARK}, {BLANK}, {NOTWEST}, "
     f"{NOUI}, {NEG}"),
    (s, "broll_2.jpg",
     f"{LEAD} Exterior of a plain austere diplomatic compound wall in Baghdad photographed from street "
     f"level in hard afternoon sun, tall sand-coloured concrete blast barriers, coils of razor wire "
     f"along the top, a bare unflagged flagpole behind, dusty palm fronds, empty street, no people, "
     f"{UP}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_3.jpg",
     f"{LEAD} An Iraqi family of travellers seen from behind waiting on a row of airport seats with "
     f"stacked luggage beside them, warm light through a tall window, the woman in a dark abaya, the "
     f"man in a short-sleeved shirt, a child leaning on a suitcase, patient waiting mood, faces not "
     f"visible, {UP}, {NOFACE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
]

# ── B · الدولار اليوم + إشاعة حذف الأصفار (P1 · دولار · 19:45 ANCHOR) ──
s = f"{D}-b-dollar-159750-zero-rumor"
JOBS += [
    (s, "hero.jpg",
     f"{LEAD} Wide editorial photojournalism shot of a currency exchange shop in Baghdad seen from the "
     f"customer's side of the grille, the money changer's hands counting a fanned bundle held edge-on, "
     f"another customer waiting behind, bright daylight through the shopfront glass, short-sleeved "
     f"shirts, busy documentary reportage mood, {UP}, {NOFACE}, {NOTE_EDGE}, {BLANK}, {NOTWEST}, "
     f"{NOUI}, {NEG}"),
    (s, "broll_1.jpg",
     f"{LEAD} Tight editorial shot of a crowded currency trading street in central Baghdad in hard "
     f"morning sun, men in short-sleeved shirts standing in small clusters along a row of small "
     f"exchange booths with completely blank fascias, dense busy kerbside market mood, faces turned "
     f"away from camera, {UP}, {NOFACE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_2.jpg",
     f"{LEAD} An ordinary Iraqi man in a short-sleeved shirt seen from behind at a kitchen table in a "
     f"modest Baghdad home, a small stack of banknotes edge-on in front of him beside a glass of tea, "
     f"warm afternoon light through a shuttered window, a mood of private household worry, face not "
     f"visible, {UP}, {NOFACE}, {NOTE_EDGE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_3.jpg",
     f"{LEAD} A gold jewellery shop window on a busy Baghdad market street in bright daylight, rows of "
     f"plain gold bangles and chains on velvet trays behind glass, warm reflected light, a shopkeeper's "
     f"hands adjusting a tray, no price tags, no lettering, {UP}, {NOFACE}, {BLANK}, {NOTWEST}, "
     f"{NOUI}, {NEG}"),
]

# ── C · 300 يوم عواصف رملية و6 بؤر ساخنة (P3 · 21:15) ──
s = f"{D}-c-sandstorms-300-days"
JOBS += [
    (s, "hero.jpg",
     f"{LEAD} Dramatic wide editorial photojournalism shot of a thick orange dust haze swallowing a "
     f"Baghdad street, low sand-coloured buildings fading into the ochre air a block away, a lone "
     f"figure walking with a hand raised to the face, diffuse sourceless orange light, everything "
     f"coated in fine dust, {UP}, {NOFACE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_1.jpg",
     f"{LEAD} Aerial editorial shot of a vast cracked dried-out lakebed in southern Iraq under a pale "
     f"washed-out sky, polygonal salt-crusted cracks stretching to the horizon, a dead shrub, the "
     f"skeleton of a small wooden boat half buried in the crust, no people, {UP}, {BLANK}, {NOTWEST}, "
     f"{NOUI}, {NEG}"),
    (s, "broll_2.jpg",
     f"{LEAD} Editorial shot of drifted sand burying the lower half of an abandoned mudbrick farmhouse "
     f"in the Iraqi south, dune ripples running up to the doorway, a bare dead palm trunk leaning "
     f"beside it, harsh flat midday desert light, a mood of abandonment, no people, {UP}, {BLANK}, "
     f"{NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_3.jpg",
     f"{LEAD} An elderly Iraqi farmer in a long dishdasha and headscarf seen from behind standing at "
     f"the edge of a cracked bare field in southern Iraq at golden hour, shoulders low, a dry "
     f"irrigation channel running away into dust, face not visible, {UP}, {NOFACE}, {BLANK}, "
     f"{NOTWEST}, {NOUI}, {NEG}"),
]

# ── D · قروض الرشيد 30 مليون دينار للطاقة الشمسية (P1 · كهرباء · 22:30) ──
s = f"{D}-d-solar-loans-30-million"
JOBS += [
    (s, "hero.jpg",
     f"{LEAD} Wide editorial photojournalism shot of a cluster of solar panels newly mounted on the "
     f"flat concrete rooftop of an ordinary Baghdad house in bright late-morning sun, a water tank and "
     f"a satellite dish beside them, densely packed low rooftops stretching to a hazy horizon, no "
     f"people, {UP}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_1.jpg",
     f"{LEAD} Tight editorial shot of a battered neighbourhood diesel generator in a Baghdad "
     f"residential alley, a thick untidy fan of subscriber cables running off it up a leaning pole, "
     f"oil stains on the ground, dust and heat, a mood of makeshift dependence, no people, {UP}, "
     f"{BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_2.jpg",
     f"{LEAD} A technician in a plain work shirt and gloves seen from behind kneeling to bolt a solar "
     f"panel frame onto a rooftop rail in Iraq, tools laid out on the concrete beside him, strong "
     f"sunlight, face not visible, {UP}, {NOFACE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_3.jpg",
     f"{LEAD} Interior of a modest Baghdad living room in the late afternoon lit only by daylight "
     f"through a half-shuttered window, a ceiling fan motionless, a small table lamp switched off, a "
     f"sofa and a patterned rug, a mood of waiting for the power to return, no people, {UP}, {BLANK}, "
     f"{NOTWEST}, {NOUI}, {NEG}"),
]

# ── E · الدين الداخلي 109.5 تريليون دينار (P1 · 23:45 · V10.1 CONTROL) ──
s = f"{D}-e-public-debt-109-trillion"
JOBS += [
    (s, "hero.jpg",
     f"{LEAD} Wide editorial photojournalism shot of an imposing modern central bank tower in Baghdad "
     f"photographed from street level in hard afternoon sun, sheer glass and pale stone facade rising "
     f"against a bleached sky, concrete bollards along the empty kerb, dusty palms, no people, {UP}, "
     f"{BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_1.jpg",
     f"{LEAD} Editorial still life of a heavy old accounting ledger lying open on a wooden desk in a "
     f"dim government office in Baghdad, ruled columns filled with faded handwriting too small to "
     f"read, a brass desk lamp casting a warm pool of light, dust in the air, no people, {UP}, "
     f"{BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_2.jpg",
     f"{LEAD} Interior of a long empty government finance office corridor in Baghdad, closed plain "
     f"doors receding down one side, worn terrazzo floor, fluorescent tubes overhead with one dark, "
     f"an abandoned trolley of stacked paper files, no people, {UP}, {BLANK}, {NOTWEST}, {NOUI}, "
     f"{NEG}"),
    (s, "broll_3.jpg",
     f"{LEAD} Editorial close shot of thick bricks of banknotes stacked edge-on inside an open steel "
     f"bank vault drawer under cold overhead light in Iraq, shallow depth of field, the stacks "
     f"deliberately out of focus, {UP}, {NOTE_EDGE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
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
            print(f"  + {slug}/{name} -> {tid}", flush=True)
        except Exception as e:  # noqa: BLE001
            print(f"  ! {slug}/{name} submit FAILED: {e}", flush=True)
        time.sleep(0.6)

    # Persist task ids BEFORE polling (2026-09-12 lesson: poll/download can 403
    # after a paid submit; without the ids the spend is unrecoverable).
    idfile = Path(__file__).resolve().parent / f"_kie_jobs_{D.replace('-', '_')}.json"
    import json as _json
    idfile.write_text(_json.dumps([{"slug": s, "name": n, "taskId": t} for s, n, t in live],
                                  indent=1), encoding="utf-8")
    print(f"task ids -> {idfile}", flush=True)

    pending = dict(((s, n), t) for s, n, t in live)
    done: dict[tuple[str, str], str] = {}
    deadline = time.time() + 18 * 60
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
                    print(f"  ! {key} success but no url", flush=True)
                    pending.pop(key, None)
                    continue
                slug, name = key
                out = IMG_ROOT / slug / name
                out.parent.mkdir(parents=True, exist_ok=True)
                try:
                    info = download(url, out)
                    done[key] = info
                    print(f"  ok {slug}/{name} {info}", flush=True)
                except Exception as e:  # noqa: BLE001
                    print(f"  ! {key} download failed: {e}", flush=True)
                pending.pop(key, None)
            elif state in ("fail", "failed", "error"):
                print(f"  ! {key} FAILED: {data.get('failMsg') or data}", flush=True)
                pending.pop(key, None)
        print(f"  ... {len(pending)} pending, {len(done)} done", flush=True)

    print(f"\ndone={len(done)} pending={len(pending)} of {len(jobs)}")
    for key in pending:
        print(f"  TIMEOUT {key}")
    return 0 if not pending else 1


if __name__ == "__main__":
    raise SystemExit(main())
