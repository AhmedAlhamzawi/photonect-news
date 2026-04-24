import React from "react";
import { AbsoluteFill, Audio, interpolate, useCurrentFrame, Easing, staticFile } from "remotion";
import { TransitionSeries, linearTiming } from "@remotion/transitions";
import { fade } from "@remotion/transitions/fade";
import {
  NewsReelProps,
  BREAKING_FRAMES,
  BEAT_FRAMES,
  BEAT3_FRAMES,
  SOURCES_FRAMES,
  computeNewsReelDurationInFrames,
  resolveVariant,
} from "./schema";
import { PHOTONECT } from "../PhotonectBrandReel/brand";
import { GrainOverlay, Vignette } from "../PhotonectBrandReel/GrainOverlay";
import { DotGrid, ScanBeam, TopStrip } from "../AINewsDaily/MotionLayers";
import { Breaking } from "./scenes/Breaking";
import { Beat } from "./scenes/Beat";
import { Sources } from "./scenes/Sources";

const BackgroundPulse: React.FC = () => {
  const frame = useCurrentFrame();
  const cx = interpolate(frame, [0, 900], [40, 60], {
    easing: Easing.bezier(0.45, 0, 0.55, 1),
  });
  const cy = interpolate(frame, [0, 900], [35, 65], {
    easing: Easing.bezier(0.45, 0, 0.55, 1),
  });
  return (
    <AbsoluteFill
      style={{
        background: `radial-gradient(ellipse at ${cx}% ${cy}%, ${PHOTONECT.signal}14 0%, ${PHOTONECT.ink} 65%)`,
      }}
    />
  );
};

// V6 rev2 (2026-04-22 23:48) — rebuilt all 12 beds as lavfi-synthesized
// compositions with distinct musical character after Ahmed's 22 Apr rejection:
// "the music you did not change it, it is the same" / "one has a new music
// and it's bullshit". The previous V6 beds had size collisions, low loudness
// (bed_ambient_syn at −33.7 dB mean), and perceptually-identical drones.
// Rebuilt via automation/scripts/make-v6-beds.py:
//   - distinct key per bed (D-/G/Am/Em/C/Fm/Bm/Gm/Dm/Am-slow/Fm/Em)
//   - BPM range 50–130, distinct rhythmic feel per bed
//   - layered: sub-bass + triad + rhythmic pulse + melodic stinger + noise pad
//   - loudness-normalized to −16 LUFS / −1 dBFS peak (broadcast-ready)
//
// Bucket → default music bed. V6 uses 7 distinct defaults so adjacent buckets
// in the rotation never collide even before per-slug audioBed overrides.
const BUCKET_BED: Record<string, string> = {
  mena_geopolitics: "audio/bed_pressure.mp3",     // tense, urgent
  iraq_domestic:    "audio/bed_anchor.mp3",       // default news feel
  gulf_regional:    "audio/bed_echo.mp3",         // spacious, regional
  europe:           "audio/bed_ambient_syn.mp3",  // cinematic pad
  global_economy:   "audio/bed_voltage.mp3",      // electric, markets
  tech_ai:          "audio/bed_cycle.mp3",        // patrol sweep, AI
  wildcard:         "audio/bed_tide.mp3",         // backwards, atmospheric
};

// V6 rev2: 12 musically distinct lavfi-synthesized beds, −16 LUFS normalized.
const AVAILABLE_BEDS = new Set<string>([
  "audio/news_bed.mp3",                    // legacy master (kept for back-compat)
  "audio/bed_anchor.mp3",                  // G major, 90 BPM — anchor-news feel
  "audio/bed_pressure.mp3",                // D minor, 56 BPM — dark throbbing tension
  "audio/bed_weight.mp3",                  // F minor, 60 BPM — oppressive low drone
  "audio/bed_velocity.mp3",                // G minor, 130 BPM — driving rhythmic
  "audio/bed_echo.mp3",                    // C major, 70 BPM — reverberant, diplomatic
  "audio/bed_tide.mp3",                    // A minor, 50 BPM — ocean swell, majestic
  "audio/bed_voltage.mp3",                 // A minor, 120 BPM — electric pulsing
  "audio/bed_fog.mp3",                     // B minor, 55 BPM — foggy lowpass, clandestine
  "audio/bed_steel.mp3",                   // E minor, 85 BPM — metallic, aecho bells
  "audio/bed_pulse_syn.mp3",               // D minor, 108 BPM — square-wave harmonic stack
  "audio/bed_cycle.mp3",                   // E minor, 100 BPM — 4-note arpeggio
  "audio/bed_ambient_syn.mp3",             // F minor, 65 BPM — atmospheric synth pad
]);

// Bucket → default accent color. Gives each topic bucket a distinct visual
// signature without requiring props.json to specify an accent per beat.
// Resolution order per beat: explicit beat.accent → bucket default → PHOTONECT.signal
// This is additive: every existing props.json keeps rendering identically
// unless it opts in by setting `topicBucket`.
const BUCKET_ACCENTS: Record<string, string> = {
  mena_geopolitics: PHOTONECT.signal,  // brand red — hot conflict coverage
  iraq_domestic:    "#FFC217",         // brand yellow — domestic politics
  gulf_regional:    "#00E5A0",         // emerald — markets/gulf
  europe:           "#5B8FF9",         // cool blue — european files
  global_economy:   "#FFB020",         // amber — macro/oil/rates
  tech_ai:          "#C084FC",         // violet — tech / AI
  wildcard:         PHOTONECT.signal,  // fall through to brand
};

const pickAccent = (
  explicit: string | undefined,
  bucket: string | undefined,
): string | undefined => {
  if (explicit) return explicit;
  if (bucket && BUCKET_ACCENTS[bucket]) return BUCKET_ACCENTS[bucket];
  return undefined;  // let Beat fall back to PHOTONECT.signal
};

const pickAudioBed = (
  explicit: string | undefined,
  bucket: string | undefined,
): string => {
  // 1. Explicit prop wins (lets a slug override bucket default)
  if (explicit) {
    if (explicit.startsWith("http")) return explicit;
    if (AVAILABLE_BEDS.has(explicit)) return explicit;
  }
  // 2. Bucket default, if the file actually exists on disk
  if (bucket && BUCKET_BED[bucket] && AVAILABLE_BEDS.has(BUCKET_BED[bucket])) {
    return BUCKET_BED[bucket];
  }
  // 3. Safe fallback — anchor bed is loudnorm'd to -16 LUFS and always in AVAILABLE_BEDS
  return "audio/bed_anchor.mp3";
};

export const NewsReel: React.FC<NewsReelProps> = ({
  dateLabel,
  arabicDateLabel,
  handle,
  audioBed,
  variant,
  topicBucket,
  breaking,
  beats,
  sources,
  arabicTicker,
}) => {
  const BEAT_DURATIONS = [BEAT_FRAMES, BEAT_FRAMES, BEAT3_FRAMES];
  const frame = useCurrentFrame();
  const totalFrames = computeNewsReelDurationInFrames();
  const activeVariant = resolveVariant(variant, topicBucket);

  const audioVolume = interpolate(
    frame,
    [0, 15, totalFrames - 45, totalFrames - 5],
    [0, 0.45, 0.45, 0],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
  );

  const bedPath = pickAudioBed(audioBed, topicBucket);
  const audioSrc = bedPath.startsWith("http") ? bedPath : staticFile(bedPath);

  return (
    <AbsoluteFill style={{ background: PHOTONECT.ink }}>
      <Audio src={audioSrc} volume={audioVolume} />

      <BackgroundPulse />
      <DotGrid />
      <ScanBeam />

      <TransitionSeries>
        <TransitionSeries.Sequence durationInFrames={BREAKING_FRAMES}>
          <Breaking
            arabicKicker={breaking.arabicKicker}
            arabicHeadline={breaking.arabicHeadline}
            englishSubhead={breaking.englishSubhead}
            heroMedia={breaking.heroMedia}
            heroMediaType={breaking.heroMediaType}
          />
        </TransitionSeries.Sequence>

        <TransitionSeries.Transition
          presentation={fade()}
          timing={linearTiming({ durationInFrames: 12 })}
        />

        {beats.map((beat, i) => (
          <React.Fragment key={i}>
            <TransitionSeries.Sequence durationInFrames={BEAT_DURATIONS[i]}>
              <Beat
                {...beat}
                accent={pickAccent(beat.accent, topicBucket)}
                index={i + 1}
                durationFrames={BEAT_DURATIONS[i]}
                variant={activeVariant}
              />
            </TransitionSeries.Sequence>
            <TransitionSeries.Transition
              presentation={fade()}
              timing={linearTiming({ durationInFrames: 12 })}
            />
          </React.Fragment>
        ))}

        <TransitionSeries.Sequence durationInFrames={SOURCES_FRAMES}>
          <Sources sources={sources} handle={handle} />
        </TransitionSeries.Sequence>
      </TransitionSeries>

      {/* Persistent UI chrome — sits inside platform-safe zone.
          BottomTicker removed: IG/TikTok occlude the bottom ~400px with
          caption/music chrome, so any ticker there is 100% invisible. */}
      <TopStrip dateLabel={dateLabel} arabicDateLabel={arabicDateLabel} showName="WORLD NEWS" />

      {/* Texture */}
      <Vignette strength={0.55} />
      <GrainOverlay opacity={0.08} seed={17} />
    </AbsoluteFill>
  );
};
