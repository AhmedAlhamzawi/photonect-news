#!/usr/bin/env python3
"""Author the 6 props.json for the 2026-05-30 slate (V10.1 engine).

V10.1 shows ONE still image per beat (variant reads each beat's `broll`), so each
beat's `broll` is set to the image that MATCHES that beat's text:
  breaking.heroMedia -> hero.jpg
  beat 0 -> broll_1.jpg, beat 1 -> broll_2.jpg, beat 2 -> broll_3.jpg
`brolls` is kept (first entry == broll) for backward-compat but engine uses `broll`.

audioBed is a placeholder here; assign-mood-rotation.py overwrites it deterministically.
Arabic is the first-pass draft; an Opus copywriter subagent polishes in place after.
"""
import json
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE")
POSTS = ROOT / "data" / "posts"
DATE = "2026-05-30"
DATE_LABEL = "MAY 30 • 2026"
AR_DATE = "30 مايو 2026"
ACCENTS = ["#FFC217", "#D72638", "#5B8FF9"]


def img(slug, name):
    return f"images/news/{DATE}-{slug}/{name}"


def brolls_for(slug, primary):
    names = ["hero.jpg", "broll_1.jpg", "broll_2.jpg", "broll_3.jpg"]
    ordered = [primary] + [n for n in names if n != primary]
    return [img(slug, n) for n in ordered]


def beat(slug, idx, label, heading, body, big_val, big_label, stats, src):
    primary = ["broll_1.jpg", "broll_2.jpg", "broll_3.jpg"][idx]
    return {
        "label": label,
        "arabicHeading": heading,
        "arabicBody": body,
        "bigStat": {"value": big_val, "label": big_label, "arabicLabel": big_label},
        "supportingStats": [{"label": l, "value": v} for (l, v) in stats],
        "broll": img(slug, primary),
        "brolls": brolls_for(slug, primary),
        "brollType": "image",
        "accent": ACCENTS[idx],
        "brollSource": src,
    }


SLATE = {}

# ───────────────────────── 1. iraq-water-crisis (iraq_domestic, C) ─────────────────────────
s = "iraq-water-crisis"
SLATE[s] = {
    "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": "@photonect.news",
    "audioBed": "audio/music_01.mp3", "topicBucket": "iraq_domestic", "variant": "C",
    "breaking": {
        "arabicKicker": "أسوأ جفاف منذ قرن",
        "arabicHeadline": "العراق في أسوأ جفاف منذ 1933 ونهراه ينحسران",
        "englishSubhead": "IRAQ'S WORST DROUGHT SINCE 1933 • TIGRIS & EUPHRATES DOWN 27% • RESERVES AT 80-YEAR LOW",
        "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
    },
    "beats": [
        beat(s, 0, "الأنهار", "دجلة والفرات إلى أدنى مستوى بثمانية عقود",
             "انخفضت مناسيب دجلة والفرات حتى 27% ووصلت الخزانات إلى أدنى مستوى منذ 80 عاماً، وفق ناسا ووزارة الموارد المائية.",
             "27%", "هبوط مناسيب النهرين",
             [("الخزانات", "أدنى 80 عاماً"), ("حصة العراق", "<35%"), ("السنة", "الأجف منذ 1933")],
             "NASA EARTH OBSERVATORY • 2026"),
        beat(s, 1, "المنبع", "سدود تركيا وإيران تخنق تدفق المياه",
             "يصل العراق أقل من 35% من حصته المائية بعد سدود بنتها تركيا وإيران على المنبع، وفق الجزيرة وذي أراب ويكلي.",
             "35%", "ما يصل العراق من حصته",
             [("المنبع", "تركيا وإيران"), ("البصرة", "3.5 مليون متأثر"), ("السبب", "سدود ومناخ")],
             "AL JAZEERA / THE ARAB WEEKLY • 2026"),
        beat(s, 2, "الإنذار", "تحذير رسمي: الفرات قد يجف بحلول 2040",
             "حذّرت وزارة الموارد المائية من جفاف الفرات كلياً بحلول 2040 دون إجراء عاجل، فيما تعتمد البصرة على صهاريج يومية، وفق الجزيرة.",
             "2040", "موعد الجفاف الكامل المحتمل",
             [("البصرة", "مياه بالصهاريج"), ("التلوث", "يتفاقم جنوباً"), ("الإنذار", "وزارة المياه")],
             "IRAQ MINISTRY OF WATER RESOURCES • 2026"),
    ],
    "sources": [
        {"name": "Al Jazeera", "domain": "aljazeera.com"},
        {"name": "NASA Earth Observatory", "domain": "science.nasa.gov"},
        {"name": "AsiaNews", "domain": "asianews.it"},
        {"name": "The Arab Weekly", "domain": "thearabweekly.com"},
        {"name": "Iraq Ministry of Water Resources", "domain": "mowr.gov.iq"},
    ],
    "arabicTicker": [
        "العراق يعيش أسوأ جفاف منذ عام 1933",
        "مناسيب دجلة والفرات تنخفض حتى 27%",
        "الخزانات المائية إلى أدنى مستوى منذ 80 عاماً",
        "سدود تركيا وإيران تقلّص حصة العراق إلى أقل من 35%",
        "وزارة الموارد المائية تحذّر من جفاف الفرات بحلول 2040",
    ],
}

# ───────────────────────── 2. gaza-seizure-70 (mena_geopolitics, A) ─────────────────────────
s = "gaza-seizure-70"
SLATE[s] = {
    "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": "@photonect.news",
    "audioBed": "audio/music_01.mp3", "topicBucket": "mena_geopolitics", "variant": "A",
    "breaking": {
        "arabicKicker": "عاجل",
        "arabicHeadline": "نتنياهو يأمر بالسيطرة على 70% من قطاع غزة",
        "englishSubhead": "NETANYAHU ORDERS SEIZURE OF 70% OF GAZA • HAMAS REJECTS DISARMAMENT • IDF KILLS ODEH",
        "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
    },
    "beats": [
        beat(s, 0, "القرار", "نتنياهو يوسّع السيطرة من 53% إلى 70%",
             "أمر نتنياهو الجيش بالسيطرة على 70% من غزة، صعوداً من 60% الأسبوع الماضي و53% قبل شهر، وفق تايمز أوف إسرائيل.",
             "70%", "مساحة غزة تحت السيطرة",
             [("قبل أسبوع", "60%"), ("قبل شهر", "53%"), ("المصدر", "تايمز أوف إسرائيل")],
             "TIMES OF ISRAEL • MAY 28, 2026"),
        beat(s, 1, "نزع السلاح", "حماس ترفض نزع السلاح وخطة ترامب تتعثر",
             "رفضت حماس توجيه مجلس السلام الدولي بنزع سلاحها، وهو شرط محوري في خطة ترامب ذات العشرين بنداً، وفق واشنطن بوست.",
             "20", "بنود خطة ترامب للسلام",
             [("الشرط", "نزع السلاح"), ("الرد", "رفض حماس"), ("الخط", "الأصفر")],
             "THE WASHINGTON POST • 2026"),
        beat(s, 2, "التصعيد", "الجيش يقتل القيادي محمد عودة و10 خروقات",
             "قتل الجيش الإسرائيلي القيادي في حماس محمد عودة، وسجّل 10 خروقات للهدنة بين 21 و28 مايو، وفق مؤسسة الدفاع عن الديمقراطيات.",
             "10", "خروقات للهدنة بأسبوع",
             [("21–28 مايو", "10 خروقات"), ("القتيل", "محمد عودة"), ("المرصد", "FDD / ACLED")],
             "FDD / ACLED • MAY 29, 2026"),
    ],
    "sources": [
        {"name": "Times of Israel", "domain": "timesofisrael.com"},
        {"name": "The Washington Post", "domain": "washingtonpost.com"},
        {"name": "FDD", "domain": "fdd.org"},
        {"name": "Al Jazeera", "domain": "aljazeera.com"},
        {"name": "ACLED", "domain": "acleddata.com"},
    ],
    "arabicTicker": [
        "نتنياهو يأمر بالسيطرة على 70% من قطاع غزة",
        "صعود من 60% قبل أسبوع و53% قبل شهر",
        "حماس ترفض نزع السلاح وخطة ترامب ذات العشرين بنداً تتعثر",
        "الجيش الإسرائيلي يقتل القيادي محمد عودة",
        "تسجيل 10 خروقات للهدنة بين 21 و28 مايو",
    ],
}

# ───────────────────────── 3. oil-worst-month (global_economy, B) ─────────────────────────
s = "oil-worst-month"
SLATE[s] = {
    "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": "@photonect.news",
    "audioBed": "audio/music_01.mp3", "topicBucket": "global_economy", "variant": "B",
    "breaking": {
        "arabicKicker": "أسوأ شهر منذ كورونا",
        "arabicHeadline": "برنت يهوي 19% في أسوأ شهر منذ كورونا",
        "englishSubhead": "BRENT DOWN 19% IN MAY — WORST MONTH SINCE COVID • $92 • HORMUZ DEAL NEARS",
        "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
    },
    "beats": [
        beat(s, 0, "السوق", "برنت يغلق مايو عند 92 دولاراً هابطاً 19%",
             "أغلق خام برنت مايو عند 92.56 دولار منخفضاً 19% خلال الشهر، في أسوأ أداء شهري منذ جائحة كورونا، وفق CNBC.",
             "-19%", "هبوط برنت في مايو",
             [("الإغلاق", "$92.56"), ("عن القمة", "-20%"), ("المصدر", "CNBC")],
             "CNBC • MAY 29, 2026"),
        beat(s, 1, "هرمز", "اتفاق أمريكي إيراني يقترب لفتح مضيق هرمز",
             "تراجع النفط مع اقتراب مذكرة تفاهم أمريكية إيرانية لـ60 يوماً تخفّف قيود الشحن عبر هرمز، بانتظار توقيع ترامب، وفق رويترز.",
             "60", "أيام مذكرة وقف التصعيد",
             [("المضيق", "هرمز"), ("الحالة", "بانتظار ترامب"), ("الأثر", "شحن أوسع")],
             "REUTERS • MAY 29, 2026"),
        beat(s, 2, "الطلب", "أوبك تخفّض توقعات نمو الطلب لـ2026",
             "خفّضت أوبك توقعات نمو الطلب العالمي في 2026 إلى 1.2 مليون برميل يومياً من 1.4 مليون، مع رهان الأسواق على هدنة دائمة، وفق أوبك.",
             "1.2M", "نمو الطلب المتوقع (ب/ي)",
             [("سابقاً", "1.4M ب/ي"), ("الرهان", "هدنة دائمة"), ("المصدر", "OPEC")],
             "OPEC / EIA • 2026"),
    ],
    "sources": [
        {"name": "CNBC", "domain": "cnbc.com"},
        {"name": "Reuters", "domain": "reuters.com"},
        {"name": "Al Jazeera", "domain": "aljazeera.com"},
        {"name": "OPEC", "domain": "opec.org"},
        {"name": "EIA", "domain": "eia.gov"},
    ],
    "arabicTicker": [
        "برنت يغلق مايو عند 92.56 دولار هابطاً 19%",
        "أسوأ أداء شهري للنفط منذ جائحة كورونا",
        "النفط يتراجع 20% عن قمته في 2026",
        "مذكرة تفاهم أمريكية إيرانية لـ60 يوماً قرب فتح هرمز",
        "أوبك تخفّض توقعات نمو الطلب إلى 1.2 مليون برميل يومياً",
    ],
}

# ───────────────────────── 4. neom-line-halt (gulf_regional, C) ─────────────────────────
s = "neom-line-halt"
SLATE[s] = {
    "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": "@photonect.news",
    "audioBed": "audio/music_01.mp3", "topicBucket": "gulf_regional", "variant": "C",
    "breaking": {
        "arabicKicker": "تحوّل استراتيجي",
        "arabicHeadline": "السعودية توقف ذا لاين حتى ما بعد 2030",
        "englishSubhead": "NEOM HALTS THE LINE TO POST-2030 • PIF PIVOTS 80% DOMESTIC • POPULATION TARGET CUT TO 100K",
        "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
    },
    "beats": [
        beat(s, 0, "الصندوق", "صندوق الاستثمارات يعيد 80% من رهانه للداخل",
             "تستهدف استراتيجية الصندوق السيادي 2026‑2030 تخصيص 80% محلياً وخفض الانكشاف الخارجي إلى 20%، تحت ضغط مالي، وفق سيمافور.",
             "80%", "التخصيص المحلي الجديد",
             [("الخارج", "20% فقط"), ("السبب", "ضغط مالي"), ("المصدر", "سيمافور")],
             "SEMAFOR • MAY 2026"),
        beat(s, 1, "ذا لاين", "ذا لاين يتأجل وهدف السكان يهوي إلى 100 ألف",
             "أجّلت نيوم مدينة ذا لاين، المقدّرة بأكثر من تريليون دولار، إلى ما بعد 2030 وخفضت هدف سكان 2030 إلى 100 ألف، وفق سيمافور.",
             "$1T+", "كلفة ذا لاين المقدّرة",
             [("الطول", "170 كم"), ("سكان 2030", "100 ألف"), ("الحالة", "مؤجل")],
             "SEMAFOR / NEOM • 2026"),
        beat(s, 2, "البديل", "نيوم تحوّل 3 مليارات نحو مدينة أوكساجون",
             "تتجه نيوم لإنفاق نحو 3 مليارات دولار على أوكساجون الصناعية ومراكز البيانات، تحوّلاً نحو مشاريع أسرع عائداً، وفق منتدى الخليج الدولي.",
             "$3B", "إنفاق أوكساجون الجديد",
             [("التوجه", "صناعة وبيانات"), ("المنطق", "عائد أسرع"), ("المصدر", "GIF")],
             "GULF INTERNATIONAL FORUM • 2026"),
    ],
    "sources": [
        {"name": "Semafor", "domain": "semafor.com"},
        {"name": "Gulf International Forum", "domain": "gulfif.org"},
        {"name": "House of Saud", "domain": "houseofsaud.com"},
        {"name": "Bloomberg", "domain": "bloomberg.com"},
    ],
    "arabicTicker": [
        "نيوم توقف مدينة ذا لاين إلى ما بعد 2030",
        "هدف سكان ذا لاين 2030 يهوي إلى 100 ألف",
        "صندوق الاستثمارات يخصّص 80% للداخل و20% للخارج",
        "ذا لاين قُدّرت كلفته بأكثر من تريليون دولار",
        "نيوم تحوّل 3 مليارات دولار نحو مدينة أوكساجون",
    ],
}

# ───────────────────────── 5. syria-energy-deal (mena_geopolitics, A) ─────────────────────────
s = "syria-energy-deal"
SLATE[s] = {
    "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": "@photonect.news",
    "audioBed": "audio/music_01.mp3", "topicBucket": "mena_geopolitics", "variant": "A",
    "breaking": {
        "arabicKicker": "إعمار سوريا",
        "arabicHeadline": "دمشق توقّع اتفاق طاقة بـ7 مليارات دولار",
        "englishSubhead": "SYRIA SIGNS $7B ENERGY DEAL IN DAMASCUS • 4,000MW GAS + 1,000MW SOLAR • 50,000 JOBS",
        "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
    },
    "beats": [
        beat(s, 0, "الاتفاق", "اتفاق بـ7 مليارات لإعادة بناء كهرباء سوريا",
             "وقّعت دمشق في 29 مايو اتفاقاً للطاقة بـ7 مليارات دولار لبناء محطات في حمص وحماة ودير الزور، وفق المجلس الأطلسي.",
             "$7B", "قيمة اتفاق الطاقة",
             [("التاريخ", "29 مايو"), ("المدن", "حمص وحماة"), ("المصدر", "المجلس الأطلسي")],
             "ATLANTIC COUNCIL • MAY 29, 2026"),
        beat(s, 1, "القدرة", "4000 ميغاواط غاز و1000 ميغاواط شمسية",
             "يضيف الاتفاق 4000 ميغاواط من الغاز و1000 من الطاقة الشمسية، بإنتاج 35 مليار كيلوواط ساعة سنوياً، وفق ديلي صباح.",
             "5,000MW", "إجمالي القدرة المضافة",
             [("غاز", "4000 ميغا"), ("شمسية", "1000 ميغا"), ("الإنتاج", "35 مليار ك.و.س")],
             "DAILY SABAH • 2026"),
        beat(s, 2, "الإعمار", "تركيا تقود إعمار سوريا بعد سقوط الأسد",
             "يأتي الاتفاق ضمن إعمار تقوده تركيا بعد سقوط الأسد، ويَعِد بنحو 50 ألف وظيفة ومحادثات شراكة اقتصادية شاملة، وفق المجلس الأوروبي للعلاقات.",
             "50,000", "وظائف متوقعة",
             [("القيادة", "تركيا"), ("الإطار", "شراكة CEPA"), ("السياق", "ما بعد الأسد")],
             "ECFR / TURKISH MINUTE • 2026"),
    ],
    "sources": [
        {"name": "Atlantic Council", "domain": "atlanticcouncil.org"},
        {"name": "Daily Sabah", "domain": "dailysabah.com"},
        {"name": "Turkish Minute", "domain": "turkishminute.com"},
        {"name": "ECFR", "domain": "ecfr.eu"},
    ],
    "arabicTicker": [
        "دمشق توقّع اتفاق طاقة بـ7 مليارات دولار في 29 مايو",
        "الاتفاق يضيف 4000 ميغاواط غاز و1000 شمسية",
        "إنتاج متوقع 35 مليار كيلوواط ساعة سنوياً",
        "محطات في حمص وحماة ودير الزور وجنوب سوريا",
        "تركيا تقود إعمار سوريا بعد سقوط الأسد بنحو 50 ألف وظيفة",
    ],
}

# ───────────────────────── 6. nasa-moonbase (wildcard, B) ─────────────────────────
s = "nasa-moonbase"
SLATE[s] = {
    "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": "@photonect.news",
    "audioBed": "audio/music_01.mp3", "topicBucket": "wildcard", "variant": "B",
    "breaking": {
        "arabicKicker": "عودة إلى القمر",
        "arabicHeadline": "ناسا تكشف أول قاعدة قمرية بتمويل خاص",
        "englishSubhead": "NASA UNVEILS MOON BASE I • FIRST PRIVATELY FUNDED LUNAR LANDER • BLUE ORIGIN MK1 • FALL 2026",
        "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
    },
    "beats": [
        beat(s, 0, "الإعلان", "إيزاكمان يعلن قاعدة القمر الأولى",
             "أعلن مدير ناسا جاريد إيزاكمان في 26 مايو مشروع قاعدة القمر الأولى، أول مهمة هبوط قمري بتمويل خاص في التاريخ، وفق ناسا.",
             "1st", "مهمة هبوط قمري بتمويل خاص",
             [("المدير", "إيزاكمان"), ("الإعلان", "26 مايو"), ("الأولى", "تمويل خاص")],
             "NASA • MAY 26, 2026"),
        beat(s, 1, "المركبة", "بلو أوريجن تهبط عند قطب القمر الجنوبي",
             "تحمل مركبة بلو أوريجن مارك 1 إنديورانس حمولتين لناسا إلى حافة شاكلتون قرب القطب الجنوبي للقمر، وفق سبيس فلايت ناو.",
             "Mk1", "مركبة بلو أوريجن إنديورانس",
             [("الموقع", "قطب جنوبي"), ("الحمولة", "حمولتا ناسا"), ("المركبة", "إنديورانس")],
             "SPACEFLIGHT NOW • 2026"),
        beat(s, 2, "الهدف", "خطوة نحو هبوط البشر مع أرتميس",
             "تستهدف المهمة الإطلاق خريف 2026 لتقليل مخاطر منظومة الهبوط البشري ضمن برنامج أرتميس للعودة إلى القمر، وفق ناسا.",
             "خريف 2026", "موعد الإطلاق المستهدف",
             [("الإطلاق", "خريف 2026"), ("البرنامج", "أرتميس"), ("الحمولات", "SCALPSS + مرايا")],
             "NASA / SPACEFLIGHT NOW • 2026"),
    ],
    "sources": [
        {"name": "NASA", "domain": "nasa.gov"},
        {"name": "Spaceflight Now", "domain": "spaceflightnow.com"},
        {"name": "Blue Origin", "domain": "blueorigin.com"},
    ],
    "arabicTicker": [
        "ناسا تكشف مشروع قاعدة القمر الأولى",
        "أول مهمة هبوط قمري بتمويل خاص في التاريخ",
        "مركبة بلو أوريجن مارك 1 إنديورانس تهبط قرب القطب الجنوبي",
        "المهمة تحمل حمولتين علميتين لناسا إلى حافة شاكلتون",
        "الإطلاق المستهدف خريف 2026 ضمن برنامج أرتميس",
    ],
}


def main():
    for slug, props in SLATE.items():
        d = POSTS / f"{DATE}-{slug}" / ".meta"
        d.mkdir(parents=True, exist_ok=True)
        (d / "props.json").write_text(json.dumps(props, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"  ✓ {DATE}-{slug}: {len(props['beats'])} beats, variant {props['variant']}, bucket {props['topicBucket']}")
    print(f"\n{len(SLATE)} props.json authored for {DATE}")


if __name__ == "__main__":
    main()
