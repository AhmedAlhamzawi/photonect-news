#!/usr/bin/env python3
"""Cha Dude — ChatReel timeline builder.

Turns a captured thread (real replies + measured latencies) and the copy JSON
into ChatReel props. Typing indicators run for the REAL measured latency; the
customer side is scripted; the agent side is verbatim from the capture.

Usage:
  build_chat_props.py demo    <capture.json> <copy.json> <out.json> [--vo-open vo/x.mp3 --vo-close vo/y.mp3] [--default]
  build_chat_props.py pile    <copy.json> <out.json> [--vo vo/z.mp3] [--default]
"""
from __future__ import annotations
import argparse, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
FPS = 30
NUMBER = "0773 894 0795"


def f(sec: float) -> int:
    return int(round(sec * FPS))


def read_time(text: str) -> int:
    """Frames a viewer needs to read a bubble: ~0.32s/word + 0.9s, clamp 1.4–5.5s."""
    words = len(re.findall(r"\S+", text))
    return f(min(5.5, max(1.4, 0.9 + 0.32 * words)))


def clock(start: str, plus_s: float) -> str:
    h, m = map(int, start.split(":"))
    total = (h * 60 + m + int(plus_s // 60)) % (24 * 60)
    return f"{total // 60:02d}:{total % 60:02d}"


def vo_seconds(rel: str) -> float:
    """Duration of a VO clip from its words.json (0 if missing)."""
    if not rel: return 0.0
    wj = ROOT / "my-video" / "public" / rel.replace("vo.mp3", "words.json")
    try: return float(json.loads(wj.read_text())["durationSeconds"])
    except Exception: return 0.0


def endcard(copy_block: dict, small: str = "") -> dict:
    e = copy_block["endcard"]
    return {"title": e["title"], "sub": e.get("sub", ""), "number": NUMBER, "cta": e.get("cta", ""), "small": small}


def build_demo(capture: dict, copy: dict, vo_open: str, vo_close: str) -> dict:
    """Reel A — the real captured conversation."""
    A = copy["reelA"]
    turns = []
    t0 = "23:41"
    cur = f(2.6)                       # hook shows first; first customer bubble after ~2.6s
    elapsed_s = 0.0
    pairs = capture["turns"]
    for i in range(0, len(pairs), 2):
        c, a = pairs[i], pairs[i + 1]
        turns.append({"who": "customer", "text": c["text"], "time": clock(t0, elapsed_s), "startF": cur})
        cur += f(0.6)                       # the customer's message lands, then the agent starts typing
        lat = float(a.get("latency_s", 0))
        typing = f(max(0.5, lat)) if lat > 0.05 else f(0.4)
        cur += typing
        elapsed_s += 30 + lat
        turns.append({"who": "agent", "text": a["text"], "time": clock(t0, elapsed_s), "startF": cur,
                      "typingF": typing, "latencyS": round(lat, 1)})
        cur += read_time(a["text"]) + f(0.5)
    endcard_start = cur + f(0.4)
    close_len = vo_seconds(vo_close)
    total = endcard_start + max(f(4.2), f(close_len + 1.2))
    props = {
        "hook": A["hook"], "hookFrames": f(2.6),
        "contactName": "چا دود", "avatarLetter": "چ", "statusLine": "متصل الآن", "clockLabel": t0,
        "turns": turns, "stopwatchOnFirst": True,
        "endcard": endcard(A, A.get("small_print", "")),
        "endcardStartF": endcard_start,
        "voClips": ([{"src": vo_open, "atF": 0}] if vo_open else []) + ([{"src": vo_close, "atF": endcard_start - f(0.8)}] if vo_close else []),
        "bed": "", "bedVolume": 0.10, "sfx": True, "totalFrames": total,
    }
    return props


def build_pile(copy: dict, vo: str) -> dict:
    """Reel B — 7 messages every clinic gets after 10 pm, unanswered."""
    B = copy["reelB"]
    turns = []
    cur = f(2.4)
    for m in B["messages"]:
        turns.append({"who": "customer", "text": m["text"], "time": m["time"], "startF": cur, "unanswered": True})
        cur += f(1.15)
    cur += f(1.6)
    vo_len = vo_seconds(vo)
    # the turn in the VO («ويا چا دود…») should land on the end card: end card at ~62% of the VO
    endcard_start = max(cur + f(0.4), f(vo_len * 0.62)) if vo_len else cur + f(0.4)
    total = endcard_start + max(f(5.0), f(vo_len - vo_len * 0.62 + 1.5))
    props = {
        "hook": B["hook"], "hookFrames": f(2.4),
        "contactName": "عيادة الدكتور", "avatarLetter": "ع", "statusLine": "آخر ظهور 10:02 م", "clockLabel": "02:31",
        "turns": turns, "stopwatchOnFirst": False,
        "endcard": endcard(B),
        "endcardStartF": endcard_start,
        "voClips": [{"src": vo, "atF": 0}] if vo else [],
        "bed": "", "bedVolume": 0.10, "sfx": True, "totalFrames": total,
    }
    return props


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["demo", "pile"])
    ap.add_argument("inputs", nargs="+")
    ap.add_argument("--vo-open", default=""); ap.add_argument("--vo-close", default=""); ap.add_argument("--vo", default="")
    ap.add_argument("--default", action="store_true")
    a = ap.parse_args()
    if a.mode == "demo":
        cap, cp, out = a.inputs
        props = build_demo(json.loads(Path(cap).read_text()), json.loads(Path(cp).read_text()), a.vo_open, a.vo_close)
    else:
        cp, out = a.inputs
        props = build_pile(json.loads(Path(cp).read_text()), a.vo)
    Path(out).write_text(json.dumps(props, ensure_ascii=False, indent=1))
    print(f"✓ {out}  total={props['totalFrames']}f ({props['totalFrames']/FPS:.1f}s) turns={len(props['turns'])}")
    if a.default:
        ts = ROOT / "my-video/src/compositions/ChatReel/defaultProps.ts"
        ts.write_text("// AUTO-GENERATED by scripts/tenants/cha_dude/build_chat_props.py\n"
                      'import type { ChatReelProps } from "./schema";\n\n'
                      "export const chatDefaultProps: ChatReelProps = " + json.dumps(props, ensure_ascii=False, indent=2) + ";\n")
        print(f"✓ {ts}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
