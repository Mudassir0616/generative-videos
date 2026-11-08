"""Find the beat grid of a music file (onsets in low/full bands + a fitted period). Used for voice/restraunt/ishqa-ve-chaddeya.mp3:
result was eighths every 0.3527 s from 0.101 s (~85 BPM), accents every 3 eighths. usage: python tools/beat_grid.py <audio> [site_dir]"""
import sys, pathlib
if len(sys.argv) > 2 and pathlib.Path(sys.argv[2]).is_dir(): sys.path.insert(0, sys.argv[2])  # optional extra site-packages dir
import subprocess, numpy as np
SR=22050
x=np.frombuffer(subprocess.run(["ffmpeg","-v","error","-i",sys.argv[1],"-ac","1","-ar",str(SR),"-f","f32le","-"],capture_output=True).stdout,np.float32).astype(float)
hop,win=128,1024; fe=SR/hop
fr=np.lib.stride_tricks.sliding_window_view(x,win)[::hop]*np.hanning(win)
mag=np.abs(np.fft.rfft(fr,axis=1)); f=np.fft.rfftfreq(win,1/SR)
def flux(band):
    m=mag[:,(f>=band[0])&(f<band[1])]; v=np.maximum(np.diff(np.log1p(m),axis=0),0).sum(1); return (v-v.mean())/(v.std()+1e-9)
low=flux((30,200)); full=flux((30,11000))
def peaks(v,th):
    return [(i/fe,v[i]) for i in range(2,len(v)-2) if v[i]==v[i-2:i+3].max() and v[i]>th]
print("LOW (kick/dhol) onsets z>2:", " ".join(f"{t:.2f}({z:.0f})" for t,z in peaks(low,2)))
print("FULL onsets 0-6s z>1.5:", " ".join(f"{t:.2f}({z:.1f})" for t,z in peaks(full,1.5) if t<6))
# grid fit on full strong onsets after 5s
P=[t for t,z in peaks(full,2.5)]
best=None
for per in np.arange(1.040,1.075,0.0005):
  for off in np.arange(0,per,0.005):
    g=np.arange(off,21.3,per); err=np.mean([np.min(np.abs(g-t)) for t in P if t>4.9])
    if best is None or err<best[0]: best=(err,per,off)
print("grid fit (t>4.9s): period %.4f offset %.3f mean err %.3f"%(best[1],best[2],best[0]))
g=np.arange(best[2],21.3,best[1]); print("grid hits:", " ".join(f"{t:.3f}" for t in g))
