#!/usr/bin/env python3
"""Author the 2026-07-29 Photonect NEWS slate.

5 slugs (Iraq/MENA money-power lens). Posting order = alphabetical slug order,
which is what `post-to-uploadpost.py --spread` maps onto the Baghdad evening slots:

  1 brent-basra-gap              mena_geopolitics  V11  A  18:00
  2 dollar-back-over-150         iraq_domestic     V11  B  19:45  (daily dollar anchor)
  3 female-volleyball-olympics   wildcard          V10  C  21:15  <- silent control, no v11
  4 graft-salahaddin-cash        iraq_domestic     V11  A  22:30
  5 small-change-gum             iraq_domestic     V11  B  23:45

Directional shift vs 2026-07-28: yesterday was "a month of movement in your
pocket". Today is "who collects the war premium" — US-Saudi strikes at dawn on
Wednesday lift world crude while Iraq's own export grade FALLS, the dinar's
month-long rally reverses back over 150,000, 2.5bn dinars booked as your salary
difference turns up in a director's house, and the 250/500 note disappears so
the change comes back as chewing gum.

The day's dominant event (the strikes) is deliberately covered through its money
consequence rather than as a casualty reel: the PMF toll is preliminary and
"subject to revision", so it is attributed, never headlined, and never a bigStat.

Banned this slate (per fact sheet):
  * the OPEC basket print ($88.91 / -8.54%) — implausible against Brent +3.72%
    on the same feed, and Baghdad Today omits it entirely
  * Basra's -17.67% move (rejected 2026-07-28, still single-outlet)
  * any small-note circulation count (795m/818m/147m/145.4m trace only to
    dinar-speculator aggregator blogs)
  * the 29 June 156,750 dinar print — not re-verified today, so the "month" arc
    is stated only as a direction, never as a second number
  * Iraqi crude export volumes (sources irreconcilable: 3.543m / 1.5m / <800k bpd)
  * the 51.8C heat / CCHF outbreak / Khor Mor shutdown packages — all stale
  * the Ukraine "false flag" claim — unproven by the official who made it
  * MoU contents for the cancelled Riyadh visit — never published

brollSource is «صورة توضيحية · Photonect AI» slate-wide: schema.ts documents that
field as a photo-credit chip and Beat.tsx paints it over every beat, while
media-stamp.json records 100% of the imagery as generated. Crediting Reuters/AP
for a generated frame is misattribution — claim attribution lives in arabicBody,
bigStat.arabicLabel, the ticker and the Sources scene instead.

Writes per slug: .meta/props.json, caption.txt, .meta/media-stamp.json, and (for
the 4 voiced) .meta/v11-brief.json. Western numerals on-screen; voText spells
numbers in words (MSA newscast register). No Persian yeh/kaf (grep-guarded).
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "data" / "posts"
DATE = "2026-07-29"
DATE_LABEL = "JUL 29 • 2026"
AR_DATE = "29 يوليو 2026"
HANDLE = "@photonect.news"

CREDIT = "صورة توضيحية · Photonect AI"

STAMP = {
    "hunted_at": "2026-07-29T11:30:00+00:00",
    "manual": True,
    "source": "higgsfield nano-banana-pro (KIE 402 — credits exhausted)",
    "date": "2026-07-29",
    "note": (
        "KIE reported a credit balance of -5.5 for the third consecutive day, so the "
        "whole slate was generated on Higgsfield's nano_banana_pro (same Nano Banana "
        "Pro model, different vendor) at 9:16/2K. Every image Read-verified by hand "
        "before acceptance. No stock imagery anywhere in the slate."
    ),
}


def img(slug, n):
    return f"images/news/{slug}/{n}"


SLUGS = {}

# ─────────────────────────────────────────────────────────────────────────
# 1 — WORLD OIL UP, IRAQ'S OWN CRUDE DOWN  (mena_geopolitics · V11 · A · LEAD)
# ─────────────────────────────────────────────────────────────────────────
s = f"{DATE}-brent-basra-gap"
SLUGS[s] = {
    "bucket": "mena_geopolitics",
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/mood_newsroom.mp3", "topicBucket": "mena_geopolitics", "variant": "A",
        "breaking": {
            "arabicKicker": "نفط · موازنة",
            "arabicHeadline": "النفط العالمي صعد… وخام العراق نزل",
            "englishSubhead": "BRENT UP 3.72% TO $87.22 AFTER STRIKES INSIDE IRAQ WHILE BASRA HEAVY FELL 0.90% TO $53.70",
            "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
        },
        "beats": [
            {
                "label": "ماذا يحدث؟",
                "arabicHeading": "برنت 87.22 دولاراً… والبصرة 53.70",
                "arabicBody": "صعد خام برنت 3.72% إلى 87.22 دولاراً للبرميل الأربعاء، بينما نزل خام البصرة الثقيل 0.90% إلى 53.70 دولاراً، بحسب شفق نيوز وبغداد اليوم.",
                "bigStat": {"value": "$87.22", "label": "Brent crude on Wednesday",
                            "arabicLabel": "سعر خام برنت الأربعاء 29 تموز 2026 بعد صعود 3.72% أي 3.13 دولار للبرميل (شفق نيوز · بغداد اليوم)"},
                "supportingStats": [
                    {"label": "برنت", "value": "+3.72%"},
                    {"label": "غرب تكساس", "value": "82.01$"},
                    {"label": "البصرة الثقيل", "value": "−0.90%"},
                ],
                "broll": img(s, "broll_1.jpg"), "brolls": [img(s, "broll_1.jpg")],
                "brollType": "image", "accent": "#FFC217", "brollSource": CREDIT,
            },
            {
                "label": "لماذا يهم؟",
                "arabicHeading": "33.52 دولاراً فرق بين السعرين",
                "arabicBody": "الفرق بين سعر برنت وخام البصرة الثقيل بلغ 33.52 دولاراً للبرميل، والموازنة العراقية تُسعَّر على خام البصرة لا على برنت.",
                "bigStat": {"value": "$33.52", "label": "Brent minus Basra Heavy",
                            "arabicLabel": "الفرق بين سعر خام برنت 87.22 دولاراً وخام البصرة الثقيل 53.70 دولاراً للبرميل الأربعاء، وهو حاصل طرح السعرين المعلنين (شفق نيوز · بغداد اليوم)"},
                "supportingStats": [
                    {"label": "برنت", "value": "87.22$"},
                    {"label": "البصرة الثقيل", "value": "53.70$"},
                    {"label": "الفرق", "value": "33.52$"},
                ],
                "broll": img(s, "broll_2.jpg"), "brolls": [img(s, "broll_2.jpg")],
                "brollType": "image", "accent": "#FF6B3D", "brollSource": CREDIT,
            },
            {
                "label": "ماذا بعد؟",
                "arabicHeading": "ضربات فجر الأربعاء في 7 محافظات",
                "arabicBody": "جاء صعود الأسعار بعد ضربات أمريكية وسعودية فجر الأربعاء على مواقع للحشد الشعبي في سبع محافظات، بحسب 964 والجزيرة.",
                "bigStat": {"value": "7", "label": "Governorates struck at dawn",
                            "arabicLabel": "عدد المحافظات التي استهدفتها ضربات أمريكية وسعودية فجر الأربعاء 29 تموز 2026: بغداد وواسط ونينوى والبصرة وكركوك وكربلاء وديالى (964 · الجزيرة)"},
                "supportingStats": [
                    {"label": "المحافظات", "value": "7"},
                    {"label": "مخزونات أمريكا", "value": "−3.3 مليون"},
                    {"label": "غرب تكساس", "value": "+3.47%"},
                ],
                "broll": img(s, "broll_3.jpg"), "brolls": [img(s, "broll_3.jpg")],
                "brollType": "image", "accent": "#D72638", "brollSource": CREDIT,
            },
        ],
        "sources": [
            {"name": "Shafaq News", "domain": "shafaq.com"},
            {"name": "Baghdad Today", "domain": "baghdadtoday.news"},
            {"name": "964media", "domain": "964media.com"},
        ],
        "arabicTicker": [
            "خام برنت صعد 3.72% أي 3.13 دولار إلى 87.22 دولاراً للبرميل الأربعاء 29 تموز 2026 (شفق نيوز · بغداد اليوم)",
            "خام غرب تكساس الوسيط صعد 3.47% أي 2.75 دولار إلى 82.01 دولاراً للبرميل (شفق نيوز · بغداد اليوم)",
            "خام البصرة الثقيل نزل 0.90% إلى 53.70 دولاراً، وخام البصرة المتوسط نزل 0.87% إلى 56.00 دولاراً (شفق نيوز · بغداد اليوم)",
            "الفرق بين برنت وخام البصرة الثقيل 33.52 دولاراً للبرميل، وهو حاصل طرح السعرين المعلنين",
            "مخزونات النفط الأمريكية نزلت نحو 3.3 مليون برميل في الأسبوع المنتهي 24 تموز (معهد البترول الأمريكي · شفق نيوز)",
            "الضربات الأمريكية والسعودية فجر الأربعاء استهدفت مواقع للحشد الشعبي في سبع محافظات (964 · الجزيرة)",
            "شفت أسعار السوق ارتفعت هالأسبوع؟",
        ],
    },
    "v11": {
        "kicker": "عاجل",
        "hookHeadline": "النفط صعد… وخام العراق نزل",
        "voText": "صعد خام برنت يوم الأربعاء إلى سبعة وثمانين دولاراً واثنين وعشرين سنتاً للبرميل، وصعد خام غرب تكساس إلى اثنين وثمانين دولاراً وسنت واحد، بحسب شفق نيوز وبغداد اليوم. وفي الوقت نفسه نزل خام البصرة الثقيل إلى ثلاثة وخمسين دولاراً وسبعين سنتاً، ونزل خام البصرة المتوسط إلى ستة وخمسين دولاراً. والفرق بين برنت وخام البصرة الثقيل بلغ ثلاثة وثلاثين دولاراً واثنين وخمسين سنتاً للبرميل، والموازنة العراقية تُسعَّر على خام البصرة. فشفت أسعار السوق ارتفعت هالأسبوع؟",
        "endQuestion": "شفت أسعار السوق ارتفعت هالأسبوع؟",
        "sourcesLine": "المصادر: شفق نيوز · بغداد اليوم · 964",
        "statPops": [
            {"value": "$87.22", "label": "برنت الأربعاء", "matchWord": "سبعة"},
            {"value": "$33.52", "label": "الفرق عن خام البصرة", "matchWord": "وثلاثين"},
        ],
    },
    "caption": """أسعار النفط اليوم — العالم صعد وخام العراق نزل

برنت 87.22 دولاراً… وخام البصرة الثقيل 53.70.

شفت أسعار السوق ارتفعت هالأسبوع؟

المصادر: شفق نيوز، بغداد اليوم، 964
#العراق #النفط #موازنة_العراق #خام_البصرة
@photonect.news
""",
}

# ─────────────────────────────────────────────────────────────────────────
# 2 — DOLLAR BACK OVER 150,000  (iraq_domestic · V11 · B · DAILY ANCHOR)
# ─────────────────────────────────────────────────────────────────────────
s = f"{DATE}-dollar-back-over-150"
SLUGS[s] = {
    "bucket": "iraq_domestic",
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/mood_cinematic.mp3", "topicBucket": "iraq_domestic", "variant": "B",
        "breaking": {
            "arabicKicker": "دولار · سوق",
            "arabicHeadline": "الدولار رجع فوق 150 ألف دينار",
            "englishSubhead": "DOLLAR BACK ABOVE 150,000 IQD PER $100 IN BAGHDAD ON 29 JULY, UP FROM 149,900",
            "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
        },
        "beats": [
            {
                "label": "ماذا يحدث؟",
                "arabicHeading": "150,300 دينار لكل 100 دولار",
                "arabicBody": "سجّلت بورصتا الكفاح والحارثية في بغداد 150,300 دينار لكل 100 دولار صباح الأربعاء، صعوداً من 149,900 ديناراً في الجلسة السابقة، بحسب شفق نيوز.",
                "bigStat": {"value": "150,300", "label": "IQD per $100 Wednesday morning",
                            "arabicLabel": "سعر 100 دولار في بورصتي الكفاح والحارثية ببغداد صباح الأربعاء 29 تموز 2026، صعوداً من 149,900 ديناراً في الجلسة السابقة (شفق نيوز)"},
                "supportingStats": [
                    {"label": "اليوم", "value": "150,300"},
                    {"label": "الجلسة السابقة", "value": "149,900"},
                    {"label": "الفرق", "value": "+400"},
                ],
                "broll": img(s, "broll_1.jpg"), "brolls": [img(s, "broll_1.jpg")],
                "brollType": "image", "accent": "#FFC217", "brollSource": CREDIT,
            },
            {
                "label": "لماذا يهم؟",
                "arabicHeading": "محال الصيرفة تبيع بـ150,750",
                "arabicBody": "في محال الصيرفة ببغداد سعر البيع 150,750 ديناراً والشراء 149,750، وفي أربيل البيع 150,350 والشراء 150,250، بحسب شفق نيوز.",
                "bigStat": {"value": "150,750", "label": "Baghdad shop selling price",
                            "arabicLabel": "سعر بيع 100 دولار في محال الصيرفة ببغداد الأربعاء 29 تموز 2026، مقابل سعر شراء 149,750 ديناراً (شفق نيوز)"},
                "supportingStats": [
                    {"label": "بغداد بيع", "value": "150,750"},
                    {"label": "بغداد شراء", "value": "149,750"},
                    {"label": "أربيل بيع", "value": "150,350"},
                ],
                "broll": img(s, "broll_2.jpg"), "brolls": [img(s, "broll_2.jpg")],
                "brollType": "image", "accent": "#4CC9F0", "brollSource": CREDIT,
            },
            {
                "label": "ماذا بعد؟",
                "arabicHeading": "فوق حدّ 150 ألفاً من جديد",
                "arabicBody": "عاد سعر 100 دولار فوق حدّ 150 ألف دينار في بورصتي بغداد، بالتوازي مع ضربات فجر الأربعاء في سبع محافظات، بحسب شفق نيوز و964.",
                "bigStat": {"value": "150,000", "label": "The line crossed back over",
                            "arabicLabel": "حدّ الـ150 ألف دينار لكل 100 دولار الذي عاد سعر السوق الموازية فوقه في بورصتي الكفاح والحارثية صباح الأربعاء 29 تموز 2026 (شفق نيوز)"},
                "supportingStats": [
                    {"label": "الحدّ", "value": "150,000"},
                    {"label": "السعر اليوم", "value": "150,300"},
                    {"label": "أربيل شراء", "value": "150,250"},
                ],
                "broll": img(s, "broll_3.jpg"), "brolls": [img(s, "broll_3.jpg")],
                "brollType": "image", "accent": "#D72638", "brollSource": CREDIT,
            },
        ],
        "sources": [
            {"name": "Shafaq News", "domain": "shafaq.com"},
            {"name": "Al-Kifah & Al-Harithiya exchanges", "domain": "shafaq.com"},
            {"name": "964media", "domain": "964media.com"},
        ],
        "arabicTicker": [
            "بورصتا الكفاح والحارثية ببغداد سجّلتا 150,300 دينار لكل 100 دولار صباح الأربعاء 29 تموز 2026 (شفق نيوز)",
            "السعر في الجلسة السابقة كان 149,900 ديناراً لكل 100 دولار، أي صعود 400 دينار (شفق نيوز)",
            "محال الصيرفة في بغداد: بيع 150,750 ديناراً وشراء 149,750 ديناراً لكل 100 دولار (شفق نيوز)",
            "أربيل: بيع 150,350 ديناراً وشراء 150,250 ديناراً لكل 100 دولار (شفق نيوز)",
            "بذلك عاد سعر السوق الموازية فوق حدّ 150 ألف دينار بعد فترة نزول (شفق نيوز)",
            "الصعود جاء بالتوازي مع ضربات أمريكية وسعودية فجر الأربعاء في سبع محافظات (964)",
            "بيش اشتريت الدولار اليوم؟",
        ],
    },
    "v11": {
        "kicker": "عاجل",
        "hookHeadline": "الدولار رجع فوق 150 ألف",
        "voText": "سجّلت بورصتا الكفاح والحارثية في بغداد مئة وخمسين ألفاً وثلاثمئة دينار لكل مئة دولار صباح الأربعاء، صعوداً من مئة وتسعة وأربعين ألفاً وتسعمئة دينار في الجلسة السابقة، بحسب شفق نيوز. وفي محال الصيرفة ببغداد سعر البيع مئة وخمسون ألفاً وسبعمئة وخمسون ديناراً، وسعر الشراء مئة وتسعة وأربعين ألفاً وسبعمئة وخمسين. وفي أربيل سعر البيع مئة وخمسون ألفاً وثلاثمئة وخمسون ديناراً. بذلك عاد السعر فوق حدّ مئة وخمسين ألفاً، بالتوازي مع ضربات فجر الأربعاء في سبع محافظات. فبيش اشتريت الدولار اليوم؟",
        "endQuestion": "بيش اشتريت الدولار اليوم؟",
        "sourcesLine": "المصادر: بورصتا الكفاح والحارثية · شفق نيوز · 964",
        "statPops": [
            {"value": "150,300", "label": "لكل 100 دولار اليوم", "matchWord": "وثلاثمئة"},
            {"value": "150,750", "label": "بيع محال الصيرفة", "matchWord": "وسبعمئة"},
        ],
    },
    "caption": """سعر الدولار اليوم في بغداد — رجع فوق 150 ألف دينار

150,300 لكل 100 دولار في بورصتي الكفاح والحارثية.

بيش اشتريت الدولار اليوم؟

المصادر: بورصتا الكفاح والحارثية، شفق نيوز
#العراق #الدولار #سعر_الصرف #الدينار_العراقي
@photonect.news
""",
}

# ─────────────────────────────────────────────────────────────────────────
# 3 — WOMEN'S VOLLEYBALL, ROAD TO LA 2028  (wildcard · V10.1 CONTROL · C)
# ─────────────────────────────────────────────────────────────────────────
s = f"{DATE}-female-volleyball-olympics"
SLUGS[s] = {
    "bucket": "wildcard",
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/music_03.mp3", "topicBucket": "wildcard", "variant": "C",
        "breaking": {
            "arabicKicker": "رياضة · طائرة",
            "arabicHeadline": "العراق بمجموعة الصين وإيران… والفائز إلى الأولمبياد",
            "englishSubhead": "IRAQ DRAWN IN POOL A WITH CHINA, IRAN AND CHINESE TAIPEI; THE CHAMPION QUALIFIES FOR LA 2028",
            "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
        },
        "beats": [
            {
                "label": "ماذا يحدث؟",
                "arabicHeading": "العراق في المجموعة الأولى",
                "arabicBody": "أوقعت قرعة 28 تموز في تيانجين منتخب العراق للكرة الطائرة للنساء في المجموعة الأولى مع الصين وإيران وتايبيه الصينية، بحسب صحيفة الشعب.",
                "bigStat": {"value": "12", "label": "Teams in the championship",
                            "arabicLabel": "عدد المنتخبات المشاركة في بطولة آسيا للكرة الطائرة للنساء 2026 موزعة على ثلاث مجموعات (الاتحاد الآسيوي للكرة الطائرة)"},
                "supportingStats": [
                    {"label": "المجموعة", "value": "الأولى"},
                    {"label": "المنافسون", "value": "الصين وإيران"},
                    {"label": "وكذلك", "value": "تايبيه الصينية"},
                ],
                "broll": img(s, "broll_1.jpg"), "brolls": [img(s, "broll_1.jpg")],
                "brollType": "image", "accent": "#4CC9F0", "brollSource": CREDIT,
            },
            {
                "label": "لماذا يهم؟",
                "arabicHeading": "21–30 آب في قاعة تيانجين",
                "arabicBody": "تُقام البطولة بين 21 و30 آب 2026 في قاعة تيانجين بمشاركة 12 منتخباً في ثلاث مجموعات، ويتأهل أول اثنين من كل مجموعة إلى ربع النهائي.",
                "bigStat": {"value": "21–30 آب", "label": "Tournament window",
                            "arabicLabel": "موعد بطولة آسيا للكرة الطائرة للنساء 2026 في قاعة تيانجين بالصين، بمشاركة 12 منتخباً في ثلاث مجموعات (الاتحاد الآسيوي للكرة الطائرة)"},
                "supportingStats": [
                    {"label": "البداية", "value": "21 آب"},
                    {"label": "النهاية", "value": "30 آب"},
                    {"label": "المنتخبات", "value": "12"},
                ],
                "broll": img(s, "broll_2.jpg"), "brolls": [img(s, "broll_2.jpg")],
                "brollType": "image", "accent": "#FFC217", "brollSource": CREDIT,
            },
            {
                "label": "ماذا بعد؟",
                "arabicHeading": "البطل يتأهل مباشرة إلى 2028",
                "arabicBody": "يتأهل بطل البطولة مباشرة إلى أولمبياد لوس أنجلوس 2028، ودخل العراق قائمة المشاركين بعد انسحاب لبنان، بحسب صحيفة الشعب.",
                "bigStat": {"value": "2028", "label": "Direct Olympic berth for the champion",
                            "arabicLabel": "دورة الألعاب الأولمبية في لوس أنجلوس التي يتأهل إليها بطل بطولة آسيا للكرة الطائرة للنساء 2026 مباشرة (الاتحاد الآسيوي للكرة الطائرة · صحيفة الشعب)"},
                "supportingStats": [
                    {"label": "المكافأة", "value": "تأهل مباشر"},
                    {"label": "الأولمبياد", "value": "لوس أنجلوس"},
                    {"label": "السنة", "value": "2028"},
                ],
                "broll": img(s, "broll_3.jpg"), "brolls": [img(s, "broll_3.jpg")],
                "brollType": "image", "accent": "#FF6B3D", "brollSource": CREDIT,
            },
        ],
        "sources": [
            {"name": "People's Daily Online", "domain": "en.people.cn"},
            {"name": "Iraq Sun", "domain": "iraqsun.com"},
            {"name": "Asian Volleyball Confederation", "domain": "asianvolleyball.net"},
        ],
        "arabicTicker": [
            "قرعة 28 تموز 2026 في تيانجين وضعت منتخب العراق للكرة الطائرة للنساء في المجموعة الأولى (صحيفة الشعب · إيراق صن)",
            "المجموعة الأولى تضم الصين المستضيفة وإيران وتايبيه الصينية والعراق (صحيفة الشعب · الاتحاد الآسيوي)",
            "البطولة تُقام بين 21 و30 آب 2026 في قاعة تيانجين (الاتحاد الآسيوي للكرة الطائرة)",
            "12 منتخباً في ثلاث مجموعات، ويتأهل أول اثنين من كل مجموعة مع أفضل ثالثين إلى ربع النهائي (الاتحاد الآسيوي)",
            "بطل البطولة يتأهل مباشرة إلى أولمبياد لوس أنجلوس 2028 (الاتحاد الآسيوي للكرة الطائرة)",
            "العراق دخل قائمة المشاركين بعد انسحاب لبنان (صحيفة الشعب)",
            "راح تتابع مباراة العراق والصين؟",
        ],
    },
    "caption": """منتخب العراق للكرة الطائرة نساء — بمجموعة الصين وإيران

قرعة تيانجين وضعته بالمجموعة الأولى، والبطولة 21–30 آب.

راح تتابع مباراة العراق والصين؟

المصادر: صحيفة الشعب، إيراق صن، الاتحاد الآسيوي للكرة الطائرة
#العراق #الكرة_الطائرة #بطولة_آسيا #رياضة_نسائية
@photonect.news
""",
}

# ─────────────────────────────────────────────────────────────────────────
# 4 — 2.5BN DINARS IN A DIRECTOR'S HOUSE  (iraq_domestic · V11 · A)
# ─────────────────────────────────────────────────────────────────────────
s = f"{DATE}-graft-salahaddin-cash"
SLUGS[s] = {
    "bucket": "iraq_domestic",
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/mood_orchestral.mp3", "topicBucket": "iraq_domestic", "variant": "A",
        "breaking": {
            "arabicKicker": "فساد · ضبط",
            "arabicHeadline": "2.5 مليار دينار في بيت… باسم فروق رواتب",
            "englishSubhead": "INTEGRITY COMMISSION SEIZES 2.5BN IQD ($1.9M) FROM THE HOME OF SALAH AL-DIN'S FORMER ACCOUNTS DIRECTOR",
            "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
        },
        "beats": [
            {
                "label": "ماذا يحدث؟",
                "arabicHeading": "2.5 مليار دينار نقداً في المنزل",
                "arabicBody": "ضبطت هيئة النزاهة الاتحادية بأمر قضائي 2.5 مليار دينار نقداً في منزل مدير قسم حسابات صلاح الدين السابق، بحسب 964 وذي ناشيونال.",
                "bigStat": {"value": "2.5 مليار د.ع", "label": "Cash seized on 28 July",
                            "arabicLabel": "المبلغ النقدي الذي ضبطته هيئة النزاهة الاتحادية بأمر قضائي في منزل مدير قسم حسابات محافظة صلاح الدين السابق في 28 تموز 2026، ويعادل 1.9 مليون دولار بالسعر الرسمي (964 · ذي ناشيونال)"},
                "supportingStats": [
                    {"label": "المبلغ", "value": "2.5 مليار"},
                    {"label": "بالدولار", "value": "1.9 مليون"},
                    {"label": "التاريخ", "value": "28 تموز"},
                ],
                "broll": img(s, "broll_1.jpg"), "brolls": [img(s, "broll_1.jpg")],
                "brollType": "image", "accent": "#D72638", "brollSource": CREDIT,
            },
            {
                "label": "لماذا يهم؟",
                "arabicHeading": "6 عقارات باسم زوجة المتهم",
                "arabicBody": "صُرفت الأموال بصك من مصرف الرافدين بذريعة مستحقات موظفين وفروق رواتب استناداً إلى مستمسكات وهمية، وسُجّلت 6 عقارات باسم زوجة المتهم.",
                "bigStat": {"value": "6", "label": "Properties in the wife's name",
                            "arabicLabel": "عدد العقارات في مجمعات سكنية استثمارية المسجّلة باسم زوجة المتهم بحسب تحقيقات هيئة النزاهة الاتحادية (964 · ذي ناشيونال)"},
                "supportingStats": [
                    {"label": "العقارات", "value": "6"},
                    {"label": "المصرف", "value": "الرافدين"},
                    {"label": "الذريعة", "value": "فروق رواتب"},
                ],
                "broll": img(s, "broll_2.jpg"), "brolls": [img(s, "broll_2.jpg")],
                "brollType": "image", "accent": "#FFC217", "brollSource": CREDIT,
            },
            {
                "label": "ماذا بعد؟",
                "arabicHeading": "موقوف وفق المادة 340",
                "arabicBody": "أُوقف المتهم وفق المادة 340 من قانون العقوبات، وسبق أن أُوقف 47 نائباً ومسؤولاً في أواخر حزيران 2026 في حملة النزاهة، بحسب ذي ناشيونال.",
                "bigStat": {"value": "340", "label": "Penal code article",
                            "arabicLabel": "مادة قانون العقوبات العراقي التي أُوقف المتهم وفقها بحسب هيئة النزاهة الاتحادية (964)"},
                "supportingStats": [
                    {"label": "المادة", "value": "340"},
                    {"label": "موقوفون سابقاً", "value": "47"},
                    {"label": "الجهة", "value": "هيئة النزاهة"},
                ],
                "broll": img(s, "broll_3.jpg"), "brolls": [img(s, "broll_3.jpg")],
                "brollType": "image", "accent": "#FF6B3D", "brollSource": CREDIT,
            },
        ],
        "sources": [
            {"name": "964media", "domain": "964media.com"},
            {"name": "The National", "domain": "thenationalnews.com"},
        ],
        "arabicTicker": [
            "هيئة النزاهة الاتحادية ضبطت بأمر قضائي 2,500,000,000 دينار نقداً في منزل مدير قسم حسابات صلاح الدين السابق في 28 تموز 2026 (964 · ذي ناشيونال)",
            "المبلغ يعادل 1.9 مليون دولار بالسعر الرسمي (964 · ذي ناشيونال)",
            "الأموال تعود إلى صك من مصرف الرافدين صُرف بذريعة مستحقات موظفين وفروق رواتب (964 · ذي ناشيونال)",
            "التحقيقات وجدت 6 عقارات في مجمعات سكنية استثمارية مسجّلة باسم زوجة المتهم (964 · ذي ناشيونال)",
            "المتهم موقوف وفق المادة 340 من قانون العقوبات، ولم تصدر بحقه أحكام حتى الآن (964)",
            "حملة النزاهة أوقفت 47 نائباً ومسؤولاً في أواخر حزيران 2026 (ذي ناشيونال)",
            "فرق راتبك وصلك لو لا؟",
        ],
    },
    "v11": {
        "kicker": "عاجل",
        "hookHeadline": "2.5 مليار دينار في بيت مسؤول",
        "voText": "ضبطت هيئة النزاهة الاتحادية بأمر قضائي ملياريْن وخمسمئة مليون دينار نقداً في منزل مدير قسم حسابات محافظة صلاح الدين السابق، أي ما يعادل مليوناً وتسعمئة ألف دولار بالسعر الرسمي، بحسب 964 وذي ناشيونال. وتعود الأموال إلى صك من مصرف الرافدين صُرف بذريعة مستحقات موظفين وفروق رواتب استناداً إلى مستمسكات وهمية. وسُجّلت ستة عقارات في مجمعات استثمارية باسم زوجة المتهم، وهو موقوف وفق المادة ثلاثمئة وأربعين من قانون العقوبات ولم تصدر بحقه أحكام. ففرق راتبك وصلك لو لا؟",
        "endQuestion": "فرق راتبك وصلك لو لا؟",
        "sourcesLine": "المصادر: 964 · ذي ناشيونال",
        "statPops": [
            {"value": "2.5 مليار د.ع", "label": "ضُبطت نقداً", "matchWord": "وخمسمئة"},
            {"value": "6 عقارات", "label": "باسم زوجة المتهم", "matchWord": "ستة"},
        ],
    },
    "caption": """فساد في صلاح الدين — 2.5 مليار دينار نقداً في بيت مسؤول

الأموال صُرفت بذريعة فروق رواتب موظفين بمستمسكات وهمية.

فرق راتبك وصلك لو لا؟

المصادر: 964، ذي ناشيونال
#العراق #النزاهة #فساد #صلاح_الدين
@photonect.news
""",
}

# ─────────────────────────────────────────────────────────────────────────
# 5 — THE SMALL CHANGE VANISHED  (iraq_domestic · V11 · B)
# ─────────────────────────────────────────────────────────────────────────
s = f"{DATE}-small-change-gum"
SLUGS[s] = {
    "bucket": "iraq_domestic",
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/music_05.mp3", "topicBucket": "iraq_domestic", "variant": "B",
        "breaking": {
            "arabicKicker": "فكة · أسعار",
            "arabicHeadline": "الفكة اختفت… والباقي علك أو تقريب سعر",
            "englishSubhead": "250 AND 500 DINAR NOTES HAVE VANISHED FROM BAGHDAD MARKETS; THE PM'S FINANCIAL ADVISER EXPLAINS WHY",
            "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
        },
        "beats": [
            {
                "label": "ماذا يحدث؟",
                "arabicHeading": "250 و500 دينار اختفت",
                "arabicBody": "اختفت أوراق 250 و500 دينار من أسواق بغداد، ويلجأ التجار إلى تقريب الأسعار أو استبدال المبلغ المتبقي بسلعة صغيرة، بحسب وكالة الصحافة المستقلة.",
                "bigStat": {"value": "250 · 500", "label": "The missing denominations",
                            "arabicLabel": "فئتا العملة الورقية اللتان اختفتا من الأسواق العراقية، ويعوّضهما التجار بتقريب الأسعار أو باستبدال المبلغ المتبقي بسلعة صغيرة (وكالة الصحافة المستقلة)"},
                "supportingStats": [
                    {"label": "الفئات", "value": "250 و500"},
                    {"label": "البديل الأول", "value": "تقريب السعر"},
                    {"label": "البديل الثاني", "value": "سلعة صغيرة"},
                ],
                "broll": img(s, "broll_1.jpg"), "brolls": [img(s, "broll_1.jpg")],
                "brollType": "image", "accent": "#FFC217", "brollSource": CREDIT,
            },
            {
                "label": "لماذا يهم؟",
                "arabicHeading": "عمر الورقة الصغيرة سنة واحدة",
                "arabicBody": "قال مظهر محمد صالح، المستشار المالي لرئيس الوزراء، إن العراق يطبع هذه الفئات ورقاً لا معدناً، وعمر الورقة الصغيرة نحو سنة بسرعة التداول العراقية.",
                "bigStat": {"value": "سنة واحدة", "label": "Life of a small paper note",
                            "arabicLabel": "العمر التقديري للورقة النقدية الصغيرة بسرعة التداول في العراق وفق المعايير الدولية، بحسب المستشار المالي لرئيس الوزراء مظهر محمد صالح (شفق نيوز)"},
                "supportingStats": [
                    {"label": "العمر", "value": "نحو سنة"},
                    {"label": "المادة", "value": "ورق لا معدن"},
                    {"label": "المصدر", "value": "مستشار رئيس الوزراء"},
                ],
                "broll": img(s, "broll_2.jpg"), "brolls": [img(s, "broll_2.jpg")],
                "brollType": "image", "accent": "#4CC9F0", "brollSource": CREDIT,
            },
            {
                "label": "ماذا بعد؟",
                "arabicHeading": "المركزي: باقية عملة قانونية",
                "arabicBody": "أكد البنك المركزي أن الفئات القديمة تبقى عملة قانونية ولا نية لسحبها، ولا تتوافر بيانات دورية معلنة عن حجم ما يُطرح منها، بحسب شفق نيوز والمستقلة.",
                "bigStat": {"value": "لا بيانات معلنة", "label": "Published data on small-note injections",
                            "arabicLabel": "لا تتوافر بيانات دورية معلنة عن حجم ما يطرحه البنك المركزي من الفئات النقدية الصغيرة (وكالة الصحافة المستقلة)"},
                "supportingStats": [
                    {"label": "البنك المركزي", "value": "باقية قانونية"},
                    {"label": "السحب", "value": "لا نية"},
                    {"label": "البيانات", "value": "غير معلنة"},
                ],
                "broll": img(s, "broll_3.jpg"), "brolls": [img(s, "broll_3.jpg")],
                "brollType": "image", "accent": "#FF6B3D", "brollSource": CREDIT,
            },
        ],
        "sources": [
            {"name": "Shafaq News", "domain": "shafaq.com"},
            {"name": "Mustaqila Press Agency", "domain": "mustaqila.com"},
        ],
        "arabicTicker": [
            "أوراق 250 و500 دينار اختفت إلى حد كبير من أسواق بغداد (شفق نيوز · وكالة الصحافة المستقلة)",
            "التجار يعوّضون النقص بتقريب الأسعار أو باستبدال المبلغ المتبقي بسلعة صغيرة (وكالة الصحافة المستقلة)",
            "مظهر محمد صالح المستشار المالي لرئيس الوزراء: العراق يطبع هذه الفئات ورقاً لا معدناً (شفق نيوز · 29 تموز)",
            "عمر الورقة النقدية الصغيرة نحو سنة واحدة بسرعة التداول العراقية وفق المعايير الدولية (مظهر محمد صالح)",
            "البنك المركزي: الفئات القديمة تبقى عملة قانونية ولا نية لسحبها (شفق نيوز)",
            "لا تتوافر بيانات دورية معلنة عن حجم ما يُطرح من الفئات الصغيرة (وكالة الصحافة المستقلة)",
            "آخر مرة ردّوا لك فكة… علك لو نقد؟",
        ],
    },
    "v11": {
        "kicker": "عاجل",
        "hookHeadline": "الفكة اختفت… والباقي علك",
        "voText": "اختفت أوراق المئتين وخمسين والخمسمئة دينار من أسواق بغداد، فصار التجار يقرّبون الأسعار أو يستبدلون المبلغ المتبقي بسلعة صغيرة، بحسب وكالة الصحافة المستقلة. وقال المستشار المالي لرئيس الوزراء مظهر محمد صالح إن العراق يطبع هذه الفئات ورقاً لا معدناً، وإن عمر الورقة الصغيرة نحو سنة واحدة بسرعة التداول العراقية، بحسب شفق نيوز. وأكد البنك المركزي أن الفئات القديمة تبقى عملة قانونية ولا نية لسحبها. فآخر مرة ردّوا لك فكة… علك لو نقد؟",
        "endQuestion": "آخر مرة ردّوا لك فكة… علك لو نقد؟",
        "sourcesLine": "المصادر: شفق نيوز · وكالة الصحافة المستقلة",
        "statPops": [
            {"value": "250 · 500", "label": "الفئات المفقودة", "matchWord": "وخمسين"},
            {"value": "سنة واحدة", "label": "عمر الورقة الصغيرة", "matchWord": "واحدة"},
        ],
    },
    "caption": """وين راحت الفكة من أسواق العراق — 250 و500 دينار

مستشار رئيس الوزراء يشرح السبب، والتجار يقرّبون الأسعار.

آخر مرة ردّوا لك فكة… علك لو نقد؟

المصادر: شفق نيوز، وكالة الصحافة المستقلة
#العراق #الدينار_العراقي #البنك_المركزي #أسعار
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
            v["audioBed"] = cfg["props"]["audioBed"]
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
