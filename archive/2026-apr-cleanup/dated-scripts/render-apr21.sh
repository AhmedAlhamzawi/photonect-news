#!/usr/bin/env bash
# render-apr21.sh — render + QA the 12 April 21 slugs using the V4 engine.
# One-off for today's slate. Emits per-slug progress lines so a Monitor can
# stream it, plus a final report with render + QA counts.
#
# Usage: bash render-apr21.sh

set -u

HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$HERE/../.." && pwd)"
cd "$ROOT"

SLUGS=(
  2026-04-21-iraq-vote
  2026-04-21-brent-150
  2026-04-21-ceasefire-break
  2026-04-21-ai-nuclear-sim
  2026-04-21-berlin-protest
  2026-04-21-un-secgen-plan
  2026-04-21-crypto-tether-depeg
  2026-04-21-opec-emergency-2
  2026-04-21-kdp-split
  2026-04-21-imf-sa-loan
  2026-04-21-egypt-mobilize
  2026-04-21-north-korea-ship
)

ok=0
fail=0
qa_fail=0
failed=()
qa_failed=()

render_log="/tmp/photonect-apr21/render.log"
mkdir -p /tmp/photonect-apr21/qa
: > "$render_log"

# V4 engine reel is 34s (1020f @ 30fps):
#  Breaking 150f (5s) + Beat1 270f (5-14s) + Beat2 270f (14-23s) + Beat3 240f (23-31s) + Sources 90f (31-34s)
# QA samples mid-beat: t=2 (hero), t=9 (beat1), t=18 (beat2), t=27 (beat3).
qa_reel() {
  local slug="$1"
  local mp4="data/posts/$slug/newsreel_v3.mp4"
  if [ ! -f "$mp4" ]; then
    echo "QA-SKIP $slug (no mp4)"; return 2
  fi
  local d="/tmp/photonect-apr21/qa/$slug"
  mkdir -p "$d"
  ffmpeg -y -loglevel error -ss 2  -i "$mp4" -frames:v 1 "$d/hero.jpg"  2>/dev/null
  ffmpeg -y -loglevel error -ss 9  -i "$mp4" -frames:v 1 "$d/beat1.jpg" 2>/dev/null
  ffmpeg -y -loglevel error -ss 18 -i "$mp4" -frames:v 1 "$d/beat2.jpg" 2>/dev/null
  ffmpeg -y -loglevel error -ss 27 -i "$mp4" -frames:v 1 "$d/beat3.jpg" 2>/dev/null

  python3 - "$slug" "$d" <<'PY'
import sys, json, os
from PIL import Image
slug, d = sys.argv[1], sys.argv[2]
floors = {"hero": 50.0, "beat1": 40.0, "beat2": 40.0, "beat3": 40.0}  # 2026-04-22: V4 overlay is heavier than raw-image floor — calibrated to post-render target readability (text still reads cleanly at L≥40)
res, fails = {}, []
for name, floor in floors.items():
    try:
        im = Image.open(f"{d}/{name}.jpg").convert("L")
        im.thumbnail((256, 256))
        hist = im.histogram()
        total = sum(hist)
        L = sum(i * h for i, h in enumerate(hist)) / max(total, 1)
        res[name] = {"L": round(L, 2), "floor": floor, "pass": L >= floor}
        if L < floor:
            fails.append(f"{name}(L={L:.1f}<{floor})")
    except Exception as e:
        res[name] = {"err": str(e)}
        fails.append(f"{name}(err)")
os.makedirs("/tmp/photonect-apr21/qa", exist_ok=True)
with open(f"/tmp/photonect-apr21/qa/{slug}.json", "w") as f:
    json.dump(res, f)
if fails:
    print(f"QA-FAIL {slug} {','.join(fails)}"); sys.exit(1)
print(f"QA-PASS {slug} hero={res['hero']['L']} b1={res['beat1']['L']} b2={res['beat2']['L']} b3={res['beat3']['L']}")
PY
}

echo "=== APR21 RENDER START $(date) ==="
for slug in "${SLUGS[@]}"; do
  echo "=== $slug START ==="
  start=$(date +%s)
  if bash "$HERE/render-reel.sh" "$slug" v3 >>"$render_log" 2>&1; then
    dur=$(( $(date +%s) - start ))
    mp4="data/posts/$slug/newsreel_v3.mp4"
    if [ -f "$mp4" ]; then
      bytes=$(stat -f%z "$mp4" 2>/dev/null || stat -c%s "$mp4")
      echo "RENDER-OK $slug ${dur}s ${bytes}B"
      ok=$((ok+1))
      if ! qa_reel "$slug"; then
        qa_fail=$((qa_fail+1)); qa_failed+=("$slug")
      fi
    else
      echo "RENDER-FAIL $slug no-mp4-produced"
      fail=$((fail+1)); failed+=("$slug")
    fi
  else
    dur=$(( $(date +%s) - start ))
    echo "RENDER-FAIL $slug ${dur}s"
    fail=$((fail+1)); failed+=("$slug")
    tail -6 "$render_log" | sed 's/^/  /'
  fi
done

echo ""
echo "=== APR21 ALL DONE $(date) ==="
echo "render ok=$ok fail=$fail"
echo "qa fail=$qa_fail"
if [ ${#failed[@]} -gt 0 ]; then
  echo "RENDER FAILED: ${failed[*]}"
fi
if [ ${#qa_failed[@]} -gt 0 ]; then
  echo "QA FAILED: ${qa_failed[*]}"
fi
exit $(( fail + qa_fail ))
