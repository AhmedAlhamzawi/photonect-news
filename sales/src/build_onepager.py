#!/usr/bin/env python3
"""1-page WhatsApp teaser — the doc that actually gets opened on a phone.
Research: Iraqi SMEs buy in-chat; long PDFs get ignored. Send this first,
full proposal on request."""
import pathlib, subprocess, sys
from copy_ar import COPY as c
A = pathlib.Path("/tmp/proposal_assets")
FONT = (A/"tajawal_embed.css").read_text()
IMG = {n:(A/f"{n}.b64").read_text() for n in ["sample_restaurant","sample_clinic","sample_realestate"]}
css = """
*{margin:0;padding:0;box-sizing:border-box;-webkit-print-color-adjust:exact;print-color-adjust:exact}
@page{size:A4;margin:0}
html{font-family:'Tajawal',sans-serif}
body{direction:rtl}
:root{--y:#FFC217;--r:#D72638;--ink:#0A0A10}
.p{width:210mm;height:297mm;position:relative;overflow:hidden;
   background:radial-gradient(120% 80% at 80% 6%,#23232c 0%,#0A0A10 60%);color:#F7F7F2;padding:14mm 13mm}
.glow{position:absolute;width:110mm;height:110mm;border-radius:99px;top:-38mm;left:-26mm;
  background:radial-gradient(circle,rgba(255,194,23,.17),transparent 68%)}
.mark{display:inline-flex;flex-direction:column;align-items:center;line-height:.84;font-weight:900}
.badge{width:14mm;height:14mm;border-radius:99px;background:#fff;display:flex;align-items:center;justify-content:center}
.badge .mark{font-size:3.2mm;color:#0A0A10}
.dash{position:absolute;left:.04em;top:-.17em;width:.30em;height:.075em;background:var(--r);border-radius:99px}
h1{font-weight:900;font-size:13mm;line-height:1.2;letter-spacing:-.01em}
.sub{font-size:4.3mm;color:#C9C9D4;line-height:1.7;margin-top:4mm;max-width:165mm}
.eyebrow{font-weight:800;font-size:3.1mm;letter-spacing:.2em;color:var(--y)}
.ph{display:flex;gap:4mm;margin-top:8mm;justify-content:center}
.card{width:40mm;border-radius:3.5mm;overflow:hidden;position:relative;box-shadow:0 4mm 10mm rgba(0,0,0,.4)}
.card img{width:100%;height:58mm;object-fit:cover;display:block}
.card .t{position:absolute;top:6mm;right:2.5mm;left:2.5mm;text-align:center;font-weight:900;font-size:3.4mm;
  color:#fff;text-shadow:0 1mm 2.5mm rgba(0,0,0,.95);line-height:1.3}
.card .lab{position:absolute;bottom:2mm;right:2mm;left:2mm;text-align:center;font-size:2.6mm;font-weight:800;
  color:#0A0A10;background:var(--y);border-radius:1.4mm;padding:.9mm}
.tiers{display:grid;grid-template-columns:1fr 1.1fr 1fr;gap:3.5mm;margin-top:9mm}
.t{background:#15151E;border:.3mm solid rgba(255,255,255,.10);border-radius:3.5mm;padding:5mm 4mm;text-align:center}
.t.hot{background:#fff;color:#0A0A10;border-color:var(--y)}
.t .n{font-weight:900;font-size:4.4mm}
.t .pr{font-weight:900;font-size:8.5mm;color:var(--y);line-height:1;margin:2.5mm 0 1mm}
.t.hot .pr{color:var(--r)}
.t .u{font-size:2.9mm;color:#9A9AA8}
.t.hot .u{color:#55555f}
.t .v{font-size:3.2mm;font-weight:700;margin-top:2mm}
.bar{display:flex;gap:3mm;margin-top:8mm}
.bar div{flex:1;background:#15151E;border-radius:3mm;padding:4mm;text-align:center}
.bar b{display:block;font-weight:900;font-size:6mm;color:var(--y)}
.bar span{font-size:2.8mm;color:#9A9AA8}
.cta{margin-top:9mm;background:var(--y);color:#0A0A10;border-radius:3.5mm;padding:6mm;text-align:center}
.cta b{font-weight:900;font-size:5.4mm;display:block}
.cta p{font-size:3.6mm;margin-top:2mm;font-weight:500}
.ct{display:flex;gap:3mm;justify-content:center;margin-top:5mm;font-size:3.2mm;font-weight:800}
.ct span{background:#15151E;border-radius:2.5mm;padding:2.5mm 5mm;color:var(--y);direction:ltr}
"""
def mk(sz,col):
    return (f'<span class="mark" style="font-size:{sz};color:{col}">'
            f'<span style="position:relative">PHOT<span style="position:relative">O'
            f'<i class="dash"></i></span></span><span>NECT</span></span>')
ph=""
for k,i in [("restaurant","sample_restaurant"),("clinic","sample_clinic"),("realestate","sample_realestate")]:
    s=c["samples"][k]
    ph+=f'<div class="card"><img src="data:image/jpeg;base64,{IMG[i]}"/><div class="t">{s["hd"]}</div><div class="lab">{s["label"]}</div></div>'
tiers=""
for t in c["pricing"]["tiers"]:
    hot=" hot" if t.get("hot") else ""
    v=t["per"].split("·")[0].strip()
    tiers+=f'<div class="t{hot}"><div class="n">{t["name"]}</div><div class="pr">{t["price"]}</div><div class="u">د.ع شهرياً</div><div class="v">{v}</div></div>'
html=f"""<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><title>فوتونكت — عرض مختصر</title>
<style>{FONT}{css}</style></head><body><div class="p"><div class="glow"></div>
<div style="display:flex;align-items:center;gap:4mm;justify-content:flex-end">
  <div style="text-align:left"><div style="font-weight:900;font-size:4mm;letter-spacing:.14em">PHOTONECT</div>
  <div style="font-size:2.8mm;color:#8A8A98">Where Light Meets Logic</div></div><span class="badge">{mk("3.2mm","#0A0A10")}</span></div>
<div style="margin-top:11mm"><div class="eyebrow">باقات إنتاج الفيديو · بغداد</div>
<h1 style="margin-top:4mm">فيديوهات احترافية لعملك<br>بدون كاميرا ولا تصوير</h1>
<p class="sub">ترسل لنا فكرة وشعارك — نرجّع لك فيديو جاهز للنشر على إنستغرام وتيك توك، خلال 48 ساعة.</p></div>
<div class="ph">{ph}</div>
<div class="tiers">{tiers}</div>
<div class="bar"><div><b>+260</b><span>فيديو من إنتاجنا</span></div>
<div><b>3</b><span>منصات نشر</span></div><div><b>48</b><span>ساعة لأول فيديو</span></div></div>
<div class="cta"><b>جرّبها بفيديو واحد — 35,000 د.ع</b>
<p>فيديو كامل بنفس مواصفات الباقات. إذا أعجبك، تُحتسب قيمته من أول اشتراك.</p></div>
<div class="ct"><span>+964 ___ ___ ____</span><span>ahmed@photonect.net</span></div>
</div></body></html>"""
(A/"onepager.html").write_text(html,encoding="utf-8")
out=sys.argv[1] if len(sys.argv)>1 else str(A/"onepager.pdf")
subprocess.run(["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome","--headless","--disable-gpu",
  "--no-pdf-header-footer",f"--print-to-pdf={out}","--virtual-time-budget=10000",f"file://{A}/onepager.html"],
  check=True,capture_output=True)
print("onepager:",pathlib.Path(out).stat().st_size//1024,"KB")
