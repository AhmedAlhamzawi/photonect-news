#!/usr/bin/env python3
"""Author the 2026-07-22 Photonect NEWS slate.

5 slugs (Iraq/MENA money-power lens):
  1 travel-dollar-2000       P1 money        V11  A
  2 kurdistan-salary-standoff P1 money/acct  V11  B
  3 arbaeen-economy          P3 pride+econ   V11  A
  4 opec-price-squeeze       P2 gulf-econ    V10  B   <- silent control
  5 graft-concealment        P1 corruption   V11  B

Writes per slug: data/posts/<slug>/.meta/props.json, caption.txt,
.meta/media-stamp.json, and (for the 4 voiced) .meta/v11-brief.json.
Western numerals on-screen; voText spells numbers in words (MSA newscast).
No Persian yeh/kaf (guarded by grep after run).
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "data" / "posts"
DATE = "2026-07-22"
DATE_LABEL = "JUL 22 • 2026"
AR_DATE = "22 يوليو 2026"
HANDLE = "@photonect.news"
ACCENTS = ["#FFC217", "#FF6B3D", "#D72638"]


def imgs(slug):
    return [f"images/news/{slug}/{n}" for n in ("hero.jpg", "broll_1.jpg", "broll_2.jpg", "broll_3.jpg")]


SLUGS = {}

# ─────────────────────────────────────────────────────────────────────────
# 1 — TRAVEL DOLLAR CUT  (P1 money · V11 · A)
# ─────────────────────────────────────────────────────────────────────────
s = f"{DATE}-travel-dollar-2000"
SLUGS[s] = {
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/mood_newsroom.mp3", "topicBucket": "iraq_economy", "variant": "A",
        "breaking": {
            "arabicKicker": "دولار · سفر",
            "arabicHeadline": "دولار المسافر ينزل إلى 2000$ فقط",
            "englishSubhead": "$3,000 → $2,000 CASH CAP | WAS $7,000 IN 2023",
            "heroMedia": f"images/news/{s}/hero.jpg", "heroMediaType": "image",
        },
        "beats": [
            {
                "label": "ماذا يحدث؟",
                "arabicHeading": "المركزي يخفض النقد الدولاري للمسافر",
                "arabicBody": "خفّض البنك المركزي العراقي سقف النقد الدولاري للمسافر من 3000 إلى 2000 دولار شهرياً لكل بالغ، بحسب شفق نيوز ومصدر مصرفي.",
                "bigStat": {"value": "$2,000", "label": "New monthly cash cap",
                            "arabicLabel": "السقف الشهري الجديد للنقد الدولاري لكل مسافر بالغ بعد خفضه من 3000 دولار (شفق نيوز · مصدر مصرفي)"},
                "supportingStats": [{"label": "السقف الجديد", "value": "2000 $"},
                                     {"label": "كان سابقاً", "value": "3000 $"},
                                     {"label": "في 2023", "value": "7000 $"}],
                "broll": f"images/news/{s}/broll_1.jpg", "brolls": [f"images/news/{s}/broll_1.jpg"],
                "brollType": "image", "accent": ACCENTS[0], "brollSource": "Shafaq News · 2026",
            },
            {
                "label": "لماذا يهم؟",
                "arabicHeading": "يمسّ كل مسافر: علاج ودراسة وعمرة",
                "arabicBody": "القرار يشمل جميع الأغراض من سياحة وعلاج ودراسة وحج وعمرة وعمل، فيما يقترب السعر الموازي من 1500 دينار للدولار مقابل 1320 رسمياً.",
                "bigStat": {"value": "1,500", "label": "Parallel rate (IQD/$)",
                            "arabicLabel": "سعر السوق الموازي للدولار الذي يقترب منه المسافرون مقابل 1320 ديناراً للسعر الرسمي (964 ميديا)"},
                "supportingStats": [{"label": "رسمي", "value": "1320 د"},
                                     {"label": "موازي", "value": "~1500 د"},
                                     {"label": "يشمل", "value": "كل الأغراض"}],
                "broll": f"images/news/{s}/broll_2.jpg", "brolls": [f"images/news/{s}/broll_2.jpg"],
                "brollType": "image", "accent": ACCENTS[1], "brollSource": "Iraqi News · 964media",
            },
            {
                "label": "ماذا بعد؟",
                "arabicHeading": "دولار المطار رسمي… وكردستان تتوقف",
                "arabicBody": "يوفّر المركزي الدولار بالسعر الرسمي في المطارات منذ 14 تموز وعبر البطاقات، بينما توقفت مبيعاته الرسمية للمسافرين في كردستان فدفعتهم للسوق الموازية.",
                "bigStat": {"value": "14 تموز", "label": "Airport official-rate dollars begin",
                            "arabicLabel": "تاريخ بدء توفير البنك المركزي الدولار بالسعر الرسمي للمسافرين في المطارات لتخفيف أثر خفض السقف (964 ميديا)"},
                "supportingStats": [{"label": "المطارات", "value": "سعر رسمي"},
                                     {"label": "الأداة", "value": "بطاقات دفع"},
                                     {"label": "كردستان", "value": "توقف رسمي"}],
                "broll": f"images/news/{s}/broll_3.jpg", "brolls": [f"images/news/{s}/broll_3.jpg"],
                "brollType": "image", "accent": ACCENTS[2], "brollSource": "Kurdistan24 · 964media",
            },
        ],
        "sources": [{"name": "Shafaq News", "domain": "shafaq.com"},
                     {"name": "Iraqi News", "domain": "iraqinews.com"},
                     {"name": "964media", "domain": "964media.com"},
                     {"name": "Kurdistan24", "domain": "kurdistan24.net"}],
        "arabicTicker": [
            "البنك المركزي العراقي يخفض سقف النقد الدولاري للمسافر من 3000 إلى 2000 دولار شهرياً (شفق نيوز · مصدر مصرفي)",
            "القرار يشمل جميع الأغراض: سياحة وعلاج ودراسة وحج وعمرة وعمل، لكل مسافر بالغ (شبكة الأخبار العراقية)",
            "السقف كان 7000 دولار في 2023 ثم خُفض عدة مرات وسط جهود لكبح تهريب الدولار (شبكة الأخبار العراقية)",
            "المركزي يبرّر الخفض بتشجيع الدفع الإلكتروني وكبح المضاربة على العملة (البنك المركزي العراقي)",
            "المركزي يوفّر الدولار بالسعر الرسمي في المطارات منذ 14 تموز وعبر بطاقات الدفع (964 ميديا)",
            "توقف بيع الدولار الرسمي للمسافرين في إقليم كردستان دفعهم نحو السوق الموازية الأعلى (كردستان24)",
            "فهل يضبط خفض السقف سوق الدولار، أم يدفع المسافرين نحو السوق الموازية؟",
        ],
    },
    "v11": {
        "slug": s, "kicker": "عاجل",
        "hookHeadline": "دولار المسافر… 2000 فقط؟",
        "voText": "خفّض البنك المركزي العراقي سقف النقد الدولاري الذي يحمله المسافر من ثلاثة آلاف إلى ألفي دولار شهرياً لكل بالغ، بحسب شفق نيوز ومصدر مصرفي. ويشمل القرار جميع الأغراض من سياحة وعلاج ودراسة وحج وعمرة وعمل. وفي المقابل يوفّر المركزي الدولار بالسعر الرسمي في المطارات وعبر البطاقات، بينما اقترب السعر الموازي من ألف وخمسمئة دينار للدولار، وتوقفت المبيعات الرسمية للمسافرين في إقليم كردستان. فهل يضبط هذا القرار سوق الدولار، أم يدفع المسافرين نحو السوق الموازية؟",
        "endQuestion": "هل يضبط خفض السقف سوق الدولار، أم يدفع المسافرين نحو السوق الموازية؟",
        "sourcesLine": "المصادر: شفق نيوز · 964 · كردستان24",
        "images": imgs(s), "audioBed": "audio/mood_newsroom.mp3",
        "statPops": [{"value": "$2,000", "label": "سقف النقد الجديد", "matchWord": "ألفي"},
                      {"value": "1,500 د", "label": "السعر الموازي", "matchWord": "وخمسمئة"}],
    },
    "caption": """سعر دولار السفر في العراق اليوم — شنو تغيّر؟

المركزي يخفض سقف النقد الدولاري للمسافر ويوفّره بالسعر الرسمي في المطارات.

برأيك، القرار يضبط السوق لو يزيد الضغط على المسافر؟

المصادر: شفق نيوز، 964، كردستان24
#العراق #الدولار #البنك_المركزي #سفر
@photonect.news
""",
    "bucket": "iraq_economy",
}

# ─────────────────────────────────────────────────────────────────────────
# 2 — KURDISTAN SALARY STANDOFF  (P1 money/acct · V11 · B)
# ─────────────────────────────────────────────────────────────────────────
s = f"{DATE}-kurdistan-salary-standoff"
SLUGS[s] = {
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/mood_cinematic.mp3", "topicBucket": "iraq_economy", "variant": "B",
        "breaking": {
            "arabicKicker": "رواتب · كردستان",
            "arabicHeadline": "رواتب كردستان بخطر… مفاوضات بغداد–أربيل تتعثّر",
            "englishSubhead": "1.2M SALARIES | 120B IQD/MO CONDITION | ~41% TRANSFERRED",
            "heroMedia": f"images/news/{s}/hero.jpg", "heroMediaType": "image",
        },
        "beats": [
            {
                "label": "ماذا يحدث؟",
                "arabicHeading": "تعثّر جديد في ملف الرواتب والنفط",
                "arabicBody": "تعثّرت مفاوضات بغداد وأربيل حول الرواتب والنفط مجدداً، ودعا النائب الأول لرئيس البرلمان عدنان فيحان إلى وقف التحويلات للإقليم حتى تُسوّى الإيرادات، بحسب العربي الجديد ورووداو.",
                "bigStat": {"value": "120 مليار د", "label": "Monthly non-oil revenue condition",
                            "arabicLabel": "المبلغ الشهري من الإيرادات غير النفطية الذي يُفترض أن يحوّله الإقليم إلى بغداد وفق آلية آب 2025 (الوكالة العراقية للأنباء)"},
                "supportingStats": [{"label": "الشرط الشهري", "value": "120 مليار د"},
                                     {"label": "الملف", "value": "نفط ورواتب"},
                                     {"label": "الوسيط", "value": "ضغط أميركي"}],
                "broll": f"images/news/{s}/broll_1.jpg", "brolls": [f"images/news/{s}/broll_1.jpg"],
                "brollType": "image", "accent": ACCENTS[0], "brollSource": "The New Arab · Rudaw",
            },
            {
                "label": "لماذا يهم؟",
                "arabicHeading": "1.2 مليون موظف ينتظرون رواتبهم",
                "arabicBody": "يعتمد نحو 1.2 مليون موظف في الإقليم على رواتب تُقدَّر بنحو تريليون دينار شهرياً، وتقول أربيل إن بغداد حوّلت 41% فقط من مستحقاتها بين 2023 و2025.",
                "bigStat": {"value": "~1 تريليون د", "label": "KRG monthly salary bill",
                            "arabicLabel": "التقدير الشهري لفاتورة رواتب موظفي إقليم كردستان الذين يعتمدون على التحويلات الاتحادية (مركز رووداو للأبحاث)"},
                "supportingStats": [{"label": "الموظفون", "value": "1.2 مليون"},
                                     {"label": "الراتب الشهري", "value": "~1 تريليون د"},
                                     {"label": "حُوّل", "value": "41%"}],
                "broll": f"images/news/{s}/broll_2.jpg", "brolls": [f"images/news/{s}/broll_2.jpg"],
                "brollType": "image", "accent": ACCENTS[1], "brollSource": "Kurdistan24 · Rudaw",
            },
            {
                "label": "ماذا بعد؟",
                "arabicHeading": "واشنطن تضغط… ومسوّدات لإنهاء الخلاف",
                "arabicBody": "تحثّ واشنطن الطرفين على حلّ، فيما يعدّان مسوّدات لتسوية الرواتب والنفط، لكن الخلاف على شفافية النفط والجمارك والضرائب لا يزال يعرقل الاتفاق.",
                "bigStat": {"value": "41%", "label": "Share of entitlements transferred 2023–25",
                            "arabicLabel": "النسبة التي تقول أربيل إن بغداد حوّلتها فقط من مستحقات الإقليم المالية بين عامي 2023 و2025 (كردستان24)"},
                "supportingStats": [{"label": "الوسيط", "value": "واشنطن"},
                                     {"label": "العقدة", "value": "شفافية النفط"},
                                     {"label": "الأداة", "value": "مسوّدات"}],
                "broll": f"images/news/{s}/broll_3.jpg", "brolls": [f"images/news/{s}/broll_3.jpg"],
                "brollType": "image", "accent": ACCENTS[2], "brollSource": "Rudaw · 2026",
            },
        ],
        "sources": [{"name": "The New Arab", "domain": "newarab.com"},
                     {"name": "Rudaw", "domain": "rudaw.net"},
                     {"name": "Kurdistan24", "domain": "kurdistan24.net"},
                     {"name": "The Arab Weekly", "domain": "thearabweekly.com"}],
        "arabicTicker": [
            "تعثّر جديد في مفاوضات بغداد وأربيل حول الرواتب والنفط وسط تعمّق أزمة الرواتب (العربي الجديد · رووداو)",
            "النائب الأول لرئيس البرلمان عدنان فيحان يدعو لوقف التحويلات الاتحادية للإقليم حتى تُسوّى الإيرادات (الأسبوعية العربية)",
            "آلية آب 2025 تربط التحويلات بتحويل الإقليم 120 مليار دينار شهرياً من الإيرادات غير النفطية (الوكالة العراقية للأنباء)",
            "نحو 1.2 مليون موظف في الإقليم يعتمدون على رواتب تُقدَّر بنحو تريليون دينار شهرياً (مركز رووداو للأبحاث)",
            "أربيل: بغداد حوّلت 41% فقط من مستحقات الإقليم المالية بين عامي 2023 و2025 (كردستان24)",
            "واشنطن تحثّ الطرفين على حلّ، والجانبان يعدّان مسوّدات لتسوية الرواتب والنفط (رووداو)",
            "فهل تُنهي المسوّدات الجديدة أزمة رواتب كردستان، أم يتجدّد الخلاف؟",
        ],
    },
    "v11": {
        "slug": s, "kicker": "عاجل",
        "hookHeadline": "رواتب كردستان بخطر… ليش؟",
        "voText": "تعثّرت مفاوضات بغداد وأربيل حول الرواتب والنفط من جديد، بينما دعا النائب الأول لرئيس البرلمان عدنان فيحان إلى وقف التحويلات الاتحادية إلى الإقليم حتى تُسوّى الإيرادات، بحسب العربي الجديد ورووداو. ويعتمد نحو مليون ومئتي ألف موظف على رواتب تُقدَّر بنحو تريليون دينار شهرياً، وتقول أربيل إن بغداد حوّلت واحداً وأربعين في المئة فقط من مستحقاتها بين عامي ألفين وثلاثة وعشرين وألفين وخمسة وعشرين. وتحثّ واشنطن الطرفين على حلّ. فهل تُنهي المسوّدات الجديدة أزمة الرواتب، أم يتجدّد الخلاف؟",
        "endQuestion": "هل تُنهي المسوّدات الجديدة أزمة رواتب كردستان، أم يتجدّد الخلاف؟",
        "sourcesLine": "المصادر: العربي الجديد · رووداو · كردستان24",
        "images": imgs(s), "audioBed": "audio/mood_cinematic.mp3",
        "statPops": [{"value": "1.2M", "label": "موظف بالإقليم", "matchWord": "ومئتي"},
                      {"value": "41%", "label": "من المستحقات حُوّل", "matchWord": "وأربعين"}],
    },
    "caption": """رواتب موظفي كردستان — ليش تتأخر اليوم؟

مفاوضات بغداد–أربيل حول النفط والرواتب تتعثّر من جديد، وواشنطن تضغط لحلّ.

برأيك، الحل بالشفافية لو بضمان الرواتب أولاً؟

المصادر: العربي الجديد، رووداو، كردستان24
#العراق #كردستان #الرواتب #بغداد_أربيل
@photonect.news
""",
    "bucket": "iraq_economy",
}

# ─────────────────────────────────────────────────────────────────────────
# 3 — ARBAEEN ECONOMY  (P3 pride+econ · V11 · A)
# ─────────────────────────────────────────────────────────────────────────
s = f"{DATE}-arbaeen-economy"
SLUGS[s] = {
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/mood_orchestral.mp3", "topicBucket": "iraq_society", "variant": "A",
        "breaking": {
            "arabicKicker": "أربعينية · كربلاء",
            "arabicHeadline": "كربلاء تستعد لأكبر تجمّع في العالم",
            "englishSubhead": "AUG 4 | 20M+ PILGRIMS | ~$1.5B LOCAL ECONOMY",
            "heroMedia": f"images/news/{s}/hero.jpg", "heroMediaType": "image",
        },
        "beats": [
            {
                "label": "ماذا يحدث؟",
                "arabicHeading": "الأربعين في 4 آب… 20 مليون زائر",
                "arabicBody": "تستعد كربلاء لزيارة الأربعين في الرابع من آب، حيث تجمع سنوياً أكثر من 20 مليون زائر في واحد من أكبر التجمعات على وجه الأرض، بحسب شفق نيوز ووكالة ديد.",
                "bigStat": {"value": "20M+", "label": "Arbaeen pilgrims in Karbala",
                            "arabicLabel": "عدد الزوار الذين يتوافدون سنوياً إلى كربلاء في زيارة الأربعين، أحد أكبر التجمعات على الأرض (شفق نيوز · وكالة ديد)"},
                "supportingStats": [{"label": "الموعد", "value": "4 آب"},
                                     {"label": "الزوار", "value": "+20 مليون"},
                                     {"label": "الترتيب", "value": "الأكبر عالمياً"}],
                "broll": f"images/news/{s}/broll_1.jpg", "brolls": [f"images/news/{s}/broll_1.jpg"],
                "brollType": "image", "accent": ACCENTS[0], "brollSource": "Shafaq News · 2026",
            },
            {
                "label": "لماذا يهم؟",
                "arabicHeading": "1.5 مليار دولار تضخّها الزيارة",
                "arabicBody": "تحقن الزيارة نحو 1.5 مليار دولار في الاقتصاد المحلي، مع آلاف المواكب التي تقدّم الطعام والماء والمبيت مجاناً، ودخول أكثر من 4 ملايين زائر أجنبي العام الماضي.",
                "bigStat": {"value": "$1.5B", "label": "Injected into local economy",
                            "arabicLabel": "المبلغ التقديري الذي تضخّه زيارة الأربعين في اقتصاد كربلاء المحلي عبر الإيواء والنقل والطعام والتبادل (تقديرات اقتصادية)"},
                "supportingStats": [{"label": "الاقتصاد", "value": "~1.5 مليار $"},
                                     {"label": "زوار أجانب", "value": "+4 مليون"},
                                     {"label": "المواكب", "value": "بالآلاف"}],
                "broll": f"images/news/{s}/broll_2.jpg", "brolls": [f"images/news/{s}/broll_2.jpg"],
                "brollType": "image", "accent": ACCENTS[1], "brollSource": "Interior Ministry · 2024",
            },
            {
                "label": "ماذا بعد؟",
                "arabicHeading": "اختبار للخدمات والكهرباء في الذروة",
                "arabicBody": "يضع الحشد ضغطاً هائلاً على الكهرباء والخدمات في ذروة حرّ الصيف، فيما تحشد السلطات الأمن والصحة واللوجستيات لتأمين ملايين السائرين نحو المدينة.",
                "bigStat": {"value": "140", "label": "Nationalities of foreign pilgrims (2024)",
                            "arabicLabel": "عدد جنسيات الزوار الأجانب الذين دخلوا العراق خلال موسم الأربعين 2024 عبر المنافذ الحدودية (السلطات العراقية)"},
                "supportingStats": [{"label": "الضغط", "value": "كهرباء وخدمات"},
                                     {"label": "الجنسيات", "value": "140"},
                                     {"label": "الحشد", "value": "أمن وصحة"}],
                "broll": f"images/news/{s}/broll_3.jpg", "brolls": [f"images/news/{s}/broll_3.jpg"],
                "brollType": "image", "accent": ACCENTS[2], "brollSource": "The Media Line · 2026",
            },
        ],
        "sources": [{"name": "Shafaq News", "domain": "shafaq.com"},
                     {"name": "DID Press", "domain": "didpress.com"},
                     {"name": "The Media Line", "domain": "themedialine.org"},
                     {"name": "Borgen Project", "domain": "borgenproject.org"}],
        "arabicTicker": [
            "كربلاء تستعد لزيارة الأربعين في الرابع من آب، أحد أكبر التجمعات السنوية على وجه الأرض (شفق نيوز · وكالة ديد)",
            "الزيارة تجمع سنوياً أكثر من 20 مليون زائر، وبلغت 22.5 مليون في 2024 بحسب وزارة الداخلية",
            "تقديرات اقتصادية: الزيارة تضخّ نحو 1.5 مليار دولار في الاقتصاد المحلي لكربلاء",
            "أكثر من 4 ملايين زائر أجنبي من 140 جنسية دخلوا العراق خلال موسم الأربعين 2024 (السلطات العراقية)",
            "آلاف المواكب تقدّم الطعام والماء والمبيت مجاناً للسائرين على طول الطريق إلى كربلاء",
            "الحشد يضع ضغطاً هائلاً على الكهرباء والخدمات في ذروة حرّ الصيف (ميديا لاين)",
            "فهل تحوّل كربلاء زخم الأربعين إلى مكسب اقتصادي دائم؟",
        ],
    },
    "v11": {
        "slug": s, "kicker": "أربعينية",
        "hookHeadline": "أكبر تجمّع بالعالم… بكربلاء",
        "voText": "تستعد مدينة كربلاء لزيارة الأربعين في الرابع من آب، حيث تجمع سنوياً أكثر من عشرين مليون زائر في واحد من أكبر التجمّعات على وجه الأرض، بحسب شفق نيوز ووكالة ديد. وتحقن الزيارة نحو مليار ونصف المليار دولار في الاقتصاد المحلي، مع آلاف المواكب التي تقدّم خدماتها مجاناً، ودخول أكثر من أربعة ملايين زائر أجنبي العام الماضي. لكن الحشد يضع ضغطاً هائلاً على الكهرباء والخدمات في ذروة الصيف. فهل تحوّل كربلاء هذا الزخم إلى مكسب دائم؟",
        "endQuestion": "هل تحوّل كربلاء زخم الأربعين إلى مكسب اقتصادي دائم؟",
        "sourcesLine": "المصادر: شفق نيوز · وكالة ديد · ميديا لاين",
        "images": imgs(s), "audioBed": "audio/mood_orchestral.mp3",
        "statPops": [{"value": "20M+", "label": "زائر", "matchWord": "عشرين"},
                      {"value": "$1.5B", "label": "للاقتصاد المحلي", "matchWord": "ونصف"}],
    },
    "caption": """زيارة الأربعين 2026 في كربلاء — متى وكم زائر؟

أكثر من 20 مليون زائر و1.5 مليار دولار تضخّها الزيارة في اقتصاد المدينة.

برأيك، تكدر كربلاء تحوّل الأربعين لاقتصاد دائم؟

المصادر: شفق نيوز، وكالة ديد، ميديا لاين
#العراق #كربلاء #الأربعين #زيارة_الاربعين
@photonect.news
""",
    "bucket": "iraq_society",
}

# ─────────────────────────────────────────────────────────────────────────
# 4 — OPEC PRICE SQUEEZE  (P2 gulf-econ · V10 CONTROL · B)  — NO v11 brief
# ─────────────────────────────────────────────────────────────────────────
s = f"{DATE}-opec-price-squeeze"
SLUGS[s] = {
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/mood_mideast.mp3", "topicBucket": "iraq_economy", "variant": "B",
        "breaking": {
            "arabicKicker": "نفط · أوبك",
            "arabicHeadline": "أوبك تزيد الضخّ… وموازنة العراق تحت الضغط",
            "englishSubhead": "+188K BPD AUG | $60 BUDGET PRICE | 90% OIL-RELIANT",
            "heroMedia": f"images/news/{s}/hero.jpg", "heroMediaType": "image",
        },
        "beats": [
            {
                "label": "ماذا يحدث؟",
                "arabicHeading": "أوبك+ ترفع الإنتاج 188 ألف برميل",
                "arabicBody": "ترفع أوبك+ إنتاجها 188 ألف برميل يومياً من آب، في خامس زيادة شهرية على التوالي، بمشاركة السعودية وروسيا والعراق، بحسب الجزيرة ووكالة الطاقة الدولية.",
                "bigStat": {"value": "188K", "label": "Barrels/day August hike",
                            "arabicLabel": "حجم الزيادة اليومية في إنتاج أوبك+ اعتباراً من آب، وهي الخامسة على التوالي بمشاركة العراق (الجزيرة · وكالة الطاقة الدولية)"},
                "supportingStats": [{"label": "الزيادة", "value": "188 ألف ب/ي"},
                                     {"label": "التسلسل", "value": "الخامسة"},
                                     {"label": "من", "value": "آب"}],
                "broll": f"images/news/{s}/broll_1.jpg", "brolls": [f"images/news/{s}/broll_1.jpg"],
                "brollType": "image", "accent": ACCENTS[0], "brollSource": "Al Jazeera · IEA",
            },
            {
                "label": "لماذا يهم؟",
                "arabicHeading": "سعر أقل للبرميل… عائد أقل للعراق",
                "arabicBody": "تراجع أسعار النفط مع هدنة واشنطن–طهران يعني عائداً أقل للعراق، الذي تعتمد موازنته بنحو 90% على النفط بسعر افتراضي 60 دولاراً للبرميل.",
                "bigStat": {"value": "90%", "label": "Budget reliance on oil",
                            "arabicLabel": "نسبة اعتماد الموازنة العامة العراقية على عائدات النفط، ما يجعلها شديدة الحساسية لأي تراجع في الأسعار (الشرق الأوسط)"},
                "supportingStats": [{"label": "اعتماد الموازنة", "value": "90%"},
                                     {"label": "السعر الافتراضي", "value": "60 $"},
                                     {"label": "السبب", "value": "هدنة وهرمز"}],
                "broll": f"images/news/{s}/broll_2.jpg", "brolls": [f"images/news/{s}/broll_2.jpg"],
                "brollType": "image", "accent": ACCENTS[1], "brollSource": "Asharq Al-Awsat · AGBI",
            },
            {
                "label": "ماذا بعد؟",
                "arabicHeading": "عجز 5 مليارات… وضغط على الرواتب",
                "arabicBody": "سجّل العراق عجزاً بـ5 مليارات دولار في 4 أشهر، والرواتب وحدها 15.3 مليار، ما يزيد الضغط لإقرار موازنة كاملة بأسرع وقت، بحسب AGBI وأكاديميين.",
                "bigStat": {"value": "$5B", "label": "4-month budget deficit",
                            "arabicLabel": "العجز الذي سجّلته موازنة العراق في الأشهر الأربعة الأولى من 2026 بعد تراجع عائدات النفط إثر حرب إيران (AGBI)"},
                "supportingStats": [{"label": "العجز", "value": "5 مليار $"},
                                     {"label": "الرواتب", "value": "15.3 مليار $"},
                                     {"label": "المطلوب", "value": "موازنة كاملة"}],
                "broll": f"images/news/{s}/broll_3.jpg", "brolls": [f"images/news/{s}/broll_3.jpg"],
                "brollType": "image", "accent": ACCENTS[2], "brollSource": "AGBI · 2026",
            },
        ],
        "sources": [{"name": "Al Jazeera", "domain": "aljazeera.com"},
                     {"name": "IEA", "domain": "iea.org"},
                     {"name": "AGBI", "domain": "agbi.com"},
                     {"name": "Asharq Al-Awsat", "domain": "aawsat.com"}],
        "arabicTicker": [
            "أوبك+ ترفع إنتاجها 188 ألف برميل يومياً اعتباراً من آب، في خامس زيادة شهرية على التوالي (الجزيرة · وكالة الطاقة الدولية)",
            "الزيادة بمشاركة السعودية وروسيا والعراق والكويت وكازاخستان والجزائر وعُمان (الجزيرة)",
            "تراجع أسعار النفط مع الهدنة الأميركية–الإيرانية وعودة تدفقات مضيق هرمز (وكالة الطاقة الدولية)",
            "موازنة العراق تعتمد بنحو 90% على النفط بسعر افتراضي 60 دولاراً للبرميل (الشرق الأوسط)",
            "العراق سجّل عجزاً بنحو 5 مليارات دولار في الأشهر الأربعة الأولى من 2026 (AGBI)",
            "الرواتب وحدها بلغت 15.3 مليار دولار، أي أكثر من نصف الإنفاق، ما يضغط لإقرار موازنة كاملة (AGBI)",
            "فهل تنجح الحكومة في إقرار موازنة كاملة وسط تراجع أسعار النفط؟",
        ],
    },
    "v11": None,  # silent V10.1 control
    "caption": """سعر النفط والموازنة العراقية — شنو العلاقة بجيبتك؟

أوبك ترفع الإنتاج والأسعار تنزل، بينما 90% من موازنة العراق تعتمد على النفط.

برأيك، تنجح الحكومة تقرّ موازنة كاملة بهذا الضغط؟

المصادر: الجزيرة، وكالة الطاقة الدولية، AGBI
#العراق #النفط #أوبك #الموازنة
@photonect.news
""",
    "bucket": "iraq_economy",
}

# ─────────────────────────────────────────────────────────────────────────
# 5 — GRAFT CONCEALMENT  (P1 corruption · V11 · B)
# ─────────────────────────────────────────────────────────────────────────
s = f"{DATE}-graft-concealment"
SLUGS[s] = {
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/mood_cinematic.mp3", "topicBucket": "iraq_politics", "variant": "B",
        "breaking": {
            "arabicKicker": "فساد · صولة الفجر",
            "arabicHeadline": "فين خبّوا الملايين؟ صولة الفجر تكشف",
            "englishSubhead": "67 ARRESTED | $100M+ CASH | 375KG GOLD",
            "heroMedia": f"images/news/{s}/hero.jpg", "heroMediaType": "image",
        },
        "beats": [
            {
                "label": "ماذا يحدث؟",
                "arabicHeading": "67 مسؤولاً موقوفاً في حملة واحدة",
                "arabicBody": "أوقفت حملة «صولة الفجر» التي أطلقها رئيس الوزراء علي الزيدي أواخر حزيران نحو 67 مسؤولاً ونائباً، وصادرت أكثر من 100 مليون دولار نقداً، بحسب برس تي في والجزيرة.",
                "bigStat": {"value": "67", "label": "Officials arrested",
                            "arabicLabel": "عدد المسؤولين والنواب الذين أوقفتهم حملة صولة الفجر لمكافحة الفساد منذ إطلاقها أواخر حزيران (برس تي في)"},
                "supportingStats": [{"label": "موقوفون", "value": "67"},
                                     {"label": "نقد مصادَر", "value": "+100 مليون $"},
                                     {"label": "الإطلاق", "value": "حزيران"}],
                "broll": f"images/news/{s}/broll_1.jpg", "brolls": [f"images/news/{s}/broll_1.jpg"],
                "brollType": "image", "accent": ACCENTS[0], "brollSource": "Press TV · Al Jazeera",
            },
            {
                "label": "لماذا يهم؟",
                "arabicHeading": "أموال في قناني ماء وجدران ومجارٍ",
                "arabicBody": "كشفت المداهمات أموالاً مخبّأة في قناني ماء وداخل جدران وحتى في مجرى تصريف، شملت 20 مليون دولار في تكريت و11 مليوناً في بالوعة، بحسب ذا ناشونال وOCCRP.",
                "bigStat": {"value": "375kg", "label": "Gold recovered",
                            "arabicLabel": "كمية الذهب التي استردّتها السلطات ضمن تحقيقات صولة الفجر لمكافحة الفساد (الجزيرة · ذا ناشونال)"},
                "supportingStats": [{"label": "ذهب مستردّ", "value": "375 كغ"},
                                     {"label": "قناني ماء", "value": "20 مليون $"},
                                     {"label": "بالوعة", "value": "11 مليون $"}],
                "broll": f"images/news/{s}/broll_2.jpg", "brolls": [f"images/news/{s}/broll_2.jpg"],
                "brollType": "image", "accent": ACCENTS[1], "brollSource": "The National · OCCRP",
            },
            {
                "label": "ماذا بعد؟",
                "arabicHeading": "150 ملياراً ضاعت منذ 2003",
                "arabicBody": "تقدّر تقارير خسائر الفساد بنحو 150 مليار دولار منذ 2003، فيما يبحث القضاء تخفيف الأحكام مقابل إعادة الأموال، وسط انقسام سياسي حول مدى الحملة.",
                "bigStat": {"value": "$150B", "label": "Lost to corruption since 2003",
                            "arabicLabel": "التقدير الذي تورده تقارير لحجم الأموال العامة التي خسرها العراق بسبب الفساد منذ عام 2003 (ذا ناشونال)"},
                "supportingStats": [{"label": "منذ 2003", "value": "~150 مليار $"},
                                     {"label": "القضاء", "value": "تخفيف مقابل إعادة"},
                                     {"label": "السياق", "value": "انقسام سياسي"}],
                "broll": f"images/news/{s}/broll_3.jpg", "brolls": [f"images/news/{s}/broll_3.jpg"],
                "brollType": "image", "accent": ACCENTS[2], "brollSource": "The National · 2026",
            },
        ],
        "sources": [{"name": "The National", "domain": "thenationalnews.com"},
                     {"name": "OCCRP", "domain": "occrp.org"},
                     {"name": "Al Jazeera", "domain": "aljazeera.com"},
                     {"name": "Press TV", "domain": "presstv.ir"}],
        "arabicTicker": [
            "حملة «صولة الفجر» التي أطلقها رئيس الوزراء علي الزيدي أواخر حزيران توقف نحو 67 مسؤولاً ونائباً (برس تي في · الجزيرة)",
            "المداهمات صادرت أكثر من 100 مليون دولار نقداً في إطار الحملة المتوسّعة (الجزيرة)",
            "أموال مخبّأة في قناني ماء وداخل جدران وحتى في مجرى تصريف كشفتها التحقيقات (ذا ناشونال · OCCRP)",
            "20 مليون دولار في تكريت و11 مليوناً في بالوعة ضمن قضية وكيل وزارة النفط (ذا ناشونال)",
            "السلطات تستردّ نحو 375 كيلوغراماً من الذهب ضمن تحقيقات مكافحة الفساد (الجزيرة)",
            "تقارير تقدّر خسائر الفساد بنحو 150 مليار دولار منذ 2003، والقضاء يبحث تخفيف الأحكام مقابل إعادة الأموال (ذا ناشونال)",
            "فوين راحت باقي المليارات… وهل تصل الحملة إلى النهاية؟",
        ],
    },
    "v11": {
        "slug": s, "kicker": "عاجل",
        "hookHeadline": "فين خبّوا الملايين؟",
        "voText": "أوقفت حملة صولة الفجر التي أطلقها رئيس الوزراء علي الزيدي نحو سبعة وستين مسؤولاً ونائباً، وصادرت أكثر من مئة مليون دولار نقداً، بحسب برس تي في والجزيرة. وكشفت المداهمات أموالاً مخبّأة في قناني ماء وجدران ومجرى تصريف، شملت عشرين مليون دولار في تكريت وأحد عشر مليوناً في بالوعة، إضافة إلى ثلاثمئة وخمسة وسبعين كيلوغراماً من الذهب. وتقدّر تقارير خسائر الفساد بنحو مئة وخمسين مليار دولار منذ عام ألفين وثلاثة. فهل تصل الحملة إلى النهاية، أم تتوقف عند أول خط أحمر؟",
        "endQuestion": "هل تصل صولة الفجر إلى النهاية، أم تتوقف عند أول خط أحمر؟",
        "sourcesLine": "المصادر: ذا ناشونال · OCCRP · الجزيرة",
        "images": imgs(s), "audioBed": "audio/mood_cinematic.mp3",
        "statPops": [{"value": "67", "label": "مسؤولاً موقوفاً", "matchWord": "وستين"},
                      {"value": "375kg", "label": "ذهب مستردّ", "matchWord": "وسبعين"}],
    },
    "caption": """صولة الفجر بالعراق — وين انخبّت الملايين؟

67 موقوفاً وأكثر من 100 مليون دولار نقداً وُجدت في قناني ماء وجدران ومجارٍ.

برأيك، وين راحت باقي المليارات؟

المصادر: ذا ناشونال، OCCRP، الجزيرة
#العراق #الفساد #صولة_الفجر #محاسبة
@photonect.news
""",
    "bucket": "iraq_politics",
}


def main():
    for slug, data in SLUGS.items():
        d = POSTS / slug
        meta = d / ".meta"
        meta.mkdir(parents=True, exist_ok=True)
        (meta / "props.json").write_text(json.dumps(data["props"], ensure_ascii=False, indent=2), encoding="utf-8")
        (d / "caption.txt").write_text(data["caption"], encoding="utf-8")
        (meta / "media-stamp.json").write_text(
            json.dumps({"hunted_at": f"{DATE}T11:00:00+00:00", "bucket": data["bucket"]}, ensure_ascii=False, indent=2),
            encoding="utf-8")
        if data["v11"]:
            (meta / "v11-brief.json").write_text(json.dumps(data["v11"], ensure_ascii=False, indent=2), encoding="utf-8")
            v11flag = "V11"
        else:
            v11flag = "V10-control"
        print(f"  wrote {slug}  [{v11flag}]")
    print(f"\n{len(SLUGS)} slugs authored for {DATE}")


if __name__ == "__main__":
    main()
