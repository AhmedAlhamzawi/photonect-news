#!/usr/bin/env python3
"""Generate the 2026-08-27 slate scenes via KIE Nano Banana Pro (9:16 2K).

Prompt shape carried over from 2026-08-17/19 (20/20 first-pass acceptance):
lead with IRAQ / MIDDLE EAST, name the architecture, name the dress, name the
currency, demand completely blank surfaces, and add explicit negatives against
the American / European / East-Asian / South-Asian defaults and winter clothing.

Scenes only. No real named individual is ever depicted.
"""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, http_get, first_image_url, download, submit  # type: ignore

D = "2026-08-27"

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

# ── 1 · BANKS — 6.19 trillion dinars left the banking system in H1 (P1 · 18:00 LEAD) ──
s = f"{D}-banks-six-trillion-out"
JOBS += [
    (s, "hero.jpg",
     f"{LEAD} Wide editorial photojournalism shot of the interior of a large plain Iraqi commercial bank "
     f"branch hall in Baghdad in the middle of the day, a long row of teller windows behind glass with "
     f"only one or two distant customers waiting, rows of empty steel chairs in the foreground, polished "
     f"tiled floor, cold fluorescent ceiling light, a deliberate feeling of emptiness and low footfall, "
     f"{UP}, {NOFACE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_1.jpg",
     f"{LEAD} Extreme close-up of a thick banded brick of Iraqi dinar banknotes being lifted out of an "
     f"open domestic floor safe in a home, a hand withdrawing the bundle, dim warm interior light from a "
     f"window, shallow depth of field, no face in frame, the sense of cash leaving an institution for a "
     f"house, {BLANK}, {NOUI}, {NEG}"),
    (s, "broll_2.jpg",
     f"{LEAD} Exterior of a plain modern central bank headquarters tower in Baghdad seen from across a "
     f"wide empty avenue at hard midday sun, sand-coloured stone and glass facade with rows of identical "
     f"windows, concrete blast barriers along the forecourt, a single unmarked flagpole, austere "
     f"institutional architecture, wide editorial shot, {UP}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_3.jpg",
     f"{LEAD} A small family-run shop counter in a Baghdad market street where the owner is counting a "
     f"stack of Iraqi dinar banknotes by hand into a wooden cash drawer, shelves of plain unlabelled "
     f"goods behind, warm dusty afternoon light through the open shopfront, hands and torso only, no face "
     f"in frame, documentary reportage, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
]

# ── 2 · DOLLAR ANCHOR — the shop price is 1,000 lower than eight days ago (P1 · 19:45) ──
s = f"{D}-dollar-shops-week-down"
JOBS += [
    (s, "hero.jpg",
     f"{LEAD} Wide editorial photojournalism shot of a currency exchange shop window in Baghdad seen "
     f"from the customer's side, a money changer's hands sliding a folded stack of United States "
     f"one-hundred-dollar bills through the grille toward the viewer while the other hand rests on a "
     f"brick of Iraqi dinars, harsh bright summer daylight on the glass, short-sleeved summer shirt, "
     f"documentary reportage, {UP}, {NOFACE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_1.jpg",
     f"{LEAD} A crowded informal currency trading street in central Baghdad in the late morning, dense "
     f"crowd of male traders in short-sleeved shirts holding fans of banknotes and gesturing to each "
     f"other, low concrete commercial buildings with plain blank frontages behind, hot white summer "
     f"light and dust haze, wide documentary editorial shot, {UP}, {NOFACE}, {BLANK}, {NOTWEST}, "
     f"{NOUI}, {NEG}"),
    (s, "broll_2.jpg",
     f"{LEAD} A small currency exchange kiosk on a clean modern street in Erbil in the Kurdistan Region "
     f"of Iraq, a trader in a light summer shirt seated behind the open window with neat stacks of "
     f"banknotes on the ledge, low-rise city buildings and young trees behind, warm late-afternoon sun, "
     f"wide documentary editorial shot, {UP}, {NOFACE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_3.jpg",
     f"{LEAD} Extreme close-up of a single United States one-hundred-dollar bill lying flat on a worn "
     f"dark wooden counter with a neatly fanned spread of Iraqi dinar banknotes laid out beside it, "
     f"shallow depth of field, dramatic hard side light raking across the paper, no faces in frame, "
     f"{BLANK}, {NOUI}, {NEG}"),
]

# ── 3 · HORMUZ — two tenders at once, and the buyers choose (P2 · 21:15) ──
s = f"{D}-hormuz-oman-transfer"
JOBS += [
    (s, "hero.jpg",
     f"{LEAD} Wide cinematic aerial editorial shot of two laden crude oil supertankers moored side by "
     f"side in open blue water far from any coast, floating fenders between their hulls and transfer "
     f"hoses rigged across, a ship-to-ship cargo transfer under way in hazy hot daylight, calm sea "
     f"stretching to an empty horizon, completely plain unmarked hulls, {UP}, {BLANK}, {NOUI}, {NEG}"),
    (s, "broll_1.jpg",
     f"{LEAD} Wide cinematic aerial editorial shot of a crude oil export terminal on the Gulf coast of "
     f"southern Iraq at golden hour, a laden supertanker moored alongside a long jetty with loading arms "
     f"connected, a tank farm of white storage tanks on the shore behind, calm sea, hazy warm light, "
     f"{UP}, {BLANK}, {NOUI}, {NEG}"),
    (s, "broll_2.jpg",
     f"{LEAD} A narrow blue sea strait between two stark arid mountainous coastlines photographed from "
     f"high altitude at golden hour, a single small tanker silhouette making way through the deep "
     f"channel far below, haze and glare on the water, vast and tense emptiness, wide cinematic "
     f"editorial shot, {UP}, {BLANK}, {NOUI}, {NEG}"),
    (s, "broll_3.jpg",
     f"{LEAD} A long dense queue of Iraqi public-sector employees waiting to collect pay at a government "
     f"cashier window inside a plain bureaucratic hall, men in short-sleeved shirts and women in dark "
     f"abayas standing in line under fluorescent light, worn tiled floor, patient tired mood, "
     f"documentary photojournalism, {UP}, {NOFACE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
]

# ── 4 · FUEL SUBSIDY LIFTED FROM 1 SEPTEMBER, citizen products carved out (P1 · 22:30) ──
s = f"{D}-mazot-subsidy-september"
JOBS += [
    (s, "hero.jpg",
     f"{LEAD} Wide editorial photojournalism shot of a busy petrol filling station forecourt in Baghdad "
     f"at hard midday sun, a long queue of dusty cars and small pickup trucks waiting at the pumps, an "
     f"attendant in a plain overall holding the nozzle into a fuel tank, heat shimmer rising off the "
     f"concrete, plain blank canopy with no lettering, documentary reportage, {UP}, {NOFACE}, {BLANK}, "
     f"{NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_1.jpg",
     f"{LEAD} A neighbourhood diesel generator installation in a Baghdad residential street, a large "
     f"weathered industrial generator unit on a concrete plinth with a thick bundle of black cables "
     f"fanning out overhead to the surrounding houses, dust and exhaust haze in hot afternoon light, "
     f"low brick and concrete homes behind, documentary reportage, {UP}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_2.jpg",
     f"{LEAD} Extreme close-up of a fuel pump nozzle being pulled from the filler neck of a dusty car, "
     f"a last drop of diesel hanging from the spout, scratched paintwork and hot reflected sunlight, "
     f"shallow depth of field, no faces in frame, {BLANK}, {NOUI}, {NEG}"),
    (s, "broll_3.jpg",
     f"{LEAD} A row of orange and white heavy goods lorries and tanker trucks parked nose to tail on a "
     f"dusty transport yard on the edge of an Iraqi city at dawn, drivers' cabs empty, flat arid horizon "
     f"and a pale sky behind, completely plain unmarked bodywork, wide documentary editorial shot, {UP}, "
     f"{BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
]

# ── 5 · GOLD — the mithqal falls with the ounce (P1 · 23:45 · V10.1 SILENT CONTROL) ──
s = f"{D}-mithqal-gold-down"
JOBS += [
    (s, "hero.jpg",
     f"{LEAD} Wide editorial photojournalism shot of a goldsmith's shop window in a Baghdad gold market "
     f"souk, dense tiers of gold necklaces bracelets and bangles hanging on plain velvet display busts "
     f"behind the glass, warm concentrated spotlights making the metal glow, a shopkeeper's silhouette "
     f"blurred deep inside, {UP}, {NOFACE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_1.jpg",
     f"{LEAD} Extreme close-up of a jeweller's small brass balance scale on a glass counter with several "
     f"thick gold bangles heaped in one pan, a hand steadying the beam, warm shop light, shallow depth "
     f"of field, no face in frame, {BLANK}, {NOUI}, {NEG}"),
    (s, "broll_2.jpg",
     f"{LEAD} A narrow covered gold souk alley in Baghdad crowded with shoppers walking between facing "
     f"rows of small jewellery shops, warm yellow light spilling from the display windows onto the "
     f"walkway, women in dark abayas and men in short-sleeved summer shirts browsing, wide documentary "
     f"editorial shot, {UP}, {NOFACE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    (s, "broll_3.jpg",
     f"{LEAD} Extreme close-up of a pair of heavy gold wedding bangles resting on dark red velvet beside "
     f"a small folded stack of Iraqi dinar banknotes, hard directional light raking across the polished "
     f"metal, shallow depth of field, no faces in frame, {BLANK}, {NOUI}, {NEG}"),
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
