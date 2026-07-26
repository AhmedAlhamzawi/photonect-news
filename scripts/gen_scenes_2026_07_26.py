#!/usr/bin/env python3
"""Generate the 2026-07-26 slate scenes via KIE Nano Banana Pro (9:16 2K).
5 slugs x 4 images each (hero + broll_1/2/3), each matched to its beat.
Scenes only (no named-person faces on this slate). Hardened anti-UI/anti-text
negatives. Submit-all-then-poll-all.
"""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, http_get, first_image_url, download, submit  # type: ignore

D = "2026-07-26"
NOUI = "absolutely no user-interface, no app screens, no news graphics, no readable text on any screen, no phone or tablet UI"
UP = "upright vertical portrait orientation, correct horizon, not rotated"

JOBS = [
    # 1 — DOLLAR FALLS BELOW 150,000 / 100USD  (money / dinar · LEAD-adjacent)
    (f"{D}-dollar-under-150", "hero.jpg", f"Wide editorial shot of a busy Baghdad currency-exchange street, a money changer in a small booth counting thick bundles of Iraqi dinar banknotes while customers wait at the window, warm daylight, documentary photojournalism, {UP}, {NOUI}, {NEG}"),
    (f"{D}-dollar-under-150", "broll_1.jpg", f"Extreme close-up of neat stacks of Iraqi dinar banknotes beside bundles of US one-hundred-dollar bills on a currency-exchange counter, hands counting, shallow depth of field, dramatic side light, {NOUI}, {NEG}"),
    (f"{D}-dollar-under-150", "broll_2.jpg", f"Exterior of an imposing modern central-bank headquarters building with tall columns and a wide plaza under a clear sky, monetary-authority theme, wide editorial architectural shot, {UP}, {NEG}"),
    (f"{D}-dollar-under-150", "broll_3.jpg", f"An Iraqi shopper in a busy Baghdad grocery market inspecting imported packaged goods on crowded shelves, everyday cost-of-living theme, natural market light, documentary photojournalism, {NOUI}, {NEG}"),
    # 2 — AUDIT: 100 TRILLION DINARS IN UNSETTLED LOANS (corruption / accountability · LEAD)
    (f"{D}-audit-100tn-loans", "hero.jpg", f"Wide editorial shot of government auditors in formal suits examining enormous open accounting ledgers spread across a long table in a state audit office, serious forensic atmosphere, overcast daylight, documentary photojournalism, {UP}, {NOUI}, {NEG}"),
    (f"{D}-audit-100tn-loans", "broll_1.jpg", f"Endless towering shelves of dusty government financial archive files and bound ledgers stretching into shadow in a vast records hall, decades of unexamined paperwork, dramatic vanishing-point perspective, {NOUI}, {NEG}"),
    (f"{D}-audit-100tn-loans", "broll_2.jpg", f"Close-up of a wooden judge's gavel resting beside a tall stack of sealed legal case files on a courtroom desk, thousands of referrals to the judiciary, dramatic side light, shallow depth of field, {NOUI}, {NEG}"),
    (f"{D}-audit-100tn-loans", "broll_3.jpg", f"Interior of a large empty bank vault with open steel door and bare shelves under cold clinical light, missing state funds theme, wide cinematic shot, {UP}, {NOUI}, {NEG}"),
    # 3 — JULY AMPERE PRICE / NEIGHBOURHOOD GENERATORS (electricity / services)
    (f"{D}-ampere-price-july", "hero.jpg", f"Wide editorial shot of a large diesel neighbourhood generator running on a Baghdad residential street with a dense tangle of subscriber cables fanning out overhead to nearby homes, dusty warm afternoon light, documentary photojournalism, {UP}, {NOUI}, {NEG}"),
    (f"{D}-ampere-price-july", "broll_1.jpg", f"Extreme close-up of a bank of analogue electricity subscriber meters mounted on a rusted metal panel beside a private generator, tangled wires, worn dials, shallow depth of field, {NOUI}, {NEG}"),
    (f"{D}-ampere-price-july", "broll_2.jpg", f"An Iraqi family sitting in a dim sweltering living room during a power cut, an electric fan and a single battery lamp providing light, extreme summer heat mood, intimate documentary photojournalism, {NOUI}, {NEG}"),
    (f"{D}-ampere-price-july", "broll_3.jpg", f"A worker in overalls pouring diesel fuel from a jerrycan into the tank of a large neighbourhood generator, fuel subsidy theme, harsh midday sunlight, documentary photojournalism, {NOUI}, {NEG}"),
    # 4 — US IMPORTS ZERO IRAQI CRUDE (oil / trade · SILENT V10 CONTROL)
    (f"{D}-us-zero-crude", "hero.jpg", f"Wide cinematic shot of a massive crude oil supertanker moored at an offshore Basra loading terminal in the Gulf at golden hour, pipelines and mooring buoys, calm steel-blue water, aerial editorial photography, {UP}, {NEG}"),
    (f"{D}-us-zero-crude", "broll_1.jpg", f"An empty deserted oil-loading berth with idle loading arms and still water at dawn, no vessel present, sense of halted trade, moody grey light, wide cinematic shot, {NOUI}, {NEG}"),
    (f"{D}-us-zero-crude", "broll_2.jpg", f"Rows of enormous white crude oil storage tanks in a desert export terminal seen from the air, long shadows at sunset, industrial scale, aerial editorial photography, {NEG}"),
    (f"{D}-us-zero-crude", "broll_3.jpg", f"A loaded crude oil tanker sailing alone across open ocean at dusk heading east, long wake behind it, global shipping route theme, wide cinematic seascape, {NEG}"),
    # 5 — NON-OIL REVENUE HITS RECORD 16% (taxes / customs / who pays)
    (f"{D}-nonoil-revenue-16", "hero.jpg", f"Wide editorial shot of a long queue of heavy cargo trucks waiting at an Iraqi land border customs checkpoint under a hot hazy sky, barriers and inspection lanes, documentary photojournalism, {UP}, {NOUI}, {NEG}"),
    (f"{D}-nonoil-revenue-16", "broll_1.jpg", f"Towering stacks of shipping containers and tall gantry cranes at a busy Iraqi seaport terminal, import trade and customs duty theme, dramatic late-afternoon light, wide industrial shot, {NEG}"),
    (f"{D}-nonoil-revenue-16", "broll_2.jpg", f"A young Iraqi customer buying a prepaid mobile top-up card at a small brightly lit street kiosk in Baghdad, everyday consumer tax theme, evening street light, documentary photojournalism, {NOUI}, {NEG}"),
    (f"{D}-nonoil-revenue-16", "broll_3.jpg", f"Rows of newly imported cars parked in a large customs impound yard awaiting clearance, vehicle customs duty theme, harsh daylight, wide aerial editorial shot, {NOUI}, {NEG}"),
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
