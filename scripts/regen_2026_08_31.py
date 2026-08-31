#!/usr/bin/env python3
"""Targeted single-frame regeneration for the 2026-08-31 slate.

Usage: regen_2026_08_31.py <key> [<key> ...]   (keys are defined in FIXES below)
Each entry replaces exactly one file that failed the Read-verify pass.
"""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, http_get, first_image_url, download, submit  # type: ignore
from gen_scenes_2026_08_31 import LEAD, NOUI, UP, NOFACE, BLANK, NOTWEST, NOTE_EDGE  # type: ignore

NOPORTRAIT = ("absolutely no banknotes anywhere in frame, no currency on display, no paper money of "
              "any kind, no printed portraits of any person")

FIXES: dict[str, tuple[str, str, str]] = {
    # ── round 1 (my own Read-verify) ───────────────────────────────────────────
    # b_broll_2 pass 1: kiosk display resolved into portrait-bearing notes (a
    # pre-2003 Saddam-era design) on a 2026 currency reel.
    # b_broll_2 pass 2: came back shuttered, under a beat quoting live Erbil prices.
    # ── round 2 (Opus audience/liability gate) ─────────────────────────────────
    # B4: pass 3 read as a Gulf/European ticket booth — manicured plaza, irrigated
    # planting, customer in shorts and flip-flops. Wrong country on a reel whose
    # whole payoff is an Iraqi shop-to-shop price comparison.
    "b_broll_2": (
        "2026-08-31-b-dollar-flat-second-day", "broll_2.jpg",
        f"{LEAD} Editorial photojournalism shot of a currency exchange shop front on an ordinary "
        f"commercial street in Erbil in the Kurdistan Region of Iraq, a glass counter under a metal "
        f"awning with the exchanger seated behind it, neighbouring shops with half-raised roll shutters "
        f"on either side, dusty tarmac and parked cars, hard midday summer light, men in long trousers "
        f"and short-sleeved shirts, {UP}, {NOFACE}, {NOPORTRAIT}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),

    # B5: a thinning grocery shelf on a currency reel reads as "the dinar buys
    # less / goods are running short" — the exact opposite of this reel's finding,
    # which is that the rate is FLAT for a second day. Nothing in the copy
    # mentions groceries, prices or supply.
    "b_broll_1": (
        "2026-08-31-b-dollar-flat-second-day", "broll_1.jpg",
        f"{LEAD} Extreme close-up of a money changer's hands at a worn wooden exchange counter, one "
        f"hand pressing the keys of an old desk calculator and the other resting on an open paper "
        f"ledger with handwriting rendered completely illegible, warm interior light, shallow depth of "
        f"field, no face in frame, absolutely no banknotes and no currency of any kind anywhere in "
        f"frame, no printed portraits, no legible text or numerals, {BLANK}, {NOUI}, {NEG}"),

    # Nit: several faces in the trading-street crowd are sharp while others are
    # smeared into what reads as deliberate editorial pixelation — that mimics the
    # grammar of a real news photo with anonymised subjects, which strengthens the
    # documentary read on a V11 reel that draws no AI chip.
    "b_broll_3": (
        "2026-08-31-b-dollar-flat-second-day", "broll_3.jpg",
        f"{LEAD} A crowded informal currency trading street in central Baghdad photographed from behind "
        f"the crowd in the late morning, every person seen from the back or in silhouette with no face "
        f"visible to the camera at all, men in short-sleeved shirts and long trousers, low concrete "
        f"commercial buildings with plain blank frontages, hot white summer light and dust haze, wide "
        f"documentary editorial shot, {UP}, {NOPORTRAIT}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),

    # Nit: a riverside institutional block with shuttered windows and weeds through
    # the pavement cycles under the finance minister's on-record «مؤمّنة بالكامل».
    # A derelict-looking building visually rebuts a statement the reel is otherwise
    # scrupulous about carrying.
    "c_broll_1": (
        "2026-08-31-c-salaries-august-last-day", "broll_1.jpg",
        f"{LEAD} Exterior of a well-maintained modern Iraqi government office building on a clean city "
        f"street in bright morning light, pale stone facade with orderly rows of clear glass windows, "
        f"trimmed palms and a swept paved forecourt, a few parked cars, wide documentary editorial shot, "
        f"no people, no dereliction, no weeds, no broken windows, {UP}, {BLANK}, {NOTWEST}, {NOUI}, "
        f"{NEG}"),

    # B3: a stalled, weed-grown concrete frame sat under «زاد 15.557 تريليوناً».
    # Slug D is V10.1, where the frame shows ONLY under that line with nothing to
    # dilute it — so it supplies a cause (waste, stalled projects) that the CBI
    # balance-sheet data never mentions. The AI chip does not cure a false
    # implication.
    "d_broll_3": (
        "2026-08-31-d-internal-debt-106", "broll_3.jpg",
        f"{LEAD} Editorial close-up of a thick printed statistical bulletin lying open on a plain desk "
        f"in an institutional office, dense columns of figures rendered completely out of focus and "
        f"entirely unreadable, soft neutral daylight from a window, shallow depth of field, no legible "
        f"text or numerals of any kind, no letterhead, no logos, no charts, no people and no hands in "
        f"frame, {BLANK}, {NOUI}, {NEG}"),

    # B2: an unmarked airliner parked alone on a deserted night apron sat under
    # «لم يُعلن رسمياً أي إغلاق للأجواء أو تأخير للرحلات». The story is TRANSIT
    # OVERFLIGHT; a motionless grounded plane says flights were stopped at an
    # Iraqi airport — the very thing the reel says was never declared.
    "e_broll_2": (
        "2026-08-31-e-oil-larak-airspace", "broll_2.jpg",
        f"Editorial night aerial photograph looking out across a high-altitude air corridor, a wide "
        f"dark blue sky above a moonlit cloud deck far below, two or three tiny distant aircraft "
        f"navigation lights as pinpoints at cruise altitude near the horizon, no airport, no runway, no "
        f"terminal, no parked aircraft, no ground, {UP}, {BLANK}, {NOUI}, {NEG}"),

    # Nit: the hero read as a narrow rocky gorge. Hormuz is roughly 33 km across —
    # a canyon misinforms about a named real place on a chip-less V11 reel.
    "e_hero": (
        "2026-08-31-e-oil-larak-airspace", "hero.jpg",
        f"Wide cinematic aerial editorial photograph of a broad open sea strait at dawn, a great "
        f"expanse of deep blue water filling most of the frame with a low arid coastline lying far off "
        f"on each horizon many kilometres apart, three distant cargo vessels as small silhouettes "
        f"strung out along the shipping lane, soft golden haze, a clear sense of great width and open "
        f"water, no narrow channel, no cliffs, no gorge, no military vessels, {UP}, {BLANK}, {NOUI}, "
        f"{NEG}"),
}


def main() -> int:
    keys = sys.argv[1:] or list(FIXES)
    jobs = []
    for k in keys:
        slug, fname, prompt = FIXES[k]
        out = IMG_ROOT / slug / fname
        out.parent.mkdir(parents=True, exist_ok=True)
        tid = submit(prompt)
        jobs.append({"slug": slug, "file": fname, "out": out, "tid": tid, "ok": False})
        print(f"  + {k}  {slug}/{fname} tid={tid}", flush=True)
        time.sleep(0.4)

    pending = list(jobs)
    deadline = time.time() + 14 * 60
    while pending and time.time() < deadline:
        time.sleep(POLL_INTERVAL)
        still = []
        for j in pending:
            try:
                data = (http_get(f"{STATUS_URL}?taskId={j['tid']}") or {}).get("data") or {}
                st = str(data.get("state") or "").lower()
                if st == "success":
                    url = first_image_url(data)
                    if url:
                        print(f"  OK  {j['slug']}/{j['file']}  {download(url, j['out'])}", flush=True)
                        j["ok"] = True
                        continue
                    continue
                if st in ("fail", "failed", "error"):
                    print(f"  XX  {j['slug']}/{j['file']} FAILED: {str(data)[:200]}", flush=True)
                    continue
                still.append(j)
            except Exception as e:
                print(f"  ?   {j['slug']}/{j['file']}: {e}", flush=True)
                still.append(j)
        pending = still
    done = sum(1 for j in jobs if j["ok"])
    print(f"== REGEN DONE {done}/{len(jobs)} ==", flush=True)
    return 0 if done == len(jobs) else 1


if __name__ == "__main__":
    raise SystemExit(main())
