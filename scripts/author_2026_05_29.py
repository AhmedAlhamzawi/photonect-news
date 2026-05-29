#!/usr/bin/env python3
"""Author 6 tight-copy props.json for the 2026-05-29 slate (V10 engine).
Short bodies (<=26 words), punchy headings, person-centric brolls.
"""
import json
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE")
DATE = "2026-05-29"
DATE_EN = "MAY 29 • 2026"
DATE_AR = "29 مايو 2026"


def brolls(slug, order):
    base = f"images/news/{slug}"
    names = ["hero.jpg", "broll_1.jpg", "broll_2.jpg", "broll_3.jpg"]
    return [f"{base}/{names[i]}" for i in order]


def beat(label, heading, body, stat_val, stat_ar, stats, slug, order, src, accent):
    return {
        "label": label,
        "arabicHeading": heading,
        "arabicBody": body,
        "bigStat": {"value": stat_val, "label": stat_ar, "arabicLabel": stat_ar},
        "supportingStats": [{"label": l, "value": v} for (l, v) in stats],
        "broll": brolls(slug, order)[1],
        "brolls": brolls(slug, order),
        "brollType": "image",
        "accent": accent,
        "brollSource": src,
    }


SLATE = {}

# 1 — IRAQ ELECTRICITY (iraq_domestic, A)
s = f"{DATE}-iraq-electricity-collapse"
SLATE[s] = {
    "dateLabel": DATE_EN, "arabicDateLabel": DATE_AR, "handle": "@photonect.news",
    "audioBed": "audio/mood_cinematic.mp3", "topicBucket": "iraq_domestic", "variant": "A",
    "breaking": {
        "arabicKicker": "انهيار الكهرباء",
        "arabicHeadline": "العراق نحو صيف بلا كهرباء.. عجز 11 ألف ميغاواط",
        "englishSubhead": "IRAQ SUMMER GRID CRISIS • 40GW DEMAND vs 29GW SUPPLY • IRAN GAS CUT",
        "heroMedia": f"images/news/{s}/hero.jpg", "heroMediaType": "image",
    },
    "beats": [
        beat("العجز", "الطلب 40 ألف ميغاواط والإنتاج 29 فقط",
             "مع اشتداد الحر يواجه العراق أسوأ عجز كهربائي منذ سنوات؛ الطلب الصيفي 40 ألف ميغاواط مقابل إنتاج 29 ألفاً، وفق Shafaq News.",
             "11", "ألف ميغاواط فجوة الكهرباء",
             [("الطلب الصيفي", "40 ألف م.و"), ("الإنتاج الحالي", "29 ألف م.و"), ("العجز", "11 ألف م.و")],
             s, [0,1,2,3], "SHAFAQ NEWS • MAY 2026", "#FFC217"),
        beat("السبب", "ضربات إيران تقطع الغاز وتُسقط 3 آلاف ميغاواط",
             "بعد الضربات على حقل بارس الجنوبي في فبراير، توقف الغاز الإيراني فجأة، ففقدت الشبكة أكثر من 3 آلاف ميغاواط، وفق Human Rights Watch.",
             "3,000", "ميغاواط فُقدت بقطع الغاز",
             [("غاز إيران", "مقطوع"), ("الفاقد الفوري", "3000+ م.و"), ("منذ", "فبراير 2026")],
             s, [1,2,3,0], "HUMAN RIGHTS WATCH • 2026", "#D72638"),
        beat("الشارع", "الغضب يعود إلى الشوارع مع طول التقنين",
             "خرج محتجون يقطعون الطرق ويحرقون الإطارات اعتراضاً على ساعات التقنين الطويلة؛ والصيف الحارق ينذر بموجة احتجاج أوسع، وفق Al Jazeera.",
             "50°", "ذروة الحرارة الصيفية",
             [("احتجاجات", "قطع طرق"), ("التقنين", "ساعات طويلة"), ("الخطر", "تصعيد صيفي")],
             s, [2,3,0,1], "AL JAZEERA / THE NATIONAL • 2026", "#5B8FF9"),
    ],
    "sources": [
        {"name": "Shafaq News", "domain": "shafaq.com"},
        {"name": "Human Rights Watch", "domain": "hrw.org"},
        {"name": "Al Jazeera", "domain": "aljazeera.com"},
        {"name": "The National", "domain": "thenationalnews.com"},
    ],
    "arabicTicker": [
        "العراق نحو صيف بلا كهرباء.. عجز 11 ألف ميغاواط",
        "الطلب الصيفي 40 ألف ميغاواط مقابل إنتاج 29 ألفاً",
        "قطع الغاز الإيراني أسقط 3 آلاف ميغاواط من الشبكة",
        "محتجون يقطعون الطرق اعتراضاً على التقنين",
        "الحر يقترب من 50 درجة مع اشتداد الأزمة",
    ],
}

# 2 — MUSK SPACEX IPO (tech_ai, B) — SHOW MUSK
s = f"{DATE}-musk-spacex-ipo"
SLATE[s] = {
    "dateLabel": DATE_EN, "arabicDateLabel": DATE_AR, "handle": "@photonect.news",
    "audioBed": "audio/mood_newsroom.mp3", "topicBucket": "tech_ai", "variant": "B",
    "breaking": {
        "arabicKicker": "أكبر اكتتاب بالتاريخ",
        "arabicHeadline": "سبيس إكس نحو أكبر اكتتاب في التاريخ بـ1.75 تريليون",
        "englishSubhead": "SPACEX FILES FOR HISTORY'S BIGGEST IPO • $1.75T • STARSHIP V3 FLIES",
        "heroMedia": f"images/news/{s}/hero.jpg", "heroMediaType": "image",
    },
    "beats": [
        beat("الاكتتاب", "ماسك يطرح سبيس إكس في بورصة ناسداك",
             "قدّمت سبيس إكس أوراق الطرح في 20 مايو، وتبدأ التداول 12 يونيو برمز SPCX مستهدفةً جمع 75 مليار دولار، وفق CNBC.",
             "$1.75T", "التقييم المستهدف لسبيس إكس",
             [("الرمز", "SPCX"), ("بدء التداول", "12 يونيو"), ("جمع", "75 مليار $")],
             s, [0,1,2,3], "CNBC • MAY 26, 2026", "#FFC217"),
        beat("الإمبراطورية", "ماسك يدمج xAI داخل سبيس إكس",
             "أعلن ماسك دمج xAI ومنصة Grok ضمن قسم SpaceXAI، رابطاً رقائق إنفيديا ببيانات تسلا عبر شبكة الأقمار في حلقة مغلقة، وفق The Motley Fool.",
             "$1.25T", "تقييم الدمج مع xAI",
             [("xAI", "مدموج"), ("Grok", "ضمن سبيس إكس"), ("الشبكة", "أقمار ستارلينك")],
             s, [1,2,3,0], "THE MOTLEY FOOL / ELECTREK • 2026", "#D72638"),
        beat("نحو المريخ", "ستارشيب الجيل الثالث يقترب من المريخ",
             "أطلقت سبيس إكس النسخة الثالثة من ستارشيب في رحلتها الثانية عشرة يوم 20 مايو، الأقوى على الإطلاق، خطوةً نحو المريخ، وفق Teslarati.",
             "V3", "أقوى نسخة من ستارشيب",
             [("الرحلة", "الثانية عشرة"), ("الإطلاق", "20 مايو"), ("الهدف", "المريخ")],
             s, [2,3,0,1], "TESLARATI / CNBC • MAY 2026", "#5B8FF9"),
    ],
    "sources": [
        {"name": "CNBC", "domain": "cnbc.com"},
        {"name": "Electrek", "domain": "electrek.co"},
        {"name": "Teslarati", "domain": "teslarati.com"},
        {"name": "The Motley Fool", "domain": "fool.com"},
    ],
    "arabicTicker": [
        "سبيس إكس نحو أكبر اكتتاب في التاريخ بـ1.75 تريليون دولار",
        "بدء التداول 12 يونيو في ناسداك برمز SPCX",
        "ماسك يدمج xAI ومنصة Grok ضمن سبيس إكس",
        "ستارشيب الجيل الثالث ينطلق في رحلته الثانية عشرة",
        "حلقة مغلقة: إنفيديا وتسلا وستارلينك تحت مظلة واحدة",
    ],
}

# 3 — WORLD CUP (wildcard, C) — SHOW MESSI + RONALDO
s = f"{DATE}-worldcup-messi-ronaldo"
SLATE[s] = {
    "dateLabel": DATE_EN, "arabicDateLabel": DATE_AR, "handle": "@photonect.news",
    "audioBed": "audio/mood_orchestral.mp3", "topicBucket": "wildcard", "variant": "C",
    "breaking": {
        "arabicKicker": "كأس العالم 2026",
        "arabicHeadline": "ميسي ورونالدو نحو مونديال سادس تاريخي",
        "englishSubhead": "MESSI & RONALDO HEADED FOR A RECORD 6TH WORLD CUP • USA/MEXICO/CANADA",
        "heroMedia": f"images/news/{s}/hero.jpg", "heroMediaType": "image",
    },
    "beats": [
        beat("الأسطورتان", "ميسي ورونالدو أول من يلعب 6 مونديالات",
             "اختار سكالوني ميسي (38 عاماً) ضمن قائمة الأرجنتين، وأُدرج رونالدو مع البرتغال؛ ليصبحا أول لاعبَين في ست بطولات عالمية، وفق ESPN.",
             "6", "مونديال لكلٍّ منهما — رقم قياسي",
             [("ميسي", "38 عاماً"), ("القائمة", "26 لاعباً"), ("الأرجنتين", "حاملة اللقب")],
             s, [0,1,2,3], "ESPN / FOX SPORTS • MAY 28, 2026", "#FFC217"),
        beat("العرب حاضرون", "المغرب والجزائر يحملان راية العرب",
             "أعلن المغرب قائمته بقيادة حكيمي وإبراهيم دياز، وتفتتح الأرجنتين مشوارها بمواجهة الجزائر في 16 يونيو بكنساس سيتي، وفق FOX Sports.",
             "48", "منتخباً في أول مونديال موسّع",
             [("المغرب", "حكيمي ودياز"), ("الافتتاح", "الأرجنتين vs الجزائر"), ("الموعد", "16 يونيو")],
             s, [1,2,3,0], "FOX SPORTS / YAHOO • 2026", "#D72638"),
        beat("الحلم", "هل تحتفظ الأرجنتين باللقب لأول مرة منذ 1962؟",
             "تسعى الأرجنتين لتصبح أول من يحتفظ باللقب منذ البرازيل 1962؛ البطولة الأولى بـ48 منتخباً وعبر ثلاث دول، وفق Yahoo Sports.",
             "1962", "آخر احتفاظ متتالٍ باللقب",
             [("المستضيف", "3 دول"), ("البداية", "يونيو 2026"), ("التحدي", "لقب متتالٍ")],
             s, [2,3,0,1], "YAHOO SPORTS / THESCORE • 2026", "#5B8FF9"),
    ],
    "sources": [
        {"name": "ESPN", "domain": "espn.com"},
        {"name": "FOX Sports", "domain": "foxsports.com"},
        {"name": "Yahoo Sports", "domain": "sports.yahoo.com"},
        {"name": "theScore", "domain": "thescore.com"},
    ],
    "arabicTicker": [
        "ميسي ورونالدو نحو مونديال سادس تاريخي",
        "أول لاعبَين يشاركان في ست بطولات كأس عالم",
        "المغرب بقيادة حكيمي ضمن المتأهلين",
        "الأرجنتين تفتتح ضد الجزائر في 16 يونيو",
        "أول مونديال بـ48 منتخباً وعبر ثلاث دول",
    ],
}

# 4 — LEBANON CEASEFIRE (mena_geopolitics, A) — SHOW al-Sharaa
s = f"{DATE}-lebanon-ceasefire-brink"
SLATE[s] = {
    "dateLabel": DATE_EN, "arabicDateLabel": DATE_AR, "handle": "@photonect.news",
    "audioBed": "audio/mood_mideast.mp3", "topicBucket": "mena_geopolitics", "variant": "A",
    "breaking": {
        "arabicKicker": "هدنة على الحافة",
        "arabicHeadline": "هدنة لبنان تُمدَّد 45 يوماً وسط خروقات متصاعدة",
        "englishSubhead": "LEBANON TRUCE EXTENDED 45 DAYS • ISRAEL-HEZBOLLAH CLASHES RISE",
        "heroMedia": f"images/news/{s}/hero.jpg", "heroMediaType": "image",
    },
    "beats": [
        beat("التمديد", "تمديد الهدنة 45 يوماً بوساطة أمريكية",
             "مُدِّدت الهدنة بين إسرائيل ولبنان 45 يوماً في 15 مايو، عقب هدنة عشرة أيام رعاها ترامب في أبريل، لكنها تبقى هشّة، وفق Council on Foreign Relations.",
             "45", "يوماً تمديد الهدنة",
             [("التمديد", "15 مايو"), ("هدنة ترامب", "أبريل"), ("الوضع", "هشّ")],
             s, [0,1,2,3], "COUNCIL ON FOREIGN RELATIONS • 2026", "#FFC217"),
        beat("الخروقات", "الجيش اللبناني ينهي المرحلة الأولى لنزع السلاح",
             "أعلن الجيش إتمام المرحلة الأولى من نزع سلاح حزب الله، فيما تتصاعد الغارات الإسرائيلية والردود المتبادلة، وفق ABC News والأمم المتحدة.",
             "1", "أولى مراحل نزع السلاح",
             [("الجيش", "أنهى المرحلة 1"), ("الغارات", "تتصاعد"), ("النزوح", "مستمر")],
             s, [1,2,3,0], "ABC NEWS / UN NEWS • 2026", "#D72638"),
        beat("تحوّل سوري", "الشرع يدعم نزع سلاح حزب الله",
             "الرئيس السوري أحمد الشرع يساند بيروت، وقد اعترضت دمشق شحنة صواريخ دقيقة من إيران إلى الحزب — تحوّل لافت، وفق The Washington Institute.",
             "0", "تهاون سوري مع تهريب السلاح",
             [("الشرع", "يدعم بيروت"), ("دمشق", "اعترضت صواريخ"), ("المصدر", "إيران")],
             s, [2,3,0,1], "THE WASHINGTON INSTITUTE • 2026", "#5B8FF9"),
    ],
    "sources": [
        {"name": "Council on Foreign Relations", "domain": "cfr.org"},
        {"name": "The Washington Institute", "domain": "washingtoninstitute.org"},
        {"name": "UN News", "domain": "news.un.org"},
        {"name": "ABC News", "domain": "abcnews.go.com"},
        {"name": "Al Jazeera", "domain": "aljazeera.com"},
    ],
    "arabicTicker": [
        "هدنة لبنان تُمدَّد 45 يوماً وسط خروقات متصاعدة",
        "الجيش اللبناني ينهي المرحلة الأولى من نزع السلاح",
        "تصاعد الغارات الإسرائيلية رغم الهدنة",
        "الرئيس السوري الشرع يدعم نزع سلاح حزب الله",
        "دمشق تعترض شحنة صواريخ إيرانية إلى الحزب",
    ],
}

# 5 — SPACE / FUSION (wildcard, B)
s = f"{DATE}-space-iss-fusion"
SLATE[s] = {
    "dateLabel": DATE_EN, "arabicDateLabel": DATE_AR, "handle": "@photonect.news",
    "audioBed": "audio/mood_cinematic.mp3", "topicBucket": "wildcard", "variant": "B",
    "breaking": {
        "arabicKicker": "قفزات الفضاء",
        "arabicHeadline": "أول إخلاء طبي من محطة الفضاء وقفزة في الاندماج النووي",
        "englishSubhead": "FIRST-EVER ISS MEDICAL EVACUATION • FUSION-ROCKET PLASMA IGNITION",
        "heroMedia": f"images/news/{s}/hero.jpg", "heroMediaType": "image",
    },
    "beats": [
        beat("الإخلاء", "ناسا تُعيد روّاداً من المحطة لأول مرة طبياً",
             "للمرة الأولى في تاريخ محطة الفضاء الدولية، تُعيد ناسا مجموعة روّاد إلى الأرض مبكراً بسبب مشكلة صحية، وفق NASA.",
             "1", "أول إخلاء طبي في تاريخ المحطة",
             [("السبب", "مشكلة صحية"), ("القرار", "عودة مبكرة"), ("السابقة", "الأولى تاريخياً")],
             s, [0,1,2,3], "NASA • MAY 2026", "#FFC217"),
        beat("الاندماج", "بريطانيا تُشعل البلازما داخل محرك اندماجي",
             "حقّق علماء بريطانيون أول إشعال بلازما داخل محرك صاروخ يعمل بالاندماج النووي، ما قد يختصر زمن الرحلات إلى المريخ، وفق Euronews.",
             "1st", "أول إشعال بلازما في محرك صاروخ",
             [("الإنجاز", "إشعال بلازما"), ("الدولة", "بريطانيا"), ("الأثر", "رحلات أسرع")],
             s, [1,2,3,0], "EURONEWS / NATURE • 2026", "#D72638"),
        beat("المريخ يقترب", "750 تجربة في المدار تُعيد رسم المستقبل",
             "كشفت ناسا أن أكثر من 750 تجربة عام 2025 شملت جراحة روبوتية في الفضاء ومواد جديدة، بفوائد تمتد إلى الأرض، وفق Nature.",
             "750", "تجربة علمية على المحطة في 2025",
             [("التجارب", "750+"), ("منها", "جراحة روبوتية"), ("الفائدة", "تمتد للأرض")],
             s, [2,3,0,1], "NATURE / NASA • 2026", "#5B8FF9"),
    ],
    "sources": [
        {"name": "NASA", "domain": "nasa.gov"},
        {"name": "Nature", "domain": "nature.com"},
        {"name": "Euronews", "domain": "euronews.com"},
        {"name": "Space.com", "domain": "space.com"},
    ],
    "arabicTicker": [
        "أول إخلاء طبي في تاريخ محطة الفضاء الدولية",
        "بريطانيا تُشعل البلازما داخل محرك صاروخ اندماجي",
        "750 تجربة علمية على المحطة في 2025",
        "جراحة روبوتية في الفضاء بفوائد تمتد للأرض",
        "الاندماج النووي يقرّب رحلات المريخ",
    ],
}

# 6 — SUDAN (mena_geopolitics, C)
s = f"{DATE}-sudan-famine-year4"
SLATE[s] = {
    "dateLabel": DATE_EN, "arabicDateLabel": DATE_AR, "handle": "@photonect.news",
    "audioBed": "audio/mood_newsroom.mp3", "topicBucket": "mena_geopolitics", "variant": "C",
    "breaking": {
        "arabicKicker": "حرب منسيّة",
        "arabicHeadline": "السودان في عامه الرابع: 14 مليون نازح ومجاعة مؤكدة",
        "englishSubhead": "SUDAN ENTERS YEAR 4 • 14M DISPLACED • FAMINE CONFIRMED IN DARFUR",
        "heroMedia": f"images/news/{s}/hero.jpg", "heroMediaType": "image",
    },
    "beats": [
        beat("الكارثة", "أكبر أزمة نزوح في العالم تدخل عامها الرابع",
             "دخلت حرب السودان عامها الرابع لتصبح أكبر أزمة إنسانية ونزوح بالعالم؛ نزح 14 مليوناً، عبر 4.4 مليون منهم الحدود، وفق UN News.",
             "14M", "نازح — أكبر أزمة نزوح بالعالم",
             [("النازحون", "14 مليون"), ("عبر الحدود", "4.4 مليون"), ("الحرب", "4 سنوات")],
             s, [0,1,2,3], "UN NEWS • 2026", "#FFC217"),
        beat("المجاعة", "المجاعة مؤكدة في دارفور وكردفان",
             "أكّدت المنظمات الأممية المجاعة في دارفور وكردفان حيث أعنف القتال؛ وحرب إيران رفعت أسعار الوقود 24% ففاقمت الجوع، وفق Arab News.",
             "+24%", "ارتفاع أسعار الوقود يفاقم الجوع",
             [("المجاعة", "دارفور وكردفان"), ("الوقود", "+24%"), ("الغذاء", "يرتفع")],
             s, [1,2,3,0], "ARAB NEWS / NPR • 2026", "#D72638"),
        beat("صمت دولي", "العالم يتخاذل والتمويل الإغاثي ينهار",
             "حذّر مسؤول الإغاثة الأممي من تخاذل العالم مع دخول الحرب عامها الرابع؛ التمويل يتعثّر ودول عدة منخرطة في الصراع، وفق Brookings.",
             "4", "سنوات حرب دون أفق للحل",
             [("التمويل", "متعثّر"), ("الانخراط", "إقليمي"), ("الأفق", "غائب")],
             s, [2,3,0,1], "BROOKINGS / CFR • 2026", "#5B8FF9"),
    ],
    "sources": [
        {"name": "UN News", "domain": "news.un.org"},
        {"name": "Arab News", "domain": "arabnews.com"},
        {"name": "Council on Foreign Relations", "domain": "cfr.org"},
        {"name": "NPR", "domain": "npr.org"},
        {"name": "Brookings", "domain": "brookings.edu"},
    ],
    "arabicTicker": [
        "السودان في عامه الرابع: 14 مليون نازح ومجاعة مؤكدة",
        "4.4 مليون سوداني عبروا الحدود هرباً من الحرب",
        "المجاعة مؤكدة في دارفور وكردفان",
        "حرب إيران ترفع أسعار الوقود 24% وتفاقم الجوع",
        "الأمم المتحدة: العالم يتخاذل عن نجدة السودان",
    ],
}


def main():
    for slug, props in SLATE.items():
        # sanity: fix any malformed supportingStats (slug 6 beat3 guard)
        for b in props["beats"]:
            b["supportingStats"] = [x for x in b["supportingStats"] if isinstance(x, dict)][:3]
        d = ROOT / "data" / "posts" / slug / ".meta"
        d.mkdir(parents=True, exist_ok=True)
        (d / "props.json").write_text(json.dumps(props, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        # media-stamp so the auto-hunter never overwrites our curated images
        (d / "media-stamp.json").write_text('{"manual":true,"source":"nano-banana-pro+real"}\n', encoding="utf-8")
        wc = max(len(b["arabicBody"].split()) for b in props["beats"])
        print(f"wrote {slug}  (max body words: {wc})")


if __name__ == "__main__":
    main()
