#!/usr/bin/env python3
"""2026-10-02 Opus gate pass 2 warnings: a hook currency, e ticker attribution."""
from pathlib import Path
P = Path(__file__).resolve().parents[1] / "data/posts"
for slug, f, old, new in [
 ("a-wasit-health-3-7-billion", ".meta/v11-brief.json", "اختلاس 3.78 مليار.. ولبنان", "اختلاس 3.78 مليار دينار.. ولبنان"),
 ("e-wrestling-bronze-16-years", ".meta/props.json", "(شفق نيوز، واع)", "(شفق نيوز)"),
]:
    p = P / f"2026-10-02-{slug}" / f; t = p.read_text()
    print("OK" if old in t else "MISS", slug); p.write_text(t.replace(old, new))
