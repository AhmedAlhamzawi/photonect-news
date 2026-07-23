#!/usr/bin/env python3
"""Author the 2026-07-23 Photonect NEWS slate.

5 slugs (Iraq/MENA money-power lens):
  1 graft-saladin-airways        P1 corruption   V11  A   (LEAD)
  2 salaries-run-late            P1 money        V11  B
  3 iraq-sprint-national-record  P3 pride        V11  A
  4 uae-us-ai-chips-greenlight   P2 gulf/AI      V11  B
  5 iraq-projects-boom-despite-war P1 jobs       V10  A   <- silent control

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
DATE = "2026-07-23"
DATE_LABEL = "JUL 23 • 2026"
AR_DATE = "23 يوليو 2026"
HANDLE = "@photonect.news"
ACCENTS = ["#FFC217", "#FF6B3D", "#D72638"]
STAMP = {"hunted_at": f"{DATE}T11:00:00+00:00"}


def imgs(slug):
    return [f"images/news/{slug}/{n}" for n in ("hero.jpg", "broll_1.jpg", "broll_2.jpg", "broll_3.jpg")]


SLUGS = {}

# ─────────────────────────────────────────────────────────────────────────
# 1 — GRAFT SPREADS TO AVIATION + BORDERS + SALADIN  (P1 corruption · V11 · A · LEAD)
# ─────────────────────────────────────────────────────────────────────────
s = f"{DATE}-graft-saladin-airways"
SLUGS[s] = {
    "bucket": "iraq_politics",
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/mood_newsroom.mp3", "topicBucket": "iraq_politics", "variant": "A",
        "breaking": {
            "arabicKicker": "فساد · صولة الفجر",
            "arabicHeadline": "الحملة توصل للطيران والمنافذ… 55 مذكرة",
            "englishSubhead": "55 WARRANTS IN SALADIN | AIRWAYS + BORDERS SWEPT",
            "heroMedia": f"images/news/{s}/hero.jpg", "heroMediaType": "image",
        },
        "beats": [
            {
                "label": "ماذا يحدث؟",
                "arabicHeading": "الحملة تتوسع إلى قطاعات جديدة",
                "arabicBody": "أوقفت حملة صولة الفجر لمكافحة الفساد 35 مسؤولاً خلال أسبوع واحد في ست قضايا وخمس محافظات وسبعة قطاعات، بحسب شفق نيوز.",
                "bigStat": {"value": "35", "label": "Officials held in one week",
                            "arabicLabel": "عدد المسؤولين الموقوفين خلال أسبوع واحد ضمن ست قضايا وخمس محافظات وسبعة قطاعات (شفق نيوز)"},
                "supportingStats": [{"label": "موقوفون", "value": "35 مسؤول"},
                                     {"label": "قضايا", "value": "6"},
                                     {"label": "محافظات", "value": "5"}],
                "broll": f"images/news/{s}/broll_1.jpg", "brolls": [f"images/news/{s}/broll_1.jpg"],
                "brollType": "image", "accent": ACCENTS[0], "brollSource": "Shafaq News · 2026",
            },
            {
                "label": "لماذا يهم؟",
                "arabicHeading": "الطيران والمنافذ الحدودية في القبضة",
                "arabicBody": "طالت الحملة الخطوط الجوية العراقية بإيقاف 8 من كبار موظفيها وفقدان 16 مليار دينار (نحو 12 مليون دولار)، كما شملت منفذاً حدودياً في كركوك، بحسب شفق نيوز.",
                "bigStat": {"value": "16 مليار", "label": "IQD missing at Iraqi Airways",
                            "arabicLabel": "قيمة الأموال المفقودة في الخطوط الجوية العراقية بالدينار (نحو 12 مليون دولار) مع إيقاف 8 من كبار موظفيها (شفق نيوز)"},
                "supportingStats": [{"label": "الخطوط الجوية", "value": "8 موقوفين"},
                                     {"label": "مفقود", "value": "16 مليار د"},
                                     {"label": "المنافذ", "value": "كركوك"}],
                "broll": f"images/news/{s}/broll_2.jpg", "brolls": [f"images/news/{s}/broll_2.jpg"],
                "brollType": "image", "accent": ACCENTS[1], "brollSource": "Shafaq News · 2026",
            },
            {
                "label": "ماذا بعد؟",
                "arabicHeading": "صلاح الدين مغلقة… 55 مذكرة توقيف",
                "arabicBody": "أصدرت هيئة النزاهة 55 مذكرة توقيف في صلاح الدين. ومنذ انطلاق الحملة أواخر حزيران أُوقف أكثر من 70 مسؤولاً وصودر 127 مليار دينار و24 مليون دولار، بحسب الجزيرة وسي بي إس.",
                "bigStat": {"value": "70+", "label": "Officials held since late June",
                            "arabicLabel": "إجمالي المسؤولين الموقوفين منذ انطلاق الحملة أواخر حزيران مع مصادرة 127 مليار دينار و24 مليون دولار (الجزيرة · سي بي إس)"},
                "supportingStats": [{"label": "صلاح الدين", "value": "55 مذكرة"},
                                     {"label": "تراكمي", "value": "70+ موقوف"},
                                     {"label": "مصادرات", "value": "127 مليار د"}],
                "broll": f"images/news/{s}/broll_3.jpg", "brolls": [f"images/news/{s}/broll_3.jpg"],
                "brollType": "image", "accent": ACCENTS[2], "brollSource": "Al Jazeera · CBS · 2026",
            },
        ],
        "sources": [
            {"name": "Shafaq News", "domain": "shafaq.com"},
            {"name": "Al Jazeera", "domain": "aljazeera.com"},
            {"name": "CBS News", "domain": "cbsnews.com"},
        ],
        "arabicTicker": [
            "حملة صولة الفجر توقف 35 مسؤولاً خلال أسبوع واحد في ست قضايا وخمس محافظات وسبعة قطاعات (شفق نيوز)",
            "الخطوط الجوية العراقية: إيقاف 8 من كبار الموظفين وفقدان 16 مليار دينار نحو 12 مليون دولار (شفق نيوز)",
            "الحملة تطال منفذاً حدودياً في كركوك ضمن توسعها إلى قطاعات جديدة (شفق نيوز)",
            "هيئة النزاهة تصدر 55 مذكرة توقيف في محافظة صلاح الدين (شفق نيوز)",
            "منذ انطلاق الحملة أواخر حزيران: أكثر من 70 مسؤولاً موقوفاً (الجزيرة · سي بي إس)",
            "مصادرات الحملة التراكمية: 127 مليار دينار و24 مليون دولار وعقارات وذهب (الجزيرة · سي بي إس)",
            "فهل تصل المحاسبة إلى كل الوزارات، أم تتوقف عند حد؟",
        ],
    },
    "caption": """حملة صولة الفجر بالعراق — لوين وصلت اليوم؟

الحملة تدخل الطيران والمنافذ الحدودية، وصلاح الدين تحت 55 مذكرة توقيف.

برأيك، توصل المحاسبة لكل الوزارات لو تتوقف عند حد؟

المصادر: شفق نيوز، الجزيرة، CBS
#العراق #الفساد #صولة_الفجر #محاسبة
@photonect.news""",
    "v11": {
        "slug": s, "kicker": "عاجل",
        "hookHeadline": "صولة الفجر… توصل للطيران؟",
        "voText": "تتوسع حملة صولة الفجر لمكافحة الفساد في العراق إلى قطاعات جديدة. فبحسب شفق نيوز، جرى توقيف خمسة وثلاثين مسؤولاً خلال أسبوع واحد في ست قضايا وخمس محافظات. وطالت الحملة الخطوط الجوية العراقية بإيقاف ثمانية من كبار موظفيها وفقدان ستة عشر مليار دينار، كما شملت منفذاً حدودياً. وفي صلاح الدين صدرت خمس وخمسون مذكرة توقيف. ومنذ انطلاقها أواخر حزيران أُوقف أكثر من سبعين مسؤولاً. فهل تصل المحاسبة إلى كل الوزارات، أم تتوقف عند حد؟",
        "endQuestion": "هل تصل المحاسبة إلى كل الوزارات، أم تتوقف عند حد؟",
        "sourcesLine": "المصادر: شفق نيوز · الجزيرة · CBS",
        "images": imgs(s), "audioBed": "audio/mood_newsroom.mp3",
        "statPops": [
            {"value": "55 مذكرة", "label": "صلاح الدين", "matchWord": "وخمسون"},
            {"value": "16 مليار", "label": "الخطوط الجوية", "matchWord": "عشر"},
        ],
    },
}

# ─────────────────────────────────────────────────────────────────────────
# 2 — JULY SALARIES RUN LATE  (P1 money · V11 · B)
# ─────────────────────────────────────────────────────────────────────────
s = f"{DATE}-salaries-run-late"
SLUGS[s] = {
    "bucket": "iraq_economy",
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/mood_newsroom.mp3", "topicBucket": "iraq_economy", "variant": "B",
        "breaking": {
            "arabicKicker": "رواتب · تأخير",
            "arabicHeadline": "راتبك تأخّر؟ الحكومة تشرح السبب",
            "englishSubhead": "JULY PAY LATE ACROSS MINISTRIES | STATE BLAMES 'TECH FAULT'",
            "heroMedia": f"images/news/{s}/hero.jpg", "heroMediaType": "image",
        },
        "beats": [
            {
                "label": "ماذا يحدث؟",
                "arabicHeading": "تأخّر صرف رواتب تموز في معظم الوزارات",
                "arabicBody": "تأخّر صرف رواتب موظفي الدولة هذا الشهر عبر معظم الوزارات، خلافاً للمعتاد في مطلع العشرين من كل شهر، بحسب شبكة 964.",
                "bigStat": {"value": "تموز", "label": "Pay delayed across ministries",
                            "arabicLabel": "شهر تموز الذي تأخّر فيه صرف الرواتب عبر معظم الوزارات خلافاً للمعتاد في مطلع العشرين من الشهر (شبكة 964)"},
                "supportingStats": [{"label": "الشهر", "value": "تموز"},
                                     {"label": "النطاق", "value": "معظم الوزارات"},
                                     {"label": "المعتاد", "value": "بعد الـ20"}],
                "broll": f"images/news/{s}/broll_1.jpg", "brolls": [f"images/news/{s}/broll_1.jpg"],
                "brollType": "image", "accent": ACCENTS[0], "brollSource": "964media · 2026",
            },
            {
                "label": "لماذا يهم؟",
                "arabicHeading": "8 تريليون دينار شهرياً… والسبب تقني",
                "arabicBody": "تحتاج الدولة نحو 8 تريليون دينار شهرياً للرواتب والمعاشات والحماية الاجتماعية، وتؤكد المالية أن السبب أعطال تقنية في التحويل الإلكتروني لا نقص سيولة، بحسب وكالة الأنباء العراقية و964.",
                "bigStat": {"value": "8 تريليون", "label": "IQD monthly payroll",
                            "arabicLabel": "قيمة ما تحتاجه الدولة شهرياً بالدينار للرواتب والمعاشات والحماية الاجتماعية (وكالة الأنباء العراقية · شبكة 964)"},
                "supportingStats": [{"label": "شهرياً", "value": "8 تريليون د"},
                                     {"label": "السبب", "value": "عطل تقني"},
                                     {"label": "المالية", "value": "مو سيولة"}],
                "broll": f"images/news/{s}/broll_2.jpg", "brolls": [f"images/news/{s}/broll_2.jpg"],
                "brollType": "image", "accent": ACCENTS[1], "brollSource": "INA · 964media",
            },
            {
                "label": "ماذا بعد؟",
                "arabicHeading": "صرف 1/12 بلا موازنة 2026",
                "arabicBody": "يجري الصرف وفق قاعدة 1/12 الشهرية بموجب قانون الإدارة المالية المعدّل رقم 6 لسنة 2019 من دون موازنة لعام 2026، فيما تنفي المالية تسييس التأخير، بحسب 964 وكردستان24.",
                "bigStat": {"value": "1/12", "label": "Monthly spending rule, no budget",
                            "arabicLabel": "قاعدة الصرف الشهرية بواحد من اثني عشر بموجب قانون الإدارة المالية المعدّل من دون إقرار موازنة 2026 (شبكة 964 · كردستان24)"},
                "supportingStats": [{"label": "الموازنة", "value": "لا 2026"},
                                     {"label": "الصرف", "value": "1/12 شهري"},
                                     {"label": "المالية", "value": "تنفي التسييس"}],
                "broll": f"images/news/{s}/broll_3.jpg", "brolls": [f"images/news/{s}/broll_3.jpg"],
                "brollType": "image", "accent": ACCENTS[2], "brollSource": "964media · Kurdistan24",
            },
        ],
        "sources": [
            {"name": "964media", "domain": "964media.com"},
            {"name": "Iraqi News Agency", "domain": "ina.iq"},
            {"name": "Kurdistan24", "domain": "kurdistan24.net"},
        ],
        "arabicTicker": [
            "تأخّر صرف رواتب موظفي الدولة في العراق هذا الشهر عبر معظم الوزارات خلافاً للمعتاد (شبكة 964)",
            "وزارة المالية: التأخير سببه أعطال تقنية في أنظمة التحويل الإلكتروني لا نقص في السيولة (شبكة 964)",
            "الدولة تحتاج نحو 8 تريليون دينار شهرياً للرواتب والمعاشات والحماية الاجتماعية (وكالة الأنباء العراقية)",
            "الصرف يجري وفق قاعدة 1/12 الشهرية بموجب قانون الإدارة المالية المعدّل رقم 6 لسنة 2019 (شبكة 964)",
            "لا موازنة لعام 2026 حتى الآن، والإنفاق يسير على قاعدة الاثني عشرية (شبكة 964)",
            "المالية تنفي تسييس تأخير صرف رواتب المتقاعدين وتؤكد أنه تقني بحت (كردستان24)",
            "فهل تأخير تموز عطل تقني عابر، أم بداية أزمة رواتب؟",
        ],
    },
    "caption": """تأخر الرواتب في العراق تموز 2026 — شنو السبب؟

معظم الوزارات صرفت رواتبها متأخرة، والمالية تقول السبب تقني مو نقص سيولة.

راتبك وصل بموعده لو تأخر هالشهر؟

المصادر: 964، الأنباء العراقية، كردستان24
#العراق #الرواتب #وزارة_المالية #موازنة
@photonect.news""",
    "v11": {
        "slug": s, "kicker": "عاجل",
        "hookHeadline": "راتبك تأخّر؟ هذا السبب",
        "voText": "تأخّر صرف رواتب موظفي الدولة في العراق هذا الشهر عبر معظم الوزارات، خلافاً للمعتاد في مطلع العشرين من كل شهر. وبحسب شبكة 964، أرجعت وزارة المالية التأخير إلى أعطال تقنية في أنظمة التحويل الإلكتروني، لا إلى نقص في السيولة. وتحتاج الدولة إلى نحو ثمانية تريليونات دينار شهرياً للرواتب والمعاشات والحماية الاجتماعية. ويجري الصرف وفق قاعدة واحد من اثني عشر من دون موازنة لعام ألفين وستة وعشرين. فهل التأخير عطل تقني عابر، أم بداية أزمة رواتب؟",
        "endQuestion": "هل التأخير عطل تقني عابر، أم بداية أزمة رواتب؟",
        "sourcesLine": "المصادر: 964 · الأنباء العراقية · كردستان24",
        "images": imgs(s), "audioBed": "audio/mood_newsroom.mp3",
        "statPops": [
            {"value": "8 تريليون", "label": "رواتب شهرياً", "matchWord": "ثمانية"},
            {"value": "1/12", "label": "قاعدة الصرف", "matchWord": "اثني"},
        ],
    },
}

# ─────────────────────────────────────────────────────────────────────────
# 3 — IRAQI SPRINT NATIONAL RECORD  (P3 pride · V11 · A)
# ─────────────────────────────────────────────────────────────────────────
s = f"{DATE}-iraq-sprint-national-record"
SLUGS[s] = {
    "bucket": "sports",
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/mood_hamasi.mp3", "topicBucket": "sports", "variant": "A",
        "breaking": {
            "arabicKicker": "رياضة · فخر",
            "arabicHeadline": "عراقي يكسر رقم العراق… 10.21 ثانية",
            "englishSubhead": "IRAQI NATIONAL RECORD 10.21s | 100m SILVER IN ASIA",
            "heroMedia": f"images/news/{s}/hero.jpg", "heroMediaType": "image",
        },
        "beats": [
            {
                "label": "ماذا يحدث؟",
                "arabicHeading": "رقم قياسي وطني جديد في المئة متر",
                "arabicBody": "سجّل العداء العراقي فلاح الخزاعي رقماً قياسياً وطنياً جديداً في سباق المئة متر بزمن 10.21 ثانية، وخطف الفضية في أول بطولة آسيوية تحت 23 عاماً، بحسب الاتحاد الدولي لألعاب القوى.",
                "bigStat": {"value": "10.21 ث", "label": "New Iraqi national record",
                            "arabicLabel": "الزمن القياسي الوطني الجديد للعراق في سباق المئة متر الذي سجّله فلاح الخزاعي (الاتحاد الدولي لألعاب القوى)"},
                "supportingStats": [{"label": "الزمن", "value": "10.21 ث"},
                                     {"label": "الميدالية", "value": "فضية 100م"},
                                     {"label": "الحدث", "value": "آسيا U23"}],
                "broll": f"images/news/{s}/broll_1.jpg", "brolls": [f"images/news/{s}/broll_1.jpg"],
                "brollType": "image", "accent": ACCENTS[0], "brollSource": "World Athletics · 2026",
            },
            {
                "label": "لماذا يهم؟",
                "arabicHeading": "0.04 ثانية فقط عن الذهب",
                "arabicBody": "جاء الذهب للماليزي عظيم فهمي بزمن 10.17 ثانية، بفارق 4 أجزاء من المئة فقط عن الخزاعي، في نهائي أقيم بمدينة أوردوس الصينية، بحسب الاتحاد الدولي وذا ستار.",
                "bigStat": {"value": "0.04 ث", "label": "Gap to gold",
                            "arabicLabel": "الفارق الزمني بين الخزاعي وبطل الذهب الماليزي عظيم فهمي الذي سجّل 10.17 ثانية في نهائي أوردوس (الاتحاد الدولي · ذا ستار)"},
                "supportingStats": [{"label": "الذهب", "value": "10.17 ث"},
                                     {"label": "الفارق", "value": "0.04 ث"},
                                     {"label": "المكان", "value": "أوردوس"}],
                "broll": f"images/news/{s}/broll_2.jpg", "brolls": [f"images/news/{s}/broll_2.jpg"],
                "brollType": "image", "accent": ACCENTS[1], "brollSource": "World Athletics · The Star",
            },
            {
                "label": "ماذا بعد؟",
                "arabicHeading": "جيل عراقي صاعد على المضمار",
                "arabicBody": "الإنجاز يعيد رسم رقم العراق في الركض ويضع الخزاعي ضمن جيل شبابي صاعد في ألعاب القوى، يطمح لأول ميدالية عراقية على المستوى العالمي في السرعة.",
                "bigStat": {"value": "U23", "label": "Rising youth generation",
                            "arabicLabel": "بطولة آسيا تحت 23 عاماً التي برز فيها جيل عراقي شبابي صاعد في ألعاب القوى بقيادة فلاح الخزاعي (الاتحاد الدولي لألعاب القوى)"},
                "supportingStats": [{"label": "البطل", "value": "الخزاعي"},
                                     {"label": "الفئة", "value": "آسيا U23"},
                                     {"label": "الطموح", "value": "جيل صاعد"}],
                "broll": f"images/news/{s}/broll_3.jpg", "brolls": [f"images/news/{s}/broll_3.jpg"],
                "brollType": "image", "accent": ACCENTS[2], "brollSource": "World Athletics · 2026",
            },
        ],
        "sources": [
            {"name": "World Athletics", "domain": "worldathletics.org"},
            {"name": "The Star", "domain": "thestar.com.my"},
            {"name": "Iraqi News", "domain": "iraqinews.com"},
        ],
        "arabicTicker": [
            "العداء العراقي فلاح الخزاعي يسجّل رقماً قياسياً وطنياً جديداً في المئة متر بزمن 10.21 ثانية (الاتحاد الدولي لألعاب القوى)",
            "الخزاعي يخطف الميدالية الفضية في نهائي المئة متر بأول بطولة آسيوية تحت 23 عاماً (الاتحاد الدولي لألعاب القوى)",
            "الذهب للماليزي عظيم فهمي بزمن 10.17 ثانية بفارق 4 أجزاء من المئة فقط (الاتحاد الدولي · ذا ستار)",
            "النهائي أقيم في مدينة أوردوس الصينية ضمن أول نسخة من بطولة آسيا تحت 23 عاماً (الاتحاد الدولي لألعاب القوى)",
            "الإنجاز يعيد رسم الرقم القياسي الوطني للعراق في سباقات السرعة (أخبار العراق)",
            "الخزاعي يمثّل جيلاً عراقياً شاباً صاعداً في ألعاب القوى (أخبار العراق)",
            "فهل يقود جيل جديد العراق نحو أول ميدالية عالمية في الركض؟",
        ],
    },
    "caption": """رقم قياسي عراقي جديد بالركض — منو حطمه؟

فلاح الخزاعي يركض 10.21 ثانية ويخطف فضية 100م في أول بطولة آسيوية تحت 23.

برأيك، هذا الجيل يوصل العراق لميدالية عالمية؟

المصادر: World Athletics، The Star
#العراق #ألعاب_القوى #رقم_قياسي #فخر_عراقي
@photonect.news""",
    "v11": {
        "slug": s, "kicker": "عاجل",
        "hookHeadline": "عراقي يكسر الرقم… 10.21!",
        "voText": "سجّل العداء العراقي فلاح الخزاعي رقماً قياسياً وطنياً جديداً في سباق المئة متر، بزمن عشر ثوانٍ وواحد وعشرين جزءاً من الثانية. وبحسب الاتحاد الدولي لألعاب القوى، خطف الخزاعي الميدالية الفضية في نهائي أول بطولة آسيوية تحت ثلاثة وعشرين عاماً في مدينة أوردوس الصينية. وجاء الذهب للماليزي عظيم فهمي بفارق أربعة أجزاء من المئة فقط. إنه إنجاز يعيد رسم رقم العراق في الركض. فهل يقود جيل جديد العراق نحو أول ميدالية عالمية؟",
        "endQuestion": "هل يقود جيل جديد العراق نحو أول ميدالية عالمية في الركض؟",
        "sourcesLine": "المصادر: وورلد أثلتيكس · ذا ستار",
        "images": imgs(s), "audioBed": "audio/mood_hamasi.mp3",
        "statPops": [
            {"value": "10.21 ث", "label": "رقم قياسي وطني", "matchWord": "وواحد"},
            {"value": "0.04 ث", "label": "الفارق عن الذهب", "matchWord": "أربعة"},
        ],
    },
}

# ─────────────────────────────────────────────────────────────────────────
# 4 — US OPENS TOP AI CHIPS TO UAE  (P2 gulf/AI · V11 · B)
# ─────────────────────────────────────────────────────────────────────────
s = f"{DATE}-uae-us-ai-chips-greenlight"
SLUGS[s] = {
    "bucket": "world",
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/mood_cinematic.mp3", "topicBucket": "world", "variant": "B",
        "breaking": {
            "arabicKicker": "ذكاء اصطناعي · الخليج",
            "arabicHeadline": "أمريكا تفتح رقائقها المتقدمة للإمارات",
            "englishSubhead": "UAE GETS TOP US CHIP TIER | NVIDIA + AMD, NO LICENSE",
            "heroMedia": f"images/news/{s}/hero.jpg", "heroMediaType": "image",
        },
        "beats": [
            {
                "label": "ماذا يحدث؟",
                "arabicHeading": "الإمارات في أعلى فئة تصدير أمريكية",
                "arabicBody": "أعادت الولايات المتحدة تصنيف الإمارات ضمن أعلى فئة من حلفائها في ضوابط تصدير التكنولوجيا، ما يتيح لها رقائق نفيديا بلاكويل وإيه إم دي المتقدمة من دون ترخيص، بحسب بلومبرغ.",
                "bigStat": {"value": "A:5", "label": "Top US export ally tier",
                            "arabicLabel": "الفئة الأعلى في ضوابط التصدير الأمريكية التي أُدرجت فيها الإمارات وتتيح رقائق الذكاء الاصطناعي المتقدمة من دون ترخيص (بلومبرغ)"},
                "supportingStats": [{"label": "التصنيف", "value": "A:5"},
                                     {"label": "الرقائق", "value": "Nvidia+AMD"},
                                     {"label": "الترخيص", "value": "بدون"}],
                "broll": f"images/news/{s}/broll_1.jpg", "brolls": [f"images/news/{s}/broll_1.jpg"],
                "brollType": "image", "accent": ACCENTS[0], "brollSource": "Bloomberg · 2026",
            },
            {
                "label": "لماذا يهم؟",
                "arabicHeading": "الوحيدة بالمنطقة… أبوظبي مركزاً",
                "arabicBody": "تصبح الإمارات الدولة الوحيدة في الشرق الأوسط التي تنال هذا التصنيف، ما يعزز موقع أبوظبي وشركتي جي42 وكور42 مركزاً لبنية الذكاء الاصطناعي في المنطقة، بحسب بلومبرغ وموقع AGBI.",
                "bigStat": {"value": "1", "label": "Only Mideast nation at this tier",
                            "arabicLabel": "الإمارات هي الدولة الوحيدة في الشرق الأوسط التي نالت أعلى فئة تصدير أمريكية للرقائق المتقدمة (بلومبرغ · AGBI)"},
                "supportingStats": [{"label": "بالمنطقة", "value": "الوحيدة"},
                                     {"label": "الشركات", "value": "G42·Core42"},
                                     {"label": "الموقع", "value": "أبوظبي"}],
                "broll": f"images/news/{s}/broll_2.jpg", "brolls": [f"images/news/{s}/broll_2.jpg"],
                "brollType": "image", "accent": ACCENTS[1], "brollSource": "Bloomberg · AGBI",
            },
            {
                "label": "ماذا بعد؟",
                "arabicHeading": "الصفقة مقابل دعم في حرب إيران",
                "arabicBody": "ربط النص الأمريكي هذه الخطوة بدعم أبوظبي في الحرب ضد إيران، لتتعمق شراكة تقنية تحدّد من يملك بنية الذكاء الاصطناعي ومستقبل البيانات في المنطقة، بحسب بلومبرغ.",
                "bigStat": {"value": "تحالف", "label": "Tech alliance reward",
                            "arabicLabel": "شراكة تقنية أمريكية إماراتية عميقة ربط النص الأمريكي توسيعها بدعم أبوظبي في الحرب ضد إيران (بلومبرغ)"},
                "supportingStats": [{"label": "المقابل", "value": "دعم الحرب"},
                                     {"label": "الأثر", "value": "بيانات المنطقة"},
                                     {"label": "الشراكة", "value": "تقنية"}],
                "broll": f"images/news/{s}/broll_3.jpg", "brolls": [f"images/news/{s}/broll_3.jpg"],
                "brollType": "image", "accent": ACCENTS[2], "brollSource": "Bloomberg · 2026",
            },
        ],
        "sources": [
            {"name": "Bloomberg", "domain": "bloomberg.com"},
            {"name": "AGBI", "domain": "agbi.com"},
            {"name": "US Commerce Dept", "domain": "commerce.gov"},
        ],
        "arabicTicker": [
            "الولايات المتحدة تعيد تصنيف الإمارات ضمن أعلى فئة من حلفائها في ضوابط تصدير التكنولوجيا (بلومبرغ)",
            "القرار يتيح للإمارات وشركتي جي42 وكور42 رقائق نفيديا بلاكويل وإيه إم دي من دون ترخيص (بلومبرغ)",
            "الإمارات تصبح الدولة الوحيدة في الشرق الأوسط التي تنال هذا التصنيف الأعلى (بلومبرغ · AGBI)",
            "الخطوة تعزّز موقع أبوظبي مركزاً لبنية الذكاء الاصطناعي في المنطقة (AGBI)",
            "النص الأمريكي ربط توسيع الوصول للرقائق بدعم أبوظبي في الحرب ضد إيران (بلومبرغ)",
            "الصفقة تحدّد من يملك بنية الذكاء الاصطناعي ومستقبل البيانات في المنطقة (بلومبرغ)",
            "فهل تصبح أبوظبي عاصمة الذكاء الاصطناعي في الشرق الأوسط؟",
        ],
    },
    "caption": """أمريكا والإمارات ورقائق الذكاء الاصطناعي — شنو صار؟

واشنطن تمنح الإمارات أعلى تصنيف تصدير وتفتح رقائق Nvidia وAMD بلا ترخيص.

برأيك، تصير أبوظبي عاصمة الذكاء الاصطناعي بالمنطقة؟

المصادر: Bloomberg، AGBI
#الإمارات #الذكاء_الاصطناعي #الخليج #تقنية
@photonect.news""",
    "v11": {
        "slug": s, "kicker": "عاجل",
        "hookHeadline": "أمريكا تفتح رقائقها للإمارات",
        "voText": "أعادت الولايات المتحدة تصنيف الإمارات ضمن أعلى فئة من حلفائها في ضوابط تصدير التكنولوجيا. وبحسب بلومبرغ، يتيح القرار لحكومة الإمارات وشركاتها التقنية الكبرى الحصول على رقائق نفيديا بلاكويل وإيه إم دي المتقدمة من دون ترخيص. وبذلك تصبح الإمارات الدولة الوحيدة في الشرق الأوسط التي تنال هذا التصنيف الأعلى. وقد ربط القرار الأمريكي هذه الخطوة بدعم أبوظبي في الحرب ضد إيران. فهل تصبح أبوظبي عاصمة الذكاء الاصطناعي في المنطقة؟",
        "endQuestion": "هل تصبح أبوظبي عاصمة الذكاء الاصطناعي في المنطقة؟",
        "sourcesLine": "المصادر: بلومبرغ · AGBI",
        "images": imgs(s), "audioBed": "audio/mood_cinematic.mp3",
        "statPops": [
            {"value": "A:5", "label": "أعلى تصنيف تصدير", "matchWord": "حلفائها"},
            {"value": "1 فقط", "label": "بالشرق الأوسط", "matchWord": "الوحيدة"},
        ],
    },
}

# ─────────────────────────────────────────────────────────────────────────
# 5 — IRAQ PROJECTS BOOM DESPITE WAR  (P1 jobs · V10 CONTROL · A)
# ─────────────────────────────────────────────────────────────────────────
s = f"{DATE}-iraq-projects-boom-despite-war"
SLUGS[s] = {
    "bucket": "iraq_economy",
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/mood_orchestral.mp3", "topicBucket": "iraq_economy", "variant": "A",
        "breaking": {
            "arabicKicker": "اقتصاد · إعمار",
            "arabicHeadline": "رغم الحرب… مشاريع العراق الأولى بالمنطقة",
            "englishSubhead": "IRAQ #1 IN MIDEAST PROJECT GROWTH | +$15B IN A MONTH",
            "heroMedia": f"images/news/{s}/hero.jpg", "heroMediaType": "image",
        },
        "beats": [
            {
                "label": "ماذا يحدث؟",
                "arabicHeading": "قفزة 15 مليار دولار في شهر واحد",
                "arabicBody": "رغم تراجع إيرادات النفط، سجّلت مشاريع العراق أكبر زيادة شهرية في قيمتها بين أسواق الشرق الأوسط: 15 مليار دولار في شهر واحد، لترتفع بنسبة 3.4%، بحسب مؤشر MEED عبر شفق نيوز.",
                "bigStat": {"value": "$444B", "label": "Iraq project pipeline",
                            "arabicLabel": "إجمالي قيمة خط مشاريع العراق المخطط والنشط بالدولار بعد أكبر زيادة شهرية بين أسواق الشرق الأوسط (مؤشر MEED · شفق نيوز)"},
                "supportingStats": [{"label": "الإجمالي", "value": "$444 مليار"},
                                     {"label": "بشهر", "value": "+$15 مليار"},
                                     {"label": "النمو", "value": "+3.4%"}],
                "broll": f"images/news/{s}/broll_1.jpg", "brolls": [f"images/news/{s}/broll_1.jpg"],
                "brollType": "image", "accent": ACCENTS[0], "brollSource": "MEED · Shafaq News",
            },
            {
                "label": "لماذا يهم؟",
                "arabicHeading": "من هنا تأتي الوظائف والإعمار",
                "arabicBody": "هذه المشاريع هي مصدر الوظائف وعقود البناء بينما الرواتب مضغوطة: طريق التنمية وميناء الفاو الكبير والإسكان ومحطات الكهرباء، لتبقى عجلة الإعمار تدور رغم أزمة النفط.",
                "bigStat": {"value": "+$15B", "label": "Added in one month",
                            "arabicLabel": "قيمة ما أُضيف إلى خط مشاريع العراق في شهر واحد، وهي أكبر زيادة بين أسواق الشرق الأوسط وتغذّي الوظائف وعقود الإعمار (مؤشر MEED · أخبار العراق)"},
                "supportingStats": [{"label": "بالمنطقة", "value": "الأعلى"},
                                     {"label": "المحرّك", "value": "شغل وإعمار"},
                                     {"label": "أبرزها", "value": "التنمية·الفاو"}],
                "broll": f"images/news/{s}/broll_2.jpg", "brolls": [f"images/news/{s}/broll_2.jpg"],
                "brollType": "image", "accent": ACCENTS[1], "brollSource": "MEED · Iraqi News",
            },
            {
                "label": "ماذا بعد؟",
                "arabicHeading": "المنطقة تنمو للشهر الـ16 توالياً",
                "arabicBody": "بلغت عقود المشاريع الموقّعة في الشرق الأوسط وشمال إفريقيا 20.5 مليار دولار في حزيران مقابل 17 ملياراً في أيار، ونما سوق المشاريع الإقليمي للشهر السادس عشر على التوالي، بحسب مؤشر MEED.",
                "bigStat": {"value": "$20.5B", "label": "MENA June contract awards",
                            "arabicLabel": "قيمة عقود المشاريع الموقّعة في الشرق الأوسط وشمال إفريقيا في حزيران مقابل 17 ملياراً في أيار (مؤشر MEED)"},
                "supportingStats": [{"label": "حزيران", "value": "$20.5 مليار"},
                                     {"label": "أيار", "value": "$17 مليار"},
                                     {"label": "النمو", "value": "16 شهراً"}],
                "broll": f"images/news/{s}/broll_3.jpg", "brolls": [f"images/news/{s}/broll_3.jpg"],
                "brollType": "image", "accent": ACCENTS[2], "brollSource": "MEED Projects Index",
            },
        ],
        "sources": [
            {"name": "MEED Projects", "domain": "meed.com"},
            {"name": "Shafaq News", "domain": "shafaq.com"},
            {"name": "Iraqi News", "domain": "iraqinews.com"},
        ],
        "arabicTicker": [
            "مشاريع العراق تسجّل أكبر زيادة شهرية في قيمتها بين أسواق الشرق الأوسط: 15 مليار دولار في شهر واحد (مؤشر MEED · شفق نيوز)",
            "إجمالي خط مشاريع العراق المخطط والنشط يرتفع إلى 444 مليار دولار بنمو 3.4% (مؤشر MEED · شفق نيوز)",
            "هذه المشاريع هي مصدر الوظائف وعقود البناء بينما الرواتب مضغوطة (أخبار العراق)",
            "أبرز المشاريع: طريق التنمية وميناء الفاو الكبير والإسكان ومحطات الكهرباء (أخبار العراق)",
            "عقود المشاريع في الشرق الأوسط وشمال إفريقيا: 20.5 مليار دولار في حزيران مقابل 17 ملياراً في أيار (مؤشر MEED)",
            "سوق المشاريع الإقليمي ينمو للشهر السادس عشر على التوالي (مؤشر MEED)",
            "فهل يترجم هذا الزخم وظائف فعلية للعراقيين، أم يبقى أرقاماً على الورق؟",
        ],
    },
    "caption": """مشاريع العراق 2026 — كيف صارت الأولى بالمنطقة؟

رغم أزمة النفط، مشاريع العراق قفزت 15 مليار دولار بشهر واحد لتصل 444 ملياراً.

برأيك، هالزخم يترجم وظائف فعلية لو يبقى أرقام؟

المصادر: MEED، شفق نيوز
#العراق #اقتصاد #إعمار #طريق_التنمية
@photonect.news""",
    # No v11 brief — this is the silent V10.1 control.
}


def main():
    for slug, spec in SLUGS.items():
        d = POSTS / slug / ".meta"
        d.mkdir(parents=True, exist_ok=True)
        (d / "props.json").write_text(json.dumps(spec["props"], ensure_ascii=False, indent=2), encoding="utf-8")
        (POSTS / slug / "caption.txt").write_text(spec["caption"] + "\n", encoding="utf-8")
        stamp = dict(STAMP, bucket=spec["bucket"])
        (d / "media-stamp.json").write_text(json.dumps(stamp, ensure_ascii=False, indent=2), encoding="utf-8")
        if "v11" in spec:
            (d / "v11-brief.json").write_text(json.dumps(spec["v11"], ensure_ascii=False, indent=2), encoding="utf-8")
        v11 = " +v11" if "v11" in spec else "  (V10 control)"
        print(f"  ✓ {slug}{v11}")
    print(f"\nAuthored {len(SLUGS)} slugs for {DATE}")


if __name__ == "__main__":
    main()
