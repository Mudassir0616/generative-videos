# 2D motion graphics ref — Web Rank Studio, "Power of motion design" (Pinterest 924363892282992611)
https://www.pinterest.com/pin/924363892282992611/ · uploader "Web Rank Studio" · pin date 2025-12-21 · 3,613 saves (repost_count) · 19.27 s · 720x1280 (9:16), 30 fps, H.264 + AAC (best format Pinterest serves; a 1080p master does not exist on the pin)

Files here: `video.mp4` (git-ignored), `probe.json`, `cuts.json`, `audio.json`, `meta.json`, `vo_words.json` (Whisper word timestamps). Built with `tools/prep_reels.py` plus 4 fps and 30 fps frame bursts checked by eye. Per the user, no frames or contact sheets are kept: this file is the record of the motion graphics.

## Overview
- **What it is:** a self-promo for motion design. Voice-over driven kinetic typography + 2D collage (photo cut-outs and stock 3D renders on flat colour), one idea per VO line. No people on camera.
- **Script (VO, Whisper, 6 sentences, 49 words):** "Ever wondered why some brands just stick in your mind? It's no accident. It's the power of motion design. Motion brings feeling to your story. Animated text captures eyes instantly. Visual metaphors make complicated concepts clear silently. This isn't decoration. It's strategic movement." The voice reads like an AI/TTS narrator: even pace, about 2.6 words/s, sentence gaps of 0.4–1.0 s.
- **Structure:** hook question (0–3 s) → reframe "it's no accident" → claim "motion design" → 4 benefits, one scene each → "this isn't decoration / it's strategic movement" → studio end card. 12 scenes in 19.27 s, **average 1.6 s per scene**. The longest is the chart scene (3.8 s), the shortest "Motion bring" (0.6 s).
- **Audio:** VO at about −14 LUFS integrated with a quiet bed under it (the gaps between sentences sit at −20 to −28 dB RMS, not silence) and a whoosh-like bump at the 6.1 s whip (−17 dB in a VO gap). The bed nearly drops out at 16.2–16.5 s (−44 dB) just before "strategic", a short pause for emphasis. I did not listen to it; music genre and SFX are inferred from levels only.

## Look
- **Palette (measured):** one brand purple **#751AA8** (solid backgrounds, label boxes, accent words), white backgrounds, black text, one cream scene **#F6F0E4** (TV scene). On purple backgrounds the accent words use a lighter, semi-transparent tint of the same purple/lavender. Everything else is the natural colour of the cut-out objects.
- **Background rhythm:** white → purple → white → purple, alternating almost every scene: W W W P W W Cream P W W/P-split P W. The colour flip is itself the transition beat.
- **Type:**
  - Main: a high-contrast didone serif in **italic**, bold for the key word and regular for the lead-in word (looks like Playfair Display Italic / Bold Italic). Pairs are stacked and slightly overlapping: small lead-in word above, big key word below ("stick in / *your mind?*", "it's no / *Accident*", "*Motion* / Design", "this isn't / *Decoration*").
  - Accent word in purple, the other word in black (on white) or white (on purple).
  - Only the opening uses a condensed sans in caps (looks like Bebas Neue / Oswald): "EVER WONDERED?" white on a purple label box, "SOME BRANDS" in purple.
  - **Ghost echo text:** the key word repeated huge in light grey (about 15% black), cropped off the frame edge behind the subject ("your", "Motion Design").
  - One rotated line: "Motion" set vertical (90° CCW) filling the frame height, with "bring" beside it. Note the typo: the VO says "brings".
  - Tiny subtitle-style caption at the bottom of the chart scene ("make complicated concepts clear").
- **Imagery (all cut-outs with soft drop shadows):** halftone B&W brain with a purple circle over it, a realistic pink brain, eyeballs with purple irises, purple 3D comedy/tragedy masks, a red retro TV on a wooden stand, a Corinthian column with a floating diamond, a white 3D chess king, a flat vector illustration (man slipping by a wet-floor sign), a vertical card of stock footage (glowing line chart on a perspective grid), product photos in rounded purple tiles (sneaker, iPhone, camera lens, McDonald's).
- **Decoration:** a faint square grid on some white and purple backgrounds; white "starburst" shards (sharp triangular spikes) in the top-right and bottom-left corners of the purple scenes; orbiting dashed rings with black dots in the opener; a mouse cursor clicking the words "Motion Design".
- **Layout:** text in the top third, object centre/bottom. Objects are often cropped by the frame edge (eyeball, masks, chess king) so the frame feels full and big.

## Scene-by-scene (times from 4 fps and 30 fps frame bursts; VO words from vo_words.json)
| # | Time | VO | Background | On screen | In / animation | Out |
|---|---|---|---|---|---|---|
| 1 | 0.00–0.93 | "Ever wondered" (0.00) | White | "EVER WONDERED?" white caps on purple label box; halftone brain cut-out with a purple circle; two dashed orbit rings with black dots | Brain blurs/scales in; orbit rings shrink inward and rotate (0.25–0.5 s) | Brain collapses into the purple circle, which shrinks to nothing (0.8–0.93); label fades |
| 2 | 1.00–1.6 | "why some brands" (0.88–1.34) | White | 2x2 grid of rounded purple tiles with product photos; "SOME BRANDS" purple caps | **Zoom-out**: grid starts about 3x size filling the frame and settles in 0.3 s (1.0–1.3), landing just before "brands" | Fades to a ghost (1.5) |
| 3 | 1.65–2.95 | "just stick in your mind?" (1.80–2.54) | White + faint grid | "stick in" purple italic over "your mind?" black bold italic; pink brain; huge grey ghost "stic / your" | Text and brain pop in over the fading grid | Everything **slides up and out** (2.95–3.05); one white frame |
| 4 | 3.1–4.25 | "It's no accident." (3.42–3.70) | Purple (fades in from white in about 0.15 s) | Vector illustration of a man slipping; "it's no" white italic; "Accident" big bold italic lavender; starburst top-right | Illustration first, then the words; "Accident" lands about 0.3 s before it is spoken | **Push left**: the whole frame slides out left (4.15–4.25) |
| 5 | 4.25–6.15 | "It's the power of motion design." (4.64–5.60) | Purple → white cross-fade (0.1 s) + grid | Big eyeball slides in from the right edge, small one top-left; "Motion" purple bold italic / "Design" black italic; cursor clicks; giant grey ghost "Motion Design" | Words write on (4.5–4.9), fully on screen by 5.0, before the VO says them at 5.34 | Fast push left (6.1–6.17) |
| 6 | 6.17–6.75 | "Motion brings" (6.50–6.86) | White + grid | Vertical "Motion" black bold italic, "bring" purple; purple 3D masks top-left and bottom-right | Snaps in on the whip with the whoosh | Hard change |
| 7 | 6.77–8.45 | "feeling to your story." (7.28–8.04) | Cream #F6F0E4 | Red retro TV on a stand; "Feelings" purple bold italic / "to your" small / "Story" black bold italic typed on | TV screen cycles short clips every 0.25–0.5 s (hand with a card, landscape, hand, food) | **Circle wipe**: a purple disc grows out of the TV screen and fills the frame (8.33–8.5) |
| 8 | 8.5–10.85 | "Animated text captures eyes instantly." (8.74–10.28) | Purple + faint grid; starbursts top-right and bottom-left | "Animated" small italic, "text" huge bold italic white with an eyeball overlapping it, "Captures" / "Eyes" / "instantly" staggered | **Word-by-word build synced to the VO** | Dissolve: purple lightens to white over about 0.35 s (10.75–11.1) |
| 9 | 10.95–14.75 | "Visual metaphors make complicated concepts clear silently." (11.28–14.0) | White | Vertical rounded card of stock footage (glowing cyan line chart on a perspective grid, rising) with drop shadow; "Visual" purple bold / "metaphors" black italic; tiny caption at the bottom | Card scales up and fades in; the footage keeps moving for 3.8 s | Card and title **slide up out**; a purple block rises from the bottom to about 25% height (14.6–14.75) |
| 10 | 14.75–16.15 | "This isn't decoration." (15.12–15.58) | White top, purple bottom block | "this isn't" black italic, "Decoration" purple bold italic (blur/fade in); Corinthian column with a diamond dropping on top | Words in order (14.9, then 15.1); diamond drops in 15.1–15.25 | Slide left (16.1–16.2) |
| 11 | 16.25–17.9 | "It's strategic movement." (16.60–17.22) | Purple (fades in from white in 0.1 s); starburst top-right | "it's" / "Strategic" white italic, "Movement." lavender bold italic; white 3D chess king rises from the bottom and scales up past the words | King rises 16.5–17.0 | Text fades out (17.5–17.75), king drops, then a **hard cut to white** at 17.9 |
| 12 | 17.9–19.27 | — | White | End card: "Web Rank Studio" purple italic on 3 lines, "all right reserved" small grey italic; tiny watermark bottom centre | Fades in 18.0–18.25 | Starts fading at 18.75 |

`cuts.json` (scene threshold 0.3) finds only 8 of these changes. The fades and colour flips sit in `soft_change_candidates_0_15`. The table above is the verified list.

## Motion language
- **Visual leads the VO by 0.2–0.4 s:** each scene changes in the gap before its sentence, and the key word is on screen just before it is spoken. Every scene change falls in a VO pause (3.0, 4.25, 6.17, 8.45, 10.9, 14.7, 16.2, 17.9).
- **Transitions are short, 0.1–0.35 s,** and vary on purpose: shrink-to-dot, zoom-out, slide up, push left, colour cross-fade, circle wipe from an object, dissolve, rising colour block, hard cut. Never the same one twice in a row.
- **Within a scene:** a 2–3 step stagger (object, then lead-in word, then key word), then a hold. Small continuous life during the hold: the eyeball looks around, footage plays inside the TV and the card, orbit rings turn.
- **Easing:** fast-in, soft-settle (strong ease-out). I saw no clear overshoot or bounce in the 30 fps strips.
- **Metaphor per line:** brain = memory, slipping man = "accident", eyeball = attention, masks = feeling, TV = story, chart = clarity, column + diamond = "not decoration", chess king = strategy.

## Recreate-it notes (HyperFrames)
- 1080x1920, 30 fps. Two-colour system: one brand colour + white, with black type. Alternate the background colour scene by scene.
- Type kit: an italic didone (Playfair Display Italic 400/800) for all lines, lead-in word small and regular, key word large and bold, overlapping by about 20% of the line height. Add a giant 15%-grey ghost copy of the key word cropped off the edge. Use one condensed caps sans only for a label box in the hook.
- Assets: background-removed PNG cut-outs with `drop-shadow`, one per sentence, cropped by the frame edge. Add a faint 60–80 px grid and corner starburst shards on brand-colour scenes.
- Timing: transcribe the VO with word timestamps (as here), change the scene about 0.3 s before each sentence starts, and bring the key word in about 0.2 s before it is spoken.
- For ZELECTRONICS, map the purple to black (or to the reel's red/blue accent rule) and the italic didone to Instrument Serif Italic. The ref capitalises key words ("Accident", "Decoration"); ZELECTRONICS copy must stay sentence case.
