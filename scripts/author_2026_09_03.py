#!/usr/bin/env python3
"""Author the 2026-09-03 slate: 5 slugs, props.json + caption.txt + 4 v11 briefs.

Pillar mix: P1 x4 (oil exports, dollar, petrol, gold), P2 x1 (Basra-Khuzestan rail).
No P3 shipped today. The only same-day science/health/sport candidates that surfaced
were the World Cup 2026 group draw (qualification was April 2026 - months stale) and
generic regional-heat forecasts. Neither is a <24h structural development, so forcing
one would have broken the editorial mandate; the slot went to a fifth verified story.

Posting order is alphabetical by slug -> a 18:00, b 19:45, c 21:15, d 22:30, e 23:45.

Slug C (Baghdad petrol queues) is the silent V10.1 control: it is the only story on
the slate with NO published figure of any kind, which is the same criterion used to
pick the control on 09-01 and 09-02.

*** SOURCING DEVIATION ON SLUG C - see DELIVERY ***
Every other slug carries >=2 named sources. Slug C has ONE: Shafaq News correspondents,
reporting their own on-the-ground observation with photographs. NO official body issued
any explanation today. Ministry of Oil statements found in search (spokesman Salim
al-Rekabi; the FCC-unit withdrawal; "shipments arrive next week") all belong to the
JUNE 3 and AUGUST 20 crises - distinct earlier events - and are deliberately NOT used.
The reel therefore reports only what the correspondents observed and states on-screen
that no official explanation has been issued.

EVERY figure below is transcribed from a dated article fetched on 2026-09-03.
Derived figures are labelled (محتسب) and compare like for like:
  * dollar -> bourse vs bourse, shop-sell vs shop-sell, gap measured inside one article
  * gold   -> wholesale-sell vs wholesale-sell; the retail figure stays a RANGE
  * oil    -> Shafaq/Marsoumi figures only. attaqa's 2.16m bpd is SEABORNE-only and is
              cited for direction (third straight monthly rise), never mixed as a number.
voText spells all numbers as Arabic words: the V11 VO has no numeral normaliser.
No Persian yeh/kaf anywhere (guard: U+06CC / U+06A9).
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE")
POSTS = ROOT / "data" / "posts"
D = "2026-09-03"
DATE_LABEL = "SEP 03 • 2026"
AR_DATE = "3 أيلول 2026"
HANDLE = "@photonect.news"

ACC = ["#FFC217", "#4CC9F0", "#D72638"]


def img(slug: str, name: str) -> str:
    return f"images/news/{slug}/{name}"


def beat(label, heading, body, stat_v, stat_en, stat_ar, pills, slug, broll, accent, phrases):
    return {
        "label": label,
        "arabicHeading": heading,
        "arabicBody": body,
        "bigStat": {"value": stat_v, "label": stat_en, "arabicLabel": stat_ar},
        "supportingStats": [{"label": l, "value": v} for l, v in pills],
        "broll": img(slug, broll),
        "brolls": [img(slug, broll)],
        "brollType": "image",
        "accent": accent,
        "brollSource": "صورة توضيحية · Photonect AI",
        "subtitlePhrases": phrases,
    }



def _validate(slug: str, props: dict) -> None:
    """Guard the schema mistakes that only surface at render time.

    `sources` MUST be a list of {name, domain} dicts: NewsReel/scenes/Sources.tsx
    calls sources.map(), so a bare string throws `sources.map is not a function`
    at ~frame 1450 and kills the whole slug. V11 slugs never draw that scene, so
    the bug hides until a slug renders V10.1 (or a V11 slug falls back) — which is
    exactly how it took down the 2026-09-03 control on the first run.
    """
    src = props.get("sources")
    if not isinstance(src, list) or not all(
        isinstance(x, dict) and {"name", "domain"} <= set(x) for x in src
    ):
        raise SystemExit(
            f"{slug}: props['sources'] must be a list of {{name, domain}} dicts, "
            f"got {type(src).__name__} -> Sources.tsx will throw at render time"
        )

SLATE: dict[str, dict] = {}

# ─────────────────────────────────────────────────────────────────────────────
# A · P1 · صادرات النفط تستعيد 71% — بخصم 25-30 دولاراً للبرميل · 18:00 LEAD
# Source: شفق نيوز 2026-09-02 15:16Z, نقلاً عن الخبير الاقتصادي نبيل المرسومي
#         + وحدة أبحاث الطاقة (attaqa 2026-09-02) للاتجاه فقط
# ─────────────────────────────────────────────────────────────────────────────
s = f"{D}-a-oil-exports-71-percent"
SLATE[s] = {
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/mood_newsroom.mp3", "topicBucket": "iraq_money", "variant": "A",
        "breaking": {
            "arabicKicker": "نفط",
            "arabicHeadline": "رجعنا نصدّر.. بخصم 25 دولاراً للبرميل",
            "englishSubhead": "IRAQ'S CRUDE EXPORTS RECOVERED TO 71% OF PRE-WAR LEVELS IN AUGUST 2026 AT 2.34 MILLION BPD, UP FROM 1.35 MILLION IN JULY | ECONOMIST NABIL AL-MARSOUMI SAYS SOMO BOUGHT THE RECOVERY WITH PRICE DISCOUNTS OF $25-$30 A BARREL | SHAFAQ NEWS, TUE 2 SEP",
            "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
        },
        "beats": [
            beat("ماذا يحدث؟",
                 "2.34 مليون برميل يومياً في آب",
                 "صادرات العراق النفطية بلغت 2.34 مليون برميل يومياً في آب، مقابل 1.35 مليون في تموز، أي 71% من مستواها قبل الحرب (شفق نيوز · الخبير نبيل المرسومي · 2 أيلول 2026).",
                 "71%", "Share of pre-war export levels Iraq recovered in August 2026",
                 "من مستوى الصادرات قبل الحرب استعادها العراق في آب 2026، بواقع 2.34 مليون برميل يومياً مقابل 1.35 مليون في تموز (شفق نيوز · نبيل المرسومي · 2 أيلول 2026)",
                 [("آب", "2.34 م ب/ي"), ("تموز", "1.35 م ب/ي"), ("الفرق", "+990 ألف")],
                 s, "broll_1.jpg", ACC[0],
                 ["صادرات العراق النفطية بلغت 2.34 مليون برميل يومياً في آب",
                  "مقابل 1.35 مليون برميل في تموز",
                  "أي 71% من مستواها قبل الحرب"]),
            beat("لماذا يهم؟",
                 "الخصم هو ثمن العودة",
                 "المرسومي يعزو التعافي إلى تكيّف سومو مع أزمة المضيق عبر سياسات الخصومات السعرية، بخصم يتراوح بين 25 و30 دولاراً للبرميل (شفق نيوز · 2 أيلول 2026).",
                 "$25-30", "Per-barrel price discount SOMO used to keep buyers, per economist Nabil al-Marsoumi",
                 "دولاراً للبرميل هو مدى الخصم السعري الذي تستخدمه سومو للحفاظ على المشترين، بحسب الخبير الاقتصادي نبيل المرسومي (شفق نيوز · 2 أيلول 2026)",
                 [("الخصم", "25-30 $"), ("الجهة", "سومو"), ("السبب", "أزمة المضيق")],
                 s, "broll_2.jpg", ACC[1],
                 ["المرسومي يعزو التعافي إلى تكيّف سومو",
                  "عبر سياسات الخصومات السعرية",
                  "بخصم بين 25 و30 دولاراً للبرميل"]),
            beat("الرقم الأهم",
                 "الكلفة تاكل من العائد",
                 "كلفة الشحن والتأمين تُقدَّر بنحو 17 دولاراً للبرميل، ما يترك هامش ربح بحدود 10 دولارات للبرميل بحسب التقدير نفسه (شفق نيوز · 2 أيلول 2026).",
                 "$10", "Estimated margin left per barrel after roughly $17 of shipping and insurance",
                 "دولارات هامش الربح التقديري للبرميل بعد نحو 17 دولاراً كلفة شحن وتأمين، بحسب التقدير المنشور (شفق نيوز · 2 أيلول 2026)",
                 [("شحن وتأمين", "~17 $"), ("الهامش", "~10 $"), ("للبرميل", "تقدير")],
                 s, "broll_3.jpg", ACC[2],
                 ["كلفة الشحن والتأمين نحو 17 دولاراً للبرميل",
                  "ما يترك هامش ربح بحدود 10 دولارات",
                  "بحسب التقدير المنشور"]),
        ],
        "arabicTicker": "صادرات النفط 2.34 مليون ب/ي في آب · 71% من مستوى ما قبل الحرب · خصم 25-30 دولاراً للبرميل · المصدر شفق نيوز",
        "endQuestion": "تتوقع رواتب الدولة تنمشي بموعدها هالسنة؟ إي لو لا؟",
        "sources": "شفق نيوز · نبيل المرسومي · وحدة أبحاث الطاقة",
    },
    "brief": {
        "slug": s,
        "kicker": "نفط",
        "hookHeadline": "نصدّر أكثر.. بخصم للبرميل",
        "voText": "استعادت صادرات العراق النفطية واحداً وسبعين بالمئة من مستواها قبل الحرب خلال آب، إذ بلغت مليونين وثلاثمئة وأربعين ألف برميل يومياً، مقابل مليون وثلاثمئة وخمسين ألفاً في تموز، بحسب شفق نيوز نقلاً عن الخبير الاقتصادي نبيل المرسومي. ويعزو المرسومي هذا التعافي إلى تكيّف سومو مع أزمة المضيق عبر سياسات الخصومات السعرية، بخصم يتراوح بين خمسة وعشرين وثلاثين دولاراً للبرميل. وتُقدَّر كلفة الشحن والتأمين بنحو سبعة عشر دولاراً للبرميل، ما يترك هامش ربح بحدود عشرة دولارات. تتوقع رواتب الدولة تنمشي بموعدها هالسنة؟",
        "endQuestion": "تتوقع رواتب الدولة تنمشي بموعدها هالسنة؟",
        "sourcesLine": "المصادر: شفق نيوز · نبيل المرسومي · وحدة أبحاث الطاقة",
        "images": [img(s, "hero.jpg"), img(s, "broll_1.jpg"), img(s, "broll_2.jpg"), img(s, "broll_3.jpg")],
        "audioBed": "audio/mood_newsroom.mp3",
        "statPops": [
            {"value": "71%", "label": "من مستوى الصادرات قبل الحرب", "matchWord": "وسبعين"},
            {"value": "$25-30", "label": "الخصم السعري للبرميل", "matchWord": "الخصومات"},
        ],
    },
    "caption": """صادرات النفط العراقية اليوم — رجعنا نصدّر، بس بأي سعر؟

الكمية تعافت، والخصم اللي دفعناه مقابلها هو القصة الحقيقية.

تتوقع رواتب الدولة تنمشي بموعدها هالسنة؟

المصادر: شفق نيوز، وحدة أبحاث الطاقة
#العراق #النفط #اقتصاد_العراق #صادرات_النفط #photonectnews
@photonect.news""",
}

# ─────────────────────────────────────────────────────────────────────────────
# B · P1 · الدولار — البورصة صعدت وسعر المحل ما تحرّك · 19:45 (المرساة اليومية)
# Source: شفق نيوز 2026-09-03 07:38Z
# ─────────────────────────────────────────────────────────────────────────────
s = f"{D}-b-dollar-bourse-shops-gap"
SLATE[s] = {
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/mood_cinematic.mp3", "topicBucket": "iraq_money", "variant": "B",
        "breaking": {
            "arabicKicker": "دولار",
            "arabicHeadline": "البورصة صعدت.. وسعر المحل ما تحرّك",
            "englishSubhead": "BAGHDAD'S AL-KIFAH AND AL-HARITHIYA BOURSES OPENED THURSDAY AT 154,650 DINARS PER $100, UP FROM 154,400 ON WEDNESDAY | EXCHANGE-SHOP SELLING PRICE HELD FLAT AT 155,000 | THE SHOP-OVER-BOURSE GAP NARROWED FROM 600 TO 350 DINARS | SHAFAQ NEWS, THU 3 SEP",
            "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
        },
        "beats": [
            beat("ماذا يحدث؟",
                 "البورصة 154,650 للمئة دولار",
                 "سجّلت بورصتا الكفاح والحارثية ببغداد 154,650 ديناراً لكل 100 دولار صباح الخميس، مقابل 154,400 ديناراً يوم الأربعاء (شفق نيوز · 3 أيلول 2026).",
                 "154,650", "Baghdad bourse rate per $100 on Thursday morning, up from 154,400 on Wednesday",
                 "ديناراً لكل 100 دولار سعر بورصتي الكفاح والحارثية صباح الخميس، مقابل 154,400 ديناراً يوم الأربعاء (شفق نيوز · 3 أيلول 2026)",
                 [("اليوم", "154,650"), ("الأربعاء", "154,400"), ("الفرق", "+250")],
                 s, "broll_1.jpg", ACC[0],
                 ["بورصتا الكفاح والحارثية سجّلتا 154,650 ديناراً",
                  "لكل 100 دولار صباح الخميس",
                  "مقابل 154,400 ديناراً يوم الأربعاء"]),
            beat("لماذا يهم؟",
                 "سعر المحل هو اللي تدفعه",
                 "في محال الصيرفة ببغداد استقر سعر البيع عند 155,000 دينار لكل 100 دولار والشراء 154,000، بلا تغيّر عن الأمس (شفق نيوز · 3 أيلول 2026).",
                 "155,000", "Baghdad exchange-shop selling price per $100 — unchanged from Wednesday",
                 "دينار سعر البيع في محال الصيرفة ببغداد لكل 100 دولار، مستقراً بلا تغيّر عن يوم الأربعاء (شفق نيوز · 3 أيلول 2026)",
                 [("بيع المحال", "155,000"), ("شراء المحال", "154,000"), ("التغيّر", "مستقر")],
                 s, "broll_2.jpg", ACC[1],
                 ["في محال الصيرفة ببغداد استقر سعر البيع",
                  "عند 155,000 دينار لكل 100 دولار",
                  "والشراء 154,000 بلا تغيّر"]),
            beat("الرقم الأهم",
                 "الفجوة ضاقت 250 ديناراً",
                 "الفارق بين بيع المحال وسعر البورصة نزل من 600 دينار يوم الأربعاء إلى 350 ديناراً اليوم (محتسب من أرقام شفق نيوز · بيع محال مقابل بورصة).",
                 "350", "Dinars between the Baghdad shop selling price and the bourse today, down from 600 on Wednesday",
                 "ديناراً الفارق بين بيع محال الصيرفة وسعر البورصة اليوم، نزولاً من 600 دينار يوم الأربعاء (محتسب من أرقام شفق نيوز · بيع محال مقابل بورصة)",
                 [("اليوم", "350"), ("الأربعاء", "600"), ("أربيل بيع", "154,600")],
                 s, "broll_3.jpg", ACC[2],
                 ["الفارق بين بيع المحال وسعر البورصة",
                  "نزل من 600 دينار يوم الأربعاء",
                  "إلى 350 ديناراً اليوم"]),
        ],
        "arabicTicker": "البورصة 154,650 · بيع المحال 155,000 مستقر · الفجوة 350 ديناراً بعد 600 · أربيل بيع 154,600 · المصدر شفق نيوز",
        "endQuestion": "شريت دولار اليوم؟ بشكد انطوك بالمحل؟",
        "sources": "شفق نيوز · بورصتا الكفاح والحارثية",
    },
    "brief": {
        "slug": s,
        "kicker": "دولار",
        "hookHeadline": "البورصة صعدت والمحل ما تحرّك",
        "voText": "سجّلت بورصتا الكفاح والحارثية ببغداد مئة وأربعة وخمسين ألفاً وستمئة وخمسين ديناراً لكل مئة دولار صباح الخميس، مقابل مئة وأربعة وخمسين ألفاً وأربعمئة دينار يوم الأربعاء، بحسب شفق نيوز. لكن سعر المحل هو ما يدفعه المواطن، وفي محال الصيرفة ببغداد استقر البيع عند مئة وخمسة وخمسين ألف دينار والشراء عند مئة وأربعة وخمسين ألفاً، بلا تغيّر. وفي أربيل استقر البيع عند مئة وأربعة وخمسين ألفاً وستمئة دينار. أي أن الفارق بين بيع المحال والبورصة ضاق من ستمئة دينار إلى ثلاثمئة وخمسين، محتسب. شريت دولار اليوم؟",
        "endQuestion": "شريت دولار اليوم؟ بشكد انطوك بالمحل؟",
        "sourcesLine": "المصادر: شفق نيوز · بورصتا الكفاح والحارثية",
        "images": [img(s, "hero.jpg"), img(s, "broll_1.jpg"), img(s, "broll_2.jpg"), img(s, "broll_3.jpg")],
        "audioBed": "audio/mood_cinematic.mp3",
        "statPops": [
            {"value": "154,650", "label": "سعر البورصة لكل 100 دولار", "matchWord": "الكفاح"},
            {"value": "155,000", "label": "بيع محال الصيرفة ببغداد", "matchWord": "الصيرفة"},
        ],
    },
    "caption": """سعر الدولار في العراق اليوم — ليش المحل ما نزّل سعره؟

البورصة تحركت والمحل لا، والفجوة بيناتهم هي القصة.

شريت دولار اليوم؟ بشكد انطوك بالمحل؟

المصادر: شفق نيوز
#العراق #الدولار #سعر_الصرف #اقتصاد_العراق #photonectnews
@photonect.news""",
}

# ─────────────────────────────────────────────────────────────────────────────
# C · P1 · طوابير البنزين ترجع لبغداد · 21:15 · V10.1 CONTROL (silent, no brief)
# Source: شفق نيوز 2026-09-03 10:51Z — مراسلو الوكالة وصورهم. مصدر واحد فقط.
# لا تفسير رسمي صدر اليوم. تصريحات وزارة النفط المتداولة تعود لأزمتَي حزيران وآب.
# ─────────────────────────────────────────────────────────────────────────────
s = f"{D}-c-petrol-queues-baghdad"
SLATE[s] = {
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/music_03.mp3", "topicBucket": "iraq_services", "variant": "C",
        "breaking": {
            "arabicKicker": "بنزين",
            "arabicHeadline": "طوابير البنزين ترجع لبغداد بلا تفسير",
            "englishSubhead": "SHAFAQ NEWS CORRESPONDENTS DOCUMENTED DOZENS OF CLOSED PETROL STATIONS AND LONG QUEUES ACROSS BAGHDAD ON THURSDAY, ABOUT 15 DAYS AFTER THE PREVIOUS SHORTAGE ENDED | NO OFFICIAL EXPLANATION HAS BEEN ISSUED | SINGLE-SOURCE EYEWITNESS REPORT, THU 3 SEP",
            "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
        },
        "beats": [
            beat("ماذا يحدث؟",
                 "محطات مغلقة وطوابير تسدّ الشوارع",
                 "وثّق مراسلو شفق نيوز يوم الخميس إغلاق عشرات محطات الوقود ببغداد وطوابير طويلة أمام العاملة منها، عرقلت السير في عدة مناطق (شفق نيوز · 3 أيلول 2026).",
                 "عشرات", "Petrol stations documented closed across Baghdad on Thursday by Shafaq News correspondents",
                 "من محطات الوقود ببغداد وثّق مراسلو شفق نيوز إغلاقها يوم الخميس، مع طوابير طويلة أمام المحطات العاملة عرقلت السير (شفق نيوز · 3 أيلول 2026)",
                 [("المدينة", "بغداد"), ("اليوم", "الخميس"), ("التوثيق", "مراسلون وصور")],
                 s, "broll_1.jpg", ACC[0],
                 ["مراسلو شفق نيوز وثّقوا يوم الخميس",
                  "إغلاق عشرات محطات الوقود ببغداد",
                  "وطوابير طويلة عرقلت السير"]),
            beat("لماذا يهم؟",
                 "بعد 15 يوماً من أزمة انتهت",
                 "الأزمة تعود بعد نحو 15 يوماً من انتهاء أزمة سابقة، ما يجدّد القلق من تكرار اضطراب توزيع الوقود في فترات قصيرة (شفق نيوز · 3 أيلول 2026).",
                 "15", "Days between the end of the previous shortage and Thursday's return of queues",
                 "يوماً تقريباً هي المدة بين انتهاء الأزمة السابقة وعودة الطوابير يوم الخميس، ما يجدّد القلق من تكرار الاضطراب (شفق نيوز · 3 أيلول 2026)",
                 [("الفاصل", "~15 يوماً"), ("التكرار", "الثانية"), ("النطاق", "بغداد ومحافظات")],
                 s, "broll_2.jpg", ACC[1],
                 ["الأزمة تعود بعد نحو 15 يوماً",
                  "من انتهاء أزمة سابقة",
                  "ما يجدّد القلق من تكرار الاضطراب"]),
            beat("ما الغائب؟",
                 "ولا تفسير رسمي لحد الآن",
                 "حتى ساعة النشر لم تصدر أي جهة رسمية توضيحاً لأسباب الإغلاق ولا للإجراءات المتخذة، والسائقون يسألون بلا جواب (شفق نيوز · 3 أيلول 2026).",
                 "0", "Official explanations issued for the closures as of publication",
                 "توضيحات رسمية صدرت حتى ساعة النشر بشأن أسباب إغلاق المحطات أو الإجراءات المتخذة، والسائقون يسألون بلا جواب (شفق نيوز · 3 أيلول 2026)",
                 [("تفسير رسمي", "لم يصدر"), ("الأسباب", "غير معلنة"), ("المصدر", "شفق نيوز")],
                 s, "broll_3.jpg", ACC[2],
                 ["حتى ساعة النشر لم تصدر أي جهة رسمية",
                  "توضيحاً لأسباب الإغلاق",
                  "ولا للإجراءات المتخذة"]),
        ],
        "arabicTicker": "عشرات محطات الوقود مغلقة ببغداد · طوابير تعرقل السير · بعد 15 يوماً من أزمة سابقة · لا تفسير رسمي · المصدر شفق نيوز",
        "endQuestion": "شكد انتظرت اليوم بطابور البنزين؟",
        "sources": "شفق نيوز · مراسلو الوكالة",
    },
    "brief": None,  # V10.1 control — silent, no VO
    "caption": """أزمة البنزين في بغداد اليوم — ليش المحطات مغلقة؟

طوابير رجعت بعد أسبوعين بس، وبلا أي توضيح رسمي لحد الآن.

شكد انتظرت اليوم بطابور البنزين؟

المصادر: شفق نيوز
#العراق #بغداد #البنزين #أزمة_الوقود #photonectnews
@photonect.news""",
}

# ─────────────────────────────────────────────────────────────────────────────
# D · P1 · الذهب — المثقال يقفز 25 ألف دينار بجلسة · 22:30
# Source: شفق نيوز 2026-09-03 09:04Z
# ─────────────────────────────────────────────────────────────────────────────
s = f"{D}-d-gold-jumps-25-thousand"
SLATE[s] = {
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/music_05.mp3", "topicBucket": "iraq_money", "variant": "A",
        "breaking": {
            "arabicKicker": "ذهب",
            "arabicHeadline": "المثقال قفز 25 ألف دينار بيوم واحد",
            "englishSubhead": "BAGHDAD WHOLESALE 21-CARAT GULF MITHQAL SOLD AT 970,000 DINARS THURSDAY AGAINST 945,000 ON WEDNESDAY, A 25,000 RISE WHOLESALE-TO-WHOLESALE | ERBIL 22-CARAT CROSSED ONE MILLION AT 1,004,000 | SHAFAQ NEWS, THU 3 SEP",
            "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
        },
        "beats": [
            beat("ماذا يحدث؟",
                 "970 ألفاً للمثقال بجملة بغداد",
                 "في أسواق الجملة بشارع النهر ببغداد سجّل بيع مثقال الذهب الخليجي عيار 21 نحو 970,000 دينار وشراؤه 966,000، مقابل 945,000 يوم الأربعاء (شفق نيوز · 3 أيلول 2026).",
                 "+25,000", "Dinar rise in the Baghdad wholesale 21-carat Gulf mithqal in one session, wholesale against wholesale",
                 "ديناراً ارتفاع بيع مثقال الذهب الخليجي عيار 21 في جملة بغداد خلال جلسة واحدة، من 945,000 إلى 970,000 (جملة مقابل جملة · شفق نيوز · 3 أيلول 2026)",
                 [("بيع الجملة", "970,000"), ("أمس", "945,000"), ("شراء", "966,000")],
                 s, "broll_1.jpg", ACC[0],
                 ["في جملة بغداد بيع مثقال الذهب الخليجي عيار 21",
                  "بنحو 970 ألف دينار وشراؤه 966 ألفاً",
                  "مقابل 945 ألفاً يوم الأربعاء"]),
            beat("لماذا يهم؟",
                 "سعر الصاغة نطاق مو رقم واحد",
                 "في محال الصاغة تراوح بيع مثقال الخليجي عيار 21 بين 975,000 و980,000 دينار، والعراقي بين 940,000 و950,000 (شفق نيوز · 3 أيلول 2026).",
                 "975-980", "Thousand-dinar range asked in Baghdad retail jewellery shops for a 21-carat Gulf mithqal",
                 "ألف دينار هو النطاق المطلوب في محال الصاغة ببغداد لمثقال الذهب الخليجي عيار 21، والعراقي بين 940 و950 ألفاً (شفق نيوز · 3 أيلول 2026)",
                 [("صاغة خليجي", "975-980 ألف"), ("صاغة عراقي", "940-950 ألف"), ("جملة عراقي", "940,000")],
                 s, "broll_2.jpg", ACC[1],
                 ["في محال الصاغة تراوح بيع المثقال الخليجي",
                  "بين 975 و980 ألف دينار",
                  "والعراقي بين 940 و950 ألفاً"]),
            beat("الرقم الأهم",
                 "بأربيل عيار 22 عبر المليون",
                 "في أربيل سجّل عيار 22 نحو 1,004,000 دينار للمثقال، وعيار 21 عند 960,000، وعيار 18 عند 822,000 (شفق نيوز · 3 أيلول 2026).",
                 "1,004,000", "Dinars for a 22-carat mithqal in Erbil — above the one-million mark",
                 "دينار سعر مثقال عيار 22 في أربيل، متجاوزاً حاجز المليون، فيما سجّل عيار 21 نحو 960,000 وعيار 18 نحو 822,000 (شفق نيوز · 3 أيلول 2026)",
                 [("أربيل 22", "1,004,000"), ("أربيل 21", "960,000"), ("أربيل 18", "822,000")],
                 s, "broll_3.jpg", ACC[2],
                 ["في أربيل سجّل عيار 22 نحو مليون وأربعة آلاف دينار",
                  "وعيار 21 عند 960 ألفاً",
                  "وعيار 18 عند 822 ألفاً"]),
        ],
        "arabicTicker": "مثقال الخليجي 21 بجملة بغداد 970,000 بعد 945,000 · الصاغة 975-980 ألفاً · أربيل عيار 22 عند 1,004,000 · المصدر شفق نيوز",
        "endQuestion": "عندك ذهب بالبيت؟ بعته لو محتفظ بيه؟",
        "sources": "شفق نيوز · أسواق الجملة بشارع النهر",
    },
    "brief": {
        "slug": s,
        "kicker": "ذهب",
        "hookHeadline": "المثقال قفز 25 ألفاً بيوم",
        "voText": "ارتفعت أسعار الذهب في بغداد وأربيل صباح الخميس. ففي أسواق الجملة بشارع النهر ببغداد سجّل بيع مثقال الذهب الخليجي عيار واحد وعشرين نحو تسعمئة وسبعين ألف دينار وشراؤه تسعمئة وستة وستين ألفاً، مقابل تسعمئة وخمسة وأربعين ألفاً يوم الأربعاء، بحسب شفق نيوز. أما في محال الصاغة فتراوح البيع بين تسعمئة وخمسة وسبعين وتسعمئة وثمانين ألف دينار، وهو نطاق لا رقم واحد. وفي أربيل تجاوز عيار اثنين وعشرين حاجز المليون عند مليون وأربعة آلاف دينار. عندك ذهب بالبيت؟",
        "endQuestion": "عندك ذهب بالبيت؟ بعته لو محتفظ بيه؟",
        "sourcesLine": "المصادر: شفق نيوز · أسواق الجملة بشارع النهر",
        "images": [img(s, "hero.jpg"), img(s, "broll_1.jpg"), img(s, "broll_2.jpg"), img(s, "broll_3.jpg")],
        "audioBed": "audio/music_05.mp3",
        "statPops": [
            {"value": "970,000", "label": "بيع المثقال الخليجي — جملة بغداد", "matchWord": "النهر"},
            {"value": "1,004,000", "label": "عيار 22 في أربيل", "matchWord": "أربيل"},
        ],
    },
    "caption": """سعر الذهب في بغداد اليوم — المثقال قفز بجلسة وحدة

سعر الجملة وسعر الصاغة مو نفس الرقم، وسعر الصاغة نطاق مو رقم واحد.

عندك ذهب بالبيت؟ بعته لو محتفظ بيه؟

المصادر: شفق نيوز
#العراق #الذهب #سعر_الذهب #اقتصاد_العراق #photonectnews
@photonect.news""",
}

# ─────────────────────────────────────────────────────────────────────────────
# E · P2 · سكة البصرة–خوزستان عند 70% · 23:45
# Source: شفق نيوز 2026-09-03 11:10Z — شمس الدين حسني، رئيس اللجنة الاقتصادية
#         في مجلس الشورى الإيراني
# ─────────────────────────────────────────────────────────────────────────────
s = f"{D}-e-basra-khuzestan-rail"
SLATE[s] = {
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/music_01.mp3", "topicBucket": "mena_geopolitics", "variant": "B",
        "breaking": {
            "arabicKicker": "سكك",
            "arabicHeadline": "سكة البصرة–خوزستان عند 70%",
            "englishSubhead": "IRANIAN SHURA COUNCIL ECONOMIC COMMITTEE HEAD SHAMS AL-DIN HASSANI TOLD SHAFAQ NEWS IN BASRA THE BASRA-KHUZESTAN RAIL LINK IS 70% COMPLETE, WITH 16 KM DEMINED ON THE IRANIAN SIDE | A FREE ZONE AND INDUSTRIAL CENTRE AT SHALAMCHEH ARE STILL PLANS | NO DATE, COST OR FINANCING PUBLISHED | THU 3 SEP",
            "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
        },
        "beats": [
            beat("ماذا يحدث؟",
                 "وفد إيراني بالبصرة: الإنجاز 70%",
                 "قال رئيس اللجنة الاقتصادية في مجلس الشورى الإيراني شمس الدين حسني لشفق نيوز خلال زيارة للبصرة إن الربط السككي مع خوزستان بلغ نسبة إنجاز 70% (شفق نيوز · 3 أيلول 2026).",
                 "70%", "Stated completion rate of the Basra-Khuzestan rail link, per Iranian committee head Shams al-Din Hassani",
                 "نسبة الإنجاز المعلنة للربط السككي بين البصرة وخوزستان، بحسب رئيس اللجنة الاقتصادية في مجلس الشورى الإيراني شمس الدين حسني (شفق نيوز · 3 أيلول 2026)",
                 [("الإنجاز", "70%"), ("الطرفان", "البصرة وخوزستان"), ("المصدر", "حسني")],
                 s, "broll_1.jpg", ACC[0],
                 ["رئيس اللجنة الاقتصادية بمجلس الشورى الإيراني",
                  "شمس الدين حسني قال لشفق نيوز",
                  "إن الربط السككي بلغ 70% إنجازاً"]),
            beat("لماذا يهم؟",
                 "16 كيلومتراً طُهّرت من الألغام",
                 "أُنجزت أعمال تطهير 16 كيلومتراً من الألغام في الجانب الإيراني، وهي عقبة عملية أمام مدّ الخط (شفق نيوز · 3 أيلول 2026).",
                 "16", "Kilometres cleared of mines on the Iranian side of the route",
                 "كيلومتراً أُنجز تطهيرها من الألغام في الجانب الإيراني من المسار، وهي عقبة عملية أمام مدّ الخط (شفق نيوز · 3 أيلول 2026)",
                 [("تطهير", "16 كم"), ("الجانب", "إيراني"), ("المنفذ", "الشلامجة")],
                 s, "broll_2.jpg", ACC[1],
                 ["أُنجزت أعمال تطهير 16 كيلومتراً من الألغام",
                  "في الجانب الإيراني من المسار",
                  "وهي عقبة عملية أمام مدّ الخط"]),
            beat("ما الغائب؟",
                 "منطقة حرة ومركز صناعي.. خطط",
                 "المنطقة التجارية الحرة والمركز الصناعي عند الشلامجة ما زالا خططاً، ولم يُعلن موعد إنجاز ولا كلفة ولا آلية تمويل (شفق نيوز · 3 أيلول 2026).",
                 "0", "Completion dates, costs or financing details published for the free zone and industrial centre",
                 "مواعيد إنجاز أو كلف أو آليات تمويل أُعلنت للمنطقة الحرة والمركز الصناعي عند الشلامجة، فكلاهما ما زال خطة (شفق نيوز · 3 أيلول 2026)",
                 [("موعد", "لم يُعلن"), ("كلفة", "لم تُعلن"), ("تمويل", "لم يُعلن")],
                 s, "broll_3.jpg", ACC[2],
                 ["المنطقة الحرة والمركز الصناعي عند الشلامجة",
                  "ما زالا خططاً",
                  "بلا موعد إنجاز ولا كلفة ولا تمويل"]),
        ],
        "arabicTicker": "الربط السككي البصرة–خوزستان عند 70% · تطهير 16 كم من الألغام · منطقة حرة ومركز صناعي بالشلامجة ما زالا خططاً · المصدر شفق نيوز",
        "endQuestion": "سافرت عبر الشلامجة؟ شكد كلّفتك السفرة؟",
        "sources": "شفق نيوز · شمس الدين حسني",
    },
    "brief": {
        "slug": s,
        "kicker": "سكك",
        "hookHeadline": "سكة البصرة–خوزستان عند سبعين بالمئة",
        "voText": "قال رئيس اللجنة الاقتصادية في مجلس الشورى الإيراني شمس الدين حسني لشفق نيوز خلال زيارة وفد إلى البصرة، إن مشروع الربط السككي بين البصرة ومحافظة خوزستان بلغ نسبة إنجاز سبعين بالمئة. وأضاف أنه جرى تطهير ستة عشر كيلومتراً من الألغام في الجانب الإيراني من المسار. وبحث الوفد أيضاً إقامة منطقة تجارية حرة ومركز صناعي عند منفذ الشلامجة، غير أن الاثنين ما زالا خططاً، إذ لم يُعلن موعد إنجاز ولا كلفة ولا آلية تمويل. سافرت عبر الشلامجة؟",
        "endQuestion": "سافرت عبر الشلامجة؟ شكد كلّفتك السفرة؟",
        "sourcesLine": "المصادر: شفق نيوز · شمس الدين حسني",
        "images": [img(s, "hero.jpg"), img(s, "broll_1.jpg"), img(s, "broll_2.jpg"), img(s, "broll_3.jpg")],
        "audioBed": "audio/music_01.mp3",
        "statPops": [
            {"value": "70%", "label": "نسبة إنجاز الربط السككي", "matchWord": "سبعين"},
            {"value": "16 كم", "label": "طُهّرت من الألغام", "matchWord": "الألغام"},
        ],
    },
    "caption": """سكة البصرة–خوزستان — وين وصل المشروع؟

نسبة الإنجاز معلنة، بس الموعد والكلفة والتمويل لا.

سافرت عبر الشلامجة؟ شكد كلّفتك السفرة؟

المصادر: شفق نيوز
#العراق #البصرة #الشلامجة #سكك_حديد #photonectnews
@photonect.news""",
}


def main() -> int:
    for slug, payload in SLATE.items():
        _validate(slug, payload["props"])
        d = POSTS / slug / ".meta"
        d.mkdir(parents=True, exist_ok=True)
        (d / "props.json").write_text(
            json.dumps(payload["props"], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        (POSTS / slug / "caption.txt").write_text(payload["caption"] + "\n", encoding="utf-8")
        if payload["brief"]:
            (d / "v11-brief.json").write_text(
                json.dumps(payload["brief"], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            tag = "V11"
        else:
            tag = "V10.1 control"
        print(f"  wrote {slug}  [{tag}]")
    print(f"\n{len(SLATE)} slugs authored")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
