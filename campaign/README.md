# The lore campaign

The 24-night season used to be the live show. It isn't any more — **["The Score"](../brands/gtad.show.json)**
is, a 14-beat cutaway film cut with 12 phone games in one night.

So the season got a better job. It's the **prequel**: a 24-drop social and web-video
campaign that runs *before* the show and teaches the audience the world — the four
gangs, the vault, the myth — so the room already knows who everybody is when it walks in.

## What's here

| File | What it is |
|---|---|
| `gtad-lore-season.json` | **The source.** The 24 written transmissions, preserved verbatim from the season, plus the retired prop-game playbook. Nothing in here is generated — it's the writing. |
| `gtad-social-campaign.json` | **The campaign.** 24 drops: hook, what it teaches, what it ladders into, the VO, caption, CTA, shot list and the platform cuts. |

The prop missions in the season file are **retired from the live show** — The Score's
games are all on the phone. They're kept because the writing is good and the fourth-wall
scenes may be worth mining for content; they are not a run sheet any more.

## The arc

| Drops | Phase | Job |
|---|---|---|
| 1–8 | **Act I — build the world** | One crew per drop. By drop 8 all four gangs are named in a single post: the campaign's anchor. |
| 9–16 | **Act II — build the stakes** | The vault, the heat, the rat, the State. **Drop 15 is the ticket announce** and 16 is last call. |
| 17–24 | **Act III — the show and after** | 17 is day-of. Then proof, community, the next date, and the payoff: the vault was empty, the score was the room. |

Pin the calendar to the event date and work backwards from **drop 15** — that's the one
carrying the ticket drive. One drop a week runs six months; three a week runs two.

## How a drop is built

Each drop already has its `vo` — that's the night's transmission, written and finished.
Everything else in the entry is the wrapper:

- **`hook`** — the first two seconds. If this doesn't land, nothing else in the drop matters.
- **`teaches`** — the one thing the audience should know afterwards. One per drop, never two.
- **`laddersTo`** — which character, gang or beat of The Score this seeds, so the campaign
  and the film stay one story.
- **`shots`** — what to generate or shoot, drawn from the B-roll buckets.
- **`cuts`** — 9:16 :30 for Reels/TikTok/Shorts, 9:16 :15 for paid, 16:9 :45–:60 for the site.

## The rules that don't bend

- **AI generates worlds, wheels and action — never a hero face.** Any human in a generated
  shot is absent, distant, back-turned, silhouetted or out of focus. Every face is a real actor.
- **The film is period-locked 1977–1983.** Run every clip, generated and filmed, through the
  house grade so one look unifies them.
- **No text in-gen.** Titles, banners and the "— H." note go on in post.
- **Never explain the myth.** The man with no face only works while the audience is still
  guessing. He never appears in the film either — because he doesn't exist.
