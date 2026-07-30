#!/usr/bin/env python3
"""Author the 2026-07-30 Photonect NEWS slate.

5 slugs (Iraq/MENA money-power lens). Posting order = alphabetical slug order,
which is exactly what `post-to-uploadpost.py --spread` maps onto the Baghdad
evening slots (`sorted(POSTS.glob(f"{date}-*"))`, slug i -> slot i):

  1 diwaniyah-graft-9bn   iraq_domestic     V11  A  18:00
  2 dollar-city-gap       iraq_domestic     V11  B  19:45  (daily dollar anchor)
  3 heat-50-saturday      wildcard          V11  C  21:15
  4 loan-law-15tn         iraq_domestic     V11  A  22:30
  5 oil-89-reroute        mena_geopolitics  V10  B  23:45  <- silent control, no v11

Directional shift vs 2026-07-29: yesterday was "who collects the war premium".
Today is "the price depends on where you stand" — the same 100 dollars costs a
different number in Baghdad, Erbil and Basra and a fourth number at the central
bank; 9 billion dinars of spending vouchers walk out of one provincial
municipality; the thermometer reads 48 in Maysan and 44 in Duhok on the same
afternoon; and the state, with no budget at all, is asking parliament for the
legal right to borrow whatever it takes to pay you.

Pillar mix: P1 x3 (diwaniyah, dollar, loan-law), P2 x1 (oil), P3 x1 (heat).
The "no two consecutive same pillar" guide cannot hold simultaneously with the
standing mandates that (a) the dollar anchor aims for the 19:45 slot and (b) a
corruption slug ships every day, because 3 P1 slugs in 5 alphabetical slots with
slot 2 pinned forces one adjacent P1 pair. The pair is slots 1-2 and the two are
maximally different in subject (provincial procurement graft vs the FX market),
so it does not read as repetition. Flagged in DELIVERY.

The day's dominant event (the US-Saudi strikes) is covered ONLY through its price
consequence in slug 5, and that slug is the unvoiced V10 control rather than the
lead. Deliberately excluded slate-wide: the PMF casualty figures (20 killed / 32
wounded per 964) — preliminary, and this channel does not headline a body count;
the "urgent security plan" package (security governance, not money); and every
attribution of blame for the strikes.

Banned this slate (per fact sheet):
  * any day-over-day dollar move — the only same-day print I could verify is the
    964 table of 30 Jul 11:10, and the 29 Jul comparison traces to a Telegram
    rate-scraper channel, not a newsroom. The slug is built on the CITY SPREAD
    and the OFFICIAL-RATE GAP, both inside that one sourced table.
  * the 07-27 framing of the official-rate gap as 18,200 / 13.8% — that implies a
    132,000 official rate, while 964 states 130,000 today. Today's number is used
    and attributed; the older one is not reconciled or referenced.
  * any electricity supply-hours figure — the candidates (Baghdad 12-13 h,
    Anbar 600-650 MW vs 2,700-3,000 MW need, generation 18,500/22,000/28,000 MW)
    could not be pinned to a dated same-day statement, so there is no
    electricity slug today despite the near-daily mandate. Flagged in DELIVERY.
  * any health, mortality or power-grid consequence of the heatwave — the met
    office bulletin makes no such claim, so neither does the reel.
  * the 10-15tn borrowing estimate as fact — it is an unnamed finance-ministry
    estimate and is labelled «تقديرات أولية» everywhere it appears.
  * the 2027 budget projection (200tn / 150tn / 50tn) — next year's plan, not a
    <24h development, and it would muddy the "no budget at all" spine.
  * Iraqi crude export volumes and any Basra differential — still irreconcilable
    across sources, same as 2026-07-29.

brollSource is «صورة توضيحية · Photonect AI» slate-wide: schema.ts documents that
field as a photo-credit chip and Beat.tsx paints it over every beat, while
media-stamp.json records 100% of the imagery as generated. Crediting Reuters/AP
for a generated frame is misattribution — claim attribution lives in arabicBody,
bigStat.arabicLabel, the ticker and the Sources scene instead.

Writes per slug: .meta/props.json, caption.txt, .meta/media-stamp.json, and (for
the 4 voiced) .meta/v11-brief.json. Western numerals on-screen; voText spells
numbers in words (MSA newscast register). No Persian yeh/kaf (grep-guarded).
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POSTS = ROOT / "data" / "posts"
DATE = "2026-07-30"

STAMP = {
    "hunted_at": f"{DATE}T12:10:00+00:00",
    "manual": True,
    "source": "higgsfield nano_banana_pro (KIE 402 — credits exhausted, 4th day)",
    "date": DATE,
    "note": (
        "KIE returned HTTP 402 'Credits insufficient' on a live submit test for the "
        "fourth consecutive day, so the whole slate was generated on Higgsfield's "
        "nano_banana_pro at 9:16 / 2k (the API echoed the model back as "
        "'nano_banana_2', same Nano Banana Pro family, different vendor). Every "
        "image Read-verified by hand before acceptance. No stock imagery anywhere "
        "in the slate, so auto-post stays ON."
    ),
}

ARABIC_DATE = "30 يوليو 2026"
DATE_LABEL = "JUL 30 • 2026"


def img(slug: str, name: str) -> str:
    return f"images/news/{slug}/{name}"


def beat(label, heading, body, stat_value, stat_label, stat_arabic,
         supporting, slug, broll, accent):
    return {
        "label": label,
        "arabicHeading": heading,
        "arabicBody": body,
        "bigStat": {"value": stat_value, "label": stat_label, "arabicLabel": stat_arabic},
        "supportingStats": [{"label": l, "value": v} for l, v in supporting],
        "broll": img(slug, broll),
        "brolls": [img(slug, broll)],
        "brollType": "image",
        "accent": accent,
        "brollSource": "صورة توضيحية · Photonect AI",
    }


S1 = f"{DATE}-diwaniyah-graft-9bn"
S2 = f"{DATE}-dollar-city-gap"
S3 = f"{DATE}-heat-50-saturday"
S4 = f"{DATE}-loan-law-15tn"
S5 = f"{DATE}-oil-89-reroute"

SLUGS: dict[str, dict] = {}

# ───────────────────────── 1 · DIWANIYAH MUNICIPALITY GRAFT (P1, LEAD 18:00) ──
SLUGS[S1] = {
    "props": {
        "dateLabel": DATE_LABEL,
        "arabicDateLabel": ARABIC_DATE,
        "handle": "@photonect.news",
        "audioBed": "audio/mood_newsroom.mp3",
        "topicBucket": "iraq_domestic",
        "variant": "A",
        "breaking": {
            "arabicKicker": "نزاهة · بلدية",
            "arabicHeadline": "9 مليارات دينار مستندات صرف… ببلدية واحدة",
            "englishSubhead": "INTEGRITY COMMISSION ISSUES ~30 WARRANTS IN DIWANIYAH MUNICIPALITY, SEIZES OVER 9BN IQD IN SPENDING VOUCHERS",
            "heroMedia": img(S1, "hero.jpg"),
            "heroMediaType": "image",
        },
        "beats": [
            beat(
                "ماذا يحدث؟",
                "نحو 30 أمر قبض وتحرٍ ببلدية الديوانية",
                "هيئة النزاهة الاتحادية أعلنت الخميس تنفيذ عملية في بلدية الديوانية بنحو 30 أمر قبض وتحرٍ، بالتنسيق مع خلية الصقور الاستخبارية.",
                "30", "arrest and search warrants",
                "عدد أوامر القبض والتحري التي أعلنت هيئة النزاهة الاتحادية تنفيذها في بلدية الديوانية يوم الخميس 30 تموز 2026، بالتنسيق مع خلية الصقور الاستخبارية (هيئة النزاهة الاتحادية · 964)",
                [("أوامر", "30"), ("مديرون سابقون", "5"), ("مقاولون", "3")],
                S1, "broll_1.jpg", "#D72638",
            ),
            beat(
                "لماذا يهم؟",
                "المدير الحالي و5 سابقون و15 موظفاً",
                "الأوامر شملت مدير البلدية الحالي و5 من مديريها السابقين و6 من موظفي الحسابات والتدقيق ومدير حسابات المحافظة و15 موظفاً و3 مقاولين، بحسب الهيئة.",
                "9", "billion IQD in seized vouchers",
                "قيمة مستندات الصرف التي قالت هيئة النزاهة الاتحادية إنها ضُبطت في العملية، وتجاوزت 9 مليارات دينار في معاملات البلدية (هيئة النزاهة الاتحادية · 964)",
                [("موظفو حسابات وتدقيق", "6"), ("موظفون آخرون", "15"), ("مستندات صرف", "9 مليارات")],
                S1, "broll_2.jpg", "#FFC217",
            ),
            beat(
                "ماذا بعد؟",
                "قوائم أسعار مبالغ فيها ووثائق أعمال وهمية",
                "الهيئة تحدثت عن قوائم أسعار مبالغ فيها ووثائق أعمال وهمية، وأحالت القضايا إلى قضاة تحقيق مختصين بجرائم النزاهة وفق المواد 315 و319 و340.",
                "315·319·340", "Penal Code articles cited",
                "مواد قانون العقوبات التي أحيلت القضايا بموجبها إلى قضاة تحقيق مختصين بجرائم النزاهة، بحسب هيئة النزاهة الاتحادية (964)",
                [("مواد قانونية", "3"), ("أختام رسمية", "مضبوطة"), ("مبالغ نقدية", "مضبوطة")],
                S1, "broll_3.jpg", "#4CC9F0",
            ),
        ],
        "sources": [
            {"name": "Federal Integrity Commission", "domain": "nazaha.iq"},
            {"name": "964media", "domain": "964media.com"},
        ],
        "arabicTicker": [
            "هيئة النزاهة الاتحادية أعلنت الخميس 30 تموز 2026 تنفيذ عملية في بلدية الديوانية بنحو 30 أمر قبض وتحرٍ (964)",
            "الأوامر شملت مدير البلدية الحالي و5 من مديريها السابقين، بحسب الهيئة (964)",
            "وشملت أيضاً 6 من موظفي الحسابات والتدقيق ومدير حسابات المحافظة و15 موظفاً و3 مقاولين (964)",
            "الهيئة قالت إنها ضبطت مستندات صرف تجاوزت 9 مليارات دينار في معاملات البلدية (964)",
            "التهم المعلنة تشمل الاختلاس والرشوة والتربح من العقود والتلاعب بالأسعار وتبديد المال العام (964)",
            "العملية نُفذت بالتنسيق مع خلية الصقور الاستخبارية، وأحيلت القضايا وفق المواد 315 و319 و340 (964)",
            "شكد صار على آخر تصليح بشارعكم؟",
        ],
    },
    "v11": {
        "kicker": "نزاهة",
        "hookHeadline": "9 مليارات دينار… ببلدية واحدة",
        "voText": (
            "أعلنت هيئة النزاهة الاتحادية يوم الخميس تنفيذ عملية في بلدية الديوانية "
            "بنحو ثلاثين أمر قبض وتحرٍ. وشملت الأوامر مدير البلدية الحالي وخمسة من "
            "مديريها السابقين وستة من موظفي الحسابات والتدقيق ومدير حسابات المحافظة "
            "وخمسة عشر موظفاً وثلاثة مقاولين. وقالت الهيئة إنها ضبطت مستندات صرف "
            "تجاوزت تسعة مليارات دينار، وتحدثت عن قوائم أسعار مبالغ فيها ووثائق أعمال "
            "وهمية. وأُحيلت القضايا إلى قضاة تحقيق مختصين بجرائم النزاهة. "
            "فشكد صار على آخر تصليح بشارعكم؟"
        ),
        "endQuestion": "شكد صار على آخر تصليح بشارعكم؟",
        "sourcesLine": "المصادر: هيئة النزاهة الاتحادية · 964",
        "statPops": [
            {"value": "9 مليارات", "label": "مستندات صرف مضبوطة", "matchWord": "تسعة"},
            {"value": "30", "label": "أمر قبض وتحرٍ", "matchWord": "ثلاثين"},
        ],
    },
    "caption": """فساد بلدية الديوانية — 9 مليارات دينار مستندات صرف

هيئة النزاهة تعلن نحو 30 أمر قبض وتحرٍ، بينهم المدير الحالي و5 سابقون.

شكد صار على آخر تصليح بشارعكم؟

المصادر: هيئة النزاهة الاتحادية، 964
#العراق #الديوانية #فساد #النزاهة
@photonect.news
""",
}

# ───────────────────────────── 2 · DOLLAR CITY SPREAD (P1, ANCHOR 19:45) ──────
SLUGS[S2] = {
    "props": {
        "dateLabel": DATE_LABEL,
        "arabicDateLabel": ARABIC_DATE,
        "handle": "@photonect.news",
        "audioBed": "audio/mood_cinematic.mp3",
        "topicBucket": "iraq_domestic",
        "variant": "B",
        "breaking": {
            "arabicKicker": "دولار · سوق",
            "arabicHeadline": "نفس 100 دولار… وثلاثة أسعار بثلاث مدن",
            "englishSubhead": "BAGHDAD SELLS $100 AT 150,750 IQD ON 30 JULY, ERBIL AND BASRA AT 150,500 — OFFICIAL RATE 130,000",
            "heroMedia": img(S2, "hero.jpg"),
            "heroMediaType": "image",
        },
        "beats": [
            beat(
                "ماذا يحدث؟",
                "بغداد الأغلى: بيع 150,750 لكل 100 دولار",
                "بورصة بغداد سجّلت صباح الخميس بيع 150,750 ديناراً لكل 100 دولار وشراء 150,500، بحسب 964.",
                "150,750", "Baghdad selling price for $100",
                "سعر بيع 100 دولار في بورصة بغداد صباح الخميس 30 تموز 2026، مقابل سعر شراء 150,500 دينار (964)",
                [("بغداد بيع", "150,750"), ("بغداد شراء", "150,500"), ("الفرق", "250")],
                S2, "broll_1.jpg", "#FFC217",
            ),
            beat(
                "لماذا يهم؟",
                "أربيل والبصرة أرخص… البصرة تشتري بـ150,000",
                "أربيل بيع 150,500 وشراء 150,250، والبصرة بيع 150,500 وشراء 150,000، أي أن أرخص سعر شراء اليوم في البصرة، بحسب 964.",
                "150,000", "Basra buying price for $100",
                "سعر شراء 100 دولار في بورصة البصرة صباح الخميس 30 تموز 2026، وهو الأدنى بين المدن الثلاث في الجدول نفسه (964)",
                [("أربيل بيع", "150,500"), ("البصرة بيع", "150,500"), ("البصرة شراء", "150,000")],
                S2, "broll_2.jpg", "#4CC9F0",
            ),
            beat(
                "ماذا بعد؟",
                "والسعر الرسمي؟ 130,000 فقط",
                "السعر الرسمي المقرر من البنك المركزي 130,000 دينار لكل 100 دولار، أي فارق 20,750 ديناراً عن سعر بيع بغداد، بحسب 964.",
                "20,750", "IQD gap vs the official rate",
                "الفارق بين سعر بيع 100 دولار في بورصة بغداد (150,750) والسعر الرسمي المقرر من البنك المركزي (130,000) صباح الخميس 30 تموز 2026 (964)",
                [("السعر الرسمي", "130,000"), ("بغداد بيع", "150,750"), ("الفارق", "20,750")],
                S2, "broll_3.jpg", "#D72638",
            ),
        ],
        "sources": [
            {"name": "964media", "domain": "964media.com"},
            {"name": "Central Bank of Iraq", "domain": "cbi.iq"},
        ],
        "arabicTicker": [
            "بورصة بغداد صباح الخميس 30 تموز 2026: بيع 150,750 ديناراً وشراء 150,500 لكل 100 دولار (964)",
            "أربيل: بيع 150,500 ديناراً وشراء 150,250 لكل 100 دولار (964)",
            "البصرة: بيع 150,500 ديناراً وشراء 150,000 لكل 100 دولار (964)",
            "أرخص سعر شراء في الجدول اليوم كان في البصرة عند 150,000 دينار (964)",
            "السعر الرسمي المقرر من البنك المركزي 130,000 دينار لكل 100 دولار (964)",
            "الفارق بين سعر بيع بغداد والسعر الرسمي 20,750 ديناراً لكل 100 دولار (964)",
            "شكد دفعت لآخر مئة دولار اشتريتها؟",
        ],
    },
    "v11": {
        "kicker": "دولار",
        "hookHeadline": "بيش الدولار اليوم؟ يعتمد وين تكون",
        "voText": (
            "سجّلت بورصة بغداد صباح الخميس سعر بيع مئة وخمسين ألفاً وسبعمئة وخمسين "
            "ديناراً لكل مئة دولار، وسعر شراء مئة وخمسين ألفاً وخمسمئة. وفي أربيل بلغ "
            "سعر البيع مئة وخمسين ألفاً وخمسمئة، وفي البصرة السعر نفسه مع شراء مئة "
            "وخمسين ألفاً، وهو الأدنى في الجدول. أما السعر الرسمي المقرر من البنك "
            "المركزي فهو مئة وثلاثون ألف دينار، أي فارق عشرين ألفاً وسبعمئة وخمسين "
            "ديناراً عن سعر بغداد. فشكد دفعت لآخر مئة دولار اشتريتها؟"
        ),
        "endQuestion": "شكد دفعت لآخر مئة دولار اشتريتها؟",
        "sourcesLine": "المصادر: 964 · البنك المركزي العراقي",
        "statPops": [
            {"value": "150,750", "label": "بيع بغداد اليوم", "matchWord": "وسبعمئة"},
            {"value": "20,750", "label": "الفارق عن السعر الرسمي", "matchWord": "عشرين"},
        ],
    },
    "caption": """سعر الدولار اليوم في العراق — ثلاث مدن وثلاثة أسعار

بغداد الأغلى، والبصرة الأرخص، والسعر الرسمي بعيد عن الاثنين.

شكد دفعت لآخر مئة دولار اشتريتها؟

المصادر: 964، البنك المركزي العراقي
#العراق #الدولار #سعر_الصرف #الدينار_العراقي
@photonect.news
""",
}

# ─────────────────────────────── 3 · HEATWAVE (P3, 21:15) ─────────────────────
SLUGS[S3] = {
    "props": {
        "dateLabel": DATE_LABEL,
        "arabicDateLabel": ARABIC_DATE,
        "handle": "@photonect.news",
        "audioBed": "audio/mood_orchestral.mp3",
        "topicBucket": "wildcard",
        "variant": "C",
        "breaking": {
            "arabicKicker": "أنواء · حرارة",
            "arabicHeadline": "48 بميسان اليوم… و50 متوقعة السبت",
            "englishSubhead": "IRAQI MET OFFICE: 48C IN MAYSAN AS TEMPERATURES CLIMB AGAIN, 50C FORECAST FOR PARTS OF CENTRE AND SOUTH ON SATURDAY",
            "heroMedia": img(S3, "hero.jpg"),
            "heroMediaType": "image",
        },
        "beats": [
            beat(
                "ماذا يحدث؟",
                "ميسان 48… والحرارة ترتفع من جديد",
                "الهيئة العامة للأنواء الجوية والرصد الزلزالي سجّلت 48 درجة في ميسان، بعد أيام أقل حرارة، بحسب 964.",
                "48°", "Maysan, the day's high",
                "أعلى درجة حرارة سجّلتها الهيئة العامة للأنواء الجوية والرصد الزلزالي في ميسان، بعد عدة أيام أقل حرارة (الأنواء الجوية · 964)",
                [("ميسان", "48°"), ("البصرة", "47°"), ("بغداد", "46°")],
                S3, "broll_1.jpg", "#D72638",
            ),
            beat(
                "لماذا يهم؟",
                "من 44 بدهوك إلى 48 بميسان بنفس اليوم",
                "47 في كركوك ونينوى وواسط والبصرة وذي قار، و46 في بغداد وأربيل وبابل والديوانية، و45 في السليمانية وكربلاء والنجف، و44 في دهوك والأنبار.",
                "44°→48°", "the spread across Iraq on one day",
                "الفارق بين أدنى وأعلى درجة حرارة في جدول الأنواء الجوية لليوم نفسه: 44 درجة في دهوك والأنبار و48 في ميسان (الأنواء الجوية · 964)",
                [("كركوك ونينوى", "47°"), ("كربلاء والنجف", "45°"), ("دهوك والأنبار", "44°")],
                S3, "broll_2.jpg", "#FFC217",
            ),
            beat(
                "ماذا بعد؟",
                "الهيئة تتوقع 50 درجة يوم السبت",
                "الهيئة تتوقع وصول الحرارة إلى 50 درجة في أجزاء من الوسط والجنوب يوم السبت، بحسب 964.",
                "50°", "forecast for Saturday",
                "الحرارة التي تتوقعها الهيئة العامة للأنواء الجوية والرصد الزلزالي في أجزاء من وسط وجنوب العراق يوم السبت (الأنواء الجوية · 964)",
                [("متوقعة السبت", "50°"), ("المناطق", "الوسط والجنوب"), ("اليوم بميسان", "48°")],
                S3, "broll_3.jpg", "#4CC9F0",
            ),
        ],
        "sources": [
            {"name": "Iraqi Meteorological Organization", "domain": "meteoseism.gov.iq"},
            {"name": "964media", "domain": "964media.com"},
        ],
        "arabicTicker": [
            "الهيئة العامة للأنواء الجوية والرصد الزلزالي: الحرارة ترتفع في معظم مناطق العراق بعد أيام أقل حرارة (964)",
            "ميسان سجّلت 48 درجة، وهي الأعلى في جدول الهيئة (964)",
            "كركوك ونينوى وواسط والبصرة وذي قار: 47 درجة (964)",
            "بغداد وأربيل وديالى وصلاح الدين وبابل والديوانية والمثنى: 46 درجة (964)",
            "السليمانية وكربلاء والنجف: 45 درجة، ودهوك والأنبار: 44 درجة (964)",
            "الهيئة تتوقع 50 درجة في أجزاء من الوسط والجنوب يوم السبت (964)",
            "شكد وصلت الحرارة بمنطقتك اليوم؟",
        ],
    },
    "v11": {
        "kicker": "أنواء",
        "hookHeadline": "48 اليوم… و50 يوم السبت",
        "voText": (
            "أعلنت الهيئة العامة للأنواء الجوية والرصد الزلزالي ارتفاع درجات الحرارة "
            "في معظم مناطق العراق بعد أيام أقل حرارة. وبلغت الحرارة ثمانياً وأربعين "
            "درجة في ميسان، وسبعاً وأربعين في كركوك ونينوى وواسط والبصرة وذي قار، "
            "وستاً وأربعين في بغداد وأربيل وبابل والديوانية، وأربعاً وأربعين في دهوك "
            "والأنبار. وتتوقع الهيئة أن تصل الحرارة إلى خمسين درجة في أجزاء من الوسط "
            "والجنوب يوم السبت. فشكد وصلت الحرارة بمنطقتك اليوم؟"
        ),
        "endQuestion": "شكد وصلت الحرارة بمنطقتك اليوم؟",
        "sourcesLine": "المصادر: الأنواء الجوية · 964",
        "statPops": [
            {"value": "48°", "label": "ميسان اليوم", "matchWord": "ثمانياً"},
            {"value": "50°", "label": "متوقعة السبت", "matchWord": "خمسين"},
        ],
    },
    "caption": """درجات الحرارة في العراق اليوم — 48 بميسان و50 متوقعة السبت

الأنواء الجوية تسجّل ارتفاعاً بمعظم المناطق، والفارق بين المحافظات 4 درجات.

شكد وصلت الحرارة بمنطقتك اليوم؟

المصادر: الأنواء الجوية، 964
#العراق #الطقس #موجة_حر #الأنواء_الجوية
@photonect.news
""",
}

# ──────────────────────── 4 · BORROWING LAW / SALARIES (P1, 22:30) ────────────
SLUGS[S4] = {
    "props": {
        "dateLabel": DATE_LABEL,
        "arabicDateLabel": ARABIC_DATE,
        "handle": "@photonect.news",
        "audioBed": "audio/mood_mideast.mp3",
        "topicBucket": "iraq_domestic",
        "variant": "A",
        "breaking": {
            "arabicKicker": "رواتب · اقتراض",
            "arabicHeadline": "بلا موازنة… والحل قانون اقتراض بلا سقف",
            "englishSubhead": "GOVERNMENT PUSHES 2026 BORROWING LAW WITH NO FIXED CEILING TO COVER SALARIES; INITIAL ESTIMATES 10-15TN IQD",
            "heroMedia": img(S4, "hero.jpg"),
            "heroMediaType": "image",
        },
        "beats": [
            beat(
                "ماذا يحدث؟",
                "مسار الراتب صار أطول وأعقد",
                "مصادر في وزارة المالية قالت لـ964 إن صرف الرواتب تأخّر بعد أن أصبح مسار الأموال يمرّ بترتيبات مصرفية ومراسلات أكثر تعقيداً من السابق.",
                "0", "federal budget laws for 2026",
                "العراق يدخل عام 2026 دون قانون موازنة اتحادية، وهو ما دفع الحكومة والبرلمان إلى البحث عن غطاء قانوني بديل للاستدانة (964 · وكالة بغداد اليوم)",
                [("موازنة 2026", "لا يوجد"), ("مصدر التصريح", "وزارة المالية"), ("النتيجة", "تأخر الصرف")],
                S4, "broll_1.jpg", "#FFC217",
            ),
            beat(
                "لماذا يهم؟",
                "قانون لا يحدد سقفاً… يرفع القيود",
                "الحكومة تدفع البرلمان لتشريع قانون الاقتراض والمنح لسنة 2026، وهو لا يحدد سقفاً ثابتاً للاقتراض بل يرفع القيود القانونية، بحسب 964.",
                "10-15", "trillion IQD — initial estimates only",
                "تقديرات أولية نقلتها 964 عن مصادر في وزارة المالية لحجم ما قد تسعى الحكومة لاقتراضه من مصادر داخلية وخارجية، وليست رقماً مثبتاً في القانون (964)",
                [("تقديرات أولية", "10-15 تريليون"), ("السقف بالقانون", "غير محدد"), ("المصادر", "داخلية وخارجية")],
                S4, "broll_2.jpg", "#D72638",
            ),
            beat(
                "ماذا بعد؟",
                "رئيس المالية النيابية: نتّجه للتشريع",
                "رئيس اللجنة المالية النيابية عدي عواد قال إن اللجنة والبرلمان يتّجهان لتشريع القانون بسبب غياب الموازنة، وإن الاقتراض الداخلي من البنك المركزي والخارجي من دول أو البنك الدولي.",
                "2026", "the borrowing and grants law year",
                "قانون الاقتراض والمنح لسنة 2026 الذي قال رئيس اللجنة المالية النيابية عدي عواد إن البرلمان يتّجه لتشريعه بسبب غياب الموازنة، بعد مناقشته مع وزير المالية فالح الساري (وكالة بغداد اليوم)",
                [("الاقتراض الداخلي", "البنك المركزي"), ("الخارجي", "دول والبنك الدولي"), ("الغاية", "ضمان الرواتب")],
                S4, "broll_3.jpg", "#4CC9F0",
            ),
        ],
        "sources": [
            {"name": "964media", "domain": "964media.com"},
            {"name": "Baghdad Today", "domain": "baghdadtoday.news"},
        ],
        "arabicTicker": [
            "مصادر في وزارة المالية لـ964: صرف الرواتب تأخّر بعد أن أصبح مسار الأموال يمرّ بترتيبات مصرفية ومراسلات أكثر تعقيداً (964)",
            "الحكومة تدفع البرلمان لتشريع قانون الاقتراض والمنح لسنة 2026 لتوفير غطاء قانوني للاستدانة (964)",
            "القانون لا يحدد سقفاً ثابتاً للاقتراض، بل يرفع القيود القانونية أمام الحكومة (964)",
            "تقديرات أولية تشير إلى أن الحكومة قد تسعى لاقتراض 10 إلى 15 تريليون دينار من مصادر داخلية وخارجية (964)",
            "رئيس اللجنة المالية النيابية عدي عواد: اللجنة والبرلمان يتّجهان للتشريع بسبب غياب الموازنة (وكالة بغداد اليوم)",
            "عواد: الاقتراض الداخلي من البنك المركزي والخارجي من دول أو البنك الدولي، بعد مناقشة المقترح مع وزير المالية فالح الساري (وكالة بغداد اليوم)",
            "راتبك وصل بموعده هذا الشهر لو تأخر؟",
        ],
    },
    "v11": {
        "kicker": "رواتب",
        "hookHeadline": "راتبك ممول بقرض؟",
        "voText": (
            "قالت مصادر في وزارة المالية إن صرف الرواتب تأخّر بعد أن أصبح مسار الأموال "
            "يمرّ بترتيبات مصرفية ومراسلات أكثر تعقيداً من السابق. وتدفع الحكومة "
            "البرلمان إلى تشريع قانون الاقتراض والمنح لسنة ألفين وستة وعشرين لتوفير "
            "غطاء قانوني للاستدانة، وهو قانون لا يحدد سقفاً ثابتاً بل يرفع القيود. "
            "وتشير تقديرات أولية إلى عشرة إلى خمسة عشر تريليون دينار. وقال رئيس اللجنة "
            "المالية النيابية عدي عواد إن البرلمان يتّجه للتشريع بسبب غياب الموازنة. "
            "فراتبك وصل بموعده هذا الشهر لو تأخر؟"
        ),
        "endQuestion": "راتبك وصل بموعده هذا الشهر لو تأخر؟",
        "sourcesLine": "المصادر: 964 · وكالة بغداد اليوم",
        "statPops": [
            {"value": "10-15 تريليون", "label": "تقديرات أولية للاقتراض", "matchWord": "تريليون"},
            {"value": "لا سقف", "label": "القانون لا يحدد سقفاً", "matchWord": "سقفاً"},
        ],
    },
    "caption": """الرواتب وقانون الاقتراض في العراق — بلا موازنة لسنة 2026

مسار الأموال صار أعقد، والحكومة تريد غطاءً قانونياً للاستدانة.

راتبك وصل بموعده هذا الشهر لو تأخر؟

المصادر: 964، وكالة بغداد اليوم
#العراق #الرواتب #الموازنة #اقتصاد
@photonect.news
""",
}

# ───────────────── 5 · OIL PRICE + SHIPPING REROUTE (P2, V10 CONTROL 23:45) ───
SLUGS[S5] = {
    "props": {
        "dateLabel": DATE_LABEL,
        "arabicDateLabel": ARABIC_DATE,
        "handle": "@photonect.news",
        "audioBed": "audio/mood_newsroom.mp3",
        "topicBucket": "mena_geopolitics",
        "variant": "B",
        "breaking": {
            "arabicKicker": "نفط · شحن",
            "arabicHeadline": "برنت 89.45 دولاراً… بعد قفزة 7.91%",
            "englishSubhead": "BRENT SLIPS 1.42% TO $89.45 AFTER PREVIOUS SESSION'S 7.91% SURGE; 39 SHIPS CROSS BAB AL-MANDAB AS HORMUZ TRAFFIC STAYS MINIMAL",
            "heroMedia": img(S5, "hero.jpg"),
            "heroMediaType": "image",
        },
        "beats": [
            beat(
                "ماذا يحدث؟",
                "برنت يتراجع 1.42% إلى 89.45 دولاراً",
                "برنت تراجع 1.29 دولاراً أي 1.42% إلى 89.45 دولاراً للبرميل، والخام الأمريكي 0.56 دولاراً أي 0.66% إلى 83.90، بحسب رويترز.",
                "$89.45", "Brent per barrel",
                "سعر خام برنت للبرميل بعد تراجعه 1.29 دولاراً أي 1.42% في الجلسة، بحسب رويترز نقلاً عن 964",
                [("برنت", "$89.45"), ("الخام الأمريكي", "$83.90"), ("تراجع برنت", "-1.42%")],
                S5, "broll_1.jpg", "#FFC217",
            ),
            beat(
                "لماذا يهم؟",
                "الجلسة السابقة كانت +7.91%",
                "الجلسة السابقة شهدت صعود برنت 7.91% والخام الأمريكي 6.56%، بعد ضربات أمريكية وسعودية على منشآت قالت الروايات إنها تُستخدم من جماعات مدعومة من إيران في العراق.",
                "+7.91%", "Brent's previous-session surge",
                "نسبة صعود خام برنت في الجلسة السابقة قبل تراجعه، مقابل 6.56% للخام الأمريكي، بحسب رويترز نقلاً عن 964",
                [("صعود برنت", "+7.91%"), ("صعود الأمريكي", "+6.56%"), ("ثم تراجع", "-1.42%")],
                S5, "broll_2.jpg", "#D72638",
            ),
            beat(
                "ماذا بعد؟",
                "39 سفينة عبرت باب المندب… وهرمز شبه فارغ",
                "39 سفينة شحن عبرت باب المندب الثلاثاء، الأعلى منذ 19 تموز، مقابل حركة ضعيفة في مضيق هرمز، بحسب رويترز.",
                "39", "ships through Bab al-Mandab Tuesday",
                "عدد سفن الشحن التي عبرت مضيق باب المندب يوم الثلاثاء، وهو الأعلى منذ 19 تموز، مقابل حركة ضعيفة في مضيق هرمز (رويترز · 964)",
                [("باب المندب", "39 سفينة"), ("الأعلى منذ", "19 تموز"), ("هرمز", "حركة ضعيفة")],
                S5, "broll_3.jpg", "#4CC9F0",
            ),
        ],
        "sources": [
            {"name": "Reuters", "domain": "reuters.com"},
            {"name": "964media", "domain": "964media.com"},
        ],
        "arabicTicker": [
            "خام برنت تراجع 1.29 دولاراً أي 1.42% إلى 89.45 دولاراً للبرميل (رويترز · 964)",
            "الخام الأمريكي تراجع 0.56 دولاراً أي 0.66% إلى 83.90 دولاراً للبرميل (رويترز · 964)",
            "الجلسة السابقة شهدت صعود برنت 7.91% والخام الأمريكي 6.56% (رويترز · 964)",
            "الصعود جاء بعد ضربات أمريكية وسعودية على منشآت قيل إنها تُستخدم من جماعات مدعومة من إيران في العراق (رويترز · 964)",
            "39 سفينة شحن عبرت مضيق باب المندب الثلاثاء، الأعلى منذ 19 تموز 2026 (رويترز · 964)",
            "حركة الملاحة في مضيق هرمز بقيت ضعيفة، مع اتجاه الصادرات إلى مسارات بديلة (رويترز · 964)",
            "شكد أثّر سعر النفط على أسعار السوق بمنطقتك؟",
        ],
    },
    "caption": """أسعار النفط اليوم — برنت 89.45 دولاراً بعد قفزة 7.91%

السعر يتراجع، والسفن تختار باب المندب بدلاً من هرمز.

شكد غلت أسعار السوق بمنطقتك هذا الأسبوع؟

المصادر: رويترز، 964
#العراق #النفط #برنت #اقتصاد
@photonect.news
""",
}


def main() -> int:
    for slug, cfg in SLUGS.items():
        d = POSTS / slug / ".meta"
        d.mkdir(parents=True, exist_ok=True)
        (d / "props.json").write_text(
            json.dumps(cfg["props"], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        (POSTS / slug / "caption.txt").write_text(cfg["caption"], encoding="utf-8")
        (d / "media-stamp.json").write_text(
            json.dumps(STAMP, ensure_ascii=False) + "\n", encoding="utf-8")
        if cfg.get("v11"):
            v = dict(cfg["v11"])
            v["slug"] = slug
            v["images"] = [img(slug, n) for n in
                           ("hero.jpg", "broll_1.jpg", "broll_2.jpg", "broll_3.jpg")]
            v["audioBed"] = cfg["props"]["audioBed"]
            ordered = {k: v[k] for k in
                       ("slug", "kicker", "hookHeadline", "voText", "endQuestion",
                        "sourcesLine", "images", "audioBed", "statPops")}
            (d / "v11-brief.json").write_text(
                json.dumps(ordered, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"  ✓ {slug}  ({'V11' if cfg.get('v11') else 'V10.1 control'})")
    print(f"\n== {len(SLUGS)} slugs written for {DATE} ==")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
