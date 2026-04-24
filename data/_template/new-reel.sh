#!/usr/bin/env bash
# new-reel.sh — scaffold a new NewsReel post folder.
#
# Usage:
#   ./new-reel.sh <slug> <topic_bucket>
#   e.g. ./new-reel.sh 2026-04-18-iraq-pm-crisis iraq_domestic
#
# Valid buckets: mena_geopolitics iraq_domestic gulf_regional europe
#                global_economy tech_ai wildcard
#
# Produces:
#   data/posts/<slug>/props.json     (template with {{PLACEHOLDERS}})
#   data/posts/<slug>/caption.txt    (template)
#   public/images/news/<slug>/       (empty — drop b-roll + hero here)

set -euo pipefail

SLUG="${1:-}"
BUCKET="${2:-}"
VALID_BUCKETS="mena_geopolitics iraq_domestic gulf_regional europe global_economy tech_ai wildcard"

if [ -z "$SLUG" ] || [ -z "$BUCKET" ]; then
  echo "usage: $0 <slug> <topic_bucket>" >&2
  echo "  e.g. $0 2026-04-18-iraq-pm-crisis iraq_domestic" >&2
  echo "  buckets: $VALID_BUCKETS" >&2
  exit 2
fi

if ! echo " $VALID_BUCKETS " | grep -q " $BUCKET "; then
  echo "error: invalid bucket '$BUCKET'" >&2
  echo "  buckets: $VALID_BUCKETS" >&2
  exit 2
fi

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
TPL="$ROOT/data/_template"
DST="$ROOT/data/posts/$SLUG"
IMG_DST="$HOME/Desktop/Claude <> Ahmed - 2nd Brain/Photonect/my-video/public/images/news/$SLUG"

if [ -d "$DST" ]; then
  echo "error: $DST already exists" >&2
  exit 1
fi

mkdir -p "$DST"
mkdir -p "$IMG_DST"

# Derive dateLabel from slug prefix YYYY-MM-DD
YEAR=$(echo "$SLUG" | cut -d- -f1)
MONTH=$(echo "$SLUG" | cut -d- -f2)
DAY=$(echo "$SLUG" | cut -d- -f3)
MONTH_EN=$(date -j -f "%Y-%m-%d" "$YEAR-$MONTH-$DAY" "+%b %d • %Y" 2>/dev/null | tr '[:lower:]' '[:upper:]' || echo "APR 18 • 2026")

sed \
  -e "s|{{SLUG}}|$SLUG|g" \
  -e "s|{{DATE_LABEL}}|$MONTH_EN|g" \
  -e "s|{{ARABIC_DATE_LABEL}}|$DAY $MONTH $YEAR|g" \
  -e "s|{{TOPIC_BUCKET}}|$BUCKET|g" \
  "$TPL/props.template.json" > "$DST/props.json"

cp "$TPL/caption.template.txt" "$DST/caption.txt"

echo "scaffolded:"
echo "  props:   $DST/props.json"
echo "  caption: $DST/caption.txt"
echo "  images:  $IMG_DST  (drop hero.mp4 + broll_1/2/3 here)"
echo ""
echo "next: fill props.json placeholders, drop media, then:"
echo "  cd '$HOME/Desktop/Claude <> Ahmed - 2nd Brain/Photonect/my-video'"
echo "  npx remotion render NewsReel '$DST/newsreel.mp4' --props='$DST/props.json'"
