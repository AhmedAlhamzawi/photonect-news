#!/usr/bin/env bash
# queue-status.sh — list every post folder + status of required files.
# Run from NEWS CODE root.

set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
POSTS="$ROOT/data/posts"

cd "$POSTS" || { echo "no posts dir" >&2; exit 1; }

printf "%-40s %-8s %-8s %-10s %s\n" "SLUG" "PROPS" "CAPTION" "VIDEO" "LATEST"
printf "%-40s %-8s %-8s %-10s %s\n" "----" "-----" "-------" "-----" "------"

for d in */; do
  slug="${d%/}"
  props="✗"; [ -f "$slug/props.json" ] && props="✓"
  caption="✗"; [ -f "$slug/caption.txt" ] && caption="✓"
  latest=""
  size=""
  if   [ -f "$slug/newsreel_v3.mp4" ]; then latest="v3"; size=$(ls -lh "$slug/newsreel_v3.mp4" | awk '{print $5}')
  elif [ -f "$slug/newsreel_v2.mp4" ]; then latest="v2"; size=$(ls -lh "$slug/newsreel_v2.mp4" | awk '{print $5}')
  elif [ -f "$slug/newsreel.mp4"    ]; then latest="v1"; size=$(ls -lh "$slug/newsreel.mp4" | awk '{print $5}')
  fi
  video="$latest"
  [ -z "$latest" ] && video="✗"
  printf "%-40s %-8s %-8s %-10s %s\n" "$slug" "$props" "$caption" "$video" "$size"
done
