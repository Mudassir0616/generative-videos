"""Audio for the ZELECTRONICS refurbished-laptops reel (31.5 s).

Voiceover: Friday (ElevenLabs, voice id hJahZg6VJqF122vA08G4), assets/vo-friday.mp3.
  - placed at OFF = 0.2 s
  - a 0.6 s pause is inserted at VO time 27.0 s (between "smart is." and "ZELECTRONICS")
Music: light, fully synthesized bed (soft pad + gentle arp + quiet pulse, 120 BPM), ducked under the voice.
SFX: whoosh + tick on every scene change, pops for hexagons/pills, type clicks, counter ticks,
     riser + soft impact into the end card.

CUE TIMES BELOW ARE ABSOLUTE VIDEO TIME and must match index.html.
usage: python3 tools/make_audio.py assets/vo-friday.mp3 assets/audio.wav
"""
import subprocess
import sys
import wave

import numpy as np

SR = 48000
DUR = 31.5
N = int(SR * DUR)
OFF = 0.2
GAP_AT, GAP = 27.0, 0.6  # VO time of the cut, inserted silence
rng = np.random.default_rng(7)


def vo_abs(t):
    """VO-file time -> absolute video time."""
    return t + OFF + (GAP if t >= GAP_AT else 0.0)


# scene starts (absolute)
CUTS = [1.65, 3.9, 6.3, 8.1, 10.4, 14.45, 16.65, 23.8, 27.65]
HEX = [vo_abs(t) for t in (10.38, 11.54, 12.72)]
PILLS = [vo_abs(t) for t in (16.6, 18.24, 18.96, 19.8, 20.94, 22.22)]
ICONS = [vo_abs(3.82), vo_abs(5.08)]
TYPE1 = (vo_abs(6.2), 21, 0.045)  # "Costs more than ever." start, chars, step
TYPE2 = (vo_abs(23.76), 31, 0.05)  # "Because new isn't an advantage."
COUNTER = (vo_abs(8.02) + 0.1, 1.4)  # counter roll start, duration
SMART = vo_abs(25.92)
END = 27.65

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
for t in HEX:
    add(pop(1.1), t)
for i, t in enumerate(PILLS):
    add(pop(0.9), t, 1.0, 0.3 if i % 2 else -0.3)
for t in ICONS:
    add(pop(0.8), t)
for (t0, n, step) in (TYPE1, TYPE2):
    for i in range(n):
        add(type_click(), t0 + i * step, 1.0, 0.1)
t0, d = COUNTER
for i in range(10):
    add(tick(0.7), t0 + d * (i / 10) ** 0.6)
add(chime(84), t0 + d, 1.0)
add(whoosh(0.5, 1.2), SMART - 0.25)
add(chime(79, 2.0), SMART + 0.25, 0.8)  # ellipse draw
add(riser(1.6), END - 1.6, 1.0)
add(impact(), END, 1.0)
add(chime(72, 2.5), END + 0.1, 1.0)
for i in range(12):  # brand letters
    add(tick(0.35), END + 0.45 + i * 0.04)
sfx_L, sfx_R = L.copy(), R.copy()

# ---------- voiceover ----------
raw = subprocess.run(["ffmpeg", "-v", "error", "-i", sys.argv[1], "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                     capture_output=True, check=True).stdout
vo_src = np.frombuffer(raw, np.float32).astype(np.float64)
cut = int(GAP_AT * SR)
vo_src = np.concatenate([vo_src[:cut], np.zeros(int(GAP * SR)), vo_src[cut:]])
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

tmp = sys.argv[2] + ".tmp.wav"
with wave.open(tmp, "wb") as w:
    w.setnchannels(2)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes((mix * 32767).astype("<i2").tobytes())
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", tmp, "-af", "loudnorm=I=-15:TP=-1.5:LRA=11", "-ar", str(SR),
                "-c:a", "pcm_s16le", sys.argv[2]], check=True)
subprocess.run(["rm", "-f", tmp])
print("wrote", sys.argv[2])
