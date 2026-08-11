#!/usr/bin/env python3
"""Apply the two Opus editorial QA gates' findings to the 2026-08-11 slate.

Run ONCE, after author_2026_08_11.py and the copywriter pass. Idempotent-ish:
every edit is an exact-string replacement that no-ops if already applied, and
the script reports any patch that did not find its target.

The single most important fix is [OIL-1]: the claim that Iraq had been the TOP
crude supplier to the United States per 2024 data. That came from a fetch
summary, not from a figure in the Shafaq piece, and it is contradicted by the
slug's own numbers — a supplier at 45,000 b/d cannot lead a market importing
millions of b/d. The claim is CUT everywhere rather than softened.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "data" / "posts"
D = "2026-08-11"

problems: list[str] = []


def load(slug: str, name: str):
    p = POSTS / f"{D}-{slug}" / ".meta" / name
    return p, json.loads(p.read_text(encoding="utf-8"))


def save(p: Path, data) -> None:
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sub(obj: dict, path: list, old: str, new: str, tag: str) -> None:
    """Replace `old` with `new` at dotted/indexed `path`; record a miss."""
    cur = obj
    for k in path[:-1]:
        cur = cur[k]
    last = path[-1]
    val = cur[last]
    if old not in val:
        if new in val:
            return  # already applied
        problems.append(f"{tag}: target not found -> {old[:60]!r}")
        return
    cur[last] = val.replace(old, new)


def setv(obj: dict, path: list, new, tag: str) -> None:
    cur = obj
    for k in path[:-1]:
        cur = cur[k]
    cur[path[-1]] = new


# ══════════════════════════════════════════════════ 1 · budget-78-salaries
p, b = load("budget-78-salaries", "props.json")

# [BUD-1] headline: source says the delay EXCEEDED 40 days; and "المستشار يقول"
#         in an adversarial position editorialises against a named official.
setv(b, ["breaking", "arabicHeadline"], "تأخير تجاوز 40 يوماً.. والمستشار: مؤمّنة", "BUD-1")

# [BUD-2] englishSubhead: the ministry ANNOUNCED SECURING funds for PART of the
#         bill. "RELEASED" asserts a disbursement that has not reached anyone.
setv(b, ["breaking", "englishSubhead"],
     "MONTHLY SALARY BILL 7.8TN IQD | MINISTRY SAYS 3.2TN SECURED FOR PART OF IT | DELAY PAST 40 DAYS",
     "BUD-2")

# [BUD-3] beat 3 pill asserted a cause the source never draws: it labelled the
#         Hormuz crisis as "السبب" of the 4.6tn salary gap.
setv(b, ["beats", 2, "supportingStats", 2], {"label": "الموانئ المتأثرة", "value": "الجنوبية"}, "BUD-3")

# [BUD-4] beat 3 heading: "فجوة" asserts 4.6tn is unfunded; the source says the
#         ministry secured 3.2tn to pay PART. The body already says "الفارق".
setv(b, ["beats", 2, "arabicHeading"], "الفارق 4.6 ترليون.. وتنويع منافذ التصدير", "BUD-4")
save(p, b)

p, v = load("budget-78-salaries", "v11-brief.json")
# [BUD-5] BLOCKER: the "وإن" put Kirkuk–Ceyhan INSIDE Salih's quote. He is
#         sourced for the reassurance and for the revenue/route framing; the
#         Kirkuk–Ceyhan line is the article's, not his. Split the sentences.
sub(v, ["voText"],
    "وإن الرهان على تعزيز الإيرادات وتنويع طرق التصدير، ومنها خط كركوك جيهان بعيداً عن هرمز، بحسب شفق نيوز.",
    "وإن الرهان على تعزيز الإيرادات وتنويع طرق التصدير. ويُطرح خط كركوك جيهان بين أبرز الخيارات بعيداً عن الموانئ الجنوبية المتأثرة بأزمة هرمز، بحسب شفق نيوز.",
    "BUD-5")
# [BUD-6] statPop anchor "الالتزامات" is word 1 of 85 — the 7.8tn pop fired
#         before the narrator spoke any number. Move it onto the figure itself.
for sp in v["statPops"]:
    if sp["matchWord"] == "الالتزامات":
        sp["matchWord"] = "سبعة"
setv(v, ["hookHeadline"], "التأخير تجاوز 40 يوم.. وين راتبك؟", "BUD-6")
save(p, v)

# ══════════════════════════════════════════════════ 2 · dollar-third-day
p, b = load("dollar-third-day", "props.json")
# [DOL-1] 7,500 is derived; its sibling pill in the SAME row carries (محتسب),
#         so leaving this one bare implies it is a published Shafaq figure.
setv(b, ["beats", 2, "supportingStats", 0], {"label": "لكل 1000$ (محتسب)", "value": "7,500"}, "DOL-1")
# [DOL-2] the 600 pill had no unit and no referent — it read as a second delta
#         on the $1,000 basis rather than the Baghdad-vs-Erbil gap.
setv(b, ["beats", 2, "supportingStats", 2],
     {"label": "بغداد أغلى من أربيل (محتسب)", "value": "600 لكل 100$"}, "DOL-2")
# [DOL-3] the 750 inside this label carried a bare Shafaq stamp although it is
#         itself computed (153,250 − 152,500). Tagged (محتسب) everywhere else.
sub(b, ["beats", 2, "bigStat", "arabicLabel"],
    "مستخرجة من فارق البورصة البالغ 750 ديناراً لكل 100 دولار (شفق نيوز، 11 آب 2026)",
    "مستخرجة من فارق البورصة البالغ 750 ديناراً لكل 100 دولار وهو رقم محتسب من سعري الثلاثاء والاثنين (شفق نيوز، 11 آب 2026)",
    "DOL-3")
# [DOL-4] beat 2 heading was a literal substring of the headline read 4s earlier.
setv(b, ["beats", 1, "arabicHeading"], "تشتري بـ152,750 وتبيع بـ153,750", "DOL-4")
save(p, b)

# ══════════════════════════════════════════════════ 3 · oil-zero-barrels
p, b = load("oil-zero-barrels", "props.json")
# [OIL-1] BLOCKER — CUT the "Iraq had topped the list" claim. Not a figure in
#         the piece, and refuted by this reel's own 45,000 b/d.
sub(b, ["beats", 1, "arabicBody"],
    "خرج العراق من قائمة أكبر موردي الخام لأميركا بعد أن تصدّرها في بيانات 2024",
    "خرج العراق من قائمة أكبر موردي الخام إلى الولايات المتحدة", "OIL-1a")
b["arabicTicker"] = [t for t in b["arabicTicker"] if "مقدمة الموردين" not in t and "2024" not in t]
b["arabicTicker"].insert(3, "خام البصرة الثقيل عند 55.09 دولاراً للبرميل (شفق نيوز)")
# [OIL-2] headline dropped "average": EIA reports monthly averages rounded to
#         thousands of b/d, so zero means "below the rounding floor".
setv(b, ["breaking", "arabicHeadline"], "متوسط صفر برميل عراقي إلى أميركا بتموز", "OIL-2")
# [OIL-3] "وسط صعود عالمي" asserted a rally, and framed it as the driver of the
#         Basrah move. Only the two Basrah grades carry sourced direction.
setv(b, ["beats", 2, "arabicBody"],
     "ارتفع خام البصرة المتوسط 0.53% إلى 57.39 دولاراً للبرميل والثقيل 0.55% إلى 55.09 دولاراً يوم الثلاثاء، فيما سُجّل برنت عند 87.94 دولاراً، بحسب شفق نيوز.",
     "OIL-3")
# [OIL-4] the oil→salary bridge. The source draws no link between the export
#         figure and wages, and the lead reel already asks a salary question.
NEWQ = "شكد تدفع بالأسبوع بنزين لسيارتك؟"
b["arabicTicker"] = [NEWQ if "براتبك حسّيت" in t else t for t in b["arabicTicker"]]
save(p, b)

p, v = load("oil-zero-barrels", "v11-brief.json")
sub(v, ["voText"], "بعد أن كان في مقدمتها وفق بيانات ألفين وأربعة وعشرين", "بعد أن كان مدرجاً ضمنها", "OIL-1b")
sub(v, ["voText"], "وفي السوق نفسه،", "وعلى صعيد الأسعار،", "OIL-5")          # false "same market" stitch
sub(v, ["voText"], "فاصلة أربعة وتسعين، بحسب شفق نيوز", "فاصلة أربعة وتسعين دولاراً، بحسب شفق نيوز", "OIL-6")
sub(v, ["voText"], "فبراتبك حسّيت بفرق من تغيّر سعر النفط؟", f"ف{NEWQ}", "OIL-4b")
setv(v, ["endQuestion"], NEWQ, "OIL-4c")
save(p, v)

# ══════════════════════════════════════════════════ 4 · showroom-sales-28
p, b = load("showroom-sales-28", "props.json")
# [CAR-1] "بنص سنة" reads as a within-period fall; the figure is H1-26 vs H1-25.
setv(b, ["breaking", "arabicHeadline"], "مبيعات السيارات بالعراق هوت 28.6% بالنصف الأول", "CAR-1")
# [CAR-2] beat 2's heading promised Hyundai; the body buried it 18 words deep
#         behind three other percentages in the 22–28 band.
setv(b, ["beats", 1, "arabicBody"],
     "سجّلت هيونداي أكبر هبوط بنسبة 69.7%، فيما تصدّرت كيا بحصة 28% من المبيعات رغم تراجعها، وتلتها تويوتا بـ22%، وفق Focus2move نقلاً عن شفق نيوز.",
     "CAR-2")
# [CAR-3] four ticker lines attributed Focus2move's proprietary data to the wire.
b["arabicTicker"] = [
    t.replace("(شفق نيوز)", "(Focus2move عبر شفق نيوز)")
    if t.endswith("(شفق نيوز)") and any(k in t for k in ("كيا", "تويوتا", "هيونداي", "الكهربائية"))
    else t
    for t in b["arabicTicker"]
]
save(p, b)

p, v = load("showroom-sales-28", "v11-brief.json")
# [CAR-4] the hook promised a cause ("ليش؟") the source explicitly does not give.
setv(v, ["hookHeadline"], "59 ألف سيارة بس.. بنص سنة", "CAR-4")
# [CAR-5] audible collision: "ثمانية وعشرين بالمئة" meant the y/y fall and then
#         Kia's share within 15 words. Name the denominator on the second one.
sub(v, ["voText"], "كيا تصدّرت بحصة ثمانية وعشرين بالمئة",
    "كيا تصدّرت بحصة ثمانية وعشرين بالمئة من إجمالي المبيعات", "CAR-5")
save(p, v)

# ══════════════════════════════════════════════════ 5 · transit-million-trucks
p, b = load("transit-million-trucks", "props.json")
# [TRA-1] six of nine pills carried no information ("سنوياً: نعم", "العراق: طرف"),
#         and beats 2 and 3 both rendered a giant "3" meaning different things.
setv(b, ["beats", 0, "supportingStats"],
     [{"label": "الهدف", "value": "مليون شاحنة"}, {"label": "الإطار الزمني", "value": "سنوياً"},
      {"label": "الوضع", "value": "استعداد لا اتفاق"}], "TRA-1a")
setv(b, ["beats", 1, "supportingStats"],
     [{"label": "ربيعة", "value": "نينوى"}, {"label": "الوليد", "value": "منفذ حدودي"},
      {"label": "القائم", "value": "منفذ حدودي"}], "TRA-1b")
setv(b, ["beats", 2, "bigStat", "value"], "ثلاثي", "TRA-1c")
setv(b, ["beats", 2, "supportingStats"],
     [{"label": "الاجتماع المقترح", "value": "ثلاثي"}, {"label": "الهدف", "value": "آلية موحدة"},
      {"label": "الإطار", "value": "طريق التنمية"}], "TRA-1d")
# [TRA-2] reported speech instead of a colon-quote on a named Lt. Gen.
setv(b, ["beats", 1, "arabicBody"],
     "حُدّدت ربيعة في نينوى والوليد والقائم ممرات رئيسية، وبحث رئيس هيئة المنافذ الفريق عمر عدنان الوائلي تخصيص ممرات ترانزيت وفق المعايير الدولية، بحسب شفق نيوز.",
     "TRA-2")
# [TRA-3] endQuestion presumed the viewer lives beside Rabia, al-Waleed or al-Qaim.
NEWQT = "بضاعتك تجيك من تركيا؟ شكد تأخذ وقت توصل؟"
b["arabicTicker"] = [NEWQT if "زحام الشاحنات" in t else t for t in b["arabicTicker"]]
save(p, b)

# ══════════════════════════════════════════════════ slate-level
# [SLATE-1] all five were tagged iraq_domestic, defeating bucket rotation.
for slug, bucket in (
    ("budget-78-salaries", "iraq_domestic"),
    ("dollar-third-day", "iraq_economy"),
    ("oil-zero-barrels", "oil_energy"),
    ("showroom-sales-28", "consumer_market"),
    ("transit-million-trucks", "trade_logistics"),
):
    p, b = load(slug, "props.json")
    setv(b, ["topicBucket"], bucket, "SLATE-1")
    save(p, b)

# [SLATE-2] captions: line 1 was <topic> — <question> five times over, three of
# them opening on "شنو", and four captions carried TWO question marks. Line 2 was
# a withholding tease four times. Rewritten to vary shape and state the figure.
CAPTIONS = {
    "budget-78-salaries": """تأخير رواتب موظفي العراق يتجاوز 40 يوماً

الالتزام الشهري 7.8 ترليون دينار، والمالية أعلنت توفير 3.2 ترليون لجزء منه.

راتبك وصل لو بعده متأخر؟

المصادر: شفق نيوز
#العراق #الرواتب #اقتصاد_العراق #وزارة_المالية
@photonect.news
""",
    "dollar-third-day": """سعر صرف الدولار اليوم في بغداد وأربيل

ثالث يوم صعود على التوالي: الصيرفة ببغداد تبيع 100 دولار بـ153,750 ديناراً.

شكد دفعت زيادة على آخر دولار اشتريته؟

المصادر: شفق نيوز
#العراق #الدولار #سعر_الصرف #الدينار_العراقي #أربيل
@photonect.news
""",
    "oil-zero-barrels": """أميركا ما استوردت ولا برميل عراقي بتموز

متوسط صفر برميل يومياً، بعد 45 ألف برميل بالفترة السابقة، وفق إدارة معلومات الطاقة الأميركية.

شكد تدفع بالأسبوع بنزين لسيارتك؟

المصادر: شفق نيوز، إدارة معلومات الطاقة الأميركية
#العراق #النفط #خام_البصرة #اقتصاد
@photonect.news
""",
    "showroom-sales-28": """مبيعات السيارات في العراق تتراجع 28.6% بالنصف الأول

59,264 سيارة بس انباعت بستة أشهر، وهيونداي الأكبر تراجعاً بـ69.7%.

مأجّل شراء سيارة هالسنة؟

المصادر: شفق نيوز، Focus2move
#العراق #سيارات #سوق_السيارات #أسعار
@photonect.news
""",
    "transit-million-trucks": """مليون شاحنة ترانزيت بالسنة عبر العراق

هذا اللي طرحه وفد تركي على هيئة المنافذ، وربيعة والوليد والقائم ممرات رئيسية.

بضاعتك تجيك من تركيا؟ شكد تأخذ وقت توصل؟

المصادر: شفق نيوز
#العراق #طريق_التنمية #المنافذ_الحدودية #تركيا
@photonect.news
""",
}
for slug, text in CAPTIONS.items():
    (POSTS / f"{D}-{slug}" / "caption.txt").write_text(text, encoding="utf-8")

if problems:
    print("PATCHES THAT MISSED THEIR TARGET:")
    for x in problems:
        print("  !", x)
    sys.exit(1)
print("all QA patches applied cleanly")
