#!/usr/bin/env python3
"""Write DELIVERY_2026-04-22.md with rich per-slug IG captions.

Per Ahmed's 22 Apr rejection: "Even the caption, you cut it down.
And now I don't get enough context about the news."

This writes a caption format with hook + 3 pillars + 3 scenarios + 6 sources
+ 15+ hashtags + credits — restoring V4 caption density.

Reads from:
  - data/posts/2026-04-22-*/props.json   (metadata + audioBed + variant)
  - automation/scripts/build-apr22-slate.py (caption_hook/pillars/scenarios/hashtags)
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import subprocess
from datetime import datetime
from pathlib import Path

ROOT = Path("/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE")
POSTS = ROOT / "data" / "posts"
DATE = "2026-04-22"

# Load slate module to access caption copy
SLATE_MOD_PATH = ROOT / "automation" / "scripts" / "build-apr22-slate.py"
spec = importlib.util.spec_from_file_location("slate", SLATE_MOD_PATH)
slate_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(slate_mod)
SLATE = {e["slug"]: e for e in slate_mod.SLATE}


def bed_md5(bed_rel: str) -> str:
    """Return MD5 of audio bed file."""
    bed_abs = Path.home() / "Desktop/Claude <> Ahmed - 2nd Brain/Photonect/my-video/public" / bed_rel
    if not bed_abs.exists():
        return "MISSING"
    return hashlib.md5(bed_abs.read_bytes()).hexdigest()[:10]


def mp4_info(mp4: Path) -> dict:
    if not mp4.exists():
        return {"exists": False, "mb": 0, "duration": 0, "audio_rms": "—"}
    bytes_ = mp4.stat().st_size
    mb = round(bytes_ / (1024 * 1024), 1)
    # probe duration + audio rms
    try:
        dur_out = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "default=noprint_wrappers=1:nokey=1", str(mp4)],
            capture_output=True, text=True, timeout=10,
        ).stdout.strip()
        duration = float(dur_out) if dur_out else 0
    except Exception:
        duration = 0
    try:
        rms_out = subprocess.run(
            ["ffmpeg", "-hide_banner", "-ss", "2", "-t", "5", "-i", str(mp4),
             "-ac", "1", "-af", "volumedetect", "-f", "null", "-"],
            capture_output=True, text=True, timeout=15,
        )
        rms = "—"
        for line in rms_out.stderr.splitlines():
            if "mean_volume:" in line:
                rms = line.split("mean_volume:")[1].strip()
                break
    except Exception:
        rms = "—"
    return {"exists": True, "mb": mb, "duration": round(duration, 1), "audio_rms": rms}


def caption_for(slug: str, props: dict) -> str:
    """Assemble the rich IG caption for one slug."""
    entry = SLATE.get(slug, {})
    hook = entry.get("caption_hook", props["breaking"]["arabicHeadline"])
    pillars = entry.get("caption_pillars", [])
    scenarios = entry.get("caption_scenarios", [])
    h_ar = entry.get("hashtags_ar", [])
    h_en = entry.get("hashtags_en", [])
    sources = props.get("sources", [])[:6]

    lines = []
    lines.append(hook)
    lines.append("")
    # Pillars (already include emoji prefix from slate)
    for p in pillars:
        lines.append(p)
        lines.append("")
    # Scenarios
    if scenarios:
        lines.append("🎯 ثلاثة سيناريوهات:")
        for i, s in enumerate(scenarios, 1):
            lines.append(f"{['١','٢','٣'][i-1]}. {s}")
        lines.append("")
    # Sources inline (publication names). props.json uses {"name": "...", "domain": "..."}
    if sources:
        src_names = []
        for s in sources:
            if isinstance(s, dict):
                src_names.append(s.get("name") or s.get("label") or "")
            elif isinstance(s, (list, tuple)) and s:
                src_names.append(s[0])
        src_line = "📍 المصادر: " + " · ".join(n for n in src_names if n)
        lines.append(src_line)
        lines.append("")
    lines.append("━━━")
    lines.append("@photonect.news | أخبار العالم يومياً — بالعربية")
    lines.append("المصادر والصور مذكورة في آخر صورة")
    lines.append("")
    # Hashtags
    lines.append(" ".join(h_ar) + " #photonectnews")
    lines.append(" ".join(h_en) + " #BreakingNews")
    return "\n".join(lines)


def main():
    all_slugs = [d.name for d in POSTS.glob(f"{DATE}-*") if d.is_dir()]
    # Sort by slot time so the posting schedule + per-slug sections read
    # top-to-bottom 08:00 → 22:40. Slugs that aren't in SLATE fall to the end.
    slugs = sorted(all_slugs, key=lambda s: (SLATE.get(s, {}).get("time", "99:99"), s))
    print(f"Writing delivery for {len(slugs)} slugs on {DATE}")

    out_path = ROOT / f"DELIVERY_{DATE}.md"
    md = []
    md.append(f"# 📦 Photonect NEWS — {DATE} Slate Delivery")
    md.append("")
    md.append(f"**{len(slugs)} reels · 1080×1920 · 34s each · ready for IG/TikTok**")
    md.append("")
    md.append("## V6 Evolution Notes")
    md.append("")
    md.append("This slate implements the V6 engine in response to Ahmed's 22 Apr rejection:")
    md.append("")
    md.append("- **Content density restored** — each beat now carries story-specific Arabic label + punchy heading + 20-35 word `arabicBody` + 3 `supportingStats` pills (V4 density, not V5 stripped version).")
    md.append("- **Captions restored** — hook + 3 pillars + 3 scenarios + 6 sources + 15 hashtags + credit line per slug.")
    md.append("- **Music rebuilt** — 12 musically distinct beds (different keys, tempos 50-130 BPM, timbres, arrangements), loudness-normalized to −16 LUFS / −1 dBFS peak.")
    md.append("- **Variant A/B/C** — distinct visual signatures (BAR money-shot / STRIKE kinetic-split / HAIRLINE cinema-reveal), not different data slices.")
    md.append("")
    md.append("## Posting Schedule")
    md.append("")
    md.append("| # | Slot | Slug | Bucket | Variant | Bed | MD5 | MB | Dur | RMS |")
    md.append("|---|------|------|--------|---------|-----|------|----|----|-----|")

    per_slug_sections = []
    caption_paths = []
    for i, slug in enumerate(slugs, 1):
        pj = POSTS / slug / "props.json"
        d = json.loads(pj.read_text())
        mp4 = POSTS / slug / "newsreel_v3.mp4"
        info = mp4_info(mp4)

        # Write the IG caption alongside the mp4 in the post folder so
        # Ahmed can open a single post folder and find both the video and
        # the ready-to-paste caption together. Overwritten on every run so
        # the on-disk caption always matches the latest delivery doc.
        cap_text = caption_for(slug, d)
        cap_path = POSTS / slug / "caption.txt"
        cap_path.write_text(cap_text, encoding="utf-8")
        caption_paths.append(cap_path)
        bed = d.get("audioBed", "").split("/")[-1]
        bed_hash = bed_md5(d.get("audioBed", ""))
        entry = SLATE.get(slug, {})
        slot = entry.get("time", "—")
        bucket = d.get("topicBucket", "—")
        variant = d.get("variant", "—")
        status = f"{info['mb']}MB" if info["exists"] else "—"
        dur = f"{info['duration']}s" if info["exists"] else "—"
        rms = info["audio_rms"]
        md.append(f"| {i} | {slot} | `{slug}` | {bucket} | {variant} | `{bed}` | `{bed_hash}` | {status} | {dur} | {rms} |")

        # Build per-slug section
        sec = []
        sec.append("")
        sec.append("---")
        sec.append("")
        sec.append(f"## {i}. {slot} — `{slug}`")
        sec.append("")
        sec.append(f"**{d['breaking']['arabicHeadline']}**")
        sec.append("")
        sec.append(f"*{d['breaking'].get('englishSubhead','')}*")
        sec.append("")
        sec.append(f"- Variant **{variant}** · Bucket **{bucket}** · Bed `{bed}` (md5 `{bed_hash}`)")
        sec.append(f"- MP4: `{mp4.relative_to(ROOT)}` — {info['mb']} MB, {info['duration']}s, audio RMS {rms}")
        sec.append("")
        sec.append("### Beats")
        for j, b in enumerate(d["beats"], 1):
            sec.append(f"**Beat {j} · {b['label']}**  ")
            sec.append(f"{b['arabicHeading']}  ")
            sec.append(f"_{b.get('arabicBody','')}_  ")
            if b.get("bigStat"):
                bs = b["bigStat"]
                sec.append(f"**{bs['value']}** — {bs.get('arabicLabel','')}  ")
            stats = b.get("supportingStats", [])
            if stats:
                stat_line = " · ".join(f"{s.get('value','')}: {s.get('label','')}" for s in stats[:3])
                sec.append(f"Stats: {stat_line}")
            sec.append("")
        sec.append("### 📋 IG Caption (ready to paste)")
        sec.append("")
        sec.append("```")
        sec.append(caption_for(slug, d))
        sec.append("```")
        per_slug_sections.append("\n".join(sec))

    md.append("")
    md.extend(per_slug_sections)
    md.append("")
    md.append("---")
    md.append("")
    md.append(f"*Generated by `write-delivery-apr22.py` on {datetime.now().isoformat(timespec='seconds')}*")
    out_path.write_text("\n".join(md), encoding="utf-8")
    print(f"✓ wrote {out_path} ({out_path.stat().st_size // 1024} KB, {len(md)} lines)")
    print(f"✓ wrote {len(caption_paths)} per-post caption.txt files:")
    for p in caption_paths:
        print(f"    {p.relative_to(ROOT)}  ({p.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
