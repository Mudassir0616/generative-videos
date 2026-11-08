"""Make assets/caliph-logo-full.png from the client logo (gold emblem + black wordmark on white).
Emblem stays gold #bb8d28; the black wordmark becomes white so it reads over video. Pixels are
classified by colour (gold has a strong red-minus-blue tint, black text has none).
usage: python tools/make_logo.py <source.png> <out.png>   (needs numpy, ffmpeg)"""
import subprocess, sys
import numpy as np

src, dst = sys.argv[1], sys.argv[2]
info = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "stream=width,height", "-of", "csv=p=0", src], capture_output=True, text=True).stdout
W, H = map(int, info.strip().split(","))
a = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", src, "-f", "rawvideo", "-pix_fmt", "rgba", "-"], capture_output=True).stdout, np.uint8)
a = a.reshape(H, W, 4).astype(float)
rgb, al = a[..., :3], a[..., 3] / 255
ink = 255 - rgb.min(2)                                  # how far from white
tint = (rgb[..., 0] - rgb[..., 2]) / np.maximum(ink, 1)  # ~0.68 gold, ~0 black
is_gold = tint > 0.3
lum = 0.299 * rgb[..., 0] + 0.587 * rgb[..., 1] + 0.114 * rgb[..., 2]
cov = np.where(is_gold, np.clip(ink / (255 - 40), 0, 1), np.clip((255 - lum) / (255 - 20), 0, 1)) * al
col = np.where(is_gold[..., None], np.array([0xBB, 0x8D, 0x28]), np.array([255, 255, 255]))
ys, xs = np.where(cov > 0.03)
y0, y1, x0, x1 = ys.min() - 8, ys.max() + 9, xs.min() - 8, xs.max() + 9
out = np.zeros((y1 - y0, x1 - x0, 4), np.uint8)
out[..., :3] = col[y0:y1, x0:x1]
out[..., 3] = (cov[y0:y1, x0:x1] * 255).round()
h, w = out.shape[:2]
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgba", "-s", f"{w}x{h}", "-i", "-", dst], input=out.tobytes(), check=True)
print("wrote", dst, w, h)
