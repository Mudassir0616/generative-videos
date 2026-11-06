"""Original 30s music bed + sound design for the ZELECTRONICS v2 reel (fully synthesized, royalty-free).

120 BPM (beat 0.5s). Every scene cut sits on the 8th-note grid, so cuts land on the music.
Structure:
  0.0-6.5   hook: tight kick/hat pulse + filtered arp, tension rises; riser into 6.5
  6.5       DROP on brand reveal (impact), full groove
  18.75     "why" section: groove continues, chip pops
  23.25     flash build (snare roll) -> 24.75 end-card impact, groove drops to pad + arp
  28-30     fade out
Also writes assets/grain.png (sparse dust specks) for the visual grain layer.
"""
import subprocess
import sys
import wave

import numpy as np

SR = 48000
DUR = 40.0
N = int(SR * DUR)
BEAT = 0.5
rng = np.random.default_rng(11)

L = np.zeros(N)
R = np.zeros(N)

CUTS = [0.75, 1.75, 3.5, 5.5, 6.25, 7.0, 7.75, 9.0, 11.5, 13.75, 16.25, 18.75, 21.25, 23.75, 26.25, 32.25, 33.0, 33.75, 34.5]


def hz(m):
    return 440.0 * 2 ** ((m - 69) / 12)


def add(sig, t, g=1.0, pan=0.0):
    i = int(round(t * SR))
    if i >= N or i < 0:
        return
    sig = sig[: N - i] * g
    L[i:i + len(sig)] += sig * np.sqrt((1 - pan) / 2)
    R[i:i + len(sig)] += sig * np.sqrt((1 + pan) / 2)


def tt(d):
    return np.arange(int(SR * d)) / SR


def hp(x):
    return x - np.concatenate([[0], x[:-1]])


def lp(x, k):
    """cheap moving-average lowpass (k samples)."""
    if k <= 1:
        return x
    c = np.cumsum(np.concatenate([[0], x]))
    y = (c[k:] - c[:-k]) / k
    return np.concatenate([y, np.zeros(k - 1)])


def kick(g=1.0):
    t = tt(0.4)
    f = 48 + 130 * np.exp(-t / 0.03)
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.15)
    x[:200] += hp(rng.uniform(-1, 1, 200)) * 0.3  # click
    return np.tanh(x * 1.6) * 0.85 * g


def hat(d=0.04):
    t = tt(0.08)
    return hp(hp(rng.uniform(-1, 1, len(t)))) * np.exp(-t / d) * 0.09


def snare():
    t = tt(0.3)
    body = np.sin(2 * np.pi * 190 * t) * np.exp(-t / 0.05) * 0.4
    nz = hp(rng.uniform(-1, 1, len(t))) * np.exp(-t / 0.09) * 0.45
    return (body + nz) * 0.7


def pluck(m, d=0.16):
    t = tt(0.3)
    f = hz(m)
    x = np.sign(np.sin(2 * np.pi * f * t)) * 0.5 + np.sin(2 * np.pi * f * t)
    x = lp(x, 6)
    return x * np.exp(-t / d) * 0.075


def bass(m, d=0.22):
    t = tt(d)
    f = hz(m)
    x = np.sin(2 * np.pi * f * t) + 0.35 * np.sin(2 * np.pi * 2 * f * t) + 0.12 * np.sign(np.sin(2 * np.pi * f * t))
    e = np.minimum(1, t / 0.003) * np.minimum(1, (d - t) / 0.03)
    return x * e * 0.3


def pad(notes, d):
    t = tt(d)
    x = sum(np.sin(2 * np.pi * hz(m) * k * t) / k ** 1.4 for m in notes for k in (1, 2, 3) for _ in (0,))
    x = x + sum(np.sin(2 * np.pi * hz(m) * 1.004 * t) for m in notes) * 0.6
    e = np.minimum(1, t / 0.3) * np.minimum(1, (d - t) / 0.3)
    return x * e * 0.022


def whoosh(d=0.28, g=1.0):
    t = tt(d)
    x = rng.uniform(-1, 1, len(t))
    x = lp(x, 3) - lp(x, 40)
    e = np.sin(np.pi * np.clip(t / d, 0, 1)) ** 2
    return x * e * 0.35 * g


def tick():
    t = tt(0.05)
    return (np.sin(2 * np.pi * 2600 * t) * 0.5 + hp(rng.uniform(-1, 1, len(t)))) * np.exp(-t / 0.008) * 0.22


def type_click():
    t = tt(0.04)
    return (hp(rng.uniform(-1, 1, len(t))) * 0.6 + np.sin(2 * np.pi * 1400 * t)) * np.exp(-t / 0.006) * 0.16


def pop():
    t = tt(0.12)
    f = 900 * np.exp(-t / 0.03) + 300
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.04) * 0.22


def impact(d=1.8):
    t = tt(d)
    f = 34 + 90 * np.exp(-t / 0.06)
    boom = np.tanh(np.sin(2 * np.pi * np.cumsum(f) / SR) * 2) * np.exp(-t / 0.55)
    air = hp(rng.uniform(-1, 1, len(t))) * np.exp(-t / 0.3) * 0.25
    return (boom * 0.75 + air) * 0.9


def riser(d):
    t = tt(d)
    x = rng.uniform(-1, 1, len(t))
    x = hp(x) * 0.5 + lp(x, 8)
    sweep = np.sin(2 * np.pi * np.cumsum(200 + 1400 * (t / d) ** 2) / SR) * 0.25
    return (x * 0.5 + sweep) * (t / d) ** 2.2 * 0.35


# progression (A minor): Am F C G, one chord per bar (2s)
CH = [[57, 60, 64], [53, 57, 60], [48, 52, 55], [55, 59, 62]]
RT = [33, 29, 36, 31]
ARP = [[69, 72, 76, 81], [65, 69, 72, 77], [64, 67, 72, 76], [67, 71, 74, 79]]

DROP, BUILD, END = 9.0, 32.25, 34.5
for b in range(20):
    bt = b * 2.0
    ci = b % 4
    add(pad(CH[ci], 2.3), bt, 1.0 if bt < DROP else 1.3)
    for s in range(16):
        st = bt + s * BEAT / 4
        if st >= DUR:
            break
        if st < DROP:
            if s % 4 == 0:
                add(kick(0.75), st)
            if s % 2 == 1:
                add(hat(), st, 0.8, 0.3)
            add(pluck(ARP[ci][s % 4]), st, 0.5 + 0.5 * st / DROP, -0.3 if s % 2 else 0.3)
        elif st < BUILD:
            if s % 4 == 0:
                add(kick(), st)
            if s in (4, 12):
                add(snare(), st, 0.8)
            add(hat(0.03 if s % 2 else 0.015), st, 1.0 if s % 2 else 0.5, 0.25)
            if s % 4 == 2:
                add(hat(0.12), st, 0.6, -0.25)
            add(pluck(ARP[ci][s % 4] + (12 if s >= 8 and st > 13.75 else 0)), st, 1.0, -0.35 if s % 2 else 0.35)
            if s % 2 == 0:
                add(bass(RT[ci] + (12 if s % 4 == 2 else 0)), st)
        elif st < END:
            add(kick(0.9), st) if s % 2 == 0 else None
            add(snare(), st, 0.25 + 0.6 * (st - BUILD) / (END - BUILD))
            add(bass(RT[ci]), st, 0.8) if s % 2 == 0 else None
        else:
            if s % 2 == 1:
                add(hat(0.02), st, 0.5, 0.3)
            add(pluck(ARP[ci][s % 4]), st, 0.7, -0.3 if s % 2 else 0.3)

# --- sound design cues ---
for c in CUTS:
    add(whoosh(0.22, 0.8), c - 0.11)
    add(tick(), c, 0.9)
add(riser(1.5), DROP - 1.5, 1.0)
add(impact(), DROP, 1.0)
add(riser(1.5), END - 1.5, 1.1)
add(impact(2.2), END, 1.1)
for i in range(8):  # "but your" typing
    add(type_click(), 1.75 + i * 0.045, 1.0)
for i in range(4):  # "meet" typing
    add(type_click(), 9.05 + i * 0.06, 1.2)
add(riser(1.4), 3.6, 0.6)  # graph climbs
add(pop(), 4.9, 1.0)
for i in range(5):  # why chips
    add(pop(), 27.0 + i * 0.55, 1.0)
for t in (14.2, 16.7, 19.2, 21.7, 24.2):  # service chips
    add(pop(), t, 0.8)
for t in (36.05,):
    add(pop(), t, 1.0)
for i in range(12):  # brand letters
    add(tick(), 34.95 + i * 0.045, 0.35)

mix = np.stack([L, R], 1)
fade = np.ones(N)
fade[:int(0.02 * SR)] = np.linspace(0, 1, int(0.02 * SR))
fo = int(2.0 * SR)
fade[-fo:] = np.linspace(1, 0, fo) ** 1.6
mix *= fade[:, None]
mix = np.tanh(mix * 1.4) / np.tanh(1.4)
mix *= 0.9 / np.abs(mix).max()

out = sys.argv[1]
with wave.open(out, "wb") as w:
    w.setnchannels(2)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes((mix * 32767).astype("<i2").tobytes())
print("wrote", out)

# --- grain texture: sparse grey dust specks on transparent background ---
if len(sys.argv) > 2:
    S = 512
    img = np.zeros((S, S, 4), np.uint8)
    n = 260
    ys, xs = rng.integers(0, S, n), rng.integers(0, S, n)
    for k, (y, x) in enumerate(zip(ys, xs)):
        v = 255 if k % 2 else 0
        img[y, x] = (v, v, v, 200)
        if k % 7 == 0 and y + 1 < S and x + 1 < S:
            img[y:y + 2, x:x + 2] = (v, v, v, 160)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgba", "-s", f"{S}x{S}", "-i", "-",
                    "-frames:v", "1", sys.argv[2]], input=img.tobytes(), check=True)
    print("wrote", sys.argv[2])
