#!/usr/bin/env python3
"""ESSAY RAP TEST — does Arabic rap work in Suno (KIE) for the Photonect Essay format?

Generates two custom-lyric vocal takes of one short economic-analysis verse:
  A) Modern Standard Arabic (فصحى) — Photonect's default register
  B) Iraqi colloquial (عامية عراقية) — the natural-rap register for our lens

Each task returns ~2 clips → ~4 takes total for Ahmed to listen and judge.
This answers the make-or-break gate BEFORE any Essay-engine code is written.

KIE Suno contract (from automation/scripts/generate-suno-music.py):
  POST /api/v1/generate  {prompt, model, customMode, instrumental, style, title, callBackUrl}
  customMode=true + instrumental=false + prompt=<our lyrics> → vocals on OUR words.
  GET  /api/v1/generate/record-info?taskId=  → data.response.sunoData[].audioUrl
"""
from __future__ import annotations
import json, os, re, sys, time, urllib.request, urllib.error
from pathlib import Path

KIE_BASE = "https://api.kie.ai"
GEN_URL = f"{KIE_BASE}/api/v1/generate"
STATUS_URL = f"{KIE_BASE}/api/v1/generate/record-info"
CALLBACK = "https://webhook.site/00000000-0000-0000-0000-000000000000"
MODEL = "V5"
POLL = 12
MAX_MIN = 12
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "essay-rap-test"

# ── Arabic verse, two registers (same idea: "huge spend — boom or debt? let the numbers judge") ──
MSA_LYRICS = """[Intro]
فوتونكت... تحليل
[Verse]
رقمٌ على الشاشةِ يُربكُ كلَّ العقول
مليارٌ يُنفَقُ، فهل هذا معقول؟
يقولونَ نهضةٌ، ويقولونَ ديون
وأنا أقول: دعِ الأرقامَ تقول
[Verse]
لا صوتَ يعلو فوقَ صوتِ البيان
وازنِ الأمرَ، واتركْ ضجيجَ الهتاف
مشروعُ قرنٍ، أم رهانٌ ثقيل؟
السؤالُ اليومَ، والجوابُ غدًا
"""

IRAQI_LYRICS = """[Intro]
فوتونكت... تحليل
[Verse]
شوف الرقم بالشاشة، يلخبط راسك
مليار ينصرف، وين راحت فلوسك؟
يكولون نهضة، ويكولون ديون
وآني أكلك: خل الأرقام تجاوبك
[Verse]
لا تصدك كلام، ولا تصدك هتاف
وزنها بعقلك، شيل الزين من الخف
مشروع القرن، لو رهان ثقيل؟
السؤال هسه، والجواب باجر
"""

JOBS = [
    {"tag": "msa",   "title": "Photonect Essay Rap Test - MSA",
     "style": "Arabic hip hop, modern boom-bap, confident clear male rap vocal, Modern Standard Arabic, cinematic news beat, 90 bpm",
     "lyrics": MSA_LYRICS},
    {"tag": "iraqi", "title": "Photonect Essay Rap Test - Iraqi",
     "style": "Iraqi Arabic hip hop, Baghdadi dialect, confident male rap vocal, trap boom-bap beat, cinematic, 90 bpm",
     "lyrics": IRAQI_LYRICS},
]


def load_key() -> str:
    k = os.environ.get("KIE_AI_API_KEY")
    if k:
        return k.strip()
    for envf in (ROOT / ".env", ROOT / ".env.local"):
        if envf.is_file():
            for line in envf.read_text().splitlines():
                m = re.match(r"\s*(?:export\s+)?KIE_AI_API_KEY\s*=\s*(.+)\s*$", line)
                if m:
                    return m.group(1).strip().strip('"').strip("'")
    sys.exit("error: KIE_AI_API_KEY not found in env or .env")


def persian_char_guard(text: str, tag: str):
    bad = [(hex(ord(c)), c) for c in text if c in ("ی", "ک")]
    if bad:
        sys.exit(f"PERSIAN-CHAR GUARD tripped in {tag}: {bad}")


def post(url, body, key, timeout=30):
    req = urllib.request.Request(url, data=json.dumps(body).encode(), method="POST",
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json", "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode())


def get(url, key, timeout=30):
    req = urllib.request.Request(url, method="GET",
        headers={"Authorization": f"Bearer {key}", "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode())


def download(url, dest, timeout=120):
    dest.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept": "audio/mpeg, audio/*, */*"})
    with urllib.request.urlopen(req, timeout=timeout) as r, dest.open("wb") as f:
        n = 0
        while True:
            c = r.read(65536)
            if not c:
                break
            f.write(c); n += len(c)
    return n


def submit(job, key) -> str:
    persian_char_guard(job["lyrics"] + job["style"], job["tag"])
    body = {"prompt": job["lyrics"], "model": MODEL, "customMode": True,
            "instrumental": False, "style": job["style"][:200],
            "title": job["title"][:80], "callBackUrl": CALLBACK}
    resp = post(GEN_URL, body, key)
    if resp.get("code") != 200:
        raise RuntimeError(f"submit failed: code={resp.get('code')} msg={resp.get('msg')!r}")
    tid = (resp.get("data") or {}).get("taskId")
    if not tid:
        raise RuntimeError(f"no taskId: {resp!r}")
    return tid


def poll(tid, key) -> dict:
    deadline = time.time() + MAX_MIN * 60
    last = None
    while time.time() < deadline:
        try:
            resp = get(f"{STATUS_URL}?taskId={tid}", key)
        except Exception as e:
            print(f"      poll err: {e}", flush=True); time.sleep(POLL); continue
        data = resp.get("data") or {}
        st = data.get("status")
        if st != last:
            print(f"      [{tid[:8]}] status: {st}", flush=True); last = st
        if st == "SUCCESS":
            return data
        if st in {"CREATE_TASK_FAILED", "GENERATE_AUDIO_FAILED", "CALLBACK_EXCEPTION", "SENSITIVE_WORD_ERROR"}:
            raise RuntimeError(f"task failed: {st}")
        time.sleep(POLL)
    raise RuntimeError("poll timeout")


def main():
    key = load_key()
    OUT.mkdir(parents=True, exist_ok=True)
    print(f"━━━ ESSAY RAP TEST — submitting {len(JOBS)} tasks (MSA + Iraqi) ━━━")
    submitted = []
    for j in JOBS:
        try:
            tid = submit(j, key)
            print(f"  {j['tag']:6} → taskId {tid}")
            submitted.append((j, tid))
        except Exception as e:
            print(f"  {j['tag']:6} SUBMIT FAIL: {e}")
    manifest = []
    for j, tid in submitted:
        print(f"\n  polling {j['tag']} ({tid[:8]})...")
        try:
            data = poll(tid, key)
            clips = (data.get("response") or {}).get("sunoData") or []
            print(f"      {len(clips)} clip(s)")
            for i, c in enumerate(clips, 1):
                url = c.get("audioUrl")
                if not url:
                    continue
                dest = OUT / f"raptest_{j['tag']}_{i}.mp3"
                size = download(url, dest)
                dur = c.get("duration")
                print(f"      saved {dest.name}  ({size/1e6:.1f} MB, {dur}s)")
                manifest.append({"tag": j["tag"], "clip": i, "file": dest.name,
                                 "duration": dur, "url": url, "lyrics_title": c.get("title")})
        except Exception as e:
            print(f"      FAIL: {e}")
            manifest.append({"tag": j["tag"], "error": str(e)})
    (OUT / "_manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False))
    print(f"\n✅ done → {OUT}")
    print(f"   {len([m for m in manifest if 'file' in m])} clips ready to listen")


if __name__ == "__main__":
    sys.exit(main())
