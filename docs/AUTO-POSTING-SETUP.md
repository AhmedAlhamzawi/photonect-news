# Auto-posting to Instagram + TikTok (upload-post.com)

The daily pipeline can auto-publish the 6 reels to IG (Reels) + TikTok via
[upload-post.com](https://app.upload-post.com) — no Meta/TikTok app review on our side.
upload-post holds the platform approvals; we just connect the accounts + call their API.

## How it works
After `render-day.yml` renders + uploads the slate to Drive, a final step runs
`automation/scripts/post-to-uploadpost.py`, which uploads each local `video.mp4` + its
`caption.txt` to upload-post (`POST /api/upload`, `Authorization: Apikey`), async, then polls
to confirm. It is:
- **Off until keyed** — the step is skipped unless the `UPLOAD_POST_API_KEY` secret is set.
- **Idempotent** — writes `.posted.json` per slug; re-runs never double-post.
- **Fail-isolated** — one bad slug/platform never blocks the others.
- **Kill-switchable** — uncheck the `auto_post` input on a manual run to render+Drive only.

## One-time setup (Ahmed — ~10 min)
1. **Sign up + subscribe** at https://app.upload-post.com — the **Basic (~$16/mo)** plan includes
   API access. (Free tier = 10 uploads/mo if you want to test first.)
2. **Make IG postable:** in the Instagram app for **@photonect.news**, switch to a
   **Business or Creator** account and link it to a **Facebook Page** (create a free Page if needed).
   This is a hard Meta requirement — API posting fails without it.
3. **Connect accounts** in the upload-post dashboard: Connect → Instagram (authorize), then
   Connect → TikTok (authorize). Create one **profile** named `photonect-news` and attach BOTH.
4. **Copy your API key** from the dashboard's **API Keys** page.
5. **Add two GitHub secrets** at
   `github.com/AhmedAlhamzawi/photonect-news → Settings → Secrets and variables → Actions → New repository secret`:
   - `UPLOAD_POST_API_KEY` = your upload-post API key
   - `UPLOAD_POST_USER` = `photonect-news` (the exact profile handle from step 3)

That's it. The next daily run (2 PM Baghdad) will auto-post to IG + TikTok. To test immediately,
trigger `render-day.yml` manually for today's date.

## Notes / risks
- **No human review gate by default** — every rendered slate publishes. The daily content already
  passes an Opus editorial-QA gate before render, but a bad render would go straight to the public
  feed. To pause posting any day: uncheck `auto_post` on a manual run, or remove the
  `UPLOAD_POST_API_KEY` secret.
- Per-account caps (IG ~50/day, TikTok ~15/day) are far above our 6/day.
- TikTok posts go out **public** (`DIRECT_POST` + `PUBLIC_TO_EVERYONE`); confirm the first one
  landed public, not self-only.
