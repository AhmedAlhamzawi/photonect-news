#!/usr/bin/env python3
"""Download the 2026-08-16 Higgsfield frames into the engine's image dirs.

KIE returned HTTP 402 (credits exhausted) at submission time, so every frame in
this slate comes from Higgsfield nano_banana_pro (resolved to nano_banana_2),
9:16, 2k — the standing fallback, not stock.

Usage:  python3 scripts/fetch_scenes_2026_08_16.py [slug ...]
Re-runnable: only downloads entries whose URL is set and whose file is missing
(or when --force is passed).
"""
from __future__ import annotations

import io
import sys
import urllib.request
from pathlib import Path

from PIL import Image  # type: ignore

ROOT = Path(__file__).resolve().parent.parent
IMG_ROOT = ROOT / "my-video" / "public" / "images" / "news"
CF = "https://d8j0ntlcm91z4.cloudfront.net/user_39tn2kD6dWbDkkGBc5tCFsOX5ON"

# (slug, filename, cloudfront basename)  — basename None means "still pending"
FRAMES: list[tuple[str, str, str | None]] = [
    ("2026-08-16-baghdad-37000-megawatt", "hero.jpg",    "hf_20260816_111649_8de40256-c125-4446-baec-f15815e0f27a.png"),
    ("2026-08-16-baghdad-37000-megawatt", "broll_1.jpg", "hf_20260816_111649_78518718-d4d5-4b04-8dc0-c81e7e611bd6.png"),
    ("2026-08-16-baghdad-37000-megawatt", "broll_2.jpg", "hf_20260816_111649_062a4463-2af5-4228-ad95-7f9b1d214fbb.png"),
    ("2026-08-16-baghdad-37000-megawatt", "broll_3.jpg", "hf_20260816_113400_01d25f29-9cea-44a0-891f-b2b7fafa693d.png"),

    ("2026-08-16-dollar-shop-gap", "hero.jpg",    "hf_20260816_113120_e6abf36e-5a25-4d5c-ac5c-a831d9458cb1.png"),
    ("2026-08-16-dollar-shop-gap", "broll_1.jpg", "hf_20260816_114831_f20d965e-ae48-4c35-abd3-1b409bc30e58.png"),
    ("2026-08-16-dollar-shop-gap", "broll_2.jpg", "hf_20260816_111649_396c7b6c-7c51-472b-b1c1-298c0cb74d29.png"),
    ("2026-08-16-dollar-shop-gap", "broll_3.jpg", "hf_20260816_111649_832a9f7c-c50a-4856-ba68-fd6eb3442200.png"),

    ("2026-08-16-homes-turkey-144", "hero.jpg",    "hf_20260816_113706_32ce2d84-7bd9-476d-a48e-f53119d91503.png"),
    ("2026-08-16-homes-turkey-144", "broll_1.jpg", "hf_20260816_113439_0f9aa135-6a70-49eb-b3d5-a26dc55d0e69.png"),
    ("2026-08-16-homes-turkey-144", "broll_2.jpg", "hf_20260816_111649_6612c235-7957-49a0-92b7-bdddb1a7fbb8.png"),
    ("2026-08-16-homes-turkey-144", "broll_3.jpg", "hf_20260816_111649_02129d55-5109-40a8-85c7-331e1e2cb94f.png"),

    ("2026-08-16-hormuz-half-exports", "hero.jpg",    "hf_20260816_111711_146862ef-901d-4cde-b3cf-79e7564c9d04.png"),
    ("2026-08-16-hormuz-half-exports", "broll_1.jpg", "hf_20260816_111712_e371cefb-b2a1-4598-b21f-10f6069ec98e.png"),
    ("2026-08-16-hormuz-half-exports", "broll_2.jpg", "hf_20260816_113503_8432cd20-ca82-420c-ab07-2e55c3af6dc5.png"),
    ("2026-08-16-hormuz-half-exports", "broll_3.jpg", "hf_20260816_113503_2ad96cc2-520e-4217-b005-68388142daf8.png"),

    ("2026-08-16-silence-currency-dinar", "hero.jpg",    "hf_20260816_113120_06acc2b9-457d-4742-8bef-b82a0b4ba2ce.png"),
    ("2026-08-16-silence-currency-dinar", "broll_1.jpg", "hf_20260816_111711_23f3076d-e938-4595-a649-038ddca19621.png"),
    ("2026-08-16-silence-currency-dinar", "broll_2.jpg", "hf_20260816_111711_6db2fe9a-268a-4ef7-afe0-e1cbd13ce916.png"),
    ("2026-08-16-silence-currency-dinar", "broll_3.jpg", "hf_20260816_113526_e83bcf84-22f0-4a07-ab2e-a0cee8506c16.png"),
]


def fetch(url: str, out: Path) -> tuple[int, int]:
    req = urllib.request.Request(url, headers={"User-Agent": "photonect/1.0"})
    with urllib.request.urlopen(req, timeout=120) as r:
        raw = r.read()
    im = Image.open(io.BytesIO(raw))
    if im.mode != "RGB":
        im = im.convert("RGB")
    out.parent.mkdir(parents=True, exist_ok=True)
    im.save(out, "JPEG", quality=92, optimize=True)
    return im.size


def main() -> int:
    force = "--force" in sys.argv
    only = {a for a in sys.argv[1:] if not a.startswith("--")}
    ok = skipped = pending = 0
    for slug, fname, base in FRAMES:
        if only and slug not in only:
            continue
        out = IMG_ROOT / slug / fname
        if base is None:
            print(f"  … PENDING  {slug}/{fname}  (no URL yet)")
            pending += 1
            continue
        if out.exists() and not force:
            print(f"  = have     {slug}/{fname}")
            skipped += 1
            continue
        try:
            w, h = fetch(f"{CF}/{base}", out)
            print(f"  ✓ {slug}/{fname}  {w}x{h}")
            ok += 1
        except Exception as e:  # noqa: BLE001
            print(f"  ! FAIL {slug}/{fname}: {e}", file=sys.stderr)
    print(f"\n== downloaded {ok} · already had {skipped} · pending {pending} ==")
    return 1 if pending else 0


if __name__ == "__main__":
    raise SystemExit(main())
