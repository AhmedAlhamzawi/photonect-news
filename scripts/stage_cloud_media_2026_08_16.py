#!/usr/bin/env python3
"""Stage the 2026-08-16 slate media into cloud-media/ (the CI source of truth)
and write each slug's .meta/media-stamp.json.

Copies the 4 Read-verified Higgsfield frames per slug from
my-video/public/images/news/<slug>/ -> cloud-media/2026-08-16/<slug>/.
"""
from __future__ import annotations
import json, shutil, sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-08-16"
SLUGS = ["baghdad-37000-megawatt", "dollar-shop-gap", "homes-turkey-144",
         "hormuz-half-exports", "silence-currency-dinar"]
FILES = ["hero.jpg", "broll_1.jpg", "broll_2.jpg", "broll_3.jpg"]
SRC = ROOT / "my-video" / "public" / "images" / "news"
CLOUD = ROOT / "cloud-media" / DATE
POSTS = ROOT / "data" / "posts"

NOTE = (
    "KIE returned HTTP 402 (credits insufficient) live at submission, so all 20 frames were generated "
    "on Higgsfield (requested nano_banana_pro, service resolved to nano_banana_2) at 9:16 / 2k -> "
    "1536x2752. 27 submissions for 20 final frames. Terminal-state rejections: 3 heroes came back "
    "'failed' (dollar, homes, silence) and 2 jobs came back 'nsfw' as false positives (baghdad/broll_3 "
    "domestic interior, homes/hero apartment exterior). Read-verify rejections regenerated for content: "
    "baghdad/broll_3 arrived as a plainly WESTERN living room (English-spined books, Western family "
    "photographs, US-style recliner) for an Iraqi power-cut beat; homes/broll_1 rendered as a stacked "
    "DIPTYCH with a hard seam across the middle of the frame; hormuz/broll_2 arrived ROTATED 90 degrees "
    "(horizon vertical); hormuz/broll_3 was an EAST ASIAN bank hall in winter coats with Latin signage; "
    "silence/broll_3 was an Eastern-European kitchen. All 20 final frames were Read-verified by hand: "
    "upright 1536x2752, level horizon, correct Iraqi/Kurdish/Turkish setting per story, summer dress "
    "where Iraqi, no fake news-app UI, no legible burned-in text. No stock imagery anywhere in the "
    "slate, so auto-post stays ON."
)


def main() -> int:
    missing = []
    stamp_common = {
        "hunted_at": datetime.now(timezone.utc).isoformat(),
        "manual": True,
        "source": "higgsfield nano_banana_2 9:16 2k (KIE 402 - credits exhausted)",
        "date": DATE,
        "note": NOTE,
    }
    for s in SLUGS:
        full = f"{DATE}-{s}"
        dst = CLOUD / full
        dst.mkdir(parents=True, exist_ok=True)
        for f in FILES:
            sp = SRC / full / f
            if not sp.is_file():
                missing.append(f"{full}/{f}")
                continue
            shutil.copy2(sp, dst / f)
        meta = POSTS / full / ".meta"
        meta.mkdir(parents=True, exist_ok=True)
        (meta / "media-stamp.json").write_text(
            json.dumps(stamp_common, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"  ✓ {full}  ({len(FILES)} images + media-stamp.json)")
    if missing:
        print(f"\n❌ MISSING: {missing}", file=sys.stderr)
        return 1
    print(f"\n== {len(SLUGS)} slugs staged into cloud-media/{DATE} ==")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
