#!/usr/bin/env python3
"""Stage the 2026-08-13 slate media into cloud-media/ (the CI source of truth)
and write each slug's .meta/media-stamp.json.

Copies the 4 Read-verified Higgsfield frames per slug from
my-video/public/images/news/<slug>/ -> cloud-media/2026-08-13/<slug>/.
"""
from __future__ import annotations
import json, shutil, sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-08-13"
SLUGS = ["blackout-tar-diverted", "dollar-streak-breaks", "gold-mithqal-946",
         "salary-ninth-month", "tanker-basra-crude"]
FILES = ["hero.jpg", "broll_1.jpg", "broll_2.jpg", "broll_3.jpg"]
SRC = ROOT / "my-video" / "public" / "images" / "news"
CLOUD = ROOT / "cloud-media" / DATE
POSTS = ROOT / "data" / "posts"

NOTE = (
    "KIE returned HTTP 402 (credits insufficient) on submission for the day, so all 20 frames were "
    "generated on Higgsfield (requested nano_banana_pro, service resolved to nano_banana_2) at 9:16 / "
    "2k -> 1536x2752. 24 submissions for 20 final frames: 1 safety-filter rejection (dollar/broll_1 "
    "banknote still-life came back 'nsfw') re-prompted as a counter hand-off, and 3 Read-verify "
    "rejections regenerated for burned-in text: blackout/broll_3 arrived with a 'MARSHLAND GIANTS' "
    "caption bar, salary/broll_3 with a legible English 'CREDIT LEDGER' heading and Latin handwriting, "
    "and dollar/hero with garbled Arabic shopfront signage. All 20 final frames were Read-verified by "
    "hand: upright 1536x2752, correct Iraqi/Kurdish setting and summer dress for an August slate, no "
    "fake news-app UI, no legible or garbled text. No stock imagery anywhere in the slate, so auto-post "
    "stays ON."
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
