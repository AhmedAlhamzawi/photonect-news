#!/usr/bin/env python3
"""Apply Opus gate pass-1/2 findings (2026-09-30): 3 blockers (b computed gap airing, c 2nd caption question,
e one-sided dispute pairing) + warnings. Exact-string replacements; asserts each target exists."""
from pathlib import Path
P = Path(__file__).resolve().parents[1] / "data/posts"
FIX = [
 ("a-gold-5kg-land-registry", [".meta/v11-brief.json"], "وبحسب الهيئة، وصل فريقها إلى الذهب بعد تدوين اعترافات زوجها المتهم، الذي نقلته شقيقتها من منزلها إلى دار شخص آخر، وضُبط بقرار من قاضي التحقيق.", "وبحسب الهيئة، نقلت شقيقة المتهمة الذهب من منزلها إلى دار شخص آخر، ووصل إليه الفريق بعد اعترافات زوجها المتهم، وضبطه بقرار قاضي التحقيق."),
 ("a-gold-5kg-land-registry", ["caption.txt"], "#مكافحة_الفساد", "#التسجيل_العقاري"),
 ("b-dollar-157250-third-rise", [".meta/v11-brief.json"], "أما الذهب، فارتفع مثقال الذهب الخليجي والتركي والأوروبي", "أما الذهب، فارتفع بيع المثقال الخليجي والتركي والأوروبي"),
 ("b-dollar-157250-third-rise", ["caption.txt"], "ومثقال الذهب بشارع النهر يقفز", "ومثقال الذهب بشارع النهر يرتفع"),
 ("c-coalition-mission-ends", ["caption.txt"], "والصدر يحل «اليوم الموعود»", "والصدر يحل لواء «اليوم الموعود»"),
 ("c-coalition-mission-ends", ["caption.txt"], "والصدر حل «اليوم الموعود»", "والصدر حل لواء «اليوم الموعود»"),
 ("d-watan-275000-plots", ["caption.txt"], "وين، ", ""),
 ("e-ali-ammar-219kg", [".meta/props.json"], "بدأ العدّ تحت العلم الإيراني ثم تبدّل.", "بدأ العدّ تحت العلم الإيراني ثم استُبدل بالعراقي."),
]
bad = 0
for slug, files, old, new in FIX:
    hit = 0
    for f in files:
        p = P / f"2026-09-30-{slug}" / f
        s = p.read_text(encoding="utf-8")
        if old in s:
            p.write_text(s.replace(old, new), encoding="utf-8"); hit += 1
    print(("OK  " if hit else "MISS"), slug, old[:50]); bad += (hit == 0)
raise SystemExit(bad)
