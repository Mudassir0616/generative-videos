# Used 2026-11-08 to build refrences/trending-restraunt-reels/ (probe, cuts, frames, sheets, audio.json, meta.json, index.json).
# Needs ffmpeg/ffprobe on PATH and numpy + faster-whisper. Download reels first with yt-dlp into NN-<id>/video.mp4 (+ --write-info-json).
"""Prepare reel folders for analysis.
usage: python tools/prep_reels.py <library_dir> [extra_site_packages_dir]
For each <library_dir>/NN-<id>/video.mp4 writes: probe.json, cuts.json, frames/, sheets/, audio.json, meta.json.
"""
import sys, pathlib
if len(sys.argv) > 2 and pathlib.Path(sys.argv[2]).is_dir(): sys.path.insert(0, sys.argv[2])  # optional extra site-packages dir
import json, os, re, subprocess, pathlib
import numpy as np

LIB = pathlib.Path(sys.argv[1])
FF, FP = "ffmpeg", "ffprobe"


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")


def probe(v):
    j = json.loads(run([FP, "-v", "error", "-show_format", "-show_streams", "-of", "json", str(v)]).stdout)
    vs = next(s for s in j["streams"] if s["codec_type"] == "video")
    a = [s for s in j["streams"] if s["codec_type"] == "audio"]
    num, den = map(int, vs["r_frame_rate"].split("/"))
    return {"duration_s": round(float(j["format"]["duration"]), 3), "width": vs["width"], "height": vs["height"],
            "aspect": f'{vs["width"]}:{vs["height"]}', "fps": round(num / den, 3), "video_codec": vs["codec_name"],
            "nb_frames": int(vs.get("nb_frames", 0) or 0), "bitrate_kbps": round(int(j["format"].get("bit_rate", 0)) / 1000),
            "audio": ({"codec": a[0]["codec_name"], "sample_rate": int(a[0]["sample_rate"]), "channels": a[0]["channels"]} if a else None)}


def scene_cuts(v, thr):
    err = run([FF, "-hide_banner", "-i", str(v), "-vf", f"select='gt(scene,{thr})',showinfo", "-an", "-f", "null", "-"]).stderr
    return [round(float(t), 3) for t in re.findall(r"pts_time:([\d.]+)", err)]


def grab(v, t, out, w=540):
    run([FF, "-v", "error", "-y", "-ss", f"{t:.3f}", "-i", str(v), "-frames:v", "1", "-vf", f"scale={w}:-2", "-q:v", "3", str(out)])


def audio_stats(v, dur):
    raw = subprocess.run([FF, "-v", "error", "-i", str(v), "-ac", "1", "-ar", "16000", "-f", "f32le", "-"], capture_output=True).stdout
    x = np.frombuffer(raw, np.float32)
    if len(x) == 0:
        return {"has_audio": False}
    # loudness
    err = run([FF, "-hide_banner", "-i", str(v), "-af", "ebur128", "-f", "null", "-"]).stderr
    m = re.findall(r"I:\s+(-?[\d.]+) LUFS", err)
    # tempo estimate: spectral-flux onset envelope -> autocorrelation, 60-180 BPM
    hop, win = 256, 1024
    frames = np.lib.stride_tricks.sliding_window_view(x, win)[::hop] * np.hanning(win)
    mag = np.abs(np.fft.rfft(frames, axis=1))
    flux = np.maximum(np.diff(np.log1p(mag), axis=0), 0).sum(1)
    flux = (flux - flux.mean()) / (flux.std() + 1e-9)
    fps_env = 16000 / hop
    ac = np.correlate(flux, flux, "full")[len(flux) - 1:]
    lags = np.arange(len(ac))
    bpm = 60 * fps_env / np.maximum(lags, 1)
    ok = (bpm >= 60) & (bpm <= 180)
    best = lags[ok][np.argmax(ac[ok])]
    conf = float(ac[best] / ac[0])
    # speech: whisper (multilingual)
    from faster_whisper import WhisperModel
    model = audio_stats.model = getattr(audio_stats, "model", None) or WhisperModel("small", device="cpu", compute_type="int8")
    segs, info = model.transcribe(x, word_timestamps=False, vad_filter=True, beam_size=5)
    segs = [{"start": round(s.start, 2), "end": round(s.end, 2), "text": s.text.strip(), "no_speech_prob": round(s.no_speech_prob, 2),
             "avg_logprob": round(s.avg_logprob, 2)} for s in segs]
    speech_s = sum(s["end"] - s["start"] for s in segs if s["no_speech_prob"] < 0.5)
    return {"has_audio": True, "integrated_lufs": float(m[-1]) if m else None,
            "tempo_estimate_bpm": round(float(60 * fps_env / best), 1), "tempo_confidence_0_1": round(conf, 2),
            "tempo_note": "autocorrelation of spectral-flux onsets; may be half/double the felt tempo",
            "whisper_language": info.language, "whisper_language_prob": round(info.language_probability, 2),
            "speech_seconds_vad": round(speech_s, 1), "speech_fraction": round(speech_s / dur, 2), "transcript_segments": segs,
            "transcript_note": "Whisper output after VAD; low avg_logprob or high no_speech_prob usually means lyrics/noise, not voiceover"}


def meta(info_path):
    j = json.load(open(info_path, encoding="utf-8"))
    keep = ["id", "webpage_url", "title", "description", "uploader", "uploader_id", "channel", "upload_date", "timestamp",
            "duration", "view_count", "like_count", "comment_count", "track", "artist", "album"]
    return {k: j.get(k) for k in keep if j.get(k) is not None}


index = []
for d in sorted(p for p in LIB.iterdir() if p.is_dir()):
    v = d / "video.mp4"
    if not v.exists():
        continue
    print("==", d.name, flush=True)
    pr = probe(v)
    dur = pr["duration_s"]
    cuts = scene_cuts(v, 0.3)
    soft = [t for t in scene_cuts(v, 0.15) if all(abs(t - c) > 0.1 for c in cuts)]
    shots = [0.0] + cuts
    (d / "frames").mkdir(exist_ok=True)
    (d / "sheets").mkdir(exist_ok=True)
    for i, t in enumerate(shots):
        grab(v, min(t + 0.05, dur - 0.05), d / "frames" / f"cut_{i + 1:02d}_{t:06.2f}s.jpg")
    for s in range(int(dur) + 1):
        if s < dur:
            grab(v, s, d / "frames" / f"sec_{s:03d}.jpg")
    # contact sheets (1 fps frames, 6 per row, in time order) + cut sheet
    run([FF, "-v", "error", "-y", "-i", str(d / "frames" / "sec_%03d.jpg"), "-vf", "scale=180:-2,tile=6x3:padding=4:color=white",
         str(d / "sheets" / "sec_sheet_%02d.jpg")])
    run([FF, "-v", "error", "-y", "-pattern_type", "glob" if os.name != "nt" else "sequence", "-i", str(d / "frames" / "sec_%03d.jpg"), "-f", "null", "-"])
    lst = d / "sheets" / "_cuts.txt"
    lst.write_text("".join(f"file '{p.as_posix()}'\n" for p in sorted((d / "frames").glob("cut_*.jpg"))), encoding="utf-8")
    run([FF, "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-vf", "scale=180:-2,tile=6x3:padding=4:color=white",
         str(d / "sheets" / "cut_sheet_%02d.jpg")])
    lst.unlink()
    au = audio_stats(v, dur)
    mt = meta(d / "video.info.json") if (d / "video.info.json").exists() else {}
    json.dump(pr, open(d / "probe.json", "w", encoding="utf-8"), indent=2)
    json.dump({"threshold": 0.3, "shot_starts_s": shots, "cut_count": len(cuts), "shot_count": len(shots),
               "avg_shot_length_s": round(dur / len(shots), 2),
               "soft_change_candidates_0_15": soft,
               "note": "cut_NN frames are grabbed 0.05 s after each detected cut; soft candidates (scene 0.15-0.3) may be dissolves, fast motion or flashes"},
              open(d / "cuts.json", "w", encoding="utf-8"), indent=2)
    json.dump(au, open(d / "audio.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    json.dump(mt, open(d / "meta.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    index.append({"folder": d.name, "url": mt.get("webpage_url"), "uploader": mt.get("uploader") or mt.get("channel"),
                  "duration_s": dur, "resolution": f'{pr["width"]}x{pr["height"]}', "fps": pr["fps"], "shots": len(shots),
                  "avg_shot_s": round(dur / len(shots), 2), "tempo_estimate_bpm": au.get("tempo_estimate_bpm"),
                  "speech_fraction": au.get("speech_fraction")})
    print(json.dumps(index[-1]), flush=True)
json.dump(index, open(LIB / "index.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False)
