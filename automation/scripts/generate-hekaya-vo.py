#!/usr/bin/env python3
"""Generate Hekaya v2 voice-over audio from script.txt.

Reads `data/hekaya/<slug>/.meta/script.txt`, runs macOS `say` with the
Majed (Arabic male) voice at a documentary pace, then converts the AIFF
to a normalized mp3 via ffmpeg.

This is the v1 VO pipeline — Majed is a built-in macOS voice. Quality is
acceptable but not premium. For v2-final we would swap in ElevenLabs
Arabic via API key. The script structure stays identical; only the TTS
backend changes.

Usage:
    python3 automation/scripts/generate-hekaya-vo.py <slug>
        e.g. 2026-05-04-fatima-al-fihri-qarawiyyin

The output mp3 lands at:
    my-video/public/audio/hekaya-vo/<slug>.mp3
"""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HEKAYA_DIR = ROOT / "data" / "hekaya"
VO_OUT_DIR = ROOT / "my-video" / "public" / "audio" / "hekaya-vo"

# Pacing: target 2.2-2.5 wps. macOS `say` default is ~175 wpm = 2.9 wps.
# Slowing to 130 wpm gives 2.17 wps — closer to documentary pacing.
SAY_RATE_WPM = 130
SAY_VOICE = "Majed"  # Arabic male, built-in on macOS

# ffmpeg loudnorm target — broadcast standard.
LOUDNORM = "loudnorm=I=-16:TP=-1:LRA=11"


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: generate-hekaya-vo.py <slug>", file=sys.stderr)
        return 2
    slug = sys.argv[1]

    if not shutil.which("say"):
        print("error: macOS `say` not available — must run on Mac", file=sys.stderr)
        return 2
    if not shutil.which("ffmpeg"):
        print("error: ffmpeg not on PATH", file=sys.stderr)
        return 2

    script_path = HEKAYA_DIR / slug / ".meta" / "script.txt"
    if not script_path.is_file():
        print(f"error: script missing at {script_path}", file=sys.stderr)
        return 2

    raw = script_path.read_text(encoding="utf-8").strip()
    if not raw:
        print(f"error: script empty at {script_path}", file=sys.stderr)
        return 2

    # Strip phase header lines that the storyteller agent emits like:
    #   [COLD OPEN — 0-2s, ~6 words]
    # Those are for human readability of the script.txt — they should NOT
    # be read aloud by the TTS. Anything between [ ... ] gets dropped.
    cleaned_lines = []
    for line in raw.splitlines():
        line = line.strip()
        if not line or line.startswith("["):
            continue
        cleaned_lines.append(line)
    script_text = "\n\n".join(cleaned_lines)

    if not script_text:
        print(f"error: script has no Arabic content after header strip", file=sys.stderr)
        return 2

    word_count = len(script_text.split())
    print(f"━━━ HEKAYA v2 VO — {slug} ━━━")
    print(f"  script: {word_count} words")
    print(f"  voice:  {SAY_VOICE} @ {SAY_RATE_WPM} wpm")

    VO_OUT_DIR.mkdir(parents=True, exist_ok=True)
    aiff = VO_OUT_DIR / f"{slug}.aiff"
    mp3 = VO_OUT_DIR / f"{slug}.mp3"

    # 1) Run say to generate AIFF
    cmd = [
        "say",
        "-v", SAY_VOICE,
        "-r", str(SAY_RATE_WPM),
        "-o", str(aiff),
        script_text,
    ]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(f"  FAIL say: {r.stderr}", file=sys.stderr)
        return 1
    aiff_bytes = aiff.stat().st_size
    print(f"  aiff:   {aiff_bytes / 1024:.0f} KB")

    # 2) Convert AIFF → MP3 with loudnorm normalization
    cmd2 = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-i", str(aiff),
        "-af", LOUDNORM,
        "-codec:a", "libmp3lame",
        "-b:a", "128k",
        "-ar", "44100",
        str(mp3),
    ]
    r = subprocess.run(cmd2, capture_output=True, text=True)
    if r.returncode != 0:
        print(f"  FAIL ffmpeg: {r.stderr}", file=sys.stderr)
        return 1

    # Cleanup AIFF
    aiff.unlink()

    mp3_bytes = mp3.stat().st_size
    # Probe duration via ffprobe-ish approach
    r2 = subprocess.run(
        ["ffmpeg", "-i", str(mp3), "-f", "null", "-"],
        capture_output=True, text=True,
    )
    duration_line = [
        line for line in r2.stderr.splitlines() if "Duration:" in line
    ]
    duration = duration_line[0].split("Duration:")[1].split(",")[0].strip() if duration_line else "?"

    print(f"  mp3:    {mp3.name} ({mp3_bytes / 1024:.0f} KB, {duration})")
    print(f"  ✓ saved to {mp3}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
