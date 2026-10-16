#!/usr/bin/env python3
"""Apply Opus QA gate pass 2 (2026-10-16) text fixes. Image fixes (d hero, d broll_2) are in place_images_2026_10_16.py."""
from pathlib import Path
P = Path(__file__).resolve().parents[1] / "data" / "posts"
D = "2026-10-16"
def sub(rel, old, new):
    f = P / f"{D}-{rel}"; s = f.read_text(encoding="utf-8")
    assert old in s, f"{rel}: not found: {old[:50]}"; f.write_text(s.replace(old, new), encoding="utf-8")
sub("a-passport-101k-reversed/.meta/v11-brief.json", "دينار — بعد تراجع الداخلية", "دينار — بحسب توجيه الداخلية")
sub("c-us-sanctions-iraqi-bank/.meta/props.json", "وكل كيان مملوك 50% فأكثر", "وكل كيان يملك المُدرَجون 50% منه فأكثر")
sub("c-us-sanctions-iraqi-bank/.meta/props.json", "والمصارف الأجنبية المتعاملة معه قد تواجه عقوبات ثانوية.", "والمصارف الأجنبية التي تُجري معاملات معيّنة معه قد تواجه عقوبات ثانوية.")
sub("e-rain-north-40-south/.meta/v11-brief.json", "ويرجّح الراصد صادق عطية برقاً ورعداً في", "ويرجّح الراصد صادق عطية أمطاراً مع برق ورعد في")
print("gate 2 applied")
sub("e-rain-north-40-south/.meta/v11-brief.json", "بحسب الهيئة العامة للأنواء الجوية، تشهد المنطقتان الوسطى والشمالية الجمعة أجواء غائمة مع مطر خفيف إلى معتدل ورعد متفرق،",
    "توقعت الهيئة العامة للأنواء الجوية للجمعة أجواء غائمة في المنطقتين الوسطى والشمالية مع مطر خفيف إلى معتدل ورعد متفرق،")
