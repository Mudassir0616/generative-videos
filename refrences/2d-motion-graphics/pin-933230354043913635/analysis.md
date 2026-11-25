# 2D motion graphics ref — MotionDesigners.Pro, "Motion inspiration - Frames" (Pinterest 933230354043913635)
https://www.pinterest.com/pin/933230354043913635/ · uploader "MotionDesigners.Pro" (credits @motiondesigners.2d / imran__visuals) · upload date 2025-10-02 · 17.87 s · 720x1280 (9:16), 25 fps, H.264 + AAC (best format Pinterest serves)

Files here: `video.mp4` (git-ignored), `probe.json`, `cuts.json`, `audio.json`, `meta.json`, `vo_words.json` (Whisper word timestamps). Built with `tools/prep_reels.py` plus 4 fps contact sheets and 25 fps strips around every transition, checked by eye. Colours were sampled from decoded pixels. Per the user, no frames or contact sheets are kept: this file is the record of the motion graphics.

## Overview
- **What it is:** a self-promo for a short-form video editor ("imran_visuals"), framed as an Instagram growth pitch. VO-driven kinetic typography with one object or emoji per line. It cuts between a **warm cream "paper" look** and a **black "glow" look**. No people on camera (one halftone suit illustration).
- **Script (VO, Whisper, 56 words):** "You've got the ideas and content, but your growth? Still stuck. Because content without an audience is just noise, and the audience is the real money. No eyeballs, no impact, no earnings. Instagram doesn't reward effort, it rewards strategy. I deliver that strategy. Your content's working hard, but not smart. Hit the DM button (to) fix that." The VO runs almost wall to wall at about 3.2 words/s (speech fraction 0.99). Whisper's word boundaries are contiguous, with no real gaps. It reads like a fast, punchy AI/TTS or edited voice. Not verified by ear.
- **Structure:** problem setup (0–3.2 s) → reason (3.2–7.5) → the cost, as a checklist (7.5–9.5) → platform truth "Instagram rewards strategy" (9.5–12.7) → offer: the editor's Instagram profile card (12.7–14.1) → re-pitch "working hard, not smart" (14.1–16.2) → CTA on black (16.3–17.87). **14 shots in 17.87 s, average 1.28 s.** The longest is the Value checklist (2.06 s), the shortest "without an audience" (0.76 s). There is **no end card**: it ends on the "to fix that" text.
- **Audio:** VO at about −14.5 LUFS integrated. 0.1 s RMS stays between −7 and −20 dB almost throughout. Most windows are dominated by energy below 120 Hz, which suggests a sub-heavy music bed or low-end hits under the voice (inferred; a male voice's fundamental also contributes). The only clear drop is 2.3–2.6 s (−24 to −30 dB, low end gone): a short dead-air beat between "growth" and "still stuck", where the bed seems to cut out for emphasis. Tempo estimate 117 BPM, low confidence. I did not listen to it; music and SFX are inferred from levels only, and no distinct whoosh peaks stand out at the transitions.

## Look
- **Palette (measured):**
  - Cream paper background **#FDF6EF** (one variant **#FCF3EA** under the Instagram scene's fading pink tint).
  - Near-black background **#030303** with a soft lighter vignette or glow around the subject. The suit scene lifts to about #0D0C0F at the bottom.
  - One accent red **≈ #F5060E** for the key words. Saturated cores measure #F8020A to #FC030E, anti-aliased medians #E9050A to #F9030A. The same red is used on cream and on black.
  - Ink: black text **#040000** on cream, white **#FBF9FB** text and shapes on black.
  - Warm grey **#BCB7B1** for the thick curved "road" stroke on cream scenes. Mid grey **#8F8F8F** for the Value card.
  - Transition-only pink tint **#F9BEB7** with a darker pink-red ring.
  - Off-palette elements: the Instagram gradient wordmark (purple → magenta → orange) and full-colour emoji (clown, sunglasses-pointing face).
- **Background rhythm:** C B B B C B C C C B C C B B (C = cream, B = black). It flips between cream and black at most cuts. Black is used for the emotional or "dark truth" lines (stuck, content without audience, money, the offer, the CTA). Cream is used for statements and objects.
- **Type:**
  - One grotesque sans throughout, tightly tracked (negative letter-spacing, about −0.04em). It looks like Inter Display / SF Pro Display / Helvetica Now; the exact face is not verified.
  - **Two-tier lines:** a small lead-in phrase in regular/medium weight in black (cream scenes) or white (black scenes), with the **key word 1.6–2× larger in extra-bold red** directly under or beside it. Line spacing is tight, so the key word almost touches the lead-in ("You've got the / **ideas** and / **content**", "But your / **growth**?", "It rewards / **strategy**", "Your content's / **working hard**", "But not / **smart**").
  - On black, **all type glows**: white text has a soft white outer glow, and the red words have a red bloom (about 10–20 px blur, around 60% opacity, inferred from frames). Some black-scene lines also have faint, blurred, horizontally offset echo copies left and right of the line ("Hit the DM button", "to fix that"), like an Echo/trail effect.
  - Type is mostly centred, set at about 40–50% of frame height, single block, 2–3 words per line.
  - The only other lettering is the Instagram script wordmark, and the UI text inside the profile card screenshot.
- **Imagery:**
  - 3D-rendered or photo cut-outs with soft drop shadows: a glass light bulb (huge, cropped off the left edge), a black keyboard tilted about 30° and cropped bottom-right with a strip of tape, an open briefcase of cash rendered in greyscale.
  - A halftone-dot B&W illustration of a man in a suit with arms crossed and a plain white circle as the head. The text sits inside the head.
  - Emoji: the clown, large in the centre with two giant, cropped, blurred clowns in the corners. The sunglasses face pointing at the viewer overlaps the word "smart".
  - A grey paper note card with a red push-pin, the heading "Value", a rule, and three icon + label rows.
  - A dark-mode Instagram profile screenshot (rounded card #1E222A).
- **Decoration:**
  - A thick warm-grey **S-curve "road" band** (about 70 px wide at 720 px) sweeping top to bottom behind the subject. It appears in 3 cream scenes (clowns, Value, sunglasses) and draws on from the top edge as the scene starts.
  - A faint thin **square grid** (about 40 px cells, very low contrast) behind the text block in the bulb and briefcase scenes.
  - A small barcode top right in the opener.
  - A tiny brand lock-up (logo + "HD" + small text) at the bottom of the opener and top centre of the keyboard scene. This is the creator's watermark.
- **Layout:** text in the centre or upper-middle, object large and cropped by the frame edge (bulb left, keyboard bottom-right, clowns in the corners). Black scenes are mostly empty space with a small glowing text block in the middle. Long lines are kept short: about 50–60% of the frame width at most.

## Scene-by-scene (times from 4 fps sheets and 25 fps strips; VO words from vo_words.json)
| # | Time | VO (word start, s) | Background | On screen | In / animation | Out |
|---|---|---|---|---|---|---|
| 1 | 0.00–1.44 | "You've got the ideas and content" (0.00–1.52) | Cream + faint grid | Huge glass bulb cropped left; barcode top-right; "You've got the" black, "ideas" red bold + "and" black, "content" big red bold; small blue butterfly flutters by the text; watermark bottom | Frame starts slightly wide and **pushes in about 15% while drifting left in 0.3 s**. Words build one at a time on the VO: "ideas" visible at 0.64 (spoken 0.54), "content" at about 1.0 | **Flicker transition** 1.44–1.64: frame dims (1.44), 1 black frame (1.48), the bulb shot returns slightly zoomed (1.52–1.56), dims again (1.60), cut |
| 2 | 1.64–3.18 | "but your growth still stuck" (1.52–3.12) | Black, white glow around the figure | Halftone suit man, white circle head with a glow; "But your" dark grey regular + "growth?" red bold inside the head; "still stuck" big white bold glowing across the bottom over the hands | Figure fades up (1.64); "But" (1.72), "your" (1.88), "growth?" (2.08) each blur-fade in; "still" then "stuck" rise from the bottom with motion blur (2.5–2.9). Slow continuous push-in (text rises and grows about 5% over the shot) | Hard cut to 1 black frame (3.20) |
| 3 | 3.20–4.06 | "because content" (3.12–3.94) | Black | "Because" small white glow + "content" red bold with red bloom, centred | "Because" blur-fades in 3.24–3.28; "content" fades in red-blurred at 3.32 and sharpens | Line vanishes: 1–2 black frames (4.08) |
| 4 | 4.10–4.86 | "without an audience" (3.94–4.76) | Black | "without an" white, "audience" big red bold with heavy bloom | "without" blur-fades in (4.12), "an" follows, "audience" at about 4.25; the glow pulses brighter at 4.84 | Hard cut to an over-exposed white frame |
| 5 | 4.88–5.94 | "is just noise" (4.76–5.74) | Cream + grey road band + faint grid | Clown emoji centre; two huge cropped blurred clowns top-right and bottom-left; "is just" black + "noise" red bold | Scene **fades up from washed-out white** (4.88–4.96) while the road band **draws in from the top**; clown pops in (scale up); "is" (5.0), "just" (5.1), "noise" (5.25) | Text group **rotates about 20° clockwise and scales** while the frame washes to white (5.76–5.92); cut |
| 6 | 5.96–7.46 | "and the audience is the real money" (5.74–7.34) | Black + faint grid + glow | Open briefcase of cash (greyscale render); "And the" white + "audience" red bold above; "is the real" white small right; "money" big red bold lower left | Whole comp starts **tilted about −30° in 3D, zoomed in, and slowly counter-rotates to about −5° over 1.2 s**; words appear on the VO ("And" 6.04, "the" 6.16, "audience" 6.32, "is the" 6.9, "real" 7.1, "money" 7.2 with blur) | Hard cut to white |
| 7 | 7.48–9.54 | "no eyeballs no impact no earnings" (7.34–9.36) | Cream + grey road band | Grey card #8F8F8F pinned with a red push-pin, hanging on the road band; "Value" white bold, a rule, then 3 rows of icon + "No eyeballs" / "No impact" / "No earnings" | Scene fades up from white (7.48–7.6) while the card scales up from about 70% and the road band draws in from the top; **checklist rows appear one per VO phrase**: row 1 about 7.6, row 2 8.28 (spoken 8.36), row 3 about 9.0 (spoken 9.0), each a blur-fade-up. The card keeps a slow scale-up | Hard cut to empty cream |
| 8 | 9.56–11.30 | "Instagram doesn't reward effort" (9.36–11.24) | Cream | Instagram gradient script wordmark, centred; under it "doesn't" black + "reward" red bold + "effort" black | Wordmark **scales up from about 15% to 100% in 3 frames (9.60–9.68), overshoots about 8% and settles by 9.9**. 10.08–10.5: **pink ripple**: a translucent pink disc with a darker ring grows from a point on the "g" until it is larger than the frame, leaving a pink tint that fades back to cream by 11.1. "doesn't" (10.3), "reward" (10.48), "effort" (10.64) fade in during the ripple | Text **breaks up / masks out letter by letter** (11.28–11.36) to empty cream |
| 9 | 11.40–12.70 | "it rewards strategy" (11.24–12.60) | Cream | "It rewards" black + "strategy" big red bold | "It" fades in (11.44), "rewards" (11.64), "strategy" (about 11.9). Slow push-in | **Black iris reveal**: a black dot appears on "strategy" (12.68) and grows into a soft-edged black circle that fills the frame by 12.92 |
| 10 | 12.76–14.14 | "I deliver that strategy" (12.60–14.02) | Black | Dark Instagram profile card of "imran_visuals" (rounded, #1E222A, bio "Helping Creators & Brands Grow…", 'DM "Grow" to get started') | Revealed inside the growing iris, slightly blurred → sharp by 13.0; then slow push-in (about 5%) and a slight upward drift | Hard cut |
| 11 | 14.16–15.50 | "your content's working hard" (14.02–15.46) | Cream | Watermark top centre; black keyboard tilted, cropped bottom-right with tape; "Your content's" black + "working hard" big red bold | Hard cut in; "Your" grey-fades in (14.2), "content's" (14.52), "working" blur-fades in 14.68–14.84, "hard" about 15.0 | Text fades out and the frame washes to white (15.48–15.54) |
| 12 | 15.56–16.24 | "but not smart" (15.46–16.18) | Cream + grey road band + corner emoji | Sunglasses-pointing emoji centre, **overlapping "smart"** (emoji in front); "But not" black, "smart" big red bold; huge cropped emoji in the corners | Emoji pops in first (15.56); "But" (15.6), "not" (15.76), "smart" (about 15.95) behind the emoji; the road band draws in from the top | **Black iris reveal** from a dot on the emoji (16.24), soft-edged circle fills the frame by 16.40 |
| 13 | 16.32–17.10 | "hit the DM button" (16.18–17.16) | Black | "Hit the" white + "DM" red bold + "button" white, one line, glow + faint echo copies | Words **slide in from the right with motion blur and trailing echoes**: "Hit" (16.36), "the" (16.44), "DM" (16.52), "button" (16.60–16.68) | Line fades out (17.12) |
| 14 | 17.12–17.87 | "fix that" (17.16–17.68) | Black | "to" white + "fix" red bold + "that" white (on-screen "to" is not in Whisper's transcript) | Same blur/echo word build: "to" (17.16), "fix" and "that" by 17.25 | Video ends on the held line (no end card) |

`cuts.json` (scene threshold 0.3) lists 11 shots. Checked at 25 fps:
- 1.44 is the start of the flicker transition. The real cut is at 1.64.
- 3.20, 4.88, 5.96, 7.48, 9.56, 14.16 and 15.56 are real cuts.
- 12.76 and 16.32 fall in the middle of the two black iris reveals (12.68–12.92 and 16.24–16.40).
- It **misses** the 4.08 black blink ("Because content" → "without an audience"), the 11.28–11.40 letter break-up to an empty frame ("Instagram…" → "It rewards strategy"), and the 17.12 text swap on black ("Hit the DM button" → "to fix that").
- The pink ripple (10.08–10.5) is an in-scene effect, not a cut.

The table above (14 shots) is the verified list.

## Motion language
- **Word-by-word kinetic type on the VO:** every word appears on its own beat, roughly 0.05–0.2 s after Whisper's word start. Whisper starts tend to run early on fast speech, so it is effectively in sync. It is not ahead of the VO the way the Web Rank Studio ref is. The key red word always lands last and biggest.
- **Word entrance:** opacity 0 → 1, blur about 8 px → 0, y +6–10 px → 0, scale about 0.95 → 1, in **3–4 frames (0.12–0.16 s)**, hard ease-out. On black scenes the glow is applied to the word as it lands. The last two scenes add a horizontal slide-in with motion blur and echo trails.
- **Constant slow push-in:** almost every shot scales up about 3–8% over its length (camera drift), so nothing is ever static. Objects are big and cropped by the frame edge.
- **Transitions are short (1–6 frames)** and varied:
  - hard cut with a colour flip (most common)
  - single black-frame blink
  - flicker/dim double-flash (opener)
  - wash to white then cut (5→6, 11→12)
  - fade up from over-exposed white (into cream scenes)
  - rotate-and-scale the text out (5)
  - letter break-up to an empty frame (8→9)
  - **black iris reveal from a dot on the key word/object**, soft-edged circle, about 0.24 s (9→10, 12→13): the signature move
  - pink ripple ring as an in-scene accent (8)
- **Recurring motifs** tie the scenes together: the grey S-curve road band that draws on from the top edge, the faint grid, the two-tier lead-in/red key word lock-up, and the glow on black.
- **Easing:** fast-in, soft-settle. A small overshoot only on the Instagram logo pop (about 8%). The briefcase scene uses a slow 3D counter-rotation settle (about −30° → −5° over 1.2 s).
- **Pacing:** 1.28 s average shot length, at times 2 scenes per sentence. Black "punch" scenes are the shortest (0.76–0.86 s); object scenes with a list or logo run longer (1.4–2.1 s).

## Recreate-it notes (HyperFrames)
- 1080x1920, 25 or 30 fps. Two backgrounds: cream #FDF6EF and near-black #030303 with a subtle radial lift (for example `radial-gradient(circle at 50% 45%, #141414, #030303 70%)`). One accent colour for key words.
- Type kit: one tight grotesque sans (letter-spacing −0.04em). Lead-in at about 44 px (on 1080 w) weight 500, key word at about 80–110 px weight 800, line-height about 0.95. Centre-stacked, the key word directly under or after the lead-in.
- Glow on black: `text-shadow: 0 0 12px rgba(255,255,255,.55), 0 0 30px rgba(255,255,255,.25)` on white words, and the same in the accent colour on key words. For the echo trail, add 2 absolutely positioned copies at ±40–80 px x with opacity .12 and `filter: blur(4px)`.
- Word build: split lines into spans and give each its own tween at its Whisper word start (from `vo_words.json`): `{opacity:0, filter:'blur(8px)', y:10, scale:.95}` → `{opacity:1, filter:'blur(0)', y:0, scale:1}`, 0.14 s, `power3.out`. Wrap each scene in a container that scales 1 → 1.05 linearly over its duration.
- Iris reveal: the next scene sits in a layer with `clip-path: circle(r at x y)`, x/y on the key word. Animate r from 0 to about 120% of the frame diagonal in 0.24 s (`power2.in`). Add a dark soft edge with a `radial-gradient` mask or a blurred black circle under it.
- Wash/flash: a full-frame white div, opacity 0 → 1 → 0 over 2–3 frames at the cut. Fade-up-from-white into cream scenes: `filter: brightness(1.6) → 1` over 0.12 s.
- Road band: an SVG path (stroke about 100 px at 1080 w, warm grey, `stroke-linecap: round`) animated with `stroke-dashoffset` from the top in about 0.25 s.
- Assets: background-removed PNG renders with a soft `drop-shadow(0 20px 30px rgba(0,0,0,.18))`, cropped by the frame edge; a grey pinned card built in HTML for any list (rows appear on the VO).

## Mapping to ZELECTRONICS (strict black & white + grey, sentence case, Figtree + Instrument Serif Italic)
- The cream/black flip maps directly to brand **white/black scenes**. Use pure white (or a very light grey) instead of cream, keep #030303–#0A0A0A for the dark scenes, and use the grey road band and grey card as they are (greys are on-brand).
- **The red key word must go.** In the strict brand, set the key word in **Instrument Serif Italic** (larger, regular weight) against a Figtree lead-in, so it stands out by font instead of colour: black on white, white with a white glow on black. In the refurbished-laptops reel only, the client's exception allows red #E10600 for problem words ("stuck", "noise") and blue #3E77EE for solution words ("strategy"), max one per scene.
- Copy is already sentence case ("But your growth?", "It rewards strategy"), which matches the rule. Brand name always "ZELECTRONICS".
- Replace the emoji, Instagram logo and gradient with B&W product cut-outs (laptops, desktops) and monochrome line icons. Use a ZELECTRONICS card (ZE tile + Michroma wordmark) in place of the profile screenshot, revealed with the black iris.
- Keep the signature moves: word-on-VO blur build, constant slow push-in, black iris reveal from the key word, white wash between scenes, and the checklist card for a "no X / no Y / no Z" line.
