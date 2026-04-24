#!/usr/bin/env bash
# hunt-media.sh — populate story-specific media for a post slug.
# Wraps media_hunter.py, validates the result, and is safe to re-run.
#
# Usage:
#   ./hunt-media.sh <slug> [--force]
#   ./hunt-media.sh --all [--force]

set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$HERE/../.." && pwd)"
PY="$HERE/media_hunter.py"

if [ ! -x "$PY" ]; then
  chmod +x "$PY"
fi

exec python3 "$PY" "$@"
