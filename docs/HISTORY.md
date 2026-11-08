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
