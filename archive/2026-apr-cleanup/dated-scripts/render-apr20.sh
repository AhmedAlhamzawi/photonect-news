#!/usr/bin/env bash
# render-apr20.sh — render + QA the 12 April 20 slugs.
# One-off script (can be deleted after today). Emits a per-slug progress
# line so a Monitor can stream it, then a final report.
#
# Usage: bash render-apr20.sh

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

ok=0
fail=0
qa_fail=0
failed=()
qa_failed=()

render_reel_log="/tmp/photonect-apr20/render.log"
mkdir -p /tmp/photonect-apr20
: > "$render_reel_log"

# Inline QA — extract 4 frames + compute luminance via PIL
qa_reel() {
  local slug="$1"
  local mp4="data/posts/$slug/newsreel_v3.mp4"
  if [ ! -f "$mp4" ]; then
    echo "QA-SKIP $slug (no mp4)"
    return 2
  fi
  local tmpdir="/tmp/photonect-apr20/qa-$slug"
  mkdir -p "$tmpdir"
  # Extract 4 frames: hero / beat1 / beat2 / beat3
  ffmpeg -y -loglevel error -ss 1.2 -i "$mp4" -frames:v 1 "$tmpdir/hero.jpg"  2>/dev/null
  ffmpeg -y -loglevel error -ss 6   -i "$mp4" -frames:v 1 "$tmpdir/beat1.jpg" 2>/dev/null
  ffmpeg -y -loglevel error -ss 14  -i "$mp4" -frames:v 1 "$tmpdir/beat2.jpg" 2>/dev/null
  ffmpeg -y -loglevel error -ss 25  -i "$mp4" -frames:v 1 "$tmpdir/beat3.jpg" 2>/dev/null

  # Compute luminance via python3+PIL
  python3 - "$slug" "$tmpdir" <<'PY'
import sys, json
from PIL import Image
slug, d = sys.argv[1], sys.argv[2]
floors = {"hero": 62.0, "beat1": 40.0, "beat2": 40.0, "beat3": 40.0}
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
import os
os.makedirs("/tmp/photonect-apr20/qa", exist_ok=True)
with open(f"/tmp/photonect-apr20/qa/{slug}.json", "w") as f:
    json.dump(res, f)
if fails:
    print(f"QA-FAIL {slug} {','.join(fails)}")
    sys.exit(1)
else:
    print(f"QA-PASS {slug} hero={res['hero']['L']} b1={res['beat1']['L']} b2={res['beat2']['L']} b3={res['beat3']['L']}")
PY
}

echo "=== RENDER START $(date) ==="
for slug in "${SLUGS[@]}"; do
  echo "=== $slug START ==="
  start=$(date +%s)
  if bash "$HERE/render-reel.sh" "$slug" v3 >>"$render_reel_log" 2>&1; then
    dur=$(( $(date +%s) - start ))
    mp4="data/posts/$slug/newsreel_v3.mp4"
    if [ -f "$mp4" ]; then
      bytes=$(stat -f%z "$mp4" 2>/dev/null || stat -c%s "$mp4")
      echo "RENDER-OK $slug ${dur}s ${bytes}B"
      ok=$((ok+1))
      # In-flight QA
      if ! qa_reel "$slug"; then
        qa_fail=$((qa_fail+1))
        qa_failed+=("$slug")
      fi
    else
      echo "RENDER-FAIL $slug no-mp4-produced"
      fail=$((fail+1)); failed+=("$slug")
    fi
  else
    dur=$(( $(date +%s) - start ))
    echo "RENDER-FAIL $slug ${dur}s"
    fail=$((fail+1)); failed+=("$slug")
    tail -6 "$render_reel_log" | sed 's/^/  /'
  fi
done

echo ""
echo "=== ALL DONE $(date) ==="
echo "render ok=$ok fail=$fail"
echo "qa fail=$qa_fail"
if [ ${#failed[@]} -gt 0 ]; then
  echo "RENDER FAILED: ${failed[*]}"
fi
if [ ${#qa_failed[@]} -gt 0 ]; then
  echo "QA FAILED: ${qa_failed[*]}"
fi
exit $(( fail + qa_fail ))
