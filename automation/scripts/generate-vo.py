#!/usr/bin/env python3
"""DEPRECATED — V9 (2026-05-26). Voice-over killed per Ahmed feedback:
"I don't need the voice over kill it … it's not synced.. not iraqi."
VO fields (voScript / voicePath / voiceDurationSeconds) removed from schema.
This script is kept for reference only — it should NOT be called.

V8 leap (2026-05-10) — generate Arabic voice-over per reel via edge-tts (ARCHIVED).

For each post folder under data/posts/<date>-* the script:
  1. Reads .meta/props.json
  2. Pulls the new `voScript` field (Arabic narration, 60-90 words)
  3. Generates voice.mp3 inside the post's .meta/ folder using
     ar-IQ-BasselNeural (Iraqi-male neural voice — free, no auth)
  4. Probes the resulting mp3 for duration; writes it into the props as
     `voiceDurationSeconds` so the composition can sync visuals to VO
  5. Sets `voicePath` field so the renderer knows where to find the audio

Usage:
    python3 automation/scripts/generate-vo.py 2026-05-10
    python3 automation/scripts/generate-vo.py 2026-05-10 --voice ar-IQ-BasselNeural

Voice register selection: Iraqi-Levantine male, mid-chest, conversational.
We use ar-IQ-BasselNeural because:
  - It's the canonical Iraqi neural voice (Bagdadi-flavored MSA)
  - Lands as familiar to the diaspora target audience
  - Sits in the AJ-documentary register the watch dossiers identified

Per-reel target: 60-90 Arabic words ≈ 30-40 seconds at 1.85 wps. Edge TTS
runs slightly slower than ElevenLabs, so we add `--rate +5%` for the
right cinematic-news pace.
"""
from __future__ import annotations

import argparse
import asyncio
import json
import subprocess
import sys
from pathlib import Path

try:
    import edge_tts
except ImportError:
    print("error: edge-tts not installed. Run:", file=sys.stderr)
    print("  pip3 install --user --break-system-packages edge-tts", file=sys.stderr)
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[2]
POSTS = ROOT / "data" / "posts"

DEFAULT_VOICE = "ar-IQ-BasselNeural"
# +15% rate (was +5%) — keeps VO under the 34-second reel runtime even for
# the longest 70-word scripts. Sounds slightly more energetic / news-anchor.
RATE = "+15%"


def probe_duration(mp3: Path) -> float:
    """ffprobe a generated mp3 and return its duration in seconds."""
    try:
        out = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "default=noprint_wrappers=1:nokey=1", str(mp3)],
            capture_output=True, text=True, timeout=8,
        )
        return float(out.stdout.strip())
    except Exception:
        return 0.0


async def synth_one(slug: str, script: str, voice: str, dest: Path) -> tuple[bool, str]:
    """Synthesize one VO mp3. Returns (success, message)."""
    if not script or not script.strip():
        return False, "empty voScript"
    dest.parent.mkdir(parents=True, exist_ok=True)
    try:
        communicate = edge_tts.Communicate(script, voice, rate=RATE)
        await communicate.save(str(dest))
    except Exception as e:
        return False, f"edge-tts error: {e}"
    if not dest.is_file() or dest.stat().st_size < 5_000:
        return False, f"output too small ({dest.stat().st_size if dest.is_file() else 0} bytes)"
    return True, "ok"


async def main_async(date: str, voice: str) -> int:
    slugs = sorted(d for d in POSTS.glob(f"{date}-*") if d.is_dir())
    if not slugs:
        print(f"error: no posts under {POSTS}/{date}-*", file=sys.stderr)
        return 2

    print(f"━━━ V8 VO generation — {date} ({len(slugs)} reels, voice={voice}) ━━━")
    ok, fail = 0, 0
    for slug_dir in slugs:
        slug = slug_dir.name
        props_path = slug_dir / ".meta" / "props.json"
        if not props_path.is_file():
            print(f"  skip {slug}: no props.json")
            fail += 1
            continue
        with props_path.open() as f:
            props = json.load(f)
        script = props.get("voScript")
        if not script:
            print(f"  skip {slug}: voScript field missing")
            fail += 1
            continue

        # Output goes inside .meta/ so cloud-media staging doesn't accidentally
        # ship it as image content. We also DON'T put it under
        # my-video/public/audio/ — instead the cloud workflow stages it the
        # same way it stages broll photos: cloud-media path → public path.
        dest = slug_dir / ".meta" / "voice.mp3"
        word_count = len(script.split())
        ok_synth, msg = await synth_one(slug, script, voice, dest)
        if not ok_synth:
            print(f"  FAIL {slug}: {msg}")
            fail += 1
            continue
        duration = probe_duration(dest)
        size_kb = dest.stat().st_size // 1024
        print(f"  ✓ {slug:60s} {word_count:3d}w → {duration:5.1f}s {size_kb:4d}KB")

        # Write voice metadata back into props
        props["voicePath"] = f"voice/{slug}.mp3"  # composition-side path (staged from cloud-media)
        props["voiceDurationSeconds"] = round(duration, 2)
        props["voiceVoiceId"] = voice
        with props_path.open("w") as f:
            json.dump(props, f, ensure_ascii=False, indent=2)
            f.write("\n")
        ok += 1

    print(f"\n{ok} VO(s) generated, {fail} failed")
    return 0 if fail == 0 else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("date", help="YYYY-MM-DD")
    ap.add_argument("--voice", default=DEFAULT_VOICE,
                    help=f"edge-tts voice id (default {DEFAULT_VOICE})")
    args = ap.parse_args()
    return asyncio.run(main_async(args.date, args.voice))


if __name__ == "__main__":
    sys.exit(main())
