"""Word-timestamped Whisper transcript of any audio/video (multilingual 'small' model). Used for VO cue times and song lyrics.
usage: python tools/transcribe.py <media>   (needs faster-whisper, numpy, ffmpeg)"""
import sys
sys.stdout.reconfigure(encoding="utf-8")
import subprocess, numpy as np
from faster_whisper import WhisperModel
x=np.frombuffer(subprocess.run(["ffmpeg","-v","error","-i",sys.argv[1],"-ac","1","-ar","16000","-f","f32le","-"],capture_output=True).stdout,np.float32)
m=WhisperModel("small",device="cpu",compute_type="int8")
segs,info=m.transcribe(x,word_timestamps=True,beam_size=5)
print("lang",info.language,round(info.language_probability,2))
for s in segs: print(f"{s.start:.2f}-{s.end:.2f} nsp={s.no_speech_prob:.2f} :: "+" ".join(f"{w.word.strip()}@{w.start:.2f}" for w in s.words))
