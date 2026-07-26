#!/usr/bin/env python3
"""Author the 2026-07-26 Photonect NEWS slate.

5 slugs (Iraq/MENA money-power lens). Posting order:
  1 audit-100tn-loans    P1 corruption/audit     V11  A   (LEAD)
  2 dollar-under-150     P1 money/dinar          V11  A   (daily dollar anchor)
  3 ampere-price-july    P1 electricity/services V11  B
  4 us-zero-crude        P2 oil/trade            V10  C   <- silent control (driest/abstract)
  5 nonoil-revenue-16    P1 revenue/taxes        V11  B

Directional shift vs 2026-07-24: moves off money-SUPPLY (printing/barter/SWF) to
the WHO-PAYS-AND-WHO-OWES lens — unsettled state loans (100tn IQD), a dinar that
is actually strengthening (below 150k for the first time in weeks), the literal
monthly generator bill, and the tax/customs share of state income. Three of five
carry a price the viewer personally pays.

Writes per slug: .meta/props.json, caption.txt, .meta/media-stamp.json, and (for
the 4 voiced) .meta/v11-brief.json. Western numerals on-screen; voText spells
numbers in words (MSA newscast). No Persian yeh/kaf (grep-guarded after run).
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "data" / "posts"
DATE = "2026-07-26"
DATE_LABEL = "JUL 26 • 2026"
AR_DATE = "26 يوليو 2026"
HANDLE = "@photonect.news"
STAMP = {"hunted_at": f"{DATE}T11:00:00+00:00"}


def img(slug, n):
    return f"images/news/{slug}/{n}"


SLUGS = {}

# ─────────────────────────────────────────────────────────────────────────
# 1 — AUDIT: 100 TRILLION DINARS IN UNSETTLED LOANS  (P1 · V11 · A · LEAD)
# ─────────────────────────────────────────────────────────────────────────
s = f"{DATE}-audit-100tn-loans"
SLUGS[s] = {
    "bucket": "iraq_politics",
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/mood_newsroom.mp3", "topicBucket": "iraq_politics", "variant": "A",
        "breaking": {
            "arabicKicker": "فساد · رقابة مالية",
            "arabicHeadline": "100 تريليون دينار… سُلف ما رجعت",
            "englishSubhead": "AUDIT BOARD PROBES 100TN IQD IN UNSETTLED STATE LOANS",
            "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
        },
        "beats": [
            {
                "label": "ماذا يحدث؟",
                "arabicHeading": "الرقابة المالية تفتح ملف السُلف",
                "arabicBody": "أعلن ديوان الرقابة المالية الاتحادي تتبّع نحو 100 تريليون دينار سُلفاً مُنحت لجهات ومسؤولين ولم تُسوَّ منذ 2004، بحسب AGBI.",
                "bigStat": {"value": "100T IQD", "label": "Unsettled state loans",
                            "arabicLabel": "إجمالي السُلف غير المُسوّاة التي يتتبّعها ديوان الرقابة المالية الاتحادي منذ عام 2004 (AGBI)"},
                "supportingStats": [
                    {"label": "القيمة", "value": "$77 مليار"},
                    {"label": "المدة", "value": "22 سنة"},
                    {"label": "الجهة", "value": "الرقابة المالية"},
                ],
                "broll": img(s, "broll_1.jpg"), "brolls": [img(s, "broll_1.jpg")],
                "brollType": "image", "accent": "#FFC217", "brollSource": "AGBI · 2026",
            },
            {
                "label": "لماذا يهم؟",
                "arabicHeading": "آلاف القضايا أُحيلت إلى القضاء",
                "arabicBody": "قال رئيس الديوان عمار المشهداني إن نحو 100 تريليون دينار من السُلف لم تُسوَّ، وإن الديوان أحال آلاف القضايا إلى القضاء.",
                "bigStat": {"value": "$77B", "label": "Value of untraced loans",
                            "arabicLabel": "القيمة الدولارية التقريبية للسُلف غير المُسوّاة وفق رئيس ديوان الرقابة المالية عمار المشهداني (AGBI)"},
                "supportingStats": [
                    {"label": "المصدر", "value": "وزارة المالية"},
                    {"label": "وأيضاً", "value": "البنك المركزي"},
                    {"label": "الإحالات", "value": "آلاف القضايا"},
                ],
                "broll": img(s, "broll_2.jpg"), "brolls": [img(s, "broll_2.jpg")],
                "brollType": "image", "accent": "#FF6B3D", "brollSource": "AGBI · 2026",
            },
            {
                "label": "ماذا بعد؟",
                "arabicHeading": "الملف ضمن حملة صولة الفجر",
                "arabicBody": "يأتي الكشف ضمن حملة مكافحة الفساد التي أطلقها رئيس الوزراء علي الزيدي في 28 حزيران، والعراق في المرتبة 136 من 182 بمؤشر الشفافية.",
                "bigStat": {"value": "136 / 182", "label": "Transparency Intl rank",
                            "arabicLabel": "ترتيب العراق في مؤشر مدركات الفساد لمنظمة الشفافية الدولية للعام الماضي (AGBI)"},
                "supportingStats": [
                    {"label": "انطلاق الحملة", "value": "28 حزيران"},
                    {"label": "المؤشر", "value": "136 / 182"},
                    {"label": "رئيس الوزراء", "value": "علي الزيدي"},
                ],
                "broll": img(s, "broll_3.jpg"), "brolls": [img(s, "broll_3.jpg")],
                "brollType": "image", "accent": "#D72638", "brollSource": "AGBI · 2026",
            },
        ],
        "sources": [
            {"name": "AGBI", "domain": "agbi.com"},
            {"name": "Federal Board of Supreme Audit", "domain": "fbsa.gov.iq"},
            {"name": "Transparency International", "domain": "transparency.org"},
        ],
        "arabicTicker": [
            "ديوان الرقابة المالية الاتحادي يتتبّع نحو 100 تريليون دينار سُلفاً لم تُسوَّ منذ 2004 (AGBI)",
            "القيمة تعادل نحو 77 مليار دولار مُنحت لمسؤولين ووزارات وجهات عامة (AGBI)",
            "رئيس الديوان عمار المشهداني: أحلنا آلاف القضايا إلى القضاء (AGBI)",
            "الكشف يأتي ضمن حملة مكافحة الفساد التي أطلقها رئيس الوزراء علي الزيدي في 28 حزيران (AGBI)",
            "العراق في المرتبة 136 من 182 دولة بمؤشر مدركات الفساد للعام الماضي (منظمة الشفافية الدولية)",
        ],
    },
    "v11": {
        "kicker": "عاجل",
        "hookHeadline": "100 تريليون دينار… وين راحت؟",
        "voText": "أعلن ديوان الرقابة المالية الاتحادي في العراق أنه يتتبّع نحو مئة تريليون دينار، أي ما يعادل سبعة وسبعين مليار دولار، سُلفاً مُنحت لمسؤولين ووزارات وجهات عامة منذ عام ألفين وأربعة ولم تُسوَّ حتى الآن، وذلك بحسب موقع AGBI. وقال رئيس الديوان عمار المشهداني إن الديوان أحال آلاف القضايا إلى القضاء. ويأتي ذلك ضمن حملة مكافحة الفساد التي أطلقها رئيس الوزراء علي الزيدي أواخر حزيران وأوقفت عشرات المسؤولين. فشنو الخدمة الناقصة بمنطقتك؟",
        "endQuestion": "شنو الخدمة الناقصة بمنطقتك؟",
        "sourcesLine": "المصادر: AGBI · ديوان الرقابة المالية · منظمة الشفافية الدولية",
        "statPops": [
            {"value": "100 تريليون", "label": "سُلف غير مُسوّاة", "matchWord": "تريليون"},
            {"value": "$77 مليار", "label": "قيمتها بالدولار", "matchWord": "وسبعين"},
            {"value": "2004", "label": "بداية الملف", "matchWord": "وأربعة"},
        ],
    },
    "caption": """100 تريليون دينار سُلف ما رجعت — وين راحت؟

ديوان الرقابة المالية يتتبّع سُلفاً مُنحت لمسؤولين وجهات عامة منذ 2004 ولم تُسوَّ.

شنو الخدمة الناقصة بمنطقتك؟

المصادر: AGBI، ديوان الرقابة المالية
#العراق #الفساد #الرقابة_المالية #صولة_الفجر
@photonect.news
""",
}

# ─────────────────────────────────────────────────────────────────────────
# 2 — DOLLAR SLIDES BELOW 150,000  (P1 · V11 · A · daily dollar anchor)
# ─────────────────────────────────────────────────────────────────────────
s = f"{DATE}-dollar-under-150"
SLUGS[s] = {
    "bucket": "iraq_economy",
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/mood_newsroom.mp3", "topicBucket": "iraq_economy", "variant": "A",
        "breaking": {
            "arabicKicker": "دولار · صرف",
            "arabicHeadline": "الدولار ينزل تحت 150 ألف",
            "englishSubhead": "DOLLAR SLIDES BELOW 150,000 IQD PER $100 IN BAGHDAD",
            "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
        },
        "beats": [
            {
                "label": "ماذا يحدث؟",
                "arabicHeading": "149,650 ديناراً لكل 100 دولار",
                "arabicBody": "فتح الدولار تداولات الأحد في بورصتي الكفاح والحارثية على 149,650 ديناراً لكل 100 دولار، نزولاً من 150,500 في الجلسة السابقة، بحسب شفق نيوز.",
                "bigStat": {"value": "149,650", "label": "IQD per $100 · Baghdad",
                            "arabicLabel": "سعر 100 دولار في بورصتي الكفاح والحارثية عند افتتاح تداولات الأحد 26 تموز 2026 (شفق نيوز)"},
                "supportingStats": [
                    {"label": "الافتتاح", "value": "149,650"},
                    {"label": "الجلسة السابقة", "value": "150,500"},
                    {"label": "السوق", "value": "الكفاح"},
                ],
                "broll": img(s, "broll_1.jpg"), "brolls": [img(s, "broll_1.jpg")],
                "brollType": "image", "accent": "#FFC217", "brollSource": "Shafaq News · 2026",
            },
            {
                "label": "لماذا يهم؟",
                "arabicHeading": "أربيل وبغداد تحت 150 ألفاً",
                "arabicBody": "في أربيل بلغ البيع 150,150 ديناراً والشراء 150,050، وفي محال الصيرفة ببغداد 150,000 بيعاً و149,000 شراءً، بحسب شفق نيوز.",
                "bigStat": {"value": "150,150", "label": "Erbil selling rate",
                            "arabicLabel": "سعر بيع 100 دولار في أسواق أربيل يوم 26 تموز 2026 (شفق نيوز)"},
                "supportingStats": [
                    {"label": "أربيل بيع", "value": "150,150"},
                    {"label": "صيرفة بيع", "value": "150,000"},
                    {"label": "صيرفة شراء", "value": "149,000"},
                ],
                "broll": img(s, "broll_2.jpg"), "brolls": [img(s, "broll_2.jpg")],
                "brollType": "image", "accent": "#FF6B3D", "brollSource": "Shafaq News · 2026",
            },
            {
                "label": "ماذا بعد؟",
                "arabicHeading": "الفجوة مع السعر الرسمي تضيق",
                "arabicBody": "السعر الرسمي للبنك المركزي 1,320 ديناراً للدولار، فيما كان الدولار عند 153,750 لكل 100 دولار في 11 تموز، بحسب شفق نيوز.",
                "bigStat": {"value": "1,320", "label": "Official CBI rate per $1",
                            "arabicLabel": "سعر الصرف الرسمي الذي يبيع به البنك المركزي العراقي الدولار للمصارف والتجار (البنك المركزي العراقي)"},
                "supportingStats": [
                    {"label": "الرسمي", "value": "1,320"},
                    {"label": "11 تموز", "value": "153,750"},
                    {"label": "اليوم", "value": "149,650"},
                ],
                "broll": img(s, "broll_3.jpg"), "brolls": [img(s, "broll_3.jpg")],
                "brollType": "image", "accent": "#D72638", "brollSource": "Shafaq News · 2026",
            },
        ],
        "sources": [
            {"name": "Shafaq News", "domain": "shafaq.com"},
            {"name": "Central Bank of Iraq", "domain": "cbi.iq"},
        ],
        "arabicTicker": [
            "الدولار يفتح تداولات الأحد على 149,650 ديناراً لكل 100 دولار في الكفاح والحارثية (شفق نيوز)",
            "نزولاً من 150,500 دينار في الجلسة السابقة (شفق نيوز)",
            "أربيل: 150,150 ديناراً بيعاً و150,050 شراءً لكل 100 دولار (شفق نيوز)",
            "محال الصيرفة ببغداد: 150,000 بيعاً و149,000 شراءً (شفق نيوز)",
            "السعر الرسمي للبنك المركزي 1,320 ديناراً للدولار الواحد (البنك المركزي العراقي)",
        ],
    },
    "v11": {
        "kicker": "عاجل",
        "hookHeadline": "الدولار طاح تحت 150 ألف",
        "voText": "فتح الدولار تداولات يوم الأحد في العراق على انخفاض جديد، إذ سُجّل سعر مئة دولار في بورصتي الكفاح والحارثية ببغداد عند مئة وتسعة وأربعين ألفاً وستمئة وخمسين ديناراً، نزولاً من مئة وخمسين ألفاً وخمسمئة دينار في الجلسة السابقة، وذلك بحسب شفق نيوز. وفي أربيل بلغ سعر البيع مئة وخمسين ألفاً ومئة وخمسين ديناراً. ويبقى السعر الرسمي للبنك المركزي العراقي عند ألف وثلاثمئة وعشرين ديناراً للدولار الواحد. فبيش شريت الدولار اليوم؟",
        "endQuestion": "بيش شريت الدولار اليوم؟",
        "sourcesLine": "المصادر: شفق نيوز · البنك المركزي العراقي",
        "statPops": [
            {"value": "149,650", "label": "لكل 100 دولار", "matchWord": "وستمئة"},
            {"value": "150,500", "label": "الجلسة السابقة", "matchWord": "وخمسمئة"},
            {"value": "1,320", "label": "السعر الرسمي", "matchWord": "وعشرين"},
        ],
    },
    "caption": """سعر الدولار في العراق اليوم — طاح تحت 150 ألف

الكفاح والحارثية فتحت تداولات الأحد على نزول جديد أمام الدينار.

بيش شريت الدولار اليوم؟

المصادر: شفق نيوز، البنك المركزي
#العراق #الدولار #الدينار_العراقي #سعر_الصرف
@photonect.news
""",
}

# ─────────────────────────────────────────────────────────────────────────
# 3 — JULY AMPERE PRICE / NEIGHBOURHOOD GENERATORS  (P1 · V11 · B)
# ─────────────────────────────────────────────────────────────────────────
s = f"{DATE}-ampere-price-july"
SLUGS[s] = {
    "bucket": "iraq_economy",
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/mood_newsroom.mp3", "topicBucket": "iraq_economy", "variant": "B",
        "breaking": {
            "arabicKicker": "كهرباء · مولدات",
            "arabicHeadline": "سعر الأمبير 10 آلاف… والليلي ملغى",
            "englishSubhead": "BAGHDAD SETS JULY AMPERE RATE AT 10,000 IQD, SCRAPS NIGHT-ONLY SERVICE",
            "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
        },
        "beats": [
            {
                "label": "ماذا يحدث؟",
                "arabicHeading": "10 آلاف دينار للأمبير الذهبي",
                "arabicBody": "حدّدت محافظة بغداد تسعيرة تموز عند 10,000 دينار للأمبير بالتشغيل الذهبي، و5,000 في مناطق الجباية، وألغت التشغيل الليلي بالكامل.",
                "bigStat": {"value": "10,000 د.ع", "label": "July ampere rate",
                            "arabicLabel": "تسعيرة الأمبير الواحد بالتشغيل الذهبي لشهر تموز 2026 التي حدّدتها محافظة بغداد (محافظة بغداد)"},
                "supportingStats": [
                    {"label": "ذهبي", "value": "10,000 د.ع"},
                    {"label": "الجباية", "value": "5,000 د.ع"},
                    {"label": "الليلي", "value": "ملغى"},
                ],
                "broll": img(s, "broll_1.jpg"), "brolls": [img(s, "broll_1.jpg")],
                "brollType": "image", "accent": "#FFC217", "brollSource": "Baghdad Governorate · 2026",
            },
            {
                "label": "لماذا يهم؟",
                "arabicHeading": "وقود مجاني و20 ساعة تجهيز",
                "arabicBody": "وافق مجلس الوزراء على تجهيز أصحاب المولدات بزيت الغاز مجاناً بواقع 45 لتراً لكل كيلوفولت أمبير في تموز وآب، على ألا تقل ساعات التجهيز عن 20 ساعة يومياً.",
                "bigStat": {"value": "20 ساعة", "label": "Minimum daily supply",
                            "arabicLabel": "الحد الأدنى لساعات تجهيز المواطنين بالطاقة من المولدات الأهلية يومياً وفق قرار مجلس الوزراء (مجلس الوزراء)"},
                "supportingStats": [
                    {"label": "الوقود", "value": "45 لتراً/kVA"},
                    {"label": "المدة", "value": "تموز وآب"},
                    {"label": "التجهيز", "value": "20 ساعة"},
                ],
                "broll": img(s, "broll_2.jpg"), "brolls": [img(s, "broll_2.jpg")],
                "brollType": "image", "accent": "#FF6B3D", "brollSource": "Council of Ministers · 2026",
            },
            {
                "label": "ماذا بعد؟",
                "arabicHeading": "غرامة 5 ملايين للمخالفين",
                "arabicBody": "حذّر مجلس محافظة بغداد من غرامات تصل إلى 5 ملايين دينار بحق أصحاب المولدات المخالفين للتسعيرة، مع إلزامهم بلوحات أسعار ووصولات رسمية.",
                "bigStat": {"value": "5 ملايين د.ع", "label": "Max fine for overcharging",
                            "arabicLabel": "أقصى غرامة أعلنها مجلس محافظة بغداد بحق أصحاب المولدات المخالفين للتسعيرة الرسمية (مجلس محافظة بغداد)"},
                "supportingStats": [
                    {"label": "الغرامة", "value": "5 ملايين"},
                    {"label": "إلزام", "value": "لوحة أسعار"},
                    {"label": "إلزام", "value": "وصل رسمي"},
                ],
                "broll": img(s, "broll_3.jpg"), "brolls": [img(s, "broll_3.jpg")],
                "brollType": "image", "accent": "#D72638", "brollSource": "Baghdad Provincial Council · 2026",
            },
        ],
        "sources": [
            {"name": "Baghdad Governorate", "domain": "baghdad.gov.iq"},
            {"name": "Council of Ministers", "domain": "pmo.iq"},
            {"name": "Baghdad Provincial Council", "domain": "baghdad.gov.iq"},
        ],
        "arabicTicker": [
            "محافظة بغداد تحدد تسعيرة تموز عند 10,000 دينار للأمبير بالتشغيل الذهبي (محافظة بغداد)",
            "5,000 دينار للأمبير في مناطق الجباية وإلغاء التشغيل الليلي بالكامل (محافظة بغداد)",
            "مجلس الوزراء: زيت غاز مجاني لأصحاب المولدات بواقع 45 لتراً لكل كيلوفولت أمبير في تموز وآب (مجلس الوزراء)",
            "القرار يشترط ألا تقل ساعات التجهيز عن 20 ساعة يومياً (مجلس الوزراء)",
            "مجلس محافظة بغداد: غرامات تصل إلى 5 ملايين دينار بحق المخالفين للتسعيرة (مجلس محافظة بغداد)",
        ],
    },
    "v11": {
        "kicker": "عاجل",
        "hookHeadline": "شكد تدفع للأمبير هالشهر؟",
        "voText": "حدّدت محافظة بغداد تسعيرة المولدات الأهلية لشهر تموز عند عشرة آلاف دينار للأمبير الواحد بالتشغيل الذهبي، وخمسة آلاف دينار في مناطق الجباية، مع إلغاء التشغيل الليلي بالكامل. وكان مجلس الوزراء قد وافق على تجهيز أصحاب المولدات بزيت الغاز مجاناً بواقع خمسة وأربعين لتراً لكل كيلوفولت أمبير خلال تموز وآب، على ألا تقل ساعات التجهيز عن عشرين ساعة يومياً. ويحذّر مجلس محافظة بغداد من غرامات تصل إلى خمسة ملايين دينار بحق المخالفين للتسعيرة. فشكد تدفع للأمبير هذا الشهر؟",
        "endQuestion": "شكد تدفع للأمبير هذا الشهر؟",
        "sourcesLine": "المصادر: محافظة بغداد · مجلس الوزراء · مجلس محافظة بغداد",
        "statPops": [
            {"value": "10,000 د.ع", "label": "سعر الأمبير", "matchWord": "عشرة"},
            {"value": "20 ساعة", "label": "حد أدنى للتجهيز", "matchWord": "عشرين"},
            {"value": "5 ملايين", "label": "غرامة المخالفين", "matchWord": "ملايين"},
        ],
    },
    "caption": """سعر الأمبير في بغداد لشهر تموز — 10 آلاف والتشغيل الليلي ملغى

وقود مجاني لأصحاب المولدات و20 ساعة تجهيز كحد أدنى.

شكد تدفع للأمبير هذا الشهر؟

المصادر: محافظة بغداد، مجلس الوزراء
#العراق #بغداد #الكهرباء #المولدات #سعر_الأمبير
@photonect.news
""",
}

# ─────────────────────────────────────────────────────────────────────────
# 4 — US IMPORTS ZERO IRAQI CRUDE  (P2 · V10 SILENT CONTROL · C)
# ─────────────────────────────────────────────────────────────────────────
s = f"{DATE}-us-zero-crude"
SLUGS[s] = {
    "bucket": "world_energy",
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/mood_cinematic.mp3", "topicBucket": "world_energy", "variant": "C",
        "breaking": {
            "arabicKicker": "نفط · تصدير",
            "arabicHeadline": "أمريكا لم تستورد نفطاً عراقياً 4 أسابيع",
            "englishSubhead": "US IMPORTS ZERO IRAQI CRUDE FOR A FOURTH STRAIGHT WEEK — EIA",
            "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
        },
        "beats": [
            {
                "label": "ماذا يحدث؟",
                "arabicHeading": "صفر برميل إلى الولايات المتحدة",
                "arabicBody": "لم تستورد الولايات المتحدة أي نفط خام عراقي في الأسبوع المنتهي في 17 تموز، للأسبوع الرابع على التوالي، بحسب إدارة معلومات الطاقة الأمريكية.",
                "bigStat": {"value": "0 bpd", "label": "Iraqi crude to the US",
                            "arabicLabel": "معدل استيراد الولايات المتحدة من النفط الخام العراقي في الأسبوع المنتهي في 17 تموز 2026 (إدارة معلومات الطاقة الأمريكية)"},
                "supportingStats": [
                    {"label": "الأسبوع", "value": "المنتهي 17 تموز"},
                    {"label": "المعدل", "value": "0 برميل"},
                    {"label": "على التوالي", "value": "4 أسابيع"},
                ],
                "broll": img(s, "broll_1.jpg"), "brolls": [img(s, "broll_1.jpg")],
                "brollType": "image", "accent": "#FFC217", "brollSource": "EIA · 2026",
            },
            {
                "label": "لماذا يهم؟",
                "arabicHeading": "كان 71 ألف برميل يومياً",
                "arabicBody": "بلغ المعدل 71,000 برميل يومياً في الأسبوع المنتهي في 19 حزيران قبل أن يتوقف تماماً على مدى الأسابيع الأربعة التالية، بحسب الإدارة.",
                "bigStat": {"value": "71,000 bpd", "label": "Rate before the halt",
                            "arabicLabel": "معدل استيراد الولايات المتحدة من الخام العراقي في الأسبوع المنتهي في 19 حزيران 2026 قبل التوقف (إدارة معلومات الطاقة الأمريكية)"},
                "supportingStats": [
                    {"label": "19 حزيران", "value": "71,000 ب/ي"},
                    {"label": "17 تموز", "value": "0 ب/ي"},
                    {"label": "الحالة", "value": "توقف تام"},
                ],
                "broll": img(s, "broll_2.jpg"), "brolls": [img(s, "broll_2.jpg")],
                "brollType": "image", "accent": "#FF6B3D", "brollSource": "EIA · 2026",
            },
            {
                "label": "ماذا بعد؟",
                "arabicHeading": "كندا تتصدر موردي الأمريكيين",
                "arabicBody": "تصدّرت كندا موردي الخام للولايات المتحدة بـ3.635 مليون برميل يومياً، تلتها فنزويلا بـ688,000 والمكسيك بـ480,000، فيما سجّلت السعودية ونيجيريا صفراً أيضاً.",
                "bigStat": {"value": "3.635M bpd", "label": "Canada — top US supplier",
                            "arabicLabel": "معدل توريد كندا من النفط الخام إلى الولايات المتحدة في الأسبوع المنتهي في 17 تموز 2026 (إدارة معلومات الطاقة الأمريكية)"},
                "supportingStats": [
                    {"label": "كندا", "value": "3.635 مليون"},
                    {"label": "فنزويلا", "value": "688,000"},
                    {"label": "المكسيك", "value": "480,000"},
                ],
                "broll": img(s, "broll_3.jpg"), "brolls": [img(s, "broll_3.jpg")],
                "brollType": "image", "accent": "#D72638", "brollSource": "EIA · 2026",
            },
        ],
        "sources": [
            {"name": "Shafaq News", "domain": "shafaq.com"},
            {"name": "US Energy Information Administration", "domain": "eia.gov"},
        ],
        "arabicTicker": [
            "الولايات المتحدة لم تستورد أي نفط خام عراقي في الأسبوع المنتهي في 17 تموز (إدارة معلومات الطاقة الأمريكية)",
            "الأسبوع الرابع على التوالي عند صفر برميل (إدارة معلومات الطاقة الأمريكية)",
            "المعدل كان 71,000 برميل يومياً في الأسبوع المنتهي في 19 حزيران (إدارة معلومات الطاقة الأمريكية)",
            "كندا تتصدر الموردين بـ3.635 مليون برميل يومياً تلتها فنزويلا بـ688,000 (إدارة معلومات الطاقة الأمريكية)",
            "السعودية ونيجيريا سجّلتا صفراً أيضاً في الأسبوع نفسه (إدارة معلومات الطاقة الأمريكية)",
        ],
    },
    "v11": None,  # silent V10 control
    "caption": """أمريكا ما استوردت ولا برميل نفط عراقي — شنو صار؟

الأسبوع الرابع على التوالي عند صفر، بعد 71 ألف برميل يومياً في حزيران.

شنو يهمك أكثر: سعر النفط لو سعر الدولار؟

المصادر: شفق نيوز، إدارة معلومات الطاقة
#العراق #النفط #أوبك #اقتصاد
@photonect.news
""",
}

# ─────────────────────────────────────────────────────────────────────────
# 5 — NON-OIL REVENUE HITS RECORD 16%  (P1 · V11 · B)
# ─────────────────────────────────────────────────────────────────────────
s = f"{DATE}-nonoil-revenue-16"
SLUGS[s] = {
    "bucket": "iraq_economy",
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/mood_orchestral.mp3", "topicBucket": "iraq_economy", "variant": "B",
        "breaking": {
            "arabicKicker": "إيرادات · ضرائب",
            "arabicHeadline": "16% من دخل الدولة… مو من النفط",
            "englishSubhead": "NON-OIL REVENUE HITS A RECORD 16% OF IRAQ'S STATE INCOME",
            "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
        },
        "beats": [
            {
                "label": "ماذا يحدث؟",
                "arabicHeading": "أعلى نسبة غير نفطية منذ سنوات",
                "arabicBody": "بلغت الإيرادات غير النفطية 16% من إجمالي دخل الدولة خلال أيار وحزيران، وهي الأعلى منذ سنوات، بحسب مرصد صدى العراق نقلاً عن شفق نيوز.",
                "bigStat": {"value": "16%", "label": "Non-oil share of state income",
                            "arabicLabel": "حصة الإيرادات غير النفطية من إجمالي إيرادات الدولة خلال أيار وحزيران 2026 (مرصد صدى العراق)"},
                "supportingStats": [
                    {"label": "الحصة", "value": "16%"},
                    {"label": "المدة", "value": "أيار وحزيران"},
                    {"label": "المصدر", "value": "مرصد صدى العراق"},
                ],
                "broll": img(s, "broll_1.jpg"), "brolls": [img(s, "broll_1.jpg")],
                "brollType": "image", "accent": "#FFC217", "brollSource": "Echo Iraq Observatory · 2026",
            },
            {
                "label": "لماذا يهم؟",
                "arabicHeading": "كانت أقل من 5% قبل سنوات",
                "arabicBody": "كانت الإيرادات غير النفطية أقل من 5% من دخل الدولة، ثم ارتفعت إلى نحو 10% في عهدي الكاظمي والسوداني، بحسب المرصد.",
                "bigStat": {"value": "5% → 16%", "label": "The shift in non-oil share",
                            "arabicLabel": "تطور حصة الإيرادات غير النفطية من أقل من 5% تاريخياً إلى 16% في أيار وحزيران 2026 (مرصد صدى العراق)"},
                "supportingStats": [
                    {"label": "تاريخياً", "value": "أقل من 5%"},
                    {"label": "الكاظمي", "value": "~10%"},
                    {"label": "اليوم", "value": "16%"},
                ],
                "broll": img(s, "broll_2.jpg"), "brolls": [img(s, "broll_2.jpg")],
                "brollType": "image", "accent": "#FF6B3D", "brollSource": "Echo Iraq Observatory · 2026",
            },
            {
                "label": "ماذا بعد؟",
                "arabicHeading": "من ضرائب السلع والخدمات",
                "arabicBody": "تأتي هذه الإيرادات من ضرائب السلع ورسوم الإنتاج ورسوم الخدمات وضرائب الدخل والثروة، فيما شكّلت تحويلات إقليم كردستان نحو 5.5% منها.",
                "bigStat": {"value": "5.5%", "label": "Kurdistan share of non-oil",
                            "arabicLabel": "حصة الإيرادات المحوّلة من إقليم كردستان من إجمالي الإيرادات غير النفطية (مرصد صدى العراق)"},
                "supportingStats": [
                    {"label": "كردستان", "value": "5.5%"},
                    {"label": "المصدر", "value": "ضرائب السلع"},
                    {"label": "وأيضاً", "value": "رسوم الخدمات"},
                ],
                "broll": img(s, "broll_3.jpg"), "brolls": [img(s, "broll_3.jpg")],
                "brollType": "image", "accent": "#D72638", "brollSource": "Echo Iraq Observatory · 2026",
            },
        ],
        "sources": [
            {"name": "Shafaq News", "domain": "shafaq.com"},
            {"name": "Echo Iraq Observatory", "domain": "shafaq.com"},
        ],
        "arabicTicker": [
            "الإيرادات غير النفطية تبلغ 16% من إجمالي دخل الدولة خلال أيار وحزيران (مرصد صدى العراق)",
            "أعلى مساهمة لمصادر خارج قطاع النفط منذ سنوات (مرصد صدى العراق)",
            "كانت أقل من 5% تاريخياً قبل أن ترتفع إلى نحو 10% في عهدي الكاظمي والسوداني (مرصد صدى العراق)",
            "مصادرها: ضرائب السلع ورسوم الإنتاج ورسوم الخدمات وضرائب الدخل والثروة (مرصد صدى العراق)",
            "تحويلات إقليم كردستان شكّلت نحو 5.5% من الإيرادات غير النفطية (مرصد صدى العراق)",
        ],
    },
    "v11": {
        "kicker": "عاجل",
        "hookHeadline": "16% من دخل الدولة… مو نفط",
        "voText": "أعلن مرصد صدى العراق أن الإيرادات غير النفطية بلغت ستة عشر بالمئة من إجمالي دخل الدولة العراقية خلال شهري أيار وحزيران، وهي الأعلى منذ سنوات، وذلك بحسب ما نقلته شفق نيوز. وكانت هذه الإيرادات أقل من خمسة بالمئة تاريخياً قبل أن ترتفع إلى نحو عشرة بالمئة في عهدي الكاظمي والسوداني. وتأتي من ضرائب السلع ورسوم الإنتاج ورسوم الخدمات وضرائب الدخل والثروة، فيما شكّلت تحويلات إقليم كردستان نحو خمسة ونصف بالمئة منها. فشنو الشي اللي زاد سعره عليك هالسنة؟",
        "endQuestion": "شنو الشي اللي زاد سعره عليك هالسنة؟",
        "sourcesLine": "المصادر: شفق نيوز · مرصد صدى العراق",
        "statPops": [
            {"value": "16%", "label": "من دخل الدولة", "matchWord": "ستة"},
            {"value": "أقل من 5%", "label": "قبل سنوات", "matchWord": "تاريخياً"},
            {"value": "5.5%", "label": "حصة كردستان", "matchWord": "كردستان"},
        ],
    },
    "caption": """الإيرادات غير النفطية في العراق — 16% وأعلى رقم منذ سنوات

ضرائب السلع ورسوم الخدمات صارت تغذّي خزينة الدولة أكثر من أي وقت.

شنو الشي اللي زاد سعره عليك هالسنة؟

المصادر: شفق نيوز، مرصد صدى العراق
#العراق #الاقتصاد #الضرائب #إيرادات
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
        stamp = dict(STAMP)
        stamp.update({"manual": True, "source": "kie-nano-banana-pro", "date": DATE})
        (d / "media-stamp.json").write_text(
            json.dumps(stamp, ensure_ascii=False) + "\n", encoding="utf-8")
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
        print(f"  ✓ {slug}  ({'V11' if cfg.get('v11') else 'V10 control'})")
    print(f"\n== {len(SLUGS)} slugs written for {DATE} ==")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
