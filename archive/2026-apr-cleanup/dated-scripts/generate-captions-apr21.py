#!/usr/bin/env python3
"""
generate-captions-apr21.py — generate ready-to-paste Arabic IG captions for
all 12 April 21 slugs based on their props.json.

Unlike the generic template, these are hand-shaped to match each slug's story arc
(the V4 labels are already story-specific, so the captions mirror them). Every
caption has:
  1. A hook line that quotes the Arabic headline
  2. Three pillars — one per beat — using the story-specific labels as anchors
  3. A "ماذا بعد" scenario prompt at the bottom for engagement
  4. Source list (up to 6 domains)
  5. Bilingual hashtags per topic bucket

Writes: data/posts/<slug>/caption.txt

Usage: python3 data/_template/generate-captions-apr21.py
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent  # NEWS CODE/
POSTS = ROOT / "data" / "posts"

# Story-tuned hook emojis + hashtag sets per bucket
BUCKET_META = {
    "iraq_domestic": {
        "emoji": "🇮🇶",
        "hashtags_ar": "#العراق #بغداد #سياسة_عراقية",
        "hashtags_en": "#Iraq #Baghdad #IraqiPolitics",
    },
    "mena_geopolitics": {
        "emoji": "🟥",
        "hashtags_ar": "#لبنان #الشرق_الأوسط #غزة #أخبار_عاجلة",
        "hashtags_en": "#Lebanon #MiddleEast #MENA #BreakingNews",
    },
    "gulf_regional": {
        "emoji": "🟨",
        "hashtags_ar": "#الخليج #السعودية #مصر #أوبك",
        "hashtags_en": "#Gulf #SaudiArabia #Egypt #OPEC",
    },
    "global_economy": {
        "emoji": "📉",
        "hashtags_ar": "#الاقتصاد_العالمي #النفط #الأسواق #أزمة",
        "hashtags_en": "#GlobalEconomy #Markets #OilPrice #Brent",
    },
    "tech_ai": {
        "emoji": "🧠",
        "hashtags_ar": "#الذكاء_الاصطناعي #تكنولوجيا #عملات_رقمية",
        "hashtags_en": "#AI #Tech #Crypto #Blockchain",
    },
    "europe": {
        "emoji": "🇪🇺",
        "hashtags_ar": "#أوروبا #ألمانيا #أزمة_الغاز",
        "hashtags_en": "#Europe #Germany #GasCrisis",
    },
    "wildcard": {
        "emoji": "🌐",
        "hashtags_ar": "#كوريا_الشمالية #البحر_الأحمر #تهريب_أسلحة",
        "hashtags_en": "#NorthKorea #RedSea #GeoIntel",
    },
}

# Per-slug scenario prompt (the "what's next" engagement hook)
SCENARIO = {
    "iraq-vote": "هل تسقط الحكومة الليلة أم تنجو بشق الأنفس؟",
    "brent-150": "هل نشهد ١٧٥ دولاراً قبل نهاية الشهر؟",
    "ceasefire-break": "كم يوماً تصمد الأمم المتحدة قبل موجة نزوح جديدة؟",
    "ai-nuclear-sim": "هل يجب إيقاف تطوير النماذج الكبرى فوراً؟",
    "berlin-protest": "هل يستقيل المستشار خلال ٤٨ ساعة؟",
    "un-secgen-plan": "هل يصبح الفيتو الروسي اختبار شرعية جديد للأمم المتحدة؟",
    "crypto-tether-depeg": "هل هذه نهاية العملات المستقرة المركزية؟",
    "opec-emergency-2": "هل يكسر الرياض-موسكو تحالف السنوات الخمس؟",
    "kdp-split": "هل يكون هذا الانشقاق نهاية إقليم كردستان كما نعرفه؟",
    "imf-sa-loan": "هل تُعيد هذه الأزمة رسم خريطة النفط العالمية؟",
    "egypt-mobilize": "هل نحن على أعتاب حرب إقليمية أم ضغط دبلوماسي؟",
    "north-korea-ship": "ما حجم شبكة التهريب الكورية الشمالية في المنطقة؟",
}


def fmt_caption(slug: str, props: dict) -> str:
    bucket = props["topicBucket"]
    meta = BUCKET_META.get(bucket, BUCKET_META["wildcard"])
    headline = props["breaking"]["arabicHeadline"]
    beats = props["beats"]

    sources = [s["domain"] for s in props.get("sources", [])][:6]
    if len(sources) < 6:
        sources = sources + [""] * (6 - len(sources))

    # Build 3 pillar lines from the beats' story labels + headings
    pillars = []
    for b in beats:
        label = b.get("label", "")
        heading = b.get("arabicHeading", "")
        if label and heading:
            pillars.append(f"▸ {label}: {heading}")
        elif heading:
            pillars.append(f"▸ {heading}")

    lines = [
        f"{meta['emoji']}  {headline}",
        "",
    ]
    lines.extend(pillars)
    lines.append("")
    lines.append(f"🔻 {SCENARIO.get(slug, 'ماذا بعد؟')}")
    lines.append("")
    lines.append(f"📍 المصادر: {' • '.join(s for s in sources if s)}")
    lines.append("━━━")
    lines.append("@photonect.news | أخبار العالم يومياً — بالعربية")
    lines.append("")
    lines.append(f"{meta['hashtags_ar']} #photonectnews")
    lines.append(f"{meta['hashtags_en']} #BreakingNews")
    return "\n".join(lines)


def main() -> None:
    slugs = sorted(p.name for p in POSTS.iterdir()
                   if p.is_dir() and p.name.startswith("2026-04-21-"))
    print(f"Processing {len(slugs)} April 21 slugs...")
    for full_slug in slugs:
        short = full_slug.replace("2026-04-21-", "")
        props_path = POSTS / full_slug / "props.json"
        cap_path = POSTS / full_slug / "caption.txt"
        if not props_path.exists():
            print(f"  ✗ {short}: no props.json")
            continue
        props = json.loads(props_path.read_text(encoding="utf-8"))
        caption = fmt_caption(short, props)
        cap_path.write_text(caption, encoding="utf-8")
        print(f"  ✓ {short}: {len(caption)} chars → caption.txt")


if __name__ == "__main__":
    main()
