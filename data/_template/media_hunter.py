#!/usr/bin/env python3
"""
Story-specific media pipeline for Photonect NEWS reels.

Reads a slug's props.json, figures out what each media slot should show,
hunts for story-fit media across free sources in tiers, writes files
into the Remotion public/images/news/<slug>/ tree, updates the ledger
to prevent reuse, and finally rewrites props.json media paths to point
at the new files.

Tiers (first hit wins, with story-fit validation):
  1. Wikimedia Commons    — landmarks, flags, maps, institutions
  2. Pexels (photos)      — stock with tightly scoped geo queries
  3. Motion graphic       — programmatic ffmpeg-generated accent video

Hard rules:
  - No URL reused within 14 days (ledger).
  - No generic "portrait of a person" unless a named individual was
    explicitly requested by the story; the human-face filter uses a
    keyword deny-list on Pexels alt-text.
  - Every downloaded file is sha256-stamped in the ledger.

Run:
  media_hunter.py <slug>
  media_hunter.py --all            # every post that has no media-stamp.json yet
  media_hunter.py --force <slug>   # ignore existing files, re-hunt
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import random
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from io import BytesIO
from pathlib import Path
from typing import Any

# Brightness filter — lazy-imported. Pillow is present on macOS system Python
# and in most venvs, but we never want an import error to break a hunt.
try:
    from PIL import Image as _PIL_Image  # type: ignore
    _PIL_OK = True
except Exception:
    _PIL_OK = False


# ---------- paths ----------

ROOT = Path(__file__).resolve().parent.parent.parent  # .../NEWS CODE/
POSTS = ROOT / "data" / "posts"
LEDGER_PATH = ROOT / "data" / "media-ledger.json"
ENV_PATH = ROOT / ".env.local"
MYVIDEO = Path(os.environ["MYVIDEO"]) if os.environ.get("MYVIDEO") else Path.home() / "Desktop/Claude <> Ahmed - 2nd Brain/Photonect/my-video"
MEDIA_ROOT = MYVIDEO / "public" / "images" / "news"

LEDGER_TTL_DAYS = 14


# ---------- env loading ----------

def load_env() -> dict[str, str]:
    env: dict[str, str] = {}
    if ENV_PATH.exists():
        for line in ENV_PATH.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()
    return env


ENV = load_env()
PEXELS_KEY = ENV.get("PEXELS_API_KEY", "")
NEWS_KEY = ENV.get("NEWS_API_KEY", "")


# ---------- entity atlas ----------
# slug-token → tightly-scoped English query terms for Wikimedia + Pexels.
# Order matters: more specific queries are tried first.

ATLAS: dict[str, dict[str, list[str]]] = {
    # Middle East geopolitics
    # NOTE: flag queries are avoided for major countries because Wikimedia
    # surfaces historical variants (e.g. the pre-1979 Iran Lion & Sun flag)
    # that carry political signaling we do not want on a neutral news feed.
    "iran": {
        "hero":   ["Azadi Tower Tehran", "Milad Tower Tehran night", "Tehran skyline mountain"],
        "broll":  ["Tehran city street wide", "Tehran bazaar interior", "Isfahan mosque dome"],
        "data":   ["Tehran Stock Exchange trading floor", "Iran oil pipeline", "oil refinery night"],
    },
    "iraq": {
        "hero":   ["Baghdad skyline Tigris river", "Al-Mutanabbi street Baghdad", "Samarra minaret"],
        "broll":  ["Basra oil field", "Iraqi security forces checkpoint", "Baghdad street traffic"],
        "data":   ["oil pump jack sunset", "Iraq power station high voltage"],
    },
    "hormuz": {
        "hero":   ["Strait of Hormuz satellite", "oil tanker Persian Gulf aerial", "container ship Gulf dusk"],
        "broll":  ["crude oil tanker wide shot", "navy destroyer at sea", "oil pipeline terminal"],
        "data":   ["oil tanker loading port", "oil barrel stack yard", "refinery pipeline closeup"],
    },
    "lebanon": {
        "hero":   ["Beirut skyline dawn Mediterranean", "Beirut corniche waterfront", "Byblos harbour Lebanon"],
        "broll":  ["Beirut street evening", "south Lebanon countryside village", "Beirut central district"],
        "data":   ["Lebanon map satellite", "Beirut reconstruction crane"],
    },
    "pakistan": {
        "hero":   ["Faisal Mosque Islamabad", "Islamabad parliament house", "Margalla Hills Islamabad"],
        "broll":  ["Islamabad Jinnah avenue", "Pakistan army headquarters Rawalpindi", "Peshawar market"],
        "data":   ["Karachi port container terminal", "Pakistan political map"],
    },
    "gulf": {
        "hero":   ["Dubai skyline Burj", "Abu Dhabi corniche", "Gulf coast aerial"],
        "broll":  ["Saudi Aramco facility", "Kuwait oil derrick", "Doha skyline night"],
        "data":   ["oil price LED ticker", "gulf map"],
    },
    "saudi": {
        "hero":   ["Riyadh Kingdom Tower", "Saudi flag", "Dammam refinery"],
        "broll":  ["Saudi Aramco pipeline", "Ghawar oil field"],
        "data":   ["oil barrel stack", "Riyadh skyline"],
    },
    # Travel / logistics
    "flight": {
        "hero":   ["empty airport departure board", "grounded airliner tarmac", "airport terminal empty"],
        "broll":  ["airport luggage conveyor empty", "air traffic control tower", "airliner on stand closed"],
        "data":   ["flight cancellation board", "airport terminal wide empty"],
    },
    "aftermath": {
        "hero":   ["airport terminal empty", "airplane grounded sunset"],
        "broll":  ["airport departure board cancelled"],
        "data":   ["airline stock chart red"],
    },
    # Energy markets
    "oil": {
        "hero":   ["offshore oil platform sunset", "crude oil tanker Gulf", "oil refinery night"],
        "broll":  ["oil pump jack field", "oil pipeline desert", "oil storage tank farm"],
        "data":   ["oil price screen red", "Brent crude chart"],
    },
    "shock": {
        "hero":   ["stock market crash screen red", "trader head in hands", "NYSE trading floor panic"],
        "broll":  ["stock market red arrows down", "trader screens multiple charts red"],
        "data":   ["Brent crude price chart", "S&P 500 falling chart"],
    },
    "pivot": {
        "hero":   ["OPEC meeting Vienna", "Gulf summit hall", "Saudi Arabia summit"],
        "broll":  ["diplomatic handshake wide", "oil ministers meeting"],
        "data":   ["oil production chart"],
    },
    "blackout": {
        "hero":   ["city skyline without power night", "high voltage power lines sunset", "electric grid tower"],
        "broll":  ["empty power substation", "power transmission lines", "streetlights dark"],
        "data":   ["power grid map", "electricity meter"],
    },
    "ceasefire": {
        "hero":   ["UN flag blue", "peacekeeping convoy", "border crossing checkpoint"],
        "broll":  ["armored vehicle patrol", "empty border road"],
        "data":   ["conflict map"],
    },
    "buffer": {
        "hero":   ["border fence barrier", "UN buffer zone", "peacekeeping post"],
        "broll":  ["military vehicle convoy", "observation tower border"],
        "data":   ["map border"],
    },
    "talks": {
        "hero":   ["international summit room", "diplomatic negotiation table", "flags in conference hall"],
        "broll":  ["G20 press conference", "UN security council chamber"],
        "data":   ["negotiation timeline chart"],
    },
    # April 19 evolution — preempt common MENA news verbs so new slugs
    # like "2026-04-19-iraq-election" land on well-scoped queries without
    # needing manual atlas edits each time.
    "election": {
        "hero":   ["parliament building chamber", "ballot box polling station", "Iraqi parliament Baghdad"],
        "broll":  ["voter queue polling station", "election rally crowd", "ballot counting"],
        "data":   ["election results screen", "parliament seat distribution"],
    },
    "vote": {
        "hero":   ["ballot box polling station", "voter hand raised"],
        "broll":  ["voter queue polling station", "election monitor observers"],
        "data":   ["election tally board"],
    },
    "protest": {
        "hero":   ["night street protest crowd", "banner march demonstrators", "protest fire at night"],
        "broll":  ["crowd raised fists", "riot police line", "protest march wide"],
        "data":   ["protest numbers chart"],
    },
    "strike": {
        "hero":   ["factory workers walkout", "empty refinery gate picket", "workers union rally"],
        "broll":  ["picket line banner", "empty production line"],
        "data":   ["output loss chart"],
    },
    "summit": {
        "hero":   ["diplomatic summit photo line", "leaders stage flags", "conference hall wide"],
        "broll":  ["handshake two leaders", "press conference podium"],
        "data":   ["agenda infographic"],
    },
    "sanctions": {
        "hero":   ["US Treasury building", "port container ship idle", "oil tanker at anchor"],
        "broll":  ["bank vault closed", "container yard stopped"],
        "data":   ["trade volume chart red", "currency exchange screen"],
    },
    "border": {
        "hero":   ["border fence barrier", "observation tower border", "remote desert checkpoint"],
        "broll":  ["military patrol vehicle", "border crossing wide"],
        "data":   ["border map satellite"],
    },
    "drone": {
        "hero":   ["military drone on runway", "UAV in sky", "loitering munition drone"],
        "broll":  ["drone operator ground station", "drone wreckage field"],
        "data":   ["strike map graphic"],
    },
    "strike-military": {
        "hero":   ["airstrike smoke night", "damaged building aftermath", "military jet launching"],
        "broll":  ["fighter jet afterburner", "missile launcher vehicle"],
        "data":   ["ordnance map region"],
    },
    "earthquake": {
        "hero":   ["earthquake damaged building", "collapsed apartment block", "rescue team rubble"],
        "broll":  ["rubble search dog", "aftermath destroyed street"],
        "data":   ["seismograph chart spike"],
    },
    "flood": {
        "hero":   ["flooded city street aerial", "rising river overbank"],
        "broll":  ["flood rescue boat", "submerged cars"],
        "data":   ["rainfall map"],
    },
    # tech/AI additions
    "chip": {
        "hero":   ["silicon wafer closeup", "semiconductor die macro", "GPU circuit board"],
        "broll":  ["semiconductor fab cleanroom", "chip packaging robot"],
        "data":   ["chip revenue chart"],
    },
    "model": {
        "hero":   ["AI data center aisle", "GPU cluster rack"],
        "broll":  ["server room engineer laptop", "GPU fans closeup"],
        "data":   ["benchmark chart"],
    },
    "deal": {
        "hero":   ["signed agreement handshake", "signature ceremony table"],
        "broll":  ["contract signing stage", "press photo opportunity"],
        "data":   ["deal value chart"],
    },
    "investment": {
        "hero":   ["Wall Street bull statue", "trading floor NYSE", "stock chart rising"],
        "broll":  ["trader multiple screens", "financial district skyline"],
        "data":   ["investment flow chart"],
    },
    "billion": {
        "hero":   ["currency stack money", "global finance map glowing"],
        "broll":  ["trading floor screens", "bank vault"],
        "data":   ["investment chart billions"],
    },
    "ceasefire": {   # override of earlier to broaden broll options (keeps first-wins order)
        "hero":   ["UN flag blue", "peacekeeping convoy", "border crossing checkpoint"],
        "broll":  ["armored vehicle patrol", "empty border road", "peace accord signing table"],
        "data":   ["conflict map"],
    },
    # Tech / AI bucket
    "ai": {
        "hero":   ["data center server rack", "GPU circuit board", "neural network abstract"],
        "broll":  ["server aisle blue light", "laboratory cleanroom semiconductor"],
        "data":   ["stock chart green red", "tech stock ticker screen"],
    },
    "frontier": {
        "hero":   ["AI lab futuristic", "semiconductor fab", "quantum computer"],
        "broll":  ["engineers cleanroom", "robot arm manufacturing"],
        "data":   ["NVIDIA trading floor", "tech IPO"],
    },
    # 2026-04-21 additions — starlink and embargo were generating motion-graphic
    # fallbacks because ATLAS had no matching token (19 fallback ledger entries found
    # across starlink-mideast and chip-embargo posts).
    "starlink": {
        "hero":   ["satellite dish array sky", "telecommunications antenna tower", "satellite in orbit"],
        "broll":  ["satellite broadband dish rural", "geostationary satellite close-up"],
        "data":   ["satellite internet coverage map"],
    },
    "embargo": {
        "hero":   ["shipping container terminal aerial", "cargo port crane", "container ship dock"],
        "broll":  ["empty dock gate locked", "customs checkpoint truck"],
        "data":   ["trade sanctions map", "export restriction chart"],
    },
    # Generic fallbacks by topic bucket
    "_mena_geopolitics": {
        "hero":   ["Middle East map political", "Arab summit flags"],
        "broll":  ["diplomatic handshake", "UN security council chamber"],
        "data":   ["oil chart", "world currency exchange"],
    },
    "_iraq_domestic": {
        "hero":   ["Baghdad Tigris river", "Iraq parliament"],
        "broll":  ["Baghdad market", "Iraq electricity grid"],
        "data":   ["oil pump jack", "Iraqi dinar"],
    },
    "_gulf_regional": {
        "hero":   ["Persian Gulf aerial", "Dubai skyline"],
        "broll":  ["oil tanker", "Gulf summit hall"],
        "data":   ["oil barrel price", "OPEC meeting"],
    },
    "_europe": {
        "hero":   ["Brussels EU headquarters", "European flag wide"],
        "broll":  ["European parliament chamber", "Berlin street"],
        "data":   ["euro currency", "European stock chart"],
    },
    "_global_economy": {
        "hero":   ["global stock exchange", "New York Stock Exchange floor"],
        "broll":  ["Wall Street bull statue", "trading floor screens"],
        "data":   ["financial chart red", "oil price ticker"],
    },
    "_tech_ai": {
        "hero":   ["data center", "GPU chip closeup"],
        "broll":  ["server room", "semiconductor fab"],
        "data":   ["stock chart tech"],
    },
    "_wildcard": {
        "hero":   ["abstract news graphic", "world map wide"],
        "broll":  ["newsroom wide shot", "breaking news graphic"],
        "data":   ["stock ticker screen"],
    },
}


SLOT_ARCHETYPE = {
    # key on beat label phrases
    "ماذا يحدث": "broll",     # What's happening — action
    "لماذا يهم":  "data",      # Why does it matter — data/consequences
    "ماذا بعد":  "broll",     # What's next — context/outlook
    "عاجل":       "hero",      # Breaking
}


FACE_DENY = {
    "selfie", "portrait", "headshot", "model", "girl", "boy",
    "woman", "man ", " man", "face", "smile", "fashion", "dating",
    "gym", "yoga", "pilates", "influencer", "beauty",
}

# Wikimedia file titles often carry their subject as plain English words.
# These deny-lists reject visually wrong hits even when the filename
# mentions the right city or country (e.g. "Baghdad Hall music recital").

# Always-reject on HERO/BROLL: a neutral news reel should never open on
# a concert, ceremony, cartoon, or household scene.
CONTENT_DENY = {
    "music", "concert", "piano", "orchestra", "opera", "choir", "recital",
    "theatre", "theater", "drama", "ballet", "dance", "dancer", "singer",
    "wedding", "birthday", "christmas", "halloween", "carnival", "parade",
    "festival", "gig", "band", "performer", "stage show", "pageant",
    "cartoon", "caricature", "illustration", "painting", "sculpture",
    "mural", "graffiti", "abstract art", "still life",
    "cat", "dog", "bird", "flower", "garden", "pet",
    "food", "meal", "dish", "recipe", "kitchen counter", "cuisine",
    "restaurant interior", "mezze", "hummus",
    "meme", "logo design",
}

# Name-collision geography — MENA stories shouldn't inherit photos from
# same-named docks/streets elsewhere (e.g. "Byblos Harbour, Millwall, London"
# matched a Lebanon query because the London dock is named Byblos).
MENA_ANCHORS = {
    "iran", "iraq", "tehran", "baghdad", "basra", "isfahan", "najaf", "karbala",
    "lebanon", "beirut", "tripoli", "byblos", "sidon", "tyre",
    "syria", "damascus", "aleppo",
    "hormuz", "persian gulf", "arabian gulf",
    "pakistan", "islamabad", "karachi", "lahore", "peshawar",
    "saudi", "riyadh", "dammam", "jeddah", "mecca",
    "uae", "emirates", "dubai", "abu dhabi",
    "qatar", "doha", "kuwait", "bahrain", "oman", "muscat", "yemen", "sanaa",
}

CONFLICT_GEO = {
    # Far-from-MENA geographies that cause false-positive matches when
    # place-names collide (e.g. Byblos in London, Paris Texas, etc.).
    "london", "millwall", "thames", "canary wharf", "docklands",
    "new york", "manhattan", "brooklyn", "chicago",
    "paris france", "tokyo", "beijing", "shanghai", "moscow",
    "berlin", "munich", "madrid", "rome italy", "barcelona",
    "seoul", "sydney", "melbourne", "toronto", "dublin",
    "texas", "california", "florida",
}

# Vintage / historical deny — Wikimedia is thick with pre-1950 content
# that looks archival and feels wrong on a breaking-news reel. These are
# only suppressed when the query does not itself ask for a historical view.
HISTORICAL_DENY = {
    "parthian", "sassanid", "sasanian", "achaemenid", "ottoman era",
    "ancient", "medieval", "manuscript", "lithograph", "engraving",
    "daguerreotype", "woodcut", "postcard", "19th century", "18th century",
    "17th century", "16th century",
    "1900s", "1910s", "1920s", "1930s", "1940s", "1950s", "1960s", "1970s",
    "black and white photograph", "sepia",
}

# Maps/diagrams/charts — fine for DATA slots, wrong for HERO/BROLL where
# we want photographic or cinematic context.
MAP_DENY = {
    "map", "atlas", "chart", "diagram", "schematic", "blueprint", "plan of",
    "route map", "topographic", "cartography", "gis ", "floor plan",
}


# ---------- slug → English entity tokens ----------

def tokenize_slug(slug: str) -> list[str]:
    # "2026-04-17-iran-talks" → ["iran", "talks"]
    tail = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", slug)
    return [p for p in tail.split("-") if p]


# ---------- ledger ----------

def load_ledger() -> dict[str, Any]:
    if LEDGER_PATH.exists():
        return json.loads(LEDGER_PATH.read_text())
    return {"entries": []}


def save_ledger(ledger: dict[str, Any]) -> None:
    cutoff = datetime.now(timezone.utc) - timedelta(days=LEDGER_TTL_DAYS)
    ledger["entries"] = [
        e for e in ledger["entries"]
        if datetime.fromisoformat(e["fetched_at"]) > cutoff
    ]
    LEDGER_PATH.parent.mkdir(parents=True, exist_ok=True)
    LEDGER_PATH.write_text(json.dumps(ledger, indent=2, ensure_ascii=False))


def ledger_has_url(ledger: dict[str, Any], url: str) -> bool:
    return any(e.get("url") == url for e in ledger["entries"])


def ledger_has_hash(ledger: dict[str, Any], sha: str) -> bool:
    return any(e.get("sha256") == sha for e in ledger["entries"])


def ledger_add(ledger: dict[str, Any], slug: str, slot: str, url: str,
               source: str, sha: str, queries: list[str]) -> None:
    ledger["entries"].append({
        "slug": slug,
        "slot": slot,
        "url": url,
        "source": source,
        "sha256": sha,
        "queries": queries,
        "fetched_at": datetime.now(timezone.utc).isoformat(),
    })


# ---------- http ----------

def fetch(url: str, headers: dict[str, str] | None = None, timeout: int = 25) -> bytes | None:
    merged = {"User-Agent": "PhotonectNews/1.0 (contact: ahmed@photonect.net)"}
    if headers:
        merged.update(headers)
    req = urllib.request.Request(url, headers=merged)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read()
    except Exception as e:
        print(f"  fetch-error {url[:80]}... → {e}", file=sys.stderr)
        return None


def fetch_json(url: str, headers: dict[str, str] | None = None) -> Any:
    raw = fetch(url, headers=headers)
    if not raw:
        return None
    try:
        return json.loads(raw.decode("utf-8"))
    except Exception:
        return None


# ---------- query synthesis ----------

def synth_queries(slug: str, slot: str, archetype: str,
                  bucket: str, beat: dict[str, Any] | None,
                  breaking: dict[str, Any] | None) -> list[str]:
    """Produce an ordered list of English search queries for this slot."""
    tokens = tokenize_slug(slug)

    queries: list[str] = []

    # 0) Per-slug editorial override — props.breaking.heroQueries (HERO only).
    # Added 2026-04-20 after the April 20 slate visual review surfaced 5/12 heroes
    # that passed luminance QA but were topically off (1887 calendar for arctic-route,
    # generic couch for qatar-pivot, etc.). Root cause: slug tokens like
    # "arctic"/"route" miss the ATLAS and fall back to bucket-wildcard generic
    # queries + a noisy englishSubhead. Editors can now seed known-good
    # Wikimedia-shaped phrases (e.g. "50 Let Pobedy icebreaker") via
    # breaking.heroQueries and the hunter will try them FIRST. The top-4-query
    # window in hunt_slot() means these seeds dominate the candidate pool.
    if slot == "hero" and breaking:
        seeds = breaking.get("heroQueries") or []
        if isinstance(seeds, list):
            queries.extend([s for s in seeds if isinstance(s, str) and s.strip()])

    # 1) atlas entries matching slug tokens
    for t in tokens:
        entry = ATLAS.get(t)
        if entry and entry.get(archetype):
            queries.extend(entry[archetype])

    # 1b) Per-beat English stat label for broll slots — seeds topically-specific queries.
    # e.g. beat.bigStat.label = "votes needed tonight" → better than generic "iraq parliament".
    # Only for broll slots (not hero) since hero is already seeded by heroQueries/englishSubhead.
    if slot != "hero" and beat:
        stat_label = (beat.get("bigStat") or {}).get("label", "").strip()
        if stat_label and len(stat_label.split()) >= 2:
            queries.append(stat_label.lower())

    # 2) atlas entry for topic bucket (generic but better than stock)
    bucket_key = "_" + (bucket or "wildcard")
    fb = ATLAS.get(bucket_key)
    if fb and fb.get(archetype):
        queries.extend(fb[archetype])

    # 3) English subhead from breaking (HERO only)
    if slot == "hero" and breaking:
        sub = breaking.get("englishSubhead", "")
        sub = re.sub(r"[•·|]", " ", sub)
        sub = re.sub(r"[^A-Za-z0-9\s-]", "", sub).strip()
        if sub:
            queries.append(sub.lower())

    # dedup preserving order
    seen: set[str] = set()
    out: list[str] = []
    for q in queries:
        q = q.strip()
        if q and q.lower() not in seen:
            seen.add(q.lower())
            out.append(q)
    return out[:6]


# ---------- Wikimedia Commons ----------

WIKI_API = "https://commons.wikimedia.org/w/api.php"


def _query_tokens(query: str) -> list[str]:
    q = re.sub(r"[^A-Za-z0-9\s]", " ", query.lower())
    STOP = {"the", "a", "an", "of", "in", "on", "at", "and", "or", "for", "to"}
    return [t for t in q.split() if t and t not in STOP]


def _title_words(title: str) -> set[str]:
    # Strip "File:" prefix + extension, split on non-alpha
    t = re.sub(r"^file:", "", title.lower())
    t = re.sub(r"\.\w{2,5}$", "", t)
    t = re.sub(r"[^a-z0-9]+", " ", t)
    return set(w for w in t.split() if len(w) >= 3)


def score_title(title: str, query: str, archetype: str) -> int:
    """Positive = relevant; negative = should reject. Returns a rank score."""
    t = title.lower()
    words = _title_words(title)
    q_tokens = _query_tokens(query)

    # Hard denies
    if any(bad in t for bad in CONTENT_DENY):
        return -100
    # Historical only allowed when query itself references it
    q_is_hist = any(bad in query.lower() for bad in HISTORICAL_DENY)
    if not q_is_hist and any(bad in t for bad in HISTORICAL_DENY):
        return -80
    # Maps only allowed on DATA slot (or when query says "map/chart")
    q_is_map = any(bad in query.lower() for bad in ("map", "chart", "diagram"))
    if archetype != "data" and not q_is_map:
        if any(bad in t for bad in MAP_DENY):
            return -60
    # Portrait/selfie unless named person
    if any(bad in t for bad in ("portrait", "selfie")) and not any_named(query):
        return -40

    # Geographic-name collision: if the query mentions a MENA anchor,
    # the title cannot sneak in a far-away geography hint that would
    # obviously belong to a different region.
    q_low = query.lower()
    if any(anchor in q_low for anchor in MENA_ANCHORS):
        if any(bad in t for bad in CONFLICT_GEO):
            return -50

    # Positive signal: title word overlap with query tokens
    overlap = sum(1 for q in q_tokens if q in words)
    # Hero/broll prefer concrete subjects
    return overlap


def hunt_wikimedia(query: str, archetype: str = "broll") -> list[dict[str, Any]]:
    params = {
        "action": "query",
        "format": "json",
        "generator": "search",
        "gsrsearch": f"filetype:bitmap {query}",
        "gsrnamespace": "6",
        "gsrlimit": "15",
        "prop": "imageinfo",
        "iiprop": "url|size|mime|extmetadata",
        "iiurlwidth": "1600",
    }
    url = WIKI_API + "?" + urllib.parse.urlencode(params)
    data = fetch_json(url)
    if not data or "query" not in data:
        return []
    pages = data["query"].get("pages", {}) or {}
    out: list[dict[str, Any]] = []
    for _, page in pages.items():
        ii = page.get("imageinfo")
        if not ii:
            continue
        info = ii[0]
        mime = info.get("mime", "")
        if not mime.startswith("image/") or mime == "image/svg+xml":
            continue
        w = info.get("width", 0)
        h = info.get("height", 0)
        if w < 900 or h < 600:
            continue
        u = info.get("thumburl") or info.get("url")
        if not u:
            continue
        title = page.get("title", "")
        score = score_title(title, query, archetype)
        if score <= 0:
            continue
        out.append({
            "url": u,
            "title": title,
            "source": "wikimedia",
            "width": w,
            "height": h,
            "score": score,
        })
    # Highest-scoring first, so the most on-topic hit wins
    out.sort(key=lambda c: c.get("score", 0), reverse=True)
    return out


def any_named(q: str) -> bool:
    q = q.lower()
    named = ("trump", "netanyahu", "putin", "biden", "xi ", "mohammed",
             "sudani", "khamenei", "aoun", "nawaf", "masih", "maliki")
    return any(n in q for n in named)


# ---------- Pexels ----------

def hunt_pexels(query: str, archetype: str = "broll") -> list[dict[str, Any]]:
    if not PEXELS_KEY:
        return []
    url = "https://api.pexels.com/v1/search?" + urllib.parse.urlencode({
        "query": query, "per_page": 20, "orientation": "portrait",
    })
    data = fetch_json(url, headers={"Authorization": PEXELS_KEY})
    if not data:
        return []
    out: list[dict[str, Any]] = []
    for p in data.get("photos", []):
        alt = (p.get("alt") or "").lower()
        # reject generic human-portrait stock unless named person requested
        if not any_named(query):
            if any(bad in alt for bad in FACE_DENY):
                continue
        # Pexels tags often include subject noise — reject same content/map denies
        if any(bad in alt for bad in CONTENT_DENY):
            continue
        if archetype != "data" and any(bad in alt for bad in MAP_DENY):
            continue
        src = p.get("src", {})
        u = src.get("portrait") or src.get("large2x") or src.get("large")
        if not u:
            continue
        out.append({
            "url": u,
            "alt": alt,
            "source": "pexels",
            "width": p.get("width", 0),
            "height": p.get("height", 0),
        })
    return out


# ---------- motion graphic fallback ----------

def make_motion_graphic(out_path: Path, accent_hex: str, seed: int) -> None:
    """Generate a 10s 1080×1920 MP4 with animated gradient + pulsing dot-grid.

    Base is a 50/50 white-tinted accent so the resulting frame luminance stays
    above L≥75 before the VideoBackdrop beat overlay, which ensures L_final≥40.
    """
    out_path.parent.mkdir(parents=True, exist_ok=True)
    r, g, b = hex_to_rgb(accent_hex)
    # Mix accent 50/50 with white so even the darkest brand color (red L≈60)
    # produces a tinted base with L≥150 that survives the beat overlay.
    rt, gt, bt = (r + 255) // 2, (g + 255) // 2, (b + 255) // 2
    ink = "0x090B11"
    tinted = f"0x{rt:02X}{gt:02X}{bt:02X}"
    accent = f"0x{r:02X}{g:02X}{b:02X}"
    filter_complex = (
        # Bright tinted-accent base — high luminance to survive the overlay
        f"color=c={tinted}:size=1080x1920:duration=10:rate=30[bg];"
        # Ink corner vignette for brand aesthetic (darkens edges only)
        f"color=c={ink}:size=1080x1920:duration=10:rate=30,"
        f"format=rgba,geq=r='r(X,Y)':a='min(255\\,200*hypot((X-W/2)/W*2\\,(Y-H/2)/H*2))'[vig];"
        # Drifting saturated accent blob for visual motion interest
        f"color=c={accent}:size=540x540:duration=10:rate=30,"
        f"format=rgba,boxblur=luma_radius=min(h\\,w)/4:luma_power=1,"
        f"geq=r='r(X,Y)':a='128*(1-hypot((X-W/2)/W*2\\,(Y-H/2)/H*2))',"
        f"scale=1080:1920,fade=t=in:st=0:d=1:alpha=1[blob];"
        f"[bg][vig]overlay=x=0:y=0:format=auto[bg2];"
        f"[bg2][blob]overlay=x=0:y=0:format=auto[v]"
    )
    cmd = [
        "ffmpeg", "-y", "-v", "error",
        "-filter_complex", filter_complex,
        "-map", "[v]",
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "medium", "-crf", "22",
        str(out_path),
    ]
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError:
        # Last-ditch: tinted accent solid — always passes luminance floor
        subprocess.run([
            "ffmpeg", "-y", "-v", "error",
            "-f", "lavfi", "-i", f"color=c={tinted}:size=1080x1920:duration=10:rate=30",
            "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "medium", "-crf", "22",
            str(out_path),
        ], check=True)


def hex_to_rgb(h: str) -> tuple[int, int, int]:
    h = h.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


# ---------- download + validate ----------

# Brightness floor per slot. Hero is the first frame viewers see and sits
# behind the biggest headline type — it MUST be legible. Broll is allowed
# to be a little darker (it's covered by stat cards), and photo-insert
# lives inside a framed card so mid-tones are fine.
_BRIGHTNESS_FLOOR = {
    # 2026-04-20 recalibration (2nd pass, 03:23): the 80 floor was necessary but
    # not sufficient. A second 7-slug re-render showed 3/7 heroes still failed
    # even with raw L≥80 because the OLD hero overlay (40/55/ED gradient — bottom
    # at 93% ink alpha) crushed mean luminance independently of raw brightness
    # (e.g. raw L=106 → rendered L=48 on arctic-route, raw L=89 → rendered L=50 on
    # opec-emergency). Side-agent follow-up lightened the hero overlay to 22/33/77
    # (bottom stop 47%). Under the new overlay, raw L≥90 yields rendered L≥62
    # with 3-5 point margin across all bucket accents. broll floor bumped too
    # since starlink-mideast's raw L=90 broll still rendered below the beat floor
    # under the current 52%-alpha beat overlay — pushing to 85 gives margin.
    "hero": 90.0,
    "broll_1": 85.0,       # beat overlay avg alpha ≈52% (77/66/BB) → L_bg≥85 → L_final≥45
    "broll_2": 85.0,
    "broll_3": 85.0,
    "photo_insert": 65.0,  # raised 5 — inside card but still overlay-affected
}


def _mean_luminance(raw: bytes) -> float | None:
    """Return mean grayscale luminance (0-255) of an image blob, or None
    if Pillow isn't available or the blob isn't a decodable image."""
    if not _PIL_OK:
        return None
    try:
        with _PIL_Image.open(BytesIO(raw)) as im:
            # Downscale first — a 2048x1365 jpeg costs ~180ms to sample.
            im.thumbnail((256, 256))
            gs = im.convert("L")
            hist = gs.histogram()
            total = sum(hist)
            if total == 0:
                return None
            weighted = sum(i * c for i, c in enumerate(hist))
            return weighted / total
    except Exception:
        return None


def _mean_luminance_video(path: Path) -> float | None:
    """Sample mean luminance of a video by extracting one frame at the midpoint.
    Uses ffmpeg to scale to 256px wide before passing bytes to _mean_luminance()."""
    if not _PIL_OK:
        return None
    try:
        probe = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
            capture_output=True, text=True, timeout=10,
        )
        if probe.returncode != 0 or not probe.stdout.strip():
            return None
        duration = float(probe.stdout.strip())
        seek_t = max(0.0, duration / 2)
        import tempfile, os as _os
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
            tmp_path = tmp.name
        try:
            result = subprocess.run(
                ["ffmpeg", "-y", "-v", "error", "-ss", str(seek_t),
                 "-i", str(path), "-vframes", "1",
                 "-vf", "scale=256:-2", tmp_path],
                capture_output=True, timeout=15,
            )
            if result.returncode != 0 or not _os.path.exists(tmp_path):
                return None
            with open(tmp_path, "rb") as f:
                return _mean_luminance(f.read())
        finally:
            try:
                _os.unlink(tmp_path)
            except Exception:
                pass
    except Exception:
        return None


def download_with_ledger(slug: str, slot: str, candidates: list[dict[str, Any]],
                         dest: Path, ledger: dict[str, Any], queries: list[str]) -> bool:
    floor = _BRIGHTNESS_FLOOR.get(slot)
    for c in candidates:
        url = c["url"]
        if ledger_has_url(ledger, url):
            continue
        raw = fetch(url)
        if not raw or len(raw) < 40_000:  # skip < 40KB (likely thumbnail/error)
            continue
        sha = hashlib.sha256(raw).hexdigest()
        if ledger_has_hash(ledger, sha):
            continue
        # Brightness gate — crushed-black stills sink under the overlay and
        # turn the hero frame into an illegible rectangle of text over void.
        if floor is not None:
            lum = _mean_luminance(raw)
            if lum is not None and lum < floor:
                print(f"  ∅ {slot} too dark (L={lum:.1f} < {floor}) ← {c['source']}")
                continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(raw)
        ledger_add(ledger, slug, slot, url, c["source"], sha, queries)
        print(f"  ✓ {slot} ← {c['source']} ({queries[0] if queries else '?'})")
        return True
    return False


# ---------- main hunt per slot ----------

def hunt_slot(slug: str, slot: str, archetype: str, accent: str,
              bucket: str, beat: dict[str, Any] | None,
              breaking: dict[str, Any] | None,
              media_dir: Path, ledger: dict[str, Any]) -> tuple[Path, str]:
    """Return (final_path, media_type) — always succeeds via motion graphic fallback."""
    queries = synth_queries(slug, slot, archetype, bucket, beat, breaking)
    print(f"[{slug}] slot={slot} arch={archetype} queries={queries[:3]}...")

    candidates: list[dict[str, Any]] = []

    # First pass — walk queries in order, keep per-query ranked results so
    # the strongest-fitting atlas query wins. Do NOT shuffle: randomization
    # was letting low-relevance maps/concerts beat the tight entity hit.
    for q in queries[:4]:
        candidates.extend(hunt_wikimedia(q, archetype))

    still_path = media_dir / f"{slot}.jpg"
    if download_with_ledger(slug, slot, candidates, still_path, ledger, queries):
        return still_path, "image"

    # Pexels tier
    pex_candidates: list[dict[str, Any]] = []
    for q in queries[:4]:
        pex_candidates.extend(hunt_pexels(q, archetype))
        time.sleep(0.15)  # be polite

    if download_with_ledger(slug, slot, pex_candidates, still_path, ledger, queries):
        return still_path, "image"

    # motion-graphic fallback — MP4
    motion_path = media_dir / f"{slot}.mp4"
    make_motion_graphic(motion_path, accent, seed=hash(slug + slot) & 0xFFFF)
    # Luminance gate: verify generated graphic meets slot brightness floor.
    # make_motion_graphic uses a 50/50 white-tinted accent base so this should
    # always pass, but an edge-case lavfi failure (or OS codec quirk) could
    # produce near-black output — catch it here rather than in the render QA.
    floor = _BRIGHTNESS_FLOOR.get(slot)  # 2026-04-22: was NameError — only defined in download_with_ledger scope
    if floor is not None:
        mg_lum = _mean_luminance_video(motion_path)
        if mg_lum is not None and mg_lum < floor:
            print(f"  ⚠ motion-graphic {slot} L={mg_lum:.1f} < floor {floor} "
                  f"— last resort; accepting but flagging for investigation")
        elif mg_lum is not None:
            print(f"  ✓ motion-graphic luminance {slot} L={mg_lum:.1f} ≥ floor {floor}")
    # record in ledger as synthetic (URL = sha fingerprint to avoid reuse)
    sha = hashlib.sha256(motion_path.read_bytes()).hexdigest()
    ledger_add(ledger, slug, slot, f"motion://{sha[:16]}", "motion", sha, queries)
    print(f"  ▲ {slot} ← motion graphic (no wire image)")
    return motion_path, "video"


# ---------- per-post orchestration ----------

def process_post(slug: str, ledger: dict[str, Any], force: bool = False) -> bool:
    post = POSTS / slug
    meta = post / ".meta"
    meta.mkdir(exist_ok=True)
    props_path = meta / "props.json"
    if not props_path.exists():
        print(f"skip {slug}: no .meta/props.json")
        return False

    props = json.loads(props_path.read_text())
    bucket = props.get("topicBucket", "wildcard")
    breaking = props.get("breaking") or {}
    beats = props.get("beats") or []

    media_dir = MEDIA_ROOT / slug
    stamp = meta / "media-stamp.json"
    if stamp.exists() and not force:
        print(f"skip {slug}: .meta/media-stamp.json present (use --force to re-hunt)")
        return False

    # Wipe old media so we do not accidentally reuse stale files.
    if media_dir.exists():
        for f in media_dir.iterdir():
            if f.is_file():
                f.unlink()
    media_dir.mkdir(parents=True, exist_ok=True)

    # --- hero
    hero_path, hero_type = hunt_slot(
        slug, "hero", "hero", "#D72638", bucket, None, breaking, media_dir, ledger,
    )
    props["breaking"]["heroMedia"] = f"images/news/{slug}/{hero_path.name}"
    props["breaking"]["heroMediaType"] = hero_type

    # --- beats (broll)
    for i, beat in enumerate(beats):
        label = beat.get("label", "")
        archetype = "broll"
        for key, val in SLOT_ARCHETYPE.items():
            if key in label:
                archetype = val
                break
        accent = beat.get("accent") or "#00E5A0"
        slot = f"broll_{i+1}"
        path, media_type = hunt_slot(
            slug, slot, archetype, accent, bucket, beat, None, media_dir, ledger,
        )
        props["beats"][i]["broll"] = f"images/news/{slug}/{path.name}"
        props["beats"][i]["brollType"] = media_type

        # Photo insert (beat 1 only, optional) — try a data-style still
        if i == 0 and "photoInsert" in beat:
            insert_slot = "photo_insert"
            insert_path, _ = hunt_slot(
                slug, insert_slot, "data", accent, bucket, beat, None, media_dir, ledger,
            )
            # always use .jpg for photo insert (Img-rendered)
            if insert_path.suffix != ".jpg":
                jpg_insert = media_dir / f"{insert_slot}.jpg"
                subprocess.run([
                    "ffmpeg", "-y", "-v", "error",
                    "-i", str(insert_path), "-vframes", "1", str(jpg_insert),
                ], check=False)
                insert_path = jpg_insert if jpg_insert.exists() else insert_path
            props["beats"][i]["photoInsert"] = f"images/news/{slug}/{insert_path.name}"

    props_path.write_text(json.dumps(props, indent=2, ensure_ascii=False))
    stamp.write_text(json.dumps({
        "hunted_at": datetime.now(timezone.utc).isoformat(),
        "bucket": bucket,
    }, indent=2))
    print(f"✓ {slug}: props rewritten + stamp written")
    return True


# ---------- CLI ----------

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("slug", nargs="?", help="post slug, e.g. 2026-04-17-iran-talks")
    ap.add_argument("--all", action="store_true", help="hunt for every post missing a stamp")
    ap.add_argument("--force", action="store_true", help="ignore existing stamp / media")
    args = ap.parse_args()

    ledger = load_ledger()

    if args.all:
        slugs = sorted([p.name for p in POSTS.iterdir() if p.is_dir() and (p / ".meta" / "props.json").exists()])
    elif args.slug:
        slugs = [args.slug]
    else:
        ap.error("pass a slug or --all")
        return 2

    ok = 0
    for s in slugs:
        try:
            if process_post(s, ledger, force=args.force):
                ok += 1
        except Exception as e:
            print(f"✗ {s}: {e}")
        finally:
            save_ledger(ledger)
    print(f"\nprocessed {ok}/{len(slugs)} posts")
    return 0


if __name__ == "__main__":
    sys.exit(main())
