import { z } from "zod";

// Life is Hard Store — parametrized product ad. One composition → N products.
// Real Fedshi footage (authentic: shows what the customer receives) + brand
// kinetic Arabic captions + logo bug + music. All copy is programmatic (never
// AI-image text) so Arabic renders correctly.
export const productAdSchema = z.object({
  clip: z.string(), // staticFile path e.g. "fedshi/clips/AFAQ2.mp4"
  clipStartSec: z.number().default(0), // skip into the footage to the good part
  brandIcon: z.string().default("fedshi/brand/icon.png"),

  teal: z.string().default("#1FFCC1"),
  charcoal: z.string().default("#222931"),

  hook: z.string(), // beat 1 — the scroll-stopper
  benefit: z.string(), // beat 2 — why you want it
  price: z.string(), // beat 3 — e.g. "٢٥,٠٠٠"
  priceUnit: z.string().default("دينار فقط"),
  priceNote: z.string().default("الدفع عند الاستلام ✅"),
  cta: z.string().default("اطلب هسه 👇"),
  ctaNote: z.string().default("توصيل لكل محافظات العراق 🚗"),

  audioBed: z.string().default("audio/bed_pulse_syn.mp3"),
  bedVolume: z.number().default(0.55),
});

export type ProductAdProps = z.infer<typeof productAdSchema>;
