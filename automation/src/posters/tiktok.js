/**
 * TikTok Content Posting API poster (PULL_FROM_URL flow).
 *
 * Flow:
 *   1. POST /v2/post/publish/video/init/  with source=PULL_FROM_URL + video_url + title + privacy_level
 *      -> publish_id
 *   2. Poll POST /v2/post/publish/status/fetch/  until status=PUBLISH_COMPLETE
 *      (or PROCESSING_*/SEND_TO_USER_INBOX/FAILED)
 *
 * Reference: developers.tiktok.com/doc/content-posting-api-reference-direct-post
 *
 * IMPORTANT requirements:
 *   - App must be approved for "video.publish" scope. Sandbox mode works for
 *     posting to the developer account as a "SELF_ONLY" draft. Public posting
 *     requires audit approval.
 *   - Access token is short-lived (~24h). Refresh before expiry using
 *     refresh_token + grant_type=refresh_token.
 *   - Video URL must be HTTPS with valid cert. Cloudinary URLs work.
 *   - Video must be mp4/mov/webm, <= 500MB, <= 10min. Our 30s h264 is fine.
 */

const OPEN_API = "https://open.tiktokapis.com";

async function tfetch(pathname, { method = "POST", body, token } = {}) {
  const access = token ?? process.env.TIKTOK_USER_ACCESS_TOKEN;
  if (!access) throw new Error("TIKTOK_USER_ACCESS_TOKEN not set");
  const res = await fetch(`${OPEN_API}${pathname}`, {
    method,
    headers: {
      Authorization: `Bearer ${access}`,
      "Content-Type": "application/json",
    },
    body: body ? JSON.stringify(body) : undefined,
  });
  const data = await res.json().catch(() => ({}));
  if (!res.ok || data?.error?.code && data.error.code !== "ok") {
    throw new Error(`TikTok ${method} ${pathname} failed: ${res.status} ${JSON.stringify(data)}`);
  }
  return data;
}

async function init({ videoUrl, title }) {
  const body = {
    post_info: {
      title: title.slice(0, 2200), // TikTok caption limit
      privacy_level: process.env.TIKTOK_PRIVACY_LEVEL || "PUBLIC_TO_EVERYONE",
      disable_duet: false,
      disable_comment: false,
      disable_stitch: false,
      video_cover_timestamp_ms: 1000,
    },
    source_info: {
      source: "PULL_FROM_URL",
      video_url: videoUrl,
    },
  };
  const data = await tfetch("/v2/post/publish/video/init/", { body });
  const publishId = data?.data?.publish_id;
  if (!publishId) throw new Error(`No publish_id in TikTok init response: ${JSON.stringify(data)}`);
  return publishId;
}

async function waitForPublished(publishId, { timeoutMs = 8 * 60 * 1000 } = {}) {
  const started = Date.now();
  let delay = 4000;
  while (Date.now() - started < timeoutMs) {
    const data = await tfetch("/v2/post/publish/status/fetch/", { body: { publish_id: publishId } });
    const status = data?.data?.status;
    if (status === "PUBLISH_COMPLETE") return data.data;
    if (status === "FAILED") throw new Error(`TikTok publish FAILED: ${JSON.stringify(data)}`);
    // PROCESSING_DOWNLOAD / PROCESSING_UPLOAD / SEND_TO_USER_INBOX etc. -> keep waiting
    await new Promise(r => setTimeout(r, delay));
    delay = Math.min(delay * 1.3, 15000);
  }
  throw new Error(`TikTok publish ${publishId} did not complete within ${timeoutMs}ms`);
}

/**
 * Refresh the TikTok access token using the refresh token.
 * Call this before posting if you suspect the token is stale.
 */
export async function refreshToken() {
  const res = await fetch(`${OPEN_API}/v2/oauth/token/`, {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({
      client_key: process.env.TIKTOK_CLIENT_KEY,
      client_secret: process.env.TIKTOK_CLIENT_SECRET,
      grant_type: "refresh_token",
      refresh_token: process.env.TIKTOK_USER_REFRESH_TOKEN,
    }),
  });
  const data = await res.json();
  if (!data?.access_token) throw new Error(`TikTok refresh failed: ${JSON.stringify(data)}`);
  return {
    accessToken: data.access_token,
    refreshToken: data.refresh_token,
    expiresIn: data.expires_in,
  };
}

/**
 * Publish a reel to TikTok.
 * @param {{ videoUrl: string, caption: string, slug: string }} opts
 */
export async function postVideo({ videoUrl, caption, slug }) {
  if (process.env.DRY_RUN === "true") {
    console.log(`[tt] DRY_RUN — would post slug=${slug} videoUrl=${videoUrl}`);
    return { publishId: "dry-run" };
  }
  const publishId = await init({ videoUrl, title: caption });
  console.log(`[tt] init publishId=${publishId} slug=${slug} — waiting for PUBLISH_COMPLETE`);
  const detail = await waitForPublished(publishId);
  console.log(`[tt] published publishId=${publishId} slug=${slug}`);
  return { publishId, detail };
}
