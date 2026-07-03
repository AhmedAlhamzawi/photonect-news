#!/usr/bin/env python3
"""V11 VO spine — generate the narrator track + word-level timestamps that DRIVE the reel.

The V11 format inverts V10: voice first, visuals cut to it. This script takes a
VO script (Arabic, MSA newscast register) and produces:
    vo.mp3       — the narration audio
    words.json   — [{word, start, end}, ...] seconds, word-level (karaoke captions + cut timing)

Engines:
  - elevenlabs (PRIMARY when ELEVENLABS_API_KEY is set): eleven_v3/multilingual TTS
    with character-level timestamps → folded into words. Broadcast-grade Arabic.
  - edge (FALLBACK, free, no key): Edge TTS neural Arabic voices; WordBoundary
    events give word timestamps natively. Quality: clean newscast, less rich.

Usage:
    python3 automation/scripts/generate-vo-v11.py --text-file script.txt --out-dir out/
    python3 automation/scripts/generate-vo-v11.py --text "..." --out-dir out/ --engine edge
    # engine auto: elevenlabs if key present, else edge
"""
from __future__ import annotations

import argparse
import asyncio
import base64
import json
import os
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# Broadcast MSA default. ar-IQ-BasselNeural = Iraqi-flavored MSA (identity without dialect-TTS risk).
EDGE_VOICE = os.environ.get("V11_EDGE_VOICE", "ar-IQ-BasselNeural")
EDGE_RATE = os.environ.get("V11_EDGE_RATE", "+8%")   # newscast pace, slightly brisk
ELEVEN_VOICE_ID = os.environ.get("ELEVENLABS_VOICE_ID", "")  # set after voice selection
ELEVEN_MODEL = os.environ.get("ELEVENLABS_MODEL", "eleven_multilingual_v2")

PERSIAN = {"ی", "ک"}  # ی ک — hard guard before any TTS


def load_env_key(name: str) -> str:
    v = os.environ.get(name, "").strip()
    if v:
        return v
    for envf in (ROOT / ".env", ROOT / ".env.local"):
        if envf.is_file():
            for line in envf.read_text().splitlines():
                m = re.match(rf"\s*(?:export\s+)?{name}\s*=\s*(.+)\s*$", line)
                if m:
                    return m.group(1).strip().strip('"').strip("'")
    return ""


def guard(text: str) -> None:
    bad = sorted({c for c in text if c in PERSIAN})
    if bad:
        sys.exit(f"PERSIAN-CHAR GUARD: {[hex(ord(c)) for c in bad]} in VO text — fix before TTS.")


# ── Edge TTS (fallback, free) ────────────────────────────────────────────────
async def _edge_generate(text: str, out_mp3: Path) -> list[dict]:
    import edge_tts
    words: list[dict] = []
    com = edge_tts.Communicate(text, EDGE_VOICE, rate=EDGE_RATE, boundary="WordBoundary")
    with out_mp3.open("wb") as f:
        async for chunk in com.stream():
            if chunk["type"] == "audio":
                f.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                start = chunk["offset"] / 1e7                       # 100ns → s
                dur = chunk.get("duration", 0) / 1e7
                words.append({"word": chunk["text"], "start": round(start, 3),
                              "end": round(start + max(dur, 0.05), 3)})
    return words


def edge_generate(text: str, out_mp3: Path) -> list[dict]:
    return asyncio.run(_edge_generate(text, out_mp3))


# ── ElevenLabs (primary) ─────────────────────────────────────────────────────
def eleven_generate(text: str, out_mp3: Path, api_key: str) -> list[dict]:
    """with-timestamps endpoint → char-level alignment folded into words."""
    voice = ELEVEN_VOICE_ID or "21m00Tcm4TlvDq8ikWAM"  # placeholder until a voice is chosen
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice}/with-timestamps"
    body = {"text": text, "model_id": ELEVEN_MODEL,
            "voice_settings": {"stability": 0.55, "similarity_boost": 0.8, "style": 0.25}}
    req = urllib.request.Request(url, data=json.dumps(body).encode(), method="POST",
        headers={"xi-api-key": api_key, "Content-Type": "application/json", "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=180) as r:
        resp = json.loads(r.read().decode())
    out_mp3.write_bytes(base64.b64decode(resp["audio_base64"]))
    al = resp.get("alignment") or resp.get("normalized_alignment")
    chars, starts, ends = al["characters"], al["character_start_times_seconds"], al["character_end_times_seconds"]
    words, cur, w_start, w_end = [], "", None, None
    for c, s, e in zip(chars, starts, ends):
        if c.strip():
            if not cur:
                w_start = s
            cur += c
            w_end = e
        elif cur:
            words.append({"word": cur, "start": round(w_start, 3), "end": round(w_end, 3)})
            cur = ""
    if cur:
        words.append({"word": cur, "start": round(w_start, 3), "end": round(w_end, 3)})
    return words


def probe_duration(mp3: Path) -> float:
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "csv=p=0", str(mp3)], capture_output=True, text=True).stdout.strip()
    return float(out) if out else 0.0


def main() -> int:
    ap = argparse.ArgumentParser()
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--text")
    src.add_argument("--text-file")
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--engine", choices=["auto", "elevenlabs", "edge"], default="auto")
    args = ap.parse_args()

    text = args.text if args.text else Path(args.text_file).read_text(encoding="utf-8")
    text = " ".join(text.split())  # normalize whitespace/newlines for clean word timing
    guard(text)

    out_dir = Path(args.out_dir); out_dir.mkdir(parents=True, exist_ok=True)
    mp3, wjson = out_dir / "vo.mp3", out_dir / "words.json"

    key = load_env_key("ELEVENLABS_API_KEY")
    engine = args.engine
    if engine == "auto":
        engine = "elevenlabs" if key else "edge"
    if engine == "elevenlabs" and not key:
        print("no ELEVENLABS_API_KEY — falling back to edge", file=sys.stderr)
        engine = "edge"

    print(f"engine={engine} words_in={len(text.split())}")
    if engine == "elevenlabs":
        words = eleven_generate(text, mp3, key)
    else:
        words = edge_generate(text, mp3)

    if not words:
        sys.exit("no word timestamps produced — HOLD (do not render without sync)")
    dur = probe_duration(mp3)
    # sanity: last word must end within the audio, timings monotonic
    if words[-1]["end"] > dur + 1.5:
        sys.exit(f"timing sanity failed: last word ends {words[-1]['end']}s but audio is {dur}s — HOLD")
    wjson.write_text(json.dumps({"engine": engine, "voice": (ELEVEN_VOICE_ID or EDGE_VOICE) if engine == "elevenlabs" else EDGE_VOICE,
                                 "durationSeconds": round(dur, 3), "words": words},
                                ensure_ascii=False, indent=1))
    print(f"vo.mp3 {dur:.1f}s · {len(words)} words · {wjson}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
