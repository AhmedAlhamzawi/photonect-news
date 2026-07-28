#!/usr/bin/env python3
"""Author the 2026-07-28 Photonect NEWS slate.

5 slugs (Iraq/MENA money-power lens). Posting order (alphabetical = slot order):
  1 arbaeen-18-million    society           V11  A   18:00
  2 dollar-month-drop     iraq_economy      V11  B   19:45  (daily dollar anchor)
  3 energy-peace-price    iraq_economy      V10  A   21:15  <- silent control, no v11
  4 graft-oil-27-billion  iraq_politics     V11  B   22:30
  5 salaries-late-july    iraq_economy      V11  C   23:45

Directional shift vs 2026-07-27: from "what the paperwork costs you" to "what a
month of movement did to your pocket" — 1,813,188 pilgrims on an 80 km road,
100 dollars that cost 6,850 dinars less than a month ago, an oil crash caused by
a pause in the war, 27 billion dinars pulled out of hiding, and a July salary
with a 48-hour clock on it.

Banned this slate (per fact sheet): the CBI official rate and any premium/gap
framing; the Basrah Heavy/Medium price moves; the "August salaries via state-bank
borrowing" claim and any monthly salary-bill figure; the 2.1m Arbaeen figure, the
Arbaeen date and the Shalamcheh crossing; the unreconciled cumulative graft total.

Writes per slug: .meta/props.json, caption.txt, .meta/media-stamp.json, and (for
the 4 voiced) .meta/v11-brief.json. Western numerals on-screen; voText spells
numbers in words (MSA newscast). No Persian yeh/kaf (grep-guarded after run).
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "data" / "posts"
DATE = "2026-07-28"
DATE_LABEL = "JUL 28 • 2026"
AR_DATE = "28 يوليو 2026"
HANDLE = "@photonect.news"

STAMP = {
    "hunted_at": "2026-07-28T11:00:00+00:00",
    "manual": True,
    "source": "higgsfield nano-banana-pro (KIE 402 — credits exhausted)",
    "date": "2026-07-28",
    "note": (
        "KIE returned HTTP 402 on all requests for the second consecutive day; "
        "the whole slate was generated on Higgsfield's nano_banana_pro (same Nano "
        "Banana Pro model, different vendor) at 9:16/2K. Every image Read-verified "
        "by hand."
    ),
}


def img(slug, n):
    return f"images/news/{slug}/{n}"


SLUGS = {}

# ─────────────────────────────────────────────────────────────────────────
# 1 — ARBAEEN: 1,813,188 FOREIGN ARRIVALS  (society · V11 · A · LEAD)
# ─────────────────────────────────────────────────────────────────────────
s = f"{DATE}-arbaeen-18-million"
SLUGS[s] = {
    "bucket": "society",
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/mood_newsroom.mp3", "topicBucket": "society", "variant": "A",
        "breaking": {
            "arabicKicker": "زيارة · طريق",
            "arabicHeadline": "1,813,188 زائراً دخلوا… والطريق 80 كيلومتراً",
            "englishSubhead": "1,813,188 FOREIGN VISITORS FROM 172 NATIONALITIES ENTERED IRAQ SINCE 16 JUNE",
            "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
        },
        "beats": [
            {
                "label": "ماذا يحدث؟",
                "arabicHeading": "1,813,188 زائراً من 172 جنسية",
                "arabicBody": "أعلن رئيس خلية الإعلام الأمني اللواء سعد معن دخول 1,813,188 زائراً أجنبياً من 172 جنسية إلى العراق بين 16 حزيران و26 تموز 2026.",
                "bigStat": {"value": "1,813,188", "label": "Foreign visitors since 16 June",
                            "arabicLabel": "عدد الزائرين الأجانب الذين دخلوا العراق من 172 جنسية بين 16 حزيران و26 تموز 2026 (خلية الإعلام الأمني · اللواء سعد معن)"},
                "supportingStats": [
                    {"label": "الجنسيات", "value": "172"},
                    {"label": "من", "value": "16 حزيران"},
                    {"label": "إلى", "value": "26 تموز"},
                ],
                "broll": img(s, "broll_3.jpg"), "brolls": [img(s, "broll_3.jpg")],
                "brollType": "image", "accent": "#FFC217", "brollSource": "Security Media Cell · 2026",
            },
            {
                "label": "لماذا يهم؟",
                "arabicHeading": "80 كيلومتراً بين النجف وكربلاء",
                "arabicBody": "يغطي أكثر من 2,500 متطوع و60 وحدة طبية طريق النجف–كربلاء البالغ 80 كيلومتراً، بحسب خلية الإعلام الأمني.",
                "bigStat": {"value": "60", "label": "Medical units on the route",
                            "arabicLabel": "عدد الوحدات الطبية التي تغطي طريق النجف–كربلاء البالغ 80 كيلومتراً إلى جانب أكثر من 2,500 متطوع (خلية الإعلام الأمني)"},
                "supportingStats": [
                    {"label": "المتطوعون", "value": "+2,500"},
                    {"label": "الوحدات الطبية", "value": "60"},
                    {"label": "الطريق", "value": "80 كم"},
                ],
                "broll": img(s, "broll_2.jpg"), "brolls": [img(s, "broll_2.jpg")],
                "brollType": "image", "accent": "#FF6B3D", "brollSource": "Security Media Cell · 2026",
            },
            {
                "label": "ماذا بعد؟",
                "arabicHeading": "1,500,977 وافداً قبل يومين فقط",
                "arabicBody": "قبل يومين أحصت خلية الإعلام الأمني عبر وكالة الأنباء العراقية 1,500,977 وافداً منذ مطلع محرم، وأبرز الحالات الإنهاك وضربات الحر والجفاف وإصابات الأقدام.",
                "bigStat": {"value": "1,500,977", "label": "Counted two days earlier",
                            "arabicLabel": "عدد الوافدين الذي أحصته خلية الإعلام الأمني منذ مطلع محرم قبل يومين عبر وكالة الأنباء العراقية (واع)"},
                "supportingStats": [
                    {"label": "أبرز الحالات", "value": "الإنهاك"},
                    {"label": "وأيضاً", "value": "الجفاف"},
                    {"label": "وكذلك", "value": "إصابات الأقدام"},
                ],
                "broll": img(s, "broll_1.jpg"), "brolls": [img(s, "broll_1.jpg")],
                "brollType": "image", "accent": "#D72638", "brollSource": "INA · 2026",
            },
        ],
        "sources": [
            {"name": "Security Media Cell", "domain": "smc.iq"},
            {"name": "Iraqi News Agency", "domain": "ina.iq"},
            {"name": "Shafaq News", "domain": "shafaq.com"},
        ],
        "arabicTicker": [
            "خلية الإعلام الأمني: 1,813,188 زائراً أجنبياً من 172 جنسية دخلوا العراق بين 16 حزيران و26 تموز 2026 (اللواء سعد معن)",
            "قبل يومين أحصت الخلية عبر وكالة الأنباء العراقية 1,500,977 وافداً منذ مطلع محرم (واع)",
            "أكثر من 2,500 متطوع و60 وحدة طبية تغطي طريق النجف–كربلاء البالغ 80 كيلومتراً (خلية الإعلام الأمني)",
            "أبرز الحالات المعالجة: الإنهاك وضربات الحر والجفاف وإصابات الأقدام (خلية الإعلام الأمني)",
            "وحالات أخرى تتعلق بارتفاع السكر وضغط الدم (خلية الإعلام الأمني)",
            "شكد كيلومتر مشيت هالسنة؟",
        ],
    },
    "v11": {
        "kicker": "عاجل",
        "hookHeadline": "1,813,188 زائراً من 172 جنسية",
        "voText": "أعلن رئيس خلية الإعلام الأمني اللواء سعد معن دخول مليون وثمانمئة وثلاثة عشر ألفاً ومئة وثمانية وثمانين زائراً أجنبياً من مئة واثنتين وسبعين جنسية إلى العراق بين السادس عشر من حزيران والسادس والعشرين من تموز. وقبل يومين أحصت الخلية عبر وكالة الأنباء العراقية مليوناً وخمسمئة ألف وتسعمئة وسبعة وسبعين وافداً منذ مطلع محرم. وعلى طريق النجف كربلاء البالغ ثمانين كيلومتراً يعمل أكثر من ألفين وخمسمئة متطوع وستون وحدة طبية، وأبرز الحالات الإنهاك وضربات الحر والجفاف وإصابات الأقدام. فشكد كيلومتر مشيت هالسنة؟",
        "endQuestion": "شكد كيلومتر مشيت هالسنة؟",
        "sourcesLine": "المصادر: خلية الإعلام الأمني · واع · شفق نيوز",
        "statPops": [
            {"value": "1,813,188", "label": "زائراً أجنبياً", "matchWord": "وثمانين"},
            {"value": "60 وحدة طبية", "label": "على طريق 80 كم", "matchWord": "وستون"},
        ],
    },
    "caption": """زيارة الأربعين 2026 — 1,813,188 زائراً دخلوا العراق

172 جنسية على الطريق، و60 وحدة طبية تغطي 80 كيلومتراً.

شكد كيلومتر مشيت هالسنة؟

المصادر: خلية الإعلام الأمني، واع، شفق نيوز
#العراق #الأربعين #كربلاء #زيارة_الأربعين
@photonect.news
""",
}

# ─────────────────────────────────────────────────────────────────────────
# 2 — DOLLAR: A MONTH OF DECLINE  (iraq_economy · V11 · B · dollar anchor)
# ─────────────────────────────────────────────────────────────────────────
s = f"{DATE}-dollar-month-drop"
SLUGS[s] = {
    "bucket": "iraq_economy",
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/mood_newsroom.mp3", "topicBucket": "iraq_economy", "variant": "B",
        "breaking": {
            "arabicKicker": "دولار · شهر كامل",
            "arabicHeadline": "100 دولار أرخص بـ6,850 ديناراً عن الشهر الماضي",
            "englishSubhead": "$100 NOW COSTS 6,850 IQD LESS THAN A MONTH AGO IN BAGHDAD",
            "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
        },
        "beats": [
            {
                "label": "ماذا يحدث؟",
                "arabicHeading": "149,900 ديناراً لكل 100 دولار",
                "arabicBody": "سجّلت بورصتا الكفاح والحارثية في بغداد 149,900 دينار لكل 100 دولار اليوم الثلاثاء، نزولاً من 150,050 يوم الاثنين.",
                "bigStat": {"value": "149,900", "label": "IQD per $100 · Baghdad",
                            "arabicLabel": "سعر 100 دولار في بورصتي الكفاح والحارثية ببغداد يوم الثلاثاء 28 تموز 2026 (بورصتا الكفاح والحارثية)"},
                "supportingStats": [
                    {"label": "الأحد 26 تموز", "value": "149,650"},
                    {"label": "الاثنين 27 تموز", "value": "150,050"},
                    {"label": "الثلاثاء 28 تموز", "value": "149,900"},
                ],
                "broll": img(s, "broll_3.jpg"), "brolls": [img(s, "broll_3.jpg")],
                "brollType": "image", "accent": "#FFC217", "brollSource": "Kifah & Harithiya · 2026",
            },
            {
                "label": "لماذا يهم؟",
                "arabicHeading": "من 156,750 إلى 149,900 بشهر",
                "arabicBody": "كان سعر 100 دولار 156,750 ديناراً في 29 حزيران، فأصبح 149,900 في 28 تموز، أي انخفاض 6,850 ديناراً بنسبة 4.4%.",
                "bigStat": {"value": "6,850 د.ع", "label": "Monthly drop per $100",
                            "arabicLabel": "مقدار انخفاض سعر 100 دولار بين 29 حزيران و28 تموز 2026 أي 4.4% (بورصتا الكفاح والحارثية · شفق نيوز)"},
                "supportingStats": [
                    {"label": "29 حزيران", "value": "156,750"},
                    {"label": "18 تموز", "value": "152,950"},
                    {"label": "28 تموز", "value": "149,900"},
                ],
                "broll": img(s, "broll_1.jpg"), "brolls": [img(s, "broll_1.jpg")],
                "brollType": "image", "accent": "#FF6B3D", "brollSource": "Shafaq News · 2026",
            },
            {
                "label": "ماذا بعد؟",
                "arabicHeading": "المحال تبيع بـ150,500 وتشتري بـ149,500",
                "arabicBody": "في محال الصيرفة ببغداد سعر البيع 150,500 والشراء 149,500 لكل 100 دولار، وفي أربيل 150,150 بيعاً و150,050 شراءً.",
                "bigStat": {"value": "150,500", "label": "Baghdad shops selling price",
                            "arabicLabel": "سعر بيع 100 دولار في محال الصيرفة ببغداد مقابل 149,500 ديناراً شراءً يوم 28 تموز 2026 (شفق نيوز · 964)"},
                "supportingStats": [
                    {"label": "بغداد بيعاً", "value": "150,500"},
                    {"label": "بغداد شراءً", "value": "149,500"},
                    {"label": "أربيل بيعاً", "value": "150,150"},
                ],
                "broll": img(s, "broll_2.jpg"), "brolls": [img(s, "broll_2.jpg")],
                "brollType": "image", "accent": "#D72638", "brollSource": "Shafaq News · 964 · 2026",
            },
        ],
        "sources": [
            {"name": "Kifah & Harithiya Bourse", "domain": "Baghdad FX"},
            {"name": "Shafaq News", "domain": "shafaq.com"},
            {"name": "964", "domain": "964media.com"},
        ],
        "arabicTicker": [
            "بورصتا الكفاح والحارثية: 149,900 دينار لكل 100 دولار الثلاثاء 28 تموز",
            "الاثنين 27 تموز فتح على 150,050 وأغلق على 149,950، والأحد 26 تموز 149,650 (شفق نيوز)",
            "المقارنة الشهرية: 156,750 في 29 حزيران و152,950 في 18 تموز و149,900 في 28 تموز",
            "الانخفاض 6,850 ديناراً لكل 100 دولار خلال شهر، بنسبة 4.4%",
            "محال الصيرفة ببغداد: 150,500 بيعاً و149,500 شراءً، وأربيل 150,150 بيعاً و150,050 شراءً (964)",
            "بيش بدلت آخر 100 دولار؟",
        ],
    },
    "v11": {
        "kicker": "عاجل",
        "hookHeadline": "الدولار نزل 6,850 ديناراً بشهر",
        "voText": "سجّلت بورصتا الكفاح والحارثية في بغداد مئة وتسعة وأربعين ألفاً وتسعمئة دينار لكل مئة دولار اليوم الثلاثاء، نزولاً من مئة وخمسين ألفاً وخمسين ديناراً يوم الاثنين. وقبل شهر، في التاسع والعشرين من حزيران، كان السعر مئة وستة وخمسين ألفاً وسبعمئة وخمسين ديناراً، أي أن مئة دولار باتت أرخص بستة آلاف وثمانمئة وخمسين ديناراً، بنسبة أربعة وأربعة من عشرة بالمئة. وفي محال الصيرفة ببغداد سعر البيع مئة وخمسون ألفاً وخمسمئة دينار. فبيش بدلت آخر مئة دولار؟",
        "endQuestion": "بيش بدلت آخر 100 دولار؟",
        "sourcesLine": "المصادر: بورصتا الكفاح والحارثية · شفق نيوز · 964",
        "statPops": [
            {"value": "149,900", "label": "لكل 100 دولار اليوم", "matchWord": "وتسعمئة"},
            {"value": "6,850 د.ع", "label": "نزول خلال شهر", "matchWord": "وثمانمئة"},
        ],
    },
    "caption": """سعر الدولار اليوم في بغداد — نزل 6,850 ديناراً خلال شهر

149,900 لكل 100 دولار في بورصتي الكفاح والحارثية.

بيش بدلت آخر 100 دولار؟

المصادر: بورصتا الكفاح والحارثية، شفق نيوز، 964
#العراق #الدولار #سعر_الصرف #الدينار_العراقي
@photonect.news
""",
}

# ─────────────────────────────────────────────────────────────────────────
# 3 — OIL FALLS ON THE PAUSE  (iraq_economy · SILENT V10.1 CONTROL · A)
# ─────────────────────────────────────────────────────────────────────────
s = f"{DATE}-energy-peace-price"
SLUGS[s] = {
    "bucket": "iraq_economy",
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/mood_newsroom.mp3", "topicBucket": "iraq_economy", "variant": "A",
        "breaking": {
            "arabicKicker": "نفط · ميزانية",
            "arabicHeadline": "النفط نزل 8.7%… وميزانية الدولة 84% نفط",
            "englishSubhead": "BRENT'S BIGGEST ONE-DAY DROP IN MONTHS HITS AN 84% OIL-FUNDED BUDGET",
            "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
        },
        "beats": [
            {
                "label": "ماذا يحدث؟",
                "arabicHeading": "برنت يغلق عند 88.36 دولاراً",
                "arabicBody": "أغلق برنت الاثنين منخفضاً 8.7% عند 88.36 دولاراً، في أكبر هبوط يومي منذ أكثر من ثلاثة أشهر، بحسب رويترز وبلومبيرغ.",
                "bigStat": {"value": "$88.36", "label": "Brent close, down 8.7%",
                            "arabicLabel": "سعر إغلاق خام برنت يوم الاثنين 27 تموز 2026 بانخفاض 8.7% وهو أكبر هبوط يومي منذ أكثر من ثلاثة أشهر (رويترز · بلومبيرغ)"},
                "supportingStats": [
                    {"label": "برنت الاثنين", "value": "$88.36"},
                    {"label": "التراجع", "value": "8.7%"},
                    {"label": "غرب تكساس", "value": "$82.61"},
                ],
                "broll": img(s, "broll_1.jpg"), "brolls": [img(s, "broll_1.jpg")],
                "brollType": "image", "accent": "#FFC217", "brollSource": "Reuters · Bloomberg · 2026",
            },
            {
                "label": "لماذا يهم؟",
                "arabicHeading": "توقف الضربات بعد 13 ليلة متتالية",
                "arabicBody": "أوقفت الولايات المتحدة ضرباتها على إيران مساء الجمعة 24 تموز بعد 13 ليلة متتالية، فيما نفت الخارجية الإيرانية وجود مفاوضات، بحسب رويترز.",
                "bigStat": {"value": "13 ليلة", "label": "Consecutive nights of strikes",
                            "arabicLabel": "عدد الليالي المتتالية من الضربات الأميركية على إيران قبل توقفها مساء الجمعة 24 تموز 2026 (رويترز)"},
                "supportingStats": [
                    {"label": "التوقف", "value": "24 تموز"},
                    {"label": "برنت الثلاثاء", "value": "$86.89"},
                    {"label": "غرب تكساس", "value": "$81.16"},
                ],
                "broll": img(s, "broll_2.jpg"), "brolls": [img(s, "broll_2.jpg")],
                "brollType": "image", "accent": "#FF6B3D", "brollSource": "Reuters · 2026",
            },
            {
                "label": "ماذا بعد؟",
                "arabicHeading": "84% من إيرادات الدولة نفط",
                "arabicBody": "بلغت إيرادات النفط والمعادن 26.946 تريليون دينار من أصل 33.747 تريليوناً بين كانون الثاني وأيار 2026، أي 84%، بانخفاض 14.985 تريليوناً ونسبته 35.7%.",
                "bigStat": {"value": "84%", "label": "Share of state revenue from oil",
                            "arabicLabel": "حصة إيرادات النفط والمعادن من إجمالي إيرادات الدولة بين كانون الثاني وأيار 2026، أي 26.946 تريليون دينار من 33.747 تريليوناً (شفق نيوز)"},
                "supportingStats": [
                    {"label": "النفط والمعادن", "value": "26.946 تريليون"},
                    {"label": "الإجمالي", "value": "33.747 تريليون"},
                    {"label": "غير النفطي", "value": "16%"},
                ],
                "broll": img(s, "broll_3.jpg"), "brolls": [img(s, "broll_3.jpg")],
                "brollType": "image", "accent": "#D72638", "brollSource": "Shafaq News · 2026",
            },
        ],
        "sources": [
            {"name": "Reuters", "domain": "reuters.com"},
            {"name": "Bloomberg", "domain": "bloomberg.com"},
            {"name": "Shafaq News", "domain": "shafaq.com"},
        ],
        "arabicTicker": [
            "برنت أغلق الاثنين 27 تموز منخفضاً 8.7% عند 88.36 دولاراً، أكبر هبوط يومي منذ أكثر من ثلاثة أشهر (رويترز · بلومبيرغ)",
            "غرب تكساس تراجع 7.5% إلى 82.61 دولاراً في الجلسة نفسها (رويترز)",
            "الثلاثاء 28 تموز: برنت 86.89 دولاراً بانخفاض 1.66%، وغرب تكساس 81.16 بانخفاض 1.76% وهو الأدنى منذ 20 تموز (بلومبيرغ)",
            "الولايات المتحدة أوقفت ضرباتها على إيران مساء الجمعة 24 تموز بعد 13 ليلة متتالية، والخارجية الإيرانية نفت وجود مفاوضات (رويترز)",
            "إيرادات النفط والمعادن 26.946 تريليون دينار من أصل 33.747 تريليوناً بين كانون الثاني وأيار 2026 أي 84%، بانخفاض 14.985 تريليوناً ونسبته 35.7% (شفق نيوز)",
            "راتبك من الدولة لو من القطاع الخاص؟",
        ],
    },
    "v11": None,  # silent V10.1 control
    "caption": """أسعار النفط تنزل بعد توقف الضربات — وميزانية العراق 84% نفط

برنت سجّل أكبر هبوط يومي منذ أكثر من ثلاثة أشهر.

راتبك من الدولة لو من القطاع الخاص؟

المصادر: رويترز، بلومبيرغ، شفق نيوز
#العراق #النفط #برنت #الموازنة
@photonect.news
""",
}

# ─────────────────────────────────────────────────────────────────────────
# 4 — 27 BILLION DINARS PULLED OUT OF HIDING  (iraq_politics · V11 · B)
# ─────────────────────────────────────────────────────────────────────────
s = f"{DATE}-graft-oil-27-billion"
SLUGS[s] = {
    "bucket": "iraq_politics",
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/mood_newsroom.mp3", "topicBucket": "iraq_politics", "variant": "B",
        "breaking": {
            "arabicKicker": "فساد · نفط",
            "arabicHeadline": "27 مليار دينار مخبأة… بقضية وكيل النفط",
            "englishSubhead": "27 BILLION DINARS FOUND HIDDEN IN THE FORMER DEPUTY OIL MINISTER'S CASE",
            "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
        },
        "beats": [
            {
                "label": "ماذا يحدث؟",
                "arabicHeading": "27 مليار دينار جديدة تُضبط",
                "arabicBody": "أعلن القاضي ضياء جعفر ضبط 27 مليار دينار كانت مخبأة لدى عدد من الأشخاص، ضمن قضية وكيل وزارة النفط الأسبق، في 26 تموز.",
                "bigStat": {"value": "27 مليار د.ع", "label": "Newly seized in the case",
                            "arabicLabel": "قيمة الأموال المضبوطة حديثاً والمخبأة لدى عدد من الأشخاص في قضية وكيل وزارة النفط الأسبق، بإعلان القاضي ضياء جعفر في 26 تموز 2026"},
                "supportingStats": [
                    {"label": "الإعلان", "value": "26 تموز"},
                    {"label": "قاضي التحقيق", "value": "ضياء جعفر"},
                    {"label": "المحكمة", "value": "تحقيق الكرخ"},
                ],
                "broll": img(s, "broll_1.jpg"), "brolls": [img(s, "broll_1.jpg")],
                "brollType": "image", "accent": "#FFC217", "brollSource": "964 · 2026",
            },
            {
                "label": "لماذا يهم؟",
                "arabicHeading": "المتهم وكيل وزارة النفط الأسبق",
                "arabicBody": "المتهم عدنان الجميلي، وكيل وزارة النفط الأسبق لشؤون التصفية، أُلقي القبض عليه أواخر أيار 2026، والقضية أمام المحكمة الجنائية المركزية المختصة بقضايا الفساد.",
                "bigStat": {"value": "أيار 2026", "label": "Arrest of the former deputy minister",
                            "arabicLabel": "تاريخ إلقاء القبض على عدنان الجميلي وكيل وزارة النفط الأسبق لشؤون التصفية، والقضية أمام المحكمة الجنائية المركزية المختصة بقضايا الفساد"},
                "supportingStats": [
                    {"label": "المتهم", "value": "عدنان الجميلي"},
                    {"label": "المنصب", "value": "وكيل وزارة النفط"},
                    {"label": "التوقيف", "value": "أواخر أيار"},
                ],
                "broll": img(s, "broll_3.jpg"), "brolls": [img(s, "broll_3.jpg")],
                "brollType": "image", "accent": "#FF6B3D", "brollSource": "Al Arabiya · 2026",
            },
            {
                "label": "ماذا بعد؟",
                "arabicHeading": "2.5 مليار و6 عقارات بصلاح الدين",
                "arabicBody": "وفي 28 تموز أعلنت هيئة النزاهة حجز 2.5 مليار دينار و6 عقارات مسجلة باسم زوجة مدير حسابات أسبق في صلاح الدين، بصك من مصرف الرافدين.",
                "bigStat": {"value": "2.5 مليار د.ع", "label": "Seized in the Salah al-Din file",
                            "arabicLabel": "قيمة الأموال المحجوزة مع 6 عقارات في قضية مدير حسابات أسبق بصلاح الدين، والحجز جرى الثلاثاء 22 تموز 2026 (هيئة النزاهة الاتحادية)"},
                "supportingStats": [
                    {"label": "العقارات", "value": "6"},
                    {"label": "تاريخ الحجز", "value": "22 تموز"},
                    {"label": "المصرف", "value": "الرافدين"},
                ],
                "broll": img(s, "broll_2.jpg"), "brolls": [img(s, "broll_2.jpg")],
                "brollType": "image", "accent": "#D72638", "brollSource": "Integrity Commission · 2026",
            },
        ],
        "sources": [
            {"name": "964", "domain": "964media.com"},
            {"name": "Al Arabiya", "domain": "alarabiya.net"},
            {"name": "Al Rasheed", "domain": "alrasheedmedia.com"},
        ],
        "arabicTicker": [
            "القاضي ضياء جعفر: ضبط 27 مليار دينار كانت مخبأة لدى عدد من الأشخاص في قضية وكيل وزارة النفط الأسبق (26 تموز 2026)",
            "المتهم عدنان الجميلي وكيل وزارة النفط الأسبق لشؤون التصفية، أُلقي القبض عليه أواخر أيار 2026",
            "القضية أمام المحكمة الجنائية المركزية المختصة بقضايا الفساد",
            "هيئة النزاهة الاتحادية: حجز 2.5 مليار دينار و6 عقارات مسجلة باسم زوجة مدير حسابات أسبق في صلاح الدين (28 تموز)",
            "الحجز جرى الثلاثاء 22 تموز على خلفية صك من مصرف الرافدين تضمّن وصولات وهمية (هيئة النزاهة الاتحادية)",
            "شفت قضية فساد بالعراق وصلت لحكم؟",
        ],
    },
    "v11": {
        "kicker": "عاجل",
        "hookHeadline": "27 مليار دينار مخبأة لدى أشخاص",
        "voText": "أعلن القاضي ضياء جعفر، قاضي التحقيق في المحكمة الجنائية المركزية المختصة بقضايا الفساد، ضبط سبعة وعشرين مليار دينار كانت مخبأة لدى عدد من الأشخاص، ضمن قضية وكيل وزارة النفط الأسبق لشؤون التصفية عدنان الجميلي، الذي أُلقي القبض عليه أواخر أيار. وفي ملف منفصل، حجزت هيئة النزاهة الاتحادية ملياري دينار ونصف المليار وستة عقارات مسجلة باسم زوجة مدير حسابات أسبق في صلاح الدين، على خلفية صك من مصرف الرافدين. فشفت قضية فساد وصلت إلى حكم؟",
        "endQuestion": "شفت قضية فساد بالعراق وصلت لحكم؟",
        "sourcesLine": "المصادر: 964 · العربية · الرشيد",
        "statPops": [
            {"value": "27 مليار د.ع", "label": "مضبوطة بقضية النفط", "matchWord": "وعشرين"},
            {"value": "6 عقارات", "label": "محجوزة بصلاح الدين", "matchWord": "وستة"},
        ],
    },
    "caption": """قضية وكيل وزارة النفط — 27 مليار دينار مخبأة تُضبط

القاضي ضياء جعفر يعلن الضبط، وملف منفصل في صلاح الدين.

شفت قضية فساد بالعراق وصلت لحكم؟

المصادر: 964، العربية، الرشيد
#العراق #الفساد #النزاهة #وزارة_النفط
@photonect.news
""",
}

# ─────────────────────────────────────────────────────────────────────────
# 5 — JULY SALARIES: FUNDED 22 JULY, STILL NOT PAID  (iraq_economy · V11 · C)
# ─────────────────────────────────────────────────────────────────────────
s = f"{DATE}-salaries-late-july"
SLUGS[s] = {
    "bucket": "iraq_economy",
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/mood_newsroom.mp3", "topicBucket": "iraq_economy", "variant": "C",
        "breaking": {
            "arabicKicker": "رواتب · مالية",
            "arabicHeadline": "راتبك تأخر؟ اللجنة المالية تقول 48 ساعة",
            "englishSubhead": "JULY SALARIES FUNDED ON 22 JULY, MP PUTS A 48-HOUR CLOCK ON PAYOUT",
            "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
        },
        "beats": [
            {
                "label": "ماذا يحدث؟",
                "arabicHeading": "التمويل أُطلق في 22 تموز",
                "arabicBody": "بدأت دائرة المحاسبة في وزارة المالية إطلاق تمويل رواتب موظفي الدولة لشهر تموز يوم الأربعاء 22 تموز 2026، بحسب شفق نيوز وأوبزرفر العراق.",
                "bigStat": {"value": "22 تموز", "label": "Funding release began",
                            "arabicLabel": "اليوم الذي بدأت فيه دائرة المحاسبة في وزارة المالية إطلاق تمويل رواتب تموز لموظفي الدولة (شفق نيوز · أوبزرفر العراق)"},
                "supportingStats": [
                    {"label": "الجهة", "value": "دائرة المحاسبة"},
                    {"label": "الشهر", "value": "تموز 2026"},
                    {"label": "اليوم", "value": "الأربعاء"},
                ],
                "broll": img(s, "broll_2.jpg"), "brolls": [img(s, "broll_2.jpg")],
                "brollType": "image", "accent": "#FFC217", "brollSource": "Shafaq News · 2026",
            },
            {
                "label": "لماذا يهم؟",
                "arabicHeading": "السيولة المحلية وتدقيق الحسابات",
                "arabicBody": "لم يكتمل الصرف في عدد من مؤسسات الدولة بسبب صعوبة توفر السيولة النقدية المحلية، وعزا عامر نصر الله التأخير إلى تدقيق وزارة المالية للبيانات والحسابات.",
                "bigStat": {"value": "27 تموز", "label": "MP explains the delay",
                            "arabicLabel": "تاريخ تصريح عضو اللجنة المالية النيابية عامر نصر الله الذي عزا التأخير إلى تدقيق وزارة المالية للبيانات والحسابات المالية (شفق نيوز)"},
                "supportingStats": [
                    {"label": "السبب الأول", "value": "السيولة المحلية"},
                    {"label": "والثاني", "value": "تدقيق الحسابات"},
                    {"label": "التصريح", "value": "27 تموز"},
                ],
                "broll": img(s, "broll_1.jpg"), "brolls": [img(s, "broll_1.jpg")],
                "brollType": "image", "accent": "#FF6B3D", "brollSource": "Observer Iraq · 2026",
            },
            {
                "label": "ماذا بعد؟",
                "arabicHeading": "48 ساعة… وعد اللجنة المالية",
                "arabicBody": "قال عامر نصر الله، عضو اللجنة المالية النيابية، في 27 تموز إن الرواتب ستُطلق خلال 48 ساعة لمؤسسات الدولة المدنية والأمنية بدفعة واحدة.",
                "bigStat": {"value": "48 ساعة", "label": "MP's timeline for release",
                            "arabicLabel": "المهلة التي حددها عضو اللجنة المالية النيابية عامر نصر الله لإطلاق الرواتب في مؤسسات الدولة المدنية والأمنية بدفعة واحدة (شفق نيوز)"},
                "supportingStats": [
                    {"label": "المهلة", "value": "48 ساعة"},
                    {"label": "الشمول", "value": "مدنية وأمنية"},
                    {"label": "الدفع", "value": "دفعة واحدة"},
                ],
                "broll": img(s, "broll_3.jpg"), "brolls": [img(s, "broll_3.jpg")],
                "brollType": "image", "accent": "#D72638", "brollSource": "Shafaq News · 2026",
            },
        ],
        "sources": [
            {"name": "Shafaq News", "domain": "shafaq.com"},
            {"name": "Observer Iraq", "domain": "observeriraq.net"},
        ],
        "arabicTicker": [
            "دائرة المحاسبة في وزارة المالية بدأت إطلاق تمويل رواتب تموز يوم الأربعاء 22 تموز 2026 (شفق نيوز · أوبزرفر العراق)",
            "رغم إطلاق التمويل لم يكتمل الصرف في عدد من مؤسسات الدولة (شفق نيوز)",
            "السبب: استمرار صعوبة توفر السيولة النقدية المحلية لدى بعض الجهات (شفق نيوز)",
            "عامر نصر الله عضو اللجنة المالية النيابية: الرواتب ستُطلق خلال 48 ساعة (27 تموز)",
            "الإطلاق يشمل مؤسسات الدولة المدنية والأمنية بدفعة واحدة، والتأخير سببه تدقيق البيانات والحسابات المالية (عامر نصر الله)",
            "راتبك وصل لو بعده متأخر؟",
        ],
    },
    "v11": {
        "kicker": "عاجل",
        "hookHeadline": "راتبك تأخر؟ 48 ساعة",
        "voText": "بدأت دائرة المحاسبة في وزارة المالية إطلاق تمويل رواتب موظفي الدولة لشهر تموز يوم الأربعاء الثاني والعشرين من تموز، بحسب شفق نيوز وأوبزرفر العراق. ورغم ذلك لم يكتمل الصرف في عدد من مؤسسات الدولة بسبب صعوبة توفر السيولة النقدية المحلية. وقال عضو اللجنة المالية النيابية عامر نصر الله إن الرواتب ستُطلق خلال ثمان وأربعين ساعة لمؤسسات الدولة المدنية والأمنية بدفعة واحدة، عازياً التأخير إلى تدقيق وزارة المالية للبيانات والحسابات. فراتبك وصل لو بعده متأخر؟",
        "endQuestion": "راتبك وصل لو بعده متأخر؟",
        "sourcesLine": "المصادر: شفق نيوز · أوبزرفر العراق",
        "statPops": [
            {"value": "22 تموز", "label": "إطلاق التمويل", "matchWord": "والعشرين"},
            {"value": "48 ساعة", "label": "مهلة اللجنة المالية", "matchWord": "وأربعين"},
        ],
    },
    "caption": """رواتب تموز في العراق — وين وصلت ومتى تنزل؟

التمويل أُطلق في 22 تموز، واللجنة المالية تتحدث عن 48 ساعة.

راتبك وصل لو بعده متأخر؟

المصادر: شفق نيوز، أوبزرفر العراق
#العراق #الرواتب #وزارة_المالية #رواتب_تموز
@photonect.news
""",
}


def main() -> int:
    for slug, cfg in SLUGS.items():
        d = POSTS / slug / ".meta"
        d.mkdir(parents=True, exist_ok=True)
        (d / "props.json").write_text(
            json.dumps(cfg["props"], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        (POSTS / slug / "caption.txt").write_text(cfg["caption"], encoding="utf-8")
        (d / "media-stamp.json").write_text(
            json.dumps(STAMP, ensure_ascii=False) + "\n", encoding="utf-8")
        if cfg.get("v11"):
            v = dict(cfg["v11"])
            v["slug"] = slug
            v["images"] = [img(slug, n) for n in
                           ("hero.jpg", "broll_1.jpg", "broll_2.jpg", "broll_3.jpg")]
            v["audioBed"] = "audio/mood_newsroom.mp3"
            ordered = {k: v[k] for k in
                       ("slug", "kicker", "hookHeadline", "voText", "endQuestion",
                        "sourcesLine", "images", "audioBed", "statPops")}
            (d / "v11-brief.json").write_text(
                json.dumps(ordered, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"  ✓ {slug}  ({'V11' if cfg.get('v11') else 'V10.1 control'})")
    print(f"\n== {len(SLUGS)} slugs written for {DATE} ==")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
