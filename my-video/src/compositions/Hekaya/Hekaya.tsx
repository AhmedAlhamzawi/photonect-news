import React from "react";
import {
  AbsoluteFill,
  Audio,
  interpolate,
  useCurrentFrame,
  Easing,
  staticFile,
  Img,
} from "remotion";
import { TransitionSeries, linearTiming } from "@remotion/transitions";
import { fade } from "@remotion/transitions/fade";
import {
  HekayaProps,
  HekayaChapterProps,
  HEKAYA_PROLOGUE_FRAMES,
  HEKAYA_CHAPTER1_FRAMES,
  HEKAYA_CHAPTER2_FRAMES,
  HEKAYA_CHAPTER3_FRAMES,
  HEKAYA_EPILOGUE_FRAMES,
  computeHekayaDurationInFrames,
  HEKAYA_PALETTE,
} from "./schema";

// ─── Slow Ken-Burns wash. Hekaya's signature image treatment. ─────────────
// Image holds for the chapter, gently zooming in or out (alternating per
// chapter). NewsReel uses pulse + scan beam — Hekaya uses calm breath.
const KenBurns: React.FC<{
  src: string;
  durationFrames: number;
  direction?: "in" | "out" | "left" | "right";
}> = ({ src, durationFrames, direction = "in" }) => {
  const frame = useCurrentFrame();
  const progress = interpolate(frame, [0, durationFrames], [0, 1], {
    extrapolateRight: "clamp",
  });

  let scale = 1;
  let translateX = 0;
  let translateY = 0;

  if (direction === "in") {
    scale = interpolate(progress, [0, 1], [1.0, 1.12], {
      easing: Easing.bezier(0.25, 0, 0.25, 1),
    });
  } else if (direction === "out") {
    scale = interpolate(progress, [0, 1], [1.18, 1.02], {
      easing: Easing.bezier(0.25, 0, 0.25, 1),
    });
  } else if (direction === "left") {
    scale = 1.12;
    translateX = interpolate(progress, [0, 1], [-3, 3]);
  } else {
    scale = 1.12;
    translateX = interpolate(progress, [0, 1], [3, -3]);
  }

  return (
    <AbsoluteFill style={{ overflow: "hidden", backgroundColor: HEKAYA_PALETTE.shadow }}>
      <Img
        src={src.startsWith("http") ? src : staticFile(src)}
        style={{
          width: "100%",
          height: "100%",
          objectFit: "cover",
          transform: `scale(${scale}) translate(${translateX}%, ${translateY}%)`,
        }}
      />
      {/* Vignette + warm overlay — pulls the photo into Hekaya's palette. */}
      <AbsoluteFill
        style={{
          background: `radial-gradient(ellipse at center,
            transparent 30%,
            ${HEKAYA_PALETTE.ink}99 75%,
            ${HEKAYA_PALETTE.ink} 100%)`,
        }}
      />
      <AbsoluteFill
        style={{
          background: `linear-gradient(180deg,
            ${HEKAYA_PALETTE.ink}40 0%,
            transparent 40%,
            transparent 60%,
            ${HEKAYA_PALETTE.ink}cc 100%)`,
        }}
      />
    </AbsoluteFill>
  );
};

// ─── Soft floating gold flecks. Replaces NewsReel's DotGrid + ScanBeam.  ──
// Subtle. Like dust in a sunbeam. Adds life without urgency.
const Embers: React.FC = () => {
  const frame = useCurrentFrame();
  const dots = Array.from({ length: 22 }, (_, i) => i);
  return (
    <AbsoluteFill style={{ pointerEvents: "none" }}>
      {dots.map((i) => {
        const seed = (i * 37) % 100;
        const x = (seed * 13) % 1080;
        const y = ((seed * 47) % 1920);
        const driftY = interpolate(frame, [0, 600], [0, -120 - (seed % 40)]);
        const opacity = interpolate(
          frame,
          [0, 60, 540, 600],
          [0, 0.45 + (seed % 30) / 200, 0.45 + (seed % 30) / 200, 0],
          { extrapolateRight: "extend" },
        );
        return (
          <div
            key={i}
            style={{
              position: "absolute",
              left: x,
              top: y + driftY,
              width: 3 + (seed % 3),
              height: 3 + (seed % 3),
              borderRadius: "50%",
              background: HEKAYA_PALETTE.gold,
              boxShadow: `0 0 8px ${HEKAYA_PALETTE.gold}`,
              opacity,
            }}
          />
        );
      })}
    </AbsoluteFill>
  );
};

// ─── Calligraphic divider — a thin gold line with a center diamond. ───────
// Used between scenes and as a header ornament. Replaces newsroom's bars.
const Divider: React.FC<{ width?: number }> = ({ width = 360 }) => (
  <div
    style={{
      width,
      height: 14,
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
      gap: 8,
    }}
  >
    <div style={{ flex: 1, height: 1, background: HEKAYA_PALETTE.gold }} />
    <div
      style={{
        width: 8,
        height: 8,
        background: HEKAYA_PALETTE.gold,
        transform: "rotate(45deg)",
      }}
    />
    <div style={{ flex: 1, height: 1, background: HEKAYA_PALETTE.gold }} />
  </div>
);

// ─── PROLOGUE — title card with era stamp + sensory hook line. ────────────
const Prologue: React.FC<HekayaProps["prologue"]> = ({
  arabicTitle,
  englishSubtitle,
  era,
  place,
  arabicHook,
  heroMedia,
}) => {
  const frame = useCurrentFrame();
  const heroFade = interpolate(frame, [0, 30, HEKAYA_PROLOGUE_FRAMES - 30, HEKAYA_PROLOGUE_FRAMES], [0, 1, 1, 0.5], {
    extrapolateRight: "clamp",
  });
  const titleY = interpolate(frame, [0, 50], [40, 0], {
    easing: Easing.bezier(0.16, 1, 0.3, 1),
    extrapolateRight: "clamp",
  });
  const titleOpacity = interpolate(frame, [10, 60], [0, 1], { extrapolateRight: "clamp" });
  const hookOpacity = interpolate(frame, [120, 180], [0, 1], { extrapolateRight: "clamp" });

  return (
    <AbsoluteFill style={{ backgroundColor: HEKAYA_PALETTE.ink }}>
      <div style={{ opacity: heroFade, width: "100%", height: "100%", position: "absolute" }}>
        <KenBurns src={heroMedia} durationFrames={HEKAYA_PROLOGUE_FRAMES} direction="in" />
      </div>
      <Embers />

      {/* Era + place stamp — top of frame, slim caps. */}
      <div
        style={{
          position: "absolute",
          top: 200,
          left: 0,
          right: 0,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          gap: 14,
          opacity: titleOpacity,
        }}
      >
        <div
          style={{
            color: HEKAYA_PALETTE.gold,
            fontFamily: "system-ui, -apple-system, sans-serif",
            fontSize: 26,
            letterSpacing: 8,
            fontWeight: 500,
            textTransform: "uppercase",
          }}
        >
          {era}
        </div>
        <Divider width={220} />
        <div
          style={{
            color: HEKAYA_PALETTE.ivory,
            fontFamily: "system-ui, -apple-system, sans-serif",
            fontSize: 22,
            letterSpacing: 5,
            opacity: 0.78,
            textTransform: "uppercase",
          }}
        >
          {place}
        </div>
      </div>

      {/* Arabic title — middle of frame, large, lyrical. */}
      <div
        style={{
          position: "absolute",
          top: "38%",
          left: 80,
          right: 80,
          textAlign: "center",
          transform: `translateY(${titleY}px)`,
          opacity: titleOpacity,
        }}
      >
        <div
          dir="rtl"
          style={{
            color: HEKAYA_PALETTE.ivory,
            fontFamily: "Cairo, system-ui, sans-serif",
            fontSize: 96,
            fontWeight: 800,
            lineHeight: 1.18,
            letterSpacing: 0,
            textShadow: `0 4px 24px ${HEKAYA_PALETTE.shadow}cc`,
          }}
        >
          {arabicTitle}
        </div>
        <div
          style={{
            color: HEKAYA_PALETTE.gold,
            fontFamily: "system-ui, -apple-system, sans-serif",
            fontSize: 24,
            letterSpacing: 4,
            marginTop: 24,
            fontStyle: "italic",
            fontWeight: 400,
            opacity: 0.85,
          }}
        >
          {englishSubtitle}
        </div>
      </div>

      {/* Sensory hook — bottom of frame, smaller, slow fade-in. */}
      <div
        style={{
          position: "absolute",
          bottom: 380,
          left: 90,
          right: 90,
          opacity: hookOpacity,
          textAlign: "center",
        }}
      >
        <Divider width={120} />
        <div
          dir="rtl"
          style={{
            color: HEKAYA_PALETTE.vellum,
            fontFamily: "Cairo, system-ui, sans-serif",
            fontSize: 38,
            fontWeight: 500,
            lineHeight: 1.55,
            marginTop: 32,
            textShadow: `0 2px 12px ${HEKAYA_PALETTE.shadow}`,
          }}
        >
          {arabicHook}
        </div>
      </div>
    </AbsoluteFill>
  );
};

// ─── CHAPTER scene — image + narration card + optional anchor fact. ───────
const Chapter: React.FC<{
  chapter: HekayaChapterProps;
  index: number;
  durationFrames: number;
}> = ({ chapter, index, durationFrames }) => {
  const frame = useCurrentFrame();
  const accent = chapter.accent ?? HEKAYA_PALETTE.gold;

  // Direction alternates: in / out / left so the eye keeps moving subtly.
  const directions: Array<"in" | "out" | "left" | "right"> = ["in", "out", "left"];

  const headingOpacity = interpolate(frame, [10, 70], [0, 1], { extrapolateRight: "clamp" });
  const headingY = interpolate(frame, [0, 60], [30, 0], {
    easing: Easing.bezier(0.16, 1, 0.3, 1),
    extrapolateRight: "clamp",
  });
  const bodyOpacity = interpolate(frame, [60, 140], [0, 1], { extrapolateRight: "clamp" });
  const bodyY = interpolate(frame, [60, 140], [20, 0], {
    easing: Easing.bezier(0.25, 0.46, 0.45, 0.94),
    extrapolateRight: "clamp",
  });
  const factOpacity = interpolate(
    frame,
    [180, 240, durationFrames - 60, durationFrames - 30],
    [0, 1, 1, 0],
    { extrapolateRight: "clamp" },
  );

  return (
    <AbsoluteFill style={{ backgroundColor: HEKAYA_PALETTE.ink }}>
      <KenBurns src={chapter.visual} durationFrames={durationFrames} direction={directions[index % 3]} />
      <Embers />

      {/* Chapter index marker — small, top-right. */}
      <div
        style={{
          position: "absolute",
          top: 220,
          right: 80,
          color: accent,
          fontFamily: "system-ui, -apple-system, sans-serif",
          fontSize: 22,
          letterSpacing: 6,
          fontWeight: 500,
          opacity: 0.8,
        }}
      >
        {`الفصل · ${["الأول", "الثاني", "الثالث"][index] ?? ""}`}
      </div>

      {/* Chapter title — big, fades in. */}
      <div
        style={{
          position: "absolute",
          top: 290,
          left: 80,
          right: 80,
          opacity: headingOpacity,
          transform: `translateY(${headingY}px)`,
        }}
      >
        <div
          dir="rtl"
          style={{
            color: HEKAYA_PALETTE.ivory,
            fontFamily: "Cairo, system-ui, sans-serif",
            fontSize: 76,
            fontWeight: 800,
            lineHeight: 1.2,
            textAlign: "center",
            textShadow: `0 4px 20px ${HEKAYA_PALETTE.shadow}`,
          }}
        >
          {chapter.arabicTitle}
        </div>
        <div style={{ marginTop: 24, display: "flex", justifyContent: "center" }}>
          <Divider width={260} />
        </div>
      </div>

      {/* Narration card — vellum-tinted background, soft. */}
      <div
        style={{
          position: "absolute",
          bottom: 360,
          left: 70,
          right: 70,
          opacity: bodyOpacity,
          transform: `translateY(${bodyY}px)`,
          padding: "44px 50px",
          background: `${HEKAYA_PALETTE.shadow}cc`,
          borderTop: `1px solid ${accent}66`,
          borderBottom: `1px solid ${accent}66`,
          backdropFilter: "blur(8px)",
        }}
      >
        <div
          dir="rtl"
          style={{
            color: HEKAYA_PALETTE.vellum,
            fontFamily: "Cairo, system-ui, sans-serif",
            fontSize: 32,
            fontWeight: 500,
            lineHeight: 1.7,
            textAlign: "right",
          }}
        >
          {chapter.arabicNarration}
        </div>
      </div>

      {/* Optional anchor fact — slim card, top-left, slow fade. */}
      {chapter.anchorFact ? (
        <div
          style={{
            position: "absolute",
            bottom: 200,
            left: 70,
            opacity: factOpacity,
            display: "flex",
            alignItems: "center",
            gap: 18,
            padding: "16px 24px",
            background: `${HEKAYA_PALETTE.ink}dd`,
            border: `1px solid ${accent}99`,
            borderRadius: 4,
          }}
        >
          <div
            style={{
              color: accent,
              fontFamily: "system-ui, -apple-system, sans-serif",
              fontSize: 36,
              fontWeight: 700,
              letterSpacing: 1,
            }}
          >
            {chapter.anchorFact.value}
          </div>
          <div
            dir="rtl"
            style={{
              color: HEKAYA_PALETTE.vellum,
              fontFamily: "Cairo, system-ui, sans-serif",
              fontSize: 20,
              fontWeight: 500,
              opacity: 0.88,
            }}
          >
            {chapter.anchorFact.label}
          </div>
        </div>
      ) : null}

      {/* Optional Latin caption — sliding in from right edge. */}
      {chapter.latinCaption ? (
        <div
          style={{
            position: "absolute",
            bottom: 130,
            right: 70,
            color: HEKAYA_PALETTE.gold,
            fontFamily: "system-ui, -apple-system, sans-serif",
            fontSize: 18,
            letterSpacing: 3,
            fontStyle: "italic",
            fontWeight: 400,
            opacity: factOpacity,
            textTransform: "uppercase",
          }}
        >
          {chapter.latinCaption}
        </div>
      ) : null}
    </AbsoluteFill>
  );
};

// ─── EPILOGUE — closing reflection over a still or a calligraphic motif. ──
const Epilogue: React.FC<{
  epilogue: HekayaProps["epilogue"];
  handle: string;
  sources: HekayaProps["sources"];
}> = ({ epilogue, handle, sources }) => {
  const frame = useCurrentFrame();
  const reflectionOpacity = interpolate(frame, [10, 70], [0, 1], { extrapolateRight: "clamp" });
  const reflectionY = interpolate(frame, [0, 70], [24, 0], {
    easing: Easing.bezier(0.16, 1, 0.3, 1),
    extrapolateRight: "clamp",
  });
  const sigOpacity = interpolate(
    frame,
    [80, 150, HEKAYA_EPILOGUE_FRAMES - 50, HEKAYA_EPILOGUE_FRAMES],
    [0, 1, 1, 0],
    { extrapolateRight: "clamp" },
  );

  const closing = epilogue.closingMedia;

  return (
    <AbsoluteFill
      style={{
        backgroundColor: HEKAYA_PALETTE.ink,
      }}
    >
      {closing ? (
        <KenBurns src={closing} durationFrames={HEKAYA_EPILOGUE_FRAMES} direction="out" />
      ) : (
        // No image? Use a quiet radial gradient as the final canvas.
        <AbsoluteFill
          style={{
            background: `radial-gradient(ellipse at center,
              ${HEKAYA_PALETTE.shadow}, ${HEKAYA_PALETTE.ink} 80%)`,
          }}
        />
      )}
      <Embers />

      <div
        style={{
          position: "absolute",
          top: "30%",
          left: 80,
          right: 80,
          textAlign: "center",
          opacity: reflectionOpacity,
          transform: `translateY(${reflectionY}px)`,
        }}
      >
        <Divider width={180} />
        <div
          dir="rtl"
          style={{
            color: HEKAYA_PALETTE.ivory,
            fontFamily: "Cairo, system-ui, sans-serif",
            fontSize: 38,
            fontWeight: 500,
            lineHeight: 1.7,
            marginTop: 36,
            textShadow: `0 2px 12px ${HEKAYA_PALETTE.shadow}`,
          }}
        >
          {epilogue.arabicReflection}
        </div>
        {epilogue.arabicSignature ? (
          <div
            dir="rtl"
            style={{
              color: HEKAYA_PALETTE.gold,
              fontFamily: "Cairo, system-ui, sans-serif",
              fontSize: 30,
              fontWeight: 600,
              lineHeight: 1.4,
              marginTop: 36,
              fontStyle: "italic",
              opacity: sigOpacity,
            }}
          >
            {epilogue.arabicSignature}
          </div>
        ) : null}
      </div>

      {/* Handle + sources strip at the bottom. */}
      <div
        style={{
          position: "absolute",
          bottom: 200,
          left: 0,
          right: 0,
          textAlign: "center",
          opacity: sigOpacity,
        }}
      >
        <div style={{ display: "flex", justifyContent: "center", marginBottom: 18 }}>
          <Divider width={120} />
        </div>
        <div
          style={{
            color: HEKAYA_PALETTE.ivory,
            fontFamily: "system-ui, -apple-system, sans-serif",
            fontSize: 26,
            letterSpacing: 4,
            fontWeight: 500,
            opacity: 0.92,
          }}
        >
          {handle}
        </div>
        <div
          style={{
            color: HEKAYA_PALETTE.gold,
            fontFamily: "system-ui, -apple-system, sans-serif",
            fontSize: 14,
            letterSpacing: 3,
            marginTop: 16,
            opacity: 0.6,
            textTransform: "uppercase",
          }}
        >
          {sources
            .slice(0, 4)
            .map((s) => s.name)
            .join(" · ")}
        </div>
      </div>
    </AbsoluteFill>
  );
};

// ═══════════════════════════════════════════════════════════════════════
// THE COMPOSITION
// ═══════════════════════════════════════════════════════════════════════
export const Hekaya: React.FC<HekayaProps> = ({
  dateLabel,
  arabicDateLabel,
  handle,
  audioBed,
  prologue,
  chapters,
  epilogue,
  sources,
}) => {
  const frame = useCurrentFrame();
  const totalFrames = computeHekayaDurationInFrames();
  const CHAPTER_DURATIONS = [HEKAYA_CHAPTER1_FRAMES, HEKAYA_CHAPTER2_FRAMES, HEKAYA_CHAPTER3_FRAMES];

  // Audio: fade in over 60 frames, sustain low (0.42 — gentler than news 0.45),
  // fade out over 75 frames so the last word can sit in silence.
  const audioVolume = interpolate(
    frame,
    [0, 60, totalFrames - 75, totalFrames - 5],
    [0, 0.42, 0.42, 0],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
  );

  const audioSrc = audioBed.startsWith("http") ? audioBed : staticFile(audioBed);

  return (
    <AbsoluteFill style={{ background: HEKAYA_PALETTE.ink }}>
      <Audio src={audioSrc} volume={audioVolume} />

      <TransitionSeries>
        <TransitionSeries.Sequence durationInFrames={HEKAYA_PROLOGUE_FRAMES}>
          <Prologue {...prologue} />
        </TransitionSeries.Sequence>

        <TransitionSeries.Transition
          presentation={fade()}
          timing={linearTiming({ durationInFrames: 24 })}
        />

        {chapters.map((chapter, i) => (
          <React.Fragment key={i}>
            <TransitionSeries.Sequence durationInFrames={CHAPTER_DURATIONS[i]}>
              <Chapter chapter={chapter} index={i} durationFrames={CHAPTER_DURATIONS[i]} />
            </TransitionSeries.Sequence>
            <TransitionSeries.Transition
              presentation={fade()}
              timing={linearTiming({ durationInFrames: 24 })}
            />
          </React.Fragment>
        ))}

        <TransitionSeries.Sequence durationInFrames={HEKAYA_EPILOGUE_FRAMES}>
          <Epilogue epilogue={epilogue} handle={handle} sources={sources} />
        </TransitionSeries.Sequence>
      </TransitionSeries>

      {/* Date stamp — bottom-left, persistent. Hekaya's only chrome. */}
      <div
        style={{
          position: "absolute",
          bottom: 70,
          left: 50,
          color: HEKAYA_PALETTE.ivory,
          fontFamily: "system-ui, -apple-system, sans-serif",
          fontSize: 16,
          letterSpacing: 4,
          fontWeight: 500,
          opacity: 0.55,
          textTransform: "uppercase",
        }}
      >
        {dateLabel}
      </div>
      <div
        dir="rtl"
        style={{
          position: "absolute",
          bottom: 70,
          right: 50,
          color: HEKAYA_PALETTE.ivory,
          fontFamily: "Cairo, system-ui, sans-serif",
          fontSize: 18,
          fontWeight: 500,
          opacity: 0.55,
        }}
      >
        {arabicDateLabel}
      </div>
    </AbsoluteFill>
  );
};
