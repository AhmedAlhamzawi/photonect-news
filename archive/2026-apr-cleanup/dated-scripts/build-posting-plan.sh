#!/usr/bin/env bash
# build-posting-plan.sh — generate POSTING_PLAN_<date>.md from all reels for a date.
#
# Usage:
#   ./build-posting-plan.sh [--date YYYY-MM-DD] [--start HH:MM] [--interval 2h]
#
# Defaults:
#   --date      today (GMT+3)
#   --start     12:00
#   --interval  2h
#
# Walks data/posts/<date>-*/, reads props.json, finds latest video, orders slots
# so that no two consecutive posts share a topicBucket. If the bucket mix makes
# that mathematically impossible, offending slots are flagged ⚠️ CONFLICT.
#
# Output: data/posts/POSTING_PLAN_<date>.md

set -euo pipefail

# ---- arg parsing ----
DATE=""
START="12:00"
INTERVAL_H=2

while [ $# -gt 0 ]; do
  case "$1" in
    --date)      DATE="$2"; shift 2 ;;
    --start)     START="$2"; shift 2 ;;
    --interval)  INTERVAL_H="${2%h}"; shift 2 ;;
    -h|--help)
      head -15 "$0" | tail -12
      exit 0 ;;
    *) echo "unknown arg: $1" >&2; exit 2 ;;
  esac
done

if [ -z "$DATE" ]; then
  DATE=$(TZ="Asia/Baghdad" date +%Y-%m-%d)
fi

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
POSTS="$ROOT/data/posts"
OUT="$POSTS/POSTING_PLAN_$DATE.md"

# ---- discover reels for the date ----
shopt -s nullglob
SLUG_DIRS=("$POSTS/$DATE"-*/)
shopt -u nullglob

if [ ${#SLUG_DIRS[@]} -eq 0 ]; then
  echo "error: no reels found for date $DATE under $POSTS/" >&2
  exit 1
fi

# ---- parallel arrays: SLUGS[], BUCKETS[], AR_HEAD[], EN_SUB[], AR_LABEL[], STAT_VAL[], VIDEO[], SIZE[], CAPTION[] ----
SLUGS=()
BUCKETS=()
AR_HEAD=()
EN_SUB=()
AR_LABEL=()
STAT_VAL=()
VIDEO=()
SIZE=()
CAPTION=()

for dir in "${SLUG_DIRS[@]}"; do
  dir="${dir%/}"
  slug=$(basename "$dir")
  props="$dir/props.json"
  cap="$dir/caption.txt"

  [ ! -f "$props" ] && { echo "error: $slug missing props.json" >&2; exit 1; }
  [ ! -f "$cap" ]   && { echo "error: $slug missing caption.txt" >&2; exit 1; }

  bucket=$(jq -r '.topicBucket // empty' "$props")
  if [ -z "$bucket" ]; then
    echo "error: $slug has no topicBucket in props.json — add one of:" >&2
    echo "  mena_geopolitics iraq_domestic gulf_regional europe global_economy tech_ai wildcard" >&2
    exit 1
  fi

  ar_head=$(jq -r '.breaking.arabicHeadline // empty' "$props")
  en_sub=$(jq -r '.breaking.englishSubhead // empty' "$props")
  ar_label=$(jq -r '.beats[0].bigStat.arabicLabel // empty' "$props")
  stat_val=$(jq -r '.beats[0].bigStat.value // empty' "$props")

  if   [ -f "$dir/newsreel_v3.mp4" ]; then vid="$dir/newsreel_v3.mp4"
  elif [ -f "$dir/newsreel_v2.mp4" ]; then vid="$dir/newsreel_v2.mp4"
  elif [ -f "$dir/newsreel.mp4"    ]; then vid="$dir/newsreel.mp4"
  else
    echo "error: $slug has no rendered video yet" >&2
    exit 1
  fi
  sz=$(ls -lh "$vid" | awk '{print $5}')
  rel_vid="${vid#$ROOT/}"

  SLUGS+=("$slug")
  BUCKETS+=("$bucket")
  AR_HEAD+=("$ar_head")
  EN_SUB+=("$en_sub")
  AR_LABEL+=("$ar_label")
  STAT_VAL+=("$stat_val")
  VIDEO+=("$rel_vid")
  SIZE+=("$sz")
  CAPTION+=("$cap")
done

N=${#SLUGS[@]}

# ---- rotation: produce ORDER[] of indices + CONFLICT[] flags ----
TSV=$(mktemp)
for i in "${!SLUGS[@]}"; do
  printf "%s\t%s\t%d\n" "${SLUGS[$i]}" "${BUCKETS[$i]}" "$i" >> "$TSV"
done

ROTATION=$(awk -F'\t' -v OFS='\t' '
  { slug[NR]=$1; bucket[NR]=$2; idx[NR]=$3; count[$2]++; total++ }
  END {
    last = ""
    for (step=1; step<=total; step++) {
      best=""; best_n=0
      for (b in count) {
        if (count[b] <= 0) continue
        if (b == last) continue
        if (count[b] > best_n) { best=b; best_n=count[b] }
      }
      conflict = "OK"
      if (best == "") {
        for (b in count) { if (count[b] > 0) { best=b; break } }
        conflict = "CONFLICT"
      }
      for (i=1; i<=total; i++) {
        if (bucket[i] == best && !used[i]) {
          print idx[i], slug[i], bucket[i], conflict
          used[i]=1; count[best]--
          break
        }
      }
      last = best
    }
  }
' "$TSV")
rm -f "$TSV"

# ---- compute slot times ----
start_h=${START%:*}
start_m=${START#*:}
start_min=$((10#$start_h * 60 + 10#$start_m))
step_min=$((INTERVAL_H * 60))

slot_times=()
for n in $(seq 0 $((N-1))); do
  total=$((start_min + n * step_min))
  h=$((total / 60))
  m=$((total % 60))
  slot_times+=("$(printf '%02d:%02d' "$h" "$m")")
done

# ---- emit markdown ----
# weekday label
WEEKDAY=$(date -j -f "%Y-%m-%d" "$DATE" "+%a" 2>/dev/null || echo "")
end_time="${slot_times[$((N-1))]}"
bucket_seq=""
conflict_total=0

{
  echo "# Posting Plan — $DATE${WEEKDAY:+ ($WEEKDAY)}"
  echo ""
  echo "**Channel:** @photonect.news · IG + TikTok · Arabic-first"
  echo "**Total slots:** $N · **Window:** $START → $end_time GMT+3 · **Interval:** ${INTERVAL_H}h"
  echo ""
  echo "| # | Time | Slug | Bucket | Size |"
  echo "|---|------|------|--------|------|"

  # Re-read rotation to emit index table
  slot=0
  while IFS=$'\t' read -r orig_idx slug bucket conflict; do
    slot=$((slot+1))
    flag=""
    [ "$conflict" = "CONFLICT" ] && { flag=" ⚠️"; conflict_total=$((conflict_total+1)); }
    echo "| $slot | ${slot_times[$((slot-1))]} | $slug | $bucket$flag | ${SIZE[$orig_idx]} |"
    if [ -z "$bucket_seq" ]; then
      bucket_seq="$bucket"
    else
      bucket_seq="$bucket_seq → $bucket"
    fi
  done <<< "$ROTATION"

  echo ""
  echo "**Rotation:** $bucket_seq"
  if [ "$conflict_total" -gt 0 ]; then
    echo ""
    echo "> ⚠️ **$conflict_total adjacent-bucket conflict(s).** The bucket mix for this date makes full diversity mathematically impossible (one bucket exceeds ceil(N/2) of the total). Consider replacing one mena slot with a different bucket for a cleaner feed."
  fi
  echo ""
  echo "---"
  echo ""

  # per-slot detail
  slot=0
  while IFS=$'\t' read -r orig_idx slug bucket conflict; do
    slot=$((slot+1))
    t="${slot_times[$((slot-1))]}"
    flag=""
    [ "$conflict" = "CONFLICT" ] && flag=" ⚠️ same bucket as previous slot"
    echo "## Slot $slot — $t GMT+3"
    echo ""
    echo "**Bucket:** \`$bucket\`$flag"
    echo "**Arabic hook:** ${AR_HEAD[$orig_idx]}"
    echo "**One-line angle (EN):** ${EN_SUB[$orig_idx]}"
    if [ -n "${STAT_VAL[$orig_idx]}" ]; then
      echo "**Big stat:** \`${STAT_VAL[$orig_idx]}\` — ${AR_LABEL[$orig_idx]}"
    fi
    echo ""
    echo "### 📹 Upload this video"
    echo "\`${VIDEO[$orig_idx]}\` (${SIZE[$orig_idx]}, 30s)"
    echo ""
    echo "### 📋 Paste this caption"
    echo "<details><summary>Tap to expand (copy everything inside the fence)</summary>"
    echo ""
    echo '````'
    cat "${CAPTION[$orig_idx]}"
    echo '````'
    echo ""
    echo "</details>"
    echo ""
    echo "### ✅ Posted?"
    echo "- [ ] Instagram"
    echo "- [ ] TikTok"
    echo ""
    echo "---"
    echo ""
  done <<< "$ROTATION"

  echo "## Re-generate"
  echo ""
  echo 'Run `bash data/_template/build-posting-plan.sh --date '"$DATE"'` any time to rebuild this file from current props.json + caption.txt.'
} > "$OUT"

# ---- stdout summary ----
echo "✓ $OUT"
echo "  $N slots · $START→$end_time GMT+3 · $bucket_seq"
[ "$conflict_total" -gt 0 ] && echo "  ⚠️  $conflict_total adjacent-bucket conflict(s)"
