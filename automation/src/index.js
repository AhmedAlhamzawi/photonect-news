import "dotenv/config";
import cron from "node-cron";
import { pickNext } from "./queue.js";
import { uploadVideo } from "./uploader.js";
import { postReel } from "./posters/instagram.js";
import { postVideo as postTikTok } from "./posters/tiktok.js";
import { markPosted } from "./state.js";

/**
 * One posting cycle: pick next post respecting diversity, upload to Cloudinary,
 * then publish to both IG and TikTok. Idempotent — state.js prevents double-posts.
 */
async function runOnce() {
  const stamp = new Date().toISOString();
  console.log(`\n[${stamp}] === posting cycle start ===`);

  // Pick one post to handle. Because state tracks per-platform, if IG was posted
  // but TikTok is behind, queue.pickNext('tiktok') will still return that post.
  let post = await pickNext("instagram");
  if (!post) post = await pickNext("tiktok");
  if (!post) {
    console.log("queue is empty — nothing to post");
    return;
  }

  console.log(`selected slug=${post.slug} bucket=${post.bucket} variant=${post.videoVariant}`);

  let videoUrl;
  try {
    videoUrl = await uploadVideo({ slug: post.slug, localPath: post.videoPath });
    console.log(`cloudinary url: ${videoUrl}`);
  } catch (err) {
    console.error(`upload failed for slug=${post.slug}:`, err.message);
    return;
  }

  // IG and TikTok can go in parallel — Cloudinary URL is the same for both.
  const tasks = [];
  tasks.push(
    postReel({ videoUrl, caption: post.caption, slug: post.slug })
      .then(result => markPosted(post.slug, "instagram", { ...result, bucket: post.bucket, videoUrl }))
      .catch(err => console.error(`[ig] slug=${post.slug} failed:`, err.message))
  );
  tasks.push(
    postTikTok({ videoUrl, caption: post.caption, slug: post.slug })
      .then(result => markPosted(post.slug, "tiktok", { ...result, bucket: post.bucket, videoUrl }))
      .catch(err => console.error(`[tt] slug=${post.slug} failed:`, err.message))
  );

  await Promise.allSettled(tasks);
  console.log(`[${new Date().toISOString()}] === cycle done ===`);
}

const once = process.argv.includes("--once");

if (once) {
  runOnce()
    .catch(err => {
      console.error("fatal:", err);
      process.exit(1);
    });
} else {
  const expr = process.env.POST_CRON || "0 */2 * * *";
  console.log(`scheduler starting — cron=${expr}`);
  cron.schedule(expr, () => {
    runOnce().catch(err => console.error("cycle error:", err));
  });
  console.log("scheduler ready. Ctrl+C to stop.");
}
