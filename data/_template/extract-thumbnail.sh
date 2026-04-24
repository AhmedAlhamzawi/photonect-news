#!/usr/bin/env bash
# extract-thumbnail.sh — extract the brightest single frame from a reel as an IG grid thumbnail.
#
# Usage:
#   ./extract-thumbnail.sh <slug>             # → data/posts/<slug>/thumbnail.jpg
#   ./extract-thumbnail.sh --all              # → process all posts with a video.mp4
#
# The script samples 10 evenly-spaced candidate frames, measures mean luminance
# via ffprobe/lavfi, and writes the brightest one as a 1080×1920 JPEG.
# IG grid shows a 1:1 crop of the top of the frame, so brightest = most legible.

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
POSTS="$ROOT/data/posts"

pick_thumbnail() {
    local slug="$1"
    local post="$POSTS/$slug"
    local mp4

    # Prefer new video.mp4 layout, fall back to legacy newsreel_v3/v2/v1 names
    if   [ -f "$post/video.mp4"       ]; then mp4="$post/video.mp4"
    elif [ -f "$post/newsreel_v3.mp4" ]; then mp4="$post/newsreel_v3.mp4"
    elif [ -f "$post/newsreel_v2.mp4" ]; then mp4="$post/newsreel_v2.mp4"
    elif [ -f "$post/newsreel.mp4"    ]; then mp4="$post/newsreel.mp4"
    else
        echo "  skip $slug: no mp4 found" >&2
        return 0
    fi

    local out="$post/thumbnail.jpg"
    local duration
    duration=$(ffprobe -v error -show_entries format=duration \
        -of default=noprint_wrappers=1:nokey=1 "$mp4" 2>/dev/null)

    if [ -z "$duration" ]; then
        echo "  skip $slug: could not probe duration" >&2
        return 0
    fi

    # Sample 10 frames, skip the first and last 5% (usually fade-in/out)
    local n=10
    local best_t="0"
    local best_lum="-1"

    for i in $(seq 1 "$n"); do
        # t = 5% + (i-1)/(n-1) * 90% of duration
        local t
        t=$(python3 -c "print(round($duration * (0.05 + ($i - 1) / ($n - 1) * 0.90), 2))" 2>/dev/null) || continue
        # Use ffmpeg -ss frame extraction + Pillow mean-L (authoritative method).
        # The ffprobe signalstats lavfi method returns a constant L≈13 regardless
        # of seek point (run-3 discovery: lavfi seek_point does not actually seek).
        local lum
        lum=$(python3 - "$mp4" "$t" 2>/dev/null << 'PYEOF'
import sys, subprocess, tempfile, os
from PIL import Image
import numpy as np
mp4, t = sys.argv[1], sys.argv[2]
tmp = tempfile.mktemp(suffix=".jpg")
try:
    r = subprocess.run(
        ["ffmpeg","-y","-v","error","-ss",t,"-i",mp4,"-vframes","1","-q:v","2",tmp],
        capture_output=True, timeout=15)
    if r.returncode != 0 or not os.path.exists(tmp):
        sys.exit(1)
    img = Image.open(tmp).convert("L")
    print(round(float(np.array(img).mean()), 2))
finally:
    try: os.unlink(tmp)
    except: pass
PYEOF
) || continue
        if [ -z "$lum" ]; then continue; fi
        if python3 -c "exit(0 if float('$lum') > float('$best_lum') else 1)" 2>/dev/null; then
            best_lum="$lum"
            best_t="$t"
        fi
    done

    # Extract the chosen frame
    ffmpeg -y -v error -ss "$best_t" -i "$mp4" \
        -vframes 1 -q:v 2 "$out" 2>/dev/null
    echo "  ✓ $slug → thumbnail.jpg (t=${best_t}s, L=${best_lum})"
}

if [ "${1:-}" = "--all" ]; then
    for post_dir in "$POSTS"/*/; do
        slug="$(basename "$post_dir")"
        pick_thumbnail "$slug"
    done
elif [ -n "${1:-}" ]; then
    pick_thumbnail "$1"
else
    echo "usage: $0 <slug> | --all" >&2
    exit 2
fi
