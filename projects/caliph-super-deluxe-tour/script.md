# The Caliph: Super Deluxe Room tour (on-screen script)

Source: `raw-footags/rooms/super-deluxe-tour.mp4` (720x1280, 24 fps, 30.21 s, no audio).
Room facts: https://thecaliphhotel.com/room/super-deluxe-room-2 (scraped 2026-11-25).
No voiceover. All information is on-screen text, so each scene has one short line (plus an optional small sub-line), and every transition is a slow 1 s cross-dissolve.

## 1. What the footage shows

The raw video is 5 smooth gimbal shots, each exactly 6.04 s, joined with hard cuts.

| Shot | Source time | What we see | Camera |
|---|---|---|---|
| A | 0.00–6.04 | The door swings open to reveal the whole room: bed with red runner, lattice panels, wall lamps, armchair and round table. | Slow push in through the doorway |
| B | 6.04–12.08 | Close on the king bed, then across to the gold full-length curtains, the armchairs and the work chair/desk. | Slow pan left |
| C | 12.08–18.13 | Close-up of the headboard: cushions, round wall lamp, white geometric lattice panel. | Slow slide right |
| D | 18.13–24.17 | From the armchairs and curtains across the work desk (water bottles, kettle, tea tray), the mirror and the wall TV. | Slow pan right |
| E | 24.17–30.21 | The wooden vanity/wardrobe unit with its mirror and the mini-fridge. | Slow push in |

**Not in the footage** (so not on screen): the bathroom, bathtub, marble fittings, toiletries, bathrobe and "separate living room". The website's "310 m²" is almost certainly a typo (maybe 310 sq ft), so the video gives no room size.

## 2. Edit timeline (≈30 s)

The shots overlap by 1 s for the dissolves, so the footage runs 26.2 s; then an end card holds for about 4 s.

| Output time | Picture | Transition in |
|---|---|---|
| 0.00–6.04 | Shot A | Fade up from black (0.6 s) |
| 5.04–11.08 | Shot B | 1.0 s cross-dissolve |
| 10.08–16.13 | Shot C | 1.0 s cross-dissolve |
| 15.13–21.17 | Shot D | 1.0 s cross-dissolve |
| 20.17–26.21 | Shot E | 1.0 s cross-dissolve |
| 25.0–30.0 | End card over Shot E's last frames (blurred and darkened) | 1.0 s soft blur/dim |

## 3. On-screen script

Text rules:
- At most one headline (≤ 4 words) and one small sub-line per scene.
- Text fades in 0.6 s (with a gentle 12 px rise) once the dissolve has finished, holds for at least 2.8 s, and fades out 0.5 s before the next dissolve starts. Text never crosses a dissolve.
- Position: lower-middle (about 60–70 % of the frame height). This stays clear of Instagram's caption and buttons in the bottom 20 %, and away from the logo at the top.

| # | Output time (text on screen) | Headline | Sub-line (small) |
|---|---|---|---|
| 1 | 1.0–4.6 | *Super Deluxe Room* | The Caliph · Powai, Mumbai |
| 2 | 6.4–9.9 | King-size comfort | Full blackout curtains |
| 3 | 11.4–14.9 | Crafted in detail | *(none: let the close-up breathe)* |
| 4 | 16.5–19.9 | Everything within reach | Work desk · Tea & coffee · Flat-screen TV |
| 5 | 21.5–24.6 | Vanity & mini-fridge | Complimentary breakfast at Pukhtoon |
| End | 25.4–30.0 | **Book your stay** | thecaliphhotel.com · +91 91677 55777 |

User decisions (2026-11-26):
- No prices on screen.
- The end card shows the front-desk number: "Front desk +91 91677 55777".
- The 720p file is the only source; it is enhanced in `tools/build_base.py`.
- Any calm instrumental will do: `tools/make_music.py` synthesizes an original piano + pad track, so there is no rights issue.

As built (`index.html`, following the HyperFrames vertical guide):
- Scene 1's title is already on screen at frame 0 (no fade from black) and fades out at 4.1–4.6 s.
- Text sits at 1010–1330 px of the 1920 px frame.
- Headlines are EB Garamond 84 px; sub-lines are Montserrat 36 px.

Alternates, unused:
- 2: "Rest, king-size"
- 3: "Quiet luxury"
- 5: "Thoughtful touches"

## 4. Look (matches the Pukhtoon reel, posted from the same account)

- **Logo:** the full Caliph logo top centre for the whole video (`projects/pakhtoon-vid-1/assets/caliph-logo-full.png`: gold emblem, white wordmark) over the same soft dark top gradient.
- **Type:**
  - Scene 1 headline in Great Vibes, the script used for "Welcome To Pukhtoon".
  - All other headlines in an elegant serif (e.g. Cormorant Garamond, medium).
  - Sub-lines in small spaced caps in a clean sans, white at 85 %.
  - Gold #bb8d28 is the one accent colour: a thin 40 px rule between headline and sub-line.
- **Legibility:** the room is bright (cream walls, marble floor), so white text sits on a soft dark radial shadow behind the text block. Use a shadow, not a box.
- **Grade:** the footage is already warm and clean. Lift the shadows slightly and keep the whites from clipping on the bed linen.
- **Motion:** add no extra zooms; the gimbal moves already carry the shots. Text only fades and rises.

## 5. Sound

The raw video is silent, so the reel needs a calm instrumental (soft piano/ambient, about 70–80 BPM), ideally placing each dissolve's midpoint on a bar line. The track must be one the hotel can legally use on a business account (Instagram's commercial library or a licensed track), unlike the open rights issue on the Pukhtoon song.

## 6. Build

From this folder, with Node 22 and ffmpeg on PATH:

1. `python tools/build_base.py` writes `assets/base.mp4`: enhanced 1080x1920 picture with the dissolves.
2. `python tools/make_music.py` writes `assets/music.wav`.
3. `npx hyperframes render --fps 24 --quality delivery -o ../../outputs/caliph-super-deluxe-room-tour-30s.mp4`.
