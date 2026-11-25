"""Original calm instrumental for the Super Deluxe Room tour (fully synthesized, royalty-free, ours to use).

usage: python tools/make_music.py      -> assets/music.wav (30.0 s, 48 kHz stereo)
Soft felt-piano arpeggios over a warm pad and a low sine bass, in D major, with a long hall reverb.
Grid: one chord every 2.5208 s (4 beats at ~95 BPM, felt as slow half-time) starting at 0.5 s, so every dissolve
midpoint in the edit (5.54, 10.58, 15.63, 20.67 s) lands on a chord change. The pad is already sounding at frame 0.
The final chord (25.71 s) arrives under the "Book your stay" end card and rings out to 30 s.
"""
import pathlib
import wave

import numpy as np

SR = 48000
DUR = 30.0
N = int(SR * DUR)
T0, BAR = 0.5, 2.5208333
BEAT = BAR / 4
rng = np.random.default_rng(7)
L = np.zeros(N)
R = np.zeros(N)


def hz(m):
    return 440.0 * 2 ** ((m - 69) / 12)


def add(sig, t, g=1.0, pan=0.0):
    i = int(round(t * SR))
    if i >= N:
        return
    sig = sig[: N - i] * g
    L[i:i + len(sig)] += sig * np.sqrt((1 - pan) / 2)
    R[i:i + len(sig)] += sig * np.sqrt((1 + pan) / 2)


def onepole(x, fc):
    """one-pole lowpass."""
    a = np.exp(-2 * np.pi * fc / SR)
    y = np.empty_like(x)
    acc = 0.0
    for i, v in enumerate(x):  # short signals only
        acc = (1 - a) * v + a * acc
        y[i] = acc
    return y


def piano(m, vel=0.5, dur=4.0):
    """soft felt piano: inharmonic partials, upper partials decay faster, gentle attack, muted hammer thump."""
    f0 = hz(m)
    t = np.arange(int(SR * dur)) / SR
    out = np.zeros_like(t)
    B = 0.00035
    bright = 0.55 + 0.6 * vel
    for n in range(1, 11):
        fn = f0 * n * np.sqrt(1 + B * n * n)
        if fn > 9000:
            break
        amp = (1 / n ** 1.6) * (bright ** (n - 1))
        dec = 0.9 + 0.35 * n + f0 / 500
        out += amp * np.sin(2 * np.pi * fn * t + rng.uniform(0, 6.28)) * np.exp(-dec * t)
    # two-stage decay (fast drop then long sustain) like a real string
    env = 0.65 * np.exp(-t * (2.2 + f0 / 900)) + 0.35 * np.exp(-t * (0.35 + f0 / 2500))
    att = np.minimum(1, t / 0.006)
    thump = rng.normal(0, 1, len(t)) * np.exp(-t * 90) * 0.04
    thump[: 2000] = onepole(thump[: 2000], 700)
    thump[2000:] = 0
    return (out * env * att + thump) * vel


def pad(notes, dur, g=1.0):
    """warm pad: a few detuned soft partials per note, slow swell, gentle tremolo."""
    t = np.arange(int(SR * dur)) / SR
    out = np.zeros_like(t)
    for m in notes:
        for det in (-0.07, 0.0, 0.07):
            f = hz(m + det)
            for n, a in ((1, 1.0), (2, 0.28), (3, 0.09)):
                out += a * np.sin(2 * np.pi * f * n * t + rng.uniform(0, 6.28))
    out /= len(notes) * 3
    swell = np.minimum(1, t / 1.4) * np.minimum(1, (dur - t) / 1.2).clip(0, 1)
    trem = 1 + 0.06 * np.sin(2 * np.pi * 0.23 * t)
    return out * swell * trem * g


def bass(m, dur):
    t = np.arange(int(SR * dur)) / SR
    s = np.sin(2 * np.pi * hz(m) * t) + 0.15 * np.sin(2 * np.pi * hz(m) * 2 * t)
    return s * np.minimum(1, t / 0.08) * np.exp(-t * 0.55)


# chord: (bass root, pad voicing, arpeggio tones low->high, melody note or None)
D, Bm, G, Asus, A, Fsm, Em = range(7)
CH = {
    D:    (38, [57, 62, 66, 69], [50, 57, 62, 64, 66, 69], 76),   # Dmaj9
    Bm:   (35, [54, 59, 62, 66], [47, 54, 59, 61, 62, 66], 74),   # Bm(add9)
    G:    (31, [55, 59, 62, 66], [43, 50, 55, 59, 62, 66], 71),   # Gmaj7
    Asus: (33, [57, 62, 64, 69], [45, 52, 57, 62, 64, 69], 73),   # Asus4
    A:    (33, [57, 61, 64, 69], [45, 52, 57, 61, 64, 69], 73),   # A
    Fsm:  (30, [54, 57, 61, 64], [42, 49, 54, 57, 61, 64], 69),   # F#m7
    Em:   (28, [55, 59, 62, 66], [40, 47, 54, 55, 59, 62], 71),   # Em9
}
PROG = [D, Bm, G, Asus, D, Fsm, G, Em, G, A, D]          # 11 chords; the last one is the ending

# pad from frame 0: a soft D chord swelling in before the first piano note
add(pad(CH[D][1], T0 + BAR + 0.6), 0.0, 0.55)

for k, c in enumerate(PROG):
    t = T0 + k * BAR
    root, voicing, arp, mel = CH[c]
    last = k == len(PROG) - 1
    length = (DUR - t) if last else BAR + 1.0
    if k > 0:
        add(pad(voicing, length), t - 0.3, 0.55)
    add(bass(root, length), t, 0.42)
    if last:
        # final chord: rolled, then left to ring
        for j, m in enumerate([arp[0], arp[2], arp[3], arp[4], arp[5], mel]):
            add(piano(m, 0.40 - 0.02 * j, 5.0), t + j * 0.11, 0.9, pan=-0.3 + 0.12 * j)
        continue
    # 8 eighth notes per chord: a slow rising-falling broken chord
    pattern = [0, 2, 3, 4, 5, 4, 3, 2]
    for j, idx in enumerate(pattern):
        m = arp[idx]
        vel = 0.34 if j == 0 else 0.24 + 0.04 * (j in (4,))
        jitter = rng.uniform(-0.008, 0.008)
        add(piano(m, vel, 3.2), t + j * BEAT / 2 + jitter, 0.85, pan=-0.35 + 0.1 * idx)
    # a sparse melody note every other chord, on beat 3
    if k % 2 == 1:
        add(piano(mel, 0.30, 4.0), t + 2 * BEAT, 0.8, pan=0.15)

# hall reverb: exponentially decaying stereo noise IR (2.8 s), FFT convolution
ir_len = int(SR * 2.8)
ti = np.arange(ir_len) / SR
irs = []
for seed in (1, 2):
    nz = np.random.default_rng(seed).normal(0, 1, ir_len) * np.exp(-ti * 2.4)
    nz = np.convolve(nz, np.ones(6) / 6, mode="same")           # darken the tail
    nz[: int(0.02 * SR)] *= np.linspace(0, 1, int(0.02 * SR))   # pre-delay feel
    irs.append(nz / np.sqrt(np.sum(nz ** 2)))
size = 1 << int(np.ceil(np.log2(N + ir_len)))


def conv(x, h):
    return np.fft.irfft(np.fft.rfft(x, size) * np.fft.rfft(h, size), size)[:N]


wetL, wetR = conv(L, irs[0]), conv(R, irs[1])
mixL = 0.72 * L + 0.55 * wetL
mixR = 0.72 * R + 0.55 * wetR

# fade out the last 2.2 s, short fade in at the very start
t = np.arange(N) / SR
fade = np.clip((DUR - t) / 2.2, 0, 1) ** 1.5 * np.clip(t / 0.05, 0, 1)
mix = np.stack([mixL * fade, mixR * fade], axis=1)
# gentle loudness target: peak -3 dBFS
mix *= 10 ** (-3 / 20) / np.max(np.abs(mix))
out = pathlib.Path(__file__).resolve().parents[1] / "assets" / "music.wav"
out.parent.mkdir(parents=True, exist_ok=True)
with wave.open(str(out), "wb") as w:
    w.setnchannels(2)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes((mix * 32767).astype("<i2").tobytes())
rms = 20 * np.log10(np.sqrt(np.mean(mix ** 2)))
print(f"wrote {out} ({DUR} s, RMS {rms:.1f} dBFS)")
