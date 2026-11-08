"""Build the silent, graded 1080x1920 / 24 fps picture edit for the Pukhtoon reel.

Cuts sit on the music grid of voice/restraunt/ishqa-ve-chaddeya.mp3: eighth notes every 0.3527 s
(~85 BPM) from 0.101 s, accents every 3 eighths (1.058 s). Cut times (s) -> frames at 24 fps.

usage:
  python tools/build_base.py render  <out.mp4> [v1|v2]   full base video (default v2)
  python tools/build_base.py preview <out_dir> [v1|v2]   one graded still per shot (for checking the grade)
v1 = 15 s fast cut (cuts every 1.5 beats); v2 = 20 s slower cut (cuts on the 3-eighth accents, 1.06 s / 2.12 s holds).
Raw footage is read from raw-footags/pakhtoon-vid-1 and never modified. Needs ffmpeg on PATH.
"""
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
RAW = ROOT / "raw-footags" / "pakhtoon-vid-1"
FPS = 24

# global look: warm amber like the reference reels, richer but not garish
GRADE = "colortemperature=temperature=4700:mix=0.6,eq=contrast=1.05:saturation=1.12:gamma=0.98"
# per-clip fixes on top of the global grade
FIX = {
    "C084": "colorbalance=bs=-0.06:bm=-0.04",   # window side drifts blue
    "C149": "huesaturation=colors=c+b:saturation=-0.55:intensity=-0.05,colorbalance=bs=-0.12:bm=-0.08:rm=0.05:rh=0.03",  # glass table reflects blue daylight
    "C096": "colorbalance=rm=0.03:bs=-0.03",    # cool exterior daylight
    "C075": "colorbalance=rm=0.02",
}

# (clip, source in-point s, frames, push-in fraction over the shot, note)
SHOTS_V1 = [
    ("C084", 0.46, 28, 0.00, "amber pendant cluster (hook); continues from shot 15 for a seamless loop"),
    ("C096", 0.20, 25, 0.00, "THE CALIPH exterior sign"),
    ("C075", 0.00, 26, 0.00, "lobby: wingback chairs + Caliph stand"),
    ("C079", 1.50, 17, 0.00, "corridor glide"),
    ("C084", 4.00, 25, 0.00, "orange chairs + marble pillar"),
    ("C138", 0.00, 25, 0.03, "first food: table-level glide (text exits here)"),
    ("C147", 0.00, 26, 0.00, "biryani handi top-down"),
    ("C143", 0.00, 25, 0.00, "tikka platter, table level"),
    ("C149", 0.40, 34, 0.05, "cream drizzle (money moment)"),
    ("C114", 0.00, 17, 0.03, "gulab jamun + red drink"),
    ("C087", 2.30, 25, 0.00, "menu logo -> whip blur"),
    ("C110", 0.50, 34, 0.05, "hero table spread (loudest part of the track)"),
    ("C143", 2.30, 17, 0.00, "tikka + shami kebabs"),
    ("C085", 5.00, 26, 0.03, "set table: menu + rose"),
    ("C084", 0.00, 11, 0.00, "pendants again -> loops into shot 1"),
]

# v2: 20.2 s, 13 shots; cut points on accents n = 5, 11, 17, 20, 26, 29, 32, 35, 41, 44, 47, 53, 57 of the eighth grid
SHOTS_V2 = [
    ("C084", 1.417, 45, 0.00, "amber pendant cluster (hook); continues from shot 13 for a seamless loop"),
    ("C096", 0.20, 51, 0.00, "THE CALIPH exterior sign, glide toward the entrance"),
    ("C075", 0.60, 50, 0.00, "lobby: wingback chairs -> reception"),
    ("C079", 1.50, 26, 0.00, "corridor glide"),
    ("C138", 0.00, 51, 0.03, "first food: table-level glide (text exits here)"),
    ("C147", 0.00, 25, 0.00, "biryani handi top-down"),
    ("C143", 0.00, 25, 0.00, "tikka platter, table level"),
    ("C084", 4.00, 26, 0.00, "orange chairs + marble pillar (breather)"),
    ("C149", 0.30, 51, 0.04, "cream drizzle (money moment)"),
    ("C114", 0.50, 25, 0.03, "gulab jamun + red drink"),
    ("C087", 2.30, 25, 0.00, "menu logo -> whip blur"),
    ("C110", 0.40, 51, 0.05, "hero table spread"),
    ("C084", 0.00, 34, 0.00, "pendants again -> loops into shot 1"),
]
VERSIONS = {"v1": SHOTS_V1, "v2": SHOTS_V2}
SHOTS = SHOTS_V2


def src(clip):
    return next(RAW.glob(f"*{clip}.mp4"))


def chain(i, clip, frames, push, still=False):
    d = frames / FPS
    # 2160x3840 -> 1080x1920 is exactly 0.5x; push-in grows the scale linearly over the shot, crop stays centred
    if push:
        sc = (f"scale=w='2*trunc(540*(1+{push}*t/{d:.4f}))':h='2*trunc(960*(1+{push}*t/{d:.4f}))'"
              f":eval=frame:flags=lanczos,crop=1080:1920")
    else:
        sc = "scale=1080:1920:flags=lanczos"
    g = GRADE + ("," + FIX[clip] if clip in FIX else "")
    head = f"[{i}:v]fps={FPS},setpts=PTS-STARTPTS," if not still else f"[{i}:v]"
    tail = f"trim=end_frame={frames},setpts=PTS-STARTPTS,setsar=1,format=yuv420p[v{i}]" if not still else f"setsar=1[v{i}]"
    return f"{head}{sc},{g},{tail}"


def render(out):
    args, parts = ["ffmpeg", "-v", "error", "-y"], []
    for i, (clip, t0, fr, push, _) in enumerate(SHOTS):
        args += ["-ss", f"{t0:.3f}", "-t", f"{fr / FPS + 0.3:.3f}", "-i", str(src(clip))]
        parts.append(chain(i, clip, fr, push))
    fc = ";".join(parts) + ";" + "".join(f"[v{i}]" for i in range(len(SHOTS))) + f"concat=n={len(SHOTS)}:v=1:a=0[out]"
    args += ["-filter_complex", fc, "-map", "[out]", "-an", "-r", str(FPS), "-c:v", "libx264", "-preset", "slow",
             "-crf", "14", "-pix_fmt", "yuv420p", "-movflags", "+faststart", out]
    subprocess.run(args, check=True)
    total = sum(s[2] for s in SHOTS)
    print(f"wrote {out}: {len(SHOTS)} shots, {total} frames = {total / FPS:.3f} s")


def preview(out_dir):
    out = pathlib.Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    for i, (clip, t0, fr, push, note) in enumerate(SHOTS):
        mid = t0 + fr / FPS / 2
        for tag, filt in (("raw", "scale=360:640"), ("graded", f"scale=360:640,{GRADE}" + ("," + FIX[clip] if clip in FIX else ""))):
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{mid:.3f}", "-i", str(src(clip)), "-frames:v", "1",
                            "-vf", filt, str(out / f"{i + 1:02d}_{tag}.png")], check=True)
    print("previews in", out)


if __name__ == "__main__":
    SHOTS = VERSIONS[sys.argv[3] if len(sys.argv) > 3 else "v2"]
    {"render": render, "preview": preview}[sys.argv[1]](sys.argv[2])
