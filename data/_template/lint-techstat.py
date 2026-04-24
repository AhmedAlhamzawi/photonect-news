#!/usr/bin/env python3
"""lint-techstat.py — verify every tech_ai post has a supportingStat with a numeric value.

Tech/AI reels lose credibility without numbers anchoring the claim. This lint
catches posts where the supportingStat field is absent or contains no digit.

Exit 0 = all clear. Exit 1 = violations found (list them to stdout).
"""
import json
import re
import sys
from pathlib import Path

POSTS = Path(__file__).parent.parent / "posts"
_NUMERIC = re.compile(r"\d")


def _has_numeric_stat(beats: list) -> bool:
    for beat in beats:
        if not isinstance(beat, dict):
            continue
        stat = beat.get("supportingStat")
        if stat is None:
            continue
        # stat can be a string or a dict with a "value" key
        if isinstance(stat, dict):
            val = str(stat.get("value", ""))
        else:
            val = str(stat)
        if _NUMERIC.search(val):
            return True
    return False


def lint(posts_dir: Path) -> list[tuple[str, str]]:
    issues: list[tuple[str, str]] = []
    for post_dir in sorted(posts_dir.iterdir()):
        if not post_dir.is_dir():
            continue
        props_path = post_dir / ".meta" / "props.json"
        if not props_path.exists():
            continue
        try:
            props = json.loads(props_path.read_text())
        except Exception as exc:
            issues.append((post_dir.name, f"JSON parse error: {exc}"))
            continue
        if props.get("topicBucket") != "tech_ai":
            continue
        beats = props.get("beats") or []
        if not _has_numeric_stat(beats):
            # Report which beats exist (helps writer know what to add)
            stat_summary = [
                b.get("supportingStat", "<missing>") if isinstance(b, dict) else "?"
                for b in beats
            ]
            issues.append((
                post_dir.name,
                f"no supportingStat with digit — beats: {stat_summary}",
            ))
    return issues


def main() -> int:
    if not POSTS.exists():
        print(f"error: posts dir not found: {POSTS}", file=sys.stderr)
        return 2

    issues = lint(POSTS)
    if issues:
        print(f"LINT FAIL — {len(issues)} tech_ai post(s) missing numeric supportingStat:")
        for slug, msg in issues:
            print(f"  ✗ {slug}: {msg}")
        return 1

    tech_ai_count = sum(
        1 for d in POSTS.iterdir()
        if d.is_dir() and (d / ".meta" / "props.json").exists()
        and json.loads((d / ".meta" / "props.json").read_text()).get("topicBucket") == "tech_ai"
    )
    print(f"LINT PASS — all {tech_ai_count} tech_ai post(s) have numeric supportingStat")
    return 0


if __name__ == "__main__":
    sys.exit(main())
