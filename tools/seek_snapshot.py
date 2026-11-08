"""Screenshot a HyperFrames index.html at given times WITHOUT HyperFrames (headless Chrome + seek harness).
Handy when Node 22 is unavailable. usage: python tools/seek_snapshot.py <project_dir> <out_dir> t1 t2 ...
It hides clips outside their data-start/data-duration window and calls __timelines.main.seek(t). JS onUpdate counters may not refresh."""
# usage: python mkshot.py <project_dir> <out_dir> t1 t2 ...  -> harness html per time + screenshot via headless Chrome
import sys, subprocess, pathlib, re
proj = pathlib.Path(sys.argv[1]).resolve(); out = pathlib.Path(sys.argv[2]).resolve(); times = sys.argv[3:]
src = (proj / "index.html").read_text(encoding="utf-8")
base = '<base href="' + proj.as_uri() + '/">'
chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
for t in times:
    hook = """<script>
document.fonts.ready.then(() => { const t = %s;
  document.querySelectorAll('.clip[data-start]').forEach(el => { const s = +el.dataset.start, d = +el.dataset.duration;
    el.style.visibility = (t >= s && t < s + d) ? 'visible' : 'hidden'; });
  window.__timelines.main.seek(t); });
</script>""" % t
    html = src.replace("<head>", "<head>" + base, 1).replace("</body>", hook + "</body>")
    h = out / f"h_{t}.html"; h.write_text(html, encoding="utf-8")
    png = out / f"s_{t}.png"
    subprocess.run([chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--allow-file-access-from-files",
                    "--window-size=1080,1920", "--virtual-time-budget=6000", f"--screenshot={png}", h.as_uri()],
                   capture_output=True, timeout=90)
    print(t, png.exists())
