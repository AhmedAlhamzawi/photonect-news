#!/usr/bin/env python3
"""Assemble the Photonect video-product sales proposal → A4 PDF.

Self-contained: Tajawal embedded as base64, sample scenes embedded as base64,
so the PDF renders identically anywhere and the HTML needs no network.
Rendered with headless Chrome --print-to-pdf.
"""
from __future__ import annotations
import base64, pathlib, subprocess, sys

A = pathlib.Path("/tmp/proposal_assets")
OUT_HTML = A / "proposal.html"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

FONT = (A / "tajawal_embed.css").read_text()
IMG = {n: (A / f"{n}.b64").read_text() for n in
       ["sample_restaurant", "sample_clinic", "sample_realestate"]}

# ── copy (filled from the Arabic copy workflow; see COPY dict below) ─────────
from copy_ar import COPY  # noqa: E402


def page(inner: str, cls: str = "") -> str:
    return f'<section class="page {cls}">{inner}</section>'


def build() -> str:
    c = COPY
    css = """
*{margin:0;padding:0;box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact}
@page{size:A4;margin:0}
html{font-family:'Tajawal',sans-serif}
body{direction:rtl;background:#fff;color:#12121a}
.page{width:210mm;height:297mm;position:relative;overflow:hidden;page-break-after:always;background:#fff}
.page:last-child{page-break-after:auto}
.pad{padding:18mm 16mm}
/* ---- brand ---- */
:root{--y:#FFC217;--r:#D72638;--ink:#0A0A10;--paper:#F7F7F2;--mut:#6B6B78}
.dark{background:var(--ink);color:#F7F7F2}
.mark{display:inline-flex;flex-direction:column;align-items:center;line-height:.84;
  font-family:'Tajawal',Arial Black,sans-serif;font-weight:900;letter-spacing:.02em}
.mark .l1{position:relative}
.mark .dash{position:absolute;left:0.06em;top:-0.16em;width:.30em;height:.075em;background:var(--r);border-radius:99px}
.markwrap{display:flex;align-items:center;gap:5mm}
.badge{width:15mm;height:15mm;border-radius:99px;background:#fff;display:flex;align-items:center;
  justify-content:center;flex:0 0 auto}
.badge .mark{font-size:3.5mm;color:#0A0A10}
h1{font-weight:900;line-height:1.18;letter-spacing:-.01em}
h2{font-weight:900;font-size:10.5mm;line-height:1.25;letter-spacing:-.01em}
h3{font-weight:800;font-size:5.6mm;line-height:1.35}
p{font-weight:400;line-height:1.75;font-size:4.1mm;color:#33333f}
.dark p{color:#C9C9D4}
.eyebrow{font-weight:800;font-size:3.2mm;letter-spacing:.22em;color:var(--r)}
.dark .eyebrow{color:var(--y)}
.rule{height:1.2mm;width:24mm;background:var(--y);border-radius:9px;margin:5mm 0}
.mut{color:var(--mut);font-size:3.5mm}
/* ---- cover ---- */
.cover{display:flex;flex-direction:column;justify-content:space-between;
  background:radial-gradient(120% 90% at 78% 8%,#23232c 0%,#0A0A10 62%)}
.cover .glow{position:absolute;width:120mm;height:120mm;border-radius:99px;top:-40mm;left:-30mm;
  background:radial-gradient(circle,rgba(255,194,23,.16),transparent 68%)}
.cover .glow2{position:absolute;width:100mm;height:100mm;border-radius:99px;bottom:-30mm;right:-24mm;
  background:radial-gradient(circle,rgba(215,38,56,.20),transparent 68%)}
.stat3{display:flex;gap:0;border-top:.4mm solid rgba(255,255,255,.16)}
.stat3 div{flex:1;padding:6mm 0 0}
.stat3 .n{font-weight:900;font-size:9mm;color:var(--y);line-height:1}
.stat3 .k{font-size:3.2mm;color:#9A9AA8;margin-top:1.5mm}
/* ---- generic blocks ---- */
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:8mm}
.card{background:var(--paper);border-radius:4mm;padding:7mm}
.card.k{background:#101018;color:#F7F7F2}
.card.k p{color:#C9C9D4}
.card.k h3{color:var(--y)}
.num{font-weight:900;font-size:7mm;color:var(--r);line-height:1}
.tick{display:flex;gap:3.5mm;align-items:flex-start;margin-bottom:3.8mm}
.tick .d{width:4.6mm;height:4.6mm;border-radius:99px;background:var(--y);flex:0 0 auto;margin-top:1mm;
  display:flex;align-items:center;justify-content:center;font-size:2.8mm;font-weight:900;color:#0A0A10}
.tick p{font-size:4mm;line-height:1.6}
/* ---- phone mockups ---- */
.phones{display:flex;gap:6mm;justify-content:center;align-items:flex-start}
.phone{width:47mm;border-radius:5mm;overflow:hidden;position:relative;background:#000;
  box-shadow:0 6mm 14mm rgba(0,0,0,.30);flex:0 0 auto}
.phone img{width:100%;height:84mm;object-fit:cover;display:block}
.phone .chip{position:absolute;top:2.4mm;right:2.4mm;background:rgba(8,8,12,.72);border-radius:1.6mm;
  padding:.9mm 1.8mm;display:flex;align-items:center;gap:1mm}
.phone .chip i{width:1.4mm;height:1.4mm;border-radius:99px;background:var(--r);display:block}
.phone .chip b{font-size:1.9mm;color:#fff;font-weight:900;letter-spacing:.06em}
.phone .hd{position:absolute;top:12mm;right:3mm;left:3mm;text-align:center;color:#fff;font-weight:900;
  font-size:4.1mm;line-height:1.3;text-shadow:0 1mm 3mm rgba(0,0,0,.9)}
.phone .pop{position:absolute;top:34mm;left:0;right:0;display:flex;justify-content:center}
.phone .pop span{background:rgba(8,8,12,.82);border:.35mm solid var(--y);border-radius:2mm;
  padding:1.4mm 3mm;color:var(--y);font-weight:900;font-size:4.6mm}
.phone .cap{position:absolute;bottom:5mm;left:2.5mm;right:2.5mm;text-align:center}
.phone .cap span{background:rgba(8,8,12,.62);border-radius:1.6mm;padding:1.2mm 2mm;display:inline;
  font-size:2.9mm;font-weight:800;color:#fff;line-height:2.2;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.phone .cap b{color:var(--y)}
.plabel{text-align:center;font-size:3.2mm;font-weight:800;color:var(--mut);margin-top:3mm}
/* ---- pricing ---- */
.tiers{display:grid;grid-template-columns:1fr 1.12fr 1fr;gap:5mm;align-items:stretch}
.tier{border:.4mm solid #E2E2E8;border-radius:4mm;padding:7mm 5.5mm;display:flex;flex-direction:column;background:#fff}
.tier.hot{background:var(--ink);color:#F7F7F2;border-color:var(--ink);box-shadow:0 5mm 12mm rgba(0,0,0,.18)}
.tier .nm{font-weight:900;font-size:5.6mm}
.tier .who{font-size:3.2mm;color:var(--mut);margin:1.5mm 0 4mm;min-height:8mm;line-height:1.5}
.tier.hot .who{color:#9A9AA8}
.tier .pr{font-weight:900;font-size:10mm;line-height:1;color:var(--r)}
.tier.hot .pr{color:var(--y)}
.tier .cur{font-size:3.2mm;font-weight:800;color:var(--mut)}
.tier.hot .cur{color:#9A9AA8}
.tier ul{list-style:none;margin-top:5mm;flex:1}
.tier li{font-size:3.4mm;line-height:1.55;padding:1.6mm 0;border-top:.25mm solid #EFEFF3;display:flex;gap:2mm}
.tier.hot li{border-color:rgba(255,255,255,.10)}
.tier li:first-child{border:0}
.tier li::before{content:"✓";color:var(--y);font-weight:900;flex:0 0 auto}
.pop-tag{position:absolute;top:-3.2mm;left:50%;transform:translateX(-50%);background:var(--y);color:#0A0A10;
  font-weight:900;font-size:2.9mm;padding:1.1mm 3.5mm;border-radius:99px;white-space:nowrap}
.faq{border-top:.3mm solid #E8E8EE;padding:4.5mm 0}
.faq b{display:block;font-size:4.1mm;font-weight:800;margin-bottom:1.5mm}
.faq p{font-size:3.6mm;color:#55555f;line-height:1.6}
.ftr{position:absolute;bottom:9mm;right:16mm;left:16mm;display:flex;justify-content:space-between;
  align-items:center;font-size:2.9mm;color:#A0A0AC;border-top:.25mm solid #EAEAEF;padding-top:3.5mm}
.dark .ftr{color:#6B6B78;border-color:rgba(255,255,255,.10)}
"""

    def mark(size="7mm", dark=False):
        col = "#F7F7F2" if dark else "#0A0A10"
        return (f'<span class="mark" style="font-size:{size};color:{col}">'
                f'<span class="l1">PHOT<span style="position:relative">O'
                f'<i class="dash" style="left:.02em"></i></span></span>'
                f'<span>NECT</span></span>')

    def badge():
        return f'<span class="badge">{mark("3.4mm")}</span>'

    def footer(n, dark=False):
        return (f'<div class="ftr"><span>{c["brand"]["footer"]}</span>'
                f'<span>{n}</span></div>')

    P = []

    # 1 — COVER
    P.append(page(f"""
      <div class="glow"></div><div class="glow2"></div>
      <div class="pad" style="height:100%;display:flex;flex-direction:column;justify-content:space-between;position:relative">
        <div class="markwrap">{badge()}
          <div><div style="font-weight:900;font-size:4.6mm;letter-spacing:.14em">PHOTONECT</div>
          <div style="font-size:3.1mm;color:#8A8A98;margin-top:.8mm">{c["brand"]["tag_en"]}</div></div>
        </div>
        <div>
          <div class="eyebrow">{c["cover"]["eyebrow"]}</div>
          <h1 style="font-size:14.5mm;margin-top:5mm;color:#fff">{c["cover"]["h1"]}</h1>
          <div class="rule" style="width:30mm;margin-top:7mm"></div>
          <p style="font-size:5mm;max-width:150mm;margin-top:5mm;color:#C9C9D4">{c["cover"]["sub"]}</p>
        </div>
        <div class="stat3">
          {"".join(f'<div><div class="n">{s[0]}</div><div class="k">{s[1]}</div></div>' for s in c["cover"]["stats"])}
        </div>
      </div>""", "dark cover"))

    # 2 — PROBLEM
    P.append(page(f"""
      <div class="pad">
        <div class="eyebrow">{c["problem"]["eyebrow"]}</div>
        <h2 style="margin-top:4mm;max-width:150mm">{c["problem"]["h2"]}</h2>
        <div class="rule"></div>
        <p style="max-width:155mm;margin-bottom:9mm">{c["problem"]["lead"]}</p>
        <div class="grid2">
          {"".join(f'<div class="card"><div class="num">{i+1:02d}</div><h3 style="margin:3mm 0 2mm">{b[0]}</h3><p style="font-size:3.7mm">{b[1]}</p></div>' for i, b in enumerate(c["problem"]["pains"]))}
        </div>
        <div class="card k" style="margin-top:9mm">
          <h3 style="color:var(--y);margin-bottom:3mm">{c["problem"]["shift_h"]}</h3>
          <p style="font-size:4mm">{c["problem"]["shift_p"]}</p>
        </div>
      </div>{footer("2")}"""))

    # 3 — THE OFFER
    P.append(page(f"""
      <div class="pad">
        <div class="eyebrow">{c["offer"]["eyebrow"]}</div>
        <h2 style="margin-top:4mm;max-width:155mm">{c["offer"]["h2"]}</h2>
        <div class="rule"></div>
        <p style="max-width:158mm;margin-bottom:8mm">{c["offer"]["lead"]}</p>
        <h3 style="margin-bottom:5mm">{c["offer"]["inside_h"]}</h3>
        {"".join(f'<div class="tick"><span class="d">✓</span><p><b>{t[0]}</b> — {t[1]}</p></div>' for t in c["offer"]["inside"])}
        <div class="card" style="margin-top:7mm;border-right:1.4mm solid var(--r)">
          <p style="font-size:4mm"><b>{c["offer"]["note_h"]}</b> {c["offer"]["note_p"]}</p>
        </div>
      </div>{footer("3")}"""))

    # 4 — SEE IT (mockups)
    ph = []
    for key, img in [("restaurant", "sample_restaurant"), ("clinic", "sample_clinic"), ("realestate", "sample_realestate")]:
        s = c["samples"][key]
        ph.append(f"""<div><div class="phone">
          <img src="data:image/jpeg;base64,{IMG[img]}"/>
          <div class="chip"><i></i><b>PHOTONECT</b></div>
          <div class="hd">{s["hd"]}</div>
          <div class="pop"><span>{s["pop"]}</span></div>
          <div class="cap"><span>{s["cap_pre"]} <b>{s["cap_hi"]}</b> {s["cap_post"]}</span></div>
        </div><div class="plabel">{s["label"]}</div></div>""")
    P.append(page(f"""
      <div class="pad">
        <div class="eyebrow">{c["samples"]["eyebrow"]}</div>
        <h2 style="margin-top:4mm;max-width:150mm">{c["samples"]["h2"]}</h2>
        <div class="rule"></div>
        <p style="max-width:158mm;margin-bottom:9mm">{c["samples"]["lead"]}</p>
        <div class="phones">{"".join(ph)}</div>
        <div class="grid2" style="margin-top:10mm">
          {"".join(f'<div class="card"><h3 style="font-size:4.4mm;margin-bottom:2mm">{f[0]}</h3><p style="font-size:3.6mm">{f[1]}</p></div>' for f in c["samples"]["feats"])}
        </div>
      </div>{footer("4")}"""))

    # 5 — HOW IT WORKS
    P.append(page(f"""
      <div class="pad">
        <div class="eyebrow">{c["how"]["eyebrow"]}</div>
        <h2 style="margin-top:4mm;max-width:150mm">{c["how"]["h2"]}</h2>
        <div class="rule"></div>
        <p style="max-width:158mm;margin-bottom:10mm">{c["how"]["lead"]}</p>
        {"".join(f'''<div style="display:flex;gap:6mm;margin-bottom:8mm;align-items:flex-start">
          <div style="flex:0 0 auto;width:16mm;height:16mm;border-radius:99px;background:var(--ink);color:var(--y);
            display:flex;align-items:center;justify-content:center;font-weight:900;font-size:7mm">{i+1}</div>
          <div style="padding-top:1mm"><h3 style="margin-bottom:2mm">{s[0]}</h3><p style="font-size:3.9mm;max-width:140mm">{s[1]}</p></div>
        </div>''' for i, s in enumerate(c["how"]["steps"]))}
        <div class="card k" style="margin-top:4mm;display:flex;justify-content:space-between;align-items:center">
          <div><h3 style="color:var(--y)">{c["how"]["speed_h"]}</h3><p style="font-size:3.7mm;margin-top:1.5mm">{c["how"]["speed_p"]}</p></div>
        </div>
        <div class="grid2" style="margin-top:8mm">
          {"".join(f'<div class="card"><h3 style="font-size:4.3mm;margin-bottom:2mm">{r[0]}</h3><p style="font-size:3.6mm">{r[1]}</p></div>' for r in c["how"]["rhythm"])}
        </div>
      </div>{footer("5")}"""))

    # 6 — PROOF
    P.append(page(f"""
      <div class="pad">
        <div class="eyebrow" style="color:var(--y)">{c["proof"]["eyebrow"]}</div>
        <h2 style="margin-top:4mm;max-width:150mm;color:#fff">{c["proof"]["h2"]}</h2>
        <div class="rule"></div>
        <p style="max-width:158mm;margin-bottom:10mm">{c["proof"]["lead"]}</p>
        <div class="grid2" style="gap:6mm">
          {"".join(f'''<div style="background:#14141C;border-radius:4mm;padding:6.5mm">
            <div style="font-weight:900;font-size:11mm;color:var(--y);line-height:1">{p[0]}</div>
            <div style="font-size:3.6mm;color:#C9C9D4;margin-top:2.5mm;line-height:1.55">{p[1]}</div></div>''' for p in c["proof"]["points"])}
        </div>
        <div style="margin-top:9mm;border-right:1.4mm solid var(--y);padding-right:6mm">
          <p style="font-size:4.4mm;color:#E8E8EE;line-height:1.7">{c["proof"]["quote"]}</p>
        </div>
        <div style="margin-top:11mm">
          <div style="font-size:3.2mm;color:#8A8A98;margin-bottom:4mm;font-weight:800;letter-spacing:.14em">{c["proof"]["pipe_h"]}</div>
          <div style="display:flex;gap:2mm;flex-wrap:wrap">
            {"".join(f'<span style="background:#191922;border:.25mm solid rgba(255,255,255,.10);border-radius:99px;padding:2.2mm 4.5mm;font-size:3.3mm;font-weight:700;color:#D8D8E2">{x}</span>' for x in c["proof"]["pipe"])}
          </div>
        </div>
      </div>{footer("6", True)}""", "dark"))

    # 7 — PRICING
    tiers_html = []
    for t in c["pricing"]["tiers"]:
        hot = t.get("hot")
        tiers_html.append(f"""<div class="tier{' hot' if hot else ''}" style="position:relative">
          {'<span class="pop-tag">'+c["pricing"]["popular"]+'</span>' if hot else ''}
          <div class="nm">{t["name"]}</div>
          <div class="who">{t["who"]}</div>
          <div class="pr">{t["price"]}<span class="cur"> {c["pricing"]["cur"]}</span></div>
          <div class="cur" style="margin-top:1.5mm">{t["per"]}</div>
          <ul>{"".join(f"<li><span>{f}</span></li>" for f in t["feats"])}</ul>
        </div>""")
    P.append(page(f"""
      <div class="pad">
        <div class="eyebrow">{c["pricing"]["eyebrow"]}</div>
        <h2 style="margin-top:4mm">{c["pricing"]["h2"]}</h2>
        <div class="rule"></div>
        <p style="max-width:158mm;margin-bottom:9mm">{c["pricing"]["lead"]}</p>
        <div class="tiers">{"".join(tiers_html)}</div>
        <div class="card" style="margin-top:8mm;border-right:1.4mm solid var(--y)">
          <h3 style="margin-bottom:2mm">{c["pricing"]["pilot_h"]}</h3>
          <p style="font-size:3.9mm">{c["pricing"]["pilot_p"]}</p>
        </div>
        <p class="mut" style="margin-top:5mm">{c["pricing"]["fine"]}</p>
      </div>{footer("7")}"""))

    # 8 — FAQ
    P.append(page(f"""
      <div class="pad">
        <div class="eyebrow">{c["faq"]["eyebrow"]}</div>
        <h2 style="margin-top:4mm">{c["faq"]["h2"]}</h2>
        <div class="rule"></div>
        <div style="margin-top:6mm">
          {"".join(f'<div class="faq"><b>{q[0]}</b><p>{q[1]}</p></div>' for q in c["faq"]["items"])}
        </div>
        <div class="card k" style="margin-top:9mm">
          <h3 style="margin-bottom:2mm">{c["faq"]["more_h"]}</h3>
          <p style="font-size:3.9mm">{c["faq"]["more_p"]}</p>
        </div>
      </div>{footer("8")}"""))

    # 9 — CTA
    P.append(page(f"""
      <div class="glow"></div><div class="glow2"></div>
      <div class="pad" style="height:100%;display:flex;flex-direction:column;justify-content:center;position:relative">
        <div class="eyebrow">{c["cta"]["eyebrow"]}</div>
        <h1 style="font-size:13mm;margin-top:5mm;color:#fff;max-width:165mm">{c["cta"]["h1"]}</h1>
        <div class="rule" style="width:30mm;margin-top:6mm"></div>
        <p style="font-size:4.6mm;max-width:150mm;margin-top:5mm;color:#C9C9D4">{c["cta"]["sub"]}</p>
        <div style="margin-top:10mm;display:flex;gap:5mm">
          {"".join(f'''<div style="background:#14141C;border-radius:3.5mm;padding:5.5mm 7mm">
            <div style="font-size:3mm;color:#8A8A98;margin-bottom:1.5mm">{k}</div>
            <div style="font-weight:900;font-size:4.6mm;color:var(--y);direction:ltr;text-align:right">{v}</div></div>''' for k, v in c["cta"]["contacts"])}
        </div>
        <div style="margin-top:14mm;display:flex;align-items:center;gap:5mm">
          {badge()}<div><div style="font-weight:900;font-size:4.4mm;letter-spacing:.14em;color:#fff">PHOTONECT</div>
          <div style="font-size:3mm;color:#8A8A98;margin-top:.8mm">{c["brand"]["tag_en"]}</div></div>
        </div>
      </div>""", "dark cover"))

    return f"""<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8">
<title>{c["brand"]["doctitle"]}</title><style>{FONT}{css}</style></head><body>{"".join(P)}</body></html>"""


if __name__ == "__main__":
    OUT_HTML.write_text(build(), encoding="utf-8")
    print(f"html: {OUT_HTML.stat().st_size//1024} KB")
    out_pdf = sys.argv[1] if len(sys.argv) > 1 else str(A / "proposal.pdf")
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={out_pdf}", "--virtual-time-budget=12000",
                    f"file://{OUT_HTML}"], check=True, capture_output=True)
    print(f"pdf:  {pathlib.Path(out_pdf).stat().st_size//1024} KB → {out_pdf}")
