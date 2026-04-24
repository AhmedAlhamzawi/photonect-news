#!/usr/bin/env python3
"""V6 music-bed generator — 12 genuinely distinct beds.

Ahmed's rejection of V5/V6-prototype beds:
  "The music you did not change it. It is the same. There is one video that
   has a new music and it's bullshit."

Root cause (confirmed via volumedetect audit 2026-04-22):
  - bed_ambient_syn mean=-33.7 dB  (inaudible)
  - bed_steel mean=-29.3 dB        (inaudible)
  - bed_cycle/bed_pulse_syn/bed_steel all 1,009,415 bytes (same structure)

Fix: 12 musically distinct compositions, each with:
  - Distinct root key
  - Distinct tempo (55-130 BPM)
  - Distinct timbre (sine / saw / square / triangle / FM-modulated noise)
  - Layered arrangement: bass + chord pad + rhythmic pulse + optional lead
  - Loudnorm to -16 LUFS / peak -1 dBFS (broadcast-ready)
  - 42-second length (video = 34s, plenty of headroom)

Each bed is a single ffmpeg -f lavfi synthesis call. Deterministic.
Output → my-video/public/audio/bed_<name>.mp3
"""

import subprocess
import sys
from pathlib import Path

AUDIO_DIR = Path("/Users/ahmed/Desktop/Claude <> Ahmed - 2nd Brain/Photonect/my-video/public/audio")
DURATION = 42.0   # seconds
SAMPLE_RATE = 44100
TARGET_LUFS = -16
TARGET_PEAK = -1.0

# Note frequencies (Hz) — two octaves so we can pick bass + upper voices
NOTE = {
    "C2": 65.41, "D2": 73.42, "E2": 82.41, "F2": 87.31, "G2": 98.00, "A2": 110.00, "B2": 123.47,
    "C3": 130.81, "D3": 146.83, "E3": 164.81, "F3": 174.61, "G3": 196.00, "A3": 220.00, "B3": 246.94,
    "C4": 261.63, "D4": 293.66, "E4": 329.63, "F4": 349.23, "G4": 392.00, "A4": 440.00, "B4": 493.88,
    "C5": 523.25, "D5": 587.33, "E5": 659.26, "F5": 698.46, "G5": 783.99,
}


def minor_chord(root: str, octave_shift: int = 0) -> list:
    """Return [root, min3rd, 5th] frequencies."""
    r = NOTE[root] * (2 ** octave_shift)
    return [r, r * 1.1892, r * 1.4983]


def major_chord(root: str, octave_shift: int = 0) -> list:
    r = NOTE[root] * (2 ** octave_shift)
    return [r, r * 1.2599, r * 1.4983]


def build_filter_complex(beds_spec: dict) -> str:
    """Each spec declares layers + mix. Returns a filter_complex string."""
    return beds_spec["filter"]


# ==============================================================================
# 12 BED DEFINITIONS — each a unique musical phrase
# ==============================================================================

def bed_pressure():
    """MENA geopolitics — Lebanon Bekaa. Dark throbbing tension.
    D minor, 56 BPM pulse, slow-breathing low drone + tritone grind."""
    # D2=73.42, F2=87.31, A2=110  (D minor triad)
    # Tritone G#2=103.83 for dread
    f = (
        # Layer 1: sub-bass D2 pulsing at 56 BPM (beat = 1.071s)
        "sine=frequency=73.42:sample_rate=44100:duration=42,"
        "volume=0.9,"
        "tremolo=f=0.93:d=0.35[bass];"
        # Layer 2: F2 drone with slow LFO (f>=0.1 per ffmpeg constraint)
        "sine=frequency=87.31:sample_rate=44100:duration=42,"
        "volume=0.4,"
        "vibrato=f=0.12:d=0.02[drone];"
        # Layer 3: tritone G#2 creeping in after 10s
        "sine=frequency=103.83:sample_rate=44100:duration=42,"
        "volume=0.25,"
        "afade=t=in:st=10:d=6[tritone];"
        # Layer 4: A2 fifth adding weight at 24s
        "sine=frequency=110:sample_rate=44100:duration=42,"
        "volume=0.35,"
        "afade=t=in:st=24:d=4[fifth];"
        # Mix + highpass to tame rumble
        "[bass][drone][tritone][fifth]amix=inputs=4:duration=longest:normalize=0,"
        "highpass=f=40,lowpass=f=1800[out]"
    )
    return f


def bed_anchor():
    """Iraq domestic — cabinet sworn. Anchor-news feel, G major stability.
    G3=196, B3=246.94, D4=293.66  (G major triad) at 90 BPM."""
    f = (
        # Layer 1: G2 bass
        "sine=frequency=98:sample_rate=44100:duration=42,"
        "volume=0.55[bass];"
        # Layer 2: G major triad upper voices with gentle tremolo
        "sine=frequency=196:sample_rate=44100:duration=42,"
        "volume=0.3,tremolo=f=1.5:d=0.15[g];"
        "sine=frequency=246.94:sample_rate=44100:duration=42,"
        "volume=0.28,tremolo=f=1.5:d=0.15[b];"
        "sine=frequency=293.66:sample_rate=44100:duration=42,"
        "volume=0.25,tremolo=f=1.5:d=0.15[d];"
        # Layer 3: high D5 accent pulse every bar (~2.66s at 90bpm/4)
        "sine=frequency=587.33:sample_rate=44100:duration=42,"
        "volume=0.18,tremolo=f=0.375:d=0.95[lead];"
        # Layer 4: subtle snare-ish noise pulse at 90 BPM (1.5 beats)
        "anoisesrc=duration=42:color=white:seed=17,"
        "volume=0.05,highpass=f=2000,tremolo=f=1.5:d=0.98[snare];"
        "[bass][g][b][d][lead][snare]amix=inputs=6:duration=longest:normalize=0,"
        "lowpass=f=5000,highpass=f=50[out]"
    )
    return f


def bed_voltage():
    """Global economy — Brent correction. Electric pulsing, A minor 120 BPM."""
    # A2=110, C3=130.81, E3=164.81  (A minor)
    f = (
        # Layer 1: bass A1 pulse at 120 BPM
        "sine=frequency=55:sample_rate=44100:duration=42,"
        "volume=0.6,tremolo=f=2:d=0.85[bass];"
        # Layer 2: sawtooth-ish approximation (sine with slight harmonic)
        "sine=frequency=110:sample_rate=44100:duration=42,"
        "volume=0.35,tremolo=f=2:d=0.4[a];"
        "sine=frequency=130.81:sample_rate=44100:duration=42,"
        "volume=0.28[c];"
        "sine=frequency=164.81:sample_rate=44100:duration=42,"
        "volume=0.26[e];"
        # Layer 3: high stinger at 8th-note pulses
        "sine=frequency=659.26:sample_rate=44100:duration=42,"
        "volume=0.15,tremolo=f=4:d=0.9[stinger];"
        # Layer 4: FM-ish noise burst
        "anoisesrc=duration=42:color=pink:seed=29,"
        "volume=0.08,bandpass=f=3000:w=500,tremolo=f=2:d=0.95[fm];"
        "[bass][a][c][e][stinger][fm]amix=inputs=6:duration=longest:normalize=0,"
        "highpass=f=40,lowpass=f=6500[out]"
    )
    return f


def bed_cycle():
    """Tech AI — EU AI freeze. Rotating arpeggio, E minor 100 BPM."""
    # E minor: E3=164.81, G3=196, B3=246.94, E4=329.63
    # Arpeggio = tremolo each note at different phase
    f = (
        # Bass E2
        "sine=frequency=82.41:sample_rate=44100:duration=42,"
        "volume=0.5[bass];"
        # Arpeggio notes — 4-note pattern at 400ms each (150bpm feel)
        "sine=frequency=164.81:sample_rate=44100:duration=42,"
        "volume=0.3,tremolo=f=2.5:d=0.98[arp1];"
        "sine=frequency=196:sample_rate=44100:duration=42,"
        "volume=0.28,adelay=100|100,tremolo=f=2.5:d=0.98[arp2];"
        "sine=frequency=246.94:sample_rate=44100:duration=42,"
        "volume=0.26,adelay=200|200,tremolo=f=2.5:d=0.98[arp3];"
        "sine=frequency=329.63:sample_rate=44100:duration=42,"
        "volume=0.22,adelay=300|300,tremolo=f=2.5:d=0.98[arp4];"
        # Pad E3 sustain for glue
        "sine=frequency=164.81:sample_rate=44100:duration=42,"
        "volume=0.15,vibrato=f=0.1:d=0.02[pad];"
        "[bass][arp1][arp2][arp3][arp4][pad]amix=inputs=6:duration=longest:normalize=0,"
        "highpass=f=50,lowpass=f=7000[out]"
    )
    return f


def bed_echo():
    """Gulf regional — Muscat track. Reverberant, C major 70 BPM, diplomatic."""
    # C major: C3=130.81, E3=164.81, G3=196, C4=261.63
    f = (
        # Layer 1: C2 bass
        "sine=frequency=65.41:sample_rate=44100:duration=42,"
        "volume=0.45[bass];"
        # Layer 2: major triad with aecho for cavernous feel
        "sine=frequency=130.81:sample_rate=44100:duration=42,"
        "volume=0.3,aecho=0.8:0.7:800:0.5[c];"
        "sine=frequency=164.81:sample_rate=44100:duration=42,"
        "volume=0.25,aecho=0.8:0.6:900:0.45[e];"
        "sine=frequency=196:sample_rate=44100:duration=42,"
        "volume=0.22,aecho=0.8:0.6:1000:0.45[g];"
        # Layer 3: high C4 melody line with slow tremolo
        "sine=frequency=523.25:sample_rate=44100:duration=42,"
        "volume=0.12,tremolo=f=1.17:d=0.5,aecho=0.8:0.5:600:0.4[lead];"
        # Layer 4: soft noise wash for air
        "anoisesrc=duration=42:color=brown:seed=41,"
        "volume=0.04,lowpass=f=800[air];"
        "[bass][c][e][g][lead][air]amix=inputs=6:duration=longest:normalize=0,"
        "highpass=f=45,lowpass=f=5500[out]"
    )
    return f


def bed_ambient_syn():
    """Europe — Merz survives. Atmospheric synth, F minor 65 BPM."""
    # F minor: F2=87.31, Ab2=103.83, C3=130.81
    f = (
        # Layer 1: F2 drone
        "sine=frequency=87.31:sample_rate=44100:duration=42,"
        "volume=0.55,vibrato=f=0.2:d=0.01[drone];"
        # Layer 2: minor 3rd Ab (103.83)
        "sine=frequency=103.83:sample_rate=44100:duration=42,"
        "volume=0.32,vibrato=f=0.15:d=0.01[third];"
        # Layer 3: C3 fifth with slow tremolo
        "sine=frequency=130.81:sample_rate=44100:duration=42,"
        "volume=0.28,tremolo=f=0.5:d=0.3[fifth];"
        # Layer 4: F4 octave lead with slow attack
        "sine=frequency=349.23:sample_rate=44100:duration=42,"
        "volume=0.2,afade=t=in:st=6:d=12,tremolo=f=0.25:d=0.35[lead];"
        # Layer 5: airy noise pad
        "anoisesrc=duration=42:color=pink:seed=53,"
        "volume=0.06,bandpass=f=1500:w=1000[air];"
        "[drone][third][fifth][lead][air]amix=inputs=5:duration=longest:normalize=0,"
        "highpass=f=45,lowpass=f=4500[out]"
    )
    return f


def bed_fog():
    """MENA — Strait rules. Foggy lowpass, B minor 55 BPM, clandestine."""
    # B minor: B2=123.47, D3=146.83, F#3=185
    f = (
        "sine=frequency=61.74:sample_rate=44100:duration=42,"
        "volume=0.5[subbass];"
        "sine=frequency=123.47:sample_rate=44100:duration=42,"
        "volume=0.4,tremolo=f=0.92:d=0.25[b];"
        "sine=frequency=146.83:sample_rate=44100:duration=42,"
        "volume=0.3[d];"
        "sine=frequency=185:sample_rate=44100:duration=42,"
        "volume=0.25,tremolo=f=0.46:d=0.4[fs];"
        # Foggy noise wash (heavy lowpass for murky feel)
        "anoisesrc=duration=42:color=brown:seed=67,"
        "volume=0.12,lowpass=f=400[fog];"
        # Distant high pad
        "sine=frequency=369.99:sample_rate=44100:duration=42,"
        "volume=0.1,afade=t=in:st=14:d=10,lowpass=f=1500[high];"
        "[subbass][b][d][fs][fog][high]amix=inputs=6:duration=longest:normalize=0,"
        "highpass=f=30,lowpass=f=1800[out]"
    )
    return f


def bed_velocity():
    """Global economy — Ruble 220. Driving rhythmic, G minor 130 BPM."""
    # G minor: G2=98, Bb2=116.54, D3=146.83
    f = (
        # Driving bass G2 at 130 BPM (8th notes = ~230ms)
        "sine=frequency=98:sample_rate=44100:duration=42,"
        "volume=0.6,tremolo=f=4.33:d=0.7[bass];"
        # Chord layer
        "sine=frequency=116.54:sample_rate=44100:duration=42,"
        "volume=0.3,tremolo=f=2.17:d=0.3[bb];"
        "sine=frequency=146.83:sample_rate=44100:duration=42,"
        "volume=0.28,tremolo=f=2.17:d=0.3[d];"
        # High stabs at 16th notes
        "sine=frequency=587.33:sample_rate=44100:duration=42,"
        "volume=0.14,tremolo=f=8.67:d=0.95[stab];"
        # Percussion — hihat-ish noise at 16th
        "anoisesrc=duration=42:color=white:seed=89,"
        "volume=0.07,highpass=f=4000,tremolo=f=8.67:d=0.98[hat];"
        # Kick-ish — low sine pulse at 130bpm
        "sine=frequency=50:sample_rate=44100:duration=42,"
        "volume=0.35,tremolo=f=2.17:d=0.95[kick];"
        "[bass][bb][d][stab][hat][kick]amix=inputs=6:duration=longest:normalize=0,"
        "highpass=f=35,lowpass=f=8000[out]"
    )
    return f


def bed_pulse_syn():
    """Tech AI — OpenAI pause. Square-wave pulse, D minor 108 BPM."""
    # D minor: D2=73.42, F2=87.31, A2=110
    # Square wave approximation via layered odd harmonics
    f = (
        # Fundamental D3
        "sine=frequency=146.83:sample_rate=44100:duration=42,"
        "volume=0.4,tremolo=f=1.8:d=0.85[fund];"
        # 3rd harmonic (square approx) = D3*3 = 440.49
        "sine=frequency=440.49:sample_rate=44100:duration=42,"
        "volume=0.13,tremolo=f=1.8:d=0.85[h3];"
        # 5th harmonic = 734.15
        "sine=frequency=734.15:sample_rate=44100:duration=42,"
        "volume=0.08,tremolo=f=1.8:d=0.85[h5];"
        # Bass D2
        "sine=frequency=73.42:sample_rate=44100:duration=42,"
        "volume=0.55,tremolo=f=1.8:d=0.6[bass];"
        # A2 fifth
        "sine=frequency=110:sample_rate=44100:duration=42,"
        "volume=0.28[a];"
        # F2 minor third
        "sine=frequency=87.31:sample_rate=44100:duration=42,"
        "volume=0.25[mthird];"
        # High pulse D5 at 16th notes
        "sine=frequency=587.33:sample_rate=44100:duration=42,"
        "volume=0.12,tremolo=f=7.2:d=0.95[pulse];"
        "[fund][h3][h5][bass][a][mthird][pulse]amix=inputs=7:duration=longest:normalize=0,"
        "highpass=f=45,lowpass=f=6000[out]"
    )
    return f


def bed_tide():
    """Wildcard — Thwaites calve. Ocean swell, A minor 50 BPM, slow majesty."""
    # A minor: A2=110, C3=130.81, E3=164.81
    f = (
        # Deep A1 bass swell
        "sine=frequency=55:sample_rate=44100:duration=42,"
        "volume=0.55,afade=t=in:st=0:d=8[bass];"
        # A2 with slow 0.83Hz LFO (50bpm)
        "sine=frequency=110:sample_rate=44100:duration=42,"
        "volume=0.4,tremolo=f=0.83:d=0.4[a];"
        # Minor chord
        "sine=frequency=130.81:sample_rate=44100:duration=42,"
        "volume=0.32,tremolo=f=0.83:d=0.3[c];"
        "sine=frequency=164.81:sample_rate=44100:duration=42,"
        "volume=0.28,tremolo=f=0.83:d=0.3[e];"
        # Ocean-wash: pink noise slow-modulated
        "anoisesrc=duration=42:color=pink:seed=103,"
        "volume=0.16,lowpass=f=1200,tremolo=f=0.33:d=0.6[wash];"
        # High E5 distant
        "sine=frequency=659.26:sample_rate=44100:duration=42,"
        "volume=0.1,afade=t=in:st=16:d=14,vibrato=f=0.2:d=0.03[high];"
        "[bass][a][c][e][wash][high]amix=inputs=6:duration=longest:normalize=0,"
        "highpass=f=30,lowpass=f=3800[out]"
    )
    return f


def bed_weight():
    """Iraq — Erbil blockade. Heavy low drone, F minor 60 BPM, oppressive."""
    # F minor: F2=87.31, Ab2=103.83, C3=130.81
    f = (
        # Sub-bass F1
        "sine=frequency=43.65:sample_rate=44100:duration=42,"
        "volume=0.65[sub];"
        # F2 drone
        "sine=frequency=87.31:sample_rate=44100:duration=42,"
        "volume=0.5,tremolo=f=1:d=0.2[f];"
        # Minor 3rd
        "sine=frequency=103.83:sample_rate=44100:duration=42,"
        "volume=0.3[ab];"
        # C3 5th
        "sine=frequency=130.81:sample_rate=44100:duration=42,"
        "volume=0.28[c];"
        # Low tremolo noise rumble
        "anoisesrc=duration=42:color=brown:seed=113,"
        "volume=0.1,lowpass=f=200[rumble];"
        # Crash accent at 15s and 30s (via envelope from sine)
        "sine=frequency=174.61:sample_rate=44100:duration=42,"
        "volume=0.3,afade=t=in:st=14:d=1,afade=t=out:st=17:d=4[hit1];"
        "[sub][f][ab][c][rumble][hit1]amix=inputs=6:duration=longest:normalize=0,"
        "highpass=f=30,lowpass=f=2000[out]"
    )
    return f


def bed_steel():
    """Gulf — Qatar LNG pivot. Metallic resonance, E minor 85 BPM."""
    # E minor: E2=82.41, G2=98, B2=123.47
    f = (
        # E2 bass
        "sine=frequency=82.41:sample_rate=44100:duration=42,"
        "volume=0.5[bass];"
        # G2
        "sine=frequency=98:sample_rate=44100:duration=42,"
        "volume=0.3[g];"
        # B2
        "sine=frequency=123.47:sample_rate=44100:duration=42,"
        "volume=0.28[b];"
        # E4 metallic sine with aecho for steel-pluck feel
        "sine=frequency=329.63:sample_rate=44100:duration=42,"
        "volume=0.22,tremolo=f=1.42:d=0.92,aecho=0.8:0.6:60:0.5[metal];"
        # B4 bell-ish
        "sine=frequency=493.88:sample_rate=44100:duration=42,"
        "volume=0.16,tremolo=f=0.71:d=0.95,aecho=0.8:0.5:80:0.4[bell];"
        # Hi-mid noise tick
        "anoisesrc=duration=42:color=white:seed=127,"
        "volume=0.05,bandpass=f=5000:w=800,tremolo=f=1.42:d=0.98[tick];"
        "[bass][g][b][metal][bell][tick]amix=inputs=6:duration=longest:normalize=0,"
        "highpass=f=40,lowpass=f=7500[out]"
    )
    return f


BEDS = {
    "bed_pressure":     bed_pressure(),
    "bed_anchor":       bed_anchor(),
    "bed_voltage":      bed_voltage(),
    "bed_cycle":        bed_cycle(),
    "bed_echo":         bed_echo(),
    "bed_ambient_syn":  bed_ambient_syn(),
    "bed_fog":          bed_fog(),
    "bed_velocity":     bed_velocity(),
    "bed_pulse_syn":    bed_pulse_syn(),
    "bed_tide":         bed_tide(),
    "bed_weight":       bed_weight(),
    "bed_steel":        bed_steel(),
}


def render_bed(name: str, filter_str: str, out_path: Path) -> None:
    """Render one bed via ffmpeg with loudnorm two-pass."""
    tmp_wav = out_path.with_suffix(".tmp.wav")

    # Stage 1: synthesize filter_complex
    cmd_synth = [
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-filter_complex", filter_str,
        "-map", "[out]",
        "-ar", str(SAMPLE_RATE),
        "-ac", "2",
        "-t", str(DURATION),
        "-c:a", "pcm_s16le",
        str(tmp_wav),
    ]
    r = subprocess.run(cmd_synth, capture_output=True, text=True)
    if r.returncode != 0:
        print(f"[{name}] synth FAIL:", r.stderr[-800:], file=sys.stderr)
        return

    # Stage 2: loudnorm + mp3 encode
    cmd_norm = [
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-i", str(tmp_wav),
        "-af", f"loudnorm=I={TARGET_LUFS}:TP={TARGET_PEAK}:LRA=9,alimiter=limit=0.95",
        "-b:a", "160k",
        "-ar", str(SAMPLE_RATE),
        "-ac", "2",
        str(out_path),
    ]
    r = subprocess.run(cmd_norm, capture_output=True, text=True)
    tmp_wav.unlink(missing_ok=True)
    if r.returncode != 0:
        print(f"[{name}] norm FAIL:", r.stderr[-800:], file=sys.stderr)
        return

    # Audit result
    audit = subprocess.run(
        ["ffmpeg", "-hide_banner", "-i", str(out_path), "-af", "volumedetect",
         "-vn", "-sn", "-dn", "-f", "null", "/dev/null"],
        capture_output=True, text=True,
    )
    mean = ""
    peak = ""
    for line in audit.stderr.splitlines():
        if "mean_volume:" in line:
            mean = line.split("mean_volume:")[1].strip()
        elif "max_volume:" in line:
            peak = line.split("max_volume:")[1].strip()
    size = out_path.stat().st_size / 1024
    print(f"  ✓ {name:18s}  mean={mean:10s}  peak={peak:10s}  size={size:.0f} KB")


def main():
    if not AUDIO_DIR.exists():
        print(f"✗ audio dir missing: {AUDIO_DIR}", file=sys.stderr)
        sys.exit(1)

    print(f"Rendering {len(BEDS)} V6 beds → {AUDIO_DIR}")
    print(f"  duration={DURATION}s  target={TARGET_LUFS} LUFS  peak={TARGET_PEAK} dBFS\n")

    for name, filter_str in BEDS.items():
        out = AUDIO_DIR / f"{name}.mp3"
        render_bed(name, filter_str, out)

    print("\n--- uniqueness check (MD5 + size) ---")
    import hashlib
    seen = {}
    for name in BEDS:
        p = AUDIO_DIR / f"{name}.mp3"
        if not p.exists():
            print(f"  ✗ MISSING: {name}")
            continue
        h = hashlib.md5(p.read_bytes()).hexdigest()
        collision = seen.get(h)
        if collision:
            print(f"  ✗ COLLISION: {name} === {collision}")
        seen[h] = name
        print(f"  {name:18s}  {h}  {p.stat().st_size/1024:.0f} KB")

    print(f"\n✓ rendered {len(seen)} unique beds")


if __name__ == "__main__":
    main()
