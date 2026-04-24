#!/usr/bin/env bash
# render-apr20-rehunts2.sh — third re-render pass for the 3 April 20 slugs that
# failed QA after the first rehunt (architectural overlay fix + hero floor 80→90
# + broll floor 75→85 applied in this pass).
set -u

HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$HERE/../.." && pwd)"
cd "$ROOT"

SLUGS=(
  2026-04-20-opec-emergency
  2026-04-20-arctic-route
  2026-04-20-starlink-mideast
)

ok=0; fail=0; qa_fail=0
failed=(); qa_failed=()
log="/tmp/photonect-apr20/render-rehunts2.log"
: > "$log"

qa_reel() {
  local slug="$1"
  local mp4="data/posts/$slug/newsreel_v3.mp4"
  local tmpdir="/tmp/photonect-apr20/qa-rehunt2-$slug"
  mkdir -p "$tmpdir"
  ffmpeg -y -loglevel error -ss 1.2 -i "$mp4" -frames:v 1 "$tmpdir/hero.jpg"  2>/dev/null
  ffmpeg -y -loglevel error -ss 6   -i "$mp4" -frames:v 1 "$tmpdir/beat1.jpg" 2>/dev/null
  ffmpeg -y -loglevel error -ss 14  -i "$mp4" -frames:v 1 "$tmpdir/beat2.jpg" 2>/dev/null
  ffmpeg -y -loglevel error -ss 25  -i "$mp4" -frames:v 1 "$tmpdir/beat3.jpg" 2>/dev/null
  python3 - "$slug" "$tmpdir" <<'PY'
import sys
from PIL import Image
slug, d = sys.argv[1], sys.argv[2]
floors = {"hero": 62.0, "beat1": 40.0, "beat2": 40.0, "beat3": 40.0}
fails=[]; res={}
for name, floor in floors.items():
    im = Image.open(f"{d}/{name}.jpg").convert("L")
    im.thumbnail((256, 256))
    hist = im.histogram(); total = sum(hist)
    L = sum(i*h for i,h in enumerate(hist))/max(total,1)
    res[name] = {"L": round(L, 2), "pass": L>=floor}
    if L<floor: fails.append(f"{name}(L={L:.1f}<{floor})")
if fails:
    print(f"QA3-FAIL {slug} {','.join(fails)}")
    sys.exit(1)
else:
    print(f"QA3-PASS {slug} hero={res['hero']['L']} b1={res['beat1']['L']} b2={res['beat2']['L']} b3={res['beat3']['L']}")
PY
}

echo "=== RE-RENDER2 START $(date) ==="
for slug in "${SLUGS[@]}"; do
  echo "=== $slug RE2-START ==="
  start=$(date +%s)
  if bash "$HERE/render-reel.sh" "$slug" v3 >>"$log" 2>&1; then
    dur=$(( $(date +%s) - start ))
    mp4="data/posts/$slug/newsreel_v3.mp4"
    bytes=$(stat -f%z "$mp4" 2>/dev/null || stat -c%s "$mp4")
    echo "RERENDER2-OK $slug ${dur}s ${bytes}B"
    ok=$((ok+1))
    if ! qa_reel "$slug"; then
      qa_fail=$((qa_fail+1)); qa_failed+=("$slug")
    fi
  else
    dur=$(( $(date +%s) - start ))
    echo "RERENDER2-FAIL $slug ${dur}s"
    fail=$((fail+1)); failed+=("$slug")
    tail -6 "$log" | sed 's/^/  /'
  fi
done

echo ""
echo "=== RE-RENDER2 ALL DONE $(date) ==="
echo "rerender2 ok=$ok fail=$fail qa-fail=$qa_fail"
[ ${#failed[@]} -gt 0 ]   && echo "RERENDER2 FAILED: ${failed[*]}"
[ ${#qa_failed[@]} -gt 0 ] && echo "QA3 STILL FAILED: ${qa_failed[*]}"
exit $(( fail + qa_fail ))
