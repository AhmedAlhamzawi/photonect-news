#!/usr/bin/env bash
# render-reel.sh — render a NewsReel for a given slug.
#
# Usage:
#   ./render-reel.sh <slug> [v1|v2|v3]
#   defaults to v2 (preferred name used by automation/*)
#
# Examples:
#   ./render-reel.sh 2026-04-17-iraq-blackout            # → newsreel_v2.mp4
#   ./render-reel.sh 2026-04-17-hormuz-week2 v3          # → video.mp4 (v3 kept as tag only)

set -euo pipefail

SLUG="${1:-}"
VARIANT="${2:-v2}"

if [ -z "$SLUG" ]; then
  echo "usage: $0 <slug> [v1|v2|v3]" >&2
  exit 2
fi

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
MYVIDEO="${MYVIDEO:-$HOME/Desktop/Claude <> Ahmed - 2nd Brain/Photonect/my-video}"
PROPS="$ROOT/data/posts/$SLUG/props.json"

case "$VARIANT" in
  v1) OUT="$ROOT/data/posts/$SLUG/newsreel.mp4" ;;
  v2) OUT="$ROOT/data/posts/$SLUG/newsreel_v2.mp4" ;;
  v3) OUT="$ROOT/data/posts/$SLUG/video.mp4" ;;
  *) echo "invalid variant: $VARIANT (use v1|v2|v3)" >&2; exit 2 ;;
esac

if [ ! -f "$PROPS" ]; then
  echo "error: $PROPS not found" >&2
  exit 1
fi

# Pre-flight: refuse to render template placeholders (e.g. {{ARABIC_HEADLINE}}).
# Silently rendering "{{ARABIC_HEADLINE}}" into a posted reel is a ship-blocker
# class of bug — the April 18 gulf-pivot reel went out with literal
# {{...}} text before this guard existed. Catch it at the door.
if grep -q '{{[A-Z0-9_]\+}}' "$PROPS"; then
  echo "error: $PROPS still contains template placeholders (e.g. {{ARABIC_HEADLINE}}) — refusing to render" >&2
  echo "offending lines:" >&2
  grep -n '{{[A-Z0-9_]\+}}' "$PROPS" | head -5 >&2
  exit 3
fi

# Pre-flight: refuse subtly-broken English subheads with trailing punctuation
# that flips under bidi. "$150?" renders as "?$150" when the parent element
# is RTL. Simpler fix: catch in props.json.
if grep -E '"englishSubhead"[^"]*"[^"]*[?!]"' "$PROPS" >/dev/null; then
  echo "warning: englishSubhead ends in punctuation — may flip under RTL bidi" >&2
fi

# Pre-flight: warn if this is a tech_ai post missing numeric supportingStats.
# Non-blocking — renders proceed — but missing stats hurt credibility of AI reels.
# Check is done inline (no --slug flag in lint-techstat.py) to avoid re-scanning
# all posts on every render. (2026-04-21: 4 tech_ai posts shipped without stats)
python3 - "$PROPS" "$SLUG" 2>/dev/null << 'LINT_EOF' || true
import json, re, sys
props = json.loads(open(sys.argv[1]).read())
slug = sys.argv[2]
if props.get("topicBucket") != "tech_ai":
    sys.exit(0)
has_num = any(
    re.search(r"\d", str((b.get("supportingStat") or {}).get("value", b.get("supportingStat", "")) or ""))
    for b in (props.get("beats") or []) if isinstance(b, dict)
)
if not has_num:
    print(f"warning: {slug} is tech_ai but has no numeric supportingStat — stats anchor credibility", file=__import__("sys").stderr)
LINT_EOF

# Auto-hunt media if not yet done for this slug. This keeps every render
# grounded in story-specific imagery and prevents reuse of stale stock.
STAMP="$ROOT/data/posts/$SLUG/media-stamp.json"
if [ ! -f "$STAMP" ]; then
  echo "no media stamp for $SLUG — running hunter first"
  "$ROOT/data/_template/hunt-media.sh" "$SLUG"
fi

echo "rendering $SLUG $VARIANT → $OUT"

# Strip macOS/iCloud conflict-duplicate files (e.g. "hero 2.jpg") that
# occasionally race back into the media dir after the hunt step — they
# break Remotion's bundle-time copy with an ETIMEDOUT on the duplicate.
MEDIA_DIR="$MYVIDEO/public/images/news/$SLUG"
if [ -d "$MEDIA_DIR" ]; then
  find "$MEDIA_DIR" -name '* 2.*' -type f -delete 2>/dev/null || true
fi

cd "$MYVIDEO"
# Run render; capture exit code so we can run post-render steps before propagating it.
# (exec was removed to allow thumbnail extraction after a successful render — 2026-04-21)
npx remotion render NewsReel "$OUT" --props="$PROPS"
RENDER_RC=$?
if [ $RENDER_RC -eq 0 ] && [ -f "$OUT" ]; then
  bash "$ROOT/data/_template/extract-thumbnail.sh" "$SLUG" 2>/dev/null || true
fi
exit $RENDER_RC
