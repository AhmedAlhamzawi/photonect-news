#!/usr/bin/env python3
"""Download the 2026-09-06 Higgsfield frames into the engine's image dirs.

KIE credit balance was -5.5 at submission time (HTTP 402 territory, unchanged
since 27 July), so every frame in this slate comes from Higgsfield
nano_banana_pro at 9:16 / 2k — the standing fallback, not stock.

Manifest-driven: reads scripts/_scene_urls_2026_09_06.json, a list of
  {"slug": ..., "file": "hero.jpg", "url": "https://..."}
entries, and writes my-video/public/images/news/<slug>/<file>.

Usage:  python3 scripts/fetch_scenes_2026_08_17.py [--force] [slug ...]
Re-runnable: skips entries whose file already exists unless --force.
"""
from __future__ import annotations

import io
import json
import sys
import urllib.request
from pathlib import Path

from PIL import Image  # type: ignore

ROOT = Path(__file__).resolve().parent.parent
IMG_ROOT = ROOT / "my-video" / "public" / "images" / "news"
MANIFEST = ROOT / "scripts" / "_scene_urls_2026_09_06.json"


def fetch(url: str, out: Path) -> tuple[int, int]:
    req = urllib.request.Request(url, headers={"User-Agent": "photonect/1.0"})
    with urllib.request.urlopen(req, timeout=180) as r:
        raw = r.read()
    im = Image.open(io.BytesIO(raw))
    if im.mode != "RGB":
        im = im.convert("RGB")
    out.parent.mkdir(parents=True, exist_ok=True)
    im.save(out, "JPEG", quality=93)
    return im.size


def main() -> int:
    args = sys.argv[1:]
    force = "--force" in args
    only = [a for a in args if not a.startswith("--")]

    frames = json.loads(MANIFEST.read_text(encoding="utf-8"))
    missing: list[str] = []
    for fr in frames:
        slug, name, url = fr["slug"], fr["file"], fr.get("url")
        if only and not any(o in slug for o in only):
            continue
        out = IMG_ROOT / slug / name
        if not url:
            missing.append(f"{slug}/{name} (no url yet)")
            continue
        if out.exists() and not force:
            print(f"  skip  {slug}/{name} (exists)")
            continue
        try:
            w, h = fetch(url, out)
        except Exception as exc:  # noqa: BLE001
            missing.append(f"{slug}/{name} ({exc})")
            continue
        flag = "" if h > w else "   <-- NOT PORTRAIT, CHECK"
        print(f"  ok    {slug}/{name}  {w}x{h}{flag}")

    if missing:
        print("\nMISSING:")
        for m in missing:
            print(f"  {m}")
    print(f"\n== {len(frames)} frames in manifest · {len(missing)} missing ==")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
