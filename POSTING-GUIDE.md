# Photonect NEWS — Posting Guide

## The whole system in one page

### Folder layout
```
data/posts/YYYY-MM-DD-slug/
    video.mp4       ← upload this
    caption.txt     ← paste this
    .meta/          ← hidden metadata, ignore
```

### To post one reel on Instagram / TikTok
1. Open the folder
2. Upload `video.mp4`
3. Open `caption.txt`, copy all, paste as caption
4. Post

That's it.

### To render a new day (cloud — once Part 1 is set up)
1. Open **GitHub** app on your phone
2. Tap the `photonect-news` repo → Actions → "Render day"
3. Tap "Run workflow", enter the date (or leave blank for today)
4. Wait ~30 min for the push notification
5. Open **Google Drive** → `Photonect NEWS / YYYY-MM-DD /`
6. 12 videos + 12 captions are waiting

### To render a day locally (fallback)
```bash
cd "Photonect NEWS/NEWS CODE"
bash generate-daily.sh 2026-04-24
```

Output goes to `data/posts/2026-04-24-*/`. Each folder has `video.mp4` + `caption.txt`.

### To evolve the engine (Part 2 — improvements with proof)
1. GitHub app → Actions → "Evolve engine" → Run workflow
2. Wait ~15 min for PR notification
3. Open the PR on your phone → watch the attached `compare.mp4` side-by-side
4. Tap **Merge** if the change looks good, **Close** if not

### Where things live
| Thing | Path |
|---|---|
| The daily pipeline | `generate-daily.sh` |
| The renderer | `data/_template/render-reel.sh` |
| The Remotion compositions | `~/Desktop/Claude <> Ahmed - 2nd Brain/Photonect/my-video/src/` |
| Audio beds | `~/Desktop/Claude <> Ahmed - 2nd Brain/Photonect/my-video/public/audio/` |
| Past posts | `data/posts/` (newest first by date) |
| Old internal engineering logs | `archive/` (don't need to read) |

### What NOT to touch
- `.meta/` folders — internal metadata, not for posting
- `archive/` — old delivery/plan docs, kept for history
- Anything without `video.mp4` and `caption.txt`

### Help
Ask Claude directly: *"Render today's 12 reels"* / *"Rebuild audio beds"* / *"Make the captions shorter"*. Claude has the whole codebase loaded.
