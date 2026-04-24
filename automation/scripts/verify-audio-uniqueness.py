#!/usr/bin/env python3
"""Verify 12 rendered reels have 12 audibly distinct audio tracks.

Ahmed's V5 feedback: "All the music is the same."
Ahmed's V6 feedback: "The music you did not change it. It is the same.
                      There is one video that has a new music and it's bullshit."

This is the final line of defence before handoff. Extracts a stable
audio fingerprint from each rendered mp4 (not just file-level MD5 of the
bed — what the user actually hears):

  - 10-second PCM slice at 5s offset
  - MD5 of the raw audio bytes (pre-encoding noise eliminated)
  - Mean volume check (must be > -50 dB)

Reports:
  - 12 unique fingerprints? ✓ / ✗
  - 12 audible tracks? ✓ / ✗
  - Any collisions? list them
"""

from __future__ import annotations

import hashlib
import subprocess
import sys
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE")
POSTS = ROOT / "data" / "posts"
DATE = "2026-04-22"


def sample_audio(mp4: Path) -> dict:
    """Extract 10s PCM slice starting 5s in, return md5 + mean volume."""
    if not mp4.exists():
        return {"ok": False, "reason": "mp4 missing"}
    try:
        pcm = subprocess.run(
            ["ffmpeg", "-v", "error", "-ss", "5", "-t", "10", "-i", str(mp4),
             "-ac", "1", "-ar", "22050", "-f", "s16le", "-"],
            capture_output=True, timeout=20, check=True,
        ).stdout
        md5 = hashlib.md5(pcm).hexdigest()
    except subprocess.CalledProcessError as e:
        return {"ok": False, "reason": f"ffmpeg fail: {e.stderr.decode()[:100]}"}

    vd = subprocess.run(
        ["ffmpeg", "-hide_banner", "-ss", "5", "-t", "10", "-i", str(mp4),
         "-ac", "1", "-af", "volumedetect", "-f", "null", "-"],
        capture_output=True, text=True, timeout=15,
    )
    mean = None
    for line in vd.stderr.splitlines():
        if "mean_volume:" in line:
            try:
                mean = float(line.split("mean_volume:")[1].strip().split()[0])
            except Exception:
                pass
            break

    return {
        "ok": True,
        "md5": md5[:12],
        "mean_db": mean,
        "audible": (mean is not None and mean > -50),
    }


def main():
    slugs = sorted([d.name for d in POSTS.glob(f"{DATE}-*") if d.is_dir()])
    if not slugs:
        print("No slugs found.", file=sys.stderr)
        sys.exit(1)

    print(f"Auditing {len(slugs)} rendered reels...\n")
    results = {}
    md5_buckets: dict[str, list[str]] = {}
    for slug in slugs:
        mp4 = POSTS / slug / "video.mp4"
        r = sample_audio(mp4)
        results[slug] = r
        if r.get("ok"):
            status = "✓" if r["audible"] else "⚠"
            print(f"  {status} {slug:42s}  md5={r['md5']}  mean={r['mean_db']:+.1f} dB")
            md5_buckets.setdefault(r["md5"], []).append(slug)
        else:
            print(f"  ✗ {slug:42s}  {r['reason']}")

    print()
    unique = len(md5_buckets)
    audible = sum(1 for r in results.values() if r.get("audible"))
    print(f"Unique fingerprints: {unique}/{len(slugs)}")
    print(f"Audible tracks:      {audible}/{len(slugs)}")

    collisions = {h: slugs for h, slugs in md5_buckets.items() if len(slugs) > 1}
    if collisions:
        print("\n⚠ COLLISIONS:")
        for h, slugs in collisions.items():
            print(f"  {h}  ← {slugs}")
        sys.exit(2)
    if audible < len(slugs):
        print("\n⚠ Silent tracks detected — review above.")
        sys.exit(2)
    print("\n✓ all tracks unique + audible")


if __name__ == "__main__":
    main()
