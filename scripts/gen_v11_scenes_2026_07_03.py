#!/usr/bin/env python3
"""Generate the V11 10x-visual sample scenes (2 stories × 5) via KIE Nano Banana Pro.
Prompts come from the Visual-Bible story packages (/tmp/pkg_0.json, /tmp/pkg_1.json)."""
from __future__ import annotations
import json, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_2026_05_28 import IMG_ROOT, POLL_INTERVAL, STATUS_URL, submit, http_get, first_image_url, download  # type: ignore


def submit_retry(p, tries=5):
    last = None
    for i in range(tries):
        try: return submit(p)
        except Exception as e: last = e; time.sleep(3*(i+1))
    raise last


def main():
    jobs = []
    for pkg_file in ("/tmp/pkg_0.json", "/tmp/pkg_1.json"):
        pkg = json.loads(Path(pkg_file).read_text())
        slug = pkg["slug"]
        for sc in pkg["scenes"]:
            out = IMG_ROOT / slug / sc["file"]
            if out.exists() and out.stat().st_size > 50_000:
                print(f"  = skip {slug}/{sc['file']}"); continue
            try:
                tid = submit_retry(sc["prompt"])
                jobs.append({"slug": slug, "file": sc["file"], "out": out, "tid": tid, "ok": False})
                print(f"  + {slug}/{sc['file']} {tid}", flush=True)
            except Exception as e:
                print(f"  ! submit {slug}/{sc['file']}: {e}", file=sys.stderr, flush=True)
            time.sleep(0.8)

    pending = [j for j in jobs if j.get("tid")]
    print(f"\n== polling {len(pending)} ==", flush=True)
    deadline = time.time() + 18*60
    while pending and time.time() < deadline:
        time.sleep(POLL_INTERVAL)
        still = []
        for j in pending:
            try: r = http_get(f"{STATUS_URL}?taskId={j['tid']}")
            except Exception: still.append(j); continue
            data = r.get("data") or {}
            st = data.get("state")
            if st == "success":
                url = first_image_url(data)
                if not url: still.append(j); continue
                try: download(url, j["out"]); j["ok"] = True; print(f"  ✓ {j['slug']}/{j['file']}", flush=True)
                except Exception as e: print(f"  ! dl {j['file']}: {e}", file=sys.stderr); still.append(j)
            elif st == "fail":
                print(f"  ✗ {j['slug']}/{j['file']} FAIL {str(data)[:100]}", file=sys.stderr)
            else: still.append(j)
        pending = still
        print(f"  ... {len(pending)} pending", flush=True)
    ok = sum(1 for j in jobs if j["ok"])
    print(f"\n== DONE {ok}/{len(jobs)} ==")
    for j in jobs:
        if not j["ok"]: print(f"  MISSING {j['slug']}/{j['file']}")
    return 0 if ok == len(jobs) else 1


if __name__ == "__main__":
    sys.exit(main())
