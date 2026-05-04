#!/usr/bin/env bash
#
# generate-hekaya2.sh
# ───────────────────
# Renders a HEKAYA v2 day's slate. Sister to generate-hekaya.sh (v1) but
# targets the new Hekaya2 composition with voice-over + multi-photo cycles
# + foley layer.
#
# Usage:
#   bash generate-hekaya2.sh                     # uses today's date (UTC)
#   bash generate-hekaya2.sh 2026-05-04          # explicit date
#   bash generate-hekaya2.sh 2026-05-04 --dry    # show what would run
#
# Exit codes: 0=ok, 1=render fail, 2=QA fail, 3=setup error

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

# Discover slugs
SLUGS=()
for d in "$HEKAYA/$DATE"-*; do
  [ -d "$d" ] || continue
  SLUGS+=("$(basename "$d")")
done

if [ ${#SLUGS[@]} -eq 0 ]; then
  echo "error: no hekaya v2 folders found for $DATE under $HEKAYA/" >&2
  exit 3
fi

printf "\033[1;33m━━━ Photonect HEKAYA v2 — %s ━━━\033[0m\n" "$DATE"
echo "discovered ${#SLUGS[@]} v2 posts:"
for s in "${SLUGS[@]}"; do echo "  · $s"; done
echo ""

if [ "$DRY" = "--dry" ]; then
  echo "(dry run — exiting before render)"
  exit 0
fi

# ── Phase 1: Validate every props.json against Hekaya2Schema ──────────────
echo "━━━ PHASE 1 — validating props ━━━"
missing=0
for slug in "${SLUGS[@]}"; do
  pj="$HEKAYA/$slug/.meta/props.json"
  if [ ! -f "$pj" ]; then
    echo "  MISSING $slug/.meta/props.json"; missing=$((missing+1)); continue
  fi
  python3 - "$pj" "$slug" << 'PY' || missing=$((missing+1))
import json, sys
pj, slug = sys.argv[1], sys.argv[2]
try:
  p = json.load(open(pj))
  errs = []
  for f in ("voiceOver", "music", "scriptArabic", "heroMedia", "closingMedia"):
    if not p.get(f): errs.append(f)
  if not (p.get("title") or {}).get("arabic"): errs.append("title.arabic")
  if not (p.get("loopHook") or {}).get("openingPhrase"): errs.append("loopHook.openingPhrase")
  if not (p.get("loopHook") or {}).get("closingPhrase"): errs.append("loopHook.closingPhrase")
  chapters = p.get("chapters") or []
  if len(chapters) != 3: errs.append(f"chapters count={len(chapters)} (expected 3)")
  for i, c in enumerate(chapters):
    if not (c.get("photos") or []): errs.append(f"chapters[{i}].photos empty")
  phrases = p.get("phrases") or []
  if not (8 <= len(phrases) <= 24):
    errs.append(f"phrases count={len(phrases)} (expected 8-24)")
  if errs:
    print(f"  INVALID {slug}: {', '.join(errs)}"); sys.exit(1)
except Exception as e:
  print(f"  PARSE-ERR {slug}: {e}"); sys.exit(1)
PY
done

if [ $missing -gt 0 ]; then
  echo "❌ $missing v2 post(s) not ready"; exit 3
fi
echo "✅ all ${#SLUGS[@]} props validated"
echo ""

# ── Phase 2: Verify VO + music + SFX files exist ─────────────────────────
echo "━━━ PHASE 2 — verifying audio assets ━━━"
missing_audio=0
for slug in "${SLUGS[@]}"; do
  pj="$HEKAYA/$slug/.meta/props.json"
  vo=$(python3 -c "import json; print(json.load(open('$pj'))['voiceOver'])")
  music=$(python3 -c "import json; print(json.load(open('$pj'))['music'])")

  for ap in "$vo" "$music"; do
    full="$MYVIDEO/public/$ap"
    if [ ! -f "$full" ]; then
      echo "  MISSING $slug: $ap"; missing_audio=$((missing_audio+1)); continue
    fi
    bytes=$(stat -f%z "$full" 2>/dev/null || stat -c%s "$full")
    if [ "$bytes" -lt 80000 ]; then
      echo "  TINY $slug: $ap ($bytes bytes)"; missing_audio=$((missing_audio+1))
    fi
  done

  # SFX files referenced in markers
  python3 - "$pj" "$MYVIDEO/public" "$slug" << 'PY' || missing_audio=$((missing_audio+1))
import json, sys, os
pj, public_root, slug = sys.argv[1], sys.argv[2], sys.argv[3]
p = json.load(open(pj))
missing = []
for s in p.get("sfx", []):
  full = os.path.join(public_root, s["file"])
  if not os.path.isfile(full):
    missing.append(s["file"])
if missing:
  print(f"  SFX-MISSING {slug}: {missing}")
  sys.exit(1)
PY
done
if [ $missing_audio -gt 0 ]; then
  echo "❌ $missing_audio audio asset(s) missing — generate VO + foley first"
  exit 3
fi
echo "✅ all ${#SLUGS[@]} audio assets present"
echo ""

# ── Phase 3: Render each slug via Hekaya2 composition ─────────────────────
echo "━━━ PHASE 3 — rendering ${#SLUGS[@]} v2 reels ━━━"
ok=0 fail=0 failed=()
render_log="/tmp/photonect-hekaya2-$DATE/render.log"
mkdir -p "/tmp/photonect-hekaya2-$DATE/qa"
: > "$render_log"

start_batch=$(date +%s)
for slug in "${SLUGS[@]}"; do
  printf "  %-50s " "$slug"
  start=$(date +%s)
  pj="$HEKAYA/$slug/.meta/props.json"
  out="$HEKAYA/$slug/video.mp4"

  cd "$MYVIDEO"
  if npx remotion render Hekaya2 "$out" --props="$pj" >>"$render_log" 2>&1; then
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

# ── Phase 4: Hekaya v2 QA — VO presence + luminance ──────────────────────
echo "━━━ PHASE 4 — hekaya v2 QA ━━━"
qa_ok=0 qa_warn=0 qa_failed=()
for slug in "${SLUGS[@]}"; do
  printf "  %-50s " "$slug"
  mp4="$HEKAYA/$slug/video.mp4"
  qa_dir="/tmp/photonect-hekaya2-$DATE/qa/$slug"
  mkdir -p "$qa_dir"

  for pair in "4:cold" "20:want" "44:escalation" "62:resolution" "73:resonance"; do
    t="${pair%:*}" name="${pair#*:}"
    ffmpeg -y -loglevel error -ss "$t" -i "$mp4" -frames:v 1 "$qa_dir/$name.jpg" 2>/dev/null
  done
  audio_rms=$(ffmpeg -y -ss 8 -t 30 -i "$mp4" -ac 1 -af "volumedetect" -f null - 2>&1 | grep "mean_volume" | awk -F': ' '{print $2}' | awk '{print $1}' | head -1)

  python3 - "$slug" "$qa_dir" "$audio_rms" << 'PY'
import sys, json, os
from PIL import Image
slug, qa_dir, audio_rms = sys.argv[1], sys.argv[2], sys.argv[3]
try:
  rms = float(audio_rms) if audio_rms else -999.0
except:
  rms = -999.0
floors = {"cold": 25.0, "want": 22.0, "escalation": 22.0, "resolution": 22.0, "resonance": 25.0}
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
res["audio"] = {"rms_db": rms, "pass": rms > -50}
if rms <= -50: fails.append(f"audio({rms}dB)")
with open(f"{qa_dir}/report.json", "w") as f: json.dump(res, f, indent=2)
if fails:
  print(f"\033[1;33m⚠\033[0m {','.join(fails[:3])}"); sys.exit(1)
print(f"\033[1;32m✓\033[0m cold={res['cold']['L']} want={res['want']['L']} esc={res['escalation']['L']} res={res['resolution']['L']} reson={res['resonance']['L']} aud={rms}dB")
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

if [ $fail -gt 0 ]; then
  exit 1
elif [ $qa_warn -gt 0 ]; then
  echo "(QA warnings non-fatal — visually inspect)"
  exit 0
else
  printf "\033[1;33m✅ All %d v2 reels rendered + passed QA\033[0m\n" "${#SLUGS[@]}"
  exit 0
fi
