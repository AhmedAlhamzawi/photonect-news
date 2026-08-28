#!/usr/bin/env python3
"""Apply every blocker from the two independent Opus editorial gates (2026-08-28).

Both gates returned DO-NOT-SHIP and converged on one root cause: synthetic frames
publishing claims the sources never made, on an engine (V11) that draws no
«صورة توضيحية» disclosure chip. Frame swaps are already on disk; this rewires the
props/brief image paths and applies the text findings.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "data" / "posts"


def load(slug, name):
    return json.loads((POSTS / slug / ".meta" / name).read_text(encoding="utf-8"))


def save(slug, name, obj):
    (POSTS / slug / ".meta" / name).write_text(
        json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def img(slug, f):
    return f"images/news/{slug}/{f}"


def set_broll(props, slug, mapping):
    """mapping: {beat_index: filename}"""
    for i, f in mapping.items():
        props["beats"][i]["broll"] = img(slug, f)
        props["beats"][i]["brolls"] = [img(slug, f)]


# ════════════════════ A · Muthanna ════════════════════
# gate2 #6 / gate1 #5 — the stamp frame re-enacted the alleged crime over a list of
# the accused. Frame deleted. gate1 #9 — hook understated the source («أكثر من 90»).
# gate1 #10 / gate2 #14 — the closing question implied the viewer's stalled tabu file
# was this ring's doing; now explicitly separated from the investigation.
s = "2026-08-28-a-lands-muthanna-61"
p = load(s, "props.json"); b = load(s, "v11-brief.json")
HEAD_A = "طابو المثنى: أكثر من 90 معاملة مزوّرة و61 موقوفاً"
p["breaking"]["arabicHeadline"] = HEAD_A
b["hookHeadline"] = HEAD_A
p["arabicTicker"][0] = HEAD_A
OLD_Q, NEW_Q = "عندك معاملة طابو معلقة من شهور؟", "سؤال منفصل عن التحقيق: عندك معاملة طابو معلقة من شهور؟"
b["voText"] = b["voText"].replace(OLD_Q, NEW_Q)
b["endQuestion"] = NEW_Q
p["arabicTicker"][-1] = NEW_Q
set_broll(p, s, {0: "broll_3.jpg", 1: "hero.jpg", 2: "broll_2.jpg"})
b["images"] = [img(s, "hero.jpg"), img(s, "broll_3.jpg"), img(s, "broll_2.jpg")]
save(s, "props.json", p); save(s, "v11-brief.json", b)

# ════════════════════ B · dollar spread ════════════════════
# gate1 #3 — broll_1 carried a fabricated Arabic denomination line on a 25,000 note,
# on a reel whose subject IS the currency. gate1 #4 / gate2 #5 — broll_2 was an open,
# staffed kiosk in the wrong country holding non-Iraqi notes, under a beat that says
# the bourse is CLOSED. Both regenerated. gate1 #7 — 1,000 and 50 are our subtraction
# and must carry «(محتسب)» on the hook card, which is the most-screenshotted frame.
# gate1 #11 — shop prices are not "closing" prices; only the bourse has a close.
s = "2026-08-28-b-dollar-spread-shops"
p = load(s, "props.json"); b = load(s, "v11-brief.json")
b["hookHeadline"] = "بين البيع والشراء: بغداد 1,000، أربيل 50 (محتسب)"
HEAD_B = "فرق البيع والشراء بمحال بغداد 1,000 دينار.. وبأربيل 50 (محتسب)"
p["breaking"]["arabicHeadline"] = HEAD_B
p["arabicTicker"][0] = HEAD_B
p["breaking"]["englishSubhead"] = "BAGHDAD SPREAD 1,000 | ERBIL 50 | SPREADS = OUR MATH | THU 27 AUG"
p["beats"][1]["arabicBody"] = (
    "بمحال أربيل: بيع 153,750 وشراء 153,700، أي 50 ديناراً مقابل 1,000 ببغداد — "
    "عشرون ضعفاً (محتسب)، ومحال مقابل محال (شفق نيوز)."
)
p["beats"][2]["supportingStats"][2]["label"] = "الصباح للإغلاق"
set_broll(p, s, {0: "broll_3.jpg", 1: "broll_2.jpg", 2: "broll_1.jpg"})
b["images"] = [img(s, "hero.jpg"), img(s, "broll_3.jpg"),
               img(s, "broll_2.jpg"), img(s, "broll_1.jpg")]
save(s, "props.json", p); save(s, "v11-brief.json", b)

# ════════════════════ C · Kurdistan lecturers ════════════════════
# gate1 #6 — "تهدد العام الدراسي" was our escalation put in a named living person's
# mouth; Kamal warned of possible strikes and boycotts, nothing more.
# gate1 #14 / gate2 #12 — the VO dropped both scenario CONDITIONS, which are the whole
# reason none of the three is decided; restored.
# gate1 #8 — broll_2's 1,000-dinar note read «ة الاعرية» / «ديناز». Regenerated edge-on.
# gate2 #4 / gate1 #17 — broll_1 staged invented faces as Monday's real delegation.
# gate2 #8 — the empty-classroom hero pre-enacted a strike that has not happened.
s = "2026-08-28-c-lecturers-78-thousand"
p = load(s, "props.json"); b = load(s, "v11-brief.json")
b["voText"] = (
    "لم تصل مستحقات تموز بعد. نحو ثمانية وسبعين ألف محاضر مجاني في إقليم كوردستان "
    "يطالبون بالتثبيت على الملاك. ممثلهم محمد كمال قال لشفق نيوز إن ما يتقاضاه "
    "المحاضر شهرياً يتراوح بين أربعمئة وخمسمئة ألف دينار. وبحسب شفق نيوز، ثلاثة "
    "سيناريوهات مطروحة لم يُحسم أي منها: إدراجهم في موازنة سنة ألفين وسبعة وعشرين "
    "بشرط شمول محاضري الوسط والجنوب، أو أن تكمل بغداد فرق الراتب بعد التثبيت، أو "
    "استثمار درجات معلمين متقاعدين ومتوفين. وحذّر كمال من إضرابات ومقاطعة للدروس. "
    "راتبك وصل بموعده هالشهر لو تأخر؟"
)
p["beats"][1]["arabicBody"] = (
    "ما يتقاضاه المحاضر شهرياً يتراوح بين 400 و500 ألف دينار، ولم تصل مستحقات تموز "
    "حتى الآن، وحذّر كمال من إضرابات ومقاطعة للدروس (شفق نيوز)."
)
p["beats"][2]["bigStat"]["arabicLabel"] = "نحو 12 ألف درجة شاغرة"
sp = p["beats"][2].get("subtitlePhrases")
if sp:
    if len(sp) > 2:
        sp[2] = "أو 12 ألف درجة لمتقاعدين ومتوفّين"
    if len(sp) > 3:
        sp[3] = "ولا قرار حُسم في أي منها"
set_broll(p, s, {0: "hero.jpg", 1: "broll_1.jpg", 2: "broll_3.jpg"})
b["images"] = [img(s, "hero.jpg"), img(s, "broll_1.jpg"), img(s, "broll_3.jpg")]
save(s, "props.json", p); save(s, "v11-brief.json", b)

# ════════════════════ D · Kirkuk electricity (V10.1 silent control) ════════════════════
# gate2 #1 — beat 1 sat a cleared office with the unfaded mark of a JUST-REMOVED
# portrait under a named, serving, UNACCUSED official. That is the visual grammar of
# disgrace and defamation by implication. Frame deleted from the slug entirely.
# gate2 #2 — beat 2 put a collapsing pole under the INCOMING director's name. Deleted.
# gate1 #2 / gate2 #3 — the third act manufactured an absence ("the order mentioned no
# supply hours" — an administrative order never would) and showed a household meter,
# publishing "he was removed because the power is bad". Rewritten with an explicit
# exculpation, and the meter deleted. D renders no ticker, so every guard must live in
# a beat body. gate1 #24 — the "1 ministerial order" bigStat was invented filler.
s = "2026-08-28-d-kirkuk-power-director"
p = load(s, "props.json")
p["breaking"]["englishSubhead"] = "KIRKUK BRANCH | NEW ACTING DIRECTOR | 3-MONTH TERM | ADMIN ORDER"
p["beats"][0]["bigStat"] = {
    "value": "وكالة",
    "label": "THE KIRKUK BRANCH IS NOW RUN IN AN ACTING CAPACITY",
    "arabicLabel": "إدارة الفرع بالوكالة",
}
p["beats"][2]["arabicHeading"] = "الوزارة لم تعلن سبباً لإنهاء التكليف"
p["beats"][2]["arabicBody"] = (
    "لم يذكر الأمر الصادر عن وزارة الكهرباء أي سبب لإنهاء تكليف المدير السابق، ولم "
    "تُنسب في القرار أي مخالفة إلى أحد، وفق ما نشرته شفق نيوز."
)
p["beats"][2]["bigStat"] = {
    "value": "0",
    "label": "REASONS STATED BY THE MINISTRY IN THE ORDER",
    "arabicLabel": "أسباب أعلنتها الوزارة",
}
p["beats"][2]["supportingStats"] = [
    {"label": "سبب معلن", "value": "لا يوجد"},
    {"label": "مخالفات وردت", "value": "لا شيء"},
    {"label": "النشر", "value": "27 آب 2026"},
]
set_broll(p, s, {0: "hero.jpg", 1: "broll_1.jpg", 2: "broll_2.jpg"})
save(s, "props.json", p)

# ════════════════════ E · Hormuz ════════════════════
# gate1 #1 — we attached Iraqi exports to CENTCOM's unverified belligerent-party
# figures and stamped (شفق نيوز) on it. The source does not mention Iraq at all.
# Replaced with the explicit fact that it does not. gate2 #7 — the only military
# hardware on the reel was American and it landed exactly as Tehran's denial was
# spoken, while doubling as photographic proof of CENTCOM's own unverified warship
# count. Frame deleted. gate1 #22/#20/#21/#23 — verb parity, Bessent attribution on
# the pill, agent of the 75 turnbacks, and the strait (not an export terminal) as hero.
s = "2026-08-28-e-hormuz-lanes-clear"
p = load(s, "props.json"); b = load(s, "v11-brief.json")
b["voText"] = (b["voText"]
               .replace("وزير النفط الإيراني يؤكد أن", "وزير النفط الإيراني يقول إن")
               .replace("ومن هذا المضيق يخرج نفط الخليج وصادرات العراق.",
                        "ولم يرد في تقرير شفق نيوز أي ذكر للعراق."))
p["breaking"]["heroMedia"] = img(s, "hero.jpg")
p["beats"][1]["arabicBody"] = (
    "تحدثت القيادة المركزية عن 750 مليون برميل عبرت، و75 سفينة أعادتها القوات "
    "الأميركية، فيما قال بيسنت إنهم نقلوا 130 مليون برميل خلال أسبوعين (شفق نيوز)."
)
p["beats"][1]["supportingStats"][1]["label"] = "بيسنت/الخزانة"
p["beats"][1]["supportingStats"][2]["label"] = "أعادتها واشنطن"
p["beats"][2]["arabicBody"] = (
    "قال وزير النفط الإيراني إن مبيعات بلاده مستمرة رغم الحصار الأميركي. وتقرير شفق "
    "نيوز عن تصريحات القيادة المركزية لم يتضمن أي ذكر للعراق (شفق نيوز)."
)
sp = p["beats"][2].get("subtitlePhrases")
if sp and len(sp) > 2:
    sp[2] = "ولا ذكر للعراق في تصريحات القيادة المركزية"
for i, line in enumerate(p["arabicTicker"]):
    if "صادرات العراق" in line:
        p["arabicTicker"][i] = "تقرير شفق نيوز عن تصريحات القيادة المركزية لم يتضمن أي ذكر للعراق"
set_broll(p, s, {0: "hero.jpg", 1: "broll_2.jpg", 2: "broll_3.jpg"})
b["images"] = [img(s, "hero.jpg"), img(s, "broll_2.jpg"), img(s, "broll_3.jpg")]
save(s, "props.json", p); save(s, "v11-brief.json", b)

print("blockers applied to all 5 slugs")
