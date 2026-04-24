/**
 * Instagram Graph API poster (REELS flow).
 *
 * Flow:
 *   1. POST /{ig_user_id}/media      with media_type=REELS + video_url + caption -> creation_id
 *   2. Poll GET /{creation_id}       until status_code=FINISHED (or ERROR/EXPIRED)
 *   3. POST /{ig_user_id}/media_publish with creation_id -> published media id
 *
 * Reference: developers.facebook.com/docs/instagram-platform/content-publishing
 */

const GRAPH = "https://graph.facebook.com/v21.0";

async function gfetch(pathname, { method = "GET", params = {}, body } = {}) {
  const token = process.env.META_LONG_LIVED_USER_TOKEN;
  if (!token) throw new Error("META_LONG_LIVED_USER_TOKEN not set");
  const url = new URL(`${GRAPH}${pathname}`);
  for (const [k, v] of Object.entries(params)) if (v !== undefined) url.searchParams.set(k, v);
  url.searchParams.set("access_token", token);
  const res = await fetch(url, {
    method,
    headers: body ? { "Content-Type": "application/json" } : undefined,
    body: body ? JSON.stringify(body) : undefined,
  });
  const data = await res.json().catch(() => ({}));
  if (!res.ok) {
    throw new Error(`IG Graph ${method} ${pathname} failed: ${res.status} ${JSON.stringify(data)}`);
  }
  return data;
}

async function createContainer({ igUserId, videoUrl, caption }) {
  const data = await gfetch(`/${igUserId}/media`, {
    method: "POST",
    params: {
      media_type: "REELS",
      video_url: videoUrl,
      caption,
      share_to_feed: "true",
    },
  });
  if (!data.id) throw new Error(`No container id returned: ${JSON.stringify(data)}`);
  return data.id;
}

async function waitForFinished(containerId, { timeoutMs = 5 * 60 * 1000 } = {}) {
  const started = Date.now();
  let delay = 3000;
  while (Date.now() - started < timeoutMs) {
    const data = await gfetch(`/${containerId}`, { params: { fields: "status_code,status" } });
    if (data.status_code === "FINISHED") return;
    if (data.status_code === "ERROR" || data.status_code === "EXPIRED") {
      throw new Error(`IG container ${containerId} entered ${data.status_code}: ${data.status ?? ""}`);
    }
    await new Promise(r => setTimeout(r, delay));
    delay = Math.min(delay * 1.3, 15000);
  }
  throw new Error(`IG container ${containerId} did not finish within ${timeoutMs}ms`);
}

async function publish({ igUserId, containerId }) {
  const data = await gfetch(`/${igUserId}/media_publish`, {
    method: "POST",
    params: { creation_id: containerId },
  });
  if (!data.id) throw new Error(`No published media id returned: ${JSON.stringify(data)}`);
  return data.id;
}

/**
 * Publish a reel to Instagram.
 * @param {{ videoUrl: string, caption: string, slug: string }} opts
 * @returns {Promise<{ mediaId: string, permalink?: string }>}
 */
export async function postReel({ videoUrl, caption, slug }) {
  const igUserId = process.env.IG_BUSINESS_ACCOUNT_ID;
  if (!igUserId) throw new Error("IG_BUSINESS_ACCOUNT_ID not set");
  if (process.env.DRY_RUN === "true") {
    console.log(`[ig] DRY_RUN — would post reel slug=${slug} videoUrl=${videoUrl}`);
    return { mediaId: "dry-run", permalink: null };
  }
  const containerId = await createContainer({ igUserId, videoUrl, caption });
  console.log(`[ig] container=${containerId} slug=${slug} — waiting for FINISHED`);
  await waitForFinished(containerId);
  const mediaId = await publish({ igUserId, containerId });
  console.log(`[ig] published mediaId=${mediaId} slug=${slug}`);

  let permalink = null;
  try {
    const p = await gfetch(`/${mediaId}`, { params: { fields: "permalink" } });
    permalink = p.permalink ?? null;
  } catch { /* ignore */ }

  return { mediaId, permalink };
}
