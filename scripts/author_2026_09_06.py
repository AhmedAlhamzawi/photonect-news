#!/usr/bin/env python3
"""Author the 2026-09-06 slate: 5 slugs, props.json + caption.txt + 4 v11 briefs.

Pillar mix: P1 x3 (dollar rumour, ghost-employee graft, fake investment firms),
P2 x1 (Lebanon->Iraq exports), P3 x1 (Asian Games, Iraqi-pride hook).
Posting order alternates pillars: a P1 · b P2 · c P1 · d P3 · e P1.
Alphabetical slug order drives posting time -> a 18:00, b 19:45, c 21:15,
d 22:30, e 23:45.

DEVIATION FROM THE DAILY-ANCHOR SPEC (aim the dollar slug at 19:45): the dollar
story today is not a routine price pulse, it is the central bank publicly
denying a circulating claim that deposits would be repriced at 1,460 IQD from
today. That is the biggest money story on the slate, so it takes the 18:00 lead
and the P2 trade story takes 19:45.

Slug E (fake investment firms) is the silent V10.1 control: it is the only story
on the slate carrying NO published figure of any kind — the same criterion used
to pick the control on 09-01, 09-02 and 09-03.

EVERY figure below is transcribed from an article fetched today, 2026-09-06,
with its dateline read before use:
  * dollar rumour + denial -> شفق نيوز, 2026-09-05T14:49Z (Arabic body verbatim)
  * market rate            -> قناة الفلوجة, 2026-09-06 13:26 محلي — bourse-vs-bourse
                              (الكفاح/الحارثية today 154,900 vs Saturday 154,650),
                              shop sell/buy quoted separately and never mixed
  * Lebanon exports        -> شفق نيوز, 2026-09-06T10:10Z, citing ITC trade map
  * ghost employee         -> هيئة النزاهة via واع / شبكة لالش, 2026-09-05
  * Asian Games            -> شفق نيوز, 2026-09-06T10:44Z
  * securities warning     -> شفق نيوز, 2026-09-06T09:37Z (Arabic body verbatim)

A NOTE ON WHAT IS DELIBERATELY *NOT* HERE: Shafaq's ENGLISH write-up of the CBI
denial adds "the bank's latest published data, dated September 3, list the US
dollar at 1,310 dinars". The Arabic original carries no such figure and I could
not verify the official rate against a CBI primary source in time, so no
official-rate number appears anywhere on slug A. The reel compares the rumoured
rate to the parallel market only, and says so.

The ghost-employee slug names no individual and states on screen that the man is
an accused person with no conviction. No synthetic portrait is used anywhere on
the slate (V11 draws no «صورة توضيحية» chip).

voText spells all numbers as Arabic words: the V11 VO has no numeral normaliser.
No Persian yeh/kaf anywhere (guard: U+06CC / U+06A9, asserted below).
"""
from __future__ import annotations
import json
import re
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE")
POSTS = ROOT / "data" / "posts"
D = "2026-09-06"
DATE_LABEL = "SEP 06 • 2026"
AR_DATE = "6 أيلول 2026"
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


PERSIAN = re.compile("[یک]")


def _validate(slug: str, props: dict, brief: dict | None) -> None:
    """Guard the schema + language mistakes that only surface at render time.

    1. `sources` MUST be a list of >=3 {name, domain} dicts: NewsReel/scenes/
       Sources.tsx calls sources.map(), so a bare string throws
       `sources.map is not a function` at ~frame 1450 and kills the slug. V11
       never mounts that scene, so the bug hides until a slug renders V10.1 (or
       a V11 slug falls back) — exactly how it took down the 09-03 control.
    2. `arabicTicker` is z.array(z.string()) in the schema. NewsReel destructures
       it and never renders it today, but authoring it as a list costs nothing
       and removes a second latent `.map` of the same shape.
    3. Persian yeh/kaf must not appear in any Arabic string.
    4. Every statPop matchWord must appear VERBATIM in its voText, otherwise the
       pop is silently dropped and the reel ships with fewer than 2.
    """
    src = props.get("sources")
    if not isinstance(src, list) or len(src) < 3 or not all(
        isinstance(x, dict) and {"name", "domain"} <= set(x) for x in src
    ):
        raise SystemExit(
            f"{slug}: props['sources'] must be a list of >=3 {{name, domain}} dicts, "
            f"got {type(src).__name__} -> Sources.tsx will throw at render time"
        )
    if not isinstance(props.get("arabicTicker"), list):
        raise SystemExit(f"{slug}: props['arabicTicker'] must be a list of strings")

    def walk(node, path="props"):
        if isinstance(node, str):
            if PERSIAN.search(node):
                raise SystemExit(f"{slug}: Persian yeh/kaf in {path}: {node[:60]}")
        elif isinstance(node, dict):
            for k, v in node.items():
                walk(v, f"{path}.{k}")
        elif isinstance(node, list):
            for i, v in enumerate(node):
                walk(v, f"{path}[{i}]")

    walk(props)
    if brief:
        walk(brief, "brief")
        vo = brief["voText"]
        pops = brief.get("statPops", [])
        if len(pops) != 2:
            raise SystemExit(f"{slug}: expected exactly 2 statPops, got {len(pops)}")
        for p in pops:
            if p["matchWord"] not in vo:
                raise SystemExit(
                    f"{slug}: statPop matchWord {p['matchWord']!r} is NOT in voText "
                    f"-> the pop will be silently dropped"
                )
            if vo.count(p["matchWord"]) > 1:
                raise SystemExit(
                    f"{slug}: statPop matchWord {p['matchWord']!r} occurs "
                    f"{vo.count(p['matchWord'])}x in voText -> anchor collision, "
                    f"the pop may fire on the wrong word"
                )
        n = len(vo.split())
        if not 60 <= n <= 95:
            raise SystemExit(f"{slug}: voText is {n} words, want 70-85 (60-95 tolerated)")


SLATE: dict[str, dict] = {}

# ─────────────────────────────────────────────────────────────────────────────
# A · P1 · خبر الـ1,460 ديناراً والمركزي ينفي · 18:00 LEAD
# Sources: شفق نيوز 2026-09-05T14:49Z (نص عربي حرفي) · قناة الفلوجة 2026-09-06 13:26
# ─────────────────────────────────────────────────────────────────────────────
s = f"{D}-a-dollar-rumour-1460"
SLATE[s] = {
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/mood_newsroom.mp3", "topicBucket": "iraq_domestic", "variant": "A",
        "breaking": {
            "arabicKicker": "دولار",
            "arabicHeadline": "خبر الـ1,460 ديناراً.. والمركزي ينفي",
            "englishSubhead": "A CLAIM SPREAD ON IRAQI SOCIAL MEDIA ON SATURDAY THAT THE CENTRAL BANK WOULD PRICE DEPOSITS AT 1,460 DINARS PER DOLLAR FROM SUNDAY | CBI MEDIA DIRECTOR HAIDER GHAZI TOLD SHAFAQ NEWS THE REPORT IS FALSE AND AIMED AT DESTABILISING THE EXCHANGE RATE | THE PARALLEL MARKET ROSE ANYWAY ON SUNDAY | SHAFAQ NEWS, AL-FALLUJAH TV",
            "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
        },
        "beats": [
            beat("ماذا حدث؟",
                 "خبر منتشر: الإيداع بـ1,460 ديناراً",
                 "انتشر يوم السبت في وسائل التواصل خبر مفاده تغيير سعر الصرف، وأن البنك المركزي أبلغ بأن الإيداع يكون على سعر 1,460 ديناراً لكل دولار ابتداءً من اليوم (شفق نيوز · 5 أيلول 2026).",
                 "1,460", "Dinars per dollar in the circulating claim about deposit pricing — a claim the central bank denies",
                 "ديناراً لكل دولار هو السعر الوارد في الخبر المتداول عن تسعير الإيداع، وهو خبر نفاه البنك المركزي (شفق نيوز · 5 أيلول 2026)",
                 [("الخبر", "1,460 د/$"), ("مصدره", "تواصل اجتماعي"), ("حالته", "منفي رسمياً")],
                 s, "broll_1.jpg", ACC[0],
                 ["انتشر يوم السبت خبر عن تغيير سعر الصرف",
                  "مفاده أن الإيداع يكون بـ1,460 ديناراً للدولار",
                  "ابتداءً من اليوم"]),
            beat("الرد الرسمي",
                 "المركزي: كاذب وعارٍ عن الصحة",
                 "نفى مدير إعلام البنك المركزي حيدر غازي يوم السبت تغيير سعر الصرف رسمياً، وقال لشفق نيوز إن الخبر المتداول \"كاذب وعار عن الصحة\"، وإن \"هدفه زعزعة الاستقرار الاقتصادي واستقرار سعر الصرف، لغايات معينة\" (شفق نيوز · 5 أيلول 2026).",
                 "0", "Official changes to the exchange rate announced by the central bank, per its media director",
                 "تغيير رسمي في سعر الصرف أعلنه البنك المركزي، بحسب مدير إعلامه حيدر غازي الذي وصف الخبر المتداول بأنه كاذب (شفق نيوز · 5 أيلول 2026)",
                 [("النافي", "حيدر غازي"), ("صفته", "مدير الإعلام"), ("الجهة", "البنك المركزي")],
                 s, "broll_2.jpg", ACC[1],
                 ["نفى مدير إعلام البنك المركزي حيدر غازي",
                  "تغيير سعر الصرف رسمياً",
                  "ووصف الخبر بأنه كاذب وعار عن الصحة"]),
            beat("السوق اليوم",
                 "البورصة 154,900 لكل 100 دولار",
                 "وفي السوق الموازية اليوم الأحد، ارتفعت بورصتا الكفاح والحارثية إلى 154,900 دينار لكل 100 دولار بعد 154,650 يوم أمس السبت، فيما بلغ البيع في محال الصيرفة ببغداد 155,500 والشراء 154,500 (قناة الفلوجة · 6 أيلول 2026).",
                 "+250", "Dinars per $100 the Al-Kifah and Al-Harithiya bourses added versus Saturday — bourse compared with bourse",
                 "ديناراً لكل 100 دولار هو فرق بورصتي الكفاح والحارثية اليوم مقارنة بأمس السبت، بورصة مقابل بورصة (محتسب من أرقام قناة الفلوجة · 6 أيلول 2026)",
                 [("البورصة اليوم", "154,900"), ("أمس السبت", "154,650"), ("الفرق (محتسب)", "+250")],
                 s, "broll_3.jpg", ACC[2],
                 ["بورصتا الكفاح والحارثية سجّلتا 154,900 دينار",
                  "لكل 100 دولار بعد 154,650 أمس السبت",
                  "ومحال الصيرفة بيع 155,500 وشراء 154,500"]),
        ],
        "arabicTicker": [
            "خبر متداول: الإيداع بـ1,460 ديناراً لكل دولار",
            "البنك المركزي: الخبر كاذب وعار عن الصحة",
            "بورصتا الكفاح والحارثية 154,900 لكل 100 دولار اليوم",
            "محال الصيرفة ببغداد: بيع 155,500 وشراء 154,500",
        ],
        "endQuestion": "وصلك خبر الـ1,460 أمس؟ إي لو لا؟",
        "sources": [
            {"name": "شفق نيوز", "domain": "shafaq.com"},
            {"name": "حيدر غازي — مدير إعلام البنك المركزي (عبر شفق نيوز)", "domain": "shafaq.com"},
            {"name": "قناة الفلوجة", "domain": "alfallujah.tv"},
        ],
    },
    "brief": {
        "slug": s,
        "kicker": "دولار",
        "hookHeadline": "خبر الـ1,460 ديناراً.. المركزي ينفي",
        "voText": "انتشر يوم السبت في وسائل التواصل خبر مفاده أن البنك المركزي العراقي أبلغ بأن الإيداع يكون على سعر ألف وأربعمئة وستين ديناراً لكل دولار ابتداءً من اليوم. ونفى مدير إعلام البنك المركزي حيدر غازي ذلك لوكالة شفق نيوز، واصفاً الخبر بأنه كاذب وعار عن الصحة، وأن هدفه زعزعة الاستقرار الاقتصادي واستقرار سعر الصرف. أما في السوق الموازية اليوم الأحد، فارتفعت بورصتا الكفاح والحارثية إلى مئة وأربعة وخمسين ألفاً وتسعمئة دينار لكل مئة دولار، بعد مئة وأربعة وخمسين ألفاً وستمئة وخمسين أمس. وصلك هذا الخبر أمس؟",
        "endQuestion": "وصلك خبر الـ1,460 أمس؟ إي لو لا؟",
        "sourcesLine": "المصادر: شفق نيوز · البنك المركزي العراقي · قناة الفلوجة",
        "images": [img(s, "hero.jpg"), img(s, "broll_1.jpg"), img(s, "broll_2.jpg"), img(s, "broll_3.jpg")],
        "audioBed": "audio/mood_newsroom.mp3",
        "statPops": [
            {"value": "1,460", "label": "السعر الوارد في الخبر المنفي", "matchWord": "وستين"},
            {"value": "154,900", "label": "بورصتا الكفاح والحارثية اليوم", "matchWord": "وتسعمئة"},
        ],
    },
    "caption": """سعر الدولار في العراق اليوم — شنو قصة خبر الـ1,460؟

خبر انتشر أمس عن تسعير الإيداع، والبنك المركزي طلع ينفيه. والسوق؟ إله رقم ثاني اليوم.

وصلك خبر الـ1,460 أمس؟ إي لو لا؟

المصادر: شفق نيوز (5 أيلول 2026) · قناة الفلوجة (6 أيلول 2026)
#العراق #الدولار #سعر_الصرف #البنك_المركزي #photonectnews
@photonect.news""",
}

# ─────────────────────────────────────────────────────────────────────────────
# B · P2 · صادرات لبنان إلى العراق 516 مليون دولار في الربع الثاني · 19:45
# Source: شفق نيوز 2026-09-06T10:10Z نقلاً عن قاعدة بيانات مركز التجارة الدولية
# ─────────────────────────────────────────────────────────────────────────────
s = f"{D}-b-lebanon-exports-516"
SLATE[s] = {
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/music_01.mp3", "topicBucket": "global_economy", "variant": "B",
        "breaking": {
            "arabicKicker": "تجارة",
            "arabicHeadline": "بضاعة لبنان للعراق قفزت لـ516 مليوناً",
            "englishSubhead": "LEBANESE EXPORTS TO IRAQ REACHED ABOUT $516 MILLION IN Q2 2026 AGAINST $350 MILLION IN Q1, A RISE OF $166 MILLION OR 47.4% | PEARLS, PRECIOUS STONES, JEWELLERY AND COINS LED AT $214 MILLION AGAINST $44 MILLION IN Q1 | SHAFAQ NEWS CITING THE INTERNATIONAL TRADE CENTRE TRADE MAP, SUN 6 SEP",
            "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
        },
        "beats": [
            beat("ماذا يحدث؟",
                 "516 مليون دولار في ثلاثة أشهر",
                 "بلغت صادرات لبنان إلى العراق نحو 516 مليون دولار في الربع الثاني من 2026، مقابل 350 مليوناً في الربع الأول، أي زيادة 166 مليوناً بنسبة 47.4% (شفق نيوز نقلاً عن مركز التجارة الدولية · 6 أيلول 2026).",
                 "47.4%", "Quarter-on-quarter rise in Lebanese exports to Iraq, Q2 2026 against Q1",
                 "نسبة ارتفاع صادرات لبنان إلى العراق في الربع الثاني من 2026 مقارنة بالربع الأول، من 350 إلى 516 مليون دولار (شفق نيوز · مركز التجارة الدولية · 6 أيلول 2026)",
                 [("الربع الثاني", "516 م$"), ("الربع الأول", "350 م$"), ("الزيادة", "166 م$")],
                 s, "broll_1.jpg", ACC[0],
                 ["صادرات لبنان إلى العراق 516 مليون دولار",
                  "في الربع الثاني مقابل 350 مليوناً في الأول",
                  "أي زيادة 166 مليوناً بنسبة 47.4%"]),
            beat("ما الذي تصدّر؟",
                 "المجوهرات والمعادن الثمينة أولاً",
                 "تصدّر بند اللآلئ والأحجار والمعادن الكريمة ومصنوعاتها والمجوهرات والمسكوكات قائمة الصادرات بـ214 مليون دولار في الربع الثاني، مقابل 44 مليوناً في الربع الأول (شفق نيوز · مركز التجارة الدولية · 6 أيلول 2026).",
                 "214", "Millions of dollars of pearls, precious stones, jewellery and coins — the single largest export line in Q2",
                 "مليون دولار قيمة بند اللآلئ والأحجار والمعادن الكريمة والمجوهرات والمسكوكات، وهو أكبر بند مفرد في الربع الثاني (شفق نيوز · مركز التجارة الدولية · 6 أيلول 2026)",
                 [("البند الأول", "214 م$"), ("بالربع الأول", "44 م$"), ("ترتيبه", "الأول")],
                 s, "broll_2.jpg", ACC[1],
                 ["بند اللآلئ والمعادن الكريمة والمجوهرات",
                  "تصدّر القائمة بـ214 مليون دولار",
                  "مقابل 44 مليوناً في الربع الأول"]),
            beat("الصورة الأوسع",
                 "866 مليوناً في نصف سنة",
                 "بجمع الربعين يبلغ إجمالي صادرات لبنان إلى العراق في النصف الأول من 2026 نحو 866 مليون دولار، وتشمل أيضاً النحاس والآلات الكهربائية والرصاص والأسمدة ومحضرات الخضار والفواكه والحديد والألمنيوم والملابس (شفق نيوز · 6 أيلول 2026).",
                 "866", "Millions of dollars of Lebanese exports to Iraq across the first half of 2026 — the two published quarters added together",
                 "مليون دولار إجمالي صادرات لبنان إلى العراق في النصف الأول من 2026، وهو حاصل جمع الربعين المنشورين (محتسب من أرقام شفق نيوز · 6 أيلول 2026)",
                 [("النصف الأول", "866 م$"), ("الاحتساب", "350+516"), ("المصدر", "مركز التجارة")],
                 s, "broll_3.jpg", ACC[2],
                 ["إجمالي النصف الأول نحو 866 مليون دولار",
                  "وهو حاصل جمع الربعين المنشورين",
                  "وتشمل السلع النحاس والأسمدة والملابس"]),
        ],
        "arabicTicker": [
            "صادرات لبنان إلى العراق 516 مليون دولار في الربع الثاني",
            "مقابل 350 مليوناً في الربع الأول بزيادة 47.4%",
            "المجوهرات والمعادن الكريمة أكبر بند بـ214 مليون دولار",
            "إجمالي النصف الأول نحو 866 مليون دولار (محتسب)",
        ],
        "endQuestion": "تشتري بضاعة لبنانية؟ إي لو لا؟",
        "sources": [
            {"name": "شفق نيوز", "domain": "shafaq.com"},
            {"name": "مركز التجارة الدولية — قاعدة بيانات Trade Map", "domain": "trademap.org"},
            {"name": "أرقام الربعين كما نشرتها شفق نيوز", "domain": "shafaq.com"},
        ],
    },
    "brief": {
        "slug": s,
        "kicker": "تجارة",
        "hookHeadline": "بضاعة لبنان للعراق قفزت بربع واحد",
        "voText": "بلغت صادرات لبنان إلى العراق في الربع الثاني من هذا العام نحو خمسمئة وستة عشر مليون دولار، مقابل ثلاثمئة وخمسين مليوناً في الربع الأول، أي بزيادة مئة وستة وستين مليوناً ونسبة تقارب سبعة وأربعين بالمئة. وتصدّر بند اللآلئ والأحجار والمعادن الكريمة والمجوهرات والمسكوكات القائمة بمئتين وأربعة عشر مليون دولار، مقابل أربعة وأربعين مليوناً في الربع الأول. وبجمع الربعين يقترب إجمالي النصف الأول من ثمانمئة وستة وستين مليون دولار، بحسب شفق نيوز نقلاً عن قاعدة بيانات مركز التجارة الدولية. تشتري بضاعة لبنانية؟",
        "endQuestion": "تشتري بضاعة لبنانية؟ إي لو لا؟",
        "sourcesLine": "المصادر: شفق نيوز · مركز التجارة الدولية",
        "images": [img(s, "hero.jpg"), img(s, "broll_1.jpg"), img(s, "broll_2.jpg"), img(s, "broll_3.jpg")],
        "audioBed": "audio/music_01.mp3",
        "statPops": [
            {"value": "$516M", "label": "صادرات لبنان للعراق — الربع الثاني", "matchWord": "وستة عشر"},
            {"value": "$214M", "label": "المجوهرات والمعادن الكريمة", "matchWord": "والمسكوكات"},
        ],
    },
    "caption": """صادرات لبنان إلى العراق — شنو صار بربع واحد؟

الرقم قفز بين الربع الأول والثاني، وأكبر بند داخل للعراق مو اللي تتوقعه.

تشتري بضاعة لبنانية؟ إي لو لا؟

المصادر: شفق نيوز (6 أيلول 2026) نقلاً عن مركز التجارة الدولية
#العراق #لبنان #تجارة #استيراد #photonectnews
@photonect.news""",
}

# ─────────────────────────────────────────────────────────────────────────────
# C · P1 · محاسب متهم بصرف راتب موظف وهمي 6 سنوات · 21:15
# Source: هيئة النزاهة الاتحادية عبر وكالة الأنباء العراقية (واع) وشبكة لالش
#         2026-09-05. لا مبلغ منشور. المتهم لم تصدر بحقه إدانة — يُقال ذلك صراحة.
# ─────────────────────────────────────────────────────────────────────────────
s = f"{D}-c-ghost-employee-six-years"
SLATE[s] = {
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/music_03.mp3", "topicBucket": "iraq_domestic", "variant": "A",
        "breaking": {
            "arabicKicker": "نزاهة",
            "arabicHeadline": "راتب موظف وهمي.. 6 سنوات وما انتبهوا",
            "englishSubhead": "IRAQ'S FEDERAL INTEGRITY COMMISSION SAYS IT DETAINED AN ACCOUNTANT AT THE AL-HADAR EDUCATION SECTION IN AL-QAYYARAH, NINEVEH, ACCUSED OF DRAWING A GHOST EMPLOYEE'S MONTHLY SALARY FROM LATE 2017 UNTIL 2023 | NO AMOUNT PUBLISHED | HELD PENDING INVESTIGATION UNDER ARTICLE 315 | NO CONVICTION | INA, LALISH NETWORK, SAT 5 SEP",
            "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
        },
        "beats": [
            beat("ماذا حدث؟",
                 "ضبط محاسب في تربية نينوى",
                 "أعلنت هيئة النزاهة الاتحادية ضبط محاسب في قسم تربية الحضر بالقيارة، التابع للمديرية العامة لتربية محافظة نينوى، بتهمة صرف وسحب رواتب شهرية باسم شخص وهمي (وكالة الأنباء العراقية · شبكة لالش · 5 أيلول 2026).",
                 "1", "Accountant detained, per the Federal Integrity Commission — an accusation, not a conviction",
                 "محاسب واحد جرى ضبطه بحسب هيئة النزاهة الاتحادية، وهي تهمة قيد التحقيق لا إدانة صادرة (وكالة الأنباء العراقية · 5 أيلول 2026)",
                 [("الجهة", "هيئة النزاهة"), ("المكان", "تربية الحضر"), ("المحافظة", "نينوى")],
                 s, "broll_1.jpg", ACC[0],
                 ["هيئة النزاهة الاتحادية أعلنت ضبط محاسب",
                  "في قسم تربية الحضر بالقيارة بنينوى",
                  "بتهمة صرف رواتب باسم شخص وهمي"]),
            beat("كم استمرت؟",
                 "من أواخر 2017 حتى 2023",
                 "وبحسب الهيئة، استمر صرف الراتب الشهري باسم شخص وهمي من أواخر عام 2017 وحتى عام 2023، أي نحو ست سنوات. ولم تُعلن الهيئة قيمة المبالغ المصروفة (وكالة الأنباء العراقية · 5 أيلول 2026).",
                 "6", "Years the ghost salary was drawn, late 2017 to 2023 — no amount has been published",
                 "سنوات تقريباً استمر خلالها صرف الراتب باسم شخص وهمي، من أواخر 2017 حتى 2023، ولم تُعلن قيمة المبالغ (وكالة الأنباء العراقية · 5 أيلول 2026)",
                 [("البداية", "أواخر 2017"), ("النهاية", "2023"), ("المبلغ", "لم يُعلن")],
                 s, "broll_2.jpg", ACC[1],
                 ["استمر الصرف من أواخر 2017 حتى 2023",
                  "أي نحو ست سنوات",
                  "ولم تُعلن الهيئة قيمة المبالغ"]),
            beat("وشنو صار بيه؟",
                 "توقيف على ذمة التحقيق",
                 "قرر قاضي التحقيق توقيف المتهم على ذمة التحقيق استناداً إلى أحكام المادة 315 من قانون العقوبات العراقي. وهو ما زال متهماً ولم تصدر بحقه إدانة (وكالة الأنباء العراقية · شبكة لالش · 5 أيلول 2026).",
                 "315", "Article of the Iraqi penal code cited in the detention order",
                 "مادة قانون العقوبات العراقي التي استند إليها قرار التوقيف على ذمة التحقيق (وكالة الأنباء العراقية · 5 أيلول 2026)",
                 [("القرار", "توقيف"), ("المادة", "315"), ("صفته", "متهم")],
                 s, "broll_3.jpg", ACC[2],
                 ["قاضي التحقيق قرر التوقيف على ذمة التحقيق",
                  "استناداً إلى المادة 315 من قانون العقوبات",
                  "وهو ما زال متهماً ولم تصدر بحقه إدانة"]),
        ],
        "arabicTicker": [
            "هيئة النزاهة تضبط محاسباً في تربية نينوى",
            "بتهمة صرف رواتب باسم شخص وهمي من أواخر 2017 حتى 2023",
            "لم تُعلن قيمة المبالغ المصروفة",
            "توقيف على ذمة التحقيق وفق المادة 315 — لا إدانة صادرة",
        ],
        "endQuestion": "بدائرتكم أكو اسم ما تشوفونه؟ إي لو لا؟",
        "sources": [
            {"name": "هيئة النزاهة الاتحادية", "domain": "nazaha.iq"},
            {"name": "وكالة الأنباء العراقية (واع)", "domain": "ina.iq"},
            {"name": "شبكة لالش الإعلامية", "domain": "lalishduhok.com"},
        ],
    },
    "brief": {
        "slug": s,
        "kicker": "نزاهة",
        "hookHeadline": "راتب موظف وهمي.. ست سنوات",
        "voText": "أعلنت هيئة النزاهة الاتحادية ضبط محاسب في قسم تربية الحضر بالقيارة، التابع للمديرية العامة لتربية محافظة نينوى، بتهمة صرف وسحب رواتب شهرية باسم شخص وهمي. وبحسب الهيئة استمر ذلك من أواخر عام ألفين وسبعة عشر وحتى عام ألفين وثلاثة وعشرين، أي نحو ست سنوات، ولم تُعلن قيمة المبالغ المصروفة. وقرر قاضي التحقيق توقيفه على ذمة التحقيق استناداً إلى المادة ثلاثمئة وخمسة عشر من قانون العقوبات العراقي. وهو ما زال متهماً ولم تصدر بحقه إدانة. بدائرتكم أكو اسم ما تشوفونه؟",
        "endQuestion": "بدائرتكم أكو اسم ما تشوفونه؟ إي لو لا؟",
        "sourcesLine": "المصادر: هيئة النزاهة الاتحادية · وكالة الأنباء العراقية · شبكة لالش",
        "images": [img(s, "hero.jpg"), img(s, "broll_1.jpg"), img(s, "broll_2.jpg"), img(s, "broll_3.jpg")],
        "audioBed": "audio/music_03.mp3",
        "statPops": [
            {"value": "6 سنوات", "label": "مدة صرف الراتب الوهمي", "matchWord": "سنوات"},
            {"value": "المادة 315", "label": "أساس قرار التوقيف", "matchWord": "العقوبات"},
        ],
    },
    "caption": """موظف وهمي براتب شهري — ست سنوات وما انتبهوا

هيئة النزاهة تقول ضبطت محاسباً بتربية نينوى. المبلغ؟ لحد الآن ما انعلن. والرجل متهم، ما عليه إدانة.

بدائرتكم أكو اسم ما تشوفونه؟ إي لو لا؟

المصادر: هيئة النزاهة الاتحادية عبر وكالة الأنباء العراقية وشبكة لالش (5 أيلول 2026)
#العراق #النزاهة #نينوى #فساد #photonectnews
@photonect.news""",
}

# ─────────────────────────────────────────────────────────────────────────────
# D · P3 · العراق بسبع ألعاب في آسياد اليابان · 22:30
# Source: شفق نيوز 2026-09-06T10:44Z — زيدون جواد، رئيس البعثة العراقية
# First P3 slug in four days. Lens test: national pride, a dated fixture every
# viewer can act on (what to watch, starting 19 Sep).
# ─────────────────────────────────────────────────────────────────────────────
s = f"{D}-d-asiad-japan-seven-sports"
SLATE[s] = {
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/music_05.mp3", "topicBucket": "wildcard", "variant": "B",
        "breaking": {
            "arabicKicker": "رياضة",
            "arabicHeadline": "العراق بسبع ألعاب في آسياد اليابان",
            "englishSubhead": "IRAQ WILL CONTEST SEVEN SPORTS AT THE 20TH ASIAN GAMES IN JAPAN — ATHLETICS, WEIGHTLIFTING, BOXING, WRESTLING, ROWING, JIU-JITSU AND TEQBALL — MISSION CHIEF ZAIDOUN JAWAD TOLD SHAFAQ NEWS | GAMES RUN 19 SEPTEMBER TO 4 OCTOBER WITH 11,000 ATHLETES FROM 45 COUNTRIES | SUN 6 SEP",
            "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
        },
        "beats": [
            beat("ماذا يحدث؟",
                 "سبع ألعاب تمثّل العراق",
                 "يشارك العراق في دورة الألعاب الآسيوية العشرين باليابان بسبع ألعاب هي ألعاب القوى ورفع الأثقال والملاكمة والمصارعة والتجديف والجوجيتسو والتك بول، بحسب رئيس البعثة زيدون جواد (شفق نيوز · 6 أيلول 2026).",
                 "7", "Sports Iraq will contest at the 20th Asian Games, per mission chief Zaidoun Jawad",
                 "ألعاب يشارك بها العراق في دورة الألعاب الآسيوية العشرين، بحسب رئيس البعثة زيدون جواد (شفق نيوز · 6 أيلول 2026)",
                 [("الألعاب", "7"), ("رئيس البعثة", "زيدون جواد"), ("الدورة", "الآسيوية 20")],
                 s, "broll_1.jpg", ACC[0],
                 ["العراق يشارك بسبع ألعاب في آسياد اليابان",
                  "ألعاب القوى ورفع الأثقال والملاكمة والمصارعة",
                  "والتجديف والجوجيتسو والتك بول"]),
            beat("متى تبدأ؟",
                 "19 أيلول حتى 4 تشرين الأول",
                 "تنطلق الدورة في 19 أيلول وتختتم في 4 تشرين الأول، وقال جواد إن البعثة أنهت استعداداتها (شفق نيوز · 6 أيلول 2026).",
                 "19", "September start date of the Games, which close on 4 October",
                 "أيلول موعد انطلاق الدورة التي تختتم في الرابع من تشرين الأول، والبعثة أنهت استعداداتها بحسب رئيسها (شفق نيوز · 6 أيلول 2026)",
                 [("الانطلاق", "19 أيلول"), ("الختام", "4 تشرين1"), ("البعثة", "أنهت الاستعداد")],
                 s, "broll_2.jpg", ACC[1],
                 ["تنطلق الدورة في 19 أيلول",
                  "وتختتم في 4 تشرين الأول",
                  "والبعثة أنهت استعداداتها"]),
            beat("كم حجمها؟",
                 "11 ألف رياضي من 45 دولة",
                 "تشهد الدورة مشاركة 11 ألف رياضي من 45 دولة، وتستضيف اليابان الألعاب الآسيوية للمرة الثالثة في تاريخها بعد نسختي طوكيو 1958 وهيروشيما 1994 (شفق نيوز · 6 أيلول 2026).",
                 "11,000", "Athletes taking part, from 45 countries",
                 "رياضي يشاركون في الدورة قادمين من 45 دولة، واليابان تستضيفها للمرة الثالثة بعد طوكيو 1958 وهيروشيما 1994 (شفق نيوز · 6 أيلول 2026)",
                 [("الرياضيون", "11 ألفاً"), ("الدول", "45"), ("استضافة اليابان", "الثالثة")],
                 s, "broll_3.jpg", ACC[2],
                 ["مشاركة 11 ألف رياضي من 45 دولة",
                  "واليابان تستضيف الآسياد للمرة الثالثة",
                  "بعد طوكيو 1958 وهيروشيما 1994"]),
        ],
        "arabicTicker": [
            "العراق يشارك بسبع ألعاب في دورة الألعاب الآسيوية العشرين",
            "ألعاب القوى ورفع الأثقال والملاكمة والمصارعة والتجديف والجوجيتسو والتك بول",
            "الدورة من 19 أيلول حتى 4 تشرين الأول",
            "11 ألف رياضي من 45 دولة واليابان تستضيف للمرة الثالثة",
        ],
        "endQuestion": "أي لعبة راح تتابعها؟ اكتبها بكلمة",
        "sources": [
            {"name": "شفق نيوز", "domain": "shafaq.com"},
            {"name": "زيدون جواد — رئيس البعثة العراقية (عبر شفق نيوز)", "domain": "shafaq.com"},
            {"name": "اللجنة الأولمبية الوطنية العراقية (البعثة)", "domain": "shafaq.com"},
        ],
    },
    "brief": {
        "slug": s,
        "kicker": "رياضة",
        "hookHeadline": "العراق بسبع ألعاب في آسياد اليابان",
        "voText": "يشارك العراق في دورة الألعاب الآسيوية العشرين في اليابان بسبع ألعاب، هي ألعاب القوى ورفع الأثقال والملاكمة والمصارعة والتجديف والجوجيتسو والتك بول، بحسب رئيس البعثة العراقية زيدون جواد لشفق نيوز. وقال جواد إن البعثة أنهت استعداداتها. وتنطلق الدورة في التاسع عشر من أيلول وتختتم في الرابع من تشرين الأول، بمشاركة أحد عشر ألف رياضي من خمس وأربعين دولة. وتستضيف اليابان الألعاب الآسيوية للمرة الثالثة في تاريخها، بعد نسختي طوكيو وهيروشيما. أي لعبة راح تتابعها؟",
        "endQuestion": "أي لعبة راح تتابعها؟ اكتبها بكلمة",
        "sourcesLine": "المصادر: شفق نيوز · زيدون جواد رئيس البعثة العراقية",
        "images": [img(s, "hero.jpg"), img(s, "broll_1.jpg"), img(s, "broll_2.jpg"), img(s, "broll_3.jpg")],
        "audioBed": "audio/music_05.mp3",
        "statPops": [
            {"value": "7", "label": "ألعاب يمثَّل بها العراق", "matchWord": "بسبع"},
            {"value": "11,000", "label": "رياضي من 45 دولة", "matchWord": "رياضي"},
        ],
    },
    "caption": """العراق في آسياد اليابان — بأي ألعاب راح نلعب؟

البعثة أنهت استعداداتها، والقائمة أقصر مما يتوقع البعض. والموعد قريب.

أي لعبة راح تتابعها؟ اكتبها بكلمة

المصادر: شفق نيوز (6 أيلول 2026) · زيدون جواد رئيس البعثة
#العراق #الألعاب_الآسيوية #رياضة_عراقية #آسياد #photonectnews
@photonect.news""",
}

# ─────────────────────────────────────────────────────────────────────────────
# E · P1 · هيئة الأوراق المالية تحذّر من الشركات الوهمية · 23:45 — V10.1 CONTROL
# Source: شفق نيوز 2026-09-06T09:37Z — بيان رسمي لرئيس الهيئة فيصل الهيمص
# This is the silent control: the ONLY story on the slate with no published
# figure of any kind, which is the criterion used since 09-01. Its two derived
# bigStats are labelled (محتسب) and count only what the statement itself lists.
# ─────────────────────────────────────────────────────────────────────────────
s = f"{D}-e-fake-investment-firms"
SLATE[s] = {
    "props": {
        "dateLabel": DATE_LABEL, "arabicDateLabel": AR_DATE, "handle": HANDLE,
        "audioBed": "audio/mood_orchestral.mp3", "topicBucket": "iraq_domestic", "variant": "C",
        "breaking": {
            "arabicKicker": "تحذير",
            "arabicHeadline": "قبل ما تودّع فلوسك.. تحذير رسمي",
            "englishSubhead": "IRAQI SECURITIES COMMISSION CHAIRMAN FAISAL AL-HAIMUS WARNED CITIZENS AND INVESTORS AGAINST PHANTOM COMPANIES AND UNLICENSED ENTITIES PROMOTING INVESTMENT SERVICES | HE NAMED THE RED FLAGS: PROMISES OF HIGH QUICK RETURNS, TRANSFERS TO PERSONAL ACCOUNTS OR UNKNOWN E-WALLETS, AND UPFRONT PAYMENTS | NO CASE COUNT OR LOSS FIGURE WAS PUBLISHED | SHAFAQ NEWS, SUN 6 SEP",
            "heroMedia": img(s, "hero.jpg"), "heroMediaType": "image",
        },
        "beats": [
            beat("ماذا حدث؟",
                 "الهيمص يحذّر من جهات غير مرخصة",
                 "حذّر رئيس هيئة الأوراق المالية فيصل الهيمص المواطنين والمستثمرين من التعامل مع الشركات الوهمية والجهات غير المرخصة التي تروّج لخدمات وفرص استثمارية، مؤكداً ضرورة التحقق من قانونية الجهة قبل إيداع الأموال (شفق نيوز · 6 أيلول 2026).",
                 "0", "Legal licences held by the entities the commission chairman warned about — he describes them as unlicensed",
                 "تراخيص قانونية لدى الجهات التي حذّر منها رئيس الهيئة، فهو يصفها بأنها غير مرخصة (شفق نيوز · 6 أيلول 2026)",
                 [("المحذِّر", "فيصل الهيمص"), ("الجهة", "الأوراق المالية"), ("التاريخ", "6 أيلول")],
                 s, "broll_1.jpg", ACC[0],
                 ["رئيس هيئة الأوراق المالية فيصل الهيمص",
                  "حذّر من الشركات الوهمية والجهات غير المرخصة",
                  "وشدد على التحقق قبل إيداع الأموال"]),
            beat("كيف تشتغل؟",
                 "أسماء ومنصات وصفحات تواصل",
                 "أوضح الهيمص أن بعض الجهات تستخدم أسماء تجارية ومنصات إلكترونية وصفحات على مواقع التواصل لإيهام المستثمرين بأنها مؤسسات مالية معتمدة، مع تقديم وعود بعوائد مرتفعة وسريعة (شفق نيوز · 6 أيلول 2026).",
                 "3", "Disguises the statement lists: trade names, online platforms and social-media pages",
                 "واجهات عدّدها البيان: أسماء تجارية ومنصات إلكترونية وصفحات على مواقع التواصل (محتسب من نص البيان · شفق نيوز · 6 أيلول 2026)",
                 [("الواجهات", "3 (محتسب)"), ("الطُعم", "عوائد مرتفعة"), ("الادعاء", "مؤسسة معتمدة")],
                 s, "broll_2.jpg", ACC[1],
                 ["أسماء تجارية ومنصات إلكترونية وصفحات تواصل",
                  "لإيهام المستثمرين بأنها مؤسسات معتمدة",
                  "مع وعود بعوائد مرتفعة وسريعة"]),
            beat("شنو علامات الخطر؟",
                 "حساب شخصي ودفعة مقدّمة",
                 "شدد الهيمص على الحذر من الجهات التي تطلب تحويل الأموال إلى حسابات شخصية أو محافظ إلكترونية غير معروفة أو تشترط دفع مبالغ مسبقة، داعياً إلى الاستفسار من الجهات الرقابية عن الشركات المرخصة قبل التعامل معها (شفق نيوز · 6 أيلول 2026).",
                 "3", "Red flags the statement names: personal accounts, unknown e-wallets, and required upfront payments",
                 "علامات خطر ذكرها البيان: التحويل إلى حساب شخصي، أو إلى محفظة إلكترونية غير معروفة، أو اشتراط دفع مبالغ مسبقة (محتسب من نص البيان · شفق نيوز · 6 أيلول 2026)",
                 [("علامة 1", "حساب شخصي"), ("علامة 2", "محفظة مجهولة"), ("علامة 3", "دفعة مسبقة")],
                 s, "broll_3.jpg", ACC[2],
                 ["احذر من طلب التحويل إلى حساب شخصي",
                  "أو محفظة إلكترونية غير معروفة",
                  "أو اشتراط دفع مبالغ مسبقة",
                  "واستفسر من الجهات الرقابية قبل التعامل"]),
        ],
        "arabicTicker": [
            "رئيس هيئة الأوراق المالية فيصل الهيمص يحذّر من الشركات الوهمية",
            "جهات تستخدم أسماء ومنصات وصفحات تواصل لإيهام المستثمرين",
            "علامات الخطر: حساب شخصي أو محفظة مجهولة أو دفعة مسبقة",
            "الهيئة تدعو للاستفسار عن الشركات المرخصة قبل التعامل",
        ],
        "endQuestion": "وصلك عرض استثمار عبر التواصل؟ إي لو لا؟",
        "sources": [
            {"name": "شفق نيوز", "domain": "shafaq.com"},
            {"name": "فيصل الهيمص — رئيس هيئة الأوراق المالية (بيان رسمي)", "domain": "isc.gov.iq"},
            {"name": "هيئة الأوراق المالية العراقية", "domain": "isc.gov.iq"},
        ],
    },
    "brief": None,
    "caption": """عروض استثمار على السوشيال ميديا — منو يضمنلك؟

هيئة الأوراق المالية طلعت ببيان رسمي اليوم، وحددت علامات تخليك توقف قبل ما تحوّل أي مبلغ.

وصلك عرض استثمار عبر التواصل؟ إي لو لا؟

المصادر: شفق نيوز (6 أيلول 2026) · بيان رئيس هيئة الأوراق المالية فيصل الهيمص
#العراق #استثمار #احتيال #الأوراق_المالية #photonectnews
@photonect.news""",
}


def main() -> int:
    for slug, payload in SLATE.items():
        _validate(slug, payload["props"], payload["brief"])
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
