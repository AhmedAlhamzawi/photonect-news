#!/usr/bin/env python3
"""Pre-flight verifier for the 2026-08-19 slate. Safe to re-run after every copy edit.

Checks, per slug:
  1. props.json / caption.txt exist and parse
  2. v11-brief.json (where expected) parses; control slug has none
  3. every statPop matchWord appears EXACTLY ONCE in its own voText
  4. voText contains ZERO commas (the 08-13 karaoke word-join bug, avoided by construction)
  5. voText word count is inside the 70-85 band the brief asks for
  6. no Persian yeh/kaf (U+06CC / U+06A9) anywhere in props, brief or caption
  7. no U+2212 minus sign (tofu/bidi risk inside an RTL pill)
  8. every image path referenced actually exists on disk
  9. exactly 2 statPops per brief (V11 hard cap)
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "data" / "posts"
IMG_ROOT = ROOT / "my-video" / "public"
D = "2026-08-19"
CONTROL = f"{D}-ghalibaf-baghdad-deadline"

PERSIAN = {"ی": "PERSIAN YEH", "ک": "PERSIAN KAF"}
MINUS = "−"

fail: list[str] = []
warn: list[str] = []


def check_text(where: str, text: str) -> None:
    for ch, name in PERSIAN.items():
        if ch in text:
            fail.append(f"{where}: contains {name} ({ch!r})")
    if MINUS in text:
        fail.append(f"{where}: contains U+2212 MINUS SIGN — use ASCII '-'")


def main() -> int:
    slugs = sorted(p for p in POSTS.glob(f"{D}-*") if p.is_dir())
    if len(slugs) != 5:
        fail.append(f"expected 5 slugs, found {len(slugs)}")

    for folder in slugs:
        slug = folder.name
        meta = folder / ".meta"
        pj, bj, cap = meta / "props.json", meta / "v11-brief.json", folder / "caption.txt"

        if not pj.exists():
            fail.append(f"{slug}: props.json MISSING")
            continue
        props = json.loads(pj.read_text(encoding="utf-8"))
        check_text(f"{slug}/props", pj.read_text(encoding="utf-8"))

        if not cap.exists():
            fail.append(f"{slug}: caption.txt MISSING")
        else:
            check_text(f"{slug}/caption", cap.read_text(encoding="utf-8"))

        # image paths on disk
        paths = [props["breaking"]["heroMedia"]] + [b["broll"] for b in props["beats"]]
        for rel in paths:
            if not (IMG_ROOT / rel).exists():
                fail.append(f"{slug}: image missing on disk -> {rel}")

        # engine split
        if slug == CONTROL:
            if bj.exists():
                fail.append(f"{slug}: is the V10.1 control but has a v11-brief.json")
            print(f"  {slug}: V10.1 control (no brief)  beats={len(props['beats'])}")
            continue

        if not bj.exists():
            fail.append(f"{slug}: v11-brief.json MISSING")
            continue
        brief = json.loads(bj.read_text(encoding="utf-8"))
        check_text(f"{slug}/brief", bj.read_text(encoding="utf-8"))

        vo = brief["voText"]
        if "," in vo or "،" in vo:
            fail.append(f"{slug}: voText CONTAINS A COMMA — karaoke word-join risk")

        words = len(vo.split())
        if not (70 <= words <= 85):
            warn.append(f"{slug}: voText is {words} words (brief asks 70-85)")

        pops = brief.get("statPops", [])
        if len(pops) != 2:
            fail.append(f"{slug}: {len(pops)} statPops — V11 caps at 2, expected exactly 2")

        for p in pops:
            mw = p["matchWord"]
            n = vo.count(mw)
            if n == 0:
                fail.append(f"{slug}: matchWord {mw!r} ABSENT from voText -> pop would be silently dropped")
            elif n > 1:
                fail.append(f"{slug}: matchWord {mw!r} appears {n}x in voText -> ambiguous anchor")

        for rel in brief["images"]:
            if not (IMG_ROOT / rel).exists():
                fail.append(f"{slug}: brief image missing on disk -> {rel}")

        print(f"  {slug}: V11  vo={words}w  pops={len(pops)}  "
              f"anchors={[p['matchWord'] for p in pops]}")

    print()
    for w in warn:
        print(f"  WARN  {w}")
    for f in fail:
        print(f"  FAIL  {f}")
    print(f"\n== {len(fail)} failures · {len(warn)} warnings ==")
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
