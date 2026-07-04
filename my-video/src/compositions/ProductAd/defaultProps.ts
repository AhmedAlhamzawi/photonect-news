import type { ProductAdProps } from "./schema";

// Speaker (AFAQ2) — the default preview. Other products override via --props.
export const productAdDefaultProps: ProductAdProps = {
  clip: "fedshi/clips/AFAQ2.mp4",
  clipStartSec: 3,
  brandIcon: "fedshi/brand/icon.png",
  teal: "#1FFCC1",
  charcoal: "#222931",
  hook: "سبيكر كرستال يضوّي بالألوان 🌈",
  benefit: "صوت خرافي وإضاءة تغيّر جوّ غرفتك 🔥",
  price: "٢٥,٠٠٠",
  priceUnit: "دينار فقط",
  priceNote: "الدفع عند الاستلام ✅",
  cta: "اطلب هسه 👇",
  ctaNote: "توصيل لكل محافظات العراق 🚗",
  audioBed: "audio/bed_pulse_syn.mp3",
  bedVolume: 0.55,
};

export const PRODUCT_AD_TOTAL_FRAMES = 18 * 30; // 18s @ 30fps
