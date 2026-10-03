#!/usr/bin/env python3
"""2026-10-03 Opus gate pass 2: 0 blockers; warnings applied (dual verb + pop, Zaidi attribution, d/e labels)."""
from pathlib import Path
P = Path(__file__).resolve().parents[1] / "data/posts"
B, PR = ".meta/v11-brief.json", ".meta/props.json"
for slug, f, old, new in [
 ("b-dollar-157300-flat", B, "ثم أغلقت السبت على", "ثم أغلقتا السبت على"),
 ("b-dollar-157300-flat", B, '"matchWord": "أغلقت"', '"matchWord": "أغلقتا"'),
 ("c-ceyhan-basra-pipeline", B, "وذكر بيرقدار هدف توريد مليون برميل.", "وذكر بيرقدار هدفاً أشار إليه الزيدي بتوريد مليون برميل."),
 ("d-moi-september-308", PR, "متهماً خلال أيلول", "متهمين خلال أيلول"),
 ("d-moi-september-308", PR, "إلى جانب 55 متهماً بقضايا مخدرات", "فيما بلغ عدد المتهمين بقضايا المخدرات 55"),
 ("e-kirkuk-water-150-cases", PR, '"arabicLabel": "حالة خلال يومين', '"arabicLabel": "+ حالة خلال يومين'),
]:
    p = P / f"2026-10-03-{slug}" / f; t = p.read_text()
    print("OK " if old in t else "MISS", slug, old[:30]); p.write_text(t.replace(old, new, 1))
