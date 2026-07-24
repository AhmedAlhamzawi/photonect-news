#!/usr/bin/env python3
"""Author the 2026-07-24 Photonect NEWS slate.

5 slugs (Iraq/MENA money-power lens). Posting order:
  1 graft-return-or-jail   P1 corruption/recovery  V11  A   (LEAD)
  2 iran-gas-oil-barter    P2 energy/power         V11  A
  3 money-printing-25tn    P1 money/dinar          V11  B
  4 gulf-swf-trillions     P2 gulf finance         V10  B   <- silent control (driest/abstract)
  5 water-heat-crisis      P3 climate-economy      V11  C

Directional shift vs 2026-07-23: pivots off arrest-COUNT corruption drama to the
money-SUPPLY / macro-plumbing lens (secret money-printing, oil-for-gas barter
economics, Gulf sovereign-fund contrast) + accountability-via-RECOVERY (amnesty
for returned funds, not arrest tallies) + a climate-economy C feature.

Writes per slug: .meta/props.json, caption.txt, .meta/media-stamp.json, and (for
the 4 voiced) .meta/v11-brief.json. Western numerals on-screen; voText spells
numbers in words (MSA newscast). No Persian yeh/kaf (grep-guarded after run).
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "data" / "posts"
DATE = "2026-07-24"
DATE_LABEL = "JUL 24 • 2026"
AR_DATE = "24 يوليو 2026"
HANDLE = "@photonect.news"
ACCENTS = ["#FFC217", "#FF6B3D", "#D72638"]
STAMP = {"hunted_at": f"{DATE}T11:00:00+00:00"}


def img(slug, n):
    return f"images/news/{slug}/{n}"


SLUGS = {}

# ─────────────────────────────────────────────────────────────────────────
# 1 — GRAFT: RETURN THE MONEY, LIGHTER SENTENCE  (P1 · V11 · A · LEAD)
# ─────────────────────────────────────────────────────────────────────────
s = f"{DATE}-graft-return-or-jail"
SLUGS[s] = {
    "bucket": "iraq_politics",
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/mood_newsroom.mp3", "topicBucket": "iraq_politics", "variant": "A",
        "breaking": {
            "arabicKicker": "فساد · محاسبة",
            "arabicHeadline": "القضاء: أعِد الأموال المنهوبة… تُخفَّف عقوبتك",
            "englishSubhead": "RETURN STOLEN FUNDS FOR A LIGHTER SENTENCE — JUDICIAL COUNCIL",
            "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
        },
        "beats": [
            {
                "label": "ماذا يحدث؟",
                "arabicHeading": "خارطة طريق لاسترداد الأموال",
                "arabicBody": "أعلن مجلس القضاء الأعلى، بالاتفاق مع رئيس الوزراء علي الزيدي، إعداد خارطة طريق لاسترداد أموال الدولة مقابل تخفيف الإجراءات القانونية بحق من يعيدها طوعاً، بحسب ذا ناشيونال.",
                "bigStat": {"value": "$100M+", "label": "Recovered so far",
                            "arabicLabel": "قيمة الأموال التي استُردت حتى الآن ضمن حملة صولة الفجر لمكافحة الفساد (ذا ناشيونال)"},
                "supportingStats": [{"label": "الجهة", "value": "مجلس القضاء"},
                                     {"label": "الآلية", "value": "إعادة طوعية"},
                                     {"label": "مسترد", "value": "$100 مليون+"}],
                "broll": img(s, "broll_1.jpg"), "brolls": [img(s, "broll_1.jpg")],
                "brollType": "image", "accent": ACCENTS[0], "brollSource": "The National · 2026",
            },
            {
                "label": "لماذا يهم؟",
                "arabicHeading": "الحملة أوقفت 47 مسؤولاً بينهم نواب",
                "arabicBody": "ضمن حملة صولة الفجر التي أطلقها الزيدي أواخر حزيران، أُوقف نحو 47 مسؤولاً بينهم نواب، فيما استُرد أكثر من 100 مليون دولار حتى الآن، بحسب ذا ناشيونال والجزيرة.",
                "bigStat": {"value": "47", "label": "Officials held incl. lawmakers",
                            "arabicLabel": "عدد المسؤولين الموقوفين في الحملة بينهم نواب منذ انطلاقها أواخر حزيران (ذا ناشيونال · الجزيرة)"},
                "supportingStats": [{"label": "موقوفون", "value": "47"},
                                     {"label": "منهم", "value": "نواب"},
                                     {"label": "الانطلاق", "value": "28 حزيران"}],
                "broll": img(s, "broll_2.jpg"), "brolls": [img(s, "broll_2.jpg")],
                "brollType": "image", "accent": ACCENTS[1], "brollSource": "Al Jazeera · 2026",
            },
            {
                "label": "ماذا بعد؟",
                "arabicHeading": "150 مليار دولار خسائر منذ 2003",
                "arabicBody": "تُقدَّر خسائر العراق من الفساد بنحو 150 مليار دولار منذ 2003 (تقدير الرئيس الأسبق برهم صالح)، وأبرز القضايا «سرقة القرن» بـ2.5 مليار دولار عام 2024، بحسب ذا ناشيونال.",
                "bigStat": {"value": "$150B", "label": "Lost to graft since 2003",
                            "arabicLabel": "التقدير الإجمالي لخسائر العراق من الفساد منذ عام 2003 وفق الرئيس الأسبق برهم صالح (ذا ناشيونال)"},
                "supportingStats": [{"label": "منذ 2003", "value": "$150 مليار"},
                                     {"label": "سرقة القرن", "value": "$2.5 مليار"},
                                     {"label": "العام", "value": "2024"}],
                "broll": img(s, "broll_3.jpg"), "brolls": [img(s, "broll_3.jpg")],
                "brollType": "image", "accent": ACCENTS[2], "brollSource": "The National · 2026",
            },
        ],
        "sources": [
            {"name": "The National", "domain": "thenationalnews.com"},
            {"name": "Supreme Judicial Council", "domain": "sjc.iq"},
            {"name": "Al Jazeera", "domain": "aljazeera.com"},
        ],
        "arabicTicker": [
            "مجلس القضاء الأعلى يعدّ خارطة طريق لاسترداد أموال الدولة مقابل تخفيف الإجراءات لمن يعيدها طوعاً (ذا ناشيونال)",
            "الخطوة بالاتفاق مع رئيس الوزراء علي الزيدي وضمن تعديل قانون العفو لعام 2025 (ذا ناشيونال)",
            "حملة صولة الفجر أوقفت نحو 47 مسؤولاً بينهم نواب منذ انطلاقها أواخر حزيران (ذا ناشيونال · الجزيرة)",
            "استُرد أكثر من 100 مليون دولار حتى الآن ضمن الحملة (ذا ناشيونال)",
            "تُقدَّر خسائر العراق من الفساد بنحو 150 مليار دولار منذ 2003 (تقدير برهم صالح)",
            "أبرز القضايا «سرقة القرن» بقيمة 2.5 مليار دولار عام 2024 (ذا ناشيونال)",
            "فهل يعيد هذا النهج المال إلى الخزينة، أم يفتح باباً للإفلات من العقاب؟",
        ],
    },
    "v11": {
        "slug": s, "kicker": "عاجل",
        "hookHeadline": "رجّع المسروق… وتخفّ العقوبة؟",
        "voText": "أعلن مجلس القضاء الأعلى في العراق، بالاتفاق مع رئيس الوزراء علي الزيدي، إعداد خارطة طريق لاسترداد أموال الدولة المنهوبة مقابل تخفيف الإجراءات القانونية بحق من يعيدها طوعاً، وذلك بحسب صحيفة ذا ناشيونال. وتأتي الخطوة ضمن حملة صولة الفجر التي انطلقت أواخر حزيران وأوقفت نحو سبعة وأربعين مسؤولاً بينهم نواب، فيما استُرد أكثر من مئة مليون دولار حتى الآن. وتُقدَّر خسائر العراق من الفساد بنحو مئة وخمسين مليار دولار منذ عام ألفين وثلاثة. فهل يعيد هذا النهج المال إلى الخزينة، أم يفتح باباً للإفلات من العقاب؟",
        "endQuestion": "هل يعيد المال إلى الخزينة، أم يفتح باب الإفلات من العقاب؟",
        "sourcesLine": "المصادر: ذا ناشيونال · مجلس القضاء الأعلى · الجزيرة",
        "images": [img(s, "hero.jpg"), img(s, "broll_1.jpg"), img(s, "broll_2.jpg"), img(s, "broll_3.jpg")],
        "audioBed": "audio/mood_newsroom.mp3",
        "statPops": [
            {"value": "$100 مليون", "label": "مستردة حتى الآن", "matchWord": "مليون"},
            {"value": "47 موقوفاً", "label": "بينهم نواب", "matchWord": "وأربعين"},
            {"value": "$150 مليار", "label": "خسائر منذ 2003", "matchWord": "مليار"},
        ],
    },
    "caption": """الفساد في العراق — رجّع الفلوس تنجو من العقوبة؟

مجلس القضاء يعدّ خطة لتخفيف العقوبة مقابل إعادة الأموال المنهوبة.

برأيك، محاسبة حقيقية لو باب للإفلات؟

المصادر: ذا ناشيونال، الجزيرة
#العراق #الفساد #صولة_الفجر #محاسبة
@photonect.news""",
}

# ─────────────────────────────────────────────────────────────────────────
# 2 — OIL-FOR-GAS BARTER WITH IRAN  (P2 · V11 · A)
# ─────────────────────────────────────────────────────────────────────────
s = f"{DATE}-iran-gas-oil-barter"
SLUGS[s] = {
    "bucket": "mena_geopolitics",
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/mood_cinematic.mp3", "topicBucket": "mena_geopolitics", "variant": "A",
        "breaking": {
            "arabicKicker": "طاقة · كهرباء",
            "arabicHeadline": "نفط مقابل غاز… العراق يبقي الكهرباء شغّالة",
            "englishSubhead": "OIL-FOR-GAS SWAP WITH IRAN TO KEEP THE LIGHTS ON",
            "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
        },
        "beats": [
            {
                "label": "ماذا يحدث؟",
                "arabicHeading": "اتفاق يدفع الغاز بالنفط",
                "arabicBody": "وقّع العراق وإيران في 11 تموز اتفاقاً يسمح لبغداد بدفع ثمن الغاز الإيراني المستورد عبر تحويلات نفطية، لتأمين الكهرباء وتفادي العقوبات الأميركية، بحسب معهد واشنطن.",
                "bigStat": {"value": "11 تموز", "label": "Oil-for-gas deal signed",
                            "arabicLabel": "تاريخ توقيع اتفاق مبادلة الغاز الإيراني بتحويلات نفطية لتفادي العقوبات الأميركية (معهد واشنطن)"},
                "supportingStats": [{"label": "الطرفان", "value": "بغداد·طهران"},
                                     {"label": "الآلية", "value": "نفط ↔ غاز"},
                                     {"label": "الهدف", "value": "تفادي العقوبات"}],
                "broll": img(s, "broll_1.jpg"), "brolls": [img(s, "broll_1.jpg")],
                "brollType": "image", "accent": ACCENTS[0], "brollSource": "Washington Institute · 2026",
            },
            {
                "label": "لماذا يهم؟",
                "arabicHeading": "الإمداد نصف الحاجة… والمحطات تختنق",
                "arabicBody": "منذ مطلع أيار تراوح الإمداد الإيراني بين 15 و20 مليون متر مكعب يومياً، أي أقل من نحو 50 مليوناً يحتاجها العراق لتشغيل محطاته الغازية، بحسب معهد واشنطن.",
                "bigStat": {"value": "50 م.م³", "label": "Daily gas Iraq needs",
                            "arabicLabel": "حجم الغاز اليومي الذي يحتاجه العراق لتشغيل محطاته مقابل إمداد فعلي بين 15 و20 مليون متر مكعب (معهد واشنطن)"},
                "supportingStats": [{"label": "المطلوب", "value": "50 م.م³"},
                                     {"label": "المورَّد", "value": "15-20 م.م³"},
                                     {"label": "منذ", "value": "أيار"}],
                "broll": img(s, "broll_2.jpg"), "brolls": [img(s, "broll_2.jpg")],
                "brollType": "image", "accent": ACCENTS[1], "brollSource": "Washington Institute · 2026",
            },
            {
                "label": "ماذا بعد؟",
                "arabicHeading": "بدائل: تراخيص وربط خليجي وسيمنس",
                "arabicBody": "يتّجه العراق إلى بدائل: جولة تراخيص غازية سادسة، وربط الشبكة بالأردن ودول الخليج، والاستعانة بشركة سيمنس لرفع إنتاج التوربينات، بحسب معهد واشنطن.",
                "bigStat": {"value": "6", "label": "Gas licensing round",
                            "arabicLabel": "الجولة السادسة لتراخيص حقول الغاز ضمن مساعي العراق لتنويع مصادر الطاقة وتقليل الاعتماد على إيران (معهد واشنطن)"},
                "supportingStats": [{"label": "تراخيص", "value": "الجولة 6"},
                                     {"label": "ربط", "value": "الأردن·الخليج"},
                                     {"label": "توربينات", "value": "سيمنس"}],
                "broll": img(s, "broll_3.jpg"), "brolls": [img(s, "broll_3.jpg")],
                "brollType": "image", "accent": ACCENTS[2], "brollSource": "Washington Institute · 2026",
            },
        ],
        "sources": [
            {"name": "Washington Institute", "domain": "washingtoninstitute.org"},
            {"name": "Oil & Gas 360", "domain": "oilandgas360.com"},
            {"name": "Middle East Online", "domain": "middle-east-online.com"},
        ],
        "arabicTicker": [
            "العراق وإيران يوقّعان في 11 تموز اتفاق مبادلة الغاز المستورد بتحويلات نفطية (معهد واشنطن)",
            "الهدف تأمين الكهرباء صيفاً وتفادي الوقوع تحت طائلة العقوبات الأميركية (معهد واشنطن)",
            "الإمداد الإيراني يتراوح بين 15 و20 مليون متر مكعب يومياً منذ مطلع أيار (معهد واشنطن)",
            "العراق يحتاج نحو 50 مليون متر مكعب يومياً لتشغيل محطاته الغازية (معهد واشنطن)",
            "بغداد تطلق جولة تراخيص غازية سادسة وتغيّر نموذج عقود النفط (معهد واشنطن)",
            "خطط لربط الشبكة الكهربائية بالأردن ودول الخليج والاستعانة بسيمنس لرفع إنتاج التوربينات (معهد واشنطن)",
            "فهل ينجح العراق في الاستغناء عن الغاز الإيراني، أم يبقى رهيناً له صيفاً بعد صيف؟",
        ],
    },
    "v11": {
        "slug": s, "kicker": "عاجل",
        "hookHeadline": "نفط مقابل غاز… تكييفك ينطفي؟",
        "voText": "وقّع العراق وإيران في الحادي عشر من تموز اتفاقاً يسمح لبغداد بدفع ثمن الغاز الإيراني المستورد عبر تحويلات نفطية، في خطوة تهدف إلى تأمين الكهرباء وتفادي العقوبات الأميركية، وذلك بحسب معهد واشنطن. ومنذ مطلع أيار تراوح الإمداد الإيراني بين خمسة عشر وعشرين مليون متر مكعب يومياً، أي أقل بكثير من نحو خمسين مليوناً يحتاجها العراق لتشغيل محطاته الغازية. وفي المقابل يتّجه العراق إلى بدائل، من جولة تراخيص غازية سادسة إلى ربط شبكته بالأردن ودول الخليج والاستعانة بشركة سيمنس. فهل ينجح العراق في الاستغناء عن الغاز الإيراني، أم يبقى رهيناً له صيفاً بعد صيف؟",
        "endQuestion": "هل يستغني العراق عن الغاز الإيراني، أم يبقى رهيناً له؟",
        "sourcesLine": "المصادر: معهد واشنطن · Oil&Gas360 · ميدل إيست أونلاين",
        "images": [img(s, "hero.jpg"), img(s, "broll_1.jpg"), img(s, "broll_2.jpg"), img(s, "broll_3.jpg")],
        "audioBed": "audio/mood_cinematic.mp3",
        "statPops": [
            {"value": "50 م.م³", "label": "الحاجة اليومية", "matchWord": "خمسين"},
            {"value": "15-20 م.م³", "label": "المورَّد فعلياً", "matchWord": "وعشرين"},
            {"value": "11 تموز", "label": "توقيع الاتفاق", "matchWord": "عشر"},
        ],
    },
    "caption": """كهرباء العراق والغاز الإيراني — شنو صار بصيف 2026؟

اتفاق «نفط مقابل غاز» مع إيران لتفادي العقوبات وتشغيل المحطات.

برأيك، يقدر العراق يستغني عن الغاز الإيراني؟

المصادر: معهد واشنطن، Oil&Gas360
#العراق #كهرباء #الطاقة #إيران
@photonect.news""",
}

# ─────────────────────────────────────────────────────────────────────────
# 3 — STATE PRINTED 25 TRILLION DINARS  (P1 · V11 · B)
# ─────────────────────────────────────────────────────────────────────────
s = f"{DATE}-money-printing-25tn"
SLUGS[s] = {
    "bucket": "iraq_politics",
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/mood_orchestral.mp3", "topicBucket": "iraq_politics", "variant": "B",
        "breaking": {
            "arabicKicker": "مال · دينار",
            "arabicHeadline": "العراق طبع 25 تريليون دينار… والمركزي صامت",
            "englishSubhead": "STATE PRINTED 25 TRILLION DINARS — CENTRAL BANK STAYED SILENT",
            "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
        },
        "beats": [
            {
                "label": "ماذا يحدث؟",
                "arabicHeading": "طبع نقود لمواجهة شحّ السيولة",
                "arabicBody": "قال وزير الخارجية فؤاد حسين إن الدولة لجأت إلى طبع 25 تريليون دينار لمواجهة شحّ حادّ في السيولة، مؤكداً أن البنك المركزي لم يعلن الخطوة، بحسب أخبار العراق.",
                "bigStat": {"value": "25 تريليون", "label": "Dinars printed",
                            "arabicLabel": "حجم النقد الذي طُبع لمواجهة شحّ السيولة بحسب تصريح وزير الخارجية فؤاد حسين، دون إعلان من البنك المركزي (أخبار العراق)"},
                "supportingStats": [{"label": "المصدر", "value": "فؤاد حسين"},
                                     {"label": "طُبع", "value": "25 تريليون"},
                                     {"label": "المركزي", "value": "لم يعلن"}],
                "broll": img(s, "broll_1.jpg"), "brolls": [img(s, "broll_1.jpg")],
                "brollType": "image", "accent": ACCENTS[0], "brollSource": "Iraqi News · 2026",
            },
            {
                "label": "لماذا يهم؟",
                "arabicHeading": "القدرة النقدية ترتفع إلى 125 تريليوناً",
                "arabicBody": "رفع الطبع القدرة النقدية الاسمية إلى 125 تريليون دينار من نحو 100 إلى 104 تريليونات، بينما يحتاج «اقتصاد الرواتب» وحده إلى نحو 9 تريليونات دينار شهرياً، بحسب الخبير محمود داغر.",
                "bigStat": {"value": "9 تريليون", "label": "Monthly salary bill (IQD)",
                            "arabicLabel": "الكلفة الشهرية لاقتصاد الرواتب وحده بالدينار العراقي وفق الخبير المالي محمود داغر (أخبار العراق)"},
                "supportingStats": [{"label": "القدرة", "value": "125 تريليون"},
                                     {"label": "قبل", "value": "100-104"},
                                     {"label": "الرواتب/شهر", "value": "9 تريليون"}],
                "broll": img(s, "broll_2.jpg"), "brolls": [img(s, "broll_2.jpg")],
                "brollType": "image", "accent": ACCENTS[1], "brollSource": "Iraqi News · Shafaq · 2026",
            },
            {
                "label": "ماذا بعد؟",
                "arabicHeading": "بلا موازنة 2026… واعتماد على القروض",
                "arabicBody": "مع تعذّر إقرار موازنة 2026، يتجاوزها العراق نحو 2027 معتمداً على القروض وتدخلات المركزي لتأمين الرواتب، بحسب لجنة المالية النيابية وشفق نيوز.",
                "bigStat": {"value": "2026", "label": "Budget bypassed",
                            "arabicLabel": "موازنة العراق الاتحادية لعام 2026 التي بات إقرارها متعذّراً مع التوجه نحو 2027 والاعتماد على القروض (لجنة المالية النيابية · شفق نيوز)"},
                "supportingStats": [{"label": "موازنة 2026", "value": "متعذّرة"},
                                     {"label": "البديل", "value": "قروض"},
                                     {"label": "الأفق", "value": "2027"}],
                "broll": img(s, "broll_3.jpg"), "brolls": [img(s, "broll_3.jpg")],
                "brollType": "image", "accent": ACCENTS[2], "brollSource": "Shafaq News · 2026",
            },
        ],
        "sources": [
            {"name": "Iraqi News", "domain": "iraqinews.com"},
            {"name": "Shafaq News", "domain": "shafaq.com"},
            {"name": "Hatha Alyoum", "domain": "hathalyoum.net"},
        ],
        "arabicTicker": [
            "وزير الخارجية فؤاد حسين: الدولة لجأت إلى طبع 25 تريليون دينار لمواجهة شحّ السيولة (أخبار العراق)",
            "حسين يؤكد أن البنك المركزي العراقي لم يعلن خطوة الطبع (أخبار العراق)",
            "الطبع رفع القدرة النقدية الاسمية إلى 125 تريليون دينار من نحو 100 إلى 104 تريليونات (أخبار العراق)",
            "الخبير محمود داغر: اقتصاد الرواتب وحده يحتاج نحو 9 تريليونات دينار شهرياً (أخبار العراق)",
            "لجنة المالية النيابية: إقرار موازنة 2026 بات متعذّراً والتوجه نحو موازنة 2027 (شفق نيوز)",
            "العراق يعتمد على القروض وتدخلات المركزي لتأمين رواتب الموظفين (شفق نيوز)",
            "فهل يحمي طبع النقود رواتب الموظفين، أم يقضم قيمة الدينار في جيوبهم؟",
        ],
    },
    "v11": {
        "slug": s, "kicker": "عاجل",
        "hookHeadline": "طبعوا 25 تريليون… راتبك شيسوي؟",
        "voText": "كشف وزير الخارجية العراقي فؤاد حسين أن الدولة لجأت إلى طبع خمسة وعشرين تريليون دينار لمواجهة شحّ حادّ في السيولة النقدية، مؤكداً أن البنك المركزي لم يعلن هذه الخطوة، وذلك بحسب موقع أخبار العراق. وبذلك ارتفعت القدرة النقدية الاسمية إلى مئة وخمسة وعشرين تريليون دينار، في حين يحتاج اقتصاد الرواتب وحده إلى نحو تسعة تريليونات دينار شهرياً بحسب الخبير محمود داغر. ومع تعذّر إقرار موازنة العام الحالي، يعتمد العراق على القروض وتدخلات المركزي لتأمين الرواتب. فهل يحمي طبع النقود رواتب الموظفين، أم يقضم قيمة الدينار في جيوبهم؟",
        "endQuestion": "هل يحمي طبع النقود الرواتب، أم يقضم قيمة الدينار؟",
        "sourcesLine": "المصادر: أخبار العراق · شفق نيوز · هذا اليوم",
        "images": [img(s, "hero.jpg"), img(s, "broll_1.jpg"), img(s, "broll_2.jpg"), img(s, "broll_3.jpg")],
        "audioBed": "audio/mood_orchestral.mp3",
        "statPops": [
            {"value": "25 تريليون", "label": "طُبعت للسيولة", "matchWord": "وعشرين"},
            {"value": "9 تريليون", "label": "الرواتب شهرياً", "matchWord": "تسعة"},
            {"value": "125 تريليون", "label": "القدرة النقدية", "matchWord": "مئة"},
        ],
    },
    "caption": """العراق يطبع 25 تريليون دينار — شنو يعني لراتبك؟

طبع نقود لمواجهة شحّ السيولة، والبنك المركزي لم يعلن الخطوة.

برأيك، الطبع يحمي الرواتب لو ياكل قيمة الدينار؟

المصادر: أخبار العراق، شفق نيوز
#العراق #الدينار #اقتصاد #الرواتب
@photonect.news""",
}

# ─────────────────────────────────────────────────────────────────────────
# 4 — GULF SOVEREIGN FUNDS DEPLOY TRILLIONS  (P2 · V10 CONTROL · B · silent)
# ─────────────────────────────────────────────────────────────────────────
s = f"{DATE}-gulf-swf-trillions"
SLUGS[s] = {
    "bucket": "gulf_regional",
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/mood_mideast.mp3", "topicBucket": "gulf_regional", "variant": "B",
        "breaking": {
            "arabicKicker": "خليج · استثمار",
            "arabicHeadline": "جيران العراق يوظّفون التريليونات… وبغداد بلا موازنة",
            "englishSubhead": "GULF FUNDS DEPLOY TRILLIONS ABROAD AS IRAQ RUNS WITHOUT A BUDGET",
            "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
        },
        "beats": [
            {
                "label": "ماذا يحدث؟",
                "arabicHeading": "صناديق الخليج بين الأكبر عالمياً",
                "arabicBody": "صندوق الاستثمارات العامة السعودي يدير نحو 900 مليار دولار، والإمارات تعهّدت بـ1.4 تريليون دولار استثمارات في الولايات المتحدة، بحسب مكتب أبحاث مجلس العموم البريطاني.",
                "bigStat": {"value": "$900B", "label": "Saudi PIF assets",
                            "arabicLabel": "قيمة أصول صندوق الاستثمارات العامة السعودي، أحد أكبر الصناديق السيادية في العالم (مكتب أبحاث مجلس العموم البريطاني)"},
                "supportingStats": [{"label": "PIF السعودي", "value": "$900 مليار"},
                                     {"label": "تعهّد الإمارات", "value": "$1.4 تريليون"},
                                     {"label": "الوجهة", "value": "أميركا"}],
                "broll": img(s, "broll_1.jpg"), "brolls": [img(s, "broll_1.jpg")],
                "brollType": "image", "accent": ACCENTS[0], "brollSource": "UK Commons Library · 2026",
            },
            {
                "label": "لماذا يهم؟",
                "arabicHeading": "توسّع من كوريا إلى الصين والهند",
                "arabicBody": "مبادلة الإماراتية ضخّت 550 مليون دولار في كوريا وهونغ كونغ، وجهاز قطر للاستثمار نحو 500 مليون في الصين، وصناديق خليجية 1.7 مليار دولار في شركات هندية، بحسب موديرن دبلوماسي.",
                "bigStat": {"value": "$1.4T", "label": "UAE US-investment pledge",
                            "arabicLabel": "قيمة التعهّد الاستثماري الإماراتي في الولايات المتحدة بعد خروجها من أوبك مطلع أيار (مكتب أبحاث مجلس العموم البريطاني)"},
                "supportingStats": [{"label": "مبادلة", "value": "$550 مليون"},
                                     {"label": "قطر", "value": "$500 مليون"},
                                     {"label": "الهند", "value": "$1.7 مليار"}],
                "broll": img(s, "broll_2.jpg"), "brolls": [img(s, "broll_2.jpg")],
                "brollType": "image", "accent": ACCENTS[1], "brollSource": "Modern Diplomacy · 2026",
            },
            {
                "label": "ماذا بعد؟",
                "arabicHeading": "والعراق خارج سباق التريليونات",
                "arabicBody": "في المقابل يخوض العراق أزمة مالية بلا موازنة 2026، بينما تعدّل أوبك+ الإنتاج بمقدار 188 ألف برميل يومياً في تموز، بحسب سول إيكونوميك ديلي.",
                "bigStat": {"value": "188k b/d", "label": "OPEC+ July adjustment",
                            "arabicLabel": "حجم تعديل إنتاج أوبك+ في تموز بمشاركة العراق، في وقت يفتقر فيه إلى موازنة اتحادية لعام 2026 (سول إيكونوميك ديلي)"},
                "supportingStats": [{"label": "أوبك+", "value": "188 ألف ب/ي"},
                                     {"label": "العراق", "value": "بلا موازنة"},
                                     {"label": "العام", "value": "2026"}],
                "broll": img(s, "broll_3.jpg"), "brolls": [img(s, "broll_3.jpg")],
                "brollType": "image", "accent": ACCENTS[2], "brollSource": "Seoul Economic Daily · 2026",
            },
        ],
        "sources": [
            {"name": "UK Commons Library", "domain": "commonslibrary.parliament.uk"},
            {"name": "Modern Diplomacy", "domain": "moderndiplomacy.eu"},
            {"name": "Seoul Economic Daily", "domain": "sedaily.com"},
        ],
        "arabicTicker": [
            "صندوق الاستثمارات العامة السعودي يدير نحو 900 مليار دولار من الأصول (مجلس العموم البريطاني)",
            "الإمارات تعهّدت باستثمار 1.4 تريليون دولار في الولايات المتحدة بعد خروجها من أوبك مطلع أيار (مجلس العموم البريطاني)",
            "مبادلة الإماراتية تستثمر 550 مليون دولار في كوريا الجنوبية وهونغ كونغ (موديرن دبلوماسي)",
            "جهاز قطر للاستثمار يضخّ نحو 500 مليون دولار في الصين (موديرن دبلوماسي)",
            "صناديق خليجية تستثمر 1.7 مليار دولار في شركات هندية (موديرن دبلوماسي)",
            "أوبك+ تعدّل الإنتاج بمقدار 188 ألف برميل يومياً في تموز بمشاركة العراق (سول إيكونوميك ديلي)",
            "فأين العراق من سباق التريليونات فيما يخوض أزمة مالية بلا موازنة 2026؟",
        ],
    },
    "caption": """صناديق الخليج السيادية 2026 — وين العراق من التريليونات؟

السعودية والإمارات وقطر يوظّفون مئات المليارات عالمياً، والعراق بلا موازنة.

برأيك، ليش العراق غايب عن سباق الاستثمار الإقليمي؟

المصادر: مجلس العموم البريطاني، موديرن دبلوماسي
#العراق #الخليج #استثمار #اقتصاد
@photonect.news""",
    # No v11 brief — silent V10.1 control.
}

# ─────────────────────────────────────────────────────────────────────────
# 5 — WATER RESERVES AT 80-YEAR LOW  (P3 · V11 · C · cinematic feature)
# ─────────────────────────────────────────────────────────────────────────
s = f"{DATE}-water-heat-crisis"
SLUGS[s] = {
    "bucket": "wildcard",
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/mood_mideast.mp3", "topicBucket": "wildcard", "variant": "C",
        "breaking": {
            "arabicKicker": "مناخ · مياه",
            "arabicHeadline": "مخزون مياه العراق عند أدنى مستوى منذ 80 عاماً",
            "englishSubhead": "IRAQ'S WATER RESERVES HIT AN 80-YEAR LOW AS HEAT TOPS 50°C",
            "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
        },
        "beats": [
            {
                "label": "ماذا يحدث؟",
                "arabicHeading": "المخزون ينزل من 18 إلى 10 مليارات م³",
                "arabicBody": "تراجع مخزون العراق المائي إلى أدنى مستوى منذ 80 عاماً، من 18 إلى نحو 10 مليارات متر مكعب، مع موجات حرّ تتجاوز 50 درجة جنوباً، بحسب تشاتام هاوس وأسيا نيوز.",
                "bigStat": {"value": "10 مليار م³", "label": "Water reserves (from 18)",
                            "arabicLabel": "مخزون العراق المائي الحالي بعد هبوطه من 18 مليار متر مكعب، وهو الأدنى منذ 80 عاماً (تشاتام هاوس · أسيا نيوز)"},
                "supportingStats": [{"label": "المخزون", "value": "10 مليار م³"},
                                     {"label": "كان", "value": "18 مليار"},
                                     {"label": "الحرارة", "value": "+50°"}],
                "broll": img(s, "broll_1.jpg"), "brolls": [img(s, "broll_1.jpg")],
                "brollType": "image", "accent": ACCENTS[0], "brollSource": "Chatham House · 2026",
            },
            {
                "label": "لماذا يهم؟",
                "arabicHeading": "أقل من 35% من حصة النهرين",
                "arabicBody": "يحصل العراق على أقل من 35% من حصته النظرية من دجلة والفرات، فيما يسخن البلد أسرع من المعدل العالمي بسبع مرات منذ السبعينيات، بحسب تشاتام هاوس.",
                "bigStat": {"value": "<35%", "label": "Of its river-water share",
                            "arabicLabel": "النسبة التي يحصل عليها العراق فعلياً من حصته النظرية في نهرَي دجلة والفرات (تشاتام هاوس)"},
                "supportingStats": [{"label": "الحصة", "value": "أقل من 35%"},
                                     {"label": "التسخّن", "value": "7 أضعاف"},
                                     {"label": "منذ", "value": "السبعينيات"}],
                "broll": img(s, "broll_2.jpg"), "brolls": [img(s, "broll_2.jpg")],
                "brollType": "image", "accent": ACCENTS[1], "brollSource": "Chatham House · 2026",
            },
            {
                "label": "ماذا بعد؟",
                "arabicHeading": "7 ملايين مهددون في أرزاقهم",
                "arabicBody": "حذّرت 13 منظمة إغاثة من كارثة غير مسبوقة تهدد أرزاق أكثر من 7 ملايين عراقي، بينما قلّص أسوأ موسم جفاف تدفق دجلة والفرات 29% و73%، بحسب أسيا نيوز.",
                "bigStat": {"value": "7 مليون", "label": "Livelihoods at risk",
                            "arabicLabel": "عدد العراقيين المهددة أرزاقهم بحسب تحذير 13 منظمة إغاثة من كارثة مائية غير مسبوقة (أسيا نيوز)"},
                "supportingStats": [{"label": "مهددون", "value": "7 مليون"},
                                     {"label": "دجلة", "value": "-29%"},
                                     {"label": "الفرات", "value": "-73%"}],
                "broll": img(s, "broll_3.jpg"), "brolls": [img(s, "broll_3.jpg")],
                "brollType": "image", "accent": ACCENTS[2], "brollSource": "AsiaNews · Kurdistan24 · 2026",
            },
        ],
        "sources": [
            {"name": "Chatham House", "domain": "chathamhouse.org"},
            {"name": "AsiaNews", "domain": "asianews.it"},
            {"name": "Kurdistan24", "domain": "kurdistan24.net"},
        ],
        "arabicTicker": [
            "مخزون العراق المائي يتراجع إلى أدنى مستوى منذ 80 عاماً، من 18 إلى نحو 10 مليارات متر مكعب (تشاتام هاوس)",
            "موجات حرّ تتجاوز 50 درجة مئوية في جنوب العراق هذا الصيف (أسيا نيوز)",
            "العراق يحصل على أقل من 35% من حصته النظرية في نهرَي دجلة والفرات (تشاتام هاوس)",
            "العراق يسخن أسرع من المعدل العالمي بسبع مرات منذ سبعينيات القرن الماضي (تشاتام هاوس)",
            "13 منظمة إغاثة تحذّر من كارثة غير مسبوقة تهدد أرزاق أكثر من 7 ملايين عراقي (أسيا نيوز)",
            "أسوأ موسم جفاف قلّص تدفق دجلة والفرات بنسبة 29% و73% على التوالي (أسيا نيوز)",
            "فهل تكفي الاتفاقات مع دول المنبع لإنقاذ ما تبقّى من مياه العراق؟",
        ],
    },
    "v11": {
        "slug": s, "kicker": "تحقيق",
        "hookHeadline": "مويتك تخلص… و50 درجة؟",
        "voText": "تراجع مخزون العراق المائي إلى أدنى مستوى له منذ ثمانين عاماً، هابطاً من ثمانية عشر إلى نحو عشرة مليارات متر مكعب، فيما تتجاوز موجات الحرّ خمسين درجة مئوية في الجنوب، وذلك بحسب تشاتام هاوس وأسيا نيوز. ولا يحصل العراق إلا على أقل من خمسة وثلاثين في المئة من حصته النظرية في نهرَي دجلة والفرات، بينما يسخن البلد أسرع من المعدل العالمي بسبع مرات منذ السبعينيات. وقد حذّرت ثلاث عشرة منظمة إغاثة من كارثة غير مسبوقة تهدد أرزاق أكثر من سبعة ملايين عراقي. فهل تكفي الاتفاقات مع دول المنبع لإنقاذ ما تبقّى من مياه العراق؟",
        "endQuestion": "هل تكفي الاتفاقات مع دول المنبع لإنقاذ مياه العراق؟",
        "sourcesLine": "المصادر: تشاتام هاوس · أسيا نيوز · كردستان24",
        "images": [img(s, "hero.jpg"), img(s, "broll_1.jpg"), img(s, "broll_2.jpg"), img(s, "broll_3.jpg")],
        "audioBed": "audio/mood_mideast.mp3",
        "statPops": [
            {"value": "10 مليار م³", "label": "المخزون المائي", "matchWord": "عشرة"},
            {"value": "+50°", "label": "حرارة الجنوب", "matchWord": "خمسين"},
            {"value": "7 مليون", "label": "مهددة أرزاقهم", "matchWord": "سبعة"},
        ],
    },
    "caption": """أزمة المياه في العراق 2026 — المخزون لأدنى مستوى بـ80 سنة

مخزون المياه هبط للنصف تقريباً، وحرارة تتجاوز 50 درجة تهدد الأرزاق.

برأيك، شنو الحل لأزمة مياه العراق؟

المصادر: تشاتام هاوس، أسيا نيوز
#العراق #المياه #الجفاف #المناخ
@photonect.news""",
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
        tag = " +v11" if "v11" in spec else "  (V10 control)"
        print(f"  ✓ {slug}{tag}")
    print(f"\nAuthored {len(SLUGS)} slugs for {DATE}")


if __name__ == "__main__":
    main()
