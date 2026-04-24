#!/usr/bin/env bash
# render-all.sh — render every post's newsreel_v3.mp4 sequentially.
#
# Usage: ./render-all.sh [variant]
#   variant defaults to v3.
#
# Emits a final report with per-slug success/duration; exits non-zero if
# any render failed.

set -u

HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$HERE/../.." && pwd)"
VARIANT="${1:-v3}"

cd "$ROOT"

SLUGS=$(ls data/posts | grep -E '^[0-9]{4}-[0-9]{2}-[0-9]{2}-' | sort)
TOTAL=$(echo "$SLUGS" | wc -l | tr -d ' ')

echo "rendering $TOTAL reels → variant $VARIANT"
echo "started: $(date)"
echo

ok=0
fail=0
failed_slugs=""

for s in $SLUGS; do
  start=$(date +%s)
  echo "--- $s ---"
  if "$HERE/render-reel.sh" "$s" "$VARIANT" >/tmp/render-$$.log 2>&1; then
    dur=$(( $(date +%s) - start ))
    echo "  ✓ ${dur}s"
    ok=$((ok+1))
  else
    dur=$(( $(date +%s) - start ))
    echo "  ✗ ${dur}s — see tail below"
    tail -10 /tmp/render-$$.log
    fail=$((fail+1))
    failed_slugs="$failed_slugs $s"
  fi
done

rm -f /tmp/render-$$.log

echo
echo "done: $(date)"
echo "ok=$ok fail=$fail"
if [ $fail -gt 0 ]; then
  echo "failed:$failed_slugs"
  exit 1
fi
