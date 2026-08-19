#!/usr/bin/env python3
"""Generate the 2026-08-19 slate scenes via KIE Nano Banana Pro (9:16 2K).

KIE credits were restored (balance read 723.5 at submission, up from -5.5 since
27 July), so this slate returns to the PRIMARY image path — no Higgsfield, no stock.

Hardened prompt shape carried over from 2026-08-17, which hit 20/20 first-pass
acceptance: lead with IRAQ / MIDDLE EAST, name the architecture, name the dress,
name the currency, demand completely blank surfaces, and add explicit negatives
against the American / European / East-Asian / South-Asian defaults and winter
clothing.

Scenes only. No real named individual is ever depicted — a synthetic frame beside
a named accused person reads as an evidence photograph (2026-08-17 blocker), and
V11 draws no «صورة توضيحية» chip at all.
"""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, http_get, first_image_url, download, submit  # type: ignore

D = "2026-08-19"

# ── hardened negative / framing constants ────────────────────────────────────
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

JOBS: list[tuple[str, str, str]] = []

# ── 1 · DOLLAR ANCHOR — the shop price breaks 155,000 (P1 dinar · 19:45) ─────
s = f"{D}-dollar-shops-155"
JOBS += [
    (s, "hero.jpg",
     f"{LEAD} Wide editorial photojournalism shot of a currency exchange shop counter in Baghdad, "
     f"a money changer's hands pushing a thick banded brick of Iraqi dinar banknotes across a worn "
     f"glass counter toward a customer, bundles of notes stacked behind the grille, harsh bright "
     f"summer daylight coming through the shopfront, short-sleeved summer shirts, "
     f"documentary reportage, {UP}, {NOFACE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_1.jpg",
     f"{LEAD} A crowded informal currency trading street in central Baghdad at mid-morning, dense "
     f"crowd of male traders in short-sleeved shirts standing shoulder to shoulder holding fans of "
     f"banknotes, low concrete commercial buildings with plain blank frontages behind, hot white "
     f"summer light and dust haze, wide documentary editorial shot, {UP}, {NOFACE}, {BLANK}, "
     f"{NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_2.jpg",
     f"{LEAD} A small currency exchange kiosk on a street in Erbil in the Kurdistan Region of Iraq, "
     f"a trader in a light summer shirt seated behind the open window with neat stacks of banknotes "
     f"on the ledge, modern low-rise city street behind, warm late-afternoon sun, wide documentary "
     f"editorial shot, {UP}, {NOFACE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_3.jpg",
     f"{LEAD} Extreme close-up of two hands counting a fan of Iraqi dinar banknotes over a plain "
     f"dark counter, a smaller folded stack of United States one-hundred-dollar bills resting "
     f"beside them, shallow depth of field, dramatic side light, no faces in frame, {BLANK}, "
     f"{NOUI}, {NEG}"),
]

# ── 2 · TRANSPORT — office director detained over the turned-back plane (P1 corruption · LEAD) ──
# NOTE: no individual is named in any source (only "مدير مكتب الوزير" and "ضابط عمليات الطيران"),
# and the order is TAWQEEF (detention), not conviction. NO courtroom, NO handcuffs, NO judge,
# NO person in a dock — a synthetic frame must never visually assert a verdict.
s = f"{D}-airport-plane-returned"
JOBS += [
    (s, "hero.jpg",
     f"{LEAD} Wide editorial photojournalism shot of a white commercial passenger jet airliner stationary "
     f"on an airport taxiway at dusk under heat haze, engines idle, empty apron and low desert horizon "
     f"beyond the perimeter, air-stairs still parked at the forward door, completely plain unmarked white "
     f"fuselage and blank tail fin, moody blue-gold light, {UP}, {BLANK}, {NOUI}, {NEG}"),
    (s, "broll_1.jpg",
     f"{LEAD} An empty airport departure gate lounge at night, rows of vacant seats facing a wall of "
     f"windows with a parked aircraft silhouette outside, one abandoned suitcase standing alone in the "
     f"foreground, cold fluorescent overhead light, nobody present, stillness and delay, wide documentary "
     f"editorial shot, {UP}, {BLANK}, {NOUI}, {NEG}"),
    (s, "broll_2.jpg",
     f"{LEAD} Bright airport terminal departures hall in full daylight, travellers with luggage trolleys "
     f"queueing at a long row of check-in counters, tall glass windows flooding the polished floor with "
     f"hard white sunlight, high clean ceiling, busy but orderly, wide documentary editorial shot, {UP}, "
     f"{NOFACE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_3.jpg",
     f"{LEAD} Exterior of a plain modern Iraqi government courthouse building with a flat sand-coloured "
     f"stone facade, concrete blast barriers and an empty forecourt in front, a single flagpole with no "
     f"flag, hard midday summer sun casting sharp shadows, nobody present, austere institutional "
     f"architecture, wide editorial shot, {UP}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
]

# ── 3 · FARMERS AT THE FINANCE MINISTRY — 350bn refused, wheat at 850k (P1 wallet) ─────
# Peaceful sit-in only. The source reports friction; a generated frame must not stage violence.
s = f"{D}-farmers-wheat-850-HELD"
JOBS += [
    (s, "hero.jpg",
     f"{LEAD} Wide editorial photojournalism shot of a large crowd of Iraqi farmers in plain long "
     f"traditional dishdasha robes and keffiyeh head cloths sitting and standing in a peaceful open-air "
     f"sit-in on a wide city street in Baghdad, blocking the road in front of a large plain government "
     f"ministry building, hot white summer daylight, dust haze, calm determined mood, no violence, "
     f"documentary reportage, {UP}, {NOFACE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_1.jpg",
     f"{LEAD} Extreme close-up of weathered farmer's hands cupped and overflowing with golden wheat "
     f"grains, more grain spilling between the fingers back into an open jute sack below, warm low "
     f"sunlight, shallow depth of field, no face in frame, {BLANK}, {NOUI}, {NEG}"),
    (s, "broll_2.jpg",
     f"{LEAD} A convoy of heavily loaded grain lorries heaped with wheat queuing on a dirt road outside "
     f"a large concrete grain silo complex in central Iraq, flat arid farmland and palm trees on the "
     f"horizon, harsh midday sun and dust, wide documentary editorial shot, {UP}, {BLANK}, {NOTWEST}, "
     f"{NOUI}, {NEG}"),
    (s, "broll_3.jpg",
     f"{LEAD} A lone Iraqi farmer in a long dishdasha standing at the edge of a harvested wheat field at "
     f"golden hour seen from behind, stubble rows stretching to a flat horizon, a distant tractor "
     f"silhouette, warm dust in the low sun, quiet and burdened mood, {UP}, {NOFACE}, {BLANK}, "
     f"{NOTWEST}, {NOUI}, {NEG}"),
]

# ── 4 · GHALIBAF IN BAGHDAD / SEPT 30 DEADLINE (P2 · V10.1 silent control) ────
# No depiction of any named politician, and no depiction of armed non-state groups.
s = f"{D}-ghalibaf-baghdad-deadline"
JOBS += [
    (s, "hero.jpg",
     f"{LEAD} Wide editorial photojournalism shot of an official state arrival on an airport tarmac in "
     f"Baghdad at midday, a white government aircraft with completely blank unmarked livery parked with "
     f"air-stairs down, a red carpet laid on hot asphalt and a receiving line of distant anonymous "
     f"officials in dark suits seen from far behind, heat shimmer, {UP}, {NOFACE}, {BLANK}, {NOUI}, {NEG}"),
    (s, "broll_1.jpg",
     f"{LEAD} A formal bilateral meeting room, two rows of empty upholstered chairs facing each other "
     f"across a low table with water glasses, the flag of Iraq and the flag of Iran standing on separate "
     f"poles at the head of the room, soft daylight through tall curtains, nobody present, wide editorial "
     f"interior shot, {UP}, {BLANK}, {NOUI}, {NEG}"),
    (s, "broll_2.jpg",
     f"{LEAD} The golden dome and twin minarets of a great Shia shrine in Karbala in southern Iraq rising "
     f"above the pilgrimage courtyard at golden hour, ornate tilework, wide crowds of pilgrims reduced to "
     f"distant anonymous figures below, warm dusty light, wide editorial establishing shot, {UP}, "
     f"{NOFACE}, {BLANK}, {NOUI}, {NEG}"),
    (s, "broll_3.jpg",
     f"{LEAD} An Iraqi army checkpoint on a wide Baghdad avenue at dusk, concrete blast walls and a "
     f"lowered barrier, two soldiers in plain desert camouflage standing with their backs to camera, tail "
     f"lights of waiting cars queued behind, dust and warm low sun, documentary reportage, {UP}, "
     f"{NOFACE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
]

# ── 5 · ONE WEEK FOR THE BARRELS / SALARIES (P1 fiscal) ──────────────────────
s = f"{D}-oil-week-salaries"
JOBS += [
    (s, "hero.jpg",
     f"{LEAD} Wide cinematic aerial editorial shot of a crude oil export terminal on the Gulf coast of "
     f"southern Iraq at golden hour, a laden supertanker moored alongside a long jetty with loading arms "
     f"connected, a tank farm of white storage tanks on the shore behind, calm sea, hazy warm light, "
     f"{UP}, {BLANK}, {NOUI}, {NEG}"),
    (s, "broll_1.jpg",
     f"{LEAD} A long dense queue of Iraqi public-sector employees waiting to collect pay at a government "
     f"cashier window inside a plain bureaucratic hall, men in short-sleeved shirts and women in dark "
     f"abayas standing in line under fluorescent light, worn tiled floor, patient tired mood, documentary "
     f"photojournalism, {UP}, {NOFACE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_2.jpg",
     f"{LEAD} Close-up of a cluster of large weathered red and steel crude oil manifold valves and "
     f"pressure gauges at a desert pumping station, peeling paint and heavy pipework, hard directional "
     f"sunlight, industrial detail photography, {BLANK}, {NOUI}, {NEG}"),
    (s, "broll_3.jpg",
     f"{LEAD} Exterior of a large plain modern Iraqi government finance ministry building at dusk, "
     f"sand-coloured concrete facade with rows of identical windows, concrete blast barriers along the "
     f"empty forecourt, deep blue evening sky, nobody present, austere institutional architecture, wide "
     f"editorial shot, {UP}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
]

# ── 6 · BASRA STADIUM AS AN ASIAN HOME GROUND (P3 sport / pride) ─────────────
s = f"{D}-stadium-basra-asia"
JOBS += [
    (s, "hero.jpg",
     f"{LEAD} Wide cinematic exterior shot of a large modern football stadium in Basra in southern Iraq "
     f"at dusk, its outer shell wrapped in a woven palm-frond-inspired lattice facade glowing warm gold, "
     f"floodlight towers lit above, palm trees and open plaza in the foreground, deep blue evening sky, "
     f"editorial architecture photography, {UP}, {BLANK}, {NOUI}, {NEG}"),
    (s, "broll_1.jpg",
     f"{LEAD} A packed football stadium crowd of Iraqi supporters at night celebrating, arms raised, "
     f"waving plain unmarked flags and scarves with no lettering or emblems, brilliant floodlights and "
     f"drifting smoke above the stand, wide editorial sports photography, {NOFACE}, {BLANK}, {NOTWEST}, "
     f"{NOUI}, {NEG}"),
    (s, "broll_2.jpg",
     f"{LEAD} A pristine empty floodlit football pitch at night seen from a high corner of the stand, "
     f"perfect green turf with mown stripes, white line markings, empty seats in shadow around it, "
     f"dramatic pools of stadium light, wide editorial shot, {UP}, {BLANK}, {NOUI}, {NEG}"),
    (s, "broll_3.jpg",
     f"{LEAD} Wide cinematic daylight shot of a large modern football stadium in Basra in southern Iraq "
     f"under a bright clear blue sky, its woven palm-frond-inspired lattice facade catching hard white "
     f"midday sun, tall palm trees and a broad sunlit plaza in front, supporters walking toward the gates "
     f"in summer clothing, {UP}, {NOFACE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
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
                        print(f"  ✓ {j['slug']}/{j['file']}  {info}", flush=True)
                        continue
                    print(f"  ? {j['slug']}/{j['file']}: success but no url", flush=True)
                    continue
                if st in ("fail", "failed", "error"):
                    print(f"  ✗ {j['slug']}/{j['file']} FAILED: {str(data)[:200]}", flush=True)
                    continue
                still.append(j)
            except Exception as e:
                print(f"  ? {j['slug']}/{j['file']}: {e}", flush=True)
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
