#!/usr/bin/env python3
"""Author the 2026-07-27 Photonect NEWS slate.

5 slugs (Iraq/MENA money-power lens). Posting order:
  1 bank-forgery-network   P1 corruption/banks     V11  A   (LEAD)
  2 dollar-official-gap    P1 money/dinar          V11  A   (daily dollar anchor)
  3 fuel-to-lebanon-debt   P2 energy/trade         V11  B
  4 gulf-power-link-delay  P1 electricity          V11  B
  5 turkey-water-road-visit P2 water/infrastructure V10 C   <- silent control

Directional shift vs 2026-07-26: from "who owes the state" to "what the paperwork
and the delays cost YOU" — forged files that pulled 243 loans out of 12 state
banks, the premium you personally pay over the official dollar rate, the fuel
Iraq keeps shipping to Lebanon unpaid, a Gulf power link that slipped past the
summer peak, and the water/road file heading to Ankara.

Writes per slug: .meta/props.json, caption.txt, .meta/media-stamp.json, and (for
the 4 voiced) .meta/v11-brief.json. Western numerals on-screen; voText spells
numbers in words (MSA newscast). No Persian yeh/kaf (grep-guarded after run).
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "data" / "posts"
DATE = "2026-07-27"
DATE_LABEL = "JUL 27 • 2026"
AR_DATE = "27 يوليو 2026"
HANDLE = "@photonect.news"
STAMP = {"hunted_at": f"{DATE}T11:00:00+00:00"}


def img(slug, n):
    return f"images/news/{slug}/{n}"


SLUGS = {}

# ─────────────────────────────────────────────────────────────────────────
# 1 — FORGERY NETWORK / 243 LOANS FROM 12 STATE BANKS  (P1 · V11 · A · LEAD)
# ─────────────────────────────────────────────────────────────────────────
s = f"{DATE}-bank-forgery-network"
SLUGS[s] = {
    "bucket": "iraq_politics",
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/mood_newsroom.mp3", "topicBucket": "iraq_politics", "variant": "A",
        "breaking": {
            "arabicKicker": "فساد · مصارف",
            "arabicHeadline": "243 قرضاً بورق مزوّر من 12 مصرفاً حكومياً",
            "englishSubhead": "FORGERY NETWORK PUSHED 243 LOAN FILES THROUGH 12 STATE BANKS",
            "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
        },
        "beats": [
            {
                "label": "ماذا يحدث؟",
                "arabicHeading": "31 موقوفاً في قضايا فساد أسبوعية",
                "arabicBody": "أوقفت السلطات العراقية 31 مسؤولاً وموظفاً ومقاولاً ومتهماً في قضايا فساد بين 20 و26 تموز، بحسب شفق نيوز.",
                "bigStat": {"value": "31", "label": "Detained in one week",
                            "arabicLabel": "عدد الموقوفين في قضايا الفساد الأسبوعية بين 20 و26 تموز 2026 (شفق نيوز)"},
                "supportingStats": [
                    {"label": "الديوانية", "value": "17"},
                    {"label": "صلاح الدين", "value": "11"},
                    {"label": "كركوك", "value": "3"},
                ],
                "broll": img(s, "broll_1.jpg"), "brolls": [img(s, "broll_1.jpg")],
                "brollType": "image", "accent": "#FFC217", "brollSource": "Shafaq News · 2026",
            },
            {
                "label": "لماذا يهم؟",
                "arabicHeading": "243 معاملة قرض بكفالات مزوّرة",
                "arabicBody": "وثّق التحقيق 243 معاملة قرض بكفالات مزوّرة قُدّمت إلى 12 مصرفاً حكومياً، وأكثر من 1,000 مستمسك مزوّر، بحسب هيئة النزاهة الاتحادية.",
                "bigStat": {"value": "243", "label": "Loan files on forged guarantees",
                            "arabicLabel": "عدد معاملات القروض المدعومة بكفالات مزوّرة التي وثّقها التحقيق في شبكة تزوير بالديوانية (هيئة النزاهة الاتحادية)"},
                "supportingStats": [
                    {"label": "المصارف", "value": "12 مصرفاً"},
                    {"label": "المستمسكات", "value": "+1,000"},
                    {"label": "المتهمون", "value": "13"},
                ],
                "broll": img(s, "broll_2.jpg"), "brolls": [img(s, "broll_2.jpg")],
                "brollType": "image", "accent": "#FF6B3D", "brollSource": "Integrity Commission · 2026",
            },
            {
                "label": "ماذا بعد؟",
                "arabicHeading": "41 مليار دينار و45 كيلو ذهب",
                "arabicBody": "استُردّت 41,143,847,719 ديناراً ونحو 400,000 دولار و45 كيلوغراماً من الذهب، ضمن حملة صولة الفجر، بحسب هيئة النزاهة الاتحادية.",
                "bigStat": {"value": "41.1B IQD", "label": "Recovered in these files",
                            "arabicLabel": "قيمة الأموال المستردّة في قضايا الأسبوع، أي نحو 31.41 مليون دولار (هيئة النزاهة الاتحادية)"},
                "supportingStats": [
                    {"label": "بالدولار", "value": "$31.41 مليون"},
                    {"label": "وأيضاً", "value": "$400,000"},
                    {"label": "ذهب", "value": "45 كغم"},
                ],
                "broll": img(s, "broll_3.jpg"), "brolls": [img(s, "broll_3.jpg")],
                "brollType": "image", "accent": "#D72638", "brollSource": "Integrity Commission · 2026",
            },
        ],
        "sources": [
            {"name": "Shafaq News", "domain": "shafaq.com"},
            {"name": "Federal Integrity Commission", "domain": "nazaha.iq"},
        ],
        "arabicTicker": [
            "السلطات العراقية توقف 31 مسؤولاً وموظفاً ومقاولاً ومتهماً في قضايا فساد بين 20 و26 تموز (شفق نيوز)",
            "التوزيع: الديوانية 17 موقوفاً، صلاح الدين 11، كركوك 3، والحصيلة خلال أسبوعين 58 موقوفاً (شفق نيوز)",
            "أكبر القضايا شبكة تزوير في الديوانية ضمّت 13 متهماً (هيئة النزاهة الاتحادية)",
            "التحقيق وثّق 243 معاملة قرض بكفالات مزوّرة قُدّمت إلى 12 مصرفاً حكومياً وأكثر من 1,000 مستمسك مزوّر (هيئة النزاهة الاتحادية)",
            "المستردّ: 41,143,847,719 ديناراً و400,000 دولار و45 كيلوغراماً من الذهب (هيئة النزاهة الاتحادية)",
            "قدمت يوم على قرض من مصرف حكومي؟",
        ],
    },
    "v11": {
        "kicker": "عاجل",
        "hookHeadline": "243 قرضاً بورق مزوّر",
        "voText": "أوقفت السلطات العراقية واحداً وثلاثين مسؤولاً وموظفاً ومقاولاً ومتهماً في قضايا فساد بين العشرين والسادس والعشرين من تموز، بحسب شفق نيوز. وكانت أكبر القضايا شبكة تزوير في الديوانية ضمّت ثلاثة عشر متهماً، إذ وثّق التحقيق مئتين وثلاثاً وأربعين معاملة قرض بكفالات مزوّرة قُدّمت إلى اثني عشر مصرفاً حكومياً، وأكثر من ألف مستمسك مزوّر. واستُردّت أكثر من واحد وأربعين مليار دينار وخمسة وأربعون كيلوغراماً من الذهب، بحسب هيئة النزاهة الاتحادية. فقدمت يوم على قرض من مصرف حكومي؟",
        "endQuestion": "قدمت يوم على قرض من مصرف حكومي؟",
        "sourcesLine": "المصادر: شفق نيوز · هيئة النزاهة الاتحادية",
        "statPops": [
            {"value": "31", "label": "موقوفاً بأسبوع", "matchWord": "وثلاثين"},
            {"value": "243", "label": "معاملة قرض مزوّرة", "matchWord": "وثلاثاً"},
            {"value": "12 مصرفاً", "label": "مصارف حكومية", "matchWord": "اثني"},
        ],
    },
    "caption": """قروض بورق مزوّر من 12 مصرفاً حكومياً في العراق

31 موقوفاً بأسبوع واحد، وأكبر قضية شبكة تزوير في الديوانية.

قدمت يوم على قرض من مصرف حكومي؟

المصادر: شفق نيوز، هيئة النزاهة الاتحادية
#العراق #الفساد #النزاهة #المصارف_الحكومية
@photonect.news
""",
}

# ─────────────────────────────────────────────────────────────────────────
# 2 — THE GAP: STREET DOLLAR vs OFFICIAL RATE  (P1 · V11 · A · dollar anchor)
# ─────────────────────────────────────────────────────────────────────────
s = f"{DATE}-dollar-official-gap"
SLUGS[s] = {
    "bucket": "iraq_economy",
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/mood_newsroom.mp3", "topicBucket": "iraq_economy", "variant": "A",
        "breaking": {
            "arabicKicker": "دولار · فجوة السعر",
            "arabicHeadline": "18,200 دينار تدفعها فرقاً عن السعر الرسمي",
            "englishSubhead": "STREET DOLLAR SITS 18,200 IQD ABOVE THE OFFICIAL RATE",
            "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
        },
        "beats": [
            {
                "label": "ماذا يحدث؟",
                "arabicHeading": "150,200 دينار لكل 100 دولار",
                "arabicBody": "بلغ سعر 100 دولار ظهر الاثنين 150,200 دينار في بغداد و150,350 في أربيل، بحسب أسعار السوق الموازية في بورصتي الكفاح والحارثية.",
                "bigStat": {"value": "150,200", "label": "IQD per $100 · Baghdad",
                            "arabicLabel": "سعر 100 دولار في السوق الموازية ببغداد ظهر الاثنين 27 تموز 2026 (بورصتا الكفاح والحارثية)"},
                "supportingStats": [
                    {"label": "بغداد", "value": "150,200"},
                    {"label": "أربيل", "value": "150,350"},
                    {"label": "التوقيت", "value": "ظهر الاثنين"},
                ],
                "broll": img(s, "broll_1.jpg"), "brolls": [img(s, "broll_1.jpg")],
                "brollType": "image", "accent": "#FFC217", "brollSource": "Kifah & Harithiya · 2026",
            },
            {
                "label": "لماذا يهم؟",
                "arabicHeading": "الرسمي 132,000 لكل 100 دولار",
                "arabicBody": "السعر الرسمي للبنك المركزي العراقي 1,320 ديناراً للدولار، أي 132,000 لكل 100 دولار، فالفارق نحو 18,200 دينار أو 13.8%.",
                "bigStat": {"value": "18,200 د.ع", "label": "Premium over official per $100",
                            "arabicLabel": "الفارق بين سعر 100 دولار في السوق الموازية والسعر الرسمي للبنك المركزي العراقي البالغ 1,320 ديناراً للدولار (البنك المركزي العراقي)"},
                "supportingStats": [
                    {"label": "الرسمي", "value": "132,000"},
                    {"label": "الموازي", "value": "150,200"},
                    {"label": "الفارق", "value": "13.8%"},
                ],
                "broll": img(s, "broll_2.jpg"), "brolls": [img(s, "broll_2.jpg")],
                "brollType": "image", "accent": "#FF6B3D", "brollSource": "Central Bank of Iraq · 2026",
            },
            {
                "label": "ماذا بعد؟",
                "arabicHeading": "من 153,750 إلى 150,200 بأسبوعين",
                "arabicBody": "كان السعر 153,750 ديناراً لكل 100 دولار في 11 تموز، وفتح الأحد على 149,650، بحسب شفق نيوز.",
                "bigStat": {"value": "153,750", "label": "Rate on 11 July",
                            "arabicLabel": "سعر 100 دولار في السوق الموازية يوم 11 تموز 2026 قبل تراجعه (شفق نيوز)"},
                "supportingStats": [
                    {"label": "11 تموز", "value": "153,750"},
                    {"label": "الأحد", "value": "149,650"},
                    {"label": "الاثنين", "value": "150,200"},
                ],
                "broll": img(s, "broll_3.jpg"), "brolls": [img(s, "broll_3.jpg")],
                "brollType": "image", "accent": "#D72638", "brollSource": "Shafaq News · 2026",
            },
        ],
        "sources": [
            {"name": "Kifah & Harithiya Bourse", "domain": "Baghdad FX"},
            {"name": "Shafaq News", "domain": "shafaq.com"},
            {"name": "Central Bank of Iraq", "domain": "cbi.iq"},
        ],
        "arabicTicker": [
            "سعر 100 دولار ظهر الاثنين 150,200 ديناراً في بغداد (أسعار السوق الموازية · بورصتا الكفاح والحارثية)",
            "أربيل: 150,350 ديناراً لكل 100 دولار (أسعار السوق الموازية)",
            "السعر الرسمي للبنك المركزي العراقي 1,320 ديناراً للدولار الواحد أي 132,000 لكل 100 دولار (البنك المركزي العراقي)",
            "الفارق بين السوق والسعر الرسمي نحو 18,200 دينار لكل 100 دولار أو 13.8%",
            "الدولار فتح الأحد على 149,650 ديناراً وكان 153,750 في 11 تموز (شفق نيوز)",
            "شكد دفعت آخر مرة بدلت دولار؟",
        ],
    },
    "v11": {
        "kicker": "عاجل",
        "hookHeadline": "18,200 دينار فرق… تدفعها أنت",
        "voText": "بلغ سعر مئة دولار ظهر يوم الاثنين في بغداد مئة وخمسين ألفاً ومئتي دينار، وفي أربيل مئة وخمسين ألفاً وثلاثمئة وخمسين ديناراً، بحسب أسعار السوق الموازية في بورصتي الكفاح والحارثية. أما السعر الرسمي للبنك المركزي العراقي فهو ألف وثلاثمئة وعشرون ديناراً للدولار الواحد، أي مئة واثنان وثلاثون ألف دينار لكل مئة دولار. والفارق بين السعرين نحو ثمانية عشر ألفاً ومئتي دينار، أي ما يقارب ثلاثة عشر وثمانية بالمئة. فشكد دفعت آخر مرة بدلت دولار؟",
        "endQuestion": "شكد دفعت آخر مرة بدلت دولار؟",
        "sourcesLine": "المصادر: بورصتا الكفاح والحارثية · شفق نيوز · البنك المركزي العراقي",
        "statPops": [
            {"value": "150,200", "label": "لكل 100 دولار ببغداد", "matchWord": "بغداد"},
            {"value": "1,320", "label": "السعر الرسمي", "matchWord": "وعشرون"},
            {"value": "18,200", "label": "الفارق عن الرسمي", "matchWord": "والفارق"},
        ],
    },
    "caption": """سعر الدولار اليوم في بغداد — 18,200 دينار فوق السعر الرسمي

السوق الموازية تسبق سعر البنك المركزي بنحو 13.8%.

شكد دفعت آخر مرة بدلت دولار؟

المصادر: بورصتا الكفاح والحارثية، شفق نيوز، البنك المركزي
#العراق #الدولار #سعر_الصرف #الدينار_العراقي
@photonect.news
""",
}

# ─────────────────────────────────────────────────────────────────────────
# 3 — IRAQ FUEL OIL TO LEBANON / $2.7BN OWED  (P2 · V11 · B)
# ─────────────────────────────────────────────────────────────────────────
s = f"{DATE}-fuel-to-lebanon-debt"
SLUGS[s] = {
    "bucket": "mena_geopolitics",
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/mood_newsroom.mp3", "topicBucket": "mena_geopolitics", "variant": "B",
        "breaking": {
            "arabicKicker": "طاقة · تجارة",
            "arabicHeadline": "2.7 مليار دولار على لبنان… وقود عراقي",
            "englishSubhead": "IRAQ SET TO RENEW LEBANON FUEL DEAL AS $2.7BN GOES UNPAID",
            "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
        },
        "beats": [
            {
                "label": "ماذا يحدث؟",
                "arabicHeading": "تجديد اتفاق زيت الوقود مع لبنان",
                "arabicBody": "أفادت شفق نيوز في 25 تموز بأن العراق ولبنان يتجهان لتجديد اتفاق زيت الوقود، بعد رفع الكميات السنوية من 1.5 إلى 2 مليون طن.",
                "bigStat": {"value": "2 مليون طن", "label": "Annual fuel oil to Lebanon",
                            "arabicLabel": "الكمية السنوية من زيت الوقود التي يزوّد بها العراق لبنان بعد رفعها من 1.5 مليون طن (شفق نيوز)"},
                "supportingStats": [
                    {"label": "سابقاً", "value": "1.5 مليون طن"},
                    {"label": "حالياً", "value": "2 مليون طن"},
                    {"label": "الغرض", "value": "كهرباء لبنان"},
                ],
                "broll": img(s, "broll_1.jpg"), "brolls": [img(s, "broll_1.jpg")],
                "brollType": "image", "accent": "#FFC217", "brollSource": "Shafaq News · 2026",
            },
            {
                "label": "لماذا يهم؟",
                "arabicHeading": "مستحقات العراق 2.7 مليار دولار",
                "arabicBody": "تبلغ مستحقات العراق على لبنان نحو 2.7 مليار دولار مقابل هذه التوريدات، بحسب شفق نيوز.",
                "bigStat": {"value": "$2.7B", "label": "Owed to Iraq for fuel",
                            "arabicLabel": "قيمة مستحقات العراق على لبنان مقابل توريدات زيت الوقود (شفق نيوز)"},
                "supportingStats": [
                    {"label": "المستحقات", "value": "$2.7 مليار"},
                    {"label": "الشرط", "value": "منصة دفع"},
                    {"label": "مالية لبنان", "value": "ياسين جابر"},
                ],
                "broll": img(s, "broll_2.jpg"), "brolls": [img(s, "broll_2.jpg")],
                "brollType": "image", "accent": "#FF6B3D", "brollSource": "Shafaq News · 2026",
            },
            {
                "label": "ماذا بعد؟",
                "arabicHeading": "لبنان منفذاً لتصدير النفط العراقي",
                "arabicBody": "بحث رئيس الوزراء اللبناني نواف سلام في بغداد مع علي الزيدي إمكانية استخدام لبنان منفذاً إضافياً لتصدير النفط العراقي إلى المتوسط، بحسب شفق نيوز.",
                "bigStat": {"value": "2021", "label": "Fuel supplies began",
                            "arabicLabel": "العام الذي بدأ فيه العراق تزويد لبنان بزيت الوقود ضمن اتفاق جُدّد عدة مرات (شفق نيوز)"},
                "supportingStats": [
                    {"label": "لبنان", "value": "نواف سلام"},
                    {"label": "العراق", "value": "علي الزيدي"},
                    {"label": "المستشار المالي", "value": "مظهر محمد صالح"},
                ],
                "broll": img(s, "broll_3.jpg"), "brolls": [img(s, "broll_3.jpg")],
                "brollType": "image", "accent": "#D72638", "brollSource": "Iraqi PM Office · 2026",
            },
        ],
        "sources": [
            {"name": "Shafaq News", "domain": "shafaq.com"},
            {"name": "Iraqi Prime Minister's Office", "domain": "pmo.iq"},
        ],
        "arabicTicker": [
            "شفق نيوز: العراق ولبنان يتجهان إلى تجديد اتفاق تزويد لبنان بزيت الوقود",
            "الكميات السنوية رُفعت من 1.5 مليون طن إلى 2 مليون طن (شفق نيوز)",
            "مستحقات العراق على لبنان مقابل التوريدات نحو 2.7 مليار دولار (شفق نيوز)",
            "التزويد بدأ عام 2021 لتخفيف أزمة الكهرباء في لبنان وجُدّد عدة مرات (شفق نيوز)",
            "نواف سلام بحث في بغداد مع علي الزيدي استخدام لبنان منفذاً إضافياً لتصدير النفط العراقي إلى المتوسط (رئاسة الوزراء العراقية)",
            "شنو أول شي تصلحه بـ2.7 مليار دولار؟",
        ],
    },
    "v11": {
        "kicker": "عاجل",
        "hookHeadline": "2.7 مليار دولار على لبنان",
        "voText": "أفادت شفق نيوز بأن العراق ولبنان يتجهان إلى تجديد اتفاق تزويد لبنان بزيت الوقود، بعد رفع الكميات السنوية إلى مليوني طن. ويزوّد العراق لبنان بزيت الوقود منذ عام ألفين وواحد وعشرين لتخفيف أزمة الكهرباء هناك، وتبلغ مستحقاته على بيروت نحو ملياري دولار وسبعمئة مليون. وبحث رئيس الوزراء اللبناني نواف سلام في بغداد مع نظيره علي الزيدي إمكانية استخدام لبنان منفذاً إضافياً لتصدير النفط العراقي إلى البحر المتوسط. فشنو أول شي تصلحه بمليارين وسبعمئة مليون دولار؟",
        "endQuestion": "شنو أول شي تصلحه بـ2.7 مليار دولار؟",
        "sourcesLine": "المصادر: شفق نيوز · رئاسة الوزراء العراقية",
        "statPops": [
            {"value": "2 مليون طن", "label": "الكمية السنوية", "matchWord": "مليوني"},
            {"value": "2021", "label": "بداية التزويد", "matchWord": "وعشرين"},
            {"value": "$2.7 مليار", "label": "مستحقات العراق", "matchWord": "مستحقاته"},
        ],
    },
    "caption": """العراق يزوّد لبنان بالوقود ومستحقاته 2.7 مليار دولار

تجديد الاتفاق ورفع الكميات، وبحث عن منفذ عراقي على المتوسط.

شنو أول شي تصلحه بـ2.7 مليار دولار؟

المصادر: شفق نيوز، رئاسة الوزراء العراقية
#العراق #لبنان #الطاقة #زيت_الوقود
@photonect.news
""",
}

# ─────────────────────────────────────────────────────────────────────────
# 4 — GULF POWER LINK SLIPS PAST THE SUMMER PEAK  (P1 · V11 · B)
# ─────────────────────────────────────────────────────────────────────────
s = f"{DATE}-gulf-power-link-delay"
SLUGS[s] = {
    "bucket": "iraq_economy",
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/mood_newsroom.mp3", "topicBucket": "iraq_economy", "variant": "B",
        "breaking": {
            "arabicKicker": "كهرباء · ربط خليجي",
            "arabicHeadline": "الربط الخليجي يتأجل… والصيف ما ينتظر",
            "englishSubhead": "GULF POWER LINK SLIPS TO LATE AUGUST AS SUMMER PEAK BITES",
            "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
        },
        "beats": [
            {
                "label": "ماذا يحدث؟",
                "arabicHeading": "500 ميغاواط تتأخر إلى نهاية آب",
                "arabicBody": "المرحلة الأولى من الربط الكهربائي مع الخليج 500 ميغاواط وكانت مقررة مطلع 2026، وأجّلتها هيئة الربط إلى نهاية آب على الأقل.",
                "bigStat": {"value": "500 MW", "label": "Phase 1 capacity",
                            "arabicLabel": "قدرة المرحلة الأولى من الربط الكهربائي بين العراق ودول الخليج (هيئة الربط الكهربائي الخليجي)"},
                "supportingStats": [
                    {"label": "المقرر سابقاً", "value": "مطلع 2026"},
                    {"label": "الموعد الجديد", "value": "نهاية آب"},
                    {"label": "احتمال التأخر", "value": "2027"},
                ],
                "broll": img(s, "broll_1.jpg"), "brolls": [img(s, "broll_1.jpg")],
                "brollType": "image", "accent": "#FFC217", "brollSource": "GCCIA · 2026",
            },
            {
                "label": "لماذا يهم؟",
                "arabicHeading": "29 غيغاواط إنتاج مقابل 40 طلباً",
                "arabicBody": "يبلغ إنتاج العراق نحو 29 غيغاواط مقابل طلب اعتيادي قرب 40 غيغاواط، وذروة صيفية بين 40 و55 غيغاواط، بحسب منتدى الشرق الأوسط.",
                "bigStat": {"value": "29 GW", "label": "Iraq's generation vs 40 GW demand",
                            "arabicLabel": "إجمالي إنتاج العراق من الطاقة الكهربائية مقابل طلب اعتيادي قرب 40 غيغاواط (منتدى الشرق الأوسط)"},
                "supportingStats": [
                    {"label": "الإنتاج", "value": "29 غيغاواط"},
                    {"label": "الطلب", "value": "40 غيغاواط"},
                    {"label": "الذروة", "value": "40-55 غيغاواط"},
                ],
                "broll": img(s, "broll_2.jpg"), "brolls": [img(s, "broll_2.jpg")],
                "brollType": "image", "accent": "#FF6B3D", "brollSource": "Middle East Forum · 2026",
            },
            {
                "label": "ماذا بعد؟",
                "arabicHeading": "الغاز الإيراني ينزل إلى 5 ملايين",
                "arabicBody": "الغاز الإيراني متعاقد عليه بـ50 مليون متر مكعب يومياً، والوارد الفعلي 15-20 مليوناً وينزل إلى 5-7، ما يفقد 3,000-4,500 ميغاواط، بحسب منتدى الشرق الأوسط.",
                "bigStat": {"value": "3,000-4,500 MW", "label": "Power lost to gas cuts",
                            "arabicLabel": "الطاقة المفقودة بسبب انخفاض إمدادات الغاز الإيراني عن الكميات المتعاقد عليها (منتدى الشرق الأوسط)"},
                "supportingStats": [
                    {"label": "المتعاقد", "value": "50 مليون م3"},
                    {"label": "الفعلي", "value": "15-20 مليوناً"},
                    {"label": "بعد الأضرار", "value": "5-7 ملايين"},
                ],
                "broll": img(s, "broll_3.jpg"), "brolls": [img(s, "broll_3.jpg")],
                "brollType": "image", "accent": "#D72638", "brollSource": "Middle East Forum · 2026",
            },
        ],
        "sources": [
            {"name": "Middle East Forum", "domain": "meforum.org"},
            {"name": "GCC Interconnection Authority", "domain": "gccia.com.sa"},
            {"name": "AGBI", "domain": "agbi.com"},
        ],
        "arabicTicker": [
            "المرحلة الأولى من الربط الكهربائي الخليجي 500 ميغاواط وكانت مقررة مطلع 2026 (هيئة الربط الكهربائي الخليجي)",
            "هيئة الربط تؤجل التشغيل إلى نهاية آب على الأقل مع احتمال التأخر إلى 2027 (منتدى الشرق الأوسط)",
            "إنتاج العراق نحو 29 غيغاواط مقابل طلب اعتيادي قرب 40 غيغاواط (منتدى الشرق الأوسط)",
            "الذروة الصيفية بين 40 و55 غيغاواط (منتدى الشرق الأوسط)",
            "الغاز الإيراني الوارد 15-20 مليون متر مكعب يومياً من أصل 50 مليوناً متعاقداً عليها (منتدى الشرق الأوسط)",
            "كم ساعة كهرباء وصلتك اليوم؟",
        ],
    },
    "v11": {
        "kicker": "عاجل",
        "hookHeadline": "500 ميغاواط تأجلت… وانت بالحر",
        "voText": "أُجّل تشغيل المرحلة الأولى من الربط الكهربائي بين العراق ودول الخليج، وقدرتها خمسمئة ميغاواط، إلى نهاية آب على الأقل بعد أن كانت مقررة مطلع العام، بحسب منتدى الشرق الأوسط. ويبلغ إنتاج العراق نحو تسعة وعشرين غيغاواط مقابل طلب اعتيادي قرب أربعين غيغاواط، وذروة صيفية تصل إلى خمسة وخمسين. أما الغاز الإيراني الوارد فبين خمسة عشر وعشرين مليون متر مكعب يومياً من أصل خمسين متعاقداً عليها، وتُقدَّر الطاقة المفقودة بثلاثة آلاف إلى أربعة آلاف وخمسمئة ميغاواط. فكم ساعة كهرباء وصلتك اليوم؟",
        "endQuestion": "كم ساعة كهرباء وصلتك اليوم؟",
        "sourcesLine": "المصادر: منتدى الشرق الأوسط · هيئة الربط الكهربائي الخليجي · AGBI",
        "statPops": [
            {"value": "500 MW", "label": "المرحلة الأولى", "matchWord": "وقدرتها"},
            {"value": "29 GW", "label": "إنتاج العراق", "matchWord": "تسعة"},
            {"value": "50 مليون م3", "label": "الغاز المتعاقد", "matchWord": "متعاقداً"},
        ],
    },
    "caption": """الربط الكهربائي الخليجي يتأجل — والصيف بذروته في العراق

500 ميغاواط كانت مقررة مطلع العام، والموعد الجديد نهاية آب.

كم ساعة كهرباء وصلتك اليوم؟

المصادر: منتدى الشرق الأوسط، هيئة الربط الكهربائي الخليجي
#العراق #الكهرباء #الربط_الخليجي #أزمة_الطاقة
@photonect.news
""",
}

# ─────────────────────────────────────────────────────────────────────────
# 5 — ANKARA VISIT: WATER + DEVELOPMENT ROAD  (P2 · V10 SILENT CONTROL · C)
# ─────────────────────────────────────────────────────────────────────────
s = f"{DATE}-turkey-water-road-visit"
SLUGS[s] = {
    "bucket": "mena_geopolitics",
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/mood_newsroom.mp3", "topicBucket": "mena_geopolitics", "variant": "C",
        "breaking": {
            "arabicKicker": "مياه · طريق التنمية",
            "arabicHeadline": "حصة العراق من المياه على طاولة أنقرة",
            "englishSubhead": "PM AL-ZAIDI HEADS TO ANKARA WITH WATER AND THE DEVELOPMENT ROAD ON TOP",
            "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
        },
        "beats": [
            {
                "label": "ماذا يحدث؟",
                "arabicHeading": "الزيدي إلى أنقرة الثلاثاء",
                "arabicBody": "يزور رئيس الوزراء علي الزيدي أنقرة الثلاثاء 28 تموز على رأس وفد حكومي رفيع، وملف المياه يتصدر جدول الأعمال، بحسب شفقنا العراق.",
                "bigStat": {"value": "28 تموز", "label": "Ankara visit date",
                            "arabicLabel": "موعد زيارة رئيس الوزراء العراقي علي الزيدي إلى أنقرة على رأس وفد حكومي رفيع (شفقنا العراق)"},
                "supportingStats": [
                    {"label": "الملفات", "value": "مياه ونفط"},
                    {"label": "وأيضاً", "value": "كهرباء واقتصاد"},
                    {"label": "الأولوية", "value": "الإطلاقات المائية"},
                ],
                "broll": img(s, "broll_1.jpg"), "brolls": [img(s, "broll_1.jpg")],
                "brollType": "image", "accent": "#FFC217", "brollSource": "Shafaqna Iraq · 2026",
            },
            {
                "label": "لماذا يهم؟",
                "arabicHeading": "6 سدود في المرحلة الأولى",
                "arabicBody": "تسعى بغداد إلى ضمانات واضحة بشأن الإطلاقات المائية، وتقول وزارة الموارد المائية إن 6 سدود جديدة تقع ضمن المرحلة الأولى من الاتفاق مع تركيا.",
                "bigStat": {"value": "6 سدود", "label": "Dams in phase one",
                            "arabicLabel": "عدد السدود الجديدة التي تقع ضمن المرحلة الأولى من الاتفاق مع تركيا (وزارة الموارد المائية العراقية)"},
                "supportingStats": [
                    {"label": "المرحلة", "value": "الأولى"},
                    {"label": "المطلب", "value": "ضمانات مائية"},
                    {"label": "الجهة", "value": "الموارد المائية"},
                ],
                "broll": img(s, "broll_2.jpg"), "brolls": [img(s, "broll_2.jpg")],
                "brollType": "image", "accent": "#FF6B3D", "brollSource": "Ministry of Water Resources · 2026",
            },
            {
                "label": "ماذا بعد؟",
                "arabicHeading": "طريق التنمية… التصاميم 100%",
                "arabicBody": "أوعز الزيدي بإعداد آلية تمويل متكاملة لطريق التنمية، والتصاميم الأولية للطريق وخط سكك الحديد مكتملة 100%، فيما قالت أنقرة إن حجر الأساس قريب، بحسب الجزيرة.",
                "bigStat": {"value": "100%", "label": "Preliminary designs complete",
                            "arabicLabel": "نسبة إنجاز التصاميم الأولية لمشروع طريق التنمية وخط السكك الحديدية المرافق له (شفقنا العراق)"},
                "supportingStats": [
                    {"label": "التصاميم", "value": "100%"},
                    {"label": "حجر الأساس", "value": "قريباً"},
                    {"label": "بعدها", "value": "زيارة السعودية"},
                ],
                "broll": img(s, "broll_3.jpg"), "brolls": [img(s, "broll_3.jpg")],
                "brollType": "image", "accent": "#D72638", "brollSource": "Al Jazeera · 2026",
            },
        ],
        "sources": [
            {"name": "Shafaqna Iraq", "domain": "shafaqna.com"},
            {"name": "Ministry of Water Resources", "domain": "mowr.gov.iq"},
            {"name": "Al Jazeera", "domain": "aljazeera.net"},
        ],
        "arabicTicker": [
            "رئيس الوزراء علي الزيدي يزور أنقرة الثلاثاء 28 تموز على رأس وفد حكومي رفيع (شفقنا العراق)",
            "ملف المياه يتصدر جدول الأعمال وبغداد تسعى لضمانات بشأن الإطلاقات المائية (شفقنا العراق)",
            "وزارة الموارد المائية: 6 سدود جديدة ضمن المرحلة الأولى من الاتفاق مع تركيا (وزارة الموارد المائية)",
            "الزيدي يوعز بإعداد آلية تمويل متكاملة لمشروع طريق التنمية والتصاميم الأولية مكتملة 100% (شفقنا العراق)",
            "وزير النقل التركي: حجر الأساس لطريق التنمية مع العراق سيوضع قريباً (الجزيرة)",
            "وصلتك مي الإسالة اليوم؟",
        ],
    },
    "v11": None,  # silent V10 control
    "caption": """زيارة الزيدي إلى أنقرة — المياه وطريق التنمية على الطاولة

بغداد تريد ضمانات بشأن الإطلاقات المائية، و6 سدود ضمن المرحلة الأولى.

وصلتك مي الإسالة اليوم؟

المصادر: شفقنا العراق، وزارة الموارد المائية، الجزيرة
#العراق #تركيا #المياه #طريق_التنمية
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
