#!/usr/bin/env python3
"""Download the 2026-09-23 KIE stills from the persisted task-id manifest.

The generator passed the full response envelope to first_image_url(), which only
matches inside data{}, so nothing downloaded even though every task succeeded.
Tasks are already paid for — this just collects them.
"""
import json, sys, time, subprocess, io
from pathlib import Path
sys.path.insert(0, "scripts")
from gen_2026_05_28 import http_get, first_image_url, STATUS_URL  # type: ignore
from PIL import Image

M = Path("scripts/_kie_jobs_2026_09_23.json")
jobs = json.load(open(M))
deadline = time.time() + 14*60
pending = list(jobs)
done = 0
while pending and time.time() < deadline:
    still = []
    for j in pending:
        try:
            info = http_get(f"{STATUS_URL}?taskId={j['tid']}")
            data = info.get("data") or {}
            url = first_image_url(data)          # <-- the fix
            state = str(data.get("state") or "").lower()
            if url:
                out = Path(j["out"]); out.parent.mkdir(parents=True, exist_ok=True)
                raw = subprocess.run(
                    ["curl","-sL","-A","Mozilla/5.0",url],
                    capture_output=True, check=True).stdout
                im = Image.open(io.BytesIO(raw)); im.load()
                im.convert("RGB").save(out, "JPEG", quality=92)
                j["ok"] = True; done += 1
                print(f"  ✓ {j['slug']}/{j['file']}  {len(raw)//1024}KB {im.size[0]}x{im.size[1]}", flush=True)
                continue
            if state in ("fail","failed","error"):
                print(f"  ✗ {j['slug']}/{j['file']} FAILED {data.get('failMsg')}", flush=True)
                continue
        except Exception as e:
            print(f"  . {j['slug']}/{j['file']}: {e}", flush=True)
        still.append(j)
    pending = still
    if pending:
        print(f"  [{len(pending)} pending]", flush=True); time.sleep(8)
M.write_text(json.dumps(jobs, ensure_ascii=False, indent=1))
print(f"\n== DOWNLOADED {done}/{len(jobs)} ==")
for j in jobs:
    if not j.get("ok"): print(f"  MISSING {j['slug']}/{j['file']} tid={j['tid']}")
