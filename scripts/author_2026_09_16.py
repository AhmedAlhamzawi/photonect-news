#!/usr/bin/env python3
"""Author the 2026-09-16 slate. Transcription of record for verify_slate_2026_09_16.py.

Every figure below was opened at source and dateline-confirmed 15-16 Sep 2026
(raw texts saved to the session scratchpad art/ for the gate).
Media: KIE (1.5) and Higgsfield (0.38) credits exhausted — every still is a
hand-vetted REAL photo (Wikimedia Commons / Pexels); brollSource says so honestly.
Dollar anchor: day-over-day deltas are computed only inside ONE outlet's own
series (Shafaq bourse Tue close-of-report vs Wed morning). No cross-outlet delta.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POSTS = ROOT / "data" / "posts"
D = "2026-09-16"
DATE_LABEL = "SEP 16 • 2026"
AR_DATE = "16 أيلول 2026"

S964 = {"name": "شبكة 964", "domain": "964media.com"}
SHAFAQ = {"name": "شفق نيوز", "domain": "shafaq.com"}
RUDAW = {"name": "رووداو", "domain": "rudawarabia.net"}
REUTERS = {"name": "رويترز", "domain": "reuters.com"}
BTODAY = {"name": "بغداد اليوم", "domain": "baghdadtoday.news"}

PEX = "صورة أرشيفية · Pexels"
WIKI = "صورة أرشيفية · Wikimedia Commons"


def beat(label, heading, body, big_v, big_en, big_ar, stats, img, accent, phrases, src=PEX):
    return {
        "label": label, "arabicHeading": heading, "arabicBody": body,
        "bigStat": {"value": big_v, "label": big_en, "arabicLabel": big_ar},
        "supportingStats": [{"label": k, "value": v} for k, v in stats],
        "broll": img, "brolls": [img], "brollType": "image",
        "accent": accent, "brollSource": src,
        "subtitlePhrases": phrases,
    }


def img(slug, n):
    return f"images/news/{D}-{slug}/{'hero' if n == 0 else f'broll_{n}'}.jpg"


def imgs(slug):
    return [img(slug, i) for i in range(4)]


def base(slug, bucket, variant, kicker, headline, sub):
    return {"dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": "@photonect.news",
            "audioBed": "audio/mood_newsroom.mp3", "topicBucket": bucket, "variant": variant,
            "breaking": {"arabicKicker": kicker, "arabicHeadline": headline, "englishSubhead": sub,
                         "heroMedia": img(slug, 0), "heroMediaType": "image"}}


SLATE = {}

# ─────────────────────── a · school year postponed to 11 Oct (P3 family/services) — LEAD
s = "a-school-start-11-october"
EQ = "كم طفل عندكم بالمدارس؟"
p = base(s, "iraq_society", "A", "التربية",
         "الدوام يتأجل: 11 تشرين الأول بدل 20 أيلول",
         "BAGHDAD · SEP 15-16 | FEDERAL EDUCATION MINISTRY POSTPONES 2026-2027 SCHOOL YEAR START FROM SUN 20 SEP TO SUN 11 OCT, PER A MINISTRY DOCUMENT DATED 15 SEP (RUDAW) | SPOKESMAN KARIM AL-SAYYID DENIES ANY LINK TO SECURITY; CITES TEACHERS' APPEALS, DILAPIDATED SCHOOLS, POWER CUTS, HEAT; MID-YEAR EXAM DATES MAY BE REVISED (964) | KURDISTAN REGION SCHOOLS START 20 SEP (RUDAW)")
p["beats"] = [
    beat("الموعد", "الدوام: 11 تشرين الأول بدل 20 أيلول",
         "وزارة التربية أجلت بدء العام الدراسي 2026-2027 من الأحد 20 أيلول إلى الأحد 11 تشرين الأول، بحسب وثيقة للوزارة نشرتها رووداو.",
         "11", "October 11 — new start date of the 2026-2027 school year (was Sep 20), per a ministry document via Rudaw",
         "تشرين الأول 2026 الموعد الجديد لبدء العام الدراسي بدلاً من 20 أيلول، بحسب وثيقة لوزارة التربية مؤرخة في 15 أيلول نشرتها رووداو",
         [("القديم", "20 أيلول"), ("الجديد", "11 تشرين الأول"), ("العام", "2026-2027")],
         img(s, 1), "#FFC217",
         ["العام الدراسي 2026-2027", "من 20 أيلول", "إلى 11 تشرين الأول"]),
    beat("السبب", "التربية: لا علاقة للوضع الأمني",
         "المتحدث باسم الوزارة كريم السيد نفى أي علاقة للتأجيل بالوضع الأمني، وقال إن السبب مناشدات المعلمين وتهالك مدارس وانقطاع الكهرباء والحر (شبكة 964).",
         "80%", "Share of textbooks the ministry relies on from books returned by students, per spokesman (964)",
         "من المناهج تعتمد فيها الوزارة على الكتب المسترجعة من الطلبة، بحسب المتحدث باسم وزارة التربية كريم السيد (شبكة 964)",
         [("الدور الثاني", "ينتهي 24 أيلول"), ("الدور الخاص", "يبدأ 26 أيلول"), ("نصف السنة", "قد يتغير")],
         img(s, 2), "#D72638",
         ["نفي أي علاقة بالوضع الأمني", "مناشدات المعلمين وتهالك مدارس", "وانقطاع الكهرباء والحر"]),
    beat("الإقليم", "كوردستان تبدأ 20 أيلول",
         "وزارة التربية في إقليم كوردستان حددت 20 أيلول لبدء الدراسة، أي قبل بقية المحافظات بنحو 3 أسابيع (رووداو).",
         "3", "Weeks, roughly, between Kurdistan Region's school start and the rest of Iraq, per Rudaw",
         "أسابيع تقريباً تفصل بين بدء الدراسة في إقليم كوردستان (20 أيلول) وبقية المحافظات (11 تشرين الأول)، بحسب رووداو",
         [("الإقليم", "20 أيلول"), ("بقية المحافظات", "11 تشرين الأول"), ("الفارق", "نحو 3 أسابيع")],
         img(s, 3), "#4CC9F0",
         ["إقليم كوردستان يبدأ 20 أيلول", "بقية المحافظات 11 تشرين الأول", "فارق نحو 3 أسابيع"]),
]
p["arabicTicker"] = [
    "وزارة التربية تؤجل بدء العام الدراسي 2026-2027 من 20 أيلول إلى 11 تشرين الأول (رووداو)",
    "المتحدث كريم السيد: لا علاقة للتأجيل بالوضع الأمني — مناشدات المعلمين وتهالك مدارس وانقطاع الكهرباء والحر (شبكة 964)",
    "الدور الثاني ينتهي 24 أيلول والدور الخاص يبدأ 26 أيلول، وموعد امتحانات نصف السنة قد يُعاد النظر فيه",
    "إقليم كوردستان يبدأ الدراسة في 20 أيلول (رووداو)",
    EQ,
]
p["endQuestion"] = EQ
p["sources"] = [RUDAW, S964]
SLATE[f"{D}-{s}"] = {
    "props": p,
    "brief": {
        "slug": f"{D}-{s}", "kicker": "التربية",
        "hookHeadline": "الدوام يتأجل.. للحادي عشر من تشرين",
        "voText": "أجلت وزارة التربية بدء العام الدراسي الجديد من العشرين من أيلول إلى الحادي عشر من تشرين الأول بحسب وثيقة للوزارة نشرتها رووداو. المتحدث باسم الوزارة كريم السيد نفى في حوار تلفزيوني أي علاقة للقرار بالوضع الأمني. وقال إن التأجيل فرضته مناشدات المعلمين وتهالك بعض المدارس وانقطاع الكهرباء وارتفاع درجات الحرارة. وأضاف أن مواعيد امتحانات نصف السنة قد يعاد النظر فيها. أما مدارس إقليم كوردستان فتبدأ الدراسة في العشرين من أيلول. كم طفل عندكم بالمدارس؟",
        "endQuestion": EQ,
        "sourcesLine": "المصادر: رووداو · شبكة 964 — 15 أيلول 2026",
        "images": imgs(s), "audioBed": "audio/mood_newsroom.mp3",
        "statPops": [
            {"value": "11 تشرين الأول", "label": "موعد بدء الدوام الجديد", "matchWord": "الحادي"},
            {"value": "20 أيلول", "label": "بدء الدراسة في إقليم كوردستان", "matchWord": "فتبدأ"},
        ],
    },
    "caption": f"""موعد الدوام في العراق 2026 — شنو تغيّر؟

التربية تؤجل.. والإقليم ماشي على موعده.

{EQ}

المصادر: رووداو، شبكة 964 (15 أيلول 2026)

#العراق #وزارة_التربية #الدوام_الرسمي #المدارس
@photonect.news
""",
}

# ─────────────────────── b · dollar today: +650 in a day, gold follows (P1 money, daily anchor)
s = "b-dollar-157250-gold-960"
EQ = "ناوي تشتري ذهب هالشهر؟"
p = base(s, "iraq_money", "B", "الدولار اليوم",
         "الدولار اليوم: 157,250 في بورصة بغداد",
         "WED SEP 16 MORNING · PER $100 | SHAFAQ: BAGHDAD BOURSES (KIFAH/HARTHIYA) 157,250 — TUESDAY 156,600 (+650, COMPUTED WITHIN SHAFAQ'S OWN SERIES); BAGHDAD SHOPS SELL 157,750 BUY 156,750; ERBIL SELL 157,250 BUY 157,200 | 964: BAGHDAD SELL 157,500; CBI OFFICIAL 131,000 | SHAFAQ GOLD: 21K GULF/TURKISH/EUROPEAN MITHQAL 960,000 SELL / 956,000 BUY (NAHR ST WHOLESALE), TUESDAY 945,000; IRAQI 21K 930,000")
p["beats"] = [
    beat("البورصة", "بورصة بغداد: 157,250.. وأمس 156,600",
         "بورصتا الكفاح والحارثية سجلتا صباح اليوم 157,250 ديناراً لكل 100 دولار، بعد 156,600 أمس الثلاثاء (شفق نيوز).",
         "157,250", "Baghdad bourse rate per $100, Wednesday morning — up from 156,600 on Tuesday, per Shafaq",
         "ديناراً لكل 100 دولار في بورصتي الكفاح والحارثية ببغداد صباح الأربعاء 16 أيلول 2026، بعد 156,600 يوم الثلاثاء، بحسب شفق نيوز",
         [("الثلاثاء", "156,600"), ("الأربعاء", "157,250"), ("الفرق", "650 (محتسب)")],
         img(s, 1), "#FFC217",
         ["بورصتا الكفاح والحارثية", "157,250 صباح الأربعاء", "بعد 156,600 أمس"]),
    beat("المحال", "محال بغداد تبيع 157,750",
         "بحسب شفق نيوز، محال الصيرفة ببغداد تبيع 100 دولار بـ157,750 وتشتريها بـ156,750. ونشرة 964 تضع البيع في بغداد عند 157,500.",
         "157,750", "Baghdad exchange-shop selling price per $100, per Shafaq",
         "ديناراً سعر بيع 100 دولار في محال الصيرفة ببغداد صباح الأربعاء، وسعر الشراء 156,750، بحسب شفق نيوز",
         [("البيع (شفق)", "157,750"), ("الشراء (شفق)", "156,750"), ("البيع (964)", "157,500")],
         img(s, 2), "#D72638",
         ["محال بغداد تبيع 157,750", "وتشتري 156,750", "ونشرة 964: 157,500"]),
    beat("الذهب", "الذهب يصعد: المثقال 960 ألفاً",
         "مثقال عيار 21 الخليجي سجل 960,000 دينار بيعاً في جملة شارع النهر، مقابل 945,000 أمس. والعراقي 930,000 (شفق نيوز).",
         "960,000", "IQD per mithqal of 21k Gulf gold (wholesale, Nahr St), vs 945,000 Tuesday, per Shafaq",
         "دينار سعر بيع مثقال الذهب الخليجي عيار 21 في أسواق الجملة بشارع النهر صباح الأربعاء، مقابل 945,000 أمس، بحسب شفق نيوز",
         [("أمس", "945,000"), ("اليوم", "960,000"), ("العراقي 21", "930,000")],
         img(s, 3), "#4CC9F0",
         ["مثقال عيار 21 الخليجي", "960,000 دينار", "والعراقي 930,000"]),
]
p["arabicTicker"] = [
    "شفق نيوز: بورصتا الكفاح والحارثية 157,250 ديناراً لكل 100 دولار صباح الأربعاء بعد 156,600 أمس",
    "محال بغداد: بيع 157,750 وشراء 156,750 (شفق نيوز) · نشرة شبكة 964: بيع بغداد 157,500 · الرسمي 131,000",
    "أربيل: بيع 157,250 وشراء 157,200 (شفق نيوز)",
    "الذهب الخليجي عيار 21 بجملة شارع النهر: 960,000 للمثقال بعد 945,000 أمس — والعراقي 930,000",
    EQ,
]
p["endQuestion"] = EQ
p["sources"] = [SHAFAQ, S964]
SLATE[f"{D}-{s}"] = {
    "props": p,
    "brief": {
        "slug": f"{D}-{s}", "kicker": "الدولار اليوم",
        "hookHeadline": "الدولار صعد.. والذهب لحقه",
        "voText": "ارتفع سعر الدولار صباح اليوم في بورصتي الكفاح والحارثية ببغداد إلى مئة وسبعة وخمسين ألفاً ومئتين وخمسين ديناراً لكل مئة دولار بحسب شفق نيوز. بعد أن سجل أمس مئة وستة وخمسين ألفاً وستمئة. ومحال الصيرفة في بغداد تبيع المئة دولار بمئة وسبعة وخمسين ألفاً وسبعمئة وخمسين. وبالتزامن ارتفع الذهب أيضاً. فمثقال عيار واحد وعشرين الخليجي سجل في جملة شارع النهر تسعمئة وستين ألف دينار. مقابل تسعمئة وخمسة وأربعين ألفاً أمس بحسب الوكالة نفسها. ناوي تشتري ذهب هالشهر؟",
        "endQuestion": EQ,
        "sourcesLine": "المصادر: شفق نيوز · شبكة 964 — نشرتا صباح 16 أيلول 2026",
        "images": imgs(s), "audioBed": "audio/mood_newsroom.mp3",
        "statPops": [
            {"value": "157,250", "label": "بورصة بغداد صباح الأربعاء لكل 100 دولار", "matchWord": "والحارثية"},
            {"value": "960,000", "label": "دينار مثقال الذهب الخليجي عيار 21 (جملة)", "matchWord": "النهر"},
        ],
    },
    "caption": f"""سعر الدولار اليوم في العراق — وشكد صار مثقال الذهب؟

البورصة صعدت من أمس.. والذهب مشى وياها.

{EQ}

المصادر: شفق نيوز · شبكة 964 (16 أيلول 2026)

#سعر_الدولار_اليوم #الدينار_العراقي #سعر_الذهب #العراق
@photonect.news
""",
}

# ─────────────────────── c · Dana Gas cut: Kurdistan loses 1000 MW (P2 Gulf firm → Iraqi power hours)
s = "c-danagas-1000-megawatts"
EQ = "كم ساعة كهرباء وصلتكم اليوم؟"
p = base(s, "iraq_services", "A", "الكهرباء",
         "دانة غاز تخفض الضخ.. وكوردستان تخسر 1000 ميغاواط",
         "ERBIL · SEP 16 | KRG ELECTRICITY MINISTRY: UAE'S DANA GAS CUT GAS SUPPLY TO POWER PLANTS — ABOUT 1000 MW OF GENERATION LOST; CUT 'DIRECTLY' HIT SUPPLY HOURS (964); NO REASON GIVEN, NO COMPANY STATEMENT YET (SHAFAQ, RUDAW) | DANA GAS SAYS KHOR MOR GAS FUELS >75% OF KURDISTAN GENERATION CAPACITY; JULY ATTACK HALTED OUTPUT, ~2500 MW DROP (RUDAW)")
p["beats"] = [
    beat("الخسارة", "كوردستان: خسرنا 1000 ميغاواط",
         "وزارة الكهرباء في الإقليم أعلنت فقدان نحو 1000 ميغاواط بعد خفض دانة غاز الإماراتية كميات الغاز للمحطات، وقالت إن ساعات التجهيز تأثرت مباشرة.",
         "1000", "Megawatts of generation lost in Kurdistan Region after Dana Gas cut supply, per KRG Electricity Ministry",
         "ميغاواط فقدتها منظومة كهرباء إقليم كوردستان بعد خفض شركة دانة غاز الإماراتية إمدادات الغاز، بحسب وزارة الكهرباء في الإقليم (شبكة 964 · شفق نيوز · رووداو)",
         [("المفقود", "1000 ميغاواط"), ("الشركة", "دانة غاز"), ("الأثر", "ساعات التجهيز")],
         img(s, 1), "#D72638",
         ["دانة غاز تخفض الغاز", "نحو 1000 ميغاواط", "وساعات التجهيز تتأثر"]),
    beat("السبب", "السبب؟ الوزارة ما ذكرته",
         "الوزارة قالت إنها تتواصل مع الشركة ووزارة الثروات الطبيعية لإعادة الضخ، ولم تذكر أسباب الخفض، ولا توضيح من الشركة بعد (شفق نيوز · رووداو).",
         "3", "Main plants run on Khor Mor gas — Erbil, Bazian, Chamchamal — per Rudaw",
         "محطات رئيسية (أربيل وبازيان وجمجمال) تعمل بغاز حقل خور مور، بحسب رووداو",
         [("الأسباب", "لم تُذكر"), ("الشركة", "لا توضيح بعد"), ("المحطات", "أربيل · بازيان · جمجمال")],
         img(s, 2), "#FFC217",
         ["الأسباب لم تُذكر", "تواصل مع الشركة", "لإعادة الضخ"]),
    beat("خور مور", "خور مور: أكثر من 75% من التوليد",
         "دانة غاز تقول إن غاز خور مور يشغّل أكثر من 75% من قدرة التوليد بالإقليم. وبتموز الماضي توقف الإنتاج بعد هجوم، فانخفضت الكهرباء نحو 2500 ميغاواط (رووداو).",
         "75%", "Share of Kurdistan Region generation capacity fuelled by Khor Mor gas, per Dana Gas via Rudaw",
         "من قدرة توليد الكهرباء في إقليم كوردستان يشغّلها غاز حقل خور مور، بحسب شركة دانة غاز كما نقلت رووداو",
         [("خور مور", "+75% من التوليد"), ("تموز", "نحو 2500 ميغاواط"), ("اليوم", "نحو 1000 ميغاواط")],
         img(s, 3), "#4CC9F0",
         ["خور مور يشغّل أكثر من 75%", "تموز: انخفاض نحو 2500 ميغاواط", "بعد هجوم على الحقل"]),
]
p["arabicTicker"] = [
    "كهرباء كوردستان: خفض دانة غاز الإماراتية إمدادات الغاز يفقد المنظومة نحو 1000 ميغاواط (شبكة 964 · شفق نيوز · رووداو)",
    "الوزارة: التنسيق جارٍ مع وزارة الثروات الطبيعية والتواصل مع الشركة لإعادة الضخ — ولم تذكر الأسباب",
    "دانة غاز: غاز خور مور يوفر الوقود لأكثر من 75% من قدرة التوليد في الإقليم (رووداو)",
    EQ,
]
p["endQuestion"] = EQ
p["sources"] = [S964, SHAFAQ, RUDAW]
SLATE[f"{D}-{s}"] = {
    "props": p,
    "brief": {
        "slug": f"{D}-{s}", "kicker": "الكهرباء",
        "hookHeadline": "كوردستان تخسر ألف ميغاواط بيوم",
        "voText": "أعلنت وزارة الكهرباء في إقليم كوردستان اليوم فقدان نحو ألف ميغاواط من إنتاج الطاقة. بعد أن خفضت شركة دانة غاز الإماراتية كميات الغاز الموردة إلى محطات التوليد. وقالت الوزارة إن الخفض انعكس مباشرة على ساعات تجهيز المواطنين. ولم تذكر أسبابه. وتقول الشركة بحسب رووداو إن غاز حقل خور مور يشغل أكثر من خمسة وسبعين بالمئة من قدرة التوليد في الإقليم. وفي تموز الماضي انخفض الإنتاج نحو ألفين وخمسمئة ميغاواط بعد هجوم على الحقل. كم ساعة كهرباء وصلتكم اليوم؟",
        "endQuestion": EQ,
        "sourcesLine": "المصادر: وزارة الكهرباء في الإقليم عبر شبكة 964 · شفق نيوز · رووداو — 16 أيلول 2026",
        "images": imgs(s), "audioBed": "audio/mood_newsroom.mp3",
        "statPops": [
            {"value": "1000 ميغاواط", "label": "فقدتها كهرباء الإقليم", "matchWord": "فقدان"},
            {"value": "75%", "label": "من التوليد بغاز خور مور", "matchWord": "يشغل"},
        ],
    },
    "caption": f"""كهرباء كوردستان اليوم — ليش خسرت 1000 ميغاواط؟

شركة خليجية خفّضت الغاز.. والوزارة ما ذكرت السبب.

{EQ}

المصادر: شبكة 964، شفق نيوز، رووداو (16 أيلول 2026)

#كوردستان #الكهرباء #العراق #دانة_غاز
@photonect.news
""",
}

# ─────────────────────── d · looted money: crypto hiding + recovery draft law (P1 corruption)
s = "d-looted-money-crypto-law"
EQ = "تتابع محاكمات صولة الفجر؟"
p = base(s, "iraq_corruption", "B", "نزاهة",
         "فلوس الفساد.. وصلت للعملات المشفرة؟",
         "BAGHDAD · SEP 14-16 | INTEGRITY COMMISSION OFFICIAL (UNNAMED) TO 964: HIDING METHODS NOW SPAN COMPANIES, PROXY NAMES, TRANSFERS ABROAD AND, IN SOME CASES, CRYPTOCURRENCY; ASSETS OF OFFICIALS WHO ENTERED STATE POSTS IN THE LAST 3-4 YEARS EASIER TO REACH | MP DIAA SHAGHATI (PARLIAMENT INTEGRITY COMMITTEE): DRAFT LAW TO RECOVER LOOTED FUNDS BEING WRITTEN WITH PM OFFICE AND PRESIDENCY, NOT FINAL (964) | INTEGRITY HEAD MOHAMMED ALI AL-LAMI MET INTERPOL IN PARIS; SAYS SOME IMPLICATED TRIED TO LEAVE IRAQ (BAGHDAD TODAY, RUDAW) | TRIAL SESSIONS OF TWO MPs AND A FORMER MP POSTPONED TO SEP 16-17 (964)")
p["beats"] = [
    beat("الإخفاء", "الأموال: شركات وأسماء بديلة.. وكريبتو",
         "مسؤول في هيئة النزاهة قال لشبكة 964 إن إخفاء أموال الفساد امتد إلى شركات وأسماء بديلة وتحويلات للخارج، وحتى عملات مشفرة في بعض الحالات.",
         "4", "Years: assets of officials who took posts in the last 3-4 years are easier to reach, per an Integrity official (964)",
         "سنوات: الوصول إلى أموال المسؤولين الذين دخلوا مواقع الدولة خلال آخر 3 أو 4 سنوات أسهل نسبياً، بحسب مسؤول في هيئة النزاهة طلب عدم ذكر اسمه (شبكة 964)",
         [("الأساليب", "شركات · أسماء بديلة"), ("الوجهة", "الخارج"), ("أحياناً", "عملات مشفرة")],
         img(s, 1), "#D72638",
         ["شركات وأسماء بديلة", "تحويلات إلى الخارج", "وعملات مشفرة أحياناً"]),
    beat("القانون", "مسودة قانون لاسترداد المنهوب",
         "النائب ضياء شغاتي، عضو لجنة النزاهة النيابية، قال إن مسودة قانون لاسترداد الأموال المنهوبة داخل العراق وخارجه قيد الصياغة ولم تكتمل (شبكة 964).",
         "3", "Bodies drafting the recovery law: parliament's integrity committee, PM's office, presidency — per MP Shaghati (964)",
         "جهات تعمل على مسودة قانون استرداد الأموال: لجنة النزاهة النيابية ورئاسة الوزراء ورئاسة الجمهورية، بحسب النائب ضياء شغاتي (شبكة 964)",
         [("الجهات", "3"), ("النطاق", "داخل العراق وخارجه"), ("الصياغة", "لم تكتمل")],
         img(s, 2), "#FFC217",
         ["مسودة قانون جديد", "لاسترداد الأموال المنهوبة", "الصياغة لم تكتمل بعد"], src=WIKI),
    beat("الملاحقة", "النزاهة والإنتربول.. والمحاكمات مستمرة",
         "رئيس هيئة النزاهة محمد علي اللامي بحث في باريس مع الإنتربول ملاحقة المطلوبين، وقال إن بعض المتورطين حاولوا مغادرة البلاد (بغداد اليوم · رووداو).",
         "16 و17", "September 16-17: postponed trial sessions of two MPs and a former MP in the 'Dawn' campaign, per 964",
         "أيلول: موعدا جلسات محاكمة نائبتين ونائبة سابقة ضمن «صولة الفجر» بعد تأجيلها، بحسب شبكة 964",
         [("الشريك", "الإنتربول"), ("اللقاء", "باريس"), ("المحاكمات", "16 و17 أيلول")],
         img(s, 3), "#4CC9F0",
         ["اللامي والإنتربول في باريس", "ملاحقة المطلوبين بالخارج", "ومحاكمات 16 و17 أيلول"], src=WIKI),
]
p["arabicTicker"] = [
    "مسؤول في النزاهة لشبكة 964: أساليب إخفاء أموال الفساد امتدت إلى الشركات والأسماء البديلة والعملات المشفرة",
    "النائب ضياء شغاتي: مسودة قانون لاسترداد الأموال المنهوبة تُكتب مع رئاستي الوزراء والجمهورية ولم تكتمل",
    "اللامي من باريس: بعض المتورطين حاولوا مغادرة البلاد — تعاون مع الإنتربول لملاحقة المطلوبين (بغداد اليوم · رووداو)",
    EQ,
]
p["endQuestion"] = EQ
p["sources"] = [S964, BTODAY, RUDAW]
SLATE[f"{D}-{s}"] = {
    "props": p,
    "brief": {
        "slug": f"{D}-{s}", "kicker": "نزاهة",
        "hookHeadline": "فلوس الفساد.. وين تنخبى؟",
        "voText": "مسؤول في هيئة النزاهة طلب عدم ذكر اسمه يقول إن أساليب إخفاء أموال الفساد تطورت. فلم تعد تقتصر على الحسابات والعقارات بل امتدت إلى شركات وأسماء بديلة وتحويلات إلى الخارج وحتى إلى العملات المشفرة في بعض الحالات. ويضيف أن الوصول إلى أموال المسؤولين القدامى أصعب. وكشف النائب ضياء شغاتي عضو لجنة النزاهة النيابية عن مسودة قانون لاسترداد الأموال المنهوبة داخل العراق وخارجه لم تكتمل صياغتها بعد. ورئيس الهيئة بحث في باريس مع الإنتربول ملاحقة المطلوبين. تتابع محاكمات صولة الفجر؟",
        "endQuestion": EQ,
        "sourcesLine": "المصادر: شبكة 964 · بغداد اليوم · رووداو — 14 إلى 16 أيلول 2026",
        "images": imgs(s), "audioBed": "audio/mood_newsroom.mp3",
        "statPops": [
            {"value": "3 جهات", "label": "تكتب مسودة قانون استرداد الأموال", "matchWord": "مسودة"},
            {"value": "3-4 سنوات", "label": "المسؤولون الأحدث أسهل ملاحقة بحسب مسؤول بالنزاهة", "matchWord": "القدامى"},
        ],
    },
    "caption": f"""صولة الفجر وأموال الفساد — وين تنخبى الفلوس؟

مسؤول بالنزاهة يحكي عن أسلوب جديد.. والبرلمان يكتب قانون.

{EQ}

المصادر: شبكة 964، بغداد اليوم، رووداو (14-16 أيلول 2026)

#العراق #هيئة_النزاهة #صولة_الفجر #مكافحة_الفساد
@photonect.news
""",
}

# ─────────────────────── e · ADNOC buys Iraqi crude at deep discounts (P2 Gulf/oil) — V10.1 control
s = "e-adnoc-iraqi-crude-discount"
EQ = "راتبك حكومي لو قطاع خاص؟"
p = base(s, "mena_geo_economy", "C", "نفط",
         "أدنوك تشتري نفط العراق.. بخصم يوصل 27 دولار",
         "NEW DELHI/BAGHDAD · REUTERS SEP 15 (THREE SOURCES) | ADNOC AGREED TO BUY 32M IRAQI BARRELS IN AUGUST AT DISCOUNTS OF $24.90-$27/BBL AND 40M IN SEPTEMBER (10M AT $18, 30M AT $25); LIFTED 20M OF AUGUST ALLOCATION DUE TO EXPORT CONSTRAINTS; IRAQ EXPORTS ~2M BPD IN SEPT VS 2.354M IN AUG (KPLER) | RUDAW SEP 16: OIL ~88% OF GOVERNMENT REVENUE IN 2025 (WORLD BANK) | REPORTED BY BAGHDAD TODAY SEP 15-16")
p["beats"] = [
    beat("آب", "32 مليون برميل.. بخصم لحد 27 دولار",
         "بحسب رويترز نقلاً عن مصادر عراقية، اتفقت أدنوك الإماراتية على شراء 32 مليون برميل عراقي في آب بخصومات بين 24.90 و27 دولاراً للبرميل.",
         "32", "Million Iraqi barrels ADNOC agreed to buy in August at $24.90-$27 discounts, per Reuters sources",
         "مليون برميل من الخام العراقي اتفقت أدنوك على شرائها في آب بخصومات بين 24.90 و27 دولاراً للبرميل، بحسب مصادر تحدثت لرويترز",
         [("الخصم الأدنى", "$24.90"), ("الخصم الأعلى", "$27"), ("المشتري", "أدنوك")],
         img(s, 1), "#FFC217",
         ["أدنوك الإماراتية", "32 مليون برميل في آب", "بخصم 24.90 إلى 27 دولاراً"]),
    beat("أيلول", "وبأيلول: 40 مليون برميل",
         "وفي أيلول 40 مليون برميل: 10 ملايين بخصم 18 دولاراً و30 مليوناً بخصم 25 دولاراً، ورُفع من حصة آب 20 مليوناً فقط بسبب قيود التصدير (رويترز).",
         "40", "Million barrels in September: 10M at an $18 discount, 30M at $25, per a Reuters source",
         "مليون برميل في أيلول: 10 ملايين بخصم 18 دولاراً و30 مليوناً بخصم 25 دولاراً للبرميل، بحسب مصدر عراقي لرويترز",
         [("بخصم $18", "10 ملايين"), ("بخصم $25", "30 مليوناً"), ("رُفع من حصة آب", "20 مليوناً")],
         img(s, 2), "#D72638",
         ["40 مليون برميل في أيلول", "10 ملايين بخصم 18 دولاراً", "و30 مليوناً بخصم 25"]),
    beat("الإيرادات", "النفط = 88% من إيرادات الدولة",
         "رووداو تنقل عن البنك الدولي أن النفط وفّر نحو 88% من إيرادات الحكومة في 2025. والصادرات نحو مليوني برميل يومياً بأيلول مقابل 2.354 مليون بآب (رويترز عن Kpler).",
         "88%", "Share of Iraqi government revenue from oil in 2025, per World Bank data cited by Rudaw",
         "من إيرادات الحكومة العراقية وفّرها النفط في 2025، بحسب بيانات البنك الدولي كما أوردتها رووداو",
         [("الإيرادات من النفط", "88%"), ("صادرات أيلول", "نحو 2 مليون ب/ي"), ("صادرات آب", "2.354 مليون ب/ي")],
         img(s, 3), "#4CC9F0",
         ["النفط نحو 88% من الإيرادات", "صادرات أيلول نحو 2 مليون ب/ي", "وآب 2.354 مليون"], src=WIKI),
]
p["arabicTicker"] = [
    "رويترز: أدنوك اشترت 32 مليون برميل عراقي في آب بخصومات بين 24.90 و27 دولاراً للبرميل",
    "و40 مليون برميل في أيلول — 10 ملايين بخصم 18 دولاراً و30 مليوناً بخصم 25 دولاراً (مصدر عراقي لرويترز)",
    "صادرات العراق نحو مليوني برميل يومياً في أيلول مقابل 2.354 مليون في آب (Kpler عبر رويترز)",
    "رووداو عن البنك الدولي: النفط وفّر نحو 88% من إيرادات الحكومة في 2025",
    EQ,
]
p["endQuestion"] = EQ
p["sources"] = [REUTERS, RUDAW, BTODAY]
SLATE[f"{D}-{s}"] = {
    "props": p,
    "brief": None,
    "caption": f"""نفط العراق يتباع بخصم — شكد الخصم ومنو المشتري؟

شركة خليجية صارت أكبر مشترٍ.. والرقم بالفيديو.

{EQ}

المصادر: رويترز، رووداو، بغداد اليوم (15-16 أيلول 2026)

#العراق #النفط #أدنوك #نفط_البصرة
@photonect.news
""",
}


def main():
    for slug, d in SLATE.items():
        meta = POSTS / slug / ".meta"
        meta.mkdir(parents=True, exist_ok=True)
        (meta / "props.json").write_text(
            json.dumps(d["props"], ensure_ascii=False, indent=2), encoding="utf-8")
        if d["brief"]:
            (meta / "v11-brief.json").write_text(
                json.dumps(d["brief"], ensure_ascii=False, indent=2), encoding="utf-8")
        (POSTS / slug / "caption.txt").write_text(d["caption"], encoding="utf-8")
        print(f"wrote {slug}{'' if d['brief'] else '  (V10.1 control, no brief)'}")


if __name__ == "__main__":
    main()
