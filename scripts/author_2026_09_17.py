#!/usr/bin/env python3
"""Author the 2026-09-17 slate. Transcription of record for verify_slate_2026_09_17.py.

Every figure below was opened at source and dateline-confirmed 16-17 Sep 2026
(raw texts saved to the session scratchpad art/ for the gate).
Media: KIE (1.5) and Higgsfield (0.38) credits exhausted — every still is a
hand-vetted REAL photo (Wikimedia Commons / Pexels); brollSource says so honestly.
Dollar anchor: day-over-day deltas are computed only inside ONE outlet's own
series (Shafaq bourse Wed morning 157,250 vs Thu morning 158,850). No cross-outlet delta.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POSTS = ROOT / "data" / "posts"
D = "2026-09-17"
DATE_LABEL = "SEP 17 • 2026"
AR_DATE = "17 أيلول 2026"

S964 = {"name": "شبكة 964", "domain": "964media.com"}
SHAFAQ = {"name": "شفق نيوز", "domain": "shafaq.com"}
RUDAW = {"name": "رووداو", "domain": "rudawarabia.net"}
REUTERS = {"name": "رويترز", "domain": "reuters.com"}
BTODAY = {"name": "بغداد اليوم", "domain": "baghdadtoday.news"}
MADA = {"name": "المدى", "domain": "almadapaper.net"}
ASHARQ = {"name": "الشرق رياضة", "domain": "sports.asharq.com"}

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

# ─────────────────────── a · Gulf Cup 27 squad: 26 players, Jalal Hassan out (P3 region sport/pride) — LEAD
s = "a-gulf-cup-26-players"
EQ = "راح تتابع مباريات المنتخب بكأس الخليج؟"
p = base(s, "region_sport", "A", "خليجي 27",
         "قائمة أسود الرافدين لخليجي 27.. وجلال حسن برّه",
         "BAGHDAD · SEP 16 | IRAQ FA NAMES 26-MAN SQUAD FOR 27TH GULF CUP IN SAUDI ARABIA, LED BY STRIKER AYMEN HUSSEIN; GOALKEEPER JALAL HASSAN ABSENT (964) | TOURNAMENT 23 SEP - 6 OCT IN JEDDAH; IRAQ IN GROUP A WITH SAUDI ARABIA, OMAN, KUWAIT (ASHARQ SPORTS) | COACH GRAHAM ARNOLD: 'WE ARE GOING TO WIN THE TITLE'; HUSSEIN ALI OUT, NEEDS SURGERY (AL-MADA)")
p["beats"] = [
    beat("القائمة", "26 لاعباً بقيادة أيمن حسين",
         "الاتحاد العراقي لكرة القدم أعلن قائمة من 26 لاعباً لخليجي 27 في السعودية بقيادة المهاجم أيمن حسين، مع غياب الحارس جلال حسن (شبكة 964 · المدى).",
         "26", "Players in Iraq's Gulf Cup 27 squad, led by striker Aymen Hussein, per 964 and Al-Mada",
         "لاعباً في قائمة المنتخب العراقي لبطولة خليجي 27 بقيادة المهاجم أيمن حسين، بحسب شبكة 964 والمدى",
         [("القائد", "أيمن حسين"), ("الغائب", "جلال حسن"), ("الحراس", "3")],
         img(s, 1), "#FFC217",
         ["قائمة من 26 لاعباً", "بقيادة أيمن حسين", "وغياب جلال حسن"], WIKI),
    beat("المجموعة", "السعودية وعُمان والكويت بمجموعتنا",
         "البطولة تقام في جدة من 23 أيلول إلى 6 تشرين الأول، والعراق بالمجموعة الأولى مع السعودية وعُمان والكويت (الشرق رياضة).",
         "23", "September 23 — Gulf Cup 27 kicks off in Jeddah, runs to October 6, per Asharq Sports",
         "أيلول موعد انطلاق خليجي 27 في جدة، وتستمر البطولة حتى 6 تشرين الأول، بحسب الشرق رياضة",
         [("المدينة", "جدة"), ("الانطلاق", "23 أيلول"), ("الختام", "6 تشرين الأول")],
         img(s, 2), "#4CC9F0",
         ["جدة من 23 أيلول", "إلى 6 تشرين الأول", "السعودية وعُمان والكويت"]),
    beat("المدرب", "أرنولد: رايحين للقب",
         "المدرب غراهام أرنولد قال إن المنتخب ذاهب للفوز بالبطولة، وإن حسين علي خرج من الحسابات لإصابة تحتاج عملية جراحية (المدى).",
         "35", "Players in the preliminary list registered about a month ago, per coach Graham Arnold (Al-Mada)",
         "لاعباً في القائمة الأولية التي سُجلت قبل نحو شهر وفق تعليمات البطولة، بحسب المدرب غراهام أرنولد (المدى)",
         [("الهدف", "اللقب"), ("المصاب", "حسين علي"), ("القائمة الأولية", "35 لاعباً")],
         img(s, 3), "#D72638",
         ["نحن ذاهبون للفوز بالبطولة", "حسين علي خارج الحسابات", "إصابة تحتاج عملية جراحية"], WIKI),
]
p["arabicTicker"] = [
    "الاتحاد العراقي يعلن قائمة من 26 لاعباً لخليجي 27 بقيادة أيمن حسين وغياب الحارس جلال حسن (شبكة 964)",
    "البطولة في جدة من 23 أيلول إلى 6 تشرين الأول — العراق بالمجموعة الأولى مع السعودية وعُمان والكويت (الشرق رياضة)",
    "أرنولد: نحن ذاهبون للفوز بالبطولة — وحسين علي خارج الحسابات بسبب الإصابة (المدى)",
    EQ,
]
p["endQuestion"] = EQ
p["sources"] = [S964, ASHARQ, MADA]
SLATE[f"{D}-{s}"] = {
    "props": p,
    "brief": {
        "slug": f"{D}-{s}", "kicker": "خليجي 27",
        "hookHeadline": "قائمة خليجي 27.. منو غاب؟",
        "voText": "أعلن الاتحاد العراقي لكرة القدم قائمة أسود الرافدين لبطولة كأس الخليج السابعة والعشرين في السعودية، وتضم ستة وعشرين لاعباً بقيادة المهاجم أيمن حسين، مع غياب الحارس جلال حسن. ويلعب العراق في المجموعة الأولى مع السعودية وعمان والكويت، وتنطلق البطولة في جدة في الثالث والعشرين من أيلول. وقال المدرب غراهام أرنولد إن المنتخب ذاهب للفوز باللقب، وإن حسين علي خرج من الحسابات بسبب إصابة تحتاج إلى عملية جراحية. راح تتابع مباريات المنتخب بكأس الخليج؟",
        "endQuestion": EQ,
        "sourcesLine": "المصادر: شبكة 964 · الشرق رياضة · المدى — 16 أيلول 2026",
        "images": imgs(s), "audioBed": "audio/mood_newsroom.mp3",
        "statPops": [
            {"value": "26 لاعباً", "label": "قائمة العراق لخليجي 27", "matchWord": "لاعباً"},
            {"value": "23 أيلول", "label": "انطلاق البطولة في جدة", "matchWord": "جدة"},
        ],
    },
    "caption": f"""قائمة منتخب العراق لخليجي 27 — منو غاب ومنو يقود؟

26 اسم.. وغياب واحد محد توقعه.

{EQ}

المصادر: شبكة 964، الشرق رياضة، المدى (16 أيلول 2026)

#منتخب_العراق #خليجي27 #أسود_الرافدين #العراق
@photonect.news
""",
}

# ─────────────────────── b · dollar crosses 159,000 (P1 money, daily anchor)
s = "b-dollar-158850-159000"
EQ = "بكم اشتريت آخر مية دولار؟"
p = base(s, "iraq_money", "B", "الدولار اليوم",
         "الدولار يتخطى 159 ألفاً.. ليش صاعد؟",
         "BAGHDAD · SEP 17 | SHAFAQ: KIFAH & HARITHIYA BOURSES 158,850 IQD PER $100 THU MORNING VS 157,250 WED (+1,600, COMPUTED WITHIN SHAFAQ'S OWN SERIES); BAGHDAD EXCHANGE SHOPS SELL 159,250 / BUY 158,250; ERBIL SELL 158,500 / BUY 158,400 | 964: BAGHDAD SELLING RATE 159,000; CBI OFFICIAL RATE 131,000 | ECONOMIST ALI DAADOUSH (SHAFAQ): POLITICIANS' STATEMENTS, UNCERTAINTY, SPECULATION, LOWER DOLLAR SUPPLY, DELAYED IMPORT TRANSFERS; PASSES INTO IMPORTED-GOODS PRICES")
p["beats"] = [
    beat("البورصة", "بورصة بغداد: 158,850 لكل 100 دولار",
         "بورصتا الكفاح والحارثية سجلتا صباح اليوم 158,850 ديناراً لكل 100 دولار، مقابل 157,250 أمس الأربعاء (شفق نيوز). وشبكة 964 سجلت سعر البيع ببغداد 159,000.",
         "+1,600", "Dinars rise per $100 in Baghdad bourses, Thu morning vs Wed — computed within Shafaq's own figures",
         "دينار ارتفاع سعر كل 100 دولار في بورصتي بغداد صباح الخميس عن الأربعاء (محتسب من أرقام شفق نيوز نفسها: 158,850 مقابل 157,250)",
         [("أمس", "157,250"), ("اليوم", "158,850"), ("964: البيع", "159,000")],
         img(s, 1), "#D72638",
         ["بورصتا الكفاح والحارثية", "158,850 لكل 100 دولار", "أمس كان 157,250"]),
    beat("الصيرفة", "بمحلات الصيرفة: البيع 159,250",
         "محال الصيرفة ببغداد باعت 100 دولار بـ159,250 واشترت بـ158,250. وفي أربيل البيع 158,500 والشراء 158,400 (شفق نيوز). والسعر الرسمي 131,000 (شبكة 964).",
         "159,250", "Selling price per $100 at Baghdad exchange shops Thursday morning, per Shafaq",
         "دينار سعر بيع كل 100 دولار في محال الصيرفة ببغداد صباح الخميس، بحسب شفق نيوز",
         [("بغداد شراء", "158,250"), ("أربيل بيع", "158,500"), ("الرسمي", "131,000")],
         img(s, 2), "#FFC217",
         ["البيع 159,250", "الشراء 158,250", "والرسمي 131,000"]),
    beat("السبب", "خبير: تصريحات ومضاربة.. والأسعار تتأثر",
         "الخبير الاقتصادي علي دعدوش قال لشفق نيوز إن تصريحات بعض السياسيين والمضاربة وتراجع المعروض من الدولار وراء الارتفاع، وإنه ينعكس على أسعار السلع المستوردة.",
         "131,000", "CBI official rate in dinars per $100, per 964",
         "دينار السعر الرسمي لكل 100 دولار المقرر من البنك المركزي العراقي، بحسب شبكة 964",
         [("السبب 1", "تصريحات سياسيين"), ("السبب 2", "المضاربة"), ("الأثر", "أسعار المستورد")],
         img(s, 3), "#4CC9F0",
         ["تصريحات بعض السياسيين", "والمضاربة وتراجع المعروض", "والأثر على أسعار السلع"]),
]
p["arabicTicker"] = [
    "بورصتا الكفاح والحارثية: 158,850 ديناراً لكل 100 دولار صباح الخميس مقابل 157,250 الأربعاء (شفق نيوز)",
    "محال الصيرفة ببغداد: البيع 159,250 والشراء 158,250 — أربيل: البيع 158,500 والشراء 158,400 (شفق نيوز)",
    "شبكة 964: سعر البيع ببغداد 159,000 — والسعر الرسمي 131,000 لكل 100 دولار",
    "الخبير علي دعدوش: تصريحات بعض السياسيين وعدم اليقين والمضاربة وراء الارتفاع (شفق نيوز)",
    EQ,
]
p["endQuestion"] = EQ
p["sources"] = [SHAFAQ, S964]
SLATE[f"{D}-{s}"] = {
    "props": p,
    "brief": {
        "slug": f"{D}-{s}", "kicker": "الدولار اليوم",
        "hookHeadline": "الدولار يعبر المية وتسعة وخمسين",
        "voText": "سجل الدولار صباح اليوم في بورصتي الكفاح والحارثية ببغداد مئة وثمانية وخمسين ألفاً وثمانمئة وخمسين ديناراً لكل مئة دولار، مقابل مئة وسبعة وخمسين ألفاً ومئتين وخمسين أمس، بحسب شفق نيوز. وفي محال الصيرفة وصل سعر البيع إلى مئة وتسعة وخمسين ألفاً ومئتين وخمسين ديناراً. ويقول الخبير الاقتصادي علي دعدوش إن تصريحات بعض السياسيين والمضاربة وتراجع المعروض من الدولار وراء الارتفاع، وإن أثره ينعكس على أسعار السلع المستوردة. بكم اشتريت آخر مية دولار؟",
        "endQuestion": EQ,
        "sourcesLine": "المصادر: شفق نيوز · شبكة 964 — 17 أيلول 2026",
        "images": imgs(s), "audioBed": "audio/mood_newsroom.mp3",
        "statPops": [
            {"value": "158,850", "label": "بورصة بغداد صباح الخميس لكل 100 دولار", "matchWord": "والحارثية"},
            {"value": "159,250", "label": "سعر البيع بمحال الصيرفة ببغداد", "matchWord": "الصيرفة"},
        ],
    },
    "caption": f"""سعر الدولار اليوم في العراق — ليش صاعد؟

البورصة عبرت أمس بفرق واضح.. والسبب بالفيديو.

{EQ}

المصادر: شفق نيوز، شبكة 964 (17 أيلول 2026)

#سعر_الدولار_اليوم #الدينار_العراقي #العراق #البورصة
@photonect.news
""",
}

# ─────────────────────── c · Hormuz: 3 ships crossed; Iraq's $45bn estimated oil-revenue loss (P2 geo-economy → Iraqi wallet)
s = "c-hormuz-45-billion"
EQ = "حسّيت الأسعار ارتفعت هالشهر؟"
p = base(s, "mena_geo_economy", "A", "هرمز",
         "3 سفن بس عبرت هرمز.. وكم خسر العراق؟",
         "HORMUZ · SEP 16-17 | KPLER SHIP-TRACKING (VIA SHAFAQ/REUTERS): ONLY 3 CARGO VESSELS CROSSED HORMUZ ON WED VS 12 ON TUE AND A ~17 10-DAY AVERAGE; FIGURES EXCLUDE SHIPS WITH TRANSPONDERS OFF | FORMER MINISTER & ENERGY ACADEMIC LUAY AL-KHATIB TO RUDAW: PER MARKET ESTIMATES IRAQ LOST UP TO $45BN OIL REVENUE IN THE CRISIS'S FIRST SIX MONTHS; TRANSPORT & INSURANCE COSTS UP MORE THAN FIVEFOLD; SOMO DISCOUNTS MAY REACH 30%; WARNS OF WIDER DEFICIT, INFLATION, WEAKER DINAR")
p["beats"] = [
    beat("الممر", "هرمز: 3 سفن بس أمس",
         "بيانات تتبع السفن من كبلر أظهرت عبور 3 سفن شحن فقط لمضيق هرمز أمس الأربعاء، مقابل 12 سفينة الثلاثاء ومتوسط نحو 17 خلال 10 أيام (شفق نيوز).",
         "3", "Cargo ships that crossed Hormuz on Wednesday, vs 12 Tuesday and a ~17 ten-day average — Kpler data via Shafaq",
         "سفن شحن فقط عبرت مضيق هرمز يوم الأربعاء، مقابل 12 يوم الثلاثاء ومتوسط نحو 17 سفينة خلال الأيام العشرة الماضية، بحسب بيانات كبلر (شفق نيوز)",
         [("الأربعاء", "3 سفن"), ("الثلاثاء", "12 سفينة"), ("متوسط 10 أيام", "نحو 17")],
         img(s, 1), "#4CC9F0",
         ["3 سفن فقط أمس", "مقابل 12 الثلاثاء", "ومتوسط نحو 17"]),
    beat("الخسارة", "45 مليار دولار.. تقدير خسارة العراق",
         "الوزير الأسبق والمتخصص بالطاقة لؤي الخطيب قال لرووداو إن العراق خسر، حسب تقديرات الأسواق، إيرادات نفطية تصل إلى 45 مليار دولار بأول 6 أشهر من الأزمة.",
         "$45B", "Iraqi oil revenue lost in the crisis's first six months, per market estimates cited by Luay al-Khatib (Rudaw)",
         "مليار دولار إيرادات نفطية خسرها العراق في أول ستة أشهر من أزمة هرمز حسب تقديرات الأسواق، بحسب الوزير الأسبق لؤي الخطيب (رووداو)",
         [("الخسارة", "حتى 45 مليار $"), ("المدة", "أول 6 أشهر"), ("المصدر", "تقديرات الأسواق")],
         img(s, 2), "#D72638",
         ["إيرادات نفطية", "تصل إلى 45 مليار دولار", "بأول 6 أشهر من الأزمة"]),
    beat("الكلفة", "النقل والتأمين تضاعفوا 5 مرات",
         "الخطيب قال إن كلفة النقل والتأمين تضاعفت لأكثر من 5 أضعاف، وإن خصومات سومو قد تصل إلى 30%، محذراً من عجز أكبر بالموازنة وتضخم وتراجع الدينار (رووداو).",
         "30%", "Possible SOMO discount off world market price to cover transport and insurance, per al-Khatib (Rudaw)",
         "من سعر السوق العالمي قد تصل إليها خصومات سومو للمشترين لتغطية كلفة النقل والتأمين، بحسب لؤي الخطيب (رووداو)",
         [("النقل والتأمين", "+5 أضعاف"), ("خصم سومو", "حتى 30%"), ("التحذير", "عجز وتضخم")],
         img(s, 3), "#FFC217",
         ["النقل والتأمين أكثر من 5 أضعاف", "خصومات سومو حتى 30%", "وتحذير من العجز والتضخم"]),
]
p["arabicTicker"] = [
    "كبلر عبر شفق نيوز: 3 سفن شحن فقط عبرت مضيق هرمز الأربعاء مقابل 12 الثلاثاء — والأرقام لا تشمل سفناً أطفأت أجهزة الإرسال",
    "لؤي الخطيب لرووداو: العراق خسر حسب تقديرات الأسواق إيرادات نفطية تصل إلى 45 مليار دولار بأول 6 أشهر من الأزمة",
    "الخطيب: كلفة النقل والتأمين تضاعفت لأكثر من 5 أضعاف وخصومات سومو قد تصل إلى 30% من سعر السوق",
    EQ,
]
p["endQuestion"] = EQ
p["sources"] = [SHAFAQ, RUDAW]
SLATE[f"{D}-{s}"] = {
    "props": p,
    "brief": {
        "slug": f"{D}-{s}", "kicker": "هرمز",
        "hookHeadline": "هرمز يختنق.. وكم خسر العراق؟",
        "voText": "أظهرت بيانات تتبع السفن من شركة كبلر أن ثلاث سفن شحن فقط عبرت مضيق هرمز يوم الأربعاء، مقابل اثنتي عشرة سفينة في اليوم السابق، بحسب شفق نيوز. ويقول الوزير الأسبق والمتخصص في الطاقة لؤي الخطيب لرووداو إن العراق خسر، حسب تقديرات الأسواق، إيرادات نفطية تصل إلى خمسة وأربعين مليار دولار في أول ستة أشهر من الأزمة. ويضيف أن كلفة النقل والتأمين تضاعفت أكثر من خمس مرات، ويحذر من عجز أكبر في الموازنة وارتفاع التضخم. حسّيت الأسعار ارتفعت هالشهر؟",
        "endQuestion": EQ,
        "sourcesLine": "المصادر: شفق نيوز (بيانات كبلر) · رووداو — 16 و17 أيلول 2026",
        "images": imgs(s), "audioBed": "audio/mood_newsroom.mp3",
        "statPops": [
            {"value": "3 سفن", "label": "عبرت هرمز الأربعاء (كبلر)", "matchWord": "كبلر"},
            {"value": "$45 مليار", "label": "تقدير خسارة إيرادات العراق بأول 6 أشهر", "matchWord": "مليار"},
        ],
    },
    "caption": f"""مضيق هرمز والعراق — كم خسرنا من النفط؟

3 سفن بس عبرت بيوم واحد.. والرقم الأكبر بالفيديو.

{EQ}

المصادر: شفق نيوز (كبلر)، رووداو (16-17 أيلول 2026)

#العراق #مضيق_هرمز #النفط #الاقتصاد_العراقي
@photonect.news
""",
}

# ─────────────────────── d · MP Bahaa al-Nouri: 7 years for illicit gain (P1 corruption)
s = "d-mp-nouri-7-years"
EQ = "تتابع أحكام قضايا الفساد؟"
p = base(s, "iraq_corruption", "B", "نزاهة",
         "نائب بالبرلمان.. 7 سنوات سجن وأكثر من 40 مليار دينار",
         "BAGHDAD · SEP 16 | FEDERAL INTEGRITY COMMISSION: CENTRAL ANTI-CORRUPTION FELONY COURT SENTENCES MP BAHAA AL-NOURI (BAHAA AL-DIN NOOR MOHAMMED HUSSEIN) TO 7 YEARS FOR ILLICIT GAIN, ART. 19/II, LAW 30 OF 2011 | ORDERED TO REPAY IQD 5,887,850,000 AND $10,990,787 PLUS AN EQUAL FINE — OVER IQD 40BN IN TOTAL | SEPARATE 3-YEAR SENTENCE FOR HIDING INFORMATION IN FINANCIAL DISCLOSURE; HARSHER PENALTY APPLIED; ASSET SEIZURE UPHELD (SHAFAQ, 964, BAGHDAD TODAY, RUDAW)")
p["beats"] = [
    beat("الحكم", "7 سنوات سجن لنائب بتهمة الكسب غير المشروع",
         "هيئة النزاهة أعلنت أن محكمة جنايات مكافحة الفساد المركزية حكمت بالسجن 7 سنوات على النائب بهاء النوري عن جريمة الكسب غير المشروع (شفق نيوز · شبكة 964).",
         "7", "Years in prison for MP Bahaa al-Nouri for illicit gain, per the Integrity Commission (Shafaq, 964)",
         "سنوات سجن للنائب بهاء النوري عن جريمة الكسب غير المشروع، بقرار محكمة جنايات مكافحة الفساد المركزية كما أعلنت هيئة النزاهة (شفق نيوز · شبكة 964)",
         [("المحكمة", "مكافحة الفساد"), ("التهمة", "الكسب غير المشروع"), ("المادة", "19/ثانياً")],
         img(s, 1), "#D72638",
         ["محكمة مكافحة الفساد", "السجن 7 سنوات", "عن الكسب غير المشروع"]),
    beat("المبالغ", "رد 5,887,850,000 دينار و10,990,787 دولار",
         "المحكمة ألزمته برد 5,887,850,000 دينار و10,990,787 دولاراً قيمة الكسب غير المشروع، مع غرامة تعادلها، بحسب بيان هيئة النزاهة.",
         "+40", "Billion dinars: illicit gain to be repaid plus an equal fine, per the Integrity Commission",
         "مليار دينار: مجموع قيمة الكسب غير المشروع الواجب ردها والغرامة المالية التي تعادلها، بحسب هيئة النزاهة",
         [("بالدينار", "5,887,850,000"), ("بالدولار", "10,990,787"), ("الغرامة", "تعادل القيمة")],
         img(s, 2), "#FFC217",
         ["5,887,850,000 دينار", "و10,990,787 دولاراً", "وغرامة تعادلها"]),
    beat("الذمة", "و3 سنوات لإخفاء معلومات الذمة المالية",
         "المحكمة أصدرت حكماً آخر بالحبس الشديد 3 سنوات لإخفائه معلومات في استمارة الذمة المالية، وطبقت العقوبة الأشد وأيدت الحجز على أمواله (بغداد اليوم · رووداو).",
         "3", "Years' strict imprisonment for hiding information in his financial disclosure; the harsher 7-year term applies (Integrity Commission)",
         "سنوات حبس شديد في حكم ثانٍ لإخفاء معلومات في استمارة الذمة المالية، مع تطبيق العقوبة الأشد، بحسب هيئة النزاهة (بغداد اليوم · رووداو)",
         [("الحكم الثاني", "3 سنوات"), ("المطبق", "العقوبة الأشد"), ("الأموال", "الحجز مؤيد")],
         img(s, 3), "#4CC9F0",
         ["حبس شديد 3 سنوات", "إخفاء معلومات الذمة المالية", "والحجز على أمواله"]),
]
p["arabicTicker"] = [
    "هيئة النزاهة: السجن 7 سنوات للنائب بهاء النوري عن جريمة الكسب غير المشروع (شفق نيوز · شبكة 964)",
    "إلزامه برد 5,887,850,000 دينار و10,990,787 دولاراً مع غرامة تعادلها — أكثر من 40 مليار دينار",
    "حكم ثانٍ بالحبس الشديد 3 سنوات لإخفاء معلومات في استمارة الذمة المالية وتطبيق العقوبة الأشد (بغداد اليوم · رووداو)",
    EQ,
]
p["endQuestion"] = EQ
p["sources"] = [SHAFAQ, S964, BTODAY, RUDAW]
SLATE[f"{D}-{s}"] = {
    "props": p,
    "brief": {
        "slug": f"{D}-{s}", "kicker": "نزاهة",
        "hookHeadline": "نائب.. وسبع سنوات سجن",
        "voText": "أعلنت هيئة النزاهة الاتحادية أن محكمة جنايات مكافحة الفساد المركزية أصدرت حكماً بالسجن سبع سنوات على النائب بهاء النوري عن جريمة الكسب غير المشروع. وألزمته المحكمة برد أكثر من خمسة مليارات وثمانمئة وسبعة وثمانين مليون دينار، وعشرة ملايين وتسعمئة وتسعين ألف دولار، مع غرامة تعادلها، ليتجاوز المجموع أربعين مليار دينار. كما حكمت عليه بالحبس ثلاث سنوات لإخفاء معلومات في استمارة الذمة المالية، وقررت تطبيق العقوبة الأشد. تتابع أحكام قضايا الفساد؟",
        "endQuestion": EQ,
        "sourcesLine": "المصادر: هيئة النزاهة عبر شفق نيوز · شبكة 964 · بغداد اليوم · رووداو — 16 أيلول 2026",
        "images": imgs(s), "audioBed": "audio/mood_newsroom.mp3",
        "statPops": [
            {"value": "7 سنوات", "label": "سجن عن الكسب غير المشروع", "matchWord": "بالسجن"},
            {"value": "+40 مليار دينار", "label": "رد الكسب غير المشروع مع الغرامة", "matchWord": "أربعين"},
        ],
    },
    "caption": f"""حكم على نائب عراقي بالكسب غير المشروع — شكد المبلغ؟

هيئة النزاهة أعلنت الحكم.. والأرقام كاملة بالفيديو.

{EQ}

المصادر: هيئة النزاهة عبر شفق نيوز، شبكة 964، بغداد اليوم، رووداو (16 أيلول 2026)

#العراق #هيئة_النزاهة #مكافحة_الفساد #الكسب_غير_المشروع
@photonect.news
""",
}

# ─────────────────────── e · Basra crude -$8 as Saudi routes cargoes via Oman; 2027 budget price 53-56 (P2 control)
s = "e-basra-crude-minus-8"
EQ = "راتبك حكومي؟"
p = base(s, "mena_geo_economy", "C", "النفط",
         "خام البصرة ينزل 8 دولارات بيوم.. والموازنة تحسب 53-56",
         "SEP 16-17 | SHAFAQ: BASRA HEAVY $94.57 (-$8, -7.80%), BASRA MEDIUM $97.87 (-7.56%) THURSDAY; OPEC BASKET $124.63 (+1.52) | REUTERS VIA 964: BRENT FUTURES -$1.24 TO $104.59 AT 00:49 GMT AFTER SOURCES SAID SAUDI ARABIA OFFERS EXTRA CRUDE VIA SHIP-TO-SHIP TRANSFERS OFF SOHAR, OMAN, EASING FEARS AFTER EAST-WEST PIPELINE ATTACKS | PARLIAMENT FINANCE COMMITTEE MEMBER JAMAL KOJAR (BAGHDAD TODAY): IRAQ EXPECTED TO PRICE 2027 BUDGET BARREL AT $53-56; KUWAIT USED $57; GOVT MAY CONSIDER $60-70")
p["beats"] = [
    beat("البصرة", "خام البصرة الثقيل: 94.57 دولاراً",
         "خام البصرة الثقيل سجل 94.57 دولاراً للبرميل منخفضاً 8 دولارات بنسبة 7.80%، والمتوسط 97.87 دولاراً بتراجع 7.56% (شفق نيوز).",
         "-7.80%", "Basra Heavy's one-day drop to $94.57 a barrel, per Shafaq",
         "نسبة تراجع خام البصرة الثقيل إلى 94.57 دولاراً للبرميل يوم الخميس، بحسب شفق نيوز",
         [("الثقيل", "94.57 $"), ("المتوسط", "97.87 $"), ("التراجع", "8 دولارات")],
         img(s, 1), "#D72638",
         ["البصرة الثقيل 94.57", "والمتوسط 97.87", "تراجع 8 دولارات"]),
    beat("السعودية", "شحنات سعودية عبر عُمان.. وبرنت ينزل",
         "رويترز نقلت عن مصادر أن السعودية تطرح شحنات إضافية عبر النقل من سفينة لأخرى قبالة صحار في عُمان، وبرنت نزل 1.24 دولار إلى 104.59 (شبكة 964).",
         "104.59", "Brent futures, $ a barrel, down $1.24 at 00:49 GMT Thursday — Reuters via 964",
         "دولاراً سعر العقود الآجلة لخام برنت بعد تراجعه 1.24 دولار صباح الخميس، بحسب رويترز كما نقلت شبكة 964",
         [("برنت", "104.59 $"), ("التراجع", "1.24 $"), ("الممر", "صحار · عُمان")],
         img(s, 2), "#4CC9F0",
         ["شحنات سعودية إضافية", "عبر صحار في عُمان", "وبرنت 104.59"]),
    beat("الموازنة", "موازنة 2027: البرميل بين 53 و56",
         "عضو اللجنة المالية النيابية جمال كوجر قال لبغداد اليوم إن المتوقع احتساب البرميل بموازنة 2027 بين 53 و56 دولاراً، وقد تفكر الحكومة بين 60 و70.",
         "53-56", "Expected 2027 budget oil price range, $ a barrel, per finance committee member Jamal Kojar (Baghdad Today)",
         "دولاراً للبرميل النطاق المتوقع لاحتساب سعر النفط في موازنة 2027، بحسب عضو اللجنة المالية النيابية جمال كوجر (بغداد اليوم)",
         [("المتوقع", "53-56 $"), ("الكويت", "57 $"), ("خيار الحكومة", "60-70 $")],
         img(s, 3), "#FFC217",
         ["موازنة 2027", "البرميل بين 53 و56", "وقد تفكر الحكومة بـ60-70"]),
]
p["arabicTicker"] = [
    "شفق نيوز: خام البصرة الثقيل 94.57 دولاراً (-7.80%) والمتوسط 97.87 دولاراً (-7.56%)",
    "رويترز: السعودية تطرح شحنات خام إضافية عبر النقل من سفينة إلى أخرى قبالة صحار في عُمان — برنت 104.59 دولاراً (شبكة 964)",
    "جمال كوجر لبغداد اليوم: سعر البرميل المتوقع في موازنة 2027 بين 53 و56 دولاراً — والكويت بنت موازنتها على 57",
    EQ,
]
p["endQuestion"] = EQ
p["sources"] = [SHAFAQ, S964, BTODAY]
SLATE[f"{D}-{s}"] = {
    "props": p,
    "brief": None,
    "caption": f"""سعر نفط البصرة اليوم — نزل 8 دولارات، شنو يعني للموازنة؟

البرميل نزل بيوم واحد.. وموازنة 2027 تحسب رقم أقل بكثير.

{EQ}

المصادر: شفق نيوز، شبكة 964 (رويترز)، بغداد اليوم (16-17 أيلول 2026)

#العراق #نفط_البصرة #موازنة_2027 #النفط
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
