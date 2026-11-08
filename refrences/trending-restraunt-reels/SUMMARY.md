# Trending restaurant reels — cross-reel summary

Four Instagram restaurant reels, downloaded 2026-11-08 and analysed shot by shot. Per-reel breakdowns are in each folder's `analysis.md`; the raw numbers are in `index.json`.

**How this was measured:**
- **Video:** ffprobe facts, ffmpeg scene detection (threshold 0.3) with every cut verified by hand against 10 fps bursts, a frame per second, and k-means colour palettes.
- **Audio:** never listened to. Audio claims come from Whisper transcripts, onset and tempo analysis, and loudness measurements. Music genre, mood and track names are unknown.
- **Engagement:** comes from the post metadata (likes and comments only, no view counts). It depends on account size as much as on craft, so treat any performance comparison as a hint, not proof (n = 4).

## At a glance
| | 01 Al Kababish | 02 Socio | 03 Nur Cafe | 04 Sahara "palace" |
|---|---|---|---|---|
| Account type | Food creator | The restaurant itself | Food creator | Lifestyle creator |
| Likes / comments | 47,550 / 1,155 | 3 / 21 | 11,131 / 60 | 396 / 364 |
| Length (picture) | 13.5 s | 28.4 s (24.0 s + 4.4 s black) | 9.9 s | 21.3 s |
| Shots (verified) | 18 | 21 | 4 | 21 |
| Average shot | 0.75 s | 1.14 s (montage 0.88 s) | 2.47 s | 1.01 s |
| Cut rhythm | Every 1.5 beats at ~110 BPM | Every 2 beats at ~138 BPM | Follows lyric phrases | Every 1.5 beats at ~86 BPM |
| Transitions | Hard cuts only | Hard cuts + white flashes, whip, dissolve, fade | Hard cuts only | Hard cuts (1 flash-like jump) |
| First frame | Amber draped ceiling | Glide into chandelier room | Dark lamp-lit interior | Chandelier hall, symmetrical |
| First food on screen | 0:02.5 | 0:05.9 | 0:04.4 (menu at 0:01.3) | 0:08.3 |
| On-screen text | One headline, whole reel | Q&A captions, first 3.5 s only | Logo + "chalein?", whole reel | Script title, whole reel |
| Audio | Music only | 2-line spoken Q&A + music | English lyric song | Punjabi vocal song |
| Light | Night, warm practicals | High-key food, warm interior | Night, warm practicals | Night, warm practicals |
| Ending | Loops (0.5 s décor shot) | 4.4 s of black, no loop | Loops (2-frame black) | Loops (0.5 s wide like the opener) |

## Shared patterns
1. **Sell the place first, food second.** All four open on the room, not a plate: a ceiling, a chandelier, a corridor. The first frame answers "what does it feel like to be there?" Food arrives 2.5–8.3 s in, and in 04 only after 8 s.
2. **One headline, on screen from frame 1, never animated.** 01, 03 and 04 hold a single static title for the entire reel. It works as the hook, the caption and the loop disguise. It sits in the upper third (24–33% of height) in 01 and 04, and centred in 03. The copy is a promise of place, not a description of food: "Found a little slice of Turkey in Mumbai 🇹🇷", "Prettiest Arebian palace Restaurant", "chalein?".
3. **Shot on a phone at night, lit only by the venue.** Three of four (01, 03, 04) are night shoots under warm tungsten practicals with deep phone focus and no added light. The palette is warm brown and amber (medians around #4f3321–#64462e). One or two saturated accents carry it: a red chandelier, teal plates, a blue mocktail, red soda.
4. **Short, even shots cut on the music.** 01 and 04 cut every 1.5 beats at a near-metronomic ~0.75–1.0 s. 02's montage cuts every 2 beats. 03 is the slow outlier, with 4 shots that follow the lyric phrasing. Hard cuts do almost all the work; motion inside the shot (slow 5–15% push-ins, tilts, a twirl) makes plain cuts feel fluid.
5. **Hands, not presenters.** No one talks to camera in any reel. People appear as hands (tear, lift, cheers, fork, stir) or as a figure from behind or at a distance (01's woman at the door, 04's twirl and stair climb).
6. **No classic "money shot".** None of the four uses a pour, steam, sizzle close-up or cheese pull. The food moments are small hand actions and one overhead hero spread, held slightly longer than the other shots (01 at 0:09.70, 04 at 0:08.27, 02's two spreads at 0:13.73).
7. **Built to loop.** 01, 03 and 04 end abruptly, 0.5 s into a shot (or 2 black frames) that looks like the opening, so the replay feels continuous. 02 is the only reel that doesn't loop: it fades out and holds 4.4 s of black. It is also the weakest performer, though its account size is the bigger factor.
8. **The location is withheld so people comment.** 01 ("Comment for location", 1,155 comments) and 04 ("Comment 'Palace' for location", comments almost equal to likes) hide the address in the video and trade it for comments. 03 does the same socially with "Hum kab?" ("when are we going?"), which prompts tagging.
9. **Music-led, mixed to about −14 LUFS.** All four are music-first. The only speech is 02's two-line "Is it nice there? / Yeah, it is." exchange.

## Key differences
- **Creator vs brand:** the three creator reels (01, 03, 04) feel like a personal visit: night light, phone look, "come with me". The restaurant's own reel (02) is polished: high-key food lighting, a gimbal glide, four transition types, a summer-menu colour story. But it ends on a logo and dead air instead of an invitation.
- **Tempo:** 03 shows a sub-10 s, 4-shot reel can perform (11k likes) on atmosphere plus a tag-a-friend line. 01 shows a fast 18-shot cut in 13.5 s working just as well. Both are short; the two longer reels (21–28 s) rely on steady rhythm to hold attention.
- **Food share:** 02 is food-heavy (12-shot montage). 04 is almost all décor (food in 2 of 21 shots). 01 alternates ambience and food almost strictly. 03 is half menu and food.
- **Text:** 02 is the only reel that uses speech-synced, changing captions, and the only one whose text disappears early (after 3.5 s).
- **Light:** 02's bright, high-key food (luma median ~155) is the exception; the others sit in low key (luma median 55–88).

## Recipe: a restaurant reel in this style
**Goal:** a 10–15 s reel that sells the feeling of the place and gets comments.

1. **Shoot at night, phone only, with the venue's own lights.**
   - Use the main 1x lens and in-phone stabilisation (or a gimbal for one glide).
   - Lock exposure on each shot and pull it down 0.3–0.7 EV so lamps and chandeliers don't clip and the blacks stay rich.
   - Use 4K at 30 fps (or 24/25), with no slow motion.
   - Hold every clip 3–4 s, perfectly still or with one slow move, so you can trim a clean second.
2. **Shot list (about 15 clips):**
   1. The signature décor element (chandelier, arch, ceiling) as a low-angle, symmetrical opener.
   2. An arrival shot: a door push or a walk down a corridor, person from behind.
   3. 3–4 more décor beats with slow push-ins (5–7%) or tilts. Repeat the signature element 2–3 times as a motif.
   4. A cheers with two colourful drinks.
   5. One hand-action food close-up (tear, lift, spoon or fork).
   6. One overhead hero spread of the whole table: the longest hold, about 1–1.3 s.
   7. A sign or mural shot that shows the name without spelling out the address.
   8. A dessert or drink detail.
   9. A closing shot that looks like the opener, so the loop is seamless.
3. **Wardrobe and props:** if a person appears, dress them in the venue's colours (maroon and gold in a gold room). Order one or two visually loud drinks for colour pops.
4. **Edit:**
   - Pick a music track (instrumental or vocal, 85–110 BPM) and cut every 1.5 beats (about 0.75–1.0 s).
   - Use hard cuts only; the in-shot movement gives the flow.
   - Alternate ambience and food, and place the hero spread on the track's biggest lift.
   - End about 0.5 s into the closing shot, on a beat. No end card, no fade, no black.
5. **Text:**
   - One static headline from frame 1 to the last frame, promising a feeling of place: "Found a little [country/vibe] in [city] [flag]", "Prettiest [theme] restaurant", or a one-word Hinglish invite like "chalein?".
   - Style it white or cream, in a condensed bold sans or an elegant script/serif.
   - Centre it at 25–33% of frame height, clear of Instagram's UI.
   - Spell-check it (04's "Arebian").
6. **Grade:** keep the phone's warm night look (warm white balance, blacks not lifted, no teal-orange) and protect the one or two saturated accent colours.
7. **Caption and CTA:** a one-line promise plus "Comment '[keyword]' for location", or a tag-a-friend question ("Hum kab?"). Add location and dish keywords as hashtags.
8. **Avoid (from 02):**
   - Black or dead air at the end.
   - Text that disappears after 3 s.
   - Long runs of static plates with no hand or human moment.
   - Flame shots so overexposed they clip to white.

## Files
```
trending-restraunt-reels/
├── SUMMARY.md            this file
├── index.json            per-reel facts (verified shot counts, engagement, audio type)
└── NN-<post id>/         one folder per reel (01–04)
    ├── video.mp4         the downloaded reel
    ├── analysis.md       shot-by-shot breakdown (shared template)
    ├── meta.json         caption, account, date, likes/comments
    ├── probe.json        ffprobe facts
    ├── cuts.json         scene-detect cut times (raw; verified counts are in analysis.md)
    ├── audio.json        loudness, tempo estimate, Whisper transcript
    ├── frames/           cut_NN_<time>s.jpg (one per cut) + sec_NNN.jpg (one per second)
    └── sheets/           contact sheets of the cut and per-second frames
```
