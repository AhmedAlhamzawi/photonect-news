#!/usr/bin/env python3
"""2026-10-08 Opus gate pass 1 fixes (1 blocker in e's caption + warnings), applied on top of the copywriter's files.
Also swaps c broll_2 <-> broll_3 so the Tehran-landing beat gets the cabin-window frame and the
religious/medical/study beat gets the Mashhad shrine."""
import json, shutil
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
P = ROOT / "data/posts"
IMG = ROOT / "my-video/public/images/news"

def edit(slug, fn):
    m = P / f"2026-10-08-{slug}/.meta"
    props = json.loads((m / "props.json").read_text())
    bp = m / "v11-brief.json"
    brief = json.loads(bp.read_text()) if bp.exists() else None
    cap = (P / f"2026-10-08-{slug}/caption.txt").read_text()
    props, brief, cap = fn(props, brief, cap)
    (m / "props.json").write_text(json.dumps(props, ensure_ascii=False, indent=1))
    if brief: bp.write_text(json.dumps(brief, ensure_ascii=False, indent=1))
    (P / f"2026-10-08-{slug}/caption.txt").write_text(cap)

def rep(s, a, b):
    assert a in s, f"missing: {a}"
    return s.replace(a, b)

def a(p, b, c):
    b["voText"] = rep(b["voText"], "وتطالب بإبقائه لحوالات", "وتطالب بالإبقاء على سعر الصرف الحالي لحوالات")
    bt = p["beats"][2]
    bt["arabicBody"] = rep(bt["arabicBody"], "وتطالب بإبقاء هذا السعر لحوالات", "وتطالب بالإبقاء على سعر الصرف الحالي لحوالات")
    for s in bt["supportingStats"]:
        if s["value"] == "إبقاء 1,320": s["value"] = "سعر الصرف الحالي"
    p["arabicTicker"] = [t.replace("بإبقاء سعر الصرف السابق", "بالإبقاء على سعر الصرف الحالي") for t in p["arabicTicker"]]
    return p, b, c

def b_(p, b, c):
    b["voText"] = rep(b["voText"], "استهلكت جزءاً من الاحتياطي", "استهلكت أجزاءً غير هيّنة من الاحتياطي")
    for s in b["statPops"]:
        if s["value"] == "1,900": s["label"] = "دينار للدولار — رقم طُرح قبل القرار (البنك المركزي)"
    bt = p["beats"][2]
    bt["arabicBody"] = bt["arabicBody"].replace("استهلكت جزءاً من الاحتياطي", "استهلكت أجزاءً غير هيّنة من الاحتياطي")
    bt["bigStat"]["arabicLabel"] = "دينار للدولار — رقم طُرح قبل القرار"
    return p, b, c

def c_(p, b, c):
    b["hookHeadline"] = "رحلات النجف لإيران رجعت.. يومياً"
    b["voText"] = rep(b["voText"], "بأن الترخيص الأميركي لهذه الرحلات ينتهي", "بأن الترخيص الأميركي لهذه الرحلات يخص الزوار الدينيين وينتهي")
    return p, b, c

def d(p, b, c):
    for s in b["statPops"]:
        if s["value"] == "3": s["label"] = "متهمين موقوفين على ذمة التحقيق"
    p["beats"][1]["bigStat"]["arabicLabel"] = "متهمين"
    p["breaking"]["arabicHeadline"] = "النزاهة: 3 متهمين بكهرباء كربلاء برشوة لتفادي غرامة 10 ملايين"
    return p, b, c

def e(p, b, c):
    c = rep(c, "أرقام جديدة من وكالة اللجوء الأوروبية، وقواعد رفض سريع بالميثاق الجديد.. التفاصيل بالفيديو.",
            "أرقام جديدة من وكالة اللجوء الأوروبية: كم قرار، كم رفض، وكم حصل على حماية.. التفاصيل بالفيديو.")
    p["beats"][0]["bigStat"]["arabicLabel"] = "من القرارات رُفضت بالكامل"
    p["breaking"]["arabicHeadline"] = "الوكالة الأوروبية: رفض كامل لـ66.61% من قرارات لجوء العراقيين"
    for bt in p["beats"]: bt["brollSource"] = "صورة توضيحية"
    return p, b, c

for s, f in [("a-food-eggs-93k", a), ("b-dollar-166800-1900", b_), ("c-iraqi-airways-iran-daily", c_),
             ("d-karbala-meter-bribe", d), ("e-eu-asylum-66-percent", e)]:
    edit(s, f); print("✓", s)

cd = IMG / "2026-10-08-c-iraqi-airways-iran-daily"
shutil.move(cd / "broll_2.jpg", cd / "tmp.jpg"); shutil.move(cd / "broll_3.jpg", cd / "broll_2.jpg"); shutil.move(cd / "tmp.jpg", cd / "broll_3.jpg")
print("✓ swapped c broll_2 <-> broll_3")
