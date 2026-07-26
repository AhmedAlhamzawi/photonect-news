#!/usr/bin/env python3
"""Apply the Opus editorial-QA gate's findings to the 2026-07-26 slate.

BLOCK items (LEAD slug, audit-100tn-loans):
  B1 voText asserted `وأوقفت عشرات المسؤولين` — no source says anyone was
     detained; the sourced fact is that FBSA referred thousands of cases to the
     judiciary. Unsupported on-air claim, removed.
  B2 Campaign launch date wrong: al-Zaidi launched the drive after taking office
     in May 2026; 28 June was the FIRST RAIDS, not the launch. Fixed in voText,
     beat 3 body, ticker[3], and the stat pill whose label said `انطلاق الحملة`.
  B3 The ~$77bn is AGBI's own conversion, not part of al-Mashadani's quote.
     Re-attributed.
  B4 beat 2 bigStat.label said "untraced" while beat 1 says the board IS tracing
     them. Now "unsettled".
  B5 ticker[4] credited Transparency International directly; AGBI is our source
     and "136 of 182" is AGBI's characterisation. Now attributed via AGBI.

Plus PASS-WITH-NOTE fixes across the other four, and two slate-level defects:
  * V11 renders audioBed from v11-brief.json, NOT props.json, so
    assign-mood-rotation.py never reached the four voiced reels — all four were
    sharing mood_newsroom. Distinct beds assigned here.
  * dollar-under-150/broll_3 and nonoil-revenue-16/broll_2 were byte-identical.
    nonoil's is re-sourced separately.
"""
from __future__ import annotations
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS = ROOT / "data" / "posts"
D = "2026-07-26"


def load(slug, name):
    p = POSTS / f"{D}-{slug}" / ".meta" / name
    return p, json.loads(p.read_text(encoding="utf-8"))


def save(p, obj):
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sub(text, old, new, where):
    if old not in text:
        print(f"  !! MISS [{where}]: {old[:60]!r}", file=sys.stderr)
        return text, False
    return text.replace(old, new), True


changes = 0

# ── 1. AUDIT (LEAD) — B1..B5 ────────────────────────────────────────────────
p, b = load("audit-100tn-loans", "v11-brief.json")
b["voText"], ok = sub(
    b["voText"],
    "ويأتي ذلك ضمن حملة مكافحة الفساد التي أطلقها رئيس الوزراء علي الزيدي أواخر حزيران وأوقفت عشرات المسؤولين.",
    "ويأتي ذلك ضمن حملة مكافحة الفساد التي أطلقها رئيس الوزراء علي الزيدي بعد توليه المنصب في أيار، وبدأت أولى مداهماتها في الثامن والعشرين من حزيران.",
    "audit voText B1+B2")
changes += ok
save(p, b)

p, a = load("audit-100tn-loans", "props.json")
a["beats"][1]["arabicBody"] = (
    "قال رئيس الديوان عمار المشهداني إن الديوان أحال آلاف القضايا إلى القضاء، "
    "فيما تعادل قيمة السُلف نحو 77 مليار دولار، بحسب AGBI.")
a["beats"][1]["bigStat"]["label"] = "Value of unsettled loans"
a["beats"][1]["bigStat"]["arabicLabel"] = "القيمة الدولارية التقريبية للسُلف غير المُسوّاة (AGBI)"
a["beats"][2]["arabicBody"] = (
    "يأتي الكشف ضمن حملة مكافحة الفساد التي أطلقها رئيس الوزراء علي الزيدي بعد توليه "
    "المنصب في أيار 2026، وبدأت أولى مداهماتها في 28 حزيران، بحسب AGBI.")
for pill in a["beats"][2]["supportingStats"]:
    if pill["label"] == "انطلاق الحملة":
        pill["label"] = "أولى المداهمات"
a["arabicTicker"][3] = ("حملة مكافحة الفساد أطلقها رئيس الوزراء علي الزيدي بعد توليه المنصب في أيار "
                        "وبدأت أولى مداهماتها في 28 حزيران (AGBI)")
a["arabicTicker"][4] = ("العراق في المرتبة 136 من 182 دولة بمؤشر مدركات الفساد للعام الماضي "
                        "(AGBI نقلاً عن منظمة الشفافية الدولية)")
save(p, a)
changes += 1

# ── 2. DOLLAR — scope the "under 150k" claim to Baghdad ─────────────────────
p, b = load("dollar-under-150", "v11-brief.json")
b["hookHeadline"] = "الدولار طاح تحت 150 ألف ببغداد"
save(p, b)
p, a = load("dollar-under-150", "props.json")
for pill in a["beats"][2]["supportingStats"]:
    if pill["label"] == "الرسمي":
        pill["label"] = "الرسمي (للدولار الواحد)"
a["beats"][2]["bigStat"]["arabicLabel"] = "سعر الصرف الرسمي للبنك المركزي العراقي للدولار الواحد"
save(p, a)
cap = POSTS / f"{D}-dollar-under-150" / "caption.txt"
t = cap.read_text(encoding="utf-8")
t, ok = sub(t, "نزل تحت 150 ألف دينار", "نزل تحت 150 ألف دينار ببغداد", "dollar caption")
cap.write_text(t, encoding="utf-8")
changes += 2

# ── 3. AMPERE — kicker, hook/end-card echo, replacement clause, qualifier ───
p, b = load("ampere-price-july", "v11-brief.json")
b["kicker"] = "تسعيرة تموز"
b["hookHeadline"] = "سعر الأمبير هالشهر 10 آلاف"
b["voText"], ok = sub(
    b["voText"], "مع إلغاء التشغيل الليلي بالكامل.",
    "مع إلغاء التشغيل الليلي بالكامل واستبداله بالتشغيل الذهبي بالتناوب مع الكهرباء الوطنية.",
    "ampere voText replacement clause")
changes += ok
save(p, b)
p, a = load("ampere-price-july", "props.json")
a["beats"][0]["arabicBody"] = (
    "حدّدت محافظة بغداد تسعيرة تموز عند 10,000 دينار للأمبير بالتشغيل الذهبي، و5,000 في "
    "مناطق الجباية، وألغت التشغيل الليلي مستبدلةً إياه بالتشغيل الذهبي بالتناوب مع الوطنية.")
a["beats"][2]["arabicHeading"] = "غرامات تصل إلى 5 ملايين للمخالفين"
save(p, a)
changes += 1

# ── 4. US-ZERO-CRUDE — drop the false pump-price link, fix hashtag ──────────
p, a = load("us-zero-crude", "props.json")
a["arabicTicker"][-1] = "منو أكبر مشتري لنفط العراق اليوم برأيك؟"
save(p, a)
cap = POSTS / f"{D}-us-zero-crude" / "caption.txt"
t = cap.read_text(encoding="utf-8")
t, _ = sub(t, "شكد سعر لتر البنزين بمحطتكم اليوم؟", "منو أكبر مشتري لنفط العراق اليوم برأيك؟", "us caption q")
t, _ = sub(t, "#أوبك", "#الطاقة", "us hashtag")
cap.write_text(t, encoding="utf-8")
changes += 2

# ── 5. NONOIL — attribution chain, pill labels, source domain ──────────────
p, a = load("nonoil-revenue-16", "props.json")
a["beats"][0]["arabicBody"], _ = sub(
    a["beats"][0]["arabicBody"], "بحسب مرصد صدى العراق نقلاً عن شفق نيوز",
    "بحسب مرصد صدى العراق، نقلته شفق نيوز", "nonoil attribution chain")
for pill in a["beats"][1]["supportingStats"]:
    if pill["label"] == "الكاظمي":
        pill["label"] = "الكاظمي والسوداني"
for pill in a["beats"][2]["supportingStats"]:
    if pill["label"] == "وأيضاً":
        pill["label"] = "ومصدر آخر"
a["sources"][1]["domain"] = "echoiraq.org"
save(p, a)
changes += 1

# ── 6. SLATE — give the four voiced reels distinct beds (V11 reads the brief)
BEDS = {
    "audit-100tn-loans": "audio/mood_cinematic.mp3",
    "dollar-under-150": "audio/mood_newsroom.mp3",
    "ampere-price-july": "audio/mood_mideast.mp3",
    "nonoil-revenue-16": "audio/mood_orchestral.mp3",
}
for slug, bed in BEDS.items():
    p, b = load(slug, "v11-brief.json")
    b["audioBed"] = bed
    save(p, b)
    print(f"  bed {slug:<22} -> {bed}")
changes += 1

print(f"\n== {changes} fix groups applied ==")
