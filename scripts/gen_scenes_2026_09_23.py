#!/usr/bin/env python3
"""Generate the 2026-09-23 slate scenes via KIE Nano Banana Pro (9:16 2K).

EDITORIAL CONSTRAINTS (2026-09-23):

* Seasonal: 23 Sep, still warm in Iraq. Light long sleeves at most. NO winter
  coats, NO heavy jackets, NO scarves-as-winterwear.
* Slug A names two REAL convicted MPs. NO person is depicted in any frame:
  no defendant, no handcuffs, no prisoner, no courtroom dock with a body in it.
  Institutions, empty benches, sealed files and sealed property only.
* Slug B money frames: banknotes edge-on and out of focus ONLY. No
  denomination, portrait, emblem or lettering legible. NO handcuffs over cash.
* Slug C is a scheduled withdrawal, not a battle. No combat, no wreckage, no
  casualties, no readable insignia or flags, no identifiable airframe era-mixing.
* Slug D is a pricing/parliament decision. Pumps, tankers, refinery, empty
  chamber. No legible price boards, no brand livery.
* Slug E is a pollution warning by a committee. Rivers, outfalls, treatment
  plants. No patients, no hospital beds, no visible illness.

Scenes only. No real named individual is ever depicted.
"""
from __future__ import annotations
import sys, time, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, http_get, first_image_url, download, submit  # type: ignore

D = "2026-09-23"

LEAD = "IRAQ, MIDDLE EAST."
NOUI = ("absolutely no user-interface, no app screens, no news graphics, no readable text "
        "on any screen, no phone or tablet UI, no burned-in captions, no price boards")
UP = "upright vertical portrait orientation, level horizon, not rotated, not tilted"
NOFACE = ("no recognisable famous person, anonymous ordinary people, faces turned away or "
          "partially obscured")
NOPEOPLE = "no people at all anywhere in the frame"
BLANK = "all signage and surfaces completely blank, no lettering of any alphabet anywhere"
NOTWEST = ("not American, not European, not East Asian, not South Asian, no Western interiors, "
           "no Latin-script books or signage, warm late-summer clothing, short or light long "
           "sleeves, no winter coats, no heavy jackets")
NOTE_EDGE = ("banknotes stacked edge-on and out of focus so that no denomination, portrait or "
             "lettering is legible anywhere, no coat of arms, no national emblem, no face on any note")
NOMARK = ("no military insignia, no national flag, no unit patch, no tail number, no company logo, "
          "no painted markings of any kind on any vehicle")

JOBS: list[tuple[str, str, str]] = []

# ── A · السجن 7 سنوات لنائبتين بالكسب غير المشروع (P1 corruption · 18:00 LEAD) ──
s = f"{D}-a-two-mps-seven-years"
JOBS += [
    (s, "hero.jpg",
     f"{LEAD} Wide editorial photojournalism shot of the austere stone facade of a central "
     f"courthouse in Baghdad in hard late-afternoon light, tall plain columns, heavy closed double "
     f"doors, broad empty steps, long shadows across the stone, a sense of institutional weight, "
     f"{UP}, {NOPEOPLE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_1.jpg",
     f"{LEAD} Interior of an empty formal courtroom in Iraq, a raised dark wooden judges' bench "
     f"with three empty high-backed chairs, plain panelled wall behind, rows of empty seats in the "
     f"foreground, cool diffuse light from high windows, solemn and completely unoccupied, "
     f"{UP}, {NOPEOPLE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_2.jpg",
     f"{LEAD} Overhead close-up of thick stacks of bound paper case files tied with cord on a dark "
     f"wooden desk in an Iraqi government office, manila folders, a brass seal and an inkpad beside "
     f"them, warm desk lamp light, shallow depth of field, every page completely blank and unreadable, "
     f"{UP}, {NOPEOPLE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_3.jpg",
     f"{LEAD} Exterior of a large empty private villa in an affluent Baghdad district seen through a "
     f"locked ornamental iron gate, chain and padlock on the gate, dusty driveway, shuttered windows, "
     f"palm trees, hard afternoon sun, a sense of seized and abandoned property, "
     f"{UP}, {NOPEOPLE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
]

# ── B · الدولار ينزل تحت 157 + شبكة مضاربة (P1 dollar anchor · 19:45) ──
s = f"{D}-b-dollar-156750-network"
JOBS += [
    (s, "hero.jpg",
     f"{LEAD} Street-level editorial shot of a row of small currency-exchange kiosks on a busy "
     f"Baghdad commercial street in warm late-afternoon light, roll-up shutters half raised, a few "
     f"anonymous men in light shirts walking past, dusty pavement, tangled overhead cables, "
     f"{UP}, {NOFACE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_1.jpg",
     f"{LEAD} Extreme close-up on a money counter's hands at a currency exchange desk, {NOTE_EDGE}, "
     f"thick bundles seen edge-on in shallow focus, a worn wooden counter, warm side light, hands "
     f"only, no face in frame, {UP}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_2.jpg",
     f"{LEAD} A plain unmarked police evidence table in an Iraqi interior-ministry office with "
     f"several ordinary mobile phones laid out in a row beside sealed transparent evidence bags, "
     f"{NOTE_EDGE}, cool overhead fluorescent light, no handcuffs, no weapons, no people, "
     f"{UP}, {NOPEOPLE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_3.jpg",
     f"{LEAD} Close-up inside a gold souk workshop on a Baghdad wholesale street, warm spotlights on "
     f"trays of plain unstamped gold bangles and chains behind polished glass, rich amber reflections, "
     f"shallow depth of field, no people, no price tags, no lettering, "
     f"{UP}, {NOPEOPLE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
]

# ── C · انسحاب القوات الأميركية 30 أيلول + حصر السلاح (P2 · 21:15) ──
s = f"{D}-c-withdrawal-30-september"
JOBS += [
    (s, "hero.jpg",
     f"{LEAD} Wide cinematic shot at dawn of a long column of modern armoured wheeled military "
     f"vehicles driving away from the camera along a straight desert highway in Iraq, dust plumes "
     f"behind them, flat arid plain and low ridges on the horizon, cold blue pre-sunrise light, "
     f"{UP}, {NOMARK}, {NOFACE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_1.jpg",
     f"{LEAD} An emptied military base in the Iraqi desert at first light, rows of bare concrete "
     f"blast walls and empty gravel pads where structures once stood, a bare flagpole with no flag, "
     f"coils of razor wire, long shadows, utterly deserted, "
     f"{UP}, {NOPEOPLE}, {NOMARK}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_2.jpg",
     f"{LEAD} Exterior of a monumental sand-coloured Iraqi government ministry building in Baghdad "
     f"in hard midday sun, symmetrical modernist facade, deep window recesses, tall palms along the "
     f"approach, an empty forecourt, formal and imposing, "
     f"{UP}, {NOPEOPLE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_3.jpg",
     f"{LEAD} A formal empty meeting room in an Iraqi ministry, a long polished wooden table with "
     f"two rows of empty leather chairs facing each other, plain bare walls, no flags and no emblems "
     f"of any country, soft daylight from tall windows, awaiting negotiation, "
     f"{UP}, {NOPEOPLE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
]

# ── D · البرلمان يطالب بإعادة النظر برفع أسعار المشتقات (P1 · 22:30) ──
s = f"{D}-d-fuel-decision-429"
JOBS += [
    (s, "hero.jpg",
     f"{LEAD} Editorial shot of a long queue of ordinary saloon cars and small pickup trucks waiting "
     f"nose to tail at a petrol station forecourt in Iraq in hot hazy late-afternoon light, plain "
     f"unbranded fuel pumps under a simple flat canopy, dusty asphalt, heat shimmer, "
     f"{UP}, {NOFACE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_1.jpg",
     f"{LEAD} Close-up of a fuel nozzle being held into the filler neck of a dusty older saloon car, "
     f"a worker's hand and light sleeve only, no face, plain unbranded nozzle and hose, warm low sun "
     f"flare, shallow depth of field, no numbers or lettering visible anywhere, "
     f"{UP}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_2.jpg",
     f"{LEAD} A line of large unmarked road tanker trucks parked in a dusty depot yard in Iraq at "
     f"golden hour, cylindrical steel tanks, long shadows across gravel, distant refinery towers and "
     f"flare stacks hazy on the horizon, {UP}, {NOPEOPLE}, {NOMARK}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_3.jpg",
     f"{LEAD} Interior of a large empty parliamentary debating chamber in Baghdad, curved tiers of "
     f"empty seats with small desks, a raised speaker's rostrum, warm wood and pale stone, no flags "
     f"and no emblems, soft light from above, completely unoccupied, "
     f"{UP}, {NOPEOPLE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
]

# ── E · تحذير لجنة تلوث دجلة والفرات (P3 health/environment · 23:45 · V10.1 control) ──
s = f"{D}-e-tigris-euphrates-pollution"
JOBS += [
    (s, "hero.jpg",
     f"{LEAD} Wide editorial shot of the Tigris river running through Baghdad in hazy late-afternoon "
     f"light, low murky brown-green water, exposed muddy banks strewn with debris, date palms and "
     f"low buildings along the far shore, a heavy still atmosphere, "
     f"{UP}, {NOPEOPLE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_1.jpg",
     f"{LEAD} Close-up of a large concrete storm and waste outfall pipe discharging grey turbid water "
     f"into a river in Iraq, foam and scum spreading across the surface, stained concrete, reeds at "
     f"the edge, harsh daylight, documentary environmental photojournalism, "
     f"{UP}, {NOPEOPLE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_2.jpg",
     f"{LEAD} A municipal water treatment plant in Iraq seen from above, circular concrete "
     f"sedimentation basins with still water, steel walkways and handrails, dusty ground around the "
     f"perimeter, hard midday sun, industrial and utilitarian, "
     f"{UP}, {NOPEOPLE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_3.jpg",
     f"{LEAD} A farmer's irrigation channel cut through cracked dry earth beside a date palm grove in "
     f"southern Iraq, shallow stagnant water with an oily sheen, wilting crops at the edge, intense "
     f"afternoon light, {UP}, {NOPEOPLE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
]


def main():
    jobs = []
    print(f"== Submitting {len(JOBS)} scene jobs ==", flush=True)
    for slug, fname, prompt in JOBS:
        out = IMG_ROOT / slug / fname
        try:
            tid = submit(prompt)
            jobs.append({"slug": slug, "file": fname, "out": str(out), "tid": tid, "ok": False})
            print(f"  + {slug}/{fname} tid={tid}", flush=True)
        except Exception as e:
            print(f"  ! submit {slug}/{fname}: {e}", file=sys.stderr, flush=True)
        time.sleep(0.4)

    Path("scripts/_kie_jobs_2026_09_23.json").write_text(
        json.dumps([{k: v for k, v in j.items()} for j in jobs], ensure_ascii=False, indent=1))
    print(f"\n[saved job ids -> scripts/_kie_jobs_2026_09_23.json]", flush=True)

    pending = [j for j in jobs if j.get("tid")]
    print(f"== Polling {len(pending)} ==", flush=True)
    deadline = time.time() + 16 * 60
    while pending and time.time() < deadline:
        time.sleep(POLL_INTERVAL)
        still = []
        for j in pending:
            try:
                info = http_get(f"{STATUS_URL}?taskId={j['tid']}")
                url = first_image_url(info)
                if url:
                    op = Path(j["out"]); op.parent.mkdir(parents=True, exist_ok=True)
                    download(url, op)
                    j["ok"] = True
                    print(f"  ✓ {j['slug']}/{j['file']}", flush=True)
                    continue
                st = (info.get("data") or {}).get("state") or ""
                if str(st).lower() in ("fail", "failed", "error"):
                    print(f"  ✗ {j['slug']}/{j['file']} FAILED: {str(info)[:200]}", flush=True)
                    continue
            except Exception as e:
                print(f"  . {j['slug']}/{j['file']} poll: {e}", flush=True)
            still.append(j)
        pending = still
        print(f"  [{len(pending)} pending]", flush=True)

    done = sum(1 for j in jobs if j["ok"])
    print(f"\n== DONE {done}/{len(jobs)} ==", flush=True)
    for j in jobs:
        if not j["ok"]:
            print(f"  MISSING {j['slug']}/{j['file']} tid={j.get('tid')}", flush=True)


if __name__ == "__main__":
    main()
