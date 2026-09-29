#!/usr/bin/env python3
"""Apply Opus editorial-gate pass-2 warnings to the 2026-09-29 slate. Every replacement must hit exactly once."""
import sys
from pathlib import Path
P = Path(__file__).resolve().parents[1] / "data" / "posts"
D = "2026-09-29"
FIX = [
 ("a-mp-farman-28-billion", ".meta/v11-brief.json", "ليتجاوز المجموع ثمانية وعشرين مليار دينار", "ليتجاوز المجموع ثمانيةً وعشرين ملياراً من الدنانير"),
 ("a-mp-farman-28-billion", "caption.txt", "في العراق بالكسب غير المشروع..", "في العراق بجريمة الكسب غير المشروع.."),
 ("b-dollar-157000-gold-up", ".meta/v11-brief.json", "إذ سجّل مثقال عيار واحد وعشرين الخليجي في جملة شارع النهر", "إذ سجّل مثقال الذهب الخليجي عيار واحد وعشرين في جملة شارع النهر"),
 ("c-zaidi-trump-oil-firms", ".meta/props.json", "جهة مرتبطة بالطيران الإيراني (الخزانة الأميركية)", "جهة طيران إيرانية عاقبتها الخزانة الأميركية في 8 أيلول"),
 ("c-zaidi-trump-oil-firms", ".meta/props.json", "والفساد والسلاح على الطاولة", "وعرض ملفي الفساد والسلاح"),
 ("d-customs-transfers-1-october", ".meta/v11-brief.json", "إيرادات الكمارك المسجلة بلغت ثلاثة تريليونات ومئة وخمسين مليار دينار.", "إيرادات الكمارك المسجلة حتى الأحد بلغت ثلاثة تريليونات ومئة وخمسين ملياراً من الدنانير."),
 ("d-customs-transfers-1-october", "caption.txt", "الرسوم تُدفع قبل الحوالة من الخميس", "الرسوم قبل الحوالة من أول تشرين الأول"),
 ("e-kurdistan-seats-1250", ".meta/v11-brief.json", "وبحث الاجتماع الموسّع أيضاً", "وبحث اجتماع موسّع للجانبين أيضاً"),
]
miss = 0
for slug, f, a, b in FIX:
    p = P / f"{D}-{slug}" / f; s = p.read_text(encoding="utf-8")
    if s.count(a) != 1: print(f"MISS/{s.count(a)}x {slug}/{f}: {a[:50]}"); miss += 1; continue
    p.write_text(s.replace(a, b), encoding="utf-8")
print("misses:", miss); sys.exit(1 if miss else 0)
