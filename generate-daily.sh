#!/usr/bin/env bash
#
# generate-daily.sh
# ─────────────────
# ON-DEMAND daily slate generator for Photonect NEWS.
#
# This is NOT a scheduled task — you run it manually when you want a slate.
# Pass a date (YYYY-MM-DD). The script:
#   1. Ensures every slug for that date has props.json + media
#   2. Runs the V5 render pipeline for each slug
#   3. Emits triple QA (margin / luminance / audio-presence)
#   4. (removed — captions live next to each video as caption.txt)
#
# Usage:
#   bash generate-daily.sh                     # uses today's date
#   bash generate-daily.sh 2026-04-22          # explicit date
#   bash generate-daily.sh 2026-04-22 --dry    # show what would run
#
# Exit codes: 0 = all good, 1 = render failure, 2 = QA failure, 3 = setup error

set -u

HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$HERE"
TEMPLATE="$ROOT/data/_template"
POSTS="$ROOT/data/posts"

DATE="${1:-$(date +%Y-%m-%d)}"
DRY="${2:-}"

if ! [[ "$DATE" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]]; then
  echo "error: date must be YYYY-MM-DD, got: $DATE" >&2
  exit 3
fi

# Discover all slugs for this date.
# Optional SLUG_FILTER env (default empty) → only include slugs whose name contains it.
# Lets a one-off subset run (e.g. a special-coverage drop) reuse this pipeline without
# changing normal daily behaviour: empty filter = all slugs, exactly as before.
SLUGS=()
for d in "$POSTS/$DATE"-*; do
  [ -d "$d" ] || continue
  slug="$(basename "$d")"
  if [ -n "${SLUG_FILTER:-}" ] && [[ "$slug" != *"$SLUG_FILTER"* ]]; then continue; fi
  SLUGS+=("$slug")
done

if [ ${#SLUGS[@]} -eq 0 ]; then
  echo "error: no slugs found for date $DATE under $POSTS/" >&2
  echo "       expected directories named $POSTS/$DATE-<slug>" >&2
  exit 3
fi

printf "\033[1;36m━━━ Photonect generate-daily — %s ━━━\033[0m\n" "$DATE"
echo "discovered ${#SLUGS[@]} slugs:"
for s in "${SLUGS[@]}"; do echo "  · $s"; done
echo ""

if [ "$DRY" = "--dry" ]; then
  echo "(dry run — exiting before render)"
  exit 0
fi

# ── Phase 1: Validate props for every slug ─────────────────────────────────
echo "━━━ PHASE 1 — validating props ━━━"
missing=0
for slug in "${SLUGS[@]}"; do
  pj="$POSTS/$slug/.meta/props.json"
  if [ ! -f "$pj" ]; then
    echo "  MISSING $slug/.meta/props.json"
    missing=$((missing+1))
    continue
  fi
  if grep -q '{{[A-Z0-9_]\+}}' "$pj"; then
    echo "  TEMPLATE $slug (placeholders still present)"
    missing=$((missing+1))
    continue
  fi
  # Check for required fields
  python3 - "$pj" "$slug" << 'PY' || missing=$((missing+1))
import json, sys
pj, slug = sys.argv[1], sys.argv[2]
try:
  p = json.load(open(pj))
  errs = []
  if not p.get("arabicDateLabel"): errs.append("arabicDateLabel")
  if not p.get("breaking", {}).get("arabicHeadline"): errs.append("breaking.arabicHeadline")
  beats = p.get("beats", [])
  if len(beats) != 3: errs.append(f"beats count={len(beats)} (expected 3)")
  for i, b in enumerate(beats):
    if not b.get("arabicHeading"): errs.append(f"beats[{i}].arabicHeading")
    if not b.get("broll"): errs.append(f"beats[{i}].broll")
  # tech_ai posts must have at least one supportingStat with a numeric value —
  # numbers anchor credibility for tech audience
  if p.get("topicBucket") == "tech_ai":
    stats = [s for b in beats for s in b.get("supportingStats", [])]
    has_numeric = any(
      any(c.isdigit() for c in str(s.get("value", ""))) for s in stats
    )
    if not has_numeric:
      errs.append("tech_ai: no beat.supportingStats with numeric value")
  if errs:
    print(f"  INVALID {slug}: {', '.join(errs)}")
    sys.exit(1)
except Exception as e:
  print(f"  PARSE-ERR {slug}: {e}")
  sys.exit(1)
PY
done

if [ $missing -gt 0 ]; then
  echo "❌ $missing slug(s) are not ready to render — fix and retry"
  exit 3
fi
echo "✅ all ${#SLUGS[@]} props validated"
echo ""

# ── Phase 2: Render all slugs ──────────────────────────────────────────────
echo "━━━ PHASE 2 — rendering ${#SLUGS[@]} reels ━━━"
ok=0 fail=0 failed=()
qa_ok=0 qa_fail=0 qa_failed=()
render_log="/tmp/photonect-$DATE/render.log"
mkdir -p "/tmp/photonect-$DATE/qa"
: > "$render_log"

start_batch=$(date +%s)
for slug in "${SLUGS[@]}"; do
  printf "  %-42s " "$slug"
  start=$(date +%s)
  if bash "$TEMPLATE/render-reel.sh" "$slug" v3 >>"$render_log" 2>&1; then
    dur=$(( $(date +%s) - start ))
    mp4="$POSTS/$slug/video.mp4"
    if [ -f "$mp4" ]; then
      bytes=$(stat -f%z "$mp4" 2>/dev/null || stat -c%s "$mp4")
      mb=$(( bytes / 1024 / 1024 ))
      printf "\033[1;32m✓\033[0m %3ds %3dMB\n" "$dur" "$mb"
      ok=$((ok+1))
    else
      printf "\033[1;31m✗ no mp4\033[0m\n"
      fail=$((fail+1)); failed+=("$slug")
    fi
  else
    dur=$(( $(date +%s) - start ))
    printf "\033[1;31m✗ render failed (%ds)\033[0m\n" "$dur"
    fail=$((fail+1)); failed+=("$slug")
  fi
done
total_dur=$(( $(date +%s) - start_batch ))
echo ""
echo "render: ok=$ok fail=$fail total ${total_dur}s"

if [ $fail -gt 0 ]; then
  echo "❌ Render failures: ${failed[*]}"
  echo "   Check $render_log"
  exit 1
fi
echo ""

# ── Phase 3: Triple QA (margin / luminance / audio) ────────────────────────
echo "━━━ PHASE 3 — triple QA ━━━"
for slug in "${SLUGS[@]}"; do
  printf "  %-42s " "$slug"
  mp4="$POSTS/$slug/video.mp4"
  qa_dir="/tmp/photonect-$DATE/qa/$slug"
  mkdir -p "$qa_dir"

  # Extract frames at 2/9/18/27s (hero, beat1, beat2, beat3)
  for pair in "2:hero" "9:beat1" "18:beat2" "27:beat3"; do
    t="${pair%:*}" name="${pair#*:}"
    ffmpeg -y -loglevel error -ss "$t" -i "$mp4" -frames:v 1 "$qa_dir/$name.jpg" 2>/dev/null
  done

  # Extract 5s of audio starting at 2s (mono RMS check)
  # NOTE: do NOT use -loglevel error — volumedetect reports to info level and gets suppressed.
  # Default log level is "info" which includes [Parsed_volumedetect_0 @ …] mean_volume lines.
  audio_rms=$(ffmpeg -y -ss 2 -t 5 -i "$mp4" -ac 1 -af "volumedetect" -f null - 2>&1 | grep "mean_volume" | awk -F': ' '{print $2}' | awk '{print $1}' | head -1)

  # Read variant: Variant B has intentional dark lower half for typography; QA must know this.
  slug_variant=$(python3 -c "import json; p=json.load(open('$POSTS/$slug/.meta/props.json')); print(p.get('variant','A'))" 2>/dev/null || echo "A")

  # Combined QA: PIL luminance + margin-safe-zone sanity + audio presence
  python3 - "$slug" "$qa_dir" "$audio_rms" "$slug_variant" << 'PY'
import sys, json, os
from PIL import Image
slug, qa_dir, audio_rms = sys.argv[1], sys.argv[2], sys.argv[3]
variant = sys.argv[4] if len(sys.argv) > 4 else "A"
try:
  rms = float(audio_rms) if audio_rms else -999.0
except:
  rms = -999.0

floors = {"hero": 50.0, "beat1": 40.0, "beat2": 40.0, "beat3": 40.0}
res, fails = {}, []

for name, floor in floors.items():
  p = f"{qa_dir}/{name}.jpg"
  if not os.path.exists(p):
    fails.append(f"{name}-missing")
    continue
  im = Image.open(p).convert("L")
  # Variant B (KINETIC-SPLIT): bottom ~50% is intentional dark typography zone.
  # Crop to upper image half before luminance check to avoid false QA failures.
  if variant == "B" and name != "hero":
    w_b, h_b = im.size
    im = im.crop((0, 0, w_b, h_b // 2))
  # 1. Full-frame luminance
  thumb = im.copy()
  thumb.thumbnail((256, 256))
  hist = thumb.histogram()
  total = sum(hist)
  L_full = sum(i * h for i, h in enumerate(hist)) / max(total, 1)

  # 2. Bottom-safe-zone check: sample bottom 400px (occluded by IG caption)
  # We want REAL content above this line; if mean luminance in bottom 400px
  # is identical to full-frame mean, content is probably in the occluded zone.
  w, h = im.size
  crop_safe = im.crop((0, 0, w, max(1, h - int(h * 0.21))))  # keep top 79% (400/1920)
  ts = crop_safe.copy()
  ts.thumbnail((256, 256))
  hist = ts.histogram()
  total = sum(hist)
  L_safe = sum(i * h for i, h in enumerate(hist)) / max(total, 1)

  res[name] = {"L_full": round(L_full, 1), "L_safe": round(L_safe, 1), "floor": floor}
  if L_safe < floor:
    fails.append(f"{name}(L={L_safe:.0f}<{floor})")

# 3. Audio presence: mean_volume below -50dB means silence
res["audio"] = {"rms_db": rms}
if rms > -50:
  res["audio"]["pass"] = True
else:
  fails.append(f"audio(rms={rms}dB)")
  res["audio"]["pass"] = False

with open(f"{qa_dir}/report.json", "w") as f:
  json.dump(res, f, indent=2)

if fails:
  print(f"\033[1;33m⚠\033[0m {','.join(fails[:3])}")
  sys.exit(1)
print(f"\033[1;32m✓\033[0m hero={res['hero']['L_safe']} b1={res['beat1']['L_safe']} b2={res['beat2']['L_safe']} b3={res['beat3']['L_safe']} aud={res['audio']['rms_db']}dB")
PY
  rc=$?
  if [ $rc -eq 0 ]; then
    qa_ok=$((qa_ok+1))
  else
    qa_fail=$((qa_fail+1)); qa_failed+=("$slug")
  fi
done

echo ""
echo "qa: ok=$qa_ok warn=$qa_fail"

# ── Phase 4: Summary (no per-day delivery doc — captions live in each post) ──
echo ""
echo "━━━ SUMMARY ━━━"
echo "Date:    $DATE"
echo "Videos:  $ok/$((ok+fail)) rendered"
echo "QA:      $qa_ok/${#SLUGS[@]} clean"
echo "Output:  data/posts/${DATE}-*/  (video.mp4 + caption.txt per folder)"
if [ ${#qa_failed[@]} -gt 0 ]; then
  echo ""
  echo "⚠ QA warnings (manually verify):"
  for s in "${qa_failed[@]}"; do
    echo "  - $s  (see /tmp/photonect-$DATE/qa/$s/report.json)"
  done
fi

# Final status
if [ $fail -gt 0 ]; then
  exit 1
elif [ $qa_fail -gt 0 ]; then
  echo "(QA warnings are non-fatal — visually inspect the flagged reels)"
  exit 0
else
  printf "\033[1;32m✅ All %d reels rendered + passed triple QA\033[0m\n" "${#SLUGS[@]}"
  exit 0
fi
