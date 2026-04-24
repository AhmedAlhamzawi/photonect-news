# Setup: Cloudinary (public video host)

**Why:** Instagram and TikTok APIs pull videos from a public HTTPS URL — they don't accept direct binary uploads for the kind of workflow we need. Cloudinary's free tier gives us 25 GB storage + 25 GB bandwidth/month, which is way more than 12 posts/day × 40 MB × 30 = ~14 GB/month.

**Time:** ~5 minutes.

## Steps

1. Go to **[cloudinary.com/users/register_free](https://cloudinary.com/users/register_free)**
2. Sign up with the photonect.net email. Pick **Programmable Media** when prompted for product focus.
3. After signup you land on the **Dashboard**. At the top you'll see:
   - Cloud name
   - API Key
   - API Secret (click "Reveal")
4. Paste them into `automation/.env`:
   ```
   CLOUDINARY_CLOUD_NAME=...
   CLOUDINARY_API_KEY=...
   CLOUDINARY_API_SECRET=...
   ```
5. Verify with a dry-run:
   ```bash
   cd automation
   npm install
   DRY_RUN=true npm run test:ig 2026-04-17-hormuz-week2
   ```
   You should see `cloudinary url: https://res.cloudinary.com/.../video/upload/...` printed, then `[ig] DRY_RUN — would post ...`.

## Notes

- Videos are uploaded under `photonect-news/<slug>` and overwritten on re-render.
- To clean up old uploads: Cloudinary Dashboard → Media Library → photonect-news folder.
- If bandwidth ever becomes an issue, upgrade to Plus plan ($99/mo for 225 GB) or switch to S3 + CloudFront (cheaper but more setup).
