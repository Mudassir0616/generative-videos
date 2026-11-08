# Reel 03 — सृषा (DbVrVh3Bm0L)
https://www.instagram.com/p/DbVrVh3Bm0L/ · account "सृषा" (@srush_stories) · uploaded 2026-07-28 · 9.94 s · 1080x1920 (9:16), 30 fps, VP9 · 11,131 likes / 60 comments

## Overview
- **Hook (0:00–0:03):** the reel opens on a dark, moody wide of Nur Cafe's interior (pendant lamps, exposed brick, diners in silhouette). From frame 0 the venue logo "nur CAFE" and a yellow handwritten "chalein?" ("shall we go?") sit centred on screen. Nothing animates. The hook is the invitation plus the old-school atmosphere. At 0:01.27 it cuts to a bright, warm, high-angle shot of the heritage menu, a jump from roughly 37 to 100 in mean luma (signalstats YAVG). That brightness jump is the second beat of the hook.
- **Total duration:** 9.937 s (ffprobe), 298 frames.
- **Shots:** 4 real shots, plus a 2-frame (0.07 s) black tail where only the overlay remains. cuts.json lists 5 shots because it counts the tail.
- **Average shot length:** 2.47 s across the 4 real shots (9.867 s / 4). cuts.json gives 1.99 s because it includes the tail.
- **Narrative arc:** a "come with me" visit in four beats: the room (ambience), then the menu on the table with the creator's phone and sunglasses (arrival/ordering), then the food spread of seekh kebabs, chicken tikka and nihari (payoff), then retro soda bottles with diners behind (lingering/social close). There is no on-screen person and no talking. The caption "Hum kab?" ("when are we going?") turns it into a tag-a-friend prompt.

## Shot-by-shot table
| # | Timecode | Shot size (ECU/CU/MS/WS) | Angle | Camera motion | Subject | Purpose |
|---|---|---|---|---|---|---|
| 1 | 0:00.00–0:01.27 | WS | Low angle, looking up at the ceiling beams and pendant lamps, brick wall and seated diners in the lower third | Handheld, near-static (very slight sway; first and last frames almost identical) | Dim heritage interior of Nur Cafe: 3 glass pendant lamps, wooden beams, exposed brick, framed pictures, silhouetted diners | Establish the venue and its old-school mood; carries the logo + "chalein?" invitation |
| 2 | 0:01.27–0:04.40 | MS (tabletop) | High angle, about 45°, Dutch-tilted (menu runs diagonally) | Handheld drift left, slow, with a slight clockwise arc (the phone and sunglasses slide right in frame, the menu rotates a little) | Printed "HERITAGE • FOOD • CULTURE" menu (All Day Nashta, Special Kebab & Rolls, Nur Biryani), a dark-blue iPhone and black sunglasses on a wooden table | "We've arrived and are ordering"; shows the menu prices and dishes to save |
| 3 | 0:04.40–0:08.80 | CU to MS | High angle, about 50–60°, looking down across two plates | Orbit/arc right, slow (about 4.4 s, handheld). The tikka plate slides left, and a bowl of nihari/curry with a steel spoon is revealed from the right edge from about 0:05.4 | Seekh kebabs on naan with coriander, a curd katori, lemon wedge, onion rings and spiced potatoes; chicken tikka on naan with green chutney and onion; a brown paper bag of breads top-left; then a nihari bowl | Food payoff, the longest shot (44% of runtime). The arc reveals more dishes, which makes the spread feel abundant |
| 4 | 0:08.80–0:09.87 | MS | Eye level, table height (lens at bottle height) | Handheld, near-static | Three vintage soda bottles on a steel table: a green marble-neck "Fresh Co" bottle with yellow soda, another with red soda, and a red "Pallonji's" raspberry bottle. Blurred diners and a stone/brick wall behind | Closing "vibe" shot: the retro Bombay drink plus people enjoying themselves; a strong colour pop (red) |
| — | 0:09.87–0:09.94 | — | — | — | Black frame with the overlay only (2 frames) | End of the clip under the persistent overlay; Instagram loops back to shot 1 |

Verification: an ffmpeg scene score pass at threshold 0.05 found only the four changes at 1.267 / 4.4 / 8.8 / 9.867 s (scores 0.72 / 0.48 / 0.42 / 0.77). There are no soft changes, so no hidden dissolves, whips or flashes. All transitions are hard cuts. The difference from cuts.json is interpretive: the fifth "shot" is a 0.07 s black tail, not footage.

## Cinematography
- **Lens feel:** a smartphone main camera, wide to normal (roughly 24–28 mm equivalent, visual judgement). There is no macro and no ultra-wide distortion.
- **Depth of field:** mostly deep, as phone footage is, except:
  - Shot 2: the far end of the wooden table at the top of the frame falls soft.
  - Shot 4: the bottles are sharp and the diners and wall behind are clearly soft. This could be the phone's natural falloff at close focus or a portrait/cinematic mode (uncertain).
- **Focus pulls:** no rack focus seen.
- **Framing:**
  - Shot 1 is loosely centred, with the lamps in the upper third.
  - Shots 2–3 are diagonal tabletop compositions, with the menu and plates running bottom-left to top-right.
  - Shot 4 lines the three bottles up as a left-to-right row, with the tallest red bottle on the right third.
  - The central band of the frame, about 47–64% of the height, is always covered by the overlay. Subjects are framed around it rather than under it: the kebabs sit below it, and the tikka and nihari sit above and to the side.
- **Aspect ratio:** native 9:16 vertical, 1080x1920.
- **Frame rate:** 30 fps (ffprobe). Motion looks real-time. No slow-mo or speed ramp is visible: bursts at 3–8 fps show smooth, even drift.

## Lighting & color
- **Light sources:** all available light.
  - Shot 1: warm tungsten pendant practicals against a near-black ceiling. Low key, with lamp bloom and a slight lens flare streak.
  - Shots 2–4: the cafe's warm overhead lighting. It throws visible specular hotspots on the steel table and plates (shot 3, top centre) and on the sunglasses lenses (shot 2), so the light comes from above and slightly in front.
- **Contrast:**
  - Shot 1 is crushed dark: RGB mean about 21/255, 5th/95th percentile luma 1/56 (measured).
  - Shots 2–4 are mid-key at about 87–90 mean, with a 5th/95th percentile range of roughly 8–19 up to 149–190.
  - The dark-to-bright jump at the first cut is a deliberate contrast beat.
- **Measured palette** (k-means on mid-shot frames, overlay area masked):
  - Shot 1 interior: #050104 (35%), #130b0a, #211916, #312a29, lamp highlight #ded3c6. Median #130c0b.
  - Shot 2 menu/table: menu paper #a58f81 and #937c70, wood #48311e / #624b3b, phone/shadow #100e13. Median #6e594b.
  - Shot 3 food: kebab/char browns #462d1b and #27160d, gravy/tikka #6a4c33 and #937350, naan/curd/steel #a2938b and #cdc1bb. Median #64462e.
  - Shot 4 bottles: wood/brick #63422a, #36190e and #88674d, stone wall #ab8e70 and #d0bba0, raspberry soda red #8e1a0c (9%). Median #7c4d37.
  - Overlay: logo white about #fbf8fb, "chalein?" yellow about #f4f911 (measured on the black tail frame).
- **Grade:** warm, natural phone processing (amber/brown dominant, no teal-orange split). Saturation is moderate: mean HSV-style saturation 0.39 (menu), 0.46 (food), 0.54 (bottles). There is no visible film grain, vignette or heavy LUT. The only cool or neon element is the acid-yellow text.

## Styling
- **Food:**
  - The food is served as the restaurant plates it, not restyled. Seekh kebabs (4 visible) sit on naan with a coriander scatter, a steel katori of curd, a lemon wedge, raw onion rings and spice-dusted potato halves.
  - Chicken tikka with charred edges sits on naan with a green-chutney katori, onion and lemon.
  - Nihari or a similar gravy comes in a steel bowl with a serving spoon and a coriander garnish.
  - Breads come in a branded brown paper bag.
  - There is no steam, sizzle, pour or pull moment (none visible).
- **Props:**
  - The creator's dark-blue iPhone (Pro, triple camera) and chunky black sunglasses on the menu. This is a lifestyle "my table" cue.
  - The vintage marble-neck soda bottles (Fresh Co, Pallonji's "Estd. 1865"), which are an Irani-cafe/old-Bombay signifier.
- **Venue:** steel-topped and wooden tables, cane-back chairs, exposed brick and stone walls, dark wood beams, vintage glass pendant lamps. This matches the "heritage cafe / vintage vibes / old school" tags.
- **People:** no hands or presenter on camera. Diners appear only as soft background silhouettes (shots 1 and 4). Wardrobe is not applicable.

## Editing & pacing
- **Cut rhythm:** shot lengths are 1.27 s, 3.13 s, 4.40 s and 1.07 s. That is a short opener, two lengthening shots that let the menu and food breathe, and a quick closer. Pacing is relaxed for a reel (2.47 s average).
- **Transitions:** 3 hard cuts, then a hard cut to black for 2 frames. There are no whips, zooms, flashes or dissolves (scene scores confirm none below 0.3).
- **Speed ramps:** none.
- **Beat-sync:** not evident.
  - audio.json estimates 79.8 BPM (confidence 0.25), a beat every 0.752 s. Cuts fall at 1.68, 5.85 and 11.70 beats from 0. Measured from the first cut, the later cuts land at 4.17 and 10.02 beats, which is near-grid but inconsistent.
  - The 4.40 s cut lands about 0.22 s after the Whisper lyric-phrase boundary at 4.18 s. The edit may follow the song's lyric phrasing more than its beat (uncertain).
- **Loop/ending:** the footage ends at 0:09.87 under a persistent overlay, then 2 black frames. Instagram loops straight back to the dark interior shot. Bright-to-dark makes a soft "reset" rather than a seamless loop.

## Text & audio
- **On-screen text:** a static branded overlay, identical on every frame from 0:00.00 to 0:09.94. It does not animate in or out.
  - Venue logo "nur" with "CAFE" in small tracked caps underneath and a ™ mark, in white (about #fbf8fb). It is a stylised high-contrast wordmark, and the "u" carries a dot that evokes Urdu script.
  - "chalein?" in lowercase acid yellow (about #f4f911), a brush/handwritten script sitting just under the logo. "Chalein?" is Hinglish for "shall we go?".
  - The logo and "chalein?" block spans y ≈ 911–1221 px (47–64% of the height) and x ≈ 368–676 px, so it is centred, slightly left of centre (measured on the black tail frame).
  - A tiny creator watermark, "stories by | सृषा", in thin white sans with the name in Devanagari, sits at about 83% of the frame height, centred.
- **Caption (not on screen):** "Hum kab?" followed by hashtags and keyword tags (seekh kebabs, Nur Cafe, Fort, rains, chai, bun maska, old school, and others).
- **Voiceover vs music:**
  - There is no voiceover. Whisper returns English song lyrics across the full duration: "Baby, come stand by my side" (0.18–4.18 s) and "Come and be my guiding light on my way" (4.18–10.18 s). The segments are long and evenly sized, with no_speech_prob 0.36, avg_logprob -0.43 and language probability 0.69. Together with the absence of any on-camera speaker, this points to a sung music track rather than spoken VO.
  - No ASMR or ambient restaurant sound is evident from the data (uncertain).
- **Music:** the track name is not in the metadata (uncertain). The lyrics suggest a slow romantic/soulful song; the mood is otherwise uncertain. The tempo estimate is about 80 BPM; the felt tempo could be about 160 (uncertain).
- **Loudness:** integrated loudness is -14.2 LUFS, a normal platform level.
- **Sound effects:** none detectable.

## Why it works
1. **The invitation is the hook, and it never leaves the screen.** The centred logo and the yellow "chalein?" are on screen from frame 0. With the caption "Hum kab?", the reel reads as a question to a friend, which drives shares and tags. The 60 comments against 11k likes fit a tag-a-friend pattern (inference).
2. **The dark-to-bright opening contrast.** The 1.27 s low-key wide of pendant lamps and brick (luma about 37) cuts to a warm, bright tabletop (luma about 100) at 0:01.27. Mood and venue are established, then the viewer is pulled into the table within the first 1.5 s.
3. **It is authentic, savable information on a short runtime.** The menu with readable prices (0:01.27–0:04.40) and an honest, unstyled food spread revealed by a slow arc (0:04.40–0:08.80) are useful to anyone planning a visit. The retro soda close (0:08.80) adds the "old Bombay" nostalgia the hashtags target. Under 10 s means high completion and replays.

## Recreate it
1. **Gear:** a phone only (main 1x lens), with no gimbal needed; steady handheld is enough. Shoot 4K or 1080p at 30 fps with no slow-mo. Lock exposure on the bright shots so highlights on the steel tables don't clip. Shoot at golden hour or night for warm practicals.
2. **Shot 1 (about 1.3 s):** a low-angle wide toward the ceiling lamps and wall, with diners in silhouette. Hold almost still and expose for the lamps, so the room falls nearly black.
3. **Shot 2 (about 3.1 s):** a 45° high-angle shot of the printed menu, angled diagonally, with your phone and sunglasses placed on top-left. Drift the camera slowly left with a slight rotation.
4. **Shot 3 (about 4.4 s):** a 50–60° high-angle shot of two loaded plates (kebabs plus tikka on naan, with katoris of curd and chutney). Do a slow arc right that reveals a third dish (a gravy bowl with a spoon) entering from the right edge. Keep the main dish below the frame centre so the overlay doesn't cover it.
5. **Shot 4 (about 1.1 s):** a table-height static shot of a row of retro soda bottles, with diners blurred behind. Use portrait/cinematic mode or close focus to soften the background.
6. **Edit:** use hard cuts only, in this order. Put a 2-frame black tail at the end, keeping the overlay. Do not ramp the speed.
7. **Grade:** keep the phone's warm, natural look. Crush shot 1 to near black (median about #130c0b) and keep shots 2–4 at a warm brown median of about #64462e to #7c4d37.
8. **Overlay for the full duration, no animation:**
   - The venue logo in white (about #fbf8fb), centred at about 47–57% of the height, roughly 300 px wide on a 1080 frame.
   - Beneath it, a one-word Hinglish question in a yellow (#f4f911) brush script, about 210 px wide.
   - A tiny "stories by | <name>" watermark at about 83% of the height.
9. **Audio and caption:** use a slow (about 80 BPM) English lyric track with no voiceover. Cut on lyric phrases rather than strict beats. Caption with a short question that prompts tagging (for example "Hum kab?") plus location and food keywords.
