"""Audio for the ZELECTRONICS refurbished-laptops reel (36.5 s).

Voiceover: Friday v2 (ElevenLabs, voice id ka2YlHIZtpI73mTUG5iF), assets/vo-friday-v2.mp3
  (full read incl. "Shop certified refurbished laptops and desktops at Zelectronics."), placed at OFF = 0.2 s.
Music: light, fully synthesized bed (soft pad + gentle arp + quiet pulse, 120 BPM), ducked under the voice.
SFX: whoosh + tick on every scene change, pops for hexagons/pills/CTA tiles, type clicks, counter ticks,
     riser + soft impact into the end card.

Word times are VO-file times from a whisper transcript; CUTS/END are absolute video time.
All of them must match index.html.
usage: python tools/make_audio.py assets/vo-friday-v2.mp3 assets/audio.wav
       (set FFMPEG=<path to ffmpeg> if ffmpeg is not on PATH)
"""
import os
import subprocess
import sys
import wave

import numpy as np

FF = os.environ.get("FFMPEG", "ffmpeg")
SR = 48000
DUR = 36.5
N = int(SR * DUR)
OFF = 0.2
rng = np.random.default_rng(7)


def vo_abs(t):
    """VO-file time -> absolute video time."""
    return t + OFF


# scene starts (absolute)
CUTS = [2.3, 4.75, 7.1, 9.15, 11.45, 15.75, 18.3, 26.2, 30.2, 32.95]
HEX = [vo_abs(t) for t in (11.68, 12.66, 14.0)]
PILLS = [vo_abs(t) for t in (18.18, 20.4, 20.9, 21.88, 22.9, 24.42)]
ICONS = [vo_abs(4.68), vo_abs(5.84)]
TYPE1 = (7.18, 21, 0.055)  # "Costs more than ever." start, chars, step
TYPE2 = (26.36, 31, 0.05)  # "Because new isn't an advantage."
COUNTER = (9.4, 1.4)  # counter roll start, duration
SMART = vo_abs(28.88)
CTA_POPS = [vo_abs(31.36), vo_abs(31.9)]  # "laptops", "desktops" tiles
END = 32.95

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
for i, t in enumerate(CTA_POPS):
    add(pop(1.0), t, 1.0, -0.25 if i == 0 else 0.25)
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
