#!/usr/bin/env python3
"""Generate the 20 editorial scenes for the 2026-07-14 slate via KIE Nano Banana Pro
(9:16, 2K). All scene-based (no named-person faces — the officials here are 2026 figures
with no reliable Commons portrait; scene-based avoids wrong-face + fake-face risk, matching
the 2026-07-11/12/13 precedent). Each prompt is matched to THAT beat's Arabic text.
Hardened anti-UI / anti-text negatives (see feedback_kie_fake_ui_govbuilding).
Read-verify every image before accept.

Slate (posting order):
  1 · graft-gold-375kg   (P1 corruption, V11)  — SJC recovers 375kg gold in oil-graft case
  2 · opec-output-iraq   (P2 oil-revenue)      — OPEC+ +188k bpd from Aug, Iraq revenue squeeze
  3 · dollar-three-tier  (P1 currency, V11)    — why the public pays 1,320 not the official 1,300
  4 · iran-mou-energy    (P2 Gulf/Iran)        — US-Iran MoU and Iraq's Iranian-gas/electricity bind
  5 · faw-port-bids      (P1 mega-project)     — Iraq invites bids for remaining Faw piers, AD Ports
"""
from __future__ import annotations
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, NEG, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore

# Extra-hard negatives for any shot at risk of hallucinated UI / gauges / labels / maps.
HARD = "absolutely no readable text, no numbers, no letters, no user interface, no app screen, no news graphics, no maps with labels, no watermark, no logos"

D = "2026-07-14"
JOBS = [
    # 1 · graft-gold-375kg (P1, V11 — 375kg gold recovered today, $100M cash in bottles/walls/drainpipe)
    (f"{D}-graft-gold-375kg", "hero.jpg", f"An editorial evidence still on a dark table under a hard police spotlight: many stacked solid gold bars and bricks beside neat tall stacks of seized US hundred-dollar banknotes, a huge state oil-corruption seizure, {HARD}, {NEG}"),
    (f"{D}-graft-gold-375kg", "broll_1.jpg", f"A secured police evidence room, a table and open metal case piled high with dozens of gleaming gold bars and gold bricks under bright forensic lighting, a large recovered gold hoard in official custody, {HARD}, {NEG}"),
    (f"{D}-graft-gold-375kg", "broll_2.jpg", f"A police evidence table with rolls of US dollar banknotes stuffed inside clear unlabeled plastic water bottles and more cash pulled from a broken-open wall cavity, an unusual cash-concealment seizure, hard evidence-photo lighting, blank bottles with no readable labels, {HARD}, {NEG}"),
    (f"{D}-graft-gold-375kg", "broll_3.jpg", f"Elite anti-corruption officers in dark tactical gear escorting a detained official out of a government building at dawn, the suspect faceless from behind with hands held behind the back, tense documentary photojournalism, no faces visible, {HARD}, {NEG}"),
    # 2 · opec-output-iraq (P2 — OPEC+ +188k bpd from Aug, Iraq 95% oil-dependent, price/revenue squeeze)
    (f"{D}-opec-output-iraq", "hero.jpg", f"A sprawling oil refinery and oilfield at dusk with tall distillation towers and a bright gas flare against a somber orange sky, national oil wealth, cinematic industrial editorial wide shot, {HARD}, {NEG}"),
    (f"{D}-opec-output-iraq", "broll_1.jpg", f"A formal international energy summit room, a long polished table with several national flags on stands behind seated delegations, figures seen from behind and the side with no clear faces, an oil-producers meeting, editorial, {HARD}, {NEG}"),
    (f"{D}-opec-output-iraq", "broll_2.jpg", f"A long row of nodding-donkey oil pump jacks silhouetted across an open desert at sunset under a heavy sky, rising crude production, cinematic industrial wide shot, {HARD}, {NEG}"),
    (f"{D}-opec-output-iraq", "broll_3.jpg", f"An oil export marine terminal with rows of large storage tanks and a moored crude tanker loading at a coastal port at dusk, oil revenue flowing out, industrial editorial aerial shot, {HARD}, {NEG}"),
    # 3 · dollar-three-tier (P1, V11 — official 1300 vs bank 1310 vs public 1320, parallel market, CBI)
    (f"{D}-dollar-three-tier", "hero.jpg", f"A close-up at a currency-exchange counter of hands fanning out US hundred-dollar banknotes beside thick stacks of Iraqi dinar banknotes, a money-changer trading cash, no faces, warm shop light, blank banknotes with no readable serial text, {HARD}, {NEG}"),
    (f"{D}-dollar-three-tier", "broll_1.jpg", f"A bank teller counter with a bill-counting machine fanning through a thick stack of US hundred-dollar banknotes, the formal banking channel, cool clean light, no faces, {HARD}, {NEG}"),
    (f"{D}-dollar-three-tier", "broll_2.jpg", f"A busy Middle Eastern street currency-exchange market with rows of money-changer booths and men trading bundles of cash seen from behind with no clear faces, the parallel market, gritty documentary photojournalism, {HARD}, {NEG}"),
    (f"{D}-dollar-three-tier", "broll_3.jpg", f"An imposing modern central bank headquarters tower of glass and stone photographed from a low heroic angle against a clear sky, monetary authority, architectural editorial, {HARD}, {NEG}"),
    # 4 · iran-mou-energy (P2 — US-Iran MoU, Iraq imports Iranian gas 30-40% of power, waiver bind)
    (f"{D}-iran-mou-energy", "hero.jpg", f"A large gas-fired power plant at dusk with tall cooling stacks and a web of high-voltage transmission pylons marching into the distance, a national electricity grid, cinematic industrial editorial wide shot, {HARD}, {NEG}"),
    (f"{D}-iran-mou-energy", "broll_1.jpg", f"A formal diplomatic negotiation room with two national flags on stands facing each other across a long polished table and empty leather chairs, a tentative US-Iran understanding, soft window light, no people, {HARD}, {NEG}"),
    (f"{D}-iran-mou-energy", "broll_2.jpg", f"A cross-border natural gas pipeline and compressor station stretching across an arid border landscape under a hazy sky, imported gas feeding power stations, industrial documentary wide shot, {HARD}, {NEG}"),
    (f"{D}-iran-mou-energy", "broll_3.jpg", f"A dense tangle of low-hanging neighborhood electrical wires above a Baghdad residential street at dusk with a small private diesel generator humming on the curb, the daily reality of unreliable power, gritty documentary photojournalism, no faces, {HARD}, {NEG}"),
    # 5 · faw-port-bids (P1 mega — remaining piers open to bids, AD Ports, Development Road to Europe)
    (f"{D}-faw-port-bids", "hero.jpg", f"A vast modern deep-water container port at golden hour with a long line of towering ship-to-shore cranes and huge stacks of shipping containers beside a moored container ship, a major new Gulf port, cinematic industrial editorial wide shot, blank unlabeled containers, {HARD}, {NEG}"),
    (f"{D}-faw-port-bids", "broll_1.jpg", f"A large port under construction over water with cranes, concrete quay works and heavy machinery building new berths, an expanding port project, industrial editorial wide shot, no faces, {HARD}, {NEG}"),
    (f"{D}-faw-port-bids", "broll_2.jpg", f"A formal high-level investment signing room, two business delegations seated across a long polished table with national flags standing behind them, figures seen from behind with no clear faces, a port operating partnership, editorial, {HARD}, {NEG}"),
    (f"{D}-faw-port-bids", "broll_3.jpg", f"A brand-new multi-lane highway running parallel to a modern railway line stretching straight across open desert toward the horizon with a few cargo trucks, a trade corridor linking a port to Europe, cinematic editorial wide shot, {HARD}, {NEG}"),
]


def main():
    jobs = []
    print(f"== Submitting {len(JOBS)} scene jobs ==", flush=True)
    for slug, fname, prompt in JOBS:
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
            except Exception as e:
                msg = str(e)
                if "402" in msg:
                    print("  !! KIE 402 out-of-credits — aborting, fall back to Pexels/Commons", file=sys.stderr, flush=True)
                    return 2
                still.append(j); continue
            data = r.get("data") or {}
            st = data.get("state")
            if st == "success":
                url = first_image_url(data)
                if not url:
                    print(f"  ? {j['slug']}/{j['file']}: success but no url", file=sys.stderr, flush=True)
                    continue
                try:
                    info = download(url, j["out"])
                    j["ok"] = True
                    print(f"  OK {j['slug']}/{j['file']}  {info}", flush=True)
                except Exception as e:
                    print(f"  ! download {j['slug']}/{j['file']}: {e}", file=sys.stderr, flush=True)
            elif st == "fail":
                print(f"  X {j['slug']}/{j['file']}: fail — {data.get('failMsg','?')}", file=sys.stderr, flush=True)
            else:
                still.append(j)
        pending = still
    ok = sum(1 for j in jobs if j["ok"])
    print(f"\n== Done: {ok}/{len(JOBS)} images ==", flush=True)
    return 0 if ok == len(JOBS) else 1


if __name__ == "__main__":
    sys.exit(main())
