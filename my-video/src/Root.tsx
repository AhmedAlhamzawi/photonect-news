import "./index.css";
import { Composition, staticFile } from "remotion";
import { MyComposition } from "./Composition";
import { PhotonectBrandReel } from "./compositions/PhotonectBrandReel/PhotonectBrandReel";
import { BrandReelSchema } from "./compositions/PhotonectBrandReel/schema";
import { PHOTONECT } from "./compositions/PhotonectBrandReel/brand";
import {
  AINewsDaily,
  computeAINewsDailyDurationInFrames,
} from "./compositions/AINewsDaily/AINewsDaily";
import { AINewsDailySchema, AINewsDailyProps } from "./compositions/AINewsDaily/schema";
import { NewsReel } from "./compositions/NewsReel/NewsReel";
import { NewsReelSchema, computeNewsReelDurationInFrames } from "./compositions/NewsReel/schema";
import { HORMUZ_WEEK2_PROPS } from "./compositions/NewsReel/props";
import { Hekaya } from "./compositions/Hekaya/Hekaya";
import { HekayaSchema, computeHekayaDurationInFrames } from "./compositions/Hekaya/schema";

const DURATION_SECONDS = 15;
const FPS = 30;

// Photonect default copy — Ahmed's business (media production + AI automation + events/fabrication)
const photonectProps = {
  brandName: "photonect",
  brandSlug: "photonect",
  primary: PHOTONECT.paper,
  secondary: PHOTONECT.signal,
  accent: PHOTONECT.signal,
  background: PHOTONECT.ink,
  paper: PHOTONECT.paper,
  taglineLatin: "Where Light Meets Logic",
  taglineArabic: "حيث يلتقي الضوء بالذكاء",
  benefits: [
    {
      headline: "Brand kits in hours, not weeks.",
      body: "AI-driven identity systems, engineered for Iraqi brands.",
    },
    {
      headline: "Content that scales itself.",
      body: "Automated production pipelines for social, video, and print.",
    },
    {
      headline: "Iraq-first, world-class.",
      body: "Local craft, global execution — delivered end-to-end.",
    },
  ],
  cta: {
    text: "Let's build something magnificent.",
    url: "photonect.net",
  },
  durationInSeconds: DURATION_SECONDS,
};

// AI News Daily — April 15, 2026
// V6 — ASML earnings day, Anthropic $30B ARR, Meta-CoreWeave $35B, Gemini Robotics 93%, Gemini 3.1 benchmark race.
// Image Truth Protocol: thematic backdrops from Unsplash/Pexels.
// NO AI-generated images. NO fake subjects.
const IMG = {
  finance: staticFile("images/daily/story_1_20260415.jpg"),    // finance/trading — Anthropic $30B ARR
  chip: staticFile("images/daily/story_2_20260415.jpg"),       // semiconductor chip — ASML Q1 earnings
  datacenter: staticFile("images/daily/story_3_20260415.jpg"), // server room — Meta×CoreWeave alliance
  robot: staticFile("images/daily/story_4_20260415.jpg"),      // Spot robot — Gemini Robotics-ER 1.6
  terminal: staticFile("images/daily/story_5_20260415.jpg"),   // code/AI — Gemini 3.1 Pro benchmark race
  // Fallbacks from V4
  fallback_money: staticFile("images/ainews_v4/money.jpg"),
  fallback_dc: staticFile("images/ainews_v4/datacenter.jpg"),
  fallback_hand: staticFile("images/ainews_v4/handshake.jpg"),
  fallback_chart: staticFile("images/ainews_v4/chart.jpg"),
  fallback_term: staticFile("images/ainews_v4/terminal.jpg"),
};

// Brand palette for BrandMark badges
const BRAND = {
  anthropic: "#D97757",
  openai: "#10A37F",
  google: "#4285F4",
  meta: "#0668E1",
  coreweave: "#FF6B00",
  deepseek: "#4A6CF7",
  nvidia: "#76B900",
  asml: "#0071C5",
};

const aiNewsProps: AINewsDailyProps = {
  dateLabel: "APR 15 • 2026",
  arabicDateLabel: "١٥ أبريل ٢٠٢٦",
  handle: "@photonect.news",
  tickerHeadlines: [
    "OPENAI CFO CONFIRMS RETAIL INVESTORS GET IPO ALLOCATION AHEAD OF RUMORED Q4 2026 DEBUT AT ~$1T",
    "OPENAI PROJECTS $2.5B IN AD REVENUE 2026 — TARGETING $100B BY 2030 AFTER TBPN ACQUISITION",
    "CLAUDE MYTHOS WITHHELD FROM PUBLIC — RESTRICTED TO 40 PARTNERS UNDER PROJECT GLASSWING",
    "ASIA AI STARTUP FUNDING HITS $27.4B IN Q1 2026 — CHINA LEADS WITH $16.5B",
    "MCP CROSSES 97M MONTHLY SDK INSTALLS — ANTHROPIC DONATES PROTOCOL TO LINUX FOUNDATION",
    "UTAH FIRST US STATE TO LET AI RENEW DRUG PRESCRIPTIONS WITHOUT PHYSICIAN SIGN-OFF",
    "CALIFORNIA COURT: GENERATIVE AI IN ADS TRIGGERS PRIMARY LIABILITY UNDER SECURITIES LAW",
  ],
  arabicTickerHeadlines: [
    "المدير المالي لأوبن أي آي يؤكد حصول المستثمرين الأفراد على أسهم الطرح العام المتوقع نهاية ٢٠٢٦",
    "أوبن أي آي تتوقع ٢٫٥ مليار دولار إيرادات إعلانية في ٢٠٢٦ وتستهدف ١٠٠ مليار بحلول ٢٠٣٠",
    "أنثروبيك تحجب كلود ميثوس — مقيّد لـ٤٠ شريكاً فقط بسبب خطر الأسلحة السيبرانية",
    "تمويل شركات الذكاء الاصطناعي الآسيوية يبلغ ٢٧٫٤ مليار في الربع الأول — الصين تقود بـ١٦٫٥ مليار",
    "بروتوكول MCP يتخطى ٩٧ مليون تثبيت شهرياً — أنثروبيك تتبرع به لمؤسسة لينكس",
    "يوتا أول ولاية أمريكية تمنح الذكاء الاصطناعي صلاحية تجديد الوصفات الطبية دون موافقة طبيب",
    "محكمة كاليفورنيا: الإعلانات بالذكاء الاصطناعي التوليدي تُعرّض المنصات للمسؤولية بقانون الاحتيال المالي",
  ],
  stories: [
    {
      // 1 — Anthropic $30B ARR — tripled from $9B in 4 months
      variant: "bigNumber",
      kicker: "ANTHROPIC • REVENUE",
      arabicKicker: "",
      prefix: "$",
      value: 30,
      suffix: "B",
      decimals: 0,
      label: "ARR — 3× in 4 months",
      arabic: "أنثروبيك تصل ٣٠ مليار دولار — تضاعفت ثلاث مرات خلال ٤ أشهر فقط",
      images: [IMG.finance],
      supportingStats: [
        { label: "4 MONTHS AGO", value: "$9B" },
        { label: "YOY GROWTH", value: "+1,400%" },
        { label: "ENTERPRISE CLIENTS", value: "1,000+" },
        { label: "FORTUNE 10", value: "8 / 10" },
      ],
      context:
        "8 of the 10 biggest companies on Earth now pay for Claude. The gap with OpenAI is shrinking by billions per week.",
      arabicContext:
        "٨ من أكبر ١٠ شركات في العالم تدفع الآن مقابل كلود. الفجوة مع أوبن أي آي تتقلص بمليارات كل أسبوع.",
    },
    {
      // 2 — ASML Q1 2026 beats + raises guidance — AI chip demand accelerating
      variant: "compute",
      kicker: "ASML • EARNINGS BEAT",
      arabicKicker: "",
      value: 40,
      unit: "B EUR",
      label: "2026 GUIDANCE — RAISED TODAY",
      partners: ["ASML", "TSMC", "SAMSUNG"],
      arabic: "ASML ترفع توقعاتها إلى ٤٠ مليار يورو — الطلب على رقاقات الذكاء الاصطناعي يتسارع",
      images: [IMG.chip],
      supportingStats: [
        { label: "Q1 SALES", value: "€8.8B beat" },
        { label: "Q1 PROFIT", value: "€2.8B beat" },
        { label: "MARGIN", value: "53%" },
        { label: "OLD GUIDE", value: "€34–39B" },
      ],
      context:
        "Every advanced AI chip requires ASML's machines. Their raised outlook proves the infrastructure boom is accelerating.",
      arabicContext:
        "كل رقاقة ذكاء اصطناعي متقدمة تحتاج آلات ASML. رفع التوقعات يثبت أن طفرة البنية التحتية تتسارع ولا تتباطأ.",
    },
    {
      // 3 — Meta × CoreWeave $35B inference pact through 2032
      variant: "alliance",
      kicker: "META × COREWEAVE × NVIDIA",
      arabicKicker: "",
      nodes: [
        { label: "META", initials: "M", brandColor: BRAND.meta },
        { label: "COREWEAVE", initials: "CW", brandColor: BRAND.coreweave },
        { label: "NVIDIA", initials: "NV", brandColor: BRAND.nvidia },
      ],
      verdict: "$35B inference pact through 2032.",
      arabic: "صفقة ٣٥ مليار دولار لبناء أكبر بنية استنتاج في التاريخ",
      images: [IMG.datacenter],
      context:
        "Even Meta — spending $135B this year — can't build fast enough. They're renting $35B more from CoreWeave for AI inference at civilization scale.",
      arabicContext:
        "حتى ميتا التي تنفق ١٣٥ مليار هذا العام لا تستطيع البناء بسرعة كافية — فاستأجرت ٣٥ مليار إضافية من كورويف لتشغيل الذكاء الاصطناعي على نطاق حضاري.",
    },
    {
      // 4 — Spot robot reads gauges at 93% — up from 23% one version ago
      variant: "reveal",
      kicker: "DEEPMIND × BOSTON DYNAMICS",
      arabicKicker: "",
      title: "93% ACCURACY",
      quote: "Spot reads gauges — up from 23% one version ago.",
      arabic: "روبوت سبوت يقرأ المقاييس بدقة ٩٣٪ — كانت ٢٣٪ في الإصدار السابق",
      images: [IMG.robot],
      supportingStats: [
        { label: "PREV VERSION", value: "23%" },
        { label: "FLASH BASELINE", value: "67%" },
        { label: "WITHOUT VISION", value: "86%" },
        { label: "API LAUNCH", value: "Apr 14" },
      ],
      context:
        "A 4× accuracy leap in one release. Spot now inspects factories autonomously — no humans needed.",
      arabicContext:
        "قفزة أربعة أضعاف في الدقة بإصدار واحد. سبوت يفحص المصانع الآن بشكل مستقل — بدون تدخل بشري.",
    },
    {
      // 5 — Gemini 3.1 Pro leads 13/16 benchmarks and costs 87% less
      variant: "race",
      kicker: "GOOGLE • AI RACE",
      arabicKicker: "",
      arabic: "جيميناي يتصدر ١٣ من ١٦ معياراً — بسعر أقل ٨٧٪ من المنافسين",
      unit: "ARC-AGI-2",
      images: [IMG.terminal],
      items: [
        { label: "GEMINI 3.1 PRO", value: 77, color: BRAND.google, initials: "G", growth: "13/16 wins" },
        { label: "CLAUDE OPUS 4.6", value: 66, color: BRAND.anthropic, initials: "A", growth: "#1 coding" },
        { label: "GPT-5.2", value: 53, color: BRAND.openai, initials: "OAI", growth: "#1 reasoning" },
        { label: "DEEPSEEK R4", value: 48, color: BRAND.deepseek, initials: "DS", growth: "cheapest" },
      ],
      context:
        "$2/M tokens vs $15 for Claude. Google is turning frontier AI into a commodity and forcing everyone to justify their prices.",
      arabicContext:
        "دولاران لكل مليون رمز مقابل ١٥ لكلود. غوغل تحوّل الذكاء الاصطناعي إلى سلعة رخيصة وتجبر الجميع على تبرير أسعارهم.",
    },
  ],
};

const AI_NEWS_FPS = 30;

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="MyComp"
        component={MyComposition}
        durationInFrames={60}
        fps={30}
        width={1280}
        height={720}
      />
      <Composition
        id="PhotonectBrandReel"
        component={PhotonectBrandReel}
        durationInFrames={DURATION_SECONDS * FPS}
        fps={FPS}
        width={1080}
        height={1920}
        schema={BrandReelSchema}
        defaultProps={photonectProps}
      />
      <Composition
        id="AINewsDaily"
        component={AINewsDaily}
        durationInFrames={computeAINewsDailyDurationInFrames(aiNewsProps.stories.length)}
        fps={AI_NEWS_FPS}
        width={1080}
        height={1920}
        schema={AINewsDailySchema}
        defaultProps={aiNewsProps}
      />
      <Composition
        id="NewsReel"
        component={NewsReel}
        durationInFrames={computeNewsReelDurationInFrames()}
        fps={30}
        width={1080}
        height={1920}
        schema={NewsReelSchema}
        defaultProps={HORMUZ_WEEK2_PROPS}
      />
      {/* HEKAYA — slow-storytelling sister track. Same channel, opposite rhythm.
          75-second reels, bespoke Suno tracks per story, warm dusk palette.
          Default props are a placeholder: render-hekaya.yml passes per-slug
          props.json via --props at render time, so this default is purely for
          local Remotion Studio preview. */}
      <Composition
        id="Hekaya"
        component={Hekaya}
        durationInFrames={computeHekayaDurationInFrames()}
        fps={30}
        width={1080}
        height={1920}
        schema={HekayaSchema}
        defaultProps={{
          dateLabel: "MAY 01 • 2026",
          arabicDateLabel: "١ مايو ٢٠٢٦",
          handle: "@photonect.news",
          audioBed: "audio/hekaya/_preview.mp3",
          prologue: {
            arabicTitle: "حكاية تُروى ببطء",
            englishSubtitle: "A TALE TOLD SLOWLY",
            era: "PREVIEW",
            place: "PLACEHOLDER",
            arabicHook:
              "في هذه الزاوية من القناة، نروي ما لا تخطفه الأخبار. نقف مع التاريخ كما يقف المرء مع نهر قديم.",
            heroMedia: "images/hekaya/_preview/hero.jpg",
            heroMediaType: "image",
          },
          chapters: [
            {
              arabicTitle: "الفصل الأول",
              arabicNarration:
                "هذا نصّ تجريبي. سيُستبدل بمحتوى الحكاية الفعليّة عند تمرير props.json الخاصة بكل قصّة وقت التصيير.",
              visual: "images/hekaya/_preview/chapter_1.jpg",
              visualType: "image",
            },
            {
              arabicTitle: "الفصل الثاني",
              arabicNarration:
                "هذا نصّ تجريبي. سيُستبدل بمحتوى الحكاية الفعليّة عند تمرير props.json الخاصة بكل قصّة وقت التصيير.",
              visual: "images/hekaya/_preview/chapter_2.jpg",
              visualType: "image",
            },
            {
              arabicTitle: "الفصل الثالث",
              arabicNarration:
                "هذا نصّ تجريبي. سيُستبدل بمحتوى الحكاية الفعليّة عند تمرير props.json الخاصة بكل قصّة وقت التصيير.",
              visual: "images/hekaya/_preview/chapter_3.jpg",
              visualType: "image",
            },
          ],
          epilogue: {
            arabicReflection:
              "في النهاية، نحمل الحكاية كما يُحمل حجر مصقول من نهر قديم — في الجيب، صامتاً، يُذكّرنا بأن الزمن مرّ، وأنّ بعض الأشياء بقيت.",
            arabicSignature: "حكاية · هكذا تُروى",
          },
          sources: [
            { name: "Photonect", domain: "photonect.net" },
          ],
        }}
      />
    </>
  );
};
