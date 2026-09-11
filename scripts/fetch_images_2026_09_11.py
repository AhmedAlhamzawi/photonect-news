#!/usr/bin/env python3
"""Download Higgsfield renders into my-video/public/images/news/<slug>/ per the job manifest."""
import json, sys, subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
MAN = json.load(open(ROOT / "scripts/_higgsfield_jobs_2026_09_11.json"))["map"]
URLS = json.load(open(sys.argv[1] if len(sys.argv) > 1 else "scripts/_urls_2026_09_11.json"))
for idx, url in URLS.items():
    e = MAN[idx]
    dest = ROOT / "my-video/public/images/news" / e["slug"] / e["file"]
    dest.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["curl", "-sSL", "-o", str(dest), url], check=True)
    # normalise PNG -> JPG in place (files are named .jpg); sips keeps it simple on macOS
    subprocess.run(["sips", "-s", "format", "jpeg", str(dest), "--out", str(dest)],
                   check=True, capture_output=True)
    print(f"  {idx:>2} -> {e['slug']}/{e['file']}")
print(f"{len(URLS)} images fetched")
