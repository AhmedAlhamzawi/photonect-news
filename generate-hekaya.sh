#!/usr/bin/env bash
#
# generate-hekaya.sh
# ──────────────────
# Renders a HEKAYA day's slate. Sister to generate-daily.sh, but for the
# slow-storytelling track. Reads from data/hekaya/, renders the Hekaya
# Remotion composition, runs HEKAYA-appropriate QA.
#
# Usage:
#   bash generate-hekaya.sh                     # uses today's date (UTC)
#   bash generate-hekaya.sh 2026-05-01          # explicit date
#   bash generate-hekaya.sh 2026-05-01 --dry    # show what would run
#
# Exit codes: 0 = all good, 1 = render failure, 2 = QA failure, 3 = setup error

set -u

HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$HERE"
HEKAYA="$ROOT/data/hekaya"
MYVIDEO="${MYVIDEO:-$ROOT/my-video}"

DATE="${1:-$(date -u +%Y-%m-%d)}"
DRY="${2:-}"

if ! [[ "$DATE" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]]; then
  echo "error: date must be YYYY-MM-DD, got: $DATE" >&2
  exit 3
fi

# Discover all hekaya slugs for this date.
SLUGS=()
for d in "$HEKAYA/$DATE"-*; do
  [ -d "$d" ] || continue
  SLUGS+=("$(basename "$d")")
done

if [ ${#SLUGS[@]} -eq 0 ]; then
  echo "error: no hekaya folders found for $DATE under $HEKAYA/" >&2
  exit 3
fi

printf "\033[1;33m━━━ Photonect HEKAYA — %s ━━━\033[0m\n" "$DATE"
echo "discovered ${#SLUGS[@]} hekaya posts:"
for s in "${SLUGS[@]}"; do echo "  · $s"; done
echo ""

if [ "$DRY" = "--dry" ]; then
  echo "(dry run — exiting before render)"
  exit 0
fi

# ── Phase 1: Validate every props.json ──────────────────────────────────
echo "━━━ PHASE 1 — validating props ━━━"
missing=0
for slug in "${SLUGS[@]}"; do
  pj="$HEKAYA/$slug/.meta/props.json"
  if [ ! -f "$pj" ]; then
    echo "  MISSING $slug/.meta/props.json"
    missing=$((missing+1))
    continue
  fi
  python3 - "$pj" "$slug" << 'PY' || missing=$((missing+1))
import json, sys
pj, slug = sys.argv[1], sys.argv[2]
try:
  p = json.load(open(pj))
  errs = []
  pro = p.get("prologue") or {}
  if not pro.get("arabicTitle"): errs.append("prologue.arabicTitle")
  if not pro.get("arabicHook"): errs.append("prologue.arabicHook")
  if not pro.get("heroMedia"): errs.append("prologue.heroMedia")
  chapters = p.get("chapters") or []
  if len(chapters) != 3: errs.append(f"chapters count={len(chapters)} (expected 3)")
  for i, c in enumerate(chapters):
    if not c.get("arabicTitle"): errs.append(f"chapters[{i}].arabicTitle")
    if not c.get("arabicNarration"): errs.append(f"chapters[{i}].arabicNarration")
    if not c.get("visual"): errs.append(f"chapters[{i}].visual")
  ep = p.get("epilogue") or {}
  if not ep.get("arabicReflection"): errs.append("epilogue.arabicReflection")
  if not p.get("audioBed"): errs.append("audioBed")
  if errs:
    print(f"  INVALID {slug}: {', '.join(errs)}")
    sys.exit(1)
except Exception as e:
  print(f"  PARSE-ERR {slug}: {e}")
  sys.exit(1)
PY
done

if [ $missing -gt 0 ]; then
  echo "❌ $missing hekaya post(s) not ready — fix and retry"
  exit 3
fi
echo "✅ all ${#SLUGS[@]} props validated"
echo ""

# ── Phase 2: Verify each Suno track exists ───────────────────────────────
echo "━━━ PHASE 2 — verifying Suno tracks ━━━"
missing_audio=0
for slug in "${SLUGS[@]}"; do
  audio_path=$(python3 -c "import json; print(json.load(open('$HEKAYA/$slug/.meta/props.json'))['audioBed'])")
  full="$MYVIDEO/public/$audio_path"
  if [ -f "$full" ]; then
    bytes=$(stat -f%z "$full" 2>/dev/null || stat -c%s "$full")
    if [ "$bytes" -lt 100000 ]; then
      echo "  TINY    $slug: $audio_path is only $bytes bytes"
      missing_audio=$((missing_audio+1))
    else
      mb=$(( bytes / 1024 / 1024 ))
      echo "  ✓ $slug  (${mb}MB)"
    fi
  else
    echo "  MISSING $slug: $audio_path"
    missing_audio=$((missing_audio+1))
  fi
done
if [ $missing_audio -gt 0 ]; then
  echo "❌ $missing_audio Suno track(s) missing — run automation/scripts/generate-suno-music.py $DATE"
  exit 3
fi
echo "✅ all ${#SLUGS[@]} Suno tracks present"
echo ""

# ── Phase 3: Render each slug ────────────────────────────────────────────
echo "━━━ PHASE 3 — rendering ${#SLUGS[@]} hekaya reels ━━━"
ok=0 fail=0 failed=()
render_log="/tmp/photonect-hekaya-$DATE/render.log"
mkdir -p "/tmp/photonect-hekaya-$DATE/qa"
: > "$render_log"

start_batch=$(date +%s)
for slug in "${SLUGS[@]}"; do
  printf "  %-50s " "$slug"
  start=$(date +%s)
  pj="$HEKAYA/$slug/.meta/props.json"
  out="$HEKAYA/$slug/video.mp4"

  cd "$MYVIDEO"
  if npx remotion render Hekaya "$out" --props="$pj" >>"$render_log" 2>&1; then
    dur=$(( $(date +%s) - start ))
    if [ -f "$out" ]; then
      bytes=$(stat -f%z "$out" 2>/dev/null || stat -c%s "$out")
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
  cd "$ROOT"
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

# ── Phase 4: Hekaya QA — different floors than NEWS ─────────────────────
# Hekaya's palette is dusk-blue; the composition deliberately darkens images
# via a vignette + warm overlay. Using the news floors (L≥40) would false-flag
# legitimate atmospheric scenes. We use floors of L=22 for chapters and L=28
# for the prologue, and we still verify audio presence + no silence.
echo "━━━ PHASE 4 — hekaya QA ━━━"
qa_ok=0 qa_warn=0 qa_failed=()
for slug in "${SLUGS[@]}"; do
  printf "  %-50s " "$slug"
  mp4="$HEKAYA/$slug/video.mp4"
  qa_dir="/tmp/photonect-hekaya-$DATE/qa/$slug"
  mkdir -p "$qa_dir"

  # Frames at 6s (prologue), 18s (chapter 1), 36s (chapter 2), 60s (chapter 3)
  for pair in "6:prologue" "18:ch1" "36:ch2" "60:ch3"; do
    t="${pair%:*}" name="${pair#*:}"
    ffmpeg -y -loglevel error -ss "$t" -i "$mp4" -frames:v 1 "$qa_dir/$name.jpg" 2>/dev/null
  done
  audio_rms=$(ffmpeg -y -ss 6 -t 5 -i "$mp4" -ac 1 -af "volumedetect" -f null - 2>&1 | grep "mean_volume" | awk -F': ' '{print $2}' | awk '{print $1}' | head -1)

  python3 - "$slug" "$qa_dir" "$audio_rms" << 'PY'
import sys, json, os
from PIL import Image
slug, qa_dir, audio_rms = sys.argv[1], sys.argv[2], sys.argv[3]
try:
  rms = float(audio_rms) if audio_rms else -999.0
except:
  rms = -999.0
floors = {"prologue": 28.0, "ch1": 22.0, "ch2": 22.0, "ch3": 22.0}
res, fails = {}, []
for name, floor in floors.items():
  p = f"{qa_dir}/{name}.jpg"
  if not os.path.exists(p):
    fails.append(f"{name}-missing"); continue
  im = Image.open(p).convert("L")
  thumb = im.copy(); thumb.thumbnail((256, 256))
  hist = thumb.histogram(); total = sum(hist)
  L = sum(i * h for i, h in enumerate(hist)) / max(total, 1)
  res[name] = {"L": round(L, 1), "floor": floor}
  if L < floor:
    fails.append(f"{name}(L={L:.0f}<{floor})")
res["audio"] = {"rms_db": rms}
if rms > -50: res["audio"]["pass"] = True
else: fails.append(f"audio(rms={rms}dB)"); res["audio"]["pass"] = False
with open(f"{qa_dir}/report.json", "w") as f:
  json.dump(res, f, indent=2)
if fails:
  print(f"\033[1;33m⚠\033[0m {','.join(fails[:3])}"); sys.exit(1)
print(f"\033[1;32m✓\033[0m pro={res['prologue']['L']} ch={res['ch1']['L']}/{res['ch2']['L']}/{res['ch3']['L']} aud={res['audio']['rms_db']}dB")
PY
  rc=$?
  if [ $rc -eq 0 ]; then qa_ok=$((qa_ok+1)); else qa_warn=$((qa_warn+1)); qa_failed+=("$slug"); fi
done

echo ""
echo "qa: ok=$qa_ok warn=$qa_warn"
echo ""

echo "━━━ SUMMARY ━━━"
echo "Date:    $DATE"
echo "Reels:   $ok/$((ok+fail)) rendered"
echo "QA:      $qa_ok/${#SLUGS[@]} clean"
echo "Output:  data/hekaya/${DATE}-*/  (video.mp4 + caption.txt per folder)"
if [ ${#qa_failed[@]} -gt 0 ]; then
  echo ""
  echo "⚠ QA warnings (manually verify):"
  for s in "${qa_failed[@]}"; do
    echo "  - $s  (see /tmp/photonect-hekaya-$DATE/qa/$s/report.json)"
  done
fi

if [ $fail -gt 0 ]; then
  exit 1
elif [ $qa_warn -gt 0 ]; then
  echo "(QA warnings are non-fatal — visually inspect)"
  exit 0
else
  printf "\033[1;33m✅ All %d hekaya reels rendered + passed QA\033[0m\n" "${#SLUGS[@]}"
  exit 0
fi
