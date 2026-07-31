#!/usr/bin/env python3
"""Author the 2026-07-31 Photonect NEWS slate.

5 slugs (Iraq/MENA money-power lens). Posting order = alphabetical slug order,
which is what `post-to-uploadpost.py --spread` maps onto the Baghdad evening
slots (`sorted(POSTS.glob(f"{date}-*"))`, slug i -> slot i):

  1 banks-open-for-salaries      iraq_domestic     V11  A  18:00  (lead)
  2 dollar-friday-shops          iraq_domestic     V11  B  19:45  (daily dollar anchor)
  3 foreign-strikes-sovereignty  mena_geopolitics  V11  A  21:15
  4 power-2tn-unused             iraq_domestic     V11  B  22:30
  5 starlink-live-iraq           tech_ai           V10  C  23:45  <- silent control, no v11

Directional shift vs 2026-07-30: yesterday was "the price depends on where you
stand." Today is "the state ran out of days." The government admits on the record
that salaries are late and that it must find more than 10 trillion dinars a month;
Rafidain keeps branches open across the weekend because Monday and Tuesday are
already gone to Arbaeen; the exchange shop takes 1,000 dinars off every 100 dollars
that crosses its counter; foreign jets hit seven governorates and Baghdad says it
was neither asked nor told; and the audit board finds two trillion dinars paid for
electricity that was produced and never used.

Pillar mix: P1 x3 (salaries, dollar, power), P2 x1 (strikes), P3 x1 (starlink).
The "no two consecutive same pillar" guide cannot hold simultaneously with the
standing mandates that (a) the dollar anchor aims for the 19:45 slot and (b) the
biggest genuine money story leads, because both are P1 and slot 2 is pinned. The
adjacent pair is slots 1-2 and the two are maximally different in subject (the
state payroll vs the FX counter). Flagged in DELIVERY.

=== VERIFICATION CORRECTIONS APPLIED (two independent verification passes) ===

Banned this slate, each for a stated reason:

  * NAMING AL-ZAIDI AS THE SALARY SPEAKER. 964media's headline reads
    «الزيدي يصارح العراقيين» but the body attributes every quote to government
    spokesman حيدر العبودي, corroborated by Baghdad Today and INA. The reel names
    al-Abodi. This would have put the wrong man on screen.
  * "11 TRILLION" as the salary bill. 11tn appears only in 964's rendering;
    al-Abodi's own words on video are «أكثر من 10 تريليونات دينار شهرياً», and
    that is the state's TOTAL monthly requirement, not the payroll. Worse, ~11tn
    is separately the well-sourced Jan-Apr fiscal deficit, so the two numbers
    would fuse on screen. Used: "more than 10tn", labelled as total requirement.
  * "OIL EXPORTS DIDN'T EXCEED 2TN OVER 4 MONTHS". A real, accurately quotable
    al-Abodi line — but the Oil Ministry/SOMO reported $2.3bn for May-June alone
    (~3tn IQD), which contradicts it outright. Cut.
  * "10.5 MILLION" on the state payroll. No source anywhere. The named figure is
    ~9 million (مظهر محمد صالح, PM's financial adviser). Used, attributed, ticker only.
  * RASHEED BANK in the weekend-opening card. Every Rasheed hit is date-drifted
    (one traces to 1 April 2026, about March salaries); the bank's own site says
    "Saturday" only. Rafidain alone is confirmed (Shafaq, 30 Jul 21:02 UTC), and
    it is «عدد من فروعه», not all branches. Written that way.
  * "THE BOURSES ARE CLOSED ON FRIDAY". UNVERIFIED — no bourse, CBI or association
    statement establishes it, and Iraqi outlets do publish Friday figures. The reel
    says «آخر تسعيرة معلنة» and dates every number to Thursday instead.
  * THE WORD «إغلاق» for the Thursday bourse level. No source uses it; Mustaqila
    says «استقرت». Written as «مستوى الخميس».
  * ANY CLAIM THE CBI DEVALUED, and the official-rate gap generally. Three official
    rungs exist (1,300 budget parity / 1,310 CBI posted / 1,320 bank-to-trader), the
    1,300 peg has stood since Feb 2023, and 2026-07-30 already ran the official-gap
    angle. Today's slug is built on the SHOP SPREAD instead — new, and fully inside
    one sourced table.
  * KATAIB HEZBOLLAH'S "6 AUGUST DEADLINE". Single-sourced to Iran International,
    which renders it as summary not verbatim; no second outlet carries the date, and
    Al Jazeera reports a DIFFERENT group (النجباء) with no deadline at all. Cut.
  * "CANCELLED" for the Saudi visit. Baghdad's own framing is تأجيل/تعليق. Also the
    city is contested (Jeddah vs Riyadh) so the reel says «السعودية», and "first
    official visit" is thinly sourced so it is dropped.
  * ISRAELI PARTICIPATION. No named source places Israel in this operation; the
    confirmed actors are the US and Saudi Arabia (CENTCOM announced it, Riyadh
    confirmed). The conflicting framing belongs to a separate ongoing campaign.
  * PMF CASUALTY FIGURES. The 20/32 count is the struck party's own explicitly
    preliminary «حصيلة أولية», there is no official government count, and the
    IRGC-adviser number is contested across four figures (4/5/~20). Excluded
    slate-wide, consistent with 2026-07-30.
  * THE 7-GOVERNORATE LIST AS ESTABLISHED FACT. The enumeration originates in the
    PMF's own statement; CENTCOM said only "eastern Iraq". Attributed to الحشد.
  * TRUMP'S COORDINATION CLAIM AS A DIRECT QUOTE. It reached print via a Fox
    correspondent, not a primary transcript. Written «نُقل عن».
  * "100 TRILLION IQD" IN UNSETTLED ADVANCES. Right figure, wrong framing: it is
    dated 23 July (not 28) and is a cumulative stock «منذ عام 2004». Presenting it
    as a 2026 number would be a material distortion. Cut.
  * THE ELECTRICITY MINISTER'S CONTESTED MIDDLE NAME (علي سعد وهيب vs علي سعدي
    وهيب — outlets disagree). Written «علي وهيب», which both agree on.
  * ANY SAME-DAY ELECTRICITY SUPPLY-HOURS FIGURE. None exists dated 30 or 31 July;
    the freshest named-official number is the minister's 27 July 22,000 MW. No
    hours-of-supply claim appears anywhere in this slate.
  * "SIGNED IN WASHINGTON" for the Starlink licence. Abu Kalal himself says it was
    signed inside Iraq «حمايةً للسيادة الوطنية» and the Washington event was
    protocol. Written «أُعلن توقيع الرخصة في 17 تموز», location omitted.
  * "STARLINK DISCOUNT ENDS 31 JULY". Traces to a Baghdad reseller Telegram channel,
    not SpaceX or the CMC. Cut.

Neutrality: the audit board's 2tn is written as هدر مالي مشخّص (waste diagnosed by
auditors), never as theft or corruption, and the reel states that the Ministry of
Electricity publicly responded to the report. The Starlink 75-150k is written as
«سيتراوح» — an indicative range, not a gazetted tariff.

brollSource is «صورة توضيحية · Photonect AI» slate-wide: media-stamp.json records
100% of the imagery as generated, so crediting a wire agency would be misattribution.
Claim attribution lives in arabicBody, bigStat.arabicLabel, the ticker and Sources.

Writes per slug: .meta/props.json, caption.txt, .meta/media-stamp.json, and (for
the 4 voiced) .meta/v11-brief.json. Western numerals on-screen; voText spells
numbers in words (MSA newscast register). No Persian yeh/kaf (grep-guarded).
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POSTS = ROOT / "data" / "posts"
DATE = "2026-07-31"

STAMP = {
    "hunted_at": f"{DATE}T11:35:00+00:00",
    "manual": True,
    "source": "higgsfield nano_banana_pro (KIE 402 — credits exhausted, 5th day)",
    "date": DATE,
    "note": (
        "KIE's credit endpoint returned a balance of -5.5 for the fifth consecutive "
        "day, so the whole slate was generated on Higgsfield's nano_banana_pro at "
        "9:16 / 2k (the API echoes the model back as 'nano_banana_2', same Nano "
        "Banana Pro family, different vendor). All 20 submissions landed — no silent "
        "drops this run. Every image Read-verified by hand before acceptance; 1 "
        "rejected and regenerated (foreign-strikes-sovereignty/broll_3 returned a "
        "Northern-European interior for an Iraq-Saudi diplomatic scene). No stock "
        "imagery anywhere in the slate, so auto-post stays ON."
    ),
}

ARABIC_DATE = "31 تموز 2026"
DATE_LABEL = "JUL 31 • 2026"


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


S1 = f"{DATE}-banks-open-for-salaries"
S2 = f"{DATE}-dollar-friday-shops"
S3 = f"{DATE}-foreign-strikes-sovereignty"
S4 = f"{DATE}-power-2tn-unused"
S5 = f"{DATE}-starlink-live-iraq"

SLUGS: dict[str, dict] = {}

# ───────────────────────────── 1 · SALARIES / WEEKEND BANKING (P1, LEAD 18:00) ──
SLUGS[S1] = {
    "props": {
        "dateLabel": DATE_LABEL,
        "arabicDateLabel": ARABIC_DATE,
        "handle": "@photonect.news",
        "audioBed": "audio/mood_newsroom.mp3",
        "topicBucket": "iraq_domestic",
        "variant": "A",
        "breaking": {
            "arabicKicker": "رواتب · مصارف",
            "arabicHeadline": "الحكومة تقر: الرواتب ستتأخر… والرافدين يفتح بالعطلة",
            "englishSubhead": "GOVERNMENT SPOKESMAN SAYS SALARIES WILL BE LATE; RAFIDAIN KEEPS BRANCHES OPEN FRIDAY AND SATURDAY",
            "heroMedia": img(S1, "hero.jpg"),
            "heroMediaType": "image",
        },
        "beats": [
            beat(
                "ماذا يحدث؟",
                "المتحدث باسم الحكومة: الرواتب ستتأخر",
                "حيدر العبودي، المتحدث باسم الحكومة، قال الخميس إن الرواتب ستتأخر وإن البلاد تمر بأزمة مالية حقيقية، بحسب 964.",
                "+10", "trillion IQD the state needs monthly",
                "ما قال المتحدث باسم الحكومة حيدر العبودي إن الحكومة مطالبة بتأمينه شهرياً: أكثر من 10 تريليونات دينار. وهو إجمالي الاحتياج الشهري للدولة وليس فاتورة الرواتب وحدها (964 · هذا اليوم)",
                [("الاحتياج الشهري", "+10 تريليون"), ("المتحدث", "حيدر العبودي"), ("التصريح", "30 تموز")],
                S1, "broll_1.jpg", "#D72638",
            ),
            beat(
                "لماذا يهم؟",
                "الرافدين يواصل الدوام الجمعة والسبت",
                "مصرف الرافدين وجّه عدداً من فروعه بالاستمرار بالدوام يومي الجمعة والسبت لإكمال توطين الرواتب، بحسب شفق نيوز.",
                "22 تموز", "date July salary funding was released",
                "اليوم الذي باشرت فيه دائرة المحاسبة في وزارة المالية إجراءات إطلاق تمويلات رواتب موظفي الدولة لشهر تموز، قبل تسعة أيام من تعليمات الدوام الإضافي (وكالة مستقلة · شفق نيوز)",
                [("دوام إضافي", "الجمعة والسبت"), ("إطلاق التمويل", "22 تموز"), ("الفروع", "عدد منها")],
                S1, "broll_2.jpg", "#FFC217",
            ),
            beat(
                "ماذا بعد؟",
                "وبعدها عطلة الاثنين والثلاثاء",
                "مجلس الوزراء عطّل الدوام الرسمي يومي 3 و4 آب بمناسبة الأربعينية، بقرار اتُخذ في جلسة 25 تموز، بحسب شفق نيوز.",
                "3-4 آب", "state institutions closed for Arbaeen",
                "يوما تعطيل الدوام الرسمي في مؤسسات الدولة بمناسبة زيارة الأربعينية، بقرار من مجلس الوزراء في جلسته يوم 25 تموز 2026 (شفق نيوز · بغداد اليوم)",
                [("العطلة", "3-4 آب"), ("قرار المجلس", "25 تموز"), ("سبب التأخير", "نقص سيولة")],
                S1, "broll_3.jpg", "#4CC9F0",
            ),
        ],
        "sources": [
            {"name": "964media", "domain": "964media.com"},
            {"name": "Shafaq News", "domain": "shafaq.com"},
        ],
        "arabicTicker": [
            "المتحدث باسم الحكومة حيدر العبودي قال الخميس 30 تموز 2026 إن الرواتب ستتأخر وإن البلاد تمر بأزمة مالية حقيقية (964)",
            "العبودي: الحكومة مطالبة بتأمين أكثر من 10 تريليونات دينار شهرياً، وهو إجمالي الاحتياج الشهري للدولة (هذا اليوم · 964)",
            "مصرف الرافدين وجّه عدداً من فروعه بالاستمرار بالدوام يومي الجمعة والسبت لإكمال توطين الرواتب (شفق نيوز)",
            "دائرة المحاسبة في وزارة المالية باشرت في 22 تموز 2026 إجراءات إطلاق تمويلات رواتب تموز (وكالة مستقلة · شفق نيوز)",
            "اللجنة المالية النيابية عزت التأخير في 28 تموز إلى نقص طارئ ومؤقت في السيولة (قناة الرشيد · المدى)",
            "مجلس الوزراء عطّل الدوام الرسمي يومي 3 و4 آب بمناسبة الأربعينية، بقرار اتُخذ في 25 تموز (شفق نيوز · بغداد اليوم)",
            "نحو 9 ملايين عراقي يتقاضون رواتب من الدولة، بحسب المستشار المالي لرئيس الوزراء مظهر محمد صالح",
            "وصل راتبك لو لا؟",
        ],
    },
    "v11": {
        "kicker": "رواتب",
        "hookHeadline": "راتبك وين؟ المصرف فتح بالعطلة",
        "voText": (
            "قال المتحدث باسم الحكومة العراقية حيدر العبودي يوم الخميس إن رواتب "
            "الموظفين ستتأخر، وإن البلاد تمر بأزمة مالية حقيقية، مضيفاً أن الحكومة "
            "مطالبة بتأمين أكثر من عشرة تريليونات دينار شهرياً. وفي المقابل، وجّه "
            "مصرف الرافدين عدداً من فروعه بالاستمرار بالدوام يومي الجمعة والسبت "
            "لإكمال توطين الرواتب. وكانت وزارة المالية قد باشرت إطلاق التمويلات في "
            "الثاني والعشرين من تموز. ثم يتوقف الدوام الرسمي في مؤسسات الدولة يومي "
            "الثالث والرابع من آب بمناسبة الأربعينية. فوصل راتبك لو لا؟"
        ),
        "endQuestion": "وصل راتبك لو لا؟",
        "sourcesLine": "المصادر: 964 · شفق نيوز · وكالة مستقلة",
        "statPops": [
            {"value": "+10 تريليون", "label": "الاحتياج الشهري للدولة", "matchWord": "عشرة"},
            {"value": "3-4 آب", "label": "تعطيل الدوام للأربعينية", "matchWord": "الأربعينية"},
        ],
    },
    "caption": """رواتب موظفي العراق — ليش تأخرت هالشهر؟

الحكومة تقر بأزمة مالية… والرافدين يواصل الدوام بالعطلة لإكمال الصرف.

وصل راتبك لو لا؟

المصادر: 964، شفق نيوز
#العراق #رواتب_الموظفين #الرافدين #أخبار_العراق
@photonect.news
""",
}

# ─────────────────────────────── 2 · DOLLAR / SHOP SPREAD (P1 ANCHOR, 19:45) ──
SLUGS[S2] = {
    "props": {
        "dateLabel": DATE_LABEL,
        "arabicDateLabel": ARABIC_DATE,
        "handle": "@photonect.news",
        "audioBed": "audio/mood_cinematic.mp3",
        "topicBucket": "iraq_domestic",
        "variant": "B",
        "breaking": {
            "arabicKicker": "دولار · صيرفة",
            "arabicHeadline": "1,000 دينار تروح بكل 100 دولار تصرّفها",
            "englishSubhead": "BAGHDAD EXCHANGE SHOPS SELL $100 AT 151,000 IQD AND BUY AT 150,000 — A 1,000 IQD SPREAD (THU 30 JUL)",
            "heroMedia": img(S2, "hero.jpg"),
            "heroMediaType": "image",
        },
        "beats": [
            beat(
                "ماذا يحدث؟",
                "الصيرفة تبيع بـ151,000 وتشتري بـ150,000",
                "آخر تسعيرة معلنة يوم الخميس: محال الصيرفة تبيع 100 دولار عند حدود 151,000 دينار وتشتريها بنحو 150,000، بحسب وكالة مستقلة.",
                "1,000", "IQD spread per $100 at exchange shops",
                "الفارق بين سعر بيع وشراء 100 دولار في محال الصيرفة يوم الخميس 30 تموز 2026: بيع عند حدود 151,000 دينار وشراء نحو 150,000 (وكالة مستقلة)",
                [("بيع", "151,000"), ("شراء", "150,000"), ("الفارق", "1,000")],
                S2, "broll_1.jpg", "#FFC217",
            ),
            beat(
                "لماذا يهم؟",
                "البورصة أرخص: 150,650 لكل 100 دولار",
                "بورصتا الكفاح والحارثية استقرتا الخميس عند 150,650 ديناراً لكل 100 دولار، صعوداً من 150,300 يوم الأربعاء، بحسب وكالة مستقلة.",
                "150,650", "al-Kifah / al-Harithiya level on Thursday",
                "مستوى بورصتي الكفاح والحارثية يوم الخميس 30 تموز 2026 لكل 100 دولار، مقابل 150,300 ديناراً يوم الأربعاء 29 تموز (وكالة مستقلة)",
                [("الخميس", "150,650"), ("الأربعاء", "150,300"), ("فرق الصيرفة", "350")],
                S2, "broll_2.jpg", "#4CC9F0",
            ),
            beat(
                "ماذا بعد؟",
                "وأربيل؟ الفارق هناك 100 دينار فقط",
                "في أربيل بيع 150,800 وشراء 150,700 يوم الخميس، أي فارق 100 دينار مقابل نحو 1,000 في محال بغداد، بحسب وكالة مستقلة.",
                "100", "IQD spread in Erbil, vs ~1,000 in Baghdad shops",
                "الفارق بين البيع والشراء لكل 100 دولار في أربيل يوم الخميس 30 تموز 2026: بيع 150,800 دينار وشراء 150,700 (وكالة مستقلة)",
                [("أربيل بيع", "150,800"), ("أربيل شراء", "150,700"), ("الفارق", "100")],
                S2, "broll_3.jpg", "#D72638",
            ),
        ],
        "sources": [
            {"name": "Wikala Mustaqila", "domain": "mustaqila.com"},
            {"name": "Shafaq News", "domain": "shafaq.com"},
        ],
        "arabicTicker": [
            "آخر تسعيرة معلنة يوم الخميس 30 تموز 2026: محال الصيرفة تبيع 100 دولار عند حدود 151,000 دينار (وكالة مستقلة)",
            "سعر الشراء في محال الصيرفة بلغ نحو 150,000 دينار لكل 100 دولار، أي فارق 1,000 دينار (وكالة مستقلة)",
            "بورصتا الكفاح والحارثية استقرتا يوم الخميس عند 150,650 ديناراً لكل 100 دولار (وكالة مستقلة)",
            "وكان مستوى البورصتين 150,300 ديناراً يوم الأربعاء 29 تموز 2026 (وكالة مستقلة)",
            "في أربيل يوم الخميس: بيع 150,800 دينار وشراء 150,700 لكل 100 دولار (وكالة مستقلة)",
            "الفارق بين البيع والشراء في أربيل 100 دينار، مقابل نحو 1,000 دينار في محال الصيرفة (وكالة مستقلة)",
            "شكد دفعت آخر مرة صرّفت دولار؟",
        ],
    },
    "v11": {
        "kicker": "دولار",
        "hookHeadline": "كل 100 دولار… 1,000 دينار تروح",
        "voText": (
            "في آخر تسعيرة معلنة يوم الخميس، كانت محال الصيرفة في بغداد تبيع المئة "
            "دولار عند حدود مئة وواحد وخمسين ألف دينار، وتشتريها بنحو مئة وخمسين "
            "ألفاً، أي فارق ألف دينار في كل مئة دولار. وفي بورصتي الكفاح والحارثية "
            "استقر السعر عند مئة وخمسين ألفاً وستمئة وخمسين ديناراً، صعوداً من مئة "
            "وخمسين ألفاً وثلاثمئة يوم الأربعاء. أما في أربيل فكان الفارق بين البيع "
            "والشراء مئة دينار فقط. فشكد دفعت آخر مرة صرّفت دولار؟"
        ),
        "endQuestion": "شكد دفعت آخر مرة صرّفت دولار؟",
        "sourcesLine": "المصادر: وكالة مستقلة",
        "statPops": [
            {"value": "151,000", "label": "بيع 100 دولار بالصيرفة", "matchWord": "وواحد"},
            {"value": "150,650", "label": "مستوى الكفاح والحارثية", "matchWord": "وستمئة"},
        ],
    },
    "caption": """سعر الدولار في العراق — بيش بمحال الصيرفة؟

الفرق بين ما تشتري بيه وما تبيع بيه… 1,000 دينار بكل 100 دولار.

شكد دفعت آخر مرة صرّفت دولار؟

المصادر: وكالة مستقلة
#العراق #الدولار #سعر_الصرف #الدينار_العراقي
@photonect.news
""",
}

# ──────────────────────────── 3 · STRIKES / SOVEREIGNTY (P2, 21:15) ──
SLUGS[S3] = {
    "props": {
        "dateLabel": DATE_LABEL,
        "arabicDateLabel": ARABIC_DATE,
        "handle": "@photonect.news",
        "audioBed": "audio/music_03.mp3",
        "topicBucket": "mena_geopolitics",
        "variant": "A",
        "breaking": {
            "arabicKicker": "سيادة · ضربات",
            "arabicHeadline": "ضربات بـ7 محافظات… وبغداد: لا علم ولا موافقة",
            "englishSubhead": "US-SAUDI STRIKES HIT SITES IN 7 IRAQI GOVERNORATES PER THE PMF; BAGHDAD SAYS IT GAVE NO APPROVAL",
            "heroMedia": img(S3, "hero.jpg"),
            "heroMediaType": "image",
        },
        "beats": [
            beat(
                "ماذا يحدث؟",
                "الحشد: الضربات طالت 7 محافظات",
                "هيئة الحشد الشعبي قالت إن ضربات فجر الأربعاء طالت مقرات في 7 محافظات، والقيادة المركزية الأمريكية أعلنت تنفيذ العملية مع السعودية، بحسب الجزيرة.",
                "7", "governorates hit, per the PMF statement",
                "عدد المحافظات التي قالت هيئة الحشد الشعبي إن الضربات طالت مقرات فيها فجر الأربعاء 29 تموز 2026: بغداد وواسط ونينوى والبصرة وكركوك وكربلاء وديالى. القيادة المركزية الأمريكية اكتفت بالقول إنها شرق العراق (الجزيرة · الحرة)",
                [("المحافظات", "7"), ("التاريخ", "29 تموز"), ("المعلن", "أمريكا والسعودية")],
                S3, "broll_1.jpg", "#D72638",
            ),
            beat(
                "لماذا يهم؟",
                "بغداد تنفي أي علم مسبق أو موافقة",
                "المتحدث باسم الحكومة حيدر العبودي قال إن بغداد لم تمنح أي موافقة ولم يكن لديها علم مسبق، فيما نُقل عن ترامب قوله إنها جرت بالتنسيق مع العراق.",
                "+30", "drone attacks CENTCOM cited as its stated reason",
                "عدد الهجمات بطائرات مسيّرة خلال 72 ساعة التي قالت القيادة المركزية الأمريكية إن الضربات جاءت رداً عليها. الرواية الأمريكية والرواية العراقية متعارضتان بشأن التنسيق المسبق (الجزيرة · ميدل إيست مونيتور)",
                [("موقف بغداد", "لا موافقة"), ("مسيّرات", "+30"), ("خلال", "72 ساعة")],
                S3, "broll_2.jpg", "#FFC217",
            ),
            beat(
                "ماذا بعد؟",
                "زيارة السعودية تأجلت… والرياض: لا نسعى للتصعيد",
                "رئيس الوزراء أجّل زيارته إلى السعودية التي كانت مقررة الخميس، والمتحدث باسم وزارة الدفاع السعودية تركي المالكي قال إن المملكة لا تسعى للتصعيد لكنها سترد بحزم.",
                "30 تموز", "date of the postponed visit to Saudi Arabia",
                "الموعد الذي كانت مقررة فيه زيارة رئيس الوزراء علي فالح الزيدي إلى السعودية قبل تأجيلها عقب الضربات. بغداد تصفها بالتأجيل لا الإلغاء (الجزيرة · CNN بالعربية)",
                [("الزيارة", "مؤجلة"), ("كانت بتاريخ", "30 تموز"), ("الرياض", "لا تصعيد")],
                S3, "broll_3.jpg", "#4CC9F0",
            ),
        ],
        "sources": [
            {"name": "Al Jazeera", "domain": "aljazeera.net"},
            {"name": "CNN Arabic", "domain": "arabic.cnn.com"},
        ],
        "arabicTicker": [
            "هيئة الحشد الشعبي قالت إن ضربات فجر الأربعاء 29 تموز 2026 طالت مقرات في 7 محافظات (الجزيرة)",
            "القيادة المركزية الأمريكية أعلنت تنفيذ العملية مع السعودية، والرياض أكدت مشاركتها (الجزيرة)",
            "المجلس الوزاري للأمن الوطني وصف ما جرى بأنه انتهاك صارخ لسيادة العراق وحرمة أراضيه (الجزيرة)",
            "المتحدث باسم الحكومة حيدر العبودي: بغداد لم تمنح أي موافقة ولم يكن لديها علم مسبق بالضربات (ميدل إيست مونيتور)",
            "القيادة المركزية الأمريكية قالت إن الضربات جاءت رداً على أكثر من 30 هجوماً بطائرات مسيّرة خلال 72 ساعة (الجزيرة)",
            "رئيس الوزراء أجّل زيارته إلى السعودية التي كانت مقررة الخميس 30 تموز 2026 (الجزيرة · CNN بالعربية)",
            "المتحدث باسم وزارة الدفاع السعودية تركي المالكي: المملكة لا تسعى للتصعيد لكنها سترد بحزم",
            "تحس القرار بسمانا بإيدنا لو لا؟",
        ],
    },
    "v11": {
        "kicker": "سيادة",
        "hookHeadline": "سبع محافظات انضربت… ومنو قرر؟",
        "voText": (
            "قالت هيئة الحشد الشعبي إن ضربات فجر الأربعاء طالت مقرات في سبع محافظات "
            "عراقية، وأعلنت القيادة المركزية الأمريكية تنفيذ العملية مع السعودية رداً "
            "على أكثر من ثلاثين هجوماً بطائرات مسيّرة. وقال المتحدث باسم الحكومة حيدر "
            "العبودي إن بغداد لم تمنح أي موافقة ولم يكن لديها علم مسبق بالضربات، فيما "
            "نُقل عن الرئيس الأمريكي قوله إنها جرت بالتنسيق مع بغداد. ثم أجّل رئيس "
            "الوزراء زيارته إلى السعودية. فتحس القرار بسمانا بإيدنا لو لا؟"
        ),
        "endQuestion": "تحس القرار بسمانا بإيدنا لو لا؟",
        "sourcesLine": "المصادر: الجزيرة · CNN بالعربية",
        "statPops": [
            {"value": "7", "label": "محافظات طالتها الضربات", "matchWord": "سبع"},
            {"value": "+30", "label": "هجمات مسيّرة ذكرتها واشنطن", "matchWord": "ثلاثين"},
        ],
    },
    "caption": """ضربات أمريكية سعودية داخل العراق — منو أعطى الإذن؟

بغداد تنفي أي علم مسبق أو موافقة… والرواية الأمريكية تقول غير ذلك.

تحس القرار بسمانا بإيدنا لو لا؟

المصادر: الجزيرة، CNN بالعربية
#العراق #أخبار_العراق #السيادة #بغداد
@photonect.news
""",
}

# ─────────────────────── 4 · AUDIT BOARD / UNUSED ELECTRICITY (P1, 22:30) ──
SLUGS[S4] = {
    "props": {
        "dateLabel": DATE_LABEL,
        "arabicDateLabel": ARABIC_DATE,
        "handle": "@photonect.news",
        "audioBed": "audio/mood_orchestral.mp3",
        "topicBucket": "iraq_domestic",
        "variant": "B",
        "breaking": {
            "arabicKicker": "رقابة · كهرباء",
            "arabicHeadline": "تريليونا دينار مقابل كهرباء أُنتجت ولم تُستغل",
            "englishSubhead": "FEDERAL BOARD OF SUPREME AUDIT DIAGNOSES ~2TN IQD PAID FOR PRODUCED-BUT-UNUSED POWER UNDER TAKE-OR-PAY CONTRACTS",
            "heroMedia": img(S4, "hero.jpg"),
            "heroMediaType": "image",
        },
        "beats": [
            beat(
                "ماذا يحدث؟",
                "الرقابة المالية تشخّص هدراً بتريليوني دينار",
                "رئيس ديوان الرقابة المالية الاتحادي عمار صبحي المشهداني قال الثلاثاء إن الحكومة دفعت نحو تريليوني دينار مقابل طاقة كهربائية أُنتجت ولم تُستغل.",
                "2", "trillion IQD paid for unused electricity",
                "قيمة ما قال رئيس ديوان الرقابة المالية الاتحادي عمار صبحي المشهداني إن الحكومة دفعته مقابل طاقة كهربائية منتجة غير مستغلة ضمن عقود خذ أو ادفع، في تصريحات يوم 28 تموز 2026. التوصيف المعلن هدر مالي مشخّص، لا اتهام بالسرقة (كلمة · شفقنا)",
                [("هدر مشخّص", "~2 تريليون"), ("نوع العقود", "خذ أو ادفع"), ("التصريح", "28 تموز")],
                S4, "broll_1.jpg", "#FFC217",
            ),
            beat(
                "لماذا يهم؟",
                "والمنظومة نزلت إلى 22,000 ميغاواط",
                "وزير الكهرباء علي وهيب قال أمام مجلس النواب الاثنين إن الإنتاج انخفض إلى 22,000 ميغاواط مقابل حاجة 60,000، وإن أكثر من 60% يُهدر بالتجاوزات.",
                "22,000", "MW generation against a 60,000 MW need",
                "مستوى الإنتاج الذي قال وزير الكهرباء علي وهيب أمام مجلس النواب يوم 27 تموز 2026 إن المنظومة انخفضت إليه، مقابل حاجة العراق البالغة 60,000 ميغاواط (non14)",
                [("الإنتاج", "22,000"), ("الحاجة", "60,000"), ("يُهدر بالتجاوزات", "+60%")],
                S4, "broll_2.jpg", "#D72638",
            ),
            beat(
                "ماذا بعد؟",
                "14 تريليوناً ديوناً و2,000 تقرير للقضاء",
                "المشهداني تحدث أيضاً عن 14 تريليون دينار ديوناً متعثرة للدولة، وإحالة نحو 2,000 تقرير رقابي إلى النزاهة والادعاء العام والمحاكم خلال 3 سنوات.",
                "14", "trillion IQD in debts owed to the state",
                "قيمة الديون المتعثرة والمستحقة السداد بذمة أشخاص وشركات ومؤسسات لمصلحة الدولة، بحسب رئيس ديوان الرقابة المالية الاتحادي في 28 تموز 2026 (كلمة)",
                [("ديون متعثرة", "14 تريليون"), ("تقارير للقضاء", "~2,000"), ("خلال", "3 سنوات")],
                S4, "broll_3.jpg", "#4CC9F0",
            ),
        ],
        "sources": [
            {"name": "Federal Board of Supreme Audit", "domain": "fbsa.gov.iq"},
            {"name": "Kalima IQ", "domain": "kalimaiq.com"},
        ],
        "arabicTicker": [
            "رئيس ديوان الرقابة المالية الاتحادي عمار صبحي المشهداني قال في 28 تموز 2026 إن الحكومة دفعت نحو تريليوني دينار مقابل طاقة منتجة غير مستغلة (كلمة)",
            "الدفع جرى ضمن عقود خذ أو ادفع، والتوصيف المعلن هو هدر مالي مشخّص وليس اتهاماً بالسرقة (كلمة · شفقنا)",
            "وزارة الكهرباء ردت علناً على ما ورد في تقرير ديوان الرقابة المالية",
            "وزير الكهرباء علي وهيب قال أمام مجلس النواب في 27 تموز 2026 إن الإنتاج انخفض إلى 22,000 ميغاواط (non14)",
            "الوزير قدّر حاجة العراق بـ60,000 ميغاواط، وقال إن أكثر من 60% من الطاقة المجهزة يُهدر بالتجاوزات (non14)",
            "المشهداني تحدث عن 14 تريليون دينار ديوناً متعثرة لمصلحة الدولة (كلمة)",
            "الديوان أحال نحو 2,000 تقرير رقابي إلى هيئة النزاهة والادعاء العام والمحاكم خلال 3 سنوات (كلمة)",
            "شكد ساعة كهرباء وطنية جتك اليوم؟",
        ],
    },
    "v11": {
        "kicker": "رقابة",
        "hookHeadline": "تريليونان مقابل كهرباء ما وصلتك",
        "voText": (
            "قال رئيس ديوان الرقابة المالية الاتحادي عمار صبحي المشهداني إن الحكومة "
            "دفعت نحو تريليوني دينار مقابل طاقة كهربائية أُنتجت ولم تُستغل، ضمن عقود "
            "خذ أو ادفع. ووصف الديوان ذلك بأنه هدر مالي مشخّص، لا اتهام بالسرقة، وقد "
            "ردت وزارة الكهرباء علناً على التقرير. وفي اليوم السابق، قال وزير الكهرباء "
            "علي وهيب أمام مجلس النواب إن الإنتاج انخفض إلى اثنين وعشرين ألف ميغاواط، "
            "مقابل حاجة ستين ألفاً. فشكد ساعة كهرباء وطنية جتك اليوم؟"
        ),
        "endQuestion": "شكد ساعة كهرباء وطنية جتك اليوم؟",
        "sourcesLine": "المصادر: ديوان الرقابة المالية · كلمة · non14",
        "statPops": [
            {"value": "2 تريليون", "label": "مقابل طاقة لم تُستغل", "matchWord": "تريليوني"},
            {"value": "22,000", "label": "ميغاواط الإنتاج الحالي", "matchWord": "وعشرين"},
        ],
    },
    "caption": """الكهرباء في العراق — وين راحت تريليونا دينار؟

ديوان الرقابة المالية يشخّص هدراً بعقود «خذ أو ادفع»… ووزارة الكهرباء ترد.

شكد ساعة كهرباء وطنية جتك اليوم؟

المصادر: كلمة، ديوان الرقابة المالية
#العراق #الكهرباء #أخبار_العراق #الرقابة_المالية
@photonect.news
""",
}

# ────────────────────────── 5 · STARLINK LIVE (P3, 23:45, V10 SILENT CONTROL) ──
SLUGS[S5] = {
    "props": {
        "dateLabel": DATE_LABEL,
        "arabicDateLabel": ARABIC_DATE,
        "handle": "@photonect.news",
        "audioBed": "audio/music_05.mp3",
        "topicBucket": "tech_ai",
        "variant": "C",
        "breaking": {
            "arabicKicker": "إنترنت · اتصالات",
            "arabicHeadline": "ستارلنك اشتغلت بالعراق… والاشتراك 75-150 ألف دينار",
            "englishSubhead": "STARLINK GOES LIVE IN IRAQ; CMC SAYS MONTHLY SUBSCRIPTIONS WILL RANGE 75,000-150,000 IQD",
            "heroMedia": img(S5, "hero.jpg"),
            "heroMediaType": "image",
        },
        "beats": [
            beat(
                "ماذا يحدث؟",
                "الإطلاق الفعلي لستارلنك في العراق",
                "رئيس الجهاز التنفيذي لهيئة الإعلام والاتصالات بليغ أبو كلل أعلن الأربعاء الإطلاق الفعلي لخدمة ستارلنك، بعد إعلان توقيع الرخصة في 17 تموز.",
                "29 تموز", "date Starlink went live in Iraq",
                "اليوم الذي أعلن فيه رئيس الجهاز التنفيذي لهيئة الإعلام والاتصالات بليغ أبو كلل الإطلاق الفعلي لخدمة ستارلنك في العراق، بعد إعلان توقيع رخصة التشغيل في 17 تموز 2026 (964 · شفق نيوز)",
                [("الإطلاق", "29 تموز"), ("إعلان الرخصة", "17 تموز"), ("محطات أرضية", "7")],
                S5, "broll_1.jpg", "#4CC9F0",
            ),
            beat(
                "لماذا يهم؟",
                "الاشتراك يتراوح بين 75 و150 ألف دينار",
                "أبو كلل قال إن سعر الاشتراك سيتراوح بين 75 و150 ألف دينار شهرياً، وهو نطاق أعلنته الهيئة وليس تعرفة نهائية، بحسب 964.",
                "75-150", "thousand IQD monthly subscription range",
                "النطاق الشهري لسعر اشتراك ستارلنك كما أعلنه رئيس الجهاز التنفيذي لهيئة الإعلام والاتصالات بليغ أبو كلل يوم 29 تموز 2026، بصيغة سيتراوح، أي نطاق معلن لا تعرفة نهائية (964)",
                [("الحد الأدنى", "75 ألف"), ("الحد الأعلى", "150 ألف"), ("الدورية", "شهرياً")],
                S5, "broll_2.jpg", "#FFC217",
            ),
            beat(
                "ماذا بعد؟",
                "40 ألف جهاز بلا ترخيص… وحصة الدولة 9%",
                "الهيئة قدّرت وجود نحو 40 ألف جهاز يعمل بلا ترخيص، وقالت إن حصة الدولة 8% من الإيرادات و1% خدمة شاملة، إضافة إلى ضريبة أرباح 15%.",
                "40,000", "unlicensed terminals estimated before launch",
                "العدد التقديري لأجهزة ستارلنك التي كانت تعمل في العراق بلا ترخيص قبل الإطلاق الرسمي، بحسب تقدير هيئة الإعلام والاتصالات وليس إحصاءً مستقلاً (964)",
                [("أجهزة بلا ترخيص", "~40,000"), ("حصة الدولة", "9%"), ("ضريبة أرباح", "15%")],
                S5, "broll_3.jpg", "#D72638",
            ),
        ],
        "sources": [
            {"name": "Communications and Media Commission", "domain": "cmc.iq"},
            {"name": "964media", "domain": "964media.com"},
        ],
        "arabicTicker": [
            "رئيس الجهاز التنفيذي لهيئة الإعلام والاتصالات بليغ أبو كلل أعلن في 29 تموز 2026 الإطلاق الفعلي لخدمة ستارلنك في العراق (964)",
            "أُعلن توقيع رخصة التشغيل في 17 تموز 2026 (964)",
            "أبو كلل: سعر الاشتراك سيتراوح بين 75 و150 ألف دينار شهرياً، وهو نطاق معلن وليس تعرفة نهائية (964)",
            "حصة الدولة 8% من الإيرادات المباشرة و1% رسم خدمة شاملة، إضافة إلى ضريبة أرباح بنسبة 15% (964)",
            "الهيئة تحدثت عن إنشاء 7 محطات أرضية حول بغداد لأغراض المراقبة (واع)",
            "الهيئة قدّرت وجود نحو 40 ألف جهاز ستارلنك يعمل في العراق بلا ترخيص قبل الإطلاق (964)",
            "تشترك بـ150 ألف بالشهر لو لا؟",
        ],
    },
    "caption": """ستارلنك في العراق — شكد يكلف الاشتراك بالشهر؟

الخدمة اشتغلت رسمياً… و40 ألف جهاز كان يشتغل بلا ترخيص قبلها.

تشترك بـ150 ألف بالشهر لو لا؟

المصادر: 964، هيئة الإعلام والاتصالات
#العراق #ستارلنك #الإنترنت #أخبار_العراق
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
