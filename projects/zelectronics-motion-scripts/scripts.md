# ZELECTRONICS: 2D motion graphics script series (draft 1, 2026-11-12)

Five short vertical videos (9:16, 1080×1920, 30 fps), each built on one fact from `market-research.md`. Each script borrows its motion language from one of the analysed references in `refrences/2d-motion-graphics/` (see `SUMMARY.md` there). All five follow the strict ZELECTRONICS brand rules.

**Timing:** the times are estimates at about 2.6 words/s. Final scene and word times come from a Whisper word-timestamp transcript of the recorded VO, as in the refurbished-laptops reel. **[Square brackets]** mark facts ZELECTRONICS must confirm (see market-research.md §3).

| # | Title | Audience | Hook fact | Length | Motion style (reference) |
|---|---|---|---|---|---|
| 1 | The memory tax | Everyone buying a laptop now | Memory shortage → new laptop prices climbing | ~25 s | Calm blur collage (Solution Wagon, pin-1061653312177886416) |
| 2 | Windows 10 is over | Offices, SMEs | Windows 10 support ended Oct 2025; CERT-In warning | ~27 s | Word-by-word caption build + mock-ups (InsiderForce, pin-901986631645535447) |
| 3 | Ten desks | Startups setting up or growing a team | Cost of kitting out an office, new vs refurbished | ~20 s | Punchy white/black flip + iris reveal (MotionDesigners, pin-933230354043913635) |
| 4 | Refurbished isn't used | Doubters, first-time buyers | Trust: tested before shipping to your door, 6-month warranty | ~24 s | Spoken pitch; one metaphor per scene (Web Rank Studio, pin-924363892282992611) + grey→black captions (InsiderForce) |
| 5 | One less on the pile | LinkedIn / CSR-minded buyers | India's e-waste volume | ~22 s | Calm blur collage (Solution Wagon) |

**Suggested order to post:** 1 → 2 → 3 (price, then business pain, then business maths), then 4 to answer the "is it reliable?" comments, then 5 as a LinkedIn piece.

## Shared brand kit (applies to all five)
- **Colour:** strictly black, white and grey tints. Light scenes are white #FFFFFF or off-white #F7F7F7 with a soft grey vignette; dark scenes are #0A0A0A with a faint white glow. Every accent colour in the references maps to **black on light** or **white on dark**. The red/blue exception was approved for the refurbished-laptops reel only; ask the client before reusing it here.
- **Type:** two-tier lock-up from the references. A small lead-in in Figtree 400–500 sits over a big key word in Figtree 800, **or** the key word is set in **Instrument Serif Italic** (one italic word per stack). All copy is in sentence case, except "ZELECTRONICS", which is always in caps. In the shot tables, *italic* marks the Instrument Serif word.
- **Imagery:** greyscale background-removed cut-outs (laptops, desktops, RAM sticks, chips, server racks, office desks, receipts) with soft drop shadows, big and often cropped by the frame edge. No third-party logos: show generic OS windows, not the Windows logo.
- **Persistent plate** (light scenes, scripts 1, 2 and 5): a small ZE tile top centre, a faint dashed grid (about 110 px cells, 6% black), and two grey four-point star ornaments slowly rotating in opposite corners.
- **Motion defaults:**
  - **Words:** each word appears on its VO word, 0.1–0.2 s early. It blurs in from 24 px with a 24 px rise over 0.25–0.35 s, using expo-out easing and no bounce.
  - **Scene changes:** they fall in the VO gaps. The default is a 0.15–0.2 s blur-out followed by a blur-in. One big set-piece transition per video marks the turn from problem to solution.
  - **Holds:** something always moves while a scene holds, such as a slow 3–5% push-in or the rotating ornaments.
- **End card:** the approved ZELECTRONICS end card: ZE tile + Michroma wordmark, zelectronics.co · +91 84518 64754 · Mumbai, India.
- **Audio:**
  - **VO:** must come from the user. The ElevenLabs MCP is disabled for this account, but Friday v2 (`ka2YlHIZtpI73mTUG5iF`) can read these scripts.
  - **Music:** a quiet bed under the VO, with whooshes only on the set-piece transitions.

---

## Script 1: "The memory tax" (~25 s)
**Angle:** prices are going up for a reason buyers can understand, and refurbished is the way around it.
**Style:** Solution Wagon. Calm, off-white, greyscale collage, everything enters and leaves through a blur, with a persistent plate.

**VO (61 words)**
> Laptop prices in India are climbing.
> Not because laptops got better.
> Because memory got scarce.
> AI data centres are buying up the world's RAM, and every new laptop pays for it.
> Memory prices have more than doubled.
> So the smart move isn't waiting.
> It's buying certified refurbished.
> Same performance. Backed by warranty. For a lot less.
> ZELECTRONICS. Laptops and desktops, without the new-price tax.

| # | Time | VO | On screen | Motion |
|---|---|---|---|---|
| 1 | 0.0–2.4 | Laptop prices in India are climbing. | Open laptop cut-out; "laptop prices" / *climbing* | Laptop focuses in from blur; a thin grey price line draws upward behind it, left to right, and ends in a small dot. Words blur in on the VO |
| 2 | 2.4–4.4 | Not because laptops got better. | Two identical laptops labelled "2025" and "2026"; "not because laptops / got *better*" | The second laptop slides in beside the first; a grey "=" fades in between them. Out: **zoom-through** into the RAM slot of the 2026 laptop |
| 3 | 4.4–6.0 | Because memory got scarce. | Extreme close-up RAM stick, pulling back; "because memory got / *scarce*" | The memory chips on the stick blur out one by one, like stock running out |
| 4 | 6.0–9.0 | AI data centres are buying up the world's RAM, | Tall server-rack silhouette cropped right; "AI data centres / are buying up / the world's *RAM*" | A stream of small RAM sticks flies from the bottom-left into the rack with motion blur; the rack glows faint white |
| 5 | 9.0–11.0 | and every new laptop pays for it. | Receipt card: "laptop", "+ memory"; "every new laptop / *pays for it*" | The receipt drops in from the top; the "+ memory" line types on. Out: **gravity drop** (the receipt tips and falls out the bottom) |
| 6 | 11.0–13.4 | Memory prices have more than doubled. | Ring counter **1× → 2×+**, label "memory prices" | A thin grey ring with a black arc sweeping as the number rolls up. Out: **light-orb wipe** to white (the set-piece transition; whoosh) |
| 7 | 13.4–15.4 | So the smart move isn't waiting. | Greyscale hourglass; "the smart move / isn't *waiting*" | The hourglass flips once, slowly; the sand keeps falling |
| 8 | 15.4–17.6 | It's buying certified refurbished. | A grey pin drops in at the top; refurbished laptop rises; "certified / *refurbished*" | The pin lands with a small shadow; the laptop rises from the bottom and settles |
| 9 | 17.6–21.0 | Same performance. Backed by warranty. For a lot less. | Pin stays. Three keyword beats swap below it: "same / *performance*", "backed by / *warranty*", "for a lot / *less*" | Solution Wagon's pin trick: the pin stays fixed and blur-pulses on each swap while the keyword below blurs out and the next one blurs in, one per phrase |
| 10 | 21.0–25.0 | ZELECTRONICS. Laptops and desktops, without the new-price tax. | End card + line "laptops and desktops, without the *new-price tax*" | A white flare burns to the dark #0A0A0A card; the ZE tile builds from fragments left to right, then the line and contact details fade in. Hold, then fade to black |

**Facts:** the memory shortage, AI demand and "more than doubled" are all supported (market-research.md rows 1–2). **[Confirm]** "certified" and "backed by warranty".

---

## Script 2: "Windows 10 is over" (~27 s)
**Angle:** a concrete business problem with a deadline that has already passed. Refurbished Windows 11-ready machines fix it without paying new prices.
**Style:** InsiderForce. Off-white, captions build word by word (each word slides in light grey and darkens to black), mock-ups enter from the frame edges, with a persistent "toggle disc" pair.

**VO (64 words)**
> Windows 10 stopped getting security updates in October 2025.
> If your office still runs it, every PC is a security risk.
> CERT-In has already warned users to upgrade.
> But a lot of older PCs can't run Windows 11.
> Replacing every machine new? Expensive. Especially now.
> Replace them refurbished instead.
> Windows 11-ready laptops and desktops. Tested. Backed by warranty and support.
> ZELECTRONICS. Upgrade the office, not the budget.

| # | Time | VO | On screen | Motion |
|---|---|---|---|---|
| 1 | 0.0–3.2 | Windows 10 stopped getting security updates in October 2025. | "Windows 10 stopped getting" / black label box "security updates" / "October 2025" | Grid zooms out to 1x; words build grey→black; the label box **wipes left to right from a thin black line** (InsiderForce hook) |
| 2 | 3.2–6.0 | If your office still runs it, every PC is a security risk. | Generic desktop monitor mock-up showing a plain OS window "Updates: not available"; "every PC is a / *security risk*" | The monitor rises from the bottom edge and settles; a small grey warning triangle pulses once on the window |
| 3 | 6.0–8.4 | CERT-In has already warned users to upgrade. | Small official-style notice card: "Advisory: upgrade from Windows 10" (no logos); "CERT-In has already / *warned* users" | The card slides in from the right with a soft shadow; words build |
| 4 | 8.4–10.8 | But a lot of older PCs can't run Windows 11. | Toggle discs: a grey disc "10" on a rail from the left edge, a black disc "11" on a rail from the right edge; "a lot of older PCs / *can't* run Windows 11" | The discs slide along their rails; the "10" disc tries to slide toward "11" and stops short with a tiny shake (the only shake in the series) |
| 5 | 10.8–13.6 | Replacing every machine new? Expensive. Especially now. | Row of six new-laptop boxes with price tags rising; "replacing every machine new?" / **expensive.** / *especially now* | The boxes pop in left to right; the tags tick up. Out: **blur to grey dissolve** (set-piece; whoosh) |
| 6 | 13.6–15.8 | Replace them refurbished instead. | Discs return: the "11" disc now holds the ZE tile; "replace them / *refurbished* instead" | Washed-out fade-in to full contrast; the ZE disc slides to centre |
| 7 | 15.8–20.6 | Windows 11-ready laptops and desktops. Tested. Backed by warranty and support. | A black pillar rises from the bottom with a white card on top; ✦ list on the left: "Windows 11-ready", "laptops and desktops", "tested", "warranty and support" | Each bullet: the ✦ grows from a dot, then the words slide in grey and darken. The pillar card **cross-fades** laptop → desktop → a small "warranty" badge, one per phrase |
| 8 | 20.6–27.0 | ZELECTRONICS. Upgrade the office, not the budget. | End card + "upgrade the office, / not the *budget*" | The ZE logo rises from the bottom onto a grid patch; words build; contact details fade in. Hold |

**Facts:** the 14 Oct 2025 end of support and the CERT-In advisory are supported (row 7). **[Confirm]** that the stock is Windows 11-ready and licensed, and what "support" and the SLA cover.

---

## Script 3: "Ten desks" (~20 s)
**Angle:** simple maths for a growing team. The saving pays for something that matters more than hardware.
**Style:** MotionDesigners. Fast, with hard flips between white and black scenes, a two-tier lock-up, a glow on black, and an iris reveal growing from the key word.

**VO (44 words)**
> Setting up ten desks?
> Ten new laptops: [₹X lakh].
> Ten certified refurbished: [₹Y lakh].
> Same work gets done.
> The difference?
> That's your next hire.
> Spend on growth, not on hardware.
> ZELECTRONICS. Bulk pricing. Free consultation. Fast turnaround in Mumbai.

| # | Time | VO | On screen | Motion |
|---|---|---|---|---|
| 1 | 0.0–1.6 | Setting up ten desks? | WHITE. Top-down office: ten empty desks in two rows; "setting up / **ten desks?**" | The desks pop in fast left to right (0.05 s apart); slow 5% push-in |
| 2 | 1.6–3.8 | Ten new laptops: [₹X lakh]. | BLACK, glow. Ten small laptop icons; "ten new laptops" / **₹X lakh** | Hard flip to black; the number rolls up with motion blur; a white glow on the figure |
| 3 | 3.8–6.2 | Ten certified refurbished: [₹Y lakh]. | WHITE. Same ten icons, now outlined; "ten certified refurbished" / **₹Y lakh** | Fade up from overexposed white; the number rolls up and lands smaller |
| 4 | 6.2–7.8 | Same work gets done. | WHITE. The desks return, now with laptops on them, screens on; "same work / *gets done*" | The laptops drop onto the desks in a quick stagger |
| 5 | 7.8–9.0 | The difference? | BLACK. "the / **difference?**" with echo copies | Words slide in from the right with motion blur and faint echoes |
| 6 | 9.0–11.2 | That's your next hire. | WHITE. Empty chair cut-out with a "hired" tag; "that's your / *next hire*" | **Iris reveal** grows from the "?" of the previous scene (set-piece; whoosh); the chair spins half a turn into place |
| 7 | 11.2–13.6 | Spend on growth, not on hardware. | WHITE + a grey S-curve road band drawing from the top; "spend on *growth*, / not on hardware" | The road band draws on; the words build; "hardware" fades to grey |
| 8 | 13.6–20.0 | ZELECTRONICS. Bulk pricing. Free consultation. Fast turnaround in Mumbai. | BLACK end card: ZE logo glowing; three short lines "bulk pricing" · "free consultation" · "fast turnaround in Mumbai"; contact details | Black iris from the road band's end; the logo glows up; the three lines blur in one per VO phrase. Hold |

**Facts:** **[Confirm]** real prices for one model new vs refurbished, ×10. Pick the payoff line to match the real difference: "that's your next hire" (a large saving), "that's two months of a new hire" or "that's your marketing budget" (smaller savings). Bulk pricing, free consultation and fast turnaround come from the approved intro; reconfirm them.

---

## Script 4: "Refurbished isn't used" (~24 s, draft 5: user's wording)
**Angle:** a short, natural pitch. It names the common doubt, then makes two promises: every laptop is tested before it ships to your doorstep, and it arrives with a six-month warranty.
**Style:** Web Rank Studio visuals (one metaphor per scene, a different short transition at each scene change) at a calm pace. Scenes change at clause breaks. Captions use the InsiderForce build: words slide in grey and darken to black on the VO. Captions show only the current clause, at most two lines, with one key phrase in Instrument Serif Italic.

**Delivery note for the VO:** conversational and unhurried, like telling a customer in person. Breathe at the commas, with no dramatic pauses.

**VO (48 words; wording from the user)**
> When people hear "refurbished", they picture someone's old laptop with a fresh sticker on it.
> At ZELECTRONICS, we test every laptop before we ship it to your doorstep, and it comes to you with a six-month warranty.
> So before you pay today's new prices, talk to us.

| # | Time | VO | On screen | Motion | Out |
|---|---|---|---|---|---|
| 1 | 0.0–1.8 | When people hear "refurbished", | WHITE. "refurbished" big in Figtree 800, with a giant light-grey ghost copy cropped behind | The word is on screen from frame 0 and darkens grey→black as it is spoken; slow 3% push-in | Cut on the comma |
| 2 | 1.8–6.0 | they picture someone's old laptop with a fresh sticker on it. | WHITE. A worn laptop cut-out; a cheap round "like new!" sticker; caption "someone's old laptop / with a *fresh sticker* on it" | The laptop slides in from the left edge; the sticker slaps on at "sticker" with a small scale settle | Laptop shrinks to a dot |
| 3 | 6.0–8.6 | At ZELECTRONICS, we test every laptop | WHITE + grid. A clean laptop in exploded view: battery, SSD, RAM, screen and keyboard lift apart; small ZE tile top centre; caption "at ZELECTRONICS, / we *test* every laptop" | The dot expands into the clean laptop (zoom-out); the parts separate on "test", and ticks stamp on each part in a fast stagger | Parts reassemble |
| 4 | 8.6–11.4 | before we ship it to your doorstep, | WHITE. The laptop closes and drops into a plain shipping box with a "tested" tape strip; the box then slides along a thin road line to a doorstep (a simple door outline and mat); caption "before we ship it / to *your doorstep*" | The flaps fold in 0.3 s and the tape draws left to right; the box travels right with a little motion blur and settles on the mat | **Circle wipe** to black from the box (the set piece; whoosh) |
| 5 | 11.4–15.4 | and it comes to you with a six-month warranty. | BLACK, faint glow. The box opens; a white shield rises out of it with "6 months"; caption "it comes to you with a / *six-month warranty*" | The flaps open; the shield draws on as a single stroke, then fills; one thin ring pulses out | Cross-fade |
| 6 | 15.8–19.8 | So before you pay today's new prices, talk to us. | WHITE. A new-laptop price tag; caption "before you pay *today's new prices*, / talk to us" | The tag's number ticks up; on "talk to us" it gets a grey strike-through and the phone number slides in under the caption | Hard cut |
| 7 | 19.8–24.0 | (music only) | WHITE end card: ZE tile + wordmark, "certified refurbished laptops and desktops", contact details | Logo fades in, then the line and the contact details. Hold | — |

**Why draft 5:** the user supplied this wording (2026-11-12). Only two small fixes were made: "every" became "every laptop" (a word was missing), and "door steps" became "doorstep". The battery/storage detail was dropped, so the test appears only visually in scene 3.

**Facts:** the six-month warranty, testing before shipping and doorstep delivery come from the user. If desktops also get the same test and warranty, change "every laptop" to "every laptop and desktop".

---

## Script 5: "One less on the pile" (~22 s)
**Angle:** sustainability as the second reason to buy. Best on LinkedIn or for CSR-minded companies.
**Style:** Solution Wagon. Calm blur collage on off-white with the persistent plate.

**VO (52 words)**
> India produced over a million tonnes of e-waste last year.
> Old laptops and desktops are part of that pile.
> Every machine that's refurbished instead of scrapped
> is one less on it, and one more doing real work.
> Good for your budget.
> Better for the planet.
> ZELECTRONICS. Certified refurbished laptops and desktops.

| # | Time | VO | On screen | Motion |
|---|---|---|---|---|
| 1 | 0.0–3.2 | India produced over a million tonnes of e-waste last year. | Greyscale heap of old electronics, cropped bottom; "over a million tonnes" (big) / "of *e-waste*" | The heap rises slightly from the bottom; the number blurs in early |
| 2 | 3.2–5.6 | Old laptops and desktops are part of that pile. | Closer on the heap: laptops and a desktop tower visible; "laptops and desktops / are part of *that pile*" | **Zoom-through** into the heap (set-piece; whoosh) |
| 3 | 5.6–8.4 | Every machine that's refurbished instead of scrapped | One laptop lifts out of the heap and floats up, cleaned; "refurbished / instead of *scrapped*" | The laptop rises and the heap blurs out below it; a soft white glow comes up behind the laptop |
| 4 | 8.4–11.6 | is one less on it, and one more doing real work. | Split: the heap counter "−1" on the left, a desk with the laptop working on the right; "one less on it" / "one more doing *real work*" | A "−1" counter ticks on the left; the laptop screen lights up on the right |
| 5 | 11.6–14.4 | Good for your budget. Better for the planet. | Pin trick: a grey pin, two keyword beats below it: "good for your / *budget*" → "better for the / *planet*" | Blur swap under the fixed pin; a small greyscale globe on the second beat |
| 6 | 14.4–22.0 | ZELECTRONICS. Certified refurbished laptops and desktops. | End card | A white flare to the dark card; the logo builds from fragments; contact details. Fade to black |

**Facts:** **[Verify]** the e-waste figure against CPCB's own data before publishing (row 9 is a newspaper summary of about 1.41 Mt in 2025-26). If it can't be confirmed, change line 1 to "India throws away more electronics every year."
