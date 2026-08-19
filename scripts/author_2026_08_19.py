#!/usr/bin/env python3
"""Author the 2026-08-19 slate: props.json + v11-brief.json + caption.txt.

Four V11 voiced slugs + one V10.1 silent control (ghalibaf-baghdad-deadline —
the only slug in the slate whose spine is a diplomatic visit rather than a
number, and it rotates the control off the currency/oil/protest stories that
have held it for most of the month).

Slug names are chosen so ALPHABETICAL order == posting order
(a < d < g < o < s), which puts the mandated dinar anchor in the 19:45 slot:
  airport- (18:00) < dollar- (19:45) < ghalibaf- (21:15) < oil- (22:30) < stadium- (23:45)

Every figure below was fetched and its dateline read off the page by the
orchestrator, not carried over from a research summary.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "data" / "posts"
D = "2026-08-19"
DATE_LABEL = "AUG 19 • 2026"
AR_DATE = "19 آب 2026"


def img(slug: str, name: str) -> str:
    return f"images/news/{D}-{slug}/{name}"


def beat(label, heading, body, value, en_label, ar_label, stats, broll, accent):
    return {
        "label": label,
        "arabicHeading": heading,
        "arabicBody": body,
        "bigStat": {"value": value, "label": en_label, "arabicLabel": ar_label},
        "supportingStats": [{"label": k, "value": v} for k, v in stats],
        "broll": broll,
        "brolls": [broll],
        "brollType": "image",
        "accent": accent,
        "brollSource": "صورة توضيحية · Photonect AI",
    }


def props(slug, bucket, variant, kicker, headline, subhead, beats, sources, ticker):
    return {
        "dateLabel": DATE_LABEL,
        "arabicDateLabel": AR_DATE,
        "handle": "@photonect.news",
        "audioBed": "audio/mood_newsroom.mp3",
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


def brief(slug, kicker, hook, vo, endq, sources_line, pops):
    return {
        "slug": f"{D}-{slug}",
        "kicker": kicker,
        "hookHeadline": hook,
        "voText": vo,
        "endQuestion": endq,
        "sourcesLine": sources_line,
        "images": [img(slug, n) for n in ("hero.jpg", "broll_1.jpg", "broll_2.jpg", "broll_3.jpg")],
        "audioBed": "audio/mood_newsroom.mp3",
        "statPops": pops,
    }


SLATE: dict[str, dict] = {}

# ═══════════════════════════════════════════════ 18:00 · P1 accountability · V11
# 964media 2026-08-18 | 17:21. NOTE: the 964 HEADLINE says «تداهم وزير النقل»;
# the BODY is a judicial detention order against two STAFF. The body governs.
# The social-media allegation about an MP's daughter is UNPROVEN and is
# deliberately absent from every surface — see DELIVERY.
s = "airport-plane-returned"
SLATE[s] = {
    "props": props(
        s, "iraq_domestic", "A", "نقل",
        "ليش رجعت الطيارة؟ توقيف مدير مكتب وزير النقل",
        "ANTI-CORRUPTION COMMITTEE DETAINS TRANSPORT MINISTER'S OFFICE DIRECTOR AND A FLIGHT OPERATIONS OFFICER | NO CONVICTION HAS BEEN ISSUED",
        [
            beat("ماذا يحدث؟", "لجنة مكافحة الفساد توقف اثنين",
                 "داهمت لجنة مكافحة الفساد العليا برئاسة القاضي ضياء جعفر وزارة النقل يوم الثلاثاء وأوقفت مدير مكتب الوزير وضابط عمليات الطيران، بحسب شبكة 964.",
                 "2",
                 "officials detained pending investigation by order of the higher anti-corruption committee",
                 "موقوفان على ذمة التحقيق: مدير مكتب وزير النقل وضابط عمليات الطيران، بأمر لجنة مكافحة الفساد العليا برئاسة القاضي ضياء جعفر (شبكة 964)",
                 [("الموقوفون", "2"), ("الجهة", "لجنة الفساد"), ("التاريخ", "18 آب")],
                 img(s, "hero.jpg"), "#FFC217"),
            beat("لماذا يهم؟", "الخلفية: طائرة رجعت من طريقها",
                 "الخلفية إعادة طائرة عراقية كانت متجهة إلى تركيا بعد بلاغ يتعلق بإحدى المسافرات، بحسب شبكة 964. ووزير النقل نفسه لم يوقف.",
                 "1",
                 "Iraqi flight bound for Turkey turned back after a report concerning one passenger",
                 "طائرة عراقية واحدة كانت متجهة إلى تركيا أعيدت بعد بلاغ يتعلق بإحدى المسافرات، وهي خلفية قرار الإيقاف (شبكة 964)",
                 [("الوجهة", "تركيا"), ("الوزير", "لم يوقف"), ("السبب", "بلاغ")],
                 img(s, "broll_1.jpg"), "#4CC9F0"),
            beat("ماذا بعد؟", "موقوفان.. وبلا إدانة ولا تهمة معلنة",
                 "الاثنان موقوفان على ذمة التحقيق ولم تصدر بحقهما أي إدانة، ولم تعلن اللجنة تهمة محددة ولا مادة قانونية حتى الآن، بحسب شبكة 964.",
                 "0",
                 "convictions issued so far — both men are detained pending investigation, not convicted",
                 "لم تصدر أي إدانة بحق الموقوفين حتى الآن، ولم تعلن اللجنة تهمة محددة ولا المادة القانونية المستند إليها (شبكة 964)",
                 [("الإدانة", "لم تصدر"), ("التهمة", "لم تعلن"), ("الصفة", "موقوف")],
                 img(s, "broll_3.jpg"), "#D72638"),
        ],
        [{"name": "964media", "domain": "964media.com"},
         {"name": "Al-Rasheed", "domain": "alrasheedmedia.com"}],
        [
            "لجنة مكافحة الفساد العليا برئاسة القاضي ضياء جعفر داهمت وزارة النقل الثلاثاء (شبكة 964)",
            "الموقوفان: مدير مكتب وزير النقل وضابط عمليات الطيران (شبكة 964)",
            "وزير النقل نفسه لم يوقف (شبكة 964)",
            "الخلفية: إعادة طائرة عراقية متجهة إلى تركيا بعد بلاغ يتعلق بإحدى المسافرات (شبكة 964)",
            "الصفة القانونية: موقوفان على ذمة التحقيق — لم تصدر إدانة ولم تعلن تهمة محددة",
            "صارت لك رحلة تأخرت لو انلغت؟",
        ],
    ),
    "brief": brief(
        s, "نقل", "طيارة رجعت.. وتوقيف بوزارة النقل",
        "داهمت لجنة مكافحة الفساد العليا برئاسة القاضي ضياء جعفر وزارة النقل يوم الثلاثاء وأوقفت مدير مكتب الوزير وضابط عمليات الطيران بحسب شبكة 964. والخلفية إعادة طائرة عراقية كانت متجهة إلى تركيا بعد بلاغ يتعلق بإحدى المسافرات. ووزير النقل نفسه لم يوقف. الاثنان موقوفان على ذمة التحقيق ولم تصدر بحقهما أي إدانة. ولم تعلن اللجنة تهمة محددة ولا مادة قانونية حتى الآن. وقرار الإيقاف قضائي وليس إدارياً. صارت لك رحلة تأخرت لو انلغت؟",
        "صارت لك رحلة تأخرت لو انلغت؟",
        "المصادر: شبكة 964 · الرشيد",
        [{"value": "2", "label": "موقوفان بذمة التحقيق", "matchWord": "الاثنان"},
         {"value": "0", "label": "إدانة صدرت", "matchWord": "إدانة"}],
    ),
    "caption": """توقيف بوزارة النقل بسبب طيارة رجعت من طريقها — شنو صار؟

لجنة مكافحة الفساد العليا أوقفت اثنين من وزارة النقل، والوزير نفسه ما انوقف. الصفة لحد الآن: موقوفان على ذمة التحقيق، بلا إدانة وبلا تهمة معلنة.

صارت لك رحلة تأخرت لو انلغت؟

المصادر: شبكة 964، الرشيد
#العراق #وزارة_النقل #مكافحة_الفساد #مطار_بغداد #photonectnews
@photonect.news
""",
}

# ═══════════════════════════════════════════════ 19:45 · P1 dinar anchor · V11
# Shafaq News, dateline read as 2026-08-19T07:34:37+00:00 (morning session).
# EVERY comparison below is LIKE-FOR-LIKE and labelled: Erbil shop-SELL vs
# Baghdad shop-SELL. The bourse figure is never compared to a shop figure
# without both price types being named (the 2026-08-17 blocker).
s = "dollar-shops-155"
SLATE[s] = {
    "props": props(
        s, "iraq_economy", "B", "دولار",
        "الصيرفة تبيع الـ100 دولار بـ155 ألف",
        "BAGHDAD SHOPS SELL $100 AT 155,000 IQD | BOURSE 154,600 VS 153,850 TUESDAY | ERBIL SELLS AT 154,300",
        [
            beat("ماذا يحدث؟", "البورصة 154,600 بعد 153,850",
                 "سجلت بورصتا الكفاح والحارثية في بغداد صباح الأربعاء 154,600 دينار لكل 100 دولار، مقابل 153,850 ديناراً أمس الثلاثاء، بحسب شفق نيوز.",
                 "154,600",
                 "IQD per $100 at the Baghdad bourses on Wednesday morning, against 153,850 on Tuesday",
                 "سعر بورصتي الكفاح والحارثية لكل 100 دولار صباح الأربعاء 19 آب 2026 مقابل 153,850 ديناراً أمس الثلاثاء (شفق نيوز)",
                 [("البورصة اليوم", "154,600"), ("أمس الثلاثاء", "153,850"), ("الفارق (محتسب)", "750")],
                 img(s, "hero.jpg"), "#FFC217"),
            beat("لماذا يهم؟", "بالمحل تدفع 155,000",
                 "محال الصيرفة في بغداد تبيع الـ100 دولار بـ155,000 دينار وتشتري بـ154,000 دينار، وهذا هو السعر الذي يدفعه المواطن عند الشباك، بحسب شفق نيوز.",
                 "155,000",
                 "IQD per $100 — the Baghdad shop SELLING price, what a buyer actually pays at the window",
                 "سعر بيع محال الصيرفة في بغداد لكل 100 دولار صباح الأربعاء 19 آب 2026، مقابل سعر شراء 154,000 دينار (شفق نيوز)",
                 [("بيع المحال", "155,000"), ("شراء المحال", "154,000"), ("فوق البورصة", "400")],
                 img(s, "broll_1.jpg"), "#4CC9F0"),
            beat("ماذا بعد؟", "أربيل أرخص 700 من محال بغداد",
                 "في أربيل بلغ سعر البيع 154,300 دينار لكل 100 دولار، أي أقل بـ700 دينار من سعر البيع في محال بغداد البالغ 155,000، بحسب شفق نيوز.",
                 "700",
                 "IQD — how much cheaper Erbil's SELLING price is than Baghdad's shop SELLING price (like for like)",
                 "الفارق بين سعر البيع في أربيل 154,300 دينار وسعر البيع في محال بغداد 155,000 دينار لكل 100 دولار، محتسب من رقمي شفق نيوز وكلاهما سعر بيع",
                 [("بيع أربيل", "154,300"), ("بيع بغداد", "155,000"), ("الفارق (محتسب)", "700")],
                 img(s, "broll_2.jpg"), "#D72638"),
        ],
        [{"name": "Shafaq News", "domain": "shafaq.com"}],
        [
            "بورصتا الكفاح والحارثية: 154,600 دينار لكل 100 دولار صباح الأربعاء (شفق نيوز)",
            "أمس الثلاثاء: 153,850 ديناراً — الفارق 750 ديناراً (محتسب)",
            "محال الصيرفة في بغداد: بيع 155,000 وشراء 154,000 لكل 100 دولار (شفق نيوز)",
            "أربيل: بيع 154,300 وشراء 154,250 لكل 100 دولار (شفق نيوز)",
            "سعر البيع في أربيل أقل بـ700 دينار من سعر البيع في محال بغداد (محتسب — بيع مقابل بيع)",
            "فارق البيع والشراء داخل بغداد 1,000 دينار مقابل 50 ديناراً في أربيل كما نشرتها شفق نيوز",
            "بأي سعر اشتريت الدولار اليوم؟",
        ],
    ),
    "brief": brief(
        s, "دولار", "الدولار بالمحل 155 ألف",
        "سجلت بورصتا الكفاح والحارثية في بغداد صباح الأربعاء مئة وأربعة وخمسين ألفاً وستمئة دينار لكل مئة دولار مقابل مئة وثلاثة وخمسين ألفاً وثمانمئة وخمسين ديناراً أمس الثلاثاء أي بفارق سبعمئة وخمسين ديناراً وهو فارق محتسب. أما محال الصيرفة في بغداد فتبيع المئة دولار بمئة وخمسة وخمسين ألف دينار وتشتريها بمئة وأربعة وخمسين ألفاً. وفي أربيل سعر البيع مئة وأربعة وخمسون ألفاً وثلاثمئة دينار أي أرخص بسبعمئة دينار من سعر البيع في محال بغداد بحسب شفق نيوز. بأي سعر اشتريت الدولار اليوم؟",
        "بأي سعر اشتريت الدولار اليوم؟",
        "المصادر: شفق نيوز",
        [{"value": "750 دينار", "label": "فرق الجلسة (محتسب)", "matchWord": "محتسب"},
         {"value": "155,000", "label": "بيع محال الصيرفة", "matchWord": "الصيرفة"}],
    ),
    "caption": """سعر الدولار اليوم بالعراق — شكد صار بالمحل؟

السعر اللي تدفعه بمحل الصيرفة مو نفسه سعر البورصة، وأربيل تبيع أرخص من محال بغداد.

بأي سعر اشتريت الدولار اليوم؟

المصادر: شفق نيوز
#العراق #الدولار #سعر_الصرف #الدينار_العراقي #photonectnews
@photonect.news
""",
}

# ═══════════════════════════ 21:15 · P2 · V10.1 SILENT CONTROL (no v11-brief)
# V10.1 renders NEITHER arabicTicker NOR a CTA card, so the end question lives
# inside beat 3's body — the one surface the composition actually draws.
# Pills are kept under ~16 characters because V10.1 clips them.
s = "ghalibaf-baghdad-deadline"
SLATE[s] = {
    "props": props(
        s, "mena_politics", "A", "إيران",
        "قاليباف في بغداد.. ومهلة 30 أيلول تقترب",
        "IRAN'S PARLIAMENT SPEAKER ARRIVES IN BAGHDAD FOR A THREE-DAY VISIT AS THE SEPTEMBER 30 DISARMAMENT DEADLINE NEARS",
        [
            beat("ماذا يحدث؟", "رئيس البرلمان الإيراني في بغداد",
                 "وصل رئيس مجلس الشورى الإيراني محمد باقر قاليباف إلى بغداد واستقبله النائب الأول لرئيس البرلمان عدنان الفيحان، في زيارة من ثلاثة أيام تشمل كربلاء والنجف وتنتهي الجمعة، بحسب ذا ناشيونال.",
                 "3",
                 "day visit to Iraq including Karbala and Najaf, concluding on Friday",
                 "زيارة من ثلاثة أيام لرئيس مجلس الشورى الإيراني محمد باقر قاليباف تشمل بغداد وكربلاء والنجف وتنتهي يوم الجمعة (ذا ناشيونال)",
                 [("مدة الزيارة", "3 أيام"), ("المدن", "بغداد وكربلاء"), ("الاستقبال", "عدنان الفيحان")],
                 img(s, "hero.jpg"), "#FFC217"),
            beat("لماذا يهم؟", "مهلة الحكومة تنتهي 30 أيلول",
                 "تأتي الزيارة فيما ترفض فصائل مسلحة مدعومة من إيران تسليم سلاحها قبل مهلة حكومية تنتهي في 30 أيلول، وهو ما يعمّق الخلاف بين بغداد وتلك الفصائل، بحسب ذا ناشيونال.",
                 "30 أيلول",
                 "government-imposed deadline for Iran-backed armed groups in Iraq to disarm",
                 "المهلة الحكومية المحددة لنزع سلاح الفصائل المسلحة المدعومة من إيران، والفصائل ترفض التسليم حتى الآن (ذا ناشيونال)",
                 [("المهلة", "30 أيلول"), ("الموقف", "رفض التسليم"), ("المصدر", "ذا ناشيونال")],
                 img(s, "broll_3.jpg"), "#4CC9F0"),
            beat("ماذا بعد؟", "وملف تصدير النفط حاضر",
                 "وتتزامن الزيارة مع مباحثات جارية بين العراق وإيران بشأن تصدير النفط العراقي عبر مضيق هرمز، بحسب ذا ناشيونال. سمعت بمهلة 30 أيلول قبل اليوم لو لا؟",
                 "هرمز",
                 "Iraq-Iran talks on exporting Iraqi crude through the Strait of Hormuz run alongside the visit",
                 "مباحثات عراقية إيرانية جارية بشأن تصدير النفط العراقي عبر مضيق هرمز تتزامن مع الزيارة (ذا ناشيونال)",
                 [("الملف", "تصدير النفط"), ("الممر", "مضيق هرمز"), ("الحالة", "مباحثات")],
                 img(s, "broll_1.jpg"), "#D72638"),
        ],
        [{"name": "The National", "domain": "thenationalnews.com"},
         {"name": "Shafaq News", "domain": "shafaq.com"}],
        [
            "قاليباف وصل بغداد في زيارة من ثلاثة أيام تشمل كربلاء والنجف (ذا ناشيونال)",
            "استقبله النائب الأول لرئيس البرلمان عدنان الفيحان (ذا ناشيونال)",
            "مهلة حكومية لنزع سلاح الفصائل المدعومة من إيران تنتهي في 30 أيلول (ذا ناشيونال)",
            "الزيارة تتزامن مع مباحثات بشأن تصدير النفط العراقي عبر مضيق هرمز (ذا ناشيونال)",
            "سمعت بمهلة 30 أيلول قبل اليوم لو لا؟",
        ],
    ),
    "brief": None,   # ← the V10.1 silent control
    "caption": """قاليباف بزيارة بغداد ومهلة 30 أيلول — شنو العلاقة؟

رئيس البرلمان الإيراني ببغداد ثلاثة أيام، بالوقت اللي مهلة نزع سلاح الفصائل تقترب وملف تصدير النفط على الطاولة.

سمعت بمهلة 30 أيلول قبل اليوم لو لا؟

المصادر: ذا ناشيونال، شفق نيوز
#العراق #إيران #بغداد #أخبار #photonectnews
@photonect.news
""",
}

# ═══════════════════════════════════════════════ 22:30 · P1 fiscal · V11
# Shafaq News (English), dateline read as 2026-08-18T14:00:05+00:00.
# The PM line is REPORTED SPEECH in the source, not a direct quotation — it is
# never rendered inside quotation marks on any surface.
s = "oil-week-salaries"
SLATE[s] = {
    "props": props(
        s, "iraq_economy", "B", "موازنة",
        "الزيدي: برميل ما ينباع.. راتب يتأخر",
        "FINANCE MINISTRY EXECUTION DATA: 18.727T IQD DEFICIT TO END-JUNE | SALARIES 30.769T | PM GIVES THE OIL MINISTRY ONE WEEK",
        [
            beat("ماذا يحدث؟", "عجز 18.727 ترليون بستة أشهر",
                 "بحسب بيانات تنفيذ الموازنة لدى وزارة المالية، بلغ الإنفاق حتى نهاية حزيران 54.673 ترليون دينار مقابل إيرادات 35.946 ترليوناً، أي بعجز قدره 18.727 ترليون دينار، بحسب شفق نيوز.",
                 "18.727 ترليون",
                 "IQD federal deficit through end-June, on spending of 54.673T against revenue of 35.946T",
                 "عجز الموازنة الاتحادية حتى نهاية حزيران 2026 بحسب بيانات تنفيذ الموازنة لدى وزارة المالية: إنفاق 54.673 ترليون دينار مقابل إيرادات 35.946 ترليوناً (شفق نيوز)",
                 [("الإنفاق", "54.673 ت"), ("الإيرادات", "35.946 ت"), ("العجز", "18.727 ت")],
                 img(s, "hero.jpg"), "#FFC217"),
            beat("لماذا يهم؟", "الرواتب وحدها 30.769 ترليون",
                 "رواتب القطاع العام وحدها بلغت 30.769 ترليون دينار من أصل الإنفاق، والنفط شكّل نحو 79% من إيرادات الدولة، بحسب شفق نيوز.",
                 "30.769 ترليون",
                 "IQD in public-sector salaries through end-June — the single largest line of state spending",
                 "رواتب القطاع العام حتى نهاية حزيران 2026 بلغت 30.769 ترليون دينار من أصل إنفاق 54.673 ترليوناً، والنفط نحو 79% من الإيرادات (شفق نيوز)",
                 [("الرواتب", "30.769 ت"), ("حصة النفط", "79%"), ("غير النفطي", "21%")],
                 img(s, "broll_1.jpg"), "#4CC9F0"),
            beat("ماذا بعد؟", "مهلة أسبوع لوزارة النفط",
                 "وبحسب شفق نيوز، أمهل رئيس الوزراء علي الزيدي يوم الاثنين وزارة النفط أسبوعاً واحداً لتقديم حلول تصديرية ملموسة، محذراً من أن كل برميل لا يُباع يعني تأخر رواتب أو خدمات وإيراداً ضائعاً للدولة.",
                 "أسبوع",
                 "one week given to the Oil Ministry, from Monday, to produce tangible export solutions",
                 "مهلة أسبوع واحد منحها رئيس الوزراء علي الزيدي يوم الاثنين لوزارة النفط لتقديم حلول تصديرية ملموسة (شفق نيوز)",
                 [("المهلة", "أسبوع"), ("بدأت", "الاثنين"), ("الجهة", "وزارة النفط")],
                 img(s, "broll_3.jpg"), "#D72638"),
        ],
        [{"name": "Shafaq News", "domain": "shafaq.com"},
         {"name": "وزارة المالية", "domain": "mof.gov.iq"}],
        [
            "بيانات تنفيذ الموازنة: إنفاق 54.673 ترليون دينار حتى نهاية حزيران (شفق نيوز)",
            "الإيرادات 35.946 ترليوناً — منها 28.433 ترليوناً نفطية و7.513 ترليوناً غير نفطية",
            "العجز 18.727 ترليون دينار في ستة أشهر",
            "رواتب القطاع العام وحدها 30.769 ترليون دينار",
            "النفط نحو 79% من إيرادات الدولة، وغير النفطي نحو 21% بعد أن كان نحو 12%",
            "رئيس الوزراء علي الزيدي أمهل وزارة النفط أسبوعاً من يوم الاثنين لحلول تصديرية (شفق نيوز)",
            "راتبك تأخر هذا الشهر لو وصل بموعده؟",
        ],
    ),
    "brief": brief(
        s, "موازنة", "العجز 18.7 ترليون.. والرواتب 30.7",
        "بحسب بيانات تنفيذ الموازنة لدى وزارة المالية سجل العراق حتى نهاية حزيران عجزاً قدره ثمانية عشر ترليوناً وسبعمئة وسبعة وعشرين مليار دينار. ورواتب القطاع العام وحدها بلغت ثلاثين ترليوناً وسبعمئة وتسعة وستين ملياراً من أصل إنفاق قدره أربعة وخمسون ترليوناً. والنفط شكّل نحو تسعة وسبعين بالمئة من إيرادات الدولة. وبحسب شفق نيوز أمهل رئيس الوزراء علي الزيدي وزارة النفط أسبوعاً واحداً لحلول تصديرية ملموسة محذراً من أن كل برميل لا يباع يعني تأخر رواتب أو خدمات. راتبك تأخر هذا الشهر لو وصل بموعده؟",
        "راتبك تأخر هذا الشهر لو وصل بموعده؟",
        "المصادر: شفق نيوز · بيانات وزارة المالية",
        [{"value": "18.727 ترليون", "label": "عجز ستة أشهر", "matchWord": "عجزاً"},
         {"value": "30.769 ترليون", "label": "رواتب ستة أشهر", "matchWord": "القطاع"}],
    ),
    "caption": """عجز الموازنة والرواتب — منين تجي فلوس راتبك؟

بيانات تنفيذ الموازنة تحچي عن ستة أشهر: إنفاق أكبر من الإيراد، والرواتب أثقل بند. ورئيس الوزراء ربط تأخر الرواتب ببرميل ما ينباع.

راتبك تأخر هذا الشهر لو وصل بموعده؟

المصادر: شفق نيوز، بيانات وزارة المالية
#العراق #الموازنة #رواتب #النفط #photonectnews
@photonect.news
""",
}

# ═══════════════════════════════════════════════ 23:45 · P3 sport/pride · V11
# Shafaq News, dateline read as 2026-08-18T07:20:10+00:00.
# The source says «final approval still pending» — every surface says so too.
s = "stadium-basra-asia"
SLATE[s] = {
    "props": props(
        s, "sport", "C", "رياضة",
        "استقلال الإيراني يطلب ملعب البصرة",
        "IRAN'S ESTEGHLAL WANTS BASRA INTERNATIONAL STADIUM AS ITS AFC CHAMPIONS LEAGUE ELITE HOME VENUE | FINAL APPROVAL STILL PENDING",
        [
            beat("ماذا يحدث؟", "طلب: البصرة مقراً آسيوياً",
                 "طلب نادي استقلال الإيراني اعتماد ملعب البصرة الدولي مقراً محايداً لمبارياته في دوري أبطال آسيا للنخبة لموسم 2026/27، بحسب شفق نيوز.",
                 "2026/27",
                 "the AFC Champions League Elite season for which Esteghlal wants Basra as its home venue",
                 "الموسم المطلوب لاعتماد ملعب البصرة الدولي مقراً محايداً لمباريات نادي استقلال في دوري أبطال آسيا للنخبة (شفق نيوز)",
                 [("الملعب", "البصرة الدولي"), ("البطولة", "أبطال آسيا"), ("الموسم", "2026/27")],
                 img(s, "hero.jpg"), "#FFC217"),
            beat("لماذا يهم؟", "الأندية الإيرانية تلعب خارج إيران",
                 "الاتحاد الآسيوي يلزم الأندية الإيرانية بخوض مبارياتها القارية خارج إيران، واستند النادي إلى قرب البصرة وسهولة تنقل جمهوره وملاءمة البنى الرياضية، بحسب شفق نيوز.",
                 "خارج إيران",
                 "AFC requirement that Iranian clubs stage their continental home fixtures outside Iran",
                 "شرط الاتحاد الآسيوي بأن تخوض الأندية الإيرانية مبارياتها القارية خارج إيران، وهو سبب البحث عن ملعب محايد (شفق نيوز)",
                 [("الشرط", "خارج إيران"), ("السبب", "قرب البصرة"), ("البديل", "أوزبكستان")],
                 img(s, "broll_1.jpg"), "#4CC9F0"),
            beat("ماذا بعد؟", "والموافقة النهائية لم تصدر",
                 "الموافقة النهائية لم تصدر بعد، وتبقى أوزبكستان بديلاً إذا حالت شروط الملاعب أو الجدولة دون ذلك، فيما جرت قرعة دور المجموعات في كوالالمبور، بحسب شفق نيوز.",
                 "بانتظار",
                 "final approval is still pending — this remains a request, not a confirmed arrangement",
                 "الموافقة النهائية على اعتماد ملعب البصرة لم تصدر بعد، والأمر ما زال طلباً لا قراراً، مع بقاء أوزبكستان خياراً بديلاً (شفق نيوز)",
                 [("الموافقة", "لم تصدر"), ("البديل", "أوزبكستان"), ("القرعة", "كوالالمبور")],
                 img(s, "broll_3.jpg"), "#D72638"),
        ],
        [{"name": "Shafaq News", "domain": "shafaq.com"}],
        [
            "نادي استقلال الإيراني يطلب ملعب البصرة الدولي مقراً محايداً لمبارياته القارية (شفق نيوز)",
            "البطولة: دوري أبطال آسيا للنخبة — موسم 2026/27",
            "الاتحاد الآسيوي يلزم الأندية الإيرانية باللعب خارج إيران (شفق نيوز)",
            "أسباب الاختيار: قرب البصرة وسهولة تنقل الجمهور وملاءمة البنى الرياضية",
            "أوزبكستان تبقى بديلاً — والموافقة النهائية لم تصدر بعد (شفق نيوز)",
            "تروح تشجع بملعب البصرة لو لا؟",
        ],
    ),
    "brief": brief(
        s, "رياضة", "ملعب البصرة بيت فريق إيراني؟",
        "طلب نادي استقلال الإيراني اعتماد ملعب البصرة الدولي مقراً لمبارياته في دوري أبطال آسيا للنخبة لموسم ألفين وستة وعشرين وسبعة وعشرين بحسب شفق نيوز. والاتحاد الآسيوي يلزم الأندية الإيرانية بخوض مبارياتها القارية خارج إيران. واستند النادي إلى قرب البصرة وسهولة تنقل جمهوره وملاءمة البنى الرياضية. وتبقى أوزبكستان بديلاً إذا حالت شروط الملاعب أو الجدولة دون ذلك. وقرعة دور المجموعات جرت في كوالالمبور. لكن الموافقة النهائية لم تصدر بعد. تروح تشجع بملعب البصرة لو لا؟",
        "تروح تشجع بملعب البصرة لو لا؟",
        "المصادر: شفق نيوز",
        [{"value": "خارج إيران", "label": "شرط الاتحاد الآسيوي", "matchWord": "الآسيوي"},
         {"value": "لم تصدر", "label": "الموافقة النهائية", "matchWord": "الموافقة"}],
    ),
    "caption": """ملعب البصرة الدولي يستضيف نادي إيراني بدوري أبطال آسيا؟

استقلال يريد البصرة مقراً لمبارياته القارية لأن الأندية الإيرانية ملزمة تلعب خارج إيران — بس القرار النهائي بعده ما صدر.

تروح تشجع بملعب البصرة لو لا؟

المصادر: شفق نيوز
#العراق #البصرة #دوري_أبطال_آسيا #كرة_القدم #photonectnews
@photonect.news
""",
}


def main() -> int:
    for slug, payload in SLATE.items():
        folder = POSTS / f"{D}-{slug}"
        meta = folder / ".meta"
        meta.mkdir(parents=True, exist_ok=True)
        (meta / "props.json").write_text(
            json.dumps(payload["props"], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        if payload["brief"] is not None:
            (meta / "v11-brief.json").write_text(
                json.dumps(payload["brief"], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        (folder / "caption.txt").write_text(payload["caption"], encoding="utf-8")
        engine = "V10.1 control" if payload["brief"] is None else "V11"
        print(f"  wrote {D}-{slug}  ({engine})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
