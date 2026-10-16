#!/usr/bin/env python3
"""Apply Opus QA gate pass 1 (2026-10-16) text fixes. Image fixes live in place_images_2026_10_16.py."""
import json
from pathlib import Path
P = Path(__file__).resolve().parents[1] / "data" / "posts"
D = "2026-10-16"

def sub(path, old, new):
    s = path.read_text(encoding="utf-8")
    assert old in s, f"{path.name}: not found: {old[:60]}"
    path.write_text(s.replace(old, new), encoding="utf-8")

def brief(slug): return P / f"{D}-{slug}" / ".meta" / "v11-brief.json"
def props(slug): return P / f"{D}-{slug}" / ".meta" / "props.json"
def cap(slug): return P / f"{D}-{slug}" / "caption.txt"

# a
sub(brief("a-passport-101k-reversed"),
    "بحسب بغداد اليوم وشفق نيوز، ونقلت شفق عن مصدر أمني أن السبب ارتفاع سعر صرف الدولار.",
    "بحسب بغداد اليوم، ونقلت شفق نيوز عن مصدر أمني أن مديرية الجوازات رفعته بسبب ارتفاع سعر صرف الدولار، من دون تأكيد رسمي.")
sub(cap("a-passport-101k-reversed"), "رسوم إصدار الجواز العراقي الجديدة — زادت فعلاً لو لا؟", "رسوم إصدار الجواز العراقي — زادت فعلاً لو لا؟")
# b
sub(brief("b-travel-dollar-2-months"), "فيصبح فرق الحصة عن السوق مئتين وواحداً وتسعين ألف دينار.",
    "وبالسعر الرسمي البالغ ألفاً وخمسمئة وعشرين ديناراً للدولار، يصبح فرق الحصة عن السوق بحسابنا مئتين وواحداً وتسعين ألف دينار.")
sub(brief("b-travel-dollar-2-months"), "أي أن الحد السنوي ينخفض بحسابنا إلى اثني عشر ألف دولار.",
    "أي أن الحد الأقصى في السنة ينخفض بحسابنا من أربعة وعشرين ألفاً إلى اثني عشر ألف دولار.")
# c (V10.1)
for f in (props("c-us-sanctions-iraqi-bank"), cap("c-us-sanctions-iraqi-bank")):
    sub(f, "عندك حساب بمصرف أهلي؟", "سمعت باسم هذا المصرف قبل؟")
# d
sub(brief("d-rafidain-cashier-6-years"), "فلوس الزبائن بالرافدين.. وين راحت؟", "أمين صندوق بالرافدين.. 6 سنين سجن")
sub(cap("d-rafidain-cashier-6-years"), "والرشوة اللي انضبطت بكركوك.. بالفيديو.", "وقضية رشوة متهم بيها مسؤول بكركوك.. بالفيديو.")
# e
sub(brief("e-rain-north-40-south"), "تشهد المنطقتان الوسطى والشمالية اليوم أجواء غائمة", "تشهد المنطقتان الوسطى والشمالية الجمعة أجواء غائمة")
for f in (brief("e-rain-north-40-south"), props("e-rain-north-40-south"), cap("e-rain-north-40-south")):
    s = f.read_text(encoding="utf-8"); assert "نزل مطر عندكم اليوم؟" in s
    f.write_text(s.replace("نزل مطر عندكم اليوم؟", "نزل مطر عندكم هاليومين؟"), encoding="utf-8")
sub(brief("e-rain-north-40-south"), "محافظات شمالية بمطر وبرق", "محافظات شمالية — توقعات الراصد عطية")
# c broll_2 is now a generated skyline again
pp = props("c-us-sanctions-iraqi-bank"); d = json.loads(pp.read_text(encoding="utf-8"))
d["beats"][1]["brollSource"] = "صورة توضيحية"
pp.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print("gate 1 applied")

# word-count trims after gate 1 (b was 95 words, a 89)
def trim():
    sub(brief("b-travel-dollar-2-months"), "أعلن البنك المركزي العراقي آلية جديدة لدولار السفر: ألفا دولار للمسافر بالسعر الرسمي كل شهرين، وبحد أقصى ست مرات في السنة، اعتباراً من الأحد الثامن عشر من تشرين الأول.",
        "أعلن البنك المركزي آلية جديدة: ألفا دولار للمسافر بالسعر الرسمي كل شهرين، وست مرات في السنة كحد أقصى، اعتباراً من الأحد.")
    sub(brief("b-travel-dollar-2-months"), "وأغلقت بورصة الكفاح الخميس على مئة وستة وستين ألفاً وخمسمئة وخمسين ديناراً لكل مئة دولار، وبالسعر الرسمي البالغ ألفاً وخمسمئة وعشرين ديناراً للدولار، يصبح",
        "ومع إغلاق الكفاح الخميس على مئة وستة وستين ألفاً وخمسمئة وخمسين لكل مئة دولار، وسعر رسمي قدره ألف وخمسمئة وعشرون، يصبح")
    sub(brief("a-passport-101k-reversed"), "وفي المساء أعلنت وزارة الداخلية أن الوكيل الأقدم حسين العوادي وجّه باستمرار استيفاء",
        "وفي المساء وجّه الوكيل الأقدم لوزارة الداخلية حسين العوادي باستمرار استيفاء")
    # a: «وفي اليوم نفسه قال النائب» -> «وقال النائب» (87 -> 85 words), applied with sed
