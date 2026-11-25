"""Build the base picture for the Super Deluxe Room tour: enhanced 1080x1920 footage with slow dissolves.

usage: python tools/build_base.py            -> assets/base.mp4 (30.0 s, 24 fps, silent)
Source: raw-footags/rooms/super-deluxe-tour.mp4 (720x1280, 24 fps, 725 frames = 5 shots of 145 frames, ~2.7 Mbps).

Enhancement (the source is a low-bitrate 720p export):
  nlmeans  - removes the blotchy chroma/compression noise on the plain walls
  deband   - smooths the banding on the walls and ceiling
  lanczos  - upscales 720x1280 -> 1080x1920
  cas      - contrast-adaptive sharpening brings back edge crispness after the denoise
  eq       - a touch of contrast/saturation (whites stay below clipping)
Edit: 1.0 s cross-dissolves between the 5 shots (26.21 s), then the last frame is held to 30.0 s and a blurred,
slightly darker copy fades in over 25.0-26.0 s as the end-card background.
Needs ffmpeg on PATH (Windows PC: %LOCALAPPDATA%/Programs/ffmpeg/bin).
"""
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = ROOT.parents[1] / "raw-footags" / "rooms" / "super-deluxe-tour.mp4"
OUT = ROOT / "assets" / "base.mp4"

FPS = 24
SHOT = 145                     # frames per shot
XF = 1.0                       # dissolve length, s
TOTAL = 30.0                   # final length, s
END_BLUR_AT = 25.0             # end-card background starts here

ENHANCE = ("nlmeans=s=2.2:p=5:r=9,"
           "deband=1thr=0.015:2thr=0.015:3thr=0.015:range=16:blur=1,"
           "scale=1080:1920:flags=lanczos,cas=0.55,"
           "eq=contrast=1.03:saturation=1.05,setsar=1")

parts = [f"[0:v]{ENHANCE},split=5" + "".join(f"[e{i}]" for i in range(5))]
for i in range(5):
    parts.append(f"[e{i}]trim=start_frame={i * SHOT}:end_frame={(i + 1) * SHOT},setpts=PTS-STARTPTS[s{i}]")

shot_len = SHOT / FPS
prev, length = "s0", shot_len
for i in range(1, 5):
    off = length - XF
    parts.append(f"[{prev}][s{i}]xfade=transition=fade:duration={XF}:offset={off:.6f}[x{i}]")
    prev, length = f"x{i}", length + shot_len - XF

hold = TOTAL - length
parts.append(f"[{prev}]tpad=stop_mode=clone:stop_duration={hold:.6f},split[sharp][tob]")
parts.append(f"[tob]trim=start={END_BLUR_AT},setpts=PTS-STARTPTS,gblur=sigma=22,eq=brightness=-0.06,"
             f"format=yuva420p,fade=t=in:st=0:d=1:alpha=1,setpts=PTS+{END_BLUR_AT}/TB[blur]")
parts.append("[sharp][blur]overlay=eof_action=pass,format=yuv420p[v]")

cmd = ["ffmpeg", "-y", "-v", "error", "-stats", "-i", str(SRC), "-filter_complex", ";".join(parts), "-map", "[v]",
       "-an", "-r", str(FPS), "-t", f"{TOTAL}", "-c:v", "libx264", "-preset", "slow", "-crf", "14",
       "-pix_fmt", "yuv420p", "-color_primaries", "bt709", "-color_trc", "bt709", "-colorspace", "bt709",
       "-movflags", "+faststart", str(OUT)]
OUT.parent.mkdir(parents=True, exist_ok=True)
print(f"dissolves end at {length:.3f} s, hold {hold:.3f} s")
subprocess.run(cmd, check=True)
print("wrote", OUT)
