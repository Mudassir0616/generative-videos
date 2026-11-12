# Project history

What has been done in this workspace, what the user (Mudassir) decided and why, and what is still open. Read this
before continuing any project here. Heavy media is not in git: `docs/MEDIA.md` lists every ignored file. Per-project
detail lives next to the code (script.md, edit-plan.md, analysis.md). Newest work at the bottom.

## Before 2026-11-08: ZELECTRONICS intro (projects/zelectronics-intro)
- Brand intro for ZELECTRONICS (refurbished electronics, Mumbai). Approved final: `outputs/zelectronics-intro-v4-40s.mp4`.
- Brand rules (strict B&W, sentence case, logo SVG, Michroma wordmark) are in CLAUDE.md.

## 2026-11-08: ZELECTRONICS refurbished-laptops reel (projects/zelectronics-refurb-laptops)
1. **Draft 1 review** (31.5 s, from 2026-11-07). Problems found:
   - The hook word "expensive" was readable for only ~0.1 s.
   - The typewriter cursor sat at the line end instead of following the letters.
   - Ghost text "…ntage." lingered under "Smart is.", and the ellipse around "Smart is." was too tight.
   - The "+" of "2×+" overlapped the ring.
2. **User asked for:**
   - All fixes.
   - A few colour accents: suggested #3E77EE and #E10600. This is an exception to the strict B&W brand rule, for this reel only.
   - A real closing line instead of just "ZELECTRONICS".
3. **Draft 2:**
   - All fixes made.
   - Colour logic: red #E10600 marks the problem (expensive, ₹, gauge, price arrows, "+"); blue #3E77EE marks the solution ("aren't paying more", the refurbished pill, the "Smart is." ellipse, "certified", the end-card rule). At most one accent per scene.
   - New ending: "Shop certified refurbished laptops and desktops at ZELECTRONICS." It gets a CTA scene with laptop and desktop tiles before the end card.
   - **Voice:** the ElevenLabs MCP failed ("Free Tier access has been disabled… unusual activity"). The user then created a new voice, **Friday v2** (`ka2YlHIZtpI73mTUG5iF`), whose preview is a full read of the new script. The whole VO was switched to it (it does not exactly match Friday v1), and every scene was retimed from a Whisper word-timestamp transcript.
   - Video is 36.5 s. Delivered as `outputs/zelectronics-refurb-laptops-draft2.mp4` (committed in 973f375).
4. **Social captions** (Instagram + LinkedIn): `projects/zelectronics-refurb-laptops/social-captions.md`.
5. **Open:** ZELECTRONICS must confirm the claims "certified" (by whom), "warranty" (length) and "fraction of the price" (typical saving).

## 2026-11-08: Trending restaurant reels reference library (refrences/trending-restraunt-reels)
- Four Instagram restaurant reels downloaded with yt-dlp and analysed shot by shot with a shared template. Folders 01–04 each hold `analysis.md`, `meta.json`, `probe.json`, `cuts.json`, `audio.json` and contact `sheets/`; the videos and frames are git-ignored.
- `SUMMARY.md` holds the cross-reel patterns and a recreate-it recipe:
  - open on the room, not the food;
  - one static headline from frame 1;
  - phone footage at night under warm practicals;
  - hard cuts every 1–1.5 beats;
  - hands, not presenters;
  - no pour or cheese-pull shots;
  - loop endings;
  - "comment for location" CTAs.
- Audio was never listened to. Tempo and lyrics come from onset analysis and Whisper; track names are unknown.
- Built with `tools/prep_reels.py`. Each reel's analysis was written by a subagent and checked against its contact sheet. Two raw scene-detect counts were corrected by hand (`index.json` holds the verified numbers).

## 2026-11-08: Pukhtoon restaurant reel for The Caliph hotel (projects/pakhtoon-vid-1)
**Brief and decisions:**
- Raw footage is in `raw-footags/pakhtoon-vid-1/`: 12 clips, 4K vertical, mostly 24 fps (C075 and C096 are 30 fps), daylight, gimbal, no people except one hand. The first 8 clips came, then 4 more (exterior sign, lobby, two food clips).
- The restaurant is **"Pukhtoon"** (menu logo "p♥khtoon Restaurant", heart as the "u"; the user first wrote "Pakhtoon"). It is inside **The Caliph** hotel.
- The reel is **posted from the hotel's account**.
- **On screen** is only the Caliph logo at top centre for the whole reel, plus "Welcome To Pukhtoon" in italic calligraphy (Great Vibes) at the start. The title is removed with a transition when the food is first shown. No other text.
- **Music:** `voice/restraunt/ishqa-ve-chaddeya.mp3`, a Punjabi vocal song at ~85 BPM. Eighth notes fall every 0.3527 s from 0.101 s, with accents every 3 eighths (found with `tools/beat_grid.py`). All cuts sit on that grid.
- **Music rights warning (open):** no source or rights note exists for this song. Business accounts can't use Instagram's commercial music library, so a reel with this song baked in may get muted. The user knows; confirm before posting.

**Process:**
1. Analysis and plan first, at the user's request ("do not execute, just analyse and plan"). The plan is `projects/pakhtoon-vid-1/edit-plan.md`, modelled on reference reel 01's structure.
2. **v1 (15.04 s, 15 shots):** the walk-in (pendant lights → Caliph sign → lobby → corridor), then food, with the hero spread on the loudest part of the song and a loop ending. Grade warmed toward the references' amber, with blue casts removed (C084 window side; C149 glass table via a cyan/blue desaturation).
3. **User feedback on v1:**
   - The emblem-only logo was not readable enough, and they wanted the logo's text visible. Fix: the full logo, with the gold emblem kept and the black wordmark recoloured **white** (`tools/make_logo.py`), 500 px wide, over a soft dark top gradient.
   - "Going too fast": they asked for a slower 20 s version.
   - Delete the no-music export.
4. **v2 (20.21 s, 13 shots, the user's preferred pace):**
   - Holds of 1.06 s or 2.12 s on the song's accents (average ~1.55 s), against 0.94 s in v1.
   - Title on screen until the first food at 7.17 s.
   - Output: `outputs/pukhtoon-caliph-reel-v2-20s.mp4`.
   - v1 was re-rendered with the logo fix and later removed from `outputs/` by the user. Rebuild it with the commands in CLAUDE.md if needed.

**Rebuild pipeline:**
1. `tools/build_base.py`: ffmpeg cut list, grade and push-ins. Writes `assets/base-vN.mp4`.
2. `tools/make_comp.py vN`: writes `index.html` (logo, gradient, title, music).
3. `npx hyperframes render --fps 24 --quality delivery`.

**Possible next steps the user may ask for:**
- Reshoot at night with people (a cheers, tearing naan, a guest walking in).
- Swap in licensed music.
- A 10 s slow version (plan section 7).

## Repo housekeeping (2026-11-08)
- The GitHub repo `Mudassir0616/generative-videos` is **public**. The user asked about pushing roughly 530 MB of new media; the recommendation was to make the repo private and keep heavy and third-party media out of git.
- Added `.gitignore`, this file, `docs/MEDIA.md` (generated by `tools/media_manifest.py`) and the session's helper scripts in `tools/`.
- Earlier commits already contain some media now covered by `.gitignore` (the IShowSpeed raw clip, ZELECTRONICS renders and audio, `.hyperframes` state). Those stay tracked until someone runs `git rm --cached` on them; that's the user's decision.
- `outputs/zelectronics-refurb-laptops-draft1.mp4` and `outputs/ishowspeed-leon-reaction-9x16-cutout-33s.mp4` were deleted from disk by the user. Their deletion is not committed yet.
- **Rule from the user:** never commit or push unless explicitly asked.

## 2026-11-12: 2D motion graphics reference (refrences/2d-motion-graphics/pin-924363892282992611)
- The user asked to go through a Pinterest motion-design reel (https://www.pinterest.com/pin/924363892282992611/, "Web Rank Studio") and store it under `refrences/2d-motion-graphics/`. It sits next to the four older loose refs (ref-*.mp4) in its own folder.
- Downloaded with yt-dlp (720x1280 is the best format the pin serves), prepped with `tools/prep_reels.py` (run on a scratch folder linking to it, so no index.json was written; its frames/ and sheets/ output was then deleted), plus Whisper word timestamps in `vo_words.json`.
- `analysis.md` has the verified 12-scene table (19.27 s, ~1.6 s per scene, VO-driven kinetic type), palette (#751AA8 purple + white + black, one cream scene), type system (italic didone pairs + grey ghost echo words), the transition vocabulary, and HyperFrames recreate notes including how to map it to ZELECTRONICS.
- Audio was not listened to; the bed/whoosh notes come from level measurements.
- **User feedback:** don't keep captured frames or contact sheets for references. Analyse the motion graphics and keep only the written context (analysis.md + small JSON). Frames/sheets were deleted. More 2D motion graphics references are coming.
- **2026-11-12, three more refs** (same folder, `pin-901986631645535447` InsiderForce "3 Claude Code skills" 60.7 s, `pin-933230354043913635` MotionDesigners.Pro Instagram-growth pitch 17.9 s, `pin-1061653312177886416` Solution Wagon agency pitch 35.8 s). Each has `analysis.md` + `vo_words.json` + data JSONs, no frames. Analysed by three parallel subagents (frames only in the scratchpad, deleted after); subagents can't write .md files, so their text was saved by the main session; one transition claim per ref was spot-checked by eye. `refrences/2d-motion-graphics/SUMMARY.md` compares all four and says which fit ZELECTRONICS (Solution Wagon and InsiderForce are closest to the B&W brand). The loose older `ref-*.mp4` files in that folder are still unanalysed.

## 2026-11-12: ZELECTRONICS 2D motion graphics script series (projects/zelectronics-motion-scripts)
- The user asked for research on the current Indian IT hardware market and scripts for ZELECTRONICS based on the 2D motion graphics theme.
- `market-research.md`: sourced fact table (memory shortage and RAM 2.5–3×, laptop price hikes, IDC Q2 2026 India +12.1% with SMB +21%, refurbished "breakout year", Cashify 65–70% business demand, Windows 10 end of support + CERT-In, e-waste), what it means for messaging, and the list of claims ZELECTRONICS must confirm.
- `scripts.md`: 5 scripts (the memory tax; Windows 10 is over; ten desks; refurbished isn't used; one less on the pile), each with VO, a shot table and a motion style taken from one analysed reference in refrences/2d-motion-graphics/, all mapped to strict B&W brand rules. Draft 1, not yet reviewed by the user or client; VO not recorded.
- **2026-11-12, script 4 refined:** the user asked to make "Refurbished isn't used" punchy but professional. Draft 2 is 42 words and ~20 s (was 55 words, ~24 s), opens on the contrast "Used is sold as it is. / Refurbished is fixed first.", gives the four process words their own white/black flips, and adds a VO delivery note. Claim placeholders ([N] checks, [12-month] warranty) are unchanged.
- **2026-11-12, script 4 draft 3:** the user said draft 2 "sounds like AI generated" and wants it to sound like a real pitch, with long sentences. Draft 3 is a conversational 102-word, ~42 s pitch (admits the "old laptop with a fresh sticker" doubt, then explains testing, honest advice and warranty, then "talk to us"). Visuals change at clause breaks, and captions show one clause at a time.
- **2026-11-12, script 4 draft 4:** the user liked the natural pitch but found it "too much talking". They gave two facts: ZELECTRONICS tests the refurbished laptops before shipping, and they ship with a **6-month warranty**. Draft 4 is 54 words and ~26 s: the "fresh sticker" doubt, then tested part by part before we ship it with a six-month warranty, then "talk to us". The warranty is now recorded in market-research.md §3.
- **2026-11-12, script 4 draft 5:** the user supplied the final wording ("…we test every laptop before we ship it to your doorstep, and it comes to you with a six-month warranty…"). Only two fixes were made: the missing "laptop" was added, and "door steps" became "doorstep". 48 words, ~24 s; the battery/storage scene was removed and a doorstep delivery scene added.

## 2026-11-12: Script 4 video v1 (projects/zelectronics-script4-refurbished)
- The user asked to produce script 4 ("Refurbished isn't used", draft 5 wording) as a 2D motion graphics video in the style of the Pinterest references. VO: `voice/zelectronics-script-4.mp3` (16.2 s, supplied by the user), copied to `assets/vo-script4.mp3` and placed at +0.2 s. Whisper word times are in `assets/vo_words.json` (whisper hears "ZELECTRONICS" as "Adds electronics").
- **Palette set by the user for this video** (an exception to the strict B&W brand rule): background #F1E9D8, graphics/accents #D8BD8A and #B18A45, primary text #111111. Gold is not used for text (too low contrast on cream).
- Built as one HyperFrames composition (20.4 s, 1080x1920, 30 fps). All graphics are hand-drawn SVGs: worn laptop + "Like new!" sticker → shrink to dot → clean laptop with the ZE screen, exploded into battery/storage/memory/processor cards with ticks → laptop into a "Tested ✓" box that slides to a door → gold-edged iris → a six-month warranty shield rising from the box → a "New laptop ₹" tag on a rising price line, struck and dropped on "talk to us" → phone pill → end card.
- Reference mapping: captions build word by word from sand to ink (InsiderForce) with a highlighter bar under the key phrase; one metaphor and a different transition per scene (Web Rank Studio: push, shrink to dot, slide, iris, blur, zoom); persistent plate of dashed grid, rotating four-point stars and a small ZE tile (Solution Wagon).
- Audio: `tools/make_audio.py assets/vo-script4.mp3 assets/audio.wav` (synth bed + SFX; cue times must match index.html). `hyperframes check` passes; the remaining contrast warnings are only for the decorative ghost word and quote marks.
- Output: `outputs/zelectronics-script4-refurbished-v1-20s.mp4`. Rebuild: `python tools/make_audio.py ...` then `npx hyperframes render --fps 30 --quality delivery -o ../../outputs/zelectronics-script4-refurbished-v1-20s.mp4` (Node 22).
