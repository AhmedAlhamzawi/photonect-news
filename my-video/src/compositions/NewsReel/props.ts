import { NewsReelProps } from "./schema";
import { PHOTONECT } from "../PhotonectBrandReel/brand";

// 2026-04-17 — US Hormuz blockade, week 2
// Lead: ships "spoofing" transponders to breach blockade; Iran warns truce at risk;
//       jet fuel soaring; Iran routing oil via Russia; Trump says truce talks in days.
// Sources cross-verified across NPR, Al Jazeera English, BBC News, CBS News, ABC News, Fortune, Reuters.

export const HORMUZ_WEEK2_PROPS: NewsReelProps = {
  dateLabel: "APR 17 • 2026",
  arabicDateLabel: "١٧ أبريل ٢٠٢٦",
  handle: "@photonect.news",
  audioBed: "audio/news_bed.mp3",

  breaking: {
    arabicKicker: "عاجل",
    arabicHeadline: "سفن تُزيّف هويتها لاختراق الحصار الأمريكي في هرمز",
    englishSubhead: "HORMUZ BLOCKADE • DAY 4",
    heroMedia: "images/news/2026-04-17-hormuz/broll_tanker.mp4",
    heroMediaType: "video",
  },

  beats: [
    {
      label: "ماذا يحدث؟",
      arabicHeading: "مشاة البحرية الأمريكية يعترضون سفن مرتبطة بإيران — وبعضها يبدّل الإشارات للتمرير",
      arabicBody:
        "بدأت القوات الأمريكية دوريات رسمية في مضيق هرمز، وسُفن تحاول اختراق الحصار بتزوير بيانات الـAIS. إيران توقف صادرات البتروكيماويات، وتدرس إعادة توجيه النفط عبر روسيا.",
      bigStat: {
        value: "4",
        label: "days of blockade",
        arabicLabel: "اليوم الرابع من الحصار",
      },
      supportingStats: [
        { label: "صادرات إيران البتروكيماوية", value: "PAUSED" },
        { label: "سفن يُشتبه بتزوير هويتها", value: "12+" },
        { label: "بديل التصدير المقترح", value: "RUSSIA" },
        { label: "مناورات مشاة البحرية", value: "USS TRIPOLI" },
      ],
      broll: "images/news/2026-04-17-hormuz/broll_carrier.mp4",
      brollType: "video",
      accent: PHOTONECT.signal,
      photoInsert: "images/news/2026-04-17-hormuz/wire_photo.jpg",
      photoCaption: "Getty / NPR — دورية أمريكية في هرمز",
    },
    {
      label: "لماذا يهم؟",
      arabicHeading: "وقود الطائرات يقفز عالمياً — وشركات طيران أوروبية على حافة النقص",
      arabicBody:
        "ارتفاع حاد في تكاليف وقود الطائرات ينقل آثار الحصار من الخليج إلى صالات المطارات العالمية. إيران تحذّر بأن استمرار الحصار يُهدد الهدنة، ومنظمات الشحن تدرس طرق بديلة أطول وأغلى.",
      bigStat: {
        value: "+34%",
        label: "jet fuel spike",
        arabicLabel: "قفزة في وقود الطائرات خلال أسبوع",
      },
      supportingStats: [
        { label: "مخاطر النقص في أوروبا", value: "HIGH" },
        { label: "الشحنات الإيرانية المحوّلة", value: "REROUTING" },
        { label: "صندوق النقد يحذر", value: "IMF ALERT" },
        { label: "ضغط على هدنة إيران", value: "AT RISK" },
      ],
      broll: "images/news/2026-04-17-hormuz/still_refinery.jpg",
      brollType: "image",
      accent: "#FF6B3D",
    },
    {
      label: "ماذا بعد؟",
      arabicHeading: "ترامب يُلمّح لاستئناف المحادثات خلال أيام — وإيران تضع روسيا بديلاً للتصدير",
      arabicBody:
        "ثلاثة مسارات محتملة خلال 72 ساعة: استئناف محادثات الهدنة، أو تمديد الحصار وموجة تصعيد، أو تحول هيكلي لصادرات النفط الإيرانية إلى ممرات بديلة عبر روسيا وباكستان.",
      bigStat: {
        value: "72h",
        label: "crucial next 72 hours",
        arabicLabel: "ساعة قادمة حاسمة",
      },
      supportingStats: [
        { label: "السيناريو الأول", value: "TRUCE TALKS" },
        { label: "السيناريو الثاني", value: "ESCALATION" },
        { label: "السيناريو الثالث", value: "REROUTE" },
      ],
      broll: "images/news/2026-04-17-hormuz/broll_cargo_night.mp4",
      brollType: "video",
      accent: "#5B8FF9",
      mapOverlay: "hormuz",
    },
  ],

  sources: [
    { name: "NPR", domain: "npr.org" },
    { name: "Al Jazeera English", domain: "aljazeera.com" },
    { name: "BBC News", domain: "bbc.com/news" },
    { name: "CBS News", domain: "cbsnews.com" },
    { name: "ABC News", domain: "abcnews.com" },
    { name: "Fortune", domain: "fortune.com" },
  ],

  arabicTicker: [
    "مشاة البحرية الأمريكية في تدريبات إنزال حيّة على يو إس إس تريبولي قرب هرمز",
    "إيران توقف صادرات البتروكيماويات وتدرس إعادة توجيه النفط عبر روسيا",
    "صندوق النقد الدولي يحذر: سعر النفط قد يلسع المستهلكين حول العالم",
    "شركات طيران أوروبية تتحسّب لنقص محتمل في وقود الطائرات",
    "ترامب: محادثات الهدنة مع إيران قد تعود خلال أيام رغم استمرار الحصار",
    "BBC: هل ينجح الحصار الأمريكي في تركيع طهران؟",
    "CBS: إيران تدّعي نجاح ناقلة في عبور المضيق رغم الحصار",
  ],
};
