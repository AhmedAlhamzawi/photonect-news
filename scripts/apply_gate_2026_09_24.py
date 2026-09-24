#!/usr/bin/env python3
"""Apply the 2026-09-24 Opus editorial-gate (pass 1) findings to copy."""
import json
from pathlib import Path
P = Path(__file__).resolve().parents[1] / "data" / "posts"
D = "2026-09-24"

def load(s, f): return json.loads((P / f"{D}-{s}" / ".meta" / f).read_text())
def save(s, f, o): (P / f"{D}-{s}" / ".meta" / f).write_text(json.dumps(o, ensure_ascii=False, indent=1))
def cap(s, old, new):
    f = P / f"{D}-{s}" / "caption.txt"; t = f.read_text(); assert old in t, (s, old); f.write_text(t.replace(old, new))

# A — no "owner not revealed" insinuation; no smuggled-asset adjacency to the $13M; sourced hook
s = "a-france-13-million"
v = load(s, "v11-brief.json")
v["hookHeadline"] = "صندوق الاسترداد: 13 مليون دولار من فرنسا"
v["voText"] = ("أعلن صندوق استرداد أموال العراق، اليوم الخميس، استعادة ثلاثة عشر مليون دولار من أموال عراقية كانت "
  "محجوزة في بنوك فرنسية بموجب قرارات قضائية. وقال رئيس الصندوق محمد علي اللامي إن المبلغ أودع في حسابات وزارة "
  "المالية بالتنسيق مع البنك العربي السويسري. وبحسب شبكة تسعة ستة أربعة، جاءت الخطوة ثمرة تفاهمات في باريس مع "
  "الوكالة الفرنسية لمكافحة الفساد ووزارة العدل، على هامش زيارة الوفد الحكومي برئاسة رئيس الوزراء علي الزيدي إلى "
  "فرنسا. هل سمعت بصندوق استرداد أموال العراق قبل اليوم؟")
save(s, "v11-brief.json", v)
p = load(s, "props.json")
b = p["beats"][1]
b["arabicBody"] = "قال رئيس الصندوق محمد علي اللامي إن المبلغ أُودع في حسابات وزارة المالية بالتنسيق مع البنك العربي السويسري (شفق، 964)."
b["supportingStats"][2] = {"label": "الإعلان", "value": "24 أيلول"}
b["subtitlePhrases"][2] = "والإعلان صدر اليوم الخميس"
p["arabicTicker"][2] = "الأموال كانت محجوزة في البنوك الفرنسية بموجب قرارات قضائية (شفق نيوز)"
save(s, "props.json", p)

# B — the 2,000 is our computation, not 964's
s = "b-dollar-week-2000"
v = load(s, "v11-brief.json"); v["hookHeadline"] = "الدولار ببغداد أقل 2,000 بأسبوع (محتسب)"; save(s, "v11-brief.json", v)

# C — forecast attributed; "assumes", not "on condition"
s = "c-ebrd-minus-12"
v = load(s, "v11-brief.json")
v["hookHeadline"] = "البنك الأوروبي: اقتصاد العراق قد ينكمش 12%"
v["voText"] = v["voText"].replace("بشرط عودة الصادرات", "بافتراض عودة الصادرات"); assert "بافتراض" in v["voText"]
v["statPops"][1]["label"] = "توقع 2027 بافتراض عودة الصادرات"
save(s, "v11-brief.json", v)
p = load(s, "props.json")
b = p["beats"][2]; b["label"] = "الافتراض"
b["arabicHeading"] = b["arabicHeading"].replace("بشرط", "بافتراض")
b["subtitlePhrases"] = [x.replace("بشرط", "بافتراض") for x in b["subtitlePhrases"]]
b["supportingStats"] = [{"label": ("الافتراض" if x["label"] == "الشرط" else x["label"]), "value": x["value"]} for x in b["supportingStats"]]
b["arabicBody"] = b["arabicBody"].replace("بشرط", "بافتراض")
p["arabicTicker"] = [x.replace("بشرط", "بافتراض") for x in p["arabicTicker"]]
save(s, "props.json", p)
cap(s, "ويضع شرطاً واحداً للتعافي", "ويربط التعافي بعودة الصادرات")

# D — credit Al-Khaleej's match judgement; sources date; drop Arnold (not in today's sources)
s = "d-gulf-cup-oman-draw"
v = load(s, "v11-brief.json")
v["voText"] = (v["voText"].replace("المنتخب العراقي، بقيادة غراهام أرنولد، مشواره", "المنتخب العراقي مشواره")
               .replace("وصنع العراق فرصاً أكثر", "وبحسب صحيفة الخليج، صنع العراق فرصاً أكثر"))
assert "أرنولد" not in v["voText"] and "وبحسب صحيفة الخليج" in v["voText"]
v["sourcesLine"] = "المصادر: صحيفة الخليج · المشهد · شفق نيوز — 23-24 أيلول 2026"
save(s, "v11-brief.json", v)
p = load(s, "props.json")
b = p["beats"][0]
b["arabicBody"] = "صافرة البداية في ملعب الأمير عبد الله الفيصل بجدة، والمنتخب العراقي يخرج بنقطة أمام عُمان مساء الأربعاء في افتتاح مشواره بالمجموعة الأولى (الخليج)."
b["supportingStats"][1] = {"label": "المدينة", "value": "جدة"}
b["subtitlePhrases"][1] = "نقطة أولى لأسود الرافدين"
save(s, "props.json", p)

# E — we read Shafaq quoting IRNA; goods cross, not "enter" Iraq
s = "e-mehran-453-million"
p = load(s, "props.json")
p["sources"] = [{"name": "شفق نيوز (نقلاً عن إرنا)", "domain": "shafaq.com"}]
p["beats"][2]["label"] = "شنو يعبر"
save(s, "props.json", p)
cap(s, "البضاعة الإيرانية بالعراق — شكد عبر من منفذ مهران؟", "صادرات إيران عبر منفذ مهران — شكد عبر للعراق والمنطقة؟")
cap(s, "المصادر: وكالة إرنا، شفق نيوز (24 أيلول 2026)", "المصادر: شفق نيوز نقلاً عن وكالة إرنا (24 أيلول 2026)")
print("gate pass-1 fixes applied")
# Pass-2 fixes (applied inline 2026-09-24 ~14:35): A caption hook «استرداد أموال العراق من فرنسا — شكد رجع للخزينة؟» and
# #مكافحة_الفساد → #فرنسا; D voText «من كل مجموعة»; E beat2 subtitle «أكثر من مليون و46 ألف طن»; D hero swapped (rugby posts).
