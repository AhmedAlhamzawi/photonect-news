#!/usr/bin/env python3
"""Download Higgsfield Nano Banana Pro renders into my-video/public/images/news/<slug>/.

KIE (Nano Banana Pro via kie.ai) returned HTTP 402 — credits exhausted — for the
second day running, so the 2026-07-28 slate was generated on Higgsfield's
nano_banana_pro instead (same underlying model, different vendor). The MCP tool
hands back a CloudFront URL per job; this script just fetches them to disk and
normalises to JPEG at the size the reel expects.

Usage:
    python3 scripts/hf_download_2026_07_28.py manifest.json

manifest.json: [{"slug": "...", "file": "hero.jpg", "url": "https://..."}, ...]
"""
from __future__ import annotations

import json
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IMG_ROOT = ROOT / "my-video/public/images/news"

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 photonect-news/1.0"


def fetch(url: str, dest: Path) -> str:
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_suffix(".download.png")
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=180) as r, tmp.open("wb") as fh:
        fh.write(r.read())
    # PNG at 1536x2752 is ~11MB; the reel wants a JPEG. sips keeps it lossless-ish
    # at q=90 and drops the file to ~1MB, which also keeps the repo sane.
    subprocess.run(
        ["sips", "-s", "format", "jpeg", "-s", "formatOptions", "85",
         str(tmp), "--out", str(dest)],
        check=True, capture_output=True,
    )
    tmp.unlink(missing_ok=True)
    out = subprocess.run(
        ["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(dest)],
        capture_output=True, text=True,
    ).stdout
    dims = "x".join(w.split(":")[1].strip() for w in out.strip().splitlines()[1:3])
    return f"{dims}  {dest.stat().st_size // 1024}KB"


def main() -> int:
    manifest = json.loads(Path(sys.argv[1]).read_text())
    ok = 0
    for job in manifest:
        dest = IMG_ROOT / job["slug"] / job["file"]
        try:
            info = fetch(job["url"], dest)
            ok += 1
            print(f"  ✓ {job['slug']}/{job['file']}  {info}", flush=True)
        except Exception as e:
            print(f"  ! {job['slug']}/{job['file']}: {e}", file=sys.stderr, flush=True)
    print(f"\n== {ok}/{len(manifest)} downloaded ==")
    return 0 if ok == len(manifest) else 1


if __name__ == "__main__":
    raise SystemExit(main())
