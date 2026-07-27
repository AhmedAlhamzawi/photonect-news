#!/usr/bin/env python3
"""Generate the 2026-07-27 slate scenes via KIE Nano Banana Pro (9:16 2K).
5 slugs x 4 images each (hero + broll_1/2/3), each matched to its beat.
Scenes only. Hardened anti-UI/anti-text negatives. Submit-all-then-poll-all.
"""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, http_get, first_image_url, download, submit  # type: ignore

D = "2026-07-27"
NOUI = "absolutely no user-interface, no app screens, no news graphics, no readable text on any screen, no phone or tablet UI"
UP = "upright vertical portrait orientation, correct horizon, not rotated"

JOBS = [
    # 1 — BANK FORGERY NETWORK / 31 DETAINED  (P1 corruption · LEAD)
    (f"{D}-bank-forgery-network", "hero.jpg", f"Wide editorial shot of anti-corruption investigators in plain dark suits examining seized document folders and evidence boxes spread across a long table in a bare government interrogation room, serious forensic atmosphere, cold overhead light, documentary photojournalism, {UP}, {NOUI}, {NEG}"),
    (f"{D}-bank-forgery-network", "broll_1.jpg", f"Extreme close-up of a tall disordered stack of paper loan application forms with official rubber ink stamps and a scattered set of stamp seals on a desk, forged paperwork theme, dramatic side light, shallow depth of field, {NOUI}, {NEG}"),
    (f"{D}-bank-forgery-network", "broll_2.jpg", f"Interior of a state bank branch hall with a long teller counter and customers waiting in an orderly queue under fluorescent light, public banking theme, wide editorial documentary shot, {UP}, {NOUI}, {NEG}"),
    (f"{D}-bank-forgery-network", "broll_3.jpg", f"Close-up of confiscated gold bars and neatly banded bundles of cash laid out as evidence on a dark table beside a numbered evidence marker, asset seizure theme, dramatic low-key light, {NOUI}, {NEG}"),
    # 2 — STREET DOLLAR vs OFFICIAL RATE GAP  (P1 dinar · daily anchor)
    (f"{D}-dollar-official-gap", "hero.jpg", f"Wide editorial shot of a crowded open-air currency trading street in Baghdad, dozens of traders standing in tight groups holding thick bundles of banknotes and negotiating, energetic informal market, harsh midday sun, documentary photojournalism, {UP}, {NOUI}, {NEG}"),
    (f"{D}-dollar-official-gap", "broll_1.jpg", f"Extreme close-up of two hands holding a fan of Iraqi dinar notes in one hand and a fan of US one-hundred-dollar bills in the other, direct side-by-side comparison, dark background, dramatic rim light, shallow depth of field, {NOUI}, {NEG}"),
    (f"{D}-dollar-official-gap", "broll_2.jpg", f"Grand marble interior hall of a national central bank with tall columns, polished floor and a sweeping staircase, austere institutional monetary-authority atmosphere, wide architectural editorial shot, {UP}, {NOUI}, {NEG}"),
    (f"{D}-dollar-official-gap", "broll_3.jpg", f"A middle-aged Iraqi man at a small exchange booth window handing over a thick stack of dinar notes to a cashier, everyday cost of buying dollars, warm afternoon light through the glass, intimate documentary photojournalism, {NOUI}, {NEG}"),
    # 3 — IRAQI FUEL OIL TO LEBANON / UNPAID DEBT  (P2 energy-trade)
    (f"{D}-fuel-to-lebanon-debt", "hero.jpg", f"Wide cinematic shot of a large fuel oil tanker ship berthed at an export terminal with loading arms connected and pipelines running along the quay, golden hour, aerial editorial photography, {UP}, {NEG}"),
    (f"{D}-fuel-to-lebanon-debt", "broll_1.jpg", f"A coastal thermal power station with tall smokestacks glowing against a Mediterranean dusk sky, sea in the foreground, electricity generation theme, wide cinematic shot, {UP}, {NOUI}, {NEG}"),
    (f"{D}-fuel-to-lebanon-debt", "broll_2.jpg", f"Two empty facing rows of chairs at a long polished negotiating table in a formal government meeting room with plain flag stands and no people, bilateral talks theme, cool daylight, wide editorial interior shot, {NOUI}, {NEG}"),
    (f"{D}-fuel-to-lebanon-debt", "broll_3.jpg", f"An unpaid ledger of stacked invoices and a closed accounting book on a desk beside an empty chair in a dim office, mounting arrears theme, moody low light, shallow depth of field, {NOUI}, {NEG}"),
    # 4 — GULF POWER LINK DELAYED  (P1 electricity)
    (f"{D}-gulf-power-link-delay", "hero.jpg", f"Wide cinematic shot of a long line of tall high-voltage electricity transmission towers marching across an empty desert plain toward the horizon under a hazy hot sky, regional interconnection theme, aerial editorial photography, {UP}, {NOUI}, {NEG}"),
    (f"{D}-gulf-power-link-delay", "broll_1.jpg", f"An unfinished electrical substation with idle transformers still wrapped in protective covering and no workers present, stalled construction site, harsh midday sun, wide documentary shot, {NOUI}, {NEG}"),
    (f"{D}-gulf-power-link-delay", "broll_2.jpg", f"An Iraqi family sitting together in a dim sweltering living room during a power cut, a single battery lamp and a still ceiling fan, extreme summer heat, intimate documentary photojournalism, {NOUI}, {NEG}"),
    (f"{D}-gulf-power-link-delay", "broll_3.jpg", f"Rows of large gas turbine generator halls at a power plant seen from the air at sunset with pipelines running to them, thermal generation theme, aerial editorial photography, {NEG}"),
    # 5 — PM ANKARA VISIT: WATER + DEVELOPMENT ROAD  (P2 · SILENT V10 CONTROL)
    (f"{D}-turkey-water-road-visit", "hero.jpg", f"Wide cinematic aerial shot of a large concrete hydroelectric dam holding back a reservoir in rugged mountains with spillway gates closed, upstream water control theme, clear daylight, {UP}, {NEG}"),
    (f"{D}-turkey-water-road-visit", "broll_1.jpg", f"A wide dried cracked riverbed with only a thin shallow channel of water remaining and bare banks on either side, drought and low river flow theme, hard midday light, wide editorial landscape, {NEG}"),
    (f"{D}-turkey-water-road-visit", "broll_2.jpg", f"A long new railway line and parallel highway under construction cutting straight across open desert terrain with earthmoving machinery working alongside, major transport corridor project, aerial editorial photography, {UP}, {NOUI}, {NEG}"),
    (f"{D}-turkey-water-road-visit", "broll_3.jpg", f"An irrigation canal running between green farm fields with a farmer opening a small sluice gate to let water into the furrows, agricultural water share theme, warm late afternoon light, documentary photojournalism, {NOUI}, {NEG}"),
]


def main() -> int:
    only = set(sys.argv[1:])
    jobs = []
    todo = [(s, f, p) for (s, f, p) in JOBS if not only or s in only]
    print(f"== Submitting {len(todo)} scene jobs ==", flush=True)
    for slug, fname, prompt in todo:
        out = IMG_ROOT / slug / fname
        out.parent.mkdir(parents=True, exist_ok=True)
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
            except Exception:
                still.append(j); continue
            data = (r.get("data") or {})
            url = first_image_url(data)
            state = str(data.get("state") or data.get("status") or "").lower()
            if url:
                try:
                    info = download(url, j["out"])
                    j["ok"] = True
                    print(f"  ✓ {j['slug']}/{j['file']}  {info}", flush=True)
                except Exception as e:
                    print(f"  ! download {j['slug']}/{j['file']}: {e}", file=sys.stderr, flush=True)
            elif state in ("fail", "failed", "error"):
                print(f"  ✗ {j['slug']}/{j['file']} FAILED: {data.get('failMsg') or data.get('msg')}", file=sys.stderr, flush=True)
            else:
                still.append(j)
        pending = still
        if pending:
            print(f"  … {len(pending)} pending", flush=True)
    ok = sum(1 for j in jobs if j.get("ok"))
    print(f"\n== Done: {ok}/{len(jobs)} ==", flush=True)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
