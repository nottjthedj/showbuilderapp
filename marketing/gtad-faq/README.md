# GTAD FAQ infographics

Seven branded graphics, one per FAQ category, for the `grandtheftafterdark.com`
FAQ page. `build.py` holds **both** the copy and the design system, so a wording
change is a one-line edit and a re-render — not a redraw.

```bash
./setup.sh                      # once per machine: fonts + playwright-core
python3 build.py && node shoot.js
# -> png/gtad-faq-NN-slug.png   (1080px wide @2x)
```

| # | Card | Covers |
|---|------|--------|
| 01 | The Basics | What GTAD is, no game knowledge needed, the night's timeline |
| 02 | Tickets & Entry | Age (venue-set), pricing tiers, dress code, refunds, waitlist |
| 03 | The Experience | Video / game app / music, what's in the app, the Arcade, bonuses |
| 04 | The Crew Card | Scan → email + nickname → you're made; what's live on the card |
| 05 | Venues & Tour | Where the next one is, city requests, venue + private bookings |
| 06 | The Handler | Who he is, the voicemail, SMS expectations |
| 07 | Guests & Partnerships | Guest DJs, talent/sponsor/crew inquiries |

## Editing

All copy lives in the `b1`…`b7` string blocks in `build.py`; shared styling is the
`CSS` block at the top. `PAGES` at the bottom controls order — numbering and the
"OF nn" file tags recalculate from it, so adding or removing a card needs no other
edit.

Output height is content-driven; width is fixed at 1080 CSS px, rendered at
`deviceScaleFactor: 2` for 2160px PNGs.

## Source of truth, and what is deliberately absent

Copy started from `06_Website_FAQ_Master` (Google Drive) but has since diverged —
**that doc is stale**; these files are current. Corrections applied here:

- Doors are **8PM** (was 9PM), whole run-of-show shifted, with a "subject to change
  based on location" callout.
- Age is **venue-set** ("typically 21+"), not an absolute. "No exceptions" attaches
  to bringing ID, not to the age.
- **Cold sparks are removed everywhere** — retired from all events.
- The promised experience is **video + game app + music**; anything else is framed
  as an unannounced bonus.
- The night's play is **in-app missions / mini games**, not crowd voting.
- Getting made takes an **email + a player nickname**.

Two things are intentionally NOT stated, and should not be added without a
decision from the show side:

1. **The loyalty ladder** (Associate → Boss, patches, VIP, name on the wall).
   Unresolved. Card 04 answers the question with "in the works" rather than
   promising tiers. The old five-rank markup was deleted, not commented out.
2. **Arcade → event carryover.** The Arcade block on card 03 presents global
   rankings and the in-room score as two separate boards, which is what they are.
   Nothing claims a character or score transfers into the night.

> Note: `templates/crew.html` in this repo does **not** match the live app — it mints
> a random member number and has no email/nickname signup, and the poll/vote system
> it ships is not what the event runs. Verify against the live app, not the
> templates, before writing new copy from this repo.

## Assets

- `gtad-logo-alpha.png` — the brand lockup with its black background converted to
  alpha, so it sits on the gradient instead of in a black box.
- Palette is read from `brands/gtad.json`: `#FF1493` / `#00E5E5` / `#ffc23d` on black.
- Type: Oswald (display), Inter (body), Barlow Condensed (labels), JetBrains Mono
  (tactical marks). All SIL OFL 1.1, fetched by `setup.sh`.
