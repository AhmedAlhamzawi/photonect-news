#!/usr/bin/env python3
"""Reshoot two rejected 2026-09-23 frames.

b/broll_2 — first take rendered as a convincing police evidence-table handout
  (real $100 bills plus redaction-style blur). On V11 there is no
  «صورة توضيحية» chip, so a synthetic frame that reads as an authentic photo of
  THIS seizure is a misrepresentation risk. Replaced with an unambiguously
  generic enforcement image: a shuttered, padlocked exchange kiosk.

d/broll_2 — first take came back rotated 90° (known KIE failure). Reshot with a
  ground-level composition and hard upright language.
"""
from __future__ import annotations
import sys, time, json, io, subprocess
from pathlib import Path
sys.path.insert(0, "scripts")
from gen_2026_05_28 import IMG_ROOT, NEG, STATUS_URL, http_get, first_image_url, submit  # type: ignore
from PIL import Image

LEAD = "IRAQ, MIDDLE EAST."
NOUI = ("absolutely no user-interface, no app screens, no news graphics, no readable text on any "
        "screen, no phone or tablet UI, no burned-in captions, no price boards")
UP = ("upright vertical portrait orientation, camera held level at standing eye height, horizon "
      "perfectly horizontal across the frame, not rotated, not tilted, not sideways, not aerial")
BLANK = "all signage and surfaces completely blank, no lettering of any alphabet anywhere"
NOTWEST = ("not American, not European, not East Asian, not South Asian, warm late-summer clothing, "
           "no winter coats")
NOPEOPLE = "no people at all anywhere in the frame"

JOBS = [
    ("2026-09-23-b-dollar-156750-network", "broll_2.jpg",
     f"{LEAD} A small currency-exchange kiosk on a Baghdad street closed and sealed, its corrugated "
     f"metal roll-down shutter pulled fully down and secured with a heavy chain and padlock, dusty "
     f"pavement in front, warm late-afternoon side light, a quiet emptied storefront, no evidence "
     f"bags, no banknotes, no handcuffs, nothing resembling a police handout photograph, "
     f"{UP}, {NOPEOPLE}, {BLANK}, {NOTWEST}, {NOUI}, {NEG}"),
    ("2026-09-23-d-fuel-decision-429", "broll_2.jpg",
     f"{LEAD} Ground-level eye-height photograph looking straight along a row of large unmarked "
     f"steel road tanker trucks parked side by side in a dusty fuel depot yard in Iraq at golden "
     f"hour, cylindrical tanks receding in perspective, gravel underfoot, tall refinery towers hazy "
     f"on the horizon behind them, the sky occupying the upper third of the frame and the ground the "
     f"lower third, {UP}, {NOPEOPLE}, no company logo or painted markings of any kind, {BLANK}, "
     f"{NOTWEST}, {NOUI}, {NEG}"),
]

def main():
    jobs = []
    for slug, fname, prompt in JOBS:
        tid = submit(prompt)
        jobs.append({"slug": slug, "file": fname, "out": str(IMG_ROOT / slug / fname), "tid": tid, "ok": False})
        print(f"  + {slug}/{fname} tid={tid}", flush=True)
        time.sleep(0.4)
    Path("scripts/_kie_jobs_2026_09_23_regen.json").write_text(json.dumps(jobs, ensure_ascii=False, indent=1))

    pending = list(jobs); deadline = time.time() + 12*60
    while pending and time.time() < deadline:
        time.sleep(8); still = []
        for j in pending:
            try:
                data = (http_get(f"{STATUS_URL}?taskId={j['tid']}") or {}).get("data") or {}
                url = first_image_url(data)
                if url:
                    out = Path(j["out"])
                    raw = subprocess.run(["curl","-sL","-A","Mozilla/5.0",url], capture_output=True, check=True).stdout
                    im = Image.open(io.BytesIO(raw)); im.load()
                    im.convert("RGB").save(out, "JPEG", quality=92)
                    j["ok"] = True
                    print(f"  ✓ {j['slug']}/{j['file']}  {im.size[0]}x{im.size[1]}", flush=True)
                    continue
                if str(data.get("state") or "").lower() in ("fail","failed","error"):
                    print(f"  ✗ {j['slug']}/{j['file']} {data.get('failMsg')}", flush=True); continue
            except Exception as e:
                print(f"  . {j['file']}: {e}", flush=True)
            still.append(j)
        pending = still
    print(f"\n== regen {sum(1 for j in jobs if j['ok'])}/{len(jobs)} ==")

main()
