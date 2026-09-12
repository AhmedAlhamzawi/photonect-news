#!/usr/bin/env python3
"""Cha Dude — weekly receipts carousel (6 × 1080×1350 JPG) via headless Chrome.

Chat-native slides in the tenant's visual system: ink ground, reply-green for
the agent, amber for the big number. Slide 3 shows a REAL thread from the
Photonect inbox (names/numbers never shown; only the first-party text).

Usage: render_carousel.py <copy.json> <receipts_raw.json> <out_dir>
"""
from __future__ import annotations
import json, re, subprocess, sys, pathlib, html

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
INK, RAISED, REPLY, AMBER, TEXT, DIM, DEAD = "#231F20", "#2E2A2B", "#24E07E", "#FDBB11", "#F4F2F0", "#9A9491", "#5C5654"
NUMBER = "0773 894 0795"

CSS = f"""
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@800;900&family=IBM+Plex+Sans+Arabic:wght@400;600&family=Inter:wght@700;900&display=swap');
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;background:{INK};color:{TEXT};direction:rtl;font-family:'IBM Plex Sans Arabic',sans-serif;overflow:hidden;position:relative}}
.pad{{position:absolute;inset:96px}}
.kicker{{font-family:'Cairo';font-weight:800;font-size:30px;color:{REPLY};letter-spacing:.02em}}
h1{{font-family:'Cairo';font-weight:900;font-size:88px;line-height:1.18;margin-top:26px;color:{TEXT}}}
h1 .amber{{color:{AMBER}}}
.sub{{font-size:38px;line-height:1.6;color:{DIM};margin-top:30px;max-width:860px}}
.foot{{position:absolute;bottom:96px;left:96px;right:96px;display:flex;justify-content:space-between;align-items:center;color:{DIM};font-size:26px}}
.mark{{font-family:'Inter';font-weight:900;letter-spacing:3px;color:{TEXT};display:flex;align-items:center;gap:12px}}
.mark i{{width:12px;height:12px;border-radius:9px;background:#D72638;display:inline-block}}
.pager{{font-family:'Inter';font-weight:700;direction:ltr}}
.big{{font-family:'Inter';font-weight:900;font-size:220px;line-height:1;color:{AMBER};margin-top:20px;direction:ltr;text-align:right}}
.bubble{{max-width:78%;border-radius:26px;padding:22px 30px 40px;font-size:34px;line-height:1.5;position:relative;margin:16px 0;box-shadow:0 6px 18px rgba(0,0,0,.35)}}
.in{{background:{RAISED};color:{TEXT};margin-left:auto;border-bottom-right-radius:6px}}
.out{{background:{REPLY};color:#0A1F14;margin-right:auto;border-bottom-left-radius:6px}}
.meta{{position:absolute;bottom:10px;left:20px;font-family:'Inter';font-size:22px;color:{DIM}}}
.out .meta{{color:#0A1F14aa}}
.badge{{position:absolute;top:-22px;left:12px;background:{INK};border:2px solid {REPLY};color:{REPLY};font-size:22px;font-weight:600;padding:2px 14px;border-radius:999px}}
.thread{{margin-top:40px;display:flex;flex-direction:column}}
.num{{display:inline-block;background:{REPLY};color:{INK};font-family:'Inter';font-weight:900;font-size:78px;letter-spacing:2px;padding:20px 44px;border-radius:24px;direction:ltr;margin-top:40px}}
.cta{{font-family:'Cairo';font-weight:800;font-size:44px;color:{AMBER};margin-top:34px}}
.tick{{color:{DEAD}}}
"""


def page(body: str, n: int) -> str:
    return f"""<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="pad">{body}</div>
<div class="foot"><span class="mark"><i></i>PHOTONECT</span><span class="pager">{n} / 6</span></div></body></html>"""


def main() -> int:
    copy = json.loads(pathlib.Path(sys.argv[1]).read_text())
    rec = json.loads(pathlib.Path(sys.argv[2]).read_text())
    out = pathlib.Path(sys.argv[3]); out.mkdir(parents=True, exist_ok=True)
    slides = copy["carousel"]["slides"]
    E = html.escape

    # pick the real 02:22 thread for slide 3 (first-party inbox, no names/numbers)
    night = [s for s in rec["snippets"] if s["h"] < "06:00" and "عباس" not in s["a"]]
    thread = night[:2] if night else rec["snippets"][:2]

    bodies = []
    s = slides[0]; bodies.append(f'<div class="kicker">{E(s["kicker"])}</div><h1>{E(s["headline"])}</h1><div class="sub">{E(s["sub"])}</div>')
    s = slides[1]; bodies.append(f'<div class="kicker">{E(s["kicker"])}</div><div class="big">{rec["after20_share"]}%</div><h1 style="font-size:70px">من الرسائل تجي بعد 8 بالليل</h1><div class="sub">{E(s["sub"])}</div>')
    s = slides[2]
    th = "".join(
        f'<div class="bubble in">{E(t["q"])}<span class="meta">{t["h"]}</span></div>'
        f'<div class="bubble out"><span class="badge">⚡ رد</span>{E(t["a"])}<span class="meta">{t["h"]}</span></div>' for t in thread)
    bodies.append(f'<div class="kicker">{E(s["kicker"])}</div><h1 style="font-size:64px">{E(s["headline"])}</h1><div class="thread">{th}</div>')
    s = slides[3]; bodies.append(f'<div class="kicker">{E(s["kicker"])}</div><div class="big" style="font-size:150px">1.8–3.4<span style="font-size:60px"> ث</span></div><h1 style="font-size:66px">{E(s["headline"])}</h1><div class="sub">{E(s["sub"])}</div>')
    s = slides[4]; h5 = re.sub(r"^\s*\d+%\s*", "", s["headline"]); bodies.append(f'<div class="kicker">{E(s["kicker"])}</div><div class="big">{rec["after22_share"]}%</div><h1 style="font-size:66px">{E(h5)}</h1><div class="sub">{E(s["sub"])}</div>')
    s = slides[5]; bodies.append(f'<div class="kicker">{E(s["kicker"])}</div><h1>{E(s["headline"])}</h1><div class="num">{NUMBER}</div><div class="cta">دزها لصاحب عيادة تعرفه</div>')

    for i, b in enumerate(bodies, 1):
        hp = out / f"slide_{i}.html"; hp.write_text(page(b, i), encoding="utf-8")
        png = out / f"slide_{i}.png"
        subprocess.run([CHROME, "--headless", "--disable-gpu", "--hide-scrollbars", "--window-size=1080,1350",
                        "--virtual-time-budget=6000", f"--screenshot={png}", f"file://{hp}"], check=True, capture_output=True)
        subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", str(png), "-q:v", "2", str(out / f"slide_{i}.jpg")], check=True)
        print(f"  ✓ slide_{i}.jpg")
    return 0


if __name__ == "__main__":
    sys.exit(main())
