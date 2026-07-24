#!/usr/bin/env python3
"""Generate the 2026-07-24 slate scenes via KIE Nano Banana Pro (9:16 2K).
5 slugs x 4 images each (hero + broll_1/2/3), each matched to its beat.
Scenes only (no named-person faces on this slate). Hardened anti-UI/anti-text
negatives. Submit-all-then-poll-all.
"""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, http_get, first_image_url, download, submit  # type: ignore

D = "2026-07-24"
NOUI = "absolutely no user-interface, no app screens, no news graphics, no readable text on any screen, no phone or tablet UI"

JOBS = [
    # 1 — GRAFT: RETURN THE MONEY, LIGHTER SENTENCE (integrity/recovery)
    (f"{D}-graft-return-or-jail", "hero.jpg", f"Wide editorial shot of Iraqi integrity-commission investigators in formal suits walking into a government ministry building carrying thick document folders, a serious accountability operation, overcast daylight, documentary photojournalism, {NEG}"),
    (f"{D}-graft-return-or-jail", "broll_1.jpg", f"Close-up of a wooden judge's gavel resting beside a stack of sealed legal case files and a small Iraqi flag on a courtroom desk, symbolizing a judicial roadmap to recover stolen funds, dramatic side light, shallow depth of field, {NEG}"),
    (f"{D}-graft-return-or-jail", "broll_2.jpg", f"Interior of a formal Iraqi anti-corruption courtroom with an empty elevated judge's bench and rows of wooden seats under cool light, solemn rule-of-law mood, editorial documentary, {NOUI}, {NEG}"),
    (f"{D}-graft-return-or-jail", "broll_3.jpg", f"Overhead shot of neat bundles of US dollar banknotes and Iraqi dinar stacks being counted on a desk beside official legal documents, symbolizing returned embezzled money, cold clinical light, shallow depth of field, {NEG}"),
    # 2 — OIL-FOR-GAS BARTER WITH IRAN (power / energy plumbing)
    (f"{D}-iran-gas-oil-barter", "hero.jpg", f"Wide cinematic shot of a large gas-fired power plant with tall stacks and steam at dusk, a network of pipelines in the foreground, industrial energy infrastructure, moody orange sky, documentary, {NEG}"),
    (f"{D}-iran-gas-oil-barter", "broll_1.jpg", f"Close-up of an oil and gas pipeline junction with heavy valves and pressure gauges in a desert facility at golden hour, energy trade and barter theme, shallow depth of field, {NOUI}, {NEG}"),
    (f"{D}-iran-gas-oil-barter", "broll_2.jpg", f"Interior of a power-plant turbine hall with massive gas turbines and an engineer in a hard hat walking the aisle, warm industrial light, sense of straining capacity, documentary, {NOUI}, {NEG}"),
    (f"{D}-iran-gas-oil-barter", "broll_3.jpg", f"A line of tall high-voltage electricity transmission towers and power lines stretching across an arid landscape at sunset, national grid theme, wide cinematic shot, {NEG}"),
    # 3 — STATE PRINTED 25 TRILLION DINARS (money supply / dinar)
    (f"{D}-money-printing-25tn", "hero.jpg", f"Dramatic close-up of freshly printed sheets of Iraqi dinar banknotes coming off an industrial currency printing press, ink rollers and stacked notes, cold factory light, {NOUI}, {NEG}"),
    (f"{D}-money-printing-25tn", "broll_1.jpg", f"Towering stacks and bundles of Iraqi dinar banknotes filling the frame on a steel table, huge volume of cash, shallow depth of field, dramatic side light, {NEG}"),
    (f"{D}-money-printing-25tn", "broll_2.jpg", f"Exterior of an imposing modern central-bank headquarters building with tall columns under an overcast sky, monetary-authority theme, wide editorial architectural shot, {NEG}"),
    (f"{D}-money-printing-25tn", "broll_3.jpg", f"A worried middle-aged Iraqi public-sector worker holding a small bundle of dinar banknotes outside a bank, anxious expression about eroding salary value, overcast street, documentary photojournalism, {NEG}"),
    # 4 — GULF SOVEREIGN FUNDS DEPLOY TRILLIONS (control — Gulf finance)
    (f"{D}-gulf-swf-trillions", "hero.jpg", f"Wide cinematic dusk skyline of a gleaming Gulf financial district with modern glass skyscrapers and illuminated towers, sovereign-wealth and capital theme, warm sky, architectural photography, {NEG}"),
    (f"{D}-gulf-swf-trillions", "broll_1.jpg", f"Low-angle shot of a single sleek mirrored corporate headquarters tower reflecting a golden sky, symbol of a giant sovereign investment fund, clean minimal architecture, {NEG}"),
    (f"{D}-gulf-swf-trillions", "broll_2.jpg", f"A busy stock-exchange trading floor with traders in suits and large abstract glowing market boards in the background, global finance energy, motion, {NOUI}, {NEG}"),
    (f"{D}-gulf-swf-trillions", "broll_3.jpg", f"A field of oil pump jacks silhouetted against a dramatic orange sunset, OPEC oil-production and petro-wealth theme, wide cinematic shot, {NEG}"),
    # 5 — WATER RESERVES AT 80-YEAR LOW (drought / climate-economy)
    (f"{D}-water-heat-crisis", "hero.jpg", f"Wide desolate shot of a cracked dried riverbed of the Euphrates under a blazing white sun, drought and extreme heat, shimmering heat haze, documentary photojournalism, {NEG}"),
    (f"{D}-water-heat-crisis", "broll_1.jpg", f"Dramatic aerial view of a shrunken Tigris river reduced to a thin channel with wide exposed cracked banks, severe water shortage, arid landscape, cinematic, {NEG}"),
    (f"{D}-water-heat-crisis", "broll_2.jpg", f"An Iraqi farmer in traditional dress standing in a cracked parched field holding withered dead crops, despair under harsh sunlight, heat haze, documentary photojournalism, {NEG}"),
    (f"{D}-water-heat-crisis", "broll_3.jpg", f"A stranded wooden boat lying on sun-scorched cracked earth of a dried-up southern Iraqi marshland at midday, climate disaster, wide cinematic shot, {NEG}"),
]


def main() -> int:
    only = set(sys.argv[1:])
    jobs = []
    todo = [(s, f, p) for (s, f, p) in JOBS if not only or s in only]
    print(f"== Submitting {len(todo)} scene jobs ==", flush=True)
    for slug, fname, prompt in todo:
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
                    still.append(j)
            elif state in ("fail", "failed", "error"):
                print(f"  ✗ {j['slug']}/{j['file']} FAILED state={state}", file=sys.stderr, flush=True)
            else:
                still.append(j)
        pending = still
        print(f"    … {len(pending)} pending", flush=True)
    ok = sum(1 for j in jobs if j["ok"])
    print(f"\n== Done: {ok}/{len(jobs)} downloaded ==", flush=True)
    return 0 if ok == len(jobs) else 1


if __name__ == "__main__":
    raise SystemExit(main())
