#!/usr/bin/env python3
"""2026-10-03 Opus gate pass 1: 0 blockers; all warnings applied (attribution + neutral wording)."""
from pathlib import Path
P = Path(__file__).resolve().parents[1] / "data/posts"
B, PR, C = ".meta/v11-brief.json", ".meta/props.json", "caption.txt"
for slug, files, old, new in [
 ("b-dollar-157300-flat", (B,), "أما في إيران، فبلغ سعر الدولار نحو", "أما في إيران، فبلغ سعر بيع الدولار بحسب بيانات السوق الإيرانية نحو"),
 ("b-dollar-157300-flat", (B,), "المصادر: شفق نيوز — 3 تشرين الأول 2026", "المصادر: شفق نيوز — 1 و3 تشرين الأول 2026"),
 ("c-ceyhan-basra-pipeline", (B,), "يبلغ طول الخط نحو", "وبحسب الترا عراق، يبلغ طول الخط نحو"),
 ("c-ceyhan-basra-pipeline", (B,), "فيما لم يذكر بيان الوزارة العراقية البصرة", "فيما لم يرد ذكر البصرة في بيان الوزارة العراقية كما نشرته شفق نيوز"),
 ("c-ceyhan-basra-pipeline", (C,), "وبيان وزارة النفط العراقية لم يذكر البصرة", "والبصرة لم ترد في بيان وزارة النفط العراقية المنشور"),
 ("c-ceyhan-basra-pipeline", (B,), "نفط البصرة يطلع من تركيا؟", "تركيا تقترح: خط جيهان للبصرة"),
 ("d-moi-september-308", (PR,), "وضبطت قطعات الفرقة", "وبحسب البيان، ضبطت قطعات الفرقة"),
 ("e-kirkuk-water-150-cases", (PR,), "ضجّ مركز صحي الرياض بالمراجعين.", "ارتفعت أعداد المراجعين في مركز صحي الرياض."),
 ("e-kirkuk-water-150-cases", (PR,), "حسين يقولها صراحة:", "قال حسين إن"),
 ("e-kirkuk-water-150-cases", (PR,), "ويطالب بتعزيز", "مؤكداً أن ذلك يتطلب تعزيز"),
]:
    for f in files:
        p = P / f"2026-10-03-{slug}" / f; t = p.read_text()
        print("OK " if old in t else "MISS", slug, f, old[:30]); p.write_text(t.replace(old, new))
