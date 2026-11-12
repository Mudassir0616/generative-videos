"""Audio for ZELECTRONICS script 4, "Refurbished isn't used" (20.4 s).

Voiceover: voice/zelectronics-script-4.mp3 (supplied by the user), copied to assets/vo-script4.mp3,
  placed at OFF = 0.2 s. Word times: assets/vo_words.json (whisper small, VO-file times).
Music: light synthesized bed (pad + soft arp + pulse, 120 BPM), ducked under the voice.
SFX: whoosh + tick on scene changes, pops on the sticker / ticks / shield / phone pill,
     tape rip, box slide, iris whoosh, strike + drop, riser + soft impact into the end card.
CUTS/END and the cues below are absolute video times and must match index.html.
usage: python tools/make_audio.py assets/vo-script4.mp3 assets/audio.wav
"""
import os
import subprocess
import sys
import wave

import numpy as np

FF = os.environ.get("FFMPEG", "ffmpeg")
SR = 48000
DUR = 20.4
N = int(SR * DUR)
OFF = 0.2
rng = np.random.default_rng(7)

CUTS = [2.2, 5.45, 8.05, 12.55]      # scene changes (S4->S5 is the iris, handled separately)
IRIS = 9.92
STICKER = 4.44
TICKS = [7.24, 7.46, 7.7, 7.92]      # part check badges
TAPE = 8.86
SLIDE = 9.16
FLAPS = 10.36
SHIELD = 10.5
SIX = 11.24
RING = 11.82
UPB = 14.34
STRIKE = 15.22
DROP = 15.5
PILL = 15.66
END = 16.7

L = np.zeros(N)
R = np.zeros(N)


def hz(m):
    return 440.0 * 2 ** ((m - 69) / 12)


def tt(d):
    return np.arange(int(SR * d)) / SR


def add(sig, t, g=1.0, pan=0.0):
    i = int(round(t * SR))
    if i >= N or i < 0:
        return
    sig = sig[: N - i] * g
    L[i:i + len(sig)] += sig * np.sqrt((1 - pan) / 2)
    R[i:i + len(sig)] += sig * np.sqrt((1 + pan) / 2)


def hp(x):
    return x - np.concatenate([[0], x[:-1]])


def lp(x, k):
    if k <= 1:
        return x
    c = np.cumsum(np.concatenate([[0], x]))
    y = (c[k:] - c[:-k]) / k
    return np.concatenate([y, np.zeros(k - 1)])


# ---------- instruments (soft) ----------
def pad(notes, d):
    t = tt(d)
    x = sum(np.sin(2 * np.pi * hz(m) * t) + 0.5 * np.sin(2 * np.pi * hz(m) * 1.003 * t)
            + 0.25 * np.sin(2 * np.pi * hz(m) * 2 * t) for m in notes)
    e = np.minimum(1, t / 0.6) * np.minimum(1, (d - t) / 0.6)
    return x * e * 0.03


def pluck(m, d=0.22):
    t = tt(0.5)
    f = hz(m)
    x = np.sin(2 * np.pi * f * t) + 0.3 * np.sin(2 * np.pi * 2 * f * t)
    return x * np.exp(-t / d) * 0.05


def softkick():
    t = tt(0.3)
    f = 50 + 70 * np.exp(-t / 0.025)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.12) * 0.35


def shaker():
    t = tt(0.06)
    return hp(rng.uniform(-1, 1, len(t))) * np.exp(-t / 0.018) * 0.035


def bass(m, d=0.9):
    t = tt(d)
    x = np.sin(2 * np.pi * hz(m) * t)
    e = np.minimum(1, t / 0.02) * np.exp(-t / 0.6)
    return x * e * 0.16


# ---------- sfx ----------
def whoosh(d=0.3, g=1.0):
    t = tt(d)
    x = rng.uniform(-1, 1, len(t))
    x = lp(x, 3) - lp(x, 30)
    e = np.sin(np.pi * np.clip(t / d, 0, 1)) ** 2
    return x * e * 0.22 * g


def tick(g=1.0):
    t = tt(0.05)
    return (np.sin(2 * np.pi * 2400 * t) * 0.5 + hp(rng.uniform(-1, 1, len(t))) * 0.5) * np.exp(-t / 0.007) * 0.14 * g


def type_click():
    t = tt(0.04)
    return (hp(rng.uniform(-1, 1, len(t))) * 0.6 + np.sin(2 * np.pi * 1500 * t)) * np.exp(-t / 0.005) * 0.09


def pop(g=1.0):
    t = tt(0.14)
    f = 1100 * np.exp(-t / 0.025) + 380
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.045) * 0.16 * g


def riser(d):
    t = tt(d)
    x = rng.uniform(-1, 1, len(t))
    x = hp(x) * 0.4 + lp(x, 10)
    sweep = np.sin(2 * np.pi * np.cumsum(300 + 1500 * (t / d) ** 2) / SR) * 0.2
    return (x * 0.4 + sweep) * (t / d) ** 2.4 * 0.22


def impact(d=2.2):
    t = tt(d)
    f = 38 + 70 * np.exp(-t / 0.06)
    boom = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.6)
    air = lp(hp(rng.uniform(-1, 1, len(t))), 4) * np.exp(-t / 0.35) * 0.3
    return (boom * 0.55 + air) * 0.7


def chime(m, d=1.6):
    t = tt(d)
    x = sum(np.sin(2 * np.pi * hz(m) * k * t) / k ** 1.5 for k in (1, 2, 3, 4.2))
    return x * np.exp(-t / 0.5) * 0.06


# ---------- music bed: C major-ish, light ----------
CH = [[60, 64, 67, 71], [57, 60, 64, 67], [53, 57, 60, 64], [55, 59, 62, 67]]  # Cmaj7 Am7 Fmaj7 G
RT = [36, 33, 29, 31]
ARP = [[72, 76, 79, 83], [69, 72, 76, 79], [65, 69, 72, 76], [67, 71, 74, 79]]
BAR = 2.0
for b in range(int(DUR / BAR) + 1):
    bt = b * BAR
    ci = b % 4
    add(pad(CH[ci], BAR + 0.5), bt, 1.0)
    add(bass(RT[ci], 1.6), bt, 1.0)
    for s in range(8):  # 8th notes
        st = bt + s * 0.25
        if st >= DUR:
            break
        if st < END:
            if s % 2 == 0:
                add(softkick(), st, 0.55 if st > 1.6 else 0.0)
            add(shaker(), st, 1.0 if s % 2 else 0.5, 0.3)
            add(pluck(ARP[ci][s % 4]), st, 0.8, -0.35 if s % 2 else 0.35)
        else:  # end card: pad + sparse arp only
            if s % 2 == 0:
                add(pluck(ARP[ci][s % 4] + 12, 0.35), st, 0.6, -0.3 if s % 4 else 0.3)

music_L, music_R = L.copy(), R.copy()
L[:] = 0
R[:] = 0

# ---------- sfx cues ----------
for c in CUTS:
    add(whoosh(0.3, 0.9), c - 0.15, 1.0, -0.2)
    add(tick(), c, 1.0)
add(whoosh(0.3, 0.7), 5.2, 1.0, 0.2)            # shrink to dot
add(pop(1.2), STICKER + 0.04)
for i, t in enumerate(TICKS):
    add(pop(0.9), t, 1.0, -0.4 + i * 0.27)
add(whoosh(0.25, 0.6), 6.9, 1.0, 0.0)            # exploded view
add(softkick(), 8.62, 0.7)                        # laptop lands in the box
add(tick(0.8), 8.68); add(tick(0.8), 8.76)        # flaps
add(whoosh(0.22, 0.8), TAPE, 1.0, 0.3)            # tape
add(whoosh(0.5, 1.0), SLIDE, 1.0, 0.5)            # box slides to the door
add(whoosh(0.55, 1.4), IRIS - 0.1)                # iris set piece
add(pop(1.0), FLAPS)
add(riser(0.5), SHIELD - 0.1, 0.7)
add(pop(1.1), SIX)
add(chime(84, 1.6), RING, 1.0)
for i in range(4):
    add(tick(0.5), RING + 0.04 + i * 0.06)
add(pop(0.9), UPB)
add(whoosh(0.18, 0.7), STRIKE, 1.0, -0.3)
add(whoosh(0.45, 0.9), DROP, 1.0, 0.2)
add(pop(1.2), PILL)
add(riser(1.4), END - 1.4, 1.0)
add(impact(), END, 1.0)
add(chime(72, 2.5), END + 0.1, 1.0)
for i in range(12):
    add(tick(0.35), END + 0.35 + i * 0.035)
sfx_L, sfx_R = L.copy(), R.copy()

# ---------- voiceover ----------
raw = subprocess.run([FF, "-v", "error", "-i", sys.argv[1], "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                     capture_output=True, check=True).stdout
vo_src = np.frombuffer(raw, np.float32).astype(np.float64)
vo = np.zeros(N)
i0 = int(OFF * SR)
vo[i0:i0 + len(vo_src)] = vo_src[: N - i0]

# ducking: smooth VO envelope -> music gain 1.0 (no voice) .. 0.45 (voice)
env = np.sqrt(lp(vo ** 2, int(0.05 * SR)))
env = env / (env.max() + 1e-9)
active = np.clip(env * 12, 0, 1)
active = lp(active, int(0.25 * SR))  # release
duck = 1.0 - 0.55 * active

MUSIC_G, SFX_G, VO_G = 0.55, 0.8, 1.0
out_L = music_L * duck * MUSIC_G + sfx_L * SFX_G + vo * VO_G
out_R = music_R * duck * MUSIC_G + sfx_R * SFX_G + vo * VO_G
mix = np.stack([out_L, out_R], 1)
fade = np.ones(N)
fade[: int(0.02 * SR)] = np.linspace(0, 1, int(0.02 * SR))
fo = int(1.8 * SR)
fade[-fo:] = np.linspace(1, 0, fo) ** 1.5
mix *= fade[:, None]
mix *= 0.89 / np.abs(mix).max()

out = sys.argv[2]
tmp = out + ".tmp.wav"
with wave.open(tmp, "wb") as w:
    w.setnchannels(2)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes((mix * 32767).astype("<i2").tobytes())
subprocess.run([FF, "-v", "error", "-y", "-i", tmp, "-af", "loudnorm=I=-15:TP=-1.5:LRA=11", "-ar", str(SR),
                "-c:a", "pcm_s16le", out], check=True)
os.remove(tmp)
print("wrote", out)
