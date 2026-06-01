#!/usr/bin/env python3
"""Author the 6 props.json for the 2026-06-01 Photonect NEWS slate.
V10.1 engine shape (one matched still per beat). Mirrors the proven 2026-05-30
structure exactly. Draft Arabic here; iraqi-copywriter agent polishes after.
"""
import json
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE")
POSTS = ROOT / "data" / "posts"
DATE = "2026-06-01"
DATE_LABEL = "JUN 1 • 2026"
AR_DATE = "1 يونيو 2026"

ACCENTS = ["#FFC217", "#D72638", "#5B8FF9"]


def img(slug, name):
    return f"images/news/{DATE}-{slug}/{name}"


def brolls(slug, lead):
    order = [lead] + [x for x in ["broll_1.jpg", "hero.jpg", "broll_2.jpg", "broll_3.jpg"] if x != lead]
    return [img(slug, x) for x in order[:4]]


def beat(slug, label, heading, body, stat, ss, lead, accent, src):
    return {
        "label": label,
        "arabicHeading": heading,
        "arabicBody": body,
        "bigStat": {"value": stat[0], "label": stat[1], "arabicLabel": stat[1]},
        "supportingStats": [{"label": a, "value": b} for a, b in ss],
        "broll": img(slug, lead),
        "brolls": brolls(slug, lead),
        "brollType": "image",
        "accent": accent,
        "brollSource": src,
    }


SLATE = {
    # 1 — iraq_domestic — A
    "iraq-oil-gas-law": {
        "variant": "A", "bucket": "iraq_domestic",
        "headline": "العراق يقترب من قانون النفط والغاز بعد 20 عاماً",
        "subhead": "IRAQ NEARS LANDMARK OIL & GAS LAW • 20 YEARS STALLED • BAGHDAD–ERBIL DEAL",
        "beats": [
            ("الإطار", "حكومة الزيدي تتصدّر أولوياتها بقانون النفط",
             "تضع حكومة الزيدي قانون النفط والغاز على رأس أولوياتها بعد توافق أغلب الكتل، وفق شفق نيوز والصباح.",
             ("20", "عاماً من التعطيل"),
             [("قوانين مُمررة", "16"), ("الموقف", "توافق الكتل"), ("المصدر", "شفق نيوز")], "broll_1.jpg"),
            ("بغداد وأربيل", "القانون يوحّد الثروة ويعيد عائدات جيهان",
             "يوحّد القانون إدارة الثروة بين بغداد وأربيل ويعيد عائدات تصدير 200 ألف برميل عبر جيهان للخزينة، وفق العربي ويكلي.",
             ("200", "ألف برميل يومياً عبر جيهان"),
             [("الوجهة", "ميناء جيهان"), ("العائدات", "للخزينة"), ("المصدر", "العربي ويكلي")], "broll_2.jpg"),
            ("ماذا بعد", "ثلاثة مسارات أمام التشريع المؤجَّل",
             "أمام القانون قراءة برلمانية مرتقبة، أو تأجيل بفعل خلافات فنية، أو طعن دستوري، وفق رووداو وكردستان24.",
             ("3", "مسارات محتملة"),
             [("الأول", "قراءة وتمرير"), ("الثاني", "تأجيل"), ("الثالث", "طعن دستوري")], "broll_3.jpg"),
        ],
        "sources": [("Shafaq News", "shafaq.com"), ("The Arab Weekly", "thearabweekly.com"),
                    ("Al-Sabah", "alsabaah.iq"), ("Rudaw", "rudaw.net"),
                    ("Kurdistan24", "kurdistan24.net"), ("Argus Media", "argusmedia.com")],
        "ticker": [
            "العراق يقترب من إقرار قانون النفط والغاز بعد 20 عاماً من التعطيل",
            "حكومة الزيدي تضع التشريع على رأس أولوياتها وسط توافق الكتل",
            "البرلمان مرّر 16 قانوناً استراتيجياً حتى الآن",
            "القانون يعيد عائدات تصدير 200 ألف برميل عبر جيهان للخزينة الاتحادية",
            "يوحّد القانون إدارة الثروة بين بغداد وأربيل",
        ],
    },
    # 2 — mena_geopolitics — A
    "redsea-reopens": {
        "variant": "A", "bucket": "mena_geopolitics",
        "headline": "مرسك تعبر البحر الأحمر لأول مرة منذ عامين",
        "subhead": "MAERSK CROSSES RED SEA FIRST TIME IN 2 YEARS • HOUTHIS HOLD FIRE • OMAN-BROKERED TRUCE",
        "beats": [
            ("الحدث", "سفن مرسك تعود إلى ممر البحر الأحمر",
             "عبرت سفن مرسك البحر الأحمر لأول مرة منذ عامين بعد التزام الحوثيين وقف النار بوساطة عُمانية، وفق تايمز أوف إسرائيل.",
             ("2", "عام منذ آخر عبور"),
             [("الوسيط", "سلطنة عُمان"), ("الهدنة", "6 مايو"), ("المصدر", "تايمز أوف إسرائيل")], "broll_1.jpg"),
            ("لماذا يهم", "باب المندب شريان 12% من التجارة",
             "يمر عبر باب المندب نحو 12% من التجارة العالمية، وعودة الملاحة تخفض أجور الشحن وتختصر مسار رأس الرجاء، وفق مجلس العلاقات الخارجية.",
             ("12%", "من التجارة العالمية"),
             [("المسار البديل", "+10 أيام"), ("التأثير", "خفض أجور الشحن"), ("المصدر", "CFR")], "broll_2.jpg"),
            ("ماذا بعد", "هدنة دائمة أم خرق جديد",
             "أمام الممر هدنة دائمة، أو خرق جديد يعيد التحويل حول إفريقيا، أو عودة جزئية حذرة، وفق ماريتايم إكزكتف وACLED.",
             ("3", "سيناريوهات للملاحة"),
             [("الأول", "هدنة دائمة"), ("الثاني", "خرق جديد"), ("الثالث", "عودة جزئية")], "broll_3.jpg"),
        ],
        "sources": [("The National", "thenationalnews.com"), ("Times of Israel", "timesofisrael.com"),
                    ("CFR", "cfr.org"), ("Maritime Executive", "maritime-executive.com"),
                    ("ACLED", "acleddata.com"), ("gCaptain", "gcaptain.com")],
        "ticker": [
            "سفن مرسك تعبر البحر الأحمر لأول مرة منذ عامين",
            "الحوثيون يلتزمون وقف إطلاق النار بوساطة عُمانية منذ 6 مايو",
            "باب المندب ممر نحو 12% من التجارة العالمية",
            "عودة الملاحة تخفض أجور الشحن وتختصر مسار رأس الرجاء الصالح",
            "المسار البديل حول إفريقيا يضيف نحو 10 أيام للرحلة",
        ],
    },
    # 3 — tech_ai — C
    "ai-price-war": {
        "variant": "C", "bucket": "tech_ai",
        "headline": "حرب أسعار تشعل سباق الذكاء الاصطناعي العالمي",
        "subhead": "AI PRICE WAR • GROK 4.3 & DEEPSEEK V4 SLASH FRONTIER COSTS • CHEAPER ARABIC AI",
        "beats": [
            ("الحدث", "Grok 4.3 ينزل بسعر منافس لـDeepSeek",
             "أطلقت xAI نموذج Grok 4.3 في 6 مايو بسعر 1.25 دولار للمليون رمز، منافساً DeepSeek V4، وفق Artificial Analysis.",
             ("$1.25", "للمليون رمز إدخال"),
             [("النافذة", "مليون رمز"), ("المنافس", "DeepSeek V4"), ("المصدر", "Artificial Analysis")], "broll_1.jpg"),
            ("لماذا يهم", "أسعار أرخص تفتح الذكاء بالعربية",
             "انهيار الأسعار يتيح خدمات ذكاء اصطناعي بالعربية أرخص للشركات الناشئة في الخليج والعراق، مع نشر Grok بالسعودية، وفق xAI.",
             ("1M", "نافذة السياق بالرموز"),
             [("السوق", "الخليج والعراق"), ("النشر", "السعودية"), ("المصدر", "xAI")], "broll_2.jpg"),
            ("ماذا بعد", "خفض أعمق أم تركّز أم تنظيم",
             "يتجه السباق إلى خفض أعمق للأسعار، أو تركّز بيد قلة، أو تنظيم حكومي للنماذج، وفق llm-stats وDataCenterDynamics.",
             ("3", "مسارات للسوق"),
             [("الأول", "خفض أعمق"), ("الثاني", "تركّز"), ("الثالث", "تنظيم")], "broll_3.jpg"),
        ],
        "sources": [("Artificial Analysis", "artificialanalysis.ai"), ("xAI", "x.ai"),
                    ("llm-stats", "llm-stats.com"), ("DataCenterDynamics", "datacenterdynamics.com"),
                    ("Bloomberg", "bloomberg.com"), ("InfoWorld", "infoworld.com")],
        "ticker": [
            "حرب أسعار تشتعل في سوق نماذج الذكاء الاصطناعي",
            "xAI تطلق Grok 4.3 بسعر 1.25 دولار للمليون رمز",
            "DeepSeek V4 ينافس بقوة على الأداء والسعر",
            "أسعار أرخص تفتح خدمات الذكاء الاصطناعي بالعربية للشركات الناشئة",
            "نافذة سياق تبلغ مليون رمز في النماذج الجديدة",
        ],
    },
    # 4 — gulf_regional — B
    "qatar-lng-expansion": {
        "variant": "B", "bucket": "gulf_regional",
        "headline": "قطر تمضي بتوسعة حقل الشمال بـ29 مليار دولار",
        "subhead": "QATAR PUSHES $29B NORTH FIELD LNG EXPANSION • FIRST OUTPUT MID-2026 • US OVERSEAS DEAL",
        "beats": [
            ("الحدث", "قطر للطاقة تمضي بتوسعة حقل الشمال",
             "تمضي قطر للطاقة بتوسعة حقل الشمال بـ29 مليار دولار وتبدأ الإنتاج منتصف 2026، رغم اضطراب الغاز، وفق يورونيوز.",
             ("$29B", "استثمار التوسعة"),
             [("بدء الإنتاج", "منتصف 2026"), ("الحقل", "الشمال"), ("المصدر", "يورونيوز")], "broll_1.jpg"),
            ("لماذا يهم", "رفع الطاقة إلى 142 مليون طن سنوياً",
             "ترفع التوسعة طاقة قطر للغاز المسال نحو 142 مليون طن سنوياً بحلول 2030، مع منح أميركي للتصدير الخارجي، وفق AGBI.",
             ("142", "مليون طن مسال سنوياً"),
             [("الحالي", "77 مليون طن"), ("الهدف", "2030"), ("المصدر", "AGBI")], "broll_2.jpg"),
            ("ماذا بعد", "ريادة مستمرة أم منافسة أم فائض",
             "أمام قطر ترسيخ الريادة العالمية، أو منافسة أميركية متصاعدة، أو فائض معروض يضغط الأسعار، وفق المصادر القطرية والأميركية.",
             ("3", "مسارات للسوق"),
             [("الأول", "ريادة"), ("الثاني", "منافسة"), ("الثالث", "فائض")], "broll_3.jpg"),
        ],
        "sources": [("Euronews", "euronews.com"), ("AGBI", "agbi.com"),
                    ("The Middle East Insider", "themiddleeastinsider.com"), ("QatarEnergy", "qatarenergy.qa"),
                    ("Reuters", "reuters.com"), ("Offshore Energy", "offshore-energy.biz")],
        "ticker": [
            "قطر تمضي بتوسعة حقل الشمال بـ29 مليار دولار",
            "بدء الإنتاج من التوسعة منتصف 2026 رغم اضطراب سوق الغاز",
            "التوسعة ترفع طاقة الغاز المسال نحو 142 مليون طن سنوياً بحلول 2030",
            "الطاقة الحالية نحو 77 مليون طن سنوياً",
            "منح أميركي يفتح لقطر باب التصدير الخارجي للغاز المسال",
        ],
    },
    # 5 — europe — B
    "ecb-rate-hike": {
        "variant": "B", "bucket": "europe",
        "headline": "المركزي الأوروبي يقترب من رفع الفائدة بصدمة النفط",
        "subhead": "ECB NEARS JUNE 11 RATE HIKE • IRAN OIL SHOCK • LAGARDE TO RAISE INFLATION OUTLOOK",
        "beats": [
            ("الحدث", "لاغارد تمهّد لرفع الفائدة في 11 يونيو",
             "تمهّد كريستين لاغارد لرفع الفائدة في 11 يونيو ورفع توقعات التضخم بعد قفزة أسعار النفط، وفق بلومبرغ.",
             ("11", "يونيو موعد القرار"),
             [("التضخم المتوقع", "2.6%"), ("الميل", "رفع ربع نقطة"), ("المصدر", "بلومبرغ")], "broll_1.jpg"),
            ("لماذا يهم", "إغلاق هرمز يدفع برنت والتضخم",
             "إغلاق مضيق هرمز رفع برنت إلى 117 دولاراً في أبريل فدفع التضخم الأوروبي صعوداً، وفق البنك الدولي.",
             ("$117", "سعر برنت في أبريل"),
             [("السبب", "حرب إيران"), ("هرمز", "20% من النفط"), ("المصدر", "البنك الدولي")], "broll_2.jpg"),
            ("ماذا بعد", "رفع أم تثبيت أم خطر ركود",
             "أمام المركزي رفع ربع نقطة، أو تثبيت إن حلّ سلام أميركي إيراني، أو خطر ركود، وفق CNBC ورويترز.",
             ("3", "مسارات للقرار"),
             [("الأول", "رفع ربع نقطة"), ("الثاني", "تثبيت"), ("الثالث", "ركود")], "broll_3.jpg"),
        ],
        "sources": [("Bloomberg", "bloomberg.com"), ("ECB", "ecb.europa.eu"),
                    ("CNBC", "cnbc.com"), ("World Bank", "worldbank.org"),
                    ("Reuters", "reuters.com"), ("Equiti", "equiti.com")],
        "ticker": [
            "المركزي الأوروبي يقترب من رفع الفائدة في 11 يونيو",
            "لاغارد تمهّد لرفع توقعات التضخم بفعل صدمة أسعار النفط",
            "إغلاق مضيق هرمز رفع برنت إلى 117 دولاراً في أبريل",
            "هرمز ممر نحو 20% من إمدادات النفط العالمية",
            "الأسواق تسعّر رفعاً بربع نقطة في اجتماع يونيو",
        ],
    },
    # 6 — wildcard — C
    "white-hydrogen": {
        "variant": "C", "bucket": "wildcard",
        "headline": "اكتشاف هيدروجين طبيعي ضخم بصخور كندا القديمة",
        "subhead": "MASSIVE NATURAL 'WHITE' HYDROGEN FOUND IN BILLION-YEAR-OLD CANADIAN ROCK • PNAS STUDY",
        "beats": [
            ("الاكتشاف", "تسرّب 140 طن هيدروجين سنوياً بأونتاريو",
             "رصد علماء تسرّب 140 طناً من الهيدروجين سنوياً من منجم في أونتاريو، في دراسة نشرتها PNAS، وفق ساينس ديلي.",
             ("140", "طن هيدروجين سنوياً"),
             [("الموقع", "أونتاريو"), ("الدراسة", "PNAS"), ("المصدر", "ساينس ديلي")], "broll_1.jpg"),
            ("لماذا يهم", "وقود نظيف يهدد خريطة النفط",
             "الهيدروجين الأبيض وقود نظيف قد يعيد رسم خريطة الطاقة التي تعتمد عليها دول النفط كالعراق والخليج، وفق جامعة تورنتو.",
             ("400", "منزل يمكن تشغيله سنوياً"),
             [("الطاقة", "4.7 مليون ك.و.س"), ("النوع", "هيدروجين أبيض"), ("المصدر", "جامعة تورنتو")], "broll_2.jpg"),
            ("ماذا بعد", "تطوير تجاري أم عقبات أم سباق",
             "أمام الاكتشاف تطوير تجاري واعد، أو عقبات اقتصادية، أو سباق تنقيب عالمي على الهيدروجين الطبيعي، وفق Phys.org.",
             ("3", "مسارات للطاقة"),
             [("الأول", "تطوير تجاري"), ("الثاني", "عقبات"), ("الثالث", "سباق تنقيب")], "broll_3.jpg"),
        ],
        "sources": [("PNAS", "pnas.org"), ("ScienceDaily", "sciencedaily.com"),
                    ("Phys.org", "phys.org"), ("University of Toronto", "utoronto.ca"),
                    ("Nature World News", "natureworldnews.com"), ("Interesting Engineering", "interestingengineering.com")],
        "ticker": [
            "اكتشاف مصدر ضخم للهيدروجين الطبيعي بصخور كندا القديمة",
            "تسرّب 140 طناً من الهيدروجين سنوياً من منجم في أونتاريو",
            "دراسة في PNAS ترصد هيدروجين أبيض في الدرع الكندي",
            "الموقع قد يولّد طاقة تكفي أكثر من 400 منزل سنوياً",
            "الهيدروجين الأبيض وقود نظيف قد يعيد رسم خريطة الطاقة",
        ],
    },
}


def build(slug_key, d):
    sl = f"{DATE}-{slug_key}"
    beats = []
    for i, (label, heading, body, stat, ss, lead) in enumerate(d["beats"]):
        beats.append(beat(slug_key, label, heading, body, stat, ss, lead, ACCENTS[i],
                          f"{d['sources'][0][0].upper()} • {DATE}"))
    return {
        "dateLabel": DATE_LABEL,
        "arabicDateLabel": AR_DATE,
        "handle": "@photonect.news",
        "audioBed": "audio/news_bed.mp3",
        "topicBucket": d["bucket"],
        "variant": d["variant"],
        "breaking": {
            "arabicKicker": "عاجل",
            "arabicHeadline": d["headline"],
            "englishSubhead": d["subhead"],
            "heroMedia": img(slug_key, "hero.jpg"),
            "heroMediaType": "image",
        },
        "beats": beats,
        "sources": [{"name": n, "domain": dom} for n, dom in d["sources"]],
        "arabicTicker": d["ticker"],
    }


def main():
    for slug_key, d in SLATE.items():
        sl = f"{DATE}-{slug_key}"
        meta = POSTS / sl / ".meta"
        meta.mkdir(parents=True, exist_ok=True)
        props = build(slug_key, d)
        (meta / "props.json").write_text(json.dumps(props, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"  ✓ {sl}  variant={d['variant']} bucket={d['bucket']} beats={len(props['beats'])}")
    print(f"\nauthored {len(SLATE)} props.json")


if __name__ == "__main__":
    main()
