#!/usr/bin/env python3
"""
!!! DO NOT RE-RUN THIS SCRIPT FOR 2026-08-16 ONCE THE SLATE HAS SHIPPED !!!
The JSON under data/posts/2026-08-16-*/ is AUTHORITATIVE after the Opus
copywriter pass and the Opus editorial QA gates, which edit wording in place.
Re-running this file would silently revert those edits.

Author the 2026-08-16 slate: props.json (x5) + v11-brief.json (x4) + caption.txt (x5).

Facts locked from Shafaq News reporting. Every article was fetched and its
dateline read off the page before any figure entered a reel:

  1. baghdad-37000-megawatt  Shafaq, 2026-08-15 15:39 UTC
  2. dollar-shop-gap         Shafaq, 2026-08-16 07:28 UTC
  3. homes-turkey-144        Shafaq, 2026-08-16 09:25 UTC (Turkish Statistical Institute)
  4. hormuz-half-exports     Shafaq EXCLUSIVE, 2026-08-16 11:09 UTC
  5. silence-currency-dinar  Shafaq, 2026-08-16 07:18 UTC (Eco Iraq observatory)

Every computed figure is labelled (محتسب).

VERIFICATION NOTES — traps caught during research:

  - The WebFetch SUMMARY of the Hormuz piece dated the war to "February 2025"
    and July exports to "July 2025". The VERBATIM article says «28 فبراير/شباط
    الماضي» and «يوليو/تموز الماضي» — i.e. 2026 both times. The summary
    back-dated the whole story by a year. Only the verbatim body is used.
  - The same Hormuz summary asserted a bare "4 million bpd previous production"
    without its qualifier. The article ties it to *before the war began on 28
    February*; the reel carries that qualifier.
  - The electricity summary rendered an import figure as «10 megawatts», which
    is not a credible national import volume and is almost certainly a mangled
    number. It is EXCLUDED entirely. The three procurement components that ARE
    used reconcile exactly: 15,000 + 12,000 + 10,000 = 37,000.
  - علي فالح الزيدي was verified as Prime Minister of Iraq (sworn in 14 May
    2026, per Al Jazeera encyclopedia + pmo.iq) before being titled as such.
    «صولة الفجر» is his anti-corruption campaign — NOT this story.
  - NOVELTY CHECK against our own archive: the 400-dinar bourse-to-shop gap on
    the dollar reel is NOT new. Our 08-15 slate published the identical shop
    prices (153,500 / 152,500) against the identical bourse (153,100). The reel
    therefore frames the 400 as a STANDING gap that explains what the viewer
    actually pays — never as a fresh development. The news today is that Baghdad
    did not move at all for a second session.

DISCARDED at verification:
  - «للأسبوع السابع على التوالي.. صادرات النفط العراقي لأميركا تسجل صفراً»
    (Shafaq, 16 Aug 06:08). Same running series as our own 08-11 slug
    `oil-zero-barrels`, and it would have put two oil stories in one slate.
  - «استقرار الذهب في بغداد وارتفاعه بأربيل» (16 Aug 08:18). Gold ran three
    days ago as `2026-08-13-gold-mithqal-946`; inside the 3-day freshness bar.
  - «تصنيف دولي: العراق يرتقي درجة على سلم الدخل العالمي خلال 30 عاماً»
    (16 Aug 10:21). A 30-year retrospective republished from a Visual Capitalist
    infographic — not a same-day structural development, and it fails the lens
    test: nothing concrete changes for the viewer.
  - «رئيس البنك المركزي الإيراني يزور العراق» (16 Aug 11:05). Genuinely today
    and genuinely money-power, but the article carries ZERO figures and the
    visit had not yet happened at author time («من المرتقب أن يصل … عصر اليوم»).
    No outcome to report; a reel would have been pure anticipation.

silence-currency-dinar is the silent V10.1 control -> no v11-brief. It is the
correct control because it is the only slug in the slate with no hard numeric
spine — it rests entirely on a named observatory's characterisation. This also
BREAKS the seven-slate run of the oil-export-price slug holding the control
role (08-04/05/06/10/11/13/15), which had made the A/B a test of one story type
as much as of one engine.

Posting order is alphabetical over slug names, producing:
  baghdad- < dollar- < homes- < hormuz- < silence-
i.e. كهرباء -> دولار -> عقارات -> نفط -> دينار (five distinct kickers, no two
consecutive alike), with the mandated dinar anchor landing in the 19:45 slot.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "data" / "posts"
D = "2026-08-16"
DATE_LABEL = "AUG 16 • 2026"
AR_DATE = "16 آب 2026"
HANDLE = "@photonect.news"
A1, A2, A3 = "#FFC217", "#4CC9F0", "#D72638"

SHAFAQ = [{"name": "Shafaq News", "domain": "shafaq.com"}]


def img(slug: str, name: str) -> str:
    return f"images/news/{D}-{slug}/{name}"


def beat(label, heading, body, big_v, big_l, big_ar, stats, slug, broll, accent):
    return {
        "label": label,
        "arabicHeading": heading,
        "arabicBody": body,
        "bigStat": {"value": big_v, "label": big_l, "arabicLabel": big_ar},
        "supportingStats": [{"label": l, "value": v} for l, v in stats],
        "broll": img(slug, broll),
        "brolls": [img(slug, broll)],
        "brollType": "image",
        "accent": accent,
        "brollSource": "صورة توضيحية · Photonect AI",
    }


def props(slug, bucket, variant, kicker, headline, subhead, beats, sources, ticker):
    return {
        "dateLabel": DATE_LABEL,
        "arabicDateLabel": AR_DATE,
        "handle": HANDLE,
        "audioBed": "audio/mood_cinematic.mp3",  # overwritten by assign-mood-rotation.py
        "topicBucket": bucket,
        "variant": variant,
        "breaking": {
            "arabicKicker": kicker,
            "arabicHeadline": headline,
            "englishSubhead": subhead,
            "heroMedia": img(slug, "hero.jpg"),
            "heroMediaType": "image",
        },
        "beats": beats,
        "sources": sources,
        "arabicTicker": ticker,
    }


def brief(slug, kicker, hook, vo, endq, sources_line, bed, pops):
    return {
        "slug": f"{D}-{slug}",
        "kicker": kicker,
        "hookHeadline": hook,
        "voText": vo,
        "endQuestion": endq,
        "sourcesLine": sources_line,
        "images": [img(slug, n) for n in ("hero.jpg", "broll_1.jpg", "broll_2.jpg", "broll_3.jpg")],
        "audioBed": bed,
        "statPops": pops,
    }


SLATE = {
    # ------------------------------------------------------------------ 18:00
    # P1 · electricity / services · near-daily summer anchor · LEAD
    "baghdad-37000-megawatt": {
        "props": props(
            "baghdad-37000-megawatt", "iraq_domestic", "A", "كهرباء",
            "37 ألف ميغاواط موعودة.. والموعد 2027",
            "PM AL-ZAIDI ORDERS 37,000MW PROCURED | 2027 SET AS THE DOUBLING YEAR",
            [
                beat(
                    "ماذا يحدث؟",
                    "الزيدي يوجّه بتأمين 37 ألف ميغاواط",
                    "وجّه رئيس مجلس الوزراء علي فالح الزيدي خلال زيارته وزارة الكهرباء بتأمين 37,000 ميغاواط إضافية، وبالصيانة الكاملة للإنتاج الحالي، بحسب شفق نيوز.",
                    "37,000",
                    "megawatts of additional capacity the prime minister directed be secured",
                    "حجم الطاقة الإضافية بالميغاواط التي وجّه رئيس مجلس الوزراء علي فالح الزيدي بتأمينها خلال زيارته وزارة الكهرباء (شفق نيوز، 15 آب 2026)",
                    [("الإنتاج الحالي", "30,000 ميغاواط"), ("التوجيه", "صيانة كاملة"), ("المصدر", "شفق نيوز")],
                    "baghdad-37000-megawatt", "hero.jpg", A1),
                beat(
                    "لماذا يهم؟",
                    "15 ألف من جنرال إلكتريك و12 شمسية",
                    "توزعت الطاقة الموجّه بتأمينها على 15,000 ميغاواط من جنرال إلكتريك و12,000 من الطاقة الشمسية و10,000 من الحرارية، بحسب شفق نيوز.",
                    "15,000",
                    "megawatts of the package assigned to General Electric",
                    "حصة شركة جنرال إلكتريك بالميغاواط ضمن الـ37,000 التي وجّه الزيدي بتأمينها، إلى جانب 12,000 من الطاقة الشمسية و10,000 من الحرارية (شفق نيوز)",
                    [("جنرال إلكتريك", "15,000"), ("الطاقة الشمسية", "12,000"), ("الحرارية", "10,000")],
                    "baghdad-37000-megawatt", "broll_1.jpg", A2),
                beat(
                    "ماذا بعد؟",
                    "2027 سنة المضاعفة.. ودراسات لهذا الصيف",
                    "قال الزيدي إن 2027 سيكون عام مضاعفة الإنتاج وقدرات النقل والتوزيع، وطلب دراسات عاجلة لتحسين التجهيز خلال الصيف المقبل، بحسب شفق نيوز.",
                    "2027",
                    "the year the prime minister named for doubling output and grid capacity",
                    "السنة التي قال رئيس مجلس الوزراء إنها ستكون عام مضاعفة إنتاج الطاقة الكهربائية ومضاعفة قدرات النقل والتوزيع (شفق نيوز)",
                    [("الوعد", "مضاعفة الإنتاج"), ("النقل والتوزيع", "مضاعفة القدرات"), ("الطلب العاجل", "دراسات للصيف")],
                    "baghdad-37000-megawatt", "broll_2.jpg", A3),
            ],
            SHAFAQ,
            [
                "رئيس مجلس الوزراء علي فالح الزيدي يزور وزارة الكهرباء ويوجّه بتأمين 37,000 ميغاواط (شفق نيوز)",
                "توزيع الطاقة الموجّه بتأمينها: 15,000 ميغاواط من جنرال إلكتريك و12,000 شمسية و10,000 حرارية (شفق نيوز)",
                "توجيه بإجراء الصيانة الكاملة للإنتاج الحالي البالغ 30,000 ميغاواط (شفق نيوز)",
                "الزيدي: 2027 عام مضاعفة الإنتاج ومضاعفة قدرات النقل والتوزيع (شفق نيوز)",
                "توجيه وزير الكهرباء بإعداد دراسات عاجلة لتحسين التجهيز خلال الصيف المقبل (شفق نيوز)",
                "كم ساعة كهرباء توصلك اليوم؟",
            ]),
        "brief": brief(
            "baghdad-37000-megawatt", "كهرباء",
            "وعد بـ37 ألف ميغاواط.. والموعد 2027",
            "وجّه رئيس مجلس الوزراء علي فالح الزيدي خلال زيارته وزارة الكهرباء بإجراء الصيانة الكاملة للإنتاج الحالي البالغ ثلاثين ألف ميغاواط. ووجّه أيضاً بتأمين سبعة وثلاثين ألف ميغاواط إضافية موزعة على خمسة عشر ألفاً من شركة جنرال إلكتريك واثني عشر ألفاً من الطاقة الشمسية وعشرة آلاف من الطاقة الحرارية. وقال الزيدي إن عام ألفين وسبعة وعشرين سيكون عام مضاعفة الإنتاج وقدرات النقل والتوزيع بحسب شفق نيوز. وطلب دراسات عاجلة لتحسين التجهيز هذا الصيف. كم ساعة كهرباء توصلك اليوم؟",
            "كم ساعة كهرباء توصلك اليوم؟",
            "المصادر: شفق نيوز",
            "audio/music_01.mp3",
            [
                {"value": "37,000", "label": "ميغاواط موجّه بتأمينها", "matchWord": "وثلاثين"},
                {"value": "2027", "label": "سنة مضاعفة الإنتاج", "matchWord": "وعشرين"},
            ]),
        "caption": """الكهرباء بالعراق.. شنو وعد بيه رئيس الوزراء؟

الزيدي وجّه بتأمين طاقة إضافية وسمّى 2027 سنة مضاعفة الإنتاج، والتفاصيل بالريل.

كم ساعة كهرباء توصلك اليوم؟

المصادر: شفق نيوز
#العراق #الكهرباء #اخبار_العراق
@photonect.news""",
    },

    # ------------------------------------------------------------------ 19:45
    # P1 · dinar · the mandated daily price-check anchor
    "dollar-shop-gap": {
        "props": props(
            "dollar-shop-gap", "iraq_economy", "B", "دولار",
            "الدولار ثابت.. بس تدفع 400 زيادة بالمحل",
            "BOURSE HOLDS AT 153,100 PER $100 | BAGHDAD SHOPS SELL 153,500 | ERBIL 153,150",
            [
                beat(
                    "ماذا يحدث؟",
                    "الكفاح والحارثية ثابتة على 153,100",
                    "استقرت بورصتا الكفاح والحارثية في بغداد عند 153,100 دينار لكل 100 دولار، وهو سعر جلسة السبت نفسه، بحسب شفق نيوز.",
                    "153,100",
                    "IQD per $100 at the Baghdad bourses, unchanged from Saturday",
                    "سعر بورصتي الكفاح والحارثية لكل 100 دولار صباح الأحد 16 آب 2026، وهو السعر نفسه المسجل في جلسة السبت (شفق نيوز)",
                    [("البورصة", "153,100"), ("مقابل السبت", "بلا تغيير"), ("المصدر", "شفق نيوز")],
                    "dollar-shop-gap", "hero.jpg", A1),
                beat(
                    "لماذا يهم؟",
                    "سعر المحل أعلى 400 دينار من البورصة",
                    "محال الصيرفة ببغداد تبيع الـ100 دولار بـ153,500 دينار وتشتري بـ152,500، أي أن سعر البيع يعلو سعر البورصة بـ400 دينار (محتسب)، بحسب شفق نيوز.",
                    "400",
                    "IQD the shop counter sits above the bourse reference rate (computed)",
                    "الفارق المحتسب بين سعر بيع محال الصيرفة في بغداد (153,500) وسعر بورصتي الكفاح والحارثية (153,100) لكل 100 دولار — وهو فارق قائم لا تغيّر جديد (شفق نيوز)",
                    [("بيع المحال", "153,500"), ("شراء المحال", "152,500"), ("فوق البورصة (محتسب)", "400")],
                    "dollar-shop-gap", "broll_1.jpg", A2),
                beat(
                    "ماذا بعد؟",
                    "أربيل تبيع بـ153,150",
                    "في أربيل بلغ سعر البيع 153,150 ديناراً لكل 100 دولار وسعر الشراء 153,050، بارتفاع طفيف مع تداولات الصباح، بحسب شفق نيوز.",
                    "153,150",
                    "IQD per $100 — the Erbil selling price on Sunday morning",
                    "سعر بيع الدولار في أربيل لكل 100 دولار صباح الأحد 16 آب 2026 مقابل سعر شراء 153,050، بارتفاع طفيف مع تداولات الصباح (شفق نيوز)",
                    [("بيع أربيل", "153,150"), ("شراء أربيل", "153,050"), ("الاتجاه", "ارتفاع طفيف")],
                    "dollar-shop-gap", "broll_2.jpg", A3),
            ],
            SHAFAQ,
            [
                "بورصتا الكفاح والحارثية في بغداد تستقران عند 153,100 دينار لكل 100 دولار (شفق نيوز)",
                "السعر نفسه المسجل في جلسة السبت — استقرار لا تغيّر (شفق نيوز)",
                "محال الصيرفة في بغداد: بيع 153,500 وشراء 152,500 لكل 100 دولار (شفق نيوز)",
                "سعر بيع المحال يعلو سعر البورصة بـ400 دينار — فارق محتسب وقائم (شفق نيوز)",
                "أربيل: بيع 153,150 وشراء 153,050 بارتفاع طفيف مع تداولات الصباح (شفق نيوز)",
                "شكد دفعت آخر مرة اشتريت دولار؟",
            ]),
        "brief": brief(
            "dollar-shop-gap", "دولار",
            "البورصة 153,100.. وبالمحل 153,500",
            "استقرت بورصتا الكفاح والحارثية في بغداد عند مئة وثلاثة وخمسين ألفاً ومئة دينار لكل مئة دولار وهو سعر جلسة السبت نفسه. لكن محال الصيرفة في بغداد تبيع المئة دولار بمئة وثلاثة وخمسين ألفاً وخمسمئة دينار أي بفارق أربعمئة دينار فوق سعر البورصة وهو فارق محتسب وقائم لا تغيّر جديد. وتشتري المحال بمئة واثنين وخمسين ألفاً وخمسمئة. أما أربيل فسعر البيع فيها مئة وثلاثة وخمسون ألفاً ومئة وخمسون ديناراً بحسب شفق نيوز. شكد دفعت آخر مرة اشتريت دولار؟",
            "شكد دفعت آخر مرة اشتريت دولار؟",
            "المصادر: شفق نيوز",
            "audio/mood_cinematic.mp3",
            [
                {"value": "400", "label": "فوق سعر البورصة (محتسب)", "matchWord": "أربعمئة"},
                {"value": "153,150", "label": "سعر البيع في أربيل", "matchWord": "أربيل"},
            ]),
        "caption": """سعر الدولار في العراق اليوم.. شكد بالبورصة وشكد بالمحل؟

البورصة ثابتة، بس السعر اللي تدفعه بمحل الصيرفة مو نفسه — الفرق بالريل.

شكد دفعت آخر مرة اشتريت دولار؟

المصادر: شفق نيوز
#العراق #الدولار #سعر_الصرف #الدينار_العراقي
@photonect.news""",
    },

    # ------------------------------------------------------------------ 21:15
    # P3 · money migration + pride · real Iraq hook
    "homes-turkey-144": {
        "props": props(
            "homes-turkey-144", "global_economy", "A", "عقارات",
            "العراقيون اشتروا 144 بيت بتركيا بشهر",
            "IRAQIS 4TH AMONG FOREIGN HOME BUYERS IN TURKEY IN JULY | ONE HOME BEHIND UKRAINE",
            [
                beat(
                    "ماذا يحدث؟",
                    "144 منزلاً في تموز.. والعراق رابعاً",
                    "اشترى العراقيون 144 منزلاً في تركيا خلال تموز، ليحلّوا رابعاً بين الجنسيات الأجنبية، بحسب بيانات معهد الإحصاء التركي التي نقلتها شفق نيوز.",
                    "144",
                    "homes bought by Iraqis in Turkey during July",
                    "عدد المنازل التي اشتراها العراقيون في تركيا خلال شهر تموز 2026 بحسب بيانات معهد الإحصاء التركي (شفق نيوز، 16 آب 2026)",
                    [("الترتيب", "الرابع"), ("الشهر", "تموز"), ("المصدر", "معهد الإحصاء التركي")],
                    "homes-turkey-144", "hero.jpg", A1),
                beat(
                    "لماذا يهم؟",
                    "بفارق منزل واحد عن أوكرانيا",
                    "تصدّر الروس بـ394 منزلاً ثم الإيرانيون بـ189 ثم الأوكرانيون بـ145، أي أن العراق جاء رابعاً بفارق منزل واحد فقط، بحسب شفق نيوز.",
                    "1",
                    "the single home separating Iraq from third place",
                    "الفارق بعدد المنازل بين العراق (144) وأوكرانيا (145) في ترتيب الجنسيات الأجنبية الأكثر شراءً للمنازل في تركيا خلال تموز (معهد الإحصاء التركي عبر شفق نيوز)",
                    [("روسيا", "394"), ("إيران", "189"), ("أوكرانيا", "145")],
                    "homes-turkey-144", "broll_1.jpg", A2),
                beat(
                    "ماذا بعد؟",
                    "و8 عقارات تجارية بالشهر نفسه",
                    "إلى جانب المنازل، سجّل العراقيون شراء 8 عقارات تجارية في تركيا خلال الشهر نفسه، بحسب البيانات التي نقلتها شفق نيوز.",
                    "8",
                    "commercial properties bought by Iraqis in Turkey in the same month",
                    "عدد العقارات التجارية التي اشتراها العراقيون في تركيا خلال تموز 2026 إلى جانب 144 منزلاً (معهد الإحصاء التركي عبر شفق نيوز)",
                    [("عقارات تجارية", "8"), ("منازل", "144"), ("الشهر", "تموز")],
                    "homes-turkey-144", "broll_2.jpg", A3),
            ],
            SHAFAQ,
            [
                "العراقيون اشتروا 144 منزلاً في تركيا خلال تموز 2026 (معهد الإحصاء التركي عبر شفق نيوز)",
                "العراق رابعاً بين الجنسيات الأجنبية الأكثر شراءً للمنازل في تركيا (شفق نيوز)",
                "روسيا أولاً بـ394 منزلاً ثم إيران بـ189 ثم أوكرانيا بـ145 (شفق نيوز)",
                "الفارق بين العراق وأوكرانيا منزل واحد فقط (شفق نيوز)",
                "العراقيون اشتروا أيضاً 8 عقارات تجارية في الشهر نفسه (شفق نيوز)",
                "تفكر تشتري بيت برة العراق؟",
            ]),
        "brief": brief(
            "homes-turkey-144", "عقارات",
            "144 بيت اشتراه العراقيون بتركيا بشهر",
            "سجّل العراقيون شراء مئة وأربعة وأربعين منزلاً في تركيا خلال شهر تموز ليحتلوا المركز الرابع بين الجنسيات الأجنبية بحسب بيانات معهد الإحصاء التركي التي نقلتها شفق نيوز. وتصدّر الروس القائمة بثلاثمئة وأربعة وتسعين منزلاً ثم الإيرانيون بمئة وتسعة وثمانين ثم الأوكرانيون بمئة وخمسة وأربعين منزلاً. أي أن العراق جاء رابعاً بفارق منزل واحد فقط عن أوكرانيا. كما اشترى العراقيون ثمانية عقارات تجارية في الشهر نفسه. تفكر تشتري بيت برة العراق؟",
            "تفكر تشتري بيت برة العراق؟",
            "المصادر: شفق نيوز · معهد الإحصاء التركي",
            "audio/music_03.mp3",
            [
                {"value": "144", "label": "منزلاً في تموز", "matchWord": "تركيا"},
                {"value": "1", "label": "الفارق عن أوكرانيا", "matchWord": "واحد"},
            ]),
        "caption": """العراقيون وشراء البيوت بتركيا.. شكد اشترينا بشهر واحد؟

بيانات معهد الإحصاء التركي تحط العراق رابعاً بين الجنسيات الأجنبية — والفارق عن الثالث أصغر مما تتوقع.

تفكر تشتري بيت برة العراق؟

المصادر: شفق نيوز، معهد الإحصاء التركي
#العراق #تركيا #عقارات
@photonect.news""",
    },

    # ------------------------------------------------------------------ 22:30
    # P2 · oil / geopolitics-economy · framed through salaries
    "hormuz-half-exports": {
        "props": props(
            "hormuz-half-exports", "mena_geopolitics", "B", "نفط",
            "نفطنا يمرّ بين ممرين.. أميركي وإيراني",
            "MP AL-KHAZRAJI: OFFICIAL TALKS WITH WASHINGTON AND TEHRAN OVER HORMUZ PASSAGE",
            [
                beat(
                    "ماذا يحدث؟",
                    "تحرك رسمي تجاه واشنطن وطهران",
                    "كشفت عضو لجنة النفط والغاز النيابية زينب الخزرجي عن تحرك دبلوماسي رسمي تجاه واشنطن وطهران لضمان مرور ناقلات النفط العراقية عبر هرمز، بحسب شفق نيوز.",
                    "2",
                    "passages in the strait — one under US forces, one under Iranian forces",
                    "عدد المسارات الرئيسية في مضيق هرمز بحسب عضو لجنة النفط والغاز النيابية زينب الخزرجي: أحدهما تسيطر عليه القوات الأميركية والآخر القوات الإيرانية (شفق نيوز، 16 آب 2026)",
                    [("المسار الأول", "قوات أميركية"), ("المسار الثاني", "قوات إيرانية"), ("المطلب", "مرور دائم")],
                    "hormuz-half-exports", "hero.jpg", A1),
                beat(
                    "لماذا يهم؟",
                    "صادرات تموز 49 مليون برميل",
                    "بلغت صادرات تموز نحو 49 مليون برميل، أكثر من 30 مليوناً منها عبر هرمز، مقابل معدل 105 ملايين برميل شهرياً قبل الحرب، بحسب وزارة النفط عبر شفق نيوز.",
                    "49M",
                    "barrels exported in July, against a 105-million monthly average before the war",
                    "إجمالي صادرات العراق النفطية في تموز 2026 بالبرميل، أكثر من 30 مليوناً منها مرّت عبر مضيق هرمز، مقابل معدل 105 ملايين برميل شهرياً قبل بدء الحرب في 28 شباط (بيان وزارة النفط الاتحادية عبر شفق نيوز)",
                    [("عبر هرمز", "أكثر من 30 مليوناً"), ("قبل الحرب (شهرياً)", "105 ملايين"), ("النفط من الإيرادات", "نحو 90%")],
                    "hormuz-half-exports", "broll_1.jpg", A2),
                beat(
                    "ماذا بعد؟",
                    "الخزرجي ترجّح 3 ملايين برميل يومياً",
                    "قالت الخزرجي إن الصادرات تجاوزت مليوني برميل يومياً بعد هبوطها دون المليون، وترجّح بلوغ 3 ملايين، ما ينعكس على الإيرادات ورواتب الموظفين، بحسب شفق نيوز.",
                    "3M",
                    "barrels per day al-Khazraji expects, which she ties to securing salaries",
                    "المستوى اليومي للصادرات الذي ترجّح عضو لجنة النفط والغاز النيابية زينب الخزرجي بلوغه، وتقول إنه سينعكس على زيادة الإيرادات المالية للدولة وتأمين رواتب الموظفين (شفق نيوز)",
                    [("حالياً", "أكثر من مليوني برميل"), ("أدنى مستوى", "دون المليون"), ("المرجّح (الخزرجي)", "3 ملايين")],
                    "hormuz-half-exports", "broll_2.jpg", A3),
            ],
            SHAFAQ,
            [
                "عضو لجنة النفط والغاز النيابية زينب الخزرجي تكشف عن تحرك رسمي تجاه واشنطن وطهران (شفق نيوز)",
                "الخزرجي: مساران رئيسيان في المضيق، أحدهما بسيطرة القوات الأميركية والآخر الإيرانية (شفق نيوز)",
                "العراق يسعى لمرور مستمر ودائم لناقلاته لا مؤقت (شفق نيوز)",
                "الصادرات تجاوزت مليوني برميل يومياً بعد هبوطها دون المليون مع بدء الحرب (شفق نيوز)",
                "صادرات تموز نحو 49 مليون برميل، أكثر من 30 مليوناً عبر هرمز (وزارة النفط الاتحادية عبر شفق نيوز)",
                "قبل الحرب في 28 شباط: نحو 4 ملايين برميل يومياً ومعدل تصدير 105 ملايين برميل شهرياً (شفق نيوز)",
                "راتبك وصل بموعده هذا الشهر؟",
            ]),
        "brief": brief(
            "hormuz-half-exports", "نفط",
            "نفطنا يمرّ بين ممرين.. أميركي وإيراني",
            "كشفت عضو لجنة النفط والغاز النيابية زينب الخزرجي عن تحرك عراقي رسمي تجاه واشنطن وطهران لضمان مرور ناقلات النفط عبر مضيق هرمز. وقالت لشفق نيوز إن في المضيق مسارين أحدهما تسيطر عليه القوات الأميركية والآخر القوات الإيرانية. وأضافت أن الصادرات تجاوزت حالياً مليوني برميل يومياً بعدما هبطت مع بدء الحرب إلى أقل من مليون. وبلغت صادرات تموز تسعة وأربعين مليون برميل مقابل معدل مئة وخمسة ملايين شهرياً قبل الحرب. وترجّح الخزرجي بلوغ ثلاثة ملايين برميل يؤمّن رواتب الموظفين. راتبك وصل بموعده هذا الشهر؟",
            "راتبك وصل بموعده هذا الشهر؟",
            "المصادر: شفق نيوز",
            "audio/mood_newsroom.mp3",
            [
                {"value": "49M", "label": "برميل صادرات تموز", "matchWord": "وأربعين"},
                {"value": "3M", "label": "برميل يومياً مرجّحة (الخزرجي)", "matchWord": "ثلاثة"},
            ]),
        "caption": """نفط العراق ومضيق هرمز.. شنو يصير بصادراتنا؟

نائبة بلجنة النفط تتحدث عن تحرك رسمي تجاه واشنطن وطهران، وتربط تعافي الصادرات بالرواتب.

راتبك وصل بموعده هذا الشهر؟

المصادر: شفق نيوز
#العراق #النفط #هرمز #الرواتب
@photonect.news""",
    },

    # ------------------------------------------------------------------ 23:45
    # P1 · accountability / dinar confidence · SILENT V10.1 CONTROL (no brief)
    "silence-currency-dinar": {
        "props": props(
            "silence-currency-dinar", "iraq_economy", "C", "دينار",
            "مرصد: الصمت عن «تغيير العملة» يربك السوق",
            "ECO IRAQ URGES OFFICIAL STATEMENT ON CURRENCY CHANGE | CBI AND FINANCE MINISTRY SILENT",
            [
                beat(
                    "ماذا يحدث؟",
                    "مرصد ينتقد إدارة الملف بتصريحات متفرقة",
                    "انتقد مرصد العراق الاقتصادي إدارة ملف بحجم العملة الوطنية عبر تصريحات متفرقة بدل المؤتمرات الرسمية، وقال إن ذلك يعكس ضعفاً في التنسيق الحكومي، بحسب شفق نيوز.",
                    "لا بيان",
                    "no official statement has been issued, the observatory says",
                    "خلاصة ما يقوله مرصد العراق الاقتصادي: لا بيان رسمي صادر عن الجهات المختصة يشرح ملف تغيير العملة، فيما يلتزم البنك المركزي ووزارة المالية الصمت (شفق نيوز، 16 آب 2026)",
                    [("الجهة", "مرصد العراق الاقتصادي"), ("المأخذ", "تصريحات متفرقة"), ("الوصف", "ضعف بالتنسيق")],
                    "silence-currency-dinar", "hero.jpg", A1),
                beat(
                    "لماذا يهم؟",
                    "المرصد: الغموض قد يهزّ الثقة بالدينار",
                    "حذّر المرصد من أن استمرار الغموض قد يضعف ثقة المواطن بالدينار ويزيد الطلب على العملات الأجنبية والذهب، بحسب شفق نيوز. وهذا تحذير المرصد لا واقعاً مسجّلاً.",
                    "الثقة",
                    "what the observatory warns is at stake — public confidence in the dinar",
                    "ما يحذّر مرصد العراق الاقتصادي من تآكله مع استمرار الغموض: ثقة المواطن بالدينار، مع ما قد يرافقها من زيادة الطلب على العملات الأجنبية والذهب — وهو تحذير المرصد لا واقع مسجّل (شفق نيوز)",
                    [("التحذير", "ثقة بالدينار"), ("الأثر المحتمل", "طلب على الدولار والذهب"), ("الصفة", "تحذير لا واقع")],
                    "silence-currency-dinar", "broll_1.jpg", A2),
                beat(
                    "ماذا بعد؟",
                    "مطالبة ببيان رسمي يضمن المدخرات",
                    "طالب المرصد الجهات المختصة بإصدار بيان رسمي يشرح أسباب تغيير العملة وآليات التنفيذ والمدد الزمنية وضمانات حماية مدخرات المواطنين، بحسب شفق نيوز.",
                    "4 مطالب",
                    "the four things the observatory wants any official statement to spell out",
                    "ما طالب مرصد العراق الاقتصادي بأن يتضمنه البيان الرسمي: أسباب تغيير العملة وآليات التنفيذ والمدد الزمنية وضمانات حماية مدخرات المواطنين (شفق نيوز)",
                    [("الأسباب والآليات", "مطلوبة"), ("المدد الزمنية", "مطلوبة"), ("ضمان المدخرات", "مطلوب")],
                    "silence-currency-dinar", "broll_2.jpg", A3),
            ],
            SHAFAQ,
            [
                "مرصد العراق الاقتصادي ينتقد إدارة ملف العملة الوطنية عبر تصريحات متفرقة بدل المؤتمرات الرسمية (شفق نيوز)",
                "المرصد: إعلان قرارات حساسة عبر جهات غير مخوّلة مع صمت المركزي والمالية يعكس ضعفاً في التنسيق الحكومي (شفق نيوز)",
                "المرصد يحذّر من أن الغموض قد يضعف ثقة المواطن بالدينار ويزيد الطلب على العملات الأجنبية والذهب (شفق نيوز)",
                "المرصد يطالب ببيان رسمي يشرح أسباب تغيير العملة وآليات التنفيذ والمدد الزمنية (شفق نيوز)",
                "المرصد يطالب بضمانات لحماية مدخرات المواطنين (شفق نيوز)",
                "تحتفظ بمدخراتك دينار لو دولار؟",
            ]),
        "brief": None,  # SILENT V10.1 CONTROL
        "caption": """تغيير العملة العراقية.. ليش ما اكو بيان رسمي؟

مرصد العراق الاقتصادي يطالب بتوضيح رسمي وبضمانات لمدخرات الناس، ويحذّر من أثر الغموض على السوق.

تحتفظ بمدخراتك دينار لو دولار؟

المصادر: شفق نيوز
#العراق #الدينار_العراقي #العملة #اقتصاد
@photonect.news""",
    },
}


def main() -> int:
    n_props = n_brief = n_cap = 0
    for slug, payload in SLATE.items():
        folder = POSTS / f"{D}-{slug}"
        meta = folder / ".meta"
        meta.mkdir(parents=True, exist_ok=True)

        (meta / "props.json").write_text(
            json.dumps(payload["props"], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        n_props += 1

        if payload["brief"] is not None:
            (meta / "v11-brief.json").write_text(
                json.dumps(payload["brief"], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            n_brief += 1

        (folder / "caption.txt").write_text(payload["caption"] + "\n", encoding="utf-8")
        n_cap += 1
        print(f"  ✓ {D}-{slug}  props{' +brief' if payload['brief'] else ' (V10.1 control)'}")

    print(f"\n== wrote {n_props} props · {n_brief} v11 briefs · {n_cap} captions ==")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
