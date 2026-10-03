#!/usr/bin/env python3
"""2026-10-03: copywriter turned c and d endQuestions into opinion/prediction questions — the
END-QUESTION mandate requires personal, one-word-answerable questions. Swap on every surface."""
from pathlib import Path
P = Path(__file__).resolve().parents[1] / "data/posts"
for slug, old, new in [
 ("c-ceyhan-basra-pipeline", "لو امتد الخط للبصرة، تؤيد تصدير نفطها عبر تركيا؟", "سمعت بخط كركوك جيهان قبل؟"),
 ("d-moi-september-308", "تتوقع حصيلة تشرين الأول تتجاوز 308 متهمين؟", "سمعت بفرقة الرد السريع قبل؟"),
]:
    for f in (".meta/props.json", ".meta/v11-brief.json", "caption.txt"):
        p = P / f"2026-10-03-{slug}" / f
        if not p.exists(): continue
        t = p.read_text(); n = t.count(old)
        print(slug, f, n); p.write_text(t.replace(old, new))
