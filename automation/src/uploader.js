import { v2 as cloudinary } from "cloudinary";

let configured = false;

function configure() {
  if (configured) return;
  cloudinary.config({
    cloud_name: process.env.CLOUDINARY_CLOUD_NAME,
    api_key: process.env.CLOUDINARY_API_KEY,
    api_secret: process.env.CLOUDINARY_API_SECRET,
    secure: true,
  });
  configured = true;
}

/**
 * Upload a local mp4 to Cloudinary. Returns a public HTTPS URL suitable for
 * IG Graph's `video_url` param and TikTok Content Posting API's PULL_FROM_URL.
 *
 * Notes:
 *  - IG Reels must be h264 + AAC, <= 1GB, <= 90min. Our output (NewsReel) is 30s
 *    h264/aac so we're fine.
 *  - Cloudinary strips query params on the delivery URL by default.
 *  - public_id uses the slug so re-uploads overwrite.
 */
export async function uploadVideo({ slug, localPath }) {
  configure();
  const res = await cloudinary.uploader.upload(localPath, {
    resource_type: "video",
    folder: "photonect-news",
    public_id: slug,
    overwrite: true,
    invalidate: true,
  });
  if (!res?.secure_url) throw new Error(`Cloudinary upload returned no secure_url: ${JSON.stringify(res)}`);
  return res.secure_url;
}

export async function deleteVideo(slug) {
  configure();
  await cloudinary.uploader.destroy(`photonect-news/${slug}`, { resource_type: "video", invalidate: true });
}
