#!/usr/bin/env bash
# watch-video.sh — download a YouTube video, extract 6 keyframes, fetch transcript.
#
# Usage:
#   ./watch-video.sh <youtube_url> <out_dir>
#
# Output (in out_dir):
#   video.mp4          — capped 720p, ≤30 MB
#   frame_0s.jpg       — cold-open frame
#   frame_2s.jpg       — first hook
#   frame_5s.jpg       — second hook
#   frame_12s.jpg      — escalation
#   frame_30s.jpg      — climax/turn
#   frame_endish.jpg   — last 3-5 seconds (the loop hook)
#   transcript.txt     — auto-captions (.vtt or .srt converted to flat text), or "<no transcript>"
#   manifest.json      — {url, duration_seconds, fps, resolution, frames, has_transcript}
#
# Exits 0 on success, non-zero on download failure (caller should treat as skip).

set -u

URL="${1:-}"
OUT_DIR="${2:-}"

if [ -z "$URL" ] || [ -z "$OUT_DIR" ]; then
  echo "usage: $0 <youtube_url> <out_dir>" >&2
  exit 2
fi

mkdir -p "$OUT_DIR"
VIDEO="$OUT_DIR/video.mp4"
TRANSCRIPT_VTT="$OUT_DIR/transcript.en.vtt"
TRANSCRIPT_TXT="$OUT_DIR/transcript.txt"

# 1. Download at 480p, remux to mp4. Use bestvideo+bestaudio (standard yt-dlp recipe) and
#    let it merge — this avoids the broken DASH-fragmented single-file streams that look
#    like 600 bytes/sec and refuse to decode.
yt-dlp \
  -f 'bv*[height<=480]+ba/b[height<=480]/bv*[height<=720]+ba/best' \
  --merge-output-format mp4 \
  --remux-video mp4 \
  -o "$VIDEO" \
  --no-playlist \
  --quiet --no-warnings \
  "$URL" 2>"$OUT_DIR/yt-dlp.log" || { echo "yt-dlp failed for $URL" >&2; cat "$OUT_DIR/yt-dlp.log" >&2; exit 1; }

if [ ! -f "$VIDEO" ]; then
  echo "video.mp4 missing after yt-dlp" >&2
  exit 1
fi

# 2. Probe duration / fps / resolution
DURATION=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$VIDEO" 2>/dev/null | awk '{printf "%.0f", $1}')
FPS=$(ffprobe -v error -select_streams v:0 -show_entries stream=avg_frame_rate -of default=noprint_wrappers=1:nokey=1 "$VIDEO" 2>/dev/null | awk -F/ '$2>0{printf "%.0f", $1/$2}')
RES=$(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0 "$VIDEO" 2>/dev/null)

DURATION="${DURATION:-0}"
FPS="${FPS:-0}"
RES="${RES:-unknown}"

# 3. Extract 6 keyframes — anchored at story-craft turning points.
#    end-3s frame depends on duration; clamp safely.
declare -a TIMES=("0" "2" "5" "12" "30")
END_TS=$(( DURATION > 5 ? DURATION - 3 : 0 ))
TIMES+=("$END_TS")

declare -a NAMES=("0s" "2s" "5s" "12s" "30s" "endish")

for i in "${!TIMES[@]}"; do
  T="${TIMES[$i]}"
  N="${NAMES[$i]}"
  # Skip frames past video end
  if [ "$T" -ge "$DURATION" ] && [ "$DURATION" -gt 0 ]; then
    continue
  fi
  ffmpeg -y -loglevel error -ss "$T" -i "$VIDEO" -frames:v 1 -q:v 4 \
    -vf "scale='min(720,iw)':-2" \
    "$OUT_DIR/frame_${N}.jpg" 2>>"$OUT_DIR/ffmpeg.log" || true
done

# 4. Fetch transcript (auto-captions if available)
yt-dlp --write-auto-subs --sub-langs 'en.*,ar.*' --skip-download --sub-format vtt \
  -o "$OUT_DIR/transcript" \
  --quiet --no-warnings \
  "$URL" 2>>"$OUT_DIR/yt-dlp.log" || true

# Collapse first available .vtt to plain text. Prefer English then Arabic.
VTT=$(ls "$OUT_DIR"/transcript*.en*.vtt 2>/dev/null | head -1)
if [ -z "$VTT" ]; then
  VTT=$(ls "$OUT_DIR"/transcript*.ar*.vtt 2>/dev/null | head -1)
fi
if [ -z "$VTT" ]; then
  VTT=$(ls "$OUT_DIR"/transcript*.vtt 2>/dev/null | head -1)
fi

if [ -n "$VTT" ] && [ -f "$VTT" ]; then
  # Strip WEBVTT headers, timestamps, and styling — keep speech only
  awk '/^WEBVTT/{next} /^[0-9]+$/{next} /-->/{next} /^[[:space:]]*$/{next} {gsub(/<[^>]*>/, ""); print}' "$VTT" \
    | python3 -c "import sys; lines=[l.strip() for l in sys.stdin if l.strip()]; seen=set(); out=[]; [out.append(l) or seen.add(l) for l in lines if l not in seen]; print(' '.join(out))" \
    > "$TRANSCRIPT_TXT"
  HAS_T=true
else
  echo "<no transcript>" > "$TRANSCRIPT_TXT"
  HAS_T=false
fi

# 5. Frame inventory
FRAME_COUNT=$(ls "$OUT_DIR"/frame_*.jpg 2>/dev/null | wc -l | tr -d ' ')
FRAMES_LIST=$(ls "$OUT_DIR"/frame_*.jpg 2>/dev/null | xargs -n1 basename | tr '\n' ',' | sed 's/,$//')

# 6. Manifest
python3 - "$URL" "$DURATION" "$FPS" "$RES" "$HAS_T" "$FRAME_COUNT" "$FRAMES_LIST" "$OUT_DIR" << 'PY'
import sys, json
url, dur, fps, res, has_t, fc, frames, out = sys.argv[1:9]
manifest = {
    "url": url,
    "duration_seconds": int(dur or 0),
    "fps": int(fps or 0),
    "resolution": res,
    "has_transcript": has_t == "true",
    "frame_count": int(fc or 0),
    "frames": frames.split(",") if frames else [],
}
with open(f"{out}/manifest.json", "w") as f:
    json.dump(manifest, f, indent=2)
print(f"OK {url}  dur={dur}s frames={fc} transcript={has_t}")
PY
