import React from "react";
import { AbsoluteFill, Series, interpolate, useCurrentFrame, Easing } from "remotion";
import { BrandReelProps } from "./schema";
import { SceneLogo } from "./scenes/SceneLogo";
import { SceneTagline } from "./scenes/SceneTagline";
import { SceneBenefit } from "./scenes/SceneBenefit";
import { SceneCTA } from "./scenes/SceneCTA";
import { GrainOverlay, Vignette } from "./GrainOverlay";

// 15s @ 30fps = 450 frames split:
// Logo 75 | Tagline 60 | B1 75 | B2 75 | B3 75 | CTA 90 = 450
const SCENE_DURATIONS = [75, 60, 75, 75, 75, 90];

// Subtle animated background — radial gradient that drifts
const BackgroundGradient: React.FC<{ ink: string; accent: string }> = ({ ink, accent }) => {
  const frame = useCurrentFrame();
  // Very slow drift across the full composition
  const cx = interpolate(frame, [0, 450], [40, 60], {
    easing: Easing.bezier(0.45, 0, 0.55, 1),
  });
  const cy = interpolate(frame, [0, 450], [35, 55], {
    easing: Easing.bezier(0.45, 0, 0.55, 1),
  });
  return (
    <AbsoluteFill
      style={{
        background: `radial-gradient(ellipse at ${cx}% ${cy}%, ${accent}22 0%, ${ink} 55%)`,
      }}
    />
  );
};

export const PhotonectBrandReel: React.FC<BrandReelProps> = (props) => {
  const { brandName, background, paper, primary, accent, taglineLatin, taglineArabic, benefits, cta } = props;

  return (
    <AbsoluteFill style={{ background }}>
      <BackgroundGradient ink={background} accent={accent} />

      <Series>
        <Series.Sequence durationInFrames={SCENE_DURATIONS[0]}>
          <SceneLogo
            brandName={brandName}
            primary={primary}
            accent={accent}
            paper={paper}
          />
        </Series.Sequence>

        <Series.Sequence durationInFrames={SCENE_DURATIONS[1]}>
          <SceneTagline latin={taglineLatin} arabic={taglineArabic} paper={paper} accent={accent} />
        </Series.Sequence>

        <Series.Sequence durationInFrames={SCENE_DURATIONS[2]}>
          <SceneBenefit
            index={1}
            headline={benefits[0].headline}
            body={benefits[0].body}
            paper={paper}
            accent={accent}
            ink={background}
          />
        </Series.Sequence>

        <Series.Sequence durationInFrames={SCENE_DURATIONS[3]}>
          <SceneBenefit
            index={2}
            headline={benefits[1].headline}
            body={benefits[1].body}
            paper={paper}
            accent={accent}
            ink={background}
          />
        </Series.Sequence>

        <Series.Sequence durationInFrames={SCENE_DURATIONS[4]}>
          <SceneBenefit
            index={3}
            headline={benefits[2].headline}
            body={benefits[2].body}
            paper={paper}
            accent={accent}
            ink={background}
          />
        </Series.Sequence>

        <Series.Sequence durationInFrames={SCENE_DURATIONS[5]}>
          <SceneCTA
            brandName={brandName}
            ctaText={cta.text}
            ctaUrl={cta.url}
            paper={paper}
            accent={accent}
            primary={primary}
          />
        </Series.Sequence>
      </Series>

      {/* Texture pass */}
      <Vignette strength={0.4} />
      <GrainOverlay opacity={0.07} seed={42} />
    </AbsoluteFill>
  );
};
