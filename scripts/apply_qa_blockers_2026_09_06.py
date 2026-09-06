#!/usr/bin/env python3
"""Apply the 2026-09-06 QA-gate blockers.

Two independent Opus editorial gates both returned DO-NOT-SHIP. This applies
every blocker I accepted, plus the non-blocking notes worth taking. Two gate
findings were REJECTED after re-checking the raw sources, and that is recorded
here so the reasoning survives:

  * Gate 1 said slug D's «البعثة أنهت استعداداتها» is unsourced. It is sourced —
    it is in Shafaq's own headline ("7 ألعاب تمثل العراق في آسياد اليابان
    والبعثة تنهي استعداداتها"). What was wrong was the ATTRIBUTION: we put it in
    Zaidoun Jawad's mouth as a quote. Re-attributed to Shafaq, fact kept.
  * Gate 1 said slug C's «6 سنوات» is our own arithmetic on "late 2017 → 2023"
    and must be stripped. It is not ours: INA's headline says «على مدى 6 سنوات»
    and Lalish's says «لنحو 6 سنوات». The count stays, hedged with «نحو» exactly
    as the sources hedge it. What DID go is the subtitle's «6 سنوات كاملة» —
    "نحو" and "كاملة" cannot both be true, and "كاملة" resolved an approximate
    range upward.

Everything else below was accepted.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE")
POSTS = ROOT / "data" / "posts"
D = "2026-09-06"
A, B, C, Dg, E = (f"{D}-a-dollar-rumour-1460", f"{D}-b-lebanon-exports-516",
                  f"{D}-c-ghost-employee-six-years", f"{D}-d-asiad-japan-seven-sports",
                  f"{D}-e-fake-investment-firms")
applied: list[str] = []


def load(slug, name):
    return json.loads((POSTS / slug / ".meta" / name).read_text(encoding="utf-8"))


def save(slug, name, data):
    (POSTS / slug / ".meta" / name).write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def cap_edit(slug, old, new, why):
    p = POSTS / slug / "caption.txt"
    t = p.read_text(encoding="utf-8")
    assert old in t, f"{slug} caption: not found -> {old!r}"
    p.write_text(t.replace(old, new), encoding="utf-8")
    applied.append(f"{slug} caption · {why}")


def note(slug, why):
    applied.append(f"{slug} · {why}")


# ── A · dollar rumour ────────────────────────────────────────────────────────
p = load(A, "props.json")
b = load(A, "v11-brief.json")

# G1#2 + G2 note: "ROSE ANYWAY" publishes a causal link between the denied claim
# and the market move that no source makes. Also drops "IRAQI" (the Arabic says
# only وسائل التواصل, with no nationality).
p["breaking"]["englishSubhead"] = (
    "A CLAIM SPREAD ON SOCIAL MEDIA ON SATURDAY THAT THE CENTRAL BANK WOULD PRICE DEPOSITS "
    "AT 1,460 DINARS PER DOLLAR FROM SUNDAY | CBI MEDIA DIRECTOR HAIDER GHAZI TOLD SHAFAQ NEWS "
    "THE REPORT IS FALSE AND AIMED AT DESTABILISING THE EXCHANGE RATE | SEPARATELY, AL-FALLUJAH TV "
    "PUT THE AL-KIFAH AND AL-HARITHIYA BOURSES AT 154,900 DINARS PER $100 ON SUNDAY AGAINST 154,650 "
    "ON SATURDAY; NO SOURCE LINKS THE TWO | SUN 6 SEP")
note(A, "englishSubhead: removed the causal 'ROSE ANYWAY', added 'no source links the two'")

# G1#13: as a standalone karaoke frame this asserted the denied rate is in force.
p["beats"][0]["subtitlePhrases"][1] = "قال الخبر إن الإيداع بـ1,460 ديناراً للدولار من اليوم"
note(A, "beat1 subtitle: the denied rate now carries «قال الخبر إن» on its own frame")

# G1#10 (milder case): a bare "0" read as "no official rate change, ever" —
# broader than Ghazi's denial of THIS change.
p["beats"][1]["bigStat"]["arabicLabel"] = (
    "لا تغيير رسمي في سعر الصرف بشأن ما تداولته المواقع، بحسب مدير إعلام البنك المركزي "
    "حيدر غازي (شفق نيوز · 5 أيلول 2026)")
p["beats"][1]["bigStat"]["label"] = (
    "Official changes to the exchange rate in respect of the circulating claim, per the CBI media director")
note(A, "beat2 bigStat '0': scoped to the circulating claim instead of all rate changes")

# G1#3 + G2#1: the reel led on a computed «+250» stamped «بورصة مقابل بورصة»,
# but Al-Fallujah never says whether Saturday's 154,650 was an opening or a
# closing print. The delta drops out of the bigStat (it stays as a labelled
# محتسب pill) and the missing basis is now stated on screen.
p["beats"][2]["bigStat"]["value"] = "154,900"
p["beats"][2]["bigStat"]["label"] = (
    "Dinars per $100 recorded by the Al-Kifah and Al-Harithiya bourses on Sunday")
p["beats"][2]["bigStat"]["arabicLabel"] = (
    "ديناراً لكل 100 دولار سجّلتها بورصتا الكفاح والحارثية اليوم الأحد، مقابل 154,650 أمس السبت — "
    "ولم تحدد القناة إن كان رقم أمس افتتاحاً أم إغلاقاً (قناة الفلوجة · 6 أيلول 2026)")
p["beats"][2]["arabicBody"] = (
    "في السوق الموازية اليوم الأحد، سجّلت بورصتا الكفاح والحارثية 154,900 دينار لكل 100 دولار "
    "مقابل 154,650 أمس السبت، ولم تحدد القناة إن كان رقم أمس افتتاحاً أم إغلاقاً (قناة الفلوجة).")
p["beats"][2]["subtitlePhrases"] = [
    "بورصتا الكفاح والحارثية 154,900 دينار لكل 100 دولار",
    "مقابل 154,650 أمس السبت",
    "ولم تحدد القناة إن كان رقم أمس افتتاحاً أم إغلاقاً",
    "ومحال الصيرفة ببغداد بيع 155,500 وشراء 154,500",
]
p["arabicTicker"] = [
    "خبر متداول: الإيداع بـ1,460 ديناراً لكل دولار — نفاه البنك المركزي",
    "مدير إعلام المركزي حيدر غازي: الخبر كاذب وعار عن الصحة",
    "بورصتا الكفاح والحارثية 154,900 لكل 100 دولار اليوم الأحد",
    "مقابل 154,650 أمس السبت — ولم يُذكر إن كان افتتاحاً أم إغلاقاً",
    "محال الصيرفة ببغداد: بيع 155,500 وشراء 154,500",
    "وصلك خبر الـ1,460 أمس؟ إي لو لا؟",
]
note(A, "beat3: '+250' demoted from the bigStat to a محتسب pill; the unstated open/close basis is now on screen")

# G2 note: the CBI published nothing — the denial reached us via Shafaq.
b["sourcesLine"] = "المصادر: شفق نيوز (حيدر غازي) · قناة الفلوجة"
# G2 note: two prices on two different bases popped with only one unit shown.
b["statPops"][1]["label"] = "بورصتا الكفاح والحارثية اليوم — لكل 100 دولار"
# Same open/close caveat, spoken.
old_vo = "بعد مئة وأربعة وخمسين ألفاً وستمئة وخمسين أمس."
new_vo = "بعد مئة وأربعة وخمسين ألفاً وستمئة وخمسين أمس السبت، بحسب قناة الفلوجة، التي لم تحدد إن كان رقم أمس افتتاحاً أم إغلاقاً."
assert old_vo in b["voText"]
b["voText"] = b["voText"].replace(old_vo, new_vo).replace("البنك المركزي العراقي أبلغ", "البنك المركزي أبلغ")
note(A, "voText + sourcesLine: attribution corrected to Shafaq/Al-Fallujah, open-close caveat spoken")
save(A, "props.json", p); save(A, "v11-brief.json", b)
cap_edit(A, " — وأرقام البورصة اليوم بالريل.", ".", "dropped the «بالريل» filler")

# ── B · Lebanon exports ──────────────────────────────────────────────────────
p = load(B, "props.json"); b = load(B, "v11-brief.json")

# G2#4: «قفزت بربع واحد» reads in Arabic as "jumped BY a quarter" = 25%. The
# real rise is 47.4% — the hook understated the reel's own headline number by
# half, in the one line most viewers read.
b["hookHeadline"] = "صادرات لبنان للعراق قفزت 47% بثلاثة أشهر"
p["breaking"]["arabicHeadline"] = "صادرات لبنان إلى العراق قفزت 47.4% في ربع واحد"
p["arabicTicker"][0] = "صادرات لبنان إلى العراق قفزت 47.4% في ربع واحد"
note(B, "hook/headline: «قفزت بربع واحد» (reads as 25%) replaced with the real 47.4%")

# G1#9: the trailing attribution handed OUR addition (350+516) to Shafaq/ITC,
# which published only the two quarters.
old = ("وبجمع الربعين، يقترب إجمالي النصف الأول من ثمانمئة وستة وستين مليون دولار، "
       "بحسب شفق نيوز نقلاً عن قاعدة بيانات مركز التجارة الدولية.")
new = ("بحسب شفق نيوز نقلاً عن قاعدة بيانات مركز التجارة الدولية. وبجمع الربعين، وهو حساب من عندنا، "
       "يقترب إجمالي النصف الأول من ثمانمئة وستة وستين مليون دولار.")
assert old in b["voText"]
b["voText"] = b["voText"].replace(old, new)
# G1 note 1: the source is 47.4%, so "approaching 47" understates it.
b["voText"] = b["voText"].replace("بزيادة تقارب سبعة وأربعين بالمئة", "بزيادة تتجاوز سبعة وأربعين بالمئة")
note(B, "voText: the 866 total is now spoken as our own arithmetic, not as an ITC figure; «تقارب»→«تتجاوز»")

# G1#12: the third source was a padded duplicate of the first.
p["sources"] = [
    {"name": "شفق نيوز", "domain": "shafaq.com"},
    {"name": "مركز التجارة الدولية", "domain": "intracen.org"},
    {"name": "قاعدة بيانات Trade Map", "domain": "trademap.org"},
]
note(B, "sources: duplicate Shafaq entry replaced with the ITC/Trade Map database actually cited")
save(B, "props.json", p); save(B, "v11-brief.json", b)
cap_edit(B, "صادرات لبنان إلى العراق قفزت إلى 516 مليون دولار بربع واحد",
         "صادرات لبنان إلى العراق قفزت 47% خلال ربع واحد", "line 1 carried the same 25%/47% ambiguity")
cap_edit(B, " — الرقم بالريل.", ".", "dropped the «بالريل» filler")

# ── C · ghost employee ───────────────────────────────────────────────────────
p = load(C, "props.json"); b = load(C, "v11-brief.json")

# G1#8 + G2 note: the old question invited viewers to allege a crime at their own
# identifiable government office, in public, under a criminal-referral reel — and
# it presupposed that ghost employees are widespread, which no source states.
OLDQ = "بدائرتكم أكو اسم ما تشوفونه؟ إي لو لا؟"
NEWQ = "تعرف شلون تبلّغ هيئة النزاهة؟ إي لو لا؟"
assert p["endQuestion"] == OLDQ and b["endQuestion"] == OLDQ
p["endQuestion"] = NEWQ; b["endQuestion"] = NEWQ
p["arabicTicker"][-1] = NEWQ
b["voText"] = b["voText"].replace("بدائرتكم أكو اسم ما تشوفونه؟", "تعرف شلون تبلّغ هيئة النزاهة؟")
note(C, "endQuestion: no longer solicits a public accusation against the viewer's own workplace")

# G1#5: the loudest on-screen element on a reel about an uncharged man stated the
# offence as fact.
b["statPops"][0]["label"] = "المدة المزعومة بحسب هيئة النزاهة"
note(C, "statPop label: «مدة صرف الراتب الوهمي» → «المدة المزعومة بحسب هيئة النزاهة»")

# G1#6: "GHOST SALARY 2017-2023" stated it happened; the ACCUSED panel arrived
# after and did not qualify it.
p["breaking"]["englishSubhead"] = (
    "IRAQ'S FEDERAL INTEGRITY COMMISSION SAYS AN ACCOUNTANT AT THE HADHAR EDUCATION SECTION IN "
    "QAYYARAH, NINEVEH, IS ACCUSED OF DRAWING MONTHLY SALARIES IN A FICTITIOUS PERSON'S NAME FROM "
    "LATE 2017 TO 2023 | HELD PENDING INVESTIGATION UNDER ARTICLE 315 | HE REMAINS ACCUSED, THERE IS "
    "NO CONVICTION | NO NAME AND NO SUM HAVE BEEN PUBLISHED | INA, LALISH NETWORK, SAT 5 SEP")
note(C, "englishSubhead: leads with 'is accused', keeps 'late' 2017, states no name and no sum published")

# G1#7: "نحو" (approximately) and "كاملة" (full) cannot both be true, and
# "كاملة" resolved the range upward. Attribution added to the first frame.
p["beats"][1]["subtitlePhrases"] = [
    "وبحسب الهيئة استمر الصرف من أواخر 2017 حتى 2023",
    "أي نحو 6 سنوات",
    "ولم تُعلن قيمة أي مبلغ",
]
note(C, "beat2 subtitles: «6 سنوات كاملة» → «نحو 6 سنوات», and the span now carries its attribution")

# G1#12: we read the Commission's statement via INA and Lalish, not on nazaha.iq.
p["sources"][0] = {"name": "هيئة النزاهة الاتحادية (عبر وكالة الأنباء العراقية)", "domain": "ina.iq"}
note(C, "sources: nazaha.iq asserted a primary read we never made")
save(C, "props.json", p); save(C, "v11-brief.json", b)
cap_edit(C, OLDQ, NEWQ, "same endQuestion fix")
cap_edit(C, "#موظفين_وهميين", "#هيئة_النزاهة", "hashtag generalised one accusation into a category")

# ── D · Asian Games ──────────────────────────────────────────────────────────
p = load(Dg, "props.json"); b = load(Dg, "v11-brief.json")

# G1#1, re-scoped: the preparations line IS in Shafaq's headline, but we had put
# it in Jawad's mouth as a quote. Re-attributed to Shafaq; the fact stays.
old = "بحسب رئيس البعثة العراقية زيدون جواد لشفق نيوز، الذي قال إن البعثة أنهت استعداداتها."
new = "بحسب رئيس البعثة العراقية زيدون جواد لشفق نيوز. وأنهت البعثة استعداداتها، بحسب شفق نيوز."
assert old in b["voText"]
b["voText"] = b["voText"].replace(old, new)
p["beats"][1]["arabicBody"] = (
    "الساعة تعدّ: الدورة تنطلق في 19 أيلول وتختتم في 4 تشرين الأول، والبعثة أنهت استعداداتها "
    "(شفق نيوز · 6 أيلول 2026).")
note(Dg, "«أنهت استعداداتها» re-attributed to Shafaq's report instead of being quoted to Jawad")

# G1 note 7: "7 ألعاب بين 11 ألف رياضي" juxtaposes incommensurable units.
p["breaking"]["arabicHeadline"] = "العراق في آسياد اليابان: 7 ألعاب.. والانطلاق 19 أيلول"
p["arabicTicker"][0] = "العراق في آسياد اليابان: 7 ألعاب.. والانطلاق 19 أيلول"
note(Dg, "headline: dropped the sports-vs-athletes scale comparison that meant nothing")

# G2#8: beat 3 is the scale beat (11,000 athletes / 45 countries) and the 11,000
# statPop fires on it, but it carried a lone rower on empty water. New crowd
# frame generated for beat 3; the rowing scull is dropped from the slate.
p["beats"][2]["subtitlePhrases"] = [
    "11 ألف رياضي من 45 دولة يتنافسون",
    "واليابان تستضيف الآسياد للمرة الثالثة",
    "بعد طوكيو 1958 وهيروشيما 1994",
]
# G1#12: the NOC was never quoted in the record.
p["sources"] = [
    {"name": "شفق نيوز", "domain": "shafaq.com"},
    {"name": "زيدون جواد — رئيس البعثة العراقية (عبر شفق نيوز)", "domain": "shafaq.com"},
]
note(Dg, "sources: the Olympic Committee entry was never a source in the record — removed")
save(Dg, "props.json", p); save(Dg, "v11-brief.json", b)

# ── E · fake investment firms (V10.1 control — every field below RENDERS) ─────
p = load(E, "props.json")

# G1#10: a giant "0" is a rhetorical restatement of the adjective «غير مرخصة»
# dressed as data. The statement publishes no figure at all — say that instead.
p["beats"][0]["bigStat"] = {
    "value": "—",
    "label": "The statement publishes no case count and no loss figure",
    "arabicLabel": "لم يُعلن أي رقم: لا عدد حالات ولا حجم خسائر (شفق نيوز · 6 أيلول 2026)",
}
note(E, "beat1 bigStat: the invented '0' replaced with what the statement actually establishes")

# G1#11: the "3 disguises" count was OUR parse — «صفحات التواصل» is a subset of
# «منصات إلكترونية», so 3 is an editorial line-drawing, not arithmetic. The
# محتسب label cannot rescue a count whose denominator we invented.
p["beats"][1]["bigStat"] = {
    "value": "وعود",
    "label": "The lure the statement names: promises of high, quick returns",
    "arabicLabel": "الطُعم الذي يذكره البيان: وعود بعوائد مرتفعة وسريعة (شفق نيوز · 6 أيلول 2026)",
}
p["beats"][1]["supportingStats"][0] = {"label": "الواجهة", "value": "منصات وصفحات"}
note(E, "beat2: the derived '3 disguises' removed (gate ruled the 3 red flags on beat 3 ship as written)")

# G1#12: isc.gov.iq was never fetched; the statement reached us via Shafaq.
p["sources"] = [
    {"name": "شفق نيوز", "domain": "shafaq.com"},
    {"name": "فيصل الهيمص — رئيس هيئة الأوراق المالية (عبر شفق نيوز)", "domain": "shafaq.com"},
]
note(E, "sources: dropped two isc.gov.iq entries asserting a primary read we never made")

# House rule the copy pass missed on the one slug where props actually render:
# arabicHeadline <= 8 words, arabicBody <= 26 words. E was 11 / 32 / 29 / 32.
p["breaking"]["arabicHeadline"] = "الأوراق المالية تحذّر: تحقّق قبل ما تحوّل فلوسك"
p["beats"][0]["arabicBody"] = (
    "حذّر رئيس هيئة الأوراق المالية فيصل الهيمص من شركات وهمية وجهات غير مرخصة تروّج لفرص "
    "استثمارية، داعياً للتحقق من قانونيتها قبل إيداع أي مبلغ (شفق نيوز).")
p["beats"][1]["arabicBody"] = (
    "أوضح الهيمص أن بعض الجهات تستخدم أسماء تجارية ومنصات إلكترونية وصفحات تواصل لإيهام "
    "المستثمرين بأنها مؤسسات مالية معتمدة، مع وعود بعوائد مرتفعة وسريعة (شفق نيوز).")
p["beats"][2]["arabicBody"] = (
    "حذّر الهيمص من جهات تطلب التحويل إلى حسابات شخصية أو محافظ إلكترونية غير معروفة أو تشترط "
    "دفعاً مسبقاً، وطلب الاستفسار من الجهات الرقابية (شفق نيوز).")
note(E, "headline 11→8 words and all three bodies 32/29/32→<=26; this is the slug whose props actually render")
save(E, "props.json", p)

print("\n".join(f"  · {x}" for x in applied))
print(f"\n{len(applied)} QA-gate edits applied")
