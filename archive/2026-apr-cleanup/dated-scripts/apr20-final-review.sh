#!/usr/bin/env bash
# apr20-final-review.sh — after all 12 April 20 reels are green,
# extract hero + beat2 frames per slug and write a combined sheet:
#   /tmp/photonect-apr20/final-review/<slug>_hero.jpg
#   /tmp/photonect-apr20/final-review/<slug>_beat2.jpg
#   /tmp/photonect-apr20/final-review/SUMMARY.md
#
# Prints a one-row-per-slug table with size (MB), duration (s), and
# luminance @ hero + beat2. Zero green rows = "OK TO POST".
set -u

HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$HERE/../.." && pwd)"
cd "$ROOT"

SLUGS=(
  2026-04-20-iraq-cabinet
  2026-04-20-iran-day-52
  2026-04-20-chip-embargo
  2026-04-20-eu-gas-bridge
  2026-04-20-opec-emergency
  2026-04-20-imf-crisis-fund
  2026-04-20-arctic-route
  2026-04-20-iaea-verdict
  2026-04-20-kurdistan-crack
  2026-04-20-starlink-mideast
  2026-04-20-yen-cliff
  2026-04-20-qatar-pivot
)

out="/tmp/photonect-apr20/final-review"
mkdir -p "$out"
summary="$out/SUMMARY.md"

{
  echo "# April 20 Final Review — $(date)"
  echo ""
  echo "| # | Slug | MB | Dur | Hero L | Beat2 L |"
  echo "|---|------|----|-----|--------|---------|"
} > "$summary"

i=0
for slug in "${SLUGS[@]}"; do
  i=$((i+1))
  mp4="data/posts/$slug/newsreel_v3.mp4"
  [ -f "$mp4" ] || { echo "| $i | $slug | MISSING | - | - | - |" >> "$summary"; continue; }

  bytes=$(stat -f%z "$mp4" 2>/dev/null || stat -c%s "$mp4")
  mb=$(awk "BEGIN{printf \"%.1f\", $bytes/1024/1024}")
  dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$mp4" | awk '{printf "%.1f", $1}')

  ffmpeg -y -loglevel error -ss 1.2 -i "$mp4" -frames:v 1 "$out/${slug}_hero.jpg"  2>/dev/null
  ffmpeg -y -loglevel error -ss 14  -i "$mp4" -frames:v 1 "$out/${slug}_beat2.jpg" 2>/dev/null

  read hero_L beat2_L < <(python3 - "$out/${slug}_hero.jpg" "$out/${slug}_beat2.jpg" <<'PY'
import sys
from PIL import Image
def L(p):
    im = Image.open(p).convert("L"); im.thumbnail((256,256))
    h = im.histogram(); t = sum(h)
    return sum(i*c for i,c in enumerate(h))/max(t,1)
print(f"{L(sys.argv[1]):.1f} {L(sys.argv[2]):.1f}")
PY
)
  echo "| $i | $slug | $mb | $dur | $hero_L | $beat2_L |" >> "$summary"
  echo "REVIEW $slug mb=$mb dur=$dur hero=$hero_L beat2=$beat2_L"
done

echo "" >> "$summary"
echo "Thresholds: hero ≥ 62 (floor for L_rendered), beat ≥ 40." >> "$summary"
echo "" >> "$summary"
echo "FINAL REVIEW written: $summary"
