# Marketing — TJ is the face

> **Status: active.** This is the live campaign for **["The Score"](../brands/gtad.show.json)**,
> the show in use. (Not to be confused with `campaign/`, which is an archived draft built from
> the retired 24-night season.)

TJ — the Handler — fronts everything. Every post is him, to camera, talking to you. He is the
only voice in this world that addresses the audience directly, on screen and in the room, and
that consistency is the whole asset: by the time someone walks through the door they've been
listening to that voice for a month.

## What's here

| File | What it is |
|---|---|
| [`origin-story.md`](origin-story.md) | **The website story.** How the four gangs formed, what the vault is, and why all four are in one building on one night. Spoiler-safe. |
| [`daily-transmissions.json`](daily-transmissions.json) | **122 daily posts** — launch to the November show — 26–45s each: hook, on-screen text, full TJ script, shot list, caption, CTA and why each gets shared. Plus the 3-a-week tour cadence for after it. |
| [`how-to-play.md`](how-to-play.md) | **The explainer video** — 75–90s, built to kill the "will I get pulled on stage" objection. |
| [`shot-sheet.json`](shot-sheet.json) | **The master prompt sheet** — the whole film in 135 clips of ≤15s, each with a ready-to-paste prompt, its negative, the camera move and the audio under it. Built for a 15-second generation limit. |
| [`shot-list.json`](shot-list.json) | **The same 135 clips regrouped for generation** — 122 single-subject clips batched by character (seed + continuity lock + prompts), and the 13 two-or-more-subject clips split out and re-prompted with frame positions and per-subject lighting. |

## Generating the film — the turn needs three clips

The Rico test proved the look works and exposed one timing problem: **the fourth-wall turn happened
between two frames** — profile at 5.47s, full-face at 5.63s. That's an internal jump cut, not a turn,
and it happens because a single 15-second prompt was asked for four things (establish the room, light
a cigar, turn to camera, deliver a rant). Given four beats and fifteen seconds, the model snaps
through the one with no dialogue attached. That's always the turn.

So in [`shot-sheet.json`](shot-sheet.json) every turn is **three clips** — APPROACH (he registers
you, still quiet) → TURN (locked camera, the rotation is the only instruction) → HOLD (he finishes
and holds while the card lands). About 30–35 seconds of material for a beat that was trying to
happen in under a second.

The same test also showed the location changing three times in five seconds, so every clip's
negative now carries `location change, background change, jump cut`. Lock the subject and the set
with a reference frame before rolling.

**Batch by subject, not by scene.** `shot-list.json` regroups the same clips so you generate one
person's whole part in a sitting: seed first, lock the reference frame, work down. The 13 shots with
two or more established subjects in frame are pulled into their own list and done **last** — you need
every solo reference frame to exist before you can put two people in one frame, and those are the
shots where faces average together and subjects swap sides. Each carries explicit FRAME LEFT / FRAME
RIGHT positions, per-crew lighting, and negatives for merging and side-swapping.

**If your generator has a character feature, use it and say so.** The shot-list page has a switch
at the top — *"I've built these as characters in my tool"*. Off, every prompt carries the full
physical description, which is what a generator with no memory between clips needs. On, each prompt
calls the person by the name you gave the character and keeps only the action, the wardrobe beat,
the location, the lighting and the lens. Two descriptions of the same face compete, and the one
that wins isn't always yours. Type the name to match your tool exactly; it's remembered, and it
applies to the ensemble page too. Anyone you've already built can skip step 1 — the seed exists.

Prompt and negative are **two different fields**, and both get used: the prompt is what to make,
the negative is what to reject. If your tool only gives you one box, every clip has a **Copy both —
one box** button that joins them into `…prompt… Avoid: …negative…`.

**Generate ~2–2.5× what you cut.** 135 clips is 26 minutes of footage for a film that cuts to about
nine. That surplus is what lets you cut on the beat instead of using whatever the model handed you.

## The thing that makes the story work

The vault takes **four keys** — one per family, four colours, all turned inside the same minute.

That single rule does all the heavy lifting:

- **It explains why they're in one building.** No crew can open it alone. They physically need
  each other and they cannot stand it.
- **It explains the alliances and the betrayals.** Every team-up in the film is two crews who
  need a second key and trust nobody.
- **It explains why you're there.** A key gets a crew a turn. It doesn't get them the room —
  so all four are recruiting off the floor.
- **It pays off in the actual game.** The finale game *is* a four-colour code. The marketing
  isn't describing the night; it's teaching people how to win it.

## The calendar — dated to the show

First show is **Saturday 21 November 2026**. Posting starts **Saturday 1 August 2026** — 113 days
inclusive. Every post in `daily-transmissions.json` carries a real `date` and `weekday`, and the
last one lands on the door.

| Days | Phase | Dates | Job |
|---|---|---|---|
| 1–7 | **The offer** | Aug 1–7 | What this is, the vault, the four keys, why tonight, why you. |
| 8–31 | **The city** | Aug 8–31 | The four districts, the dial, the texture of the world. |
| 32–61 | **The families** | Sep | The fifty years that made this inevitable. |
| 62–92 | **The heat** | Oct | The keys move, the gala is announced, tickets go up, McGraw gets a lead. |
| 93–99 | **Final approach** | Nov 1–8 | Everybody's committed to something they can't undo. |
| 100–122 | **The countdown** | Nov 9–21 | The crews, the people, the games, the ask. |

**The dates that matter:**

| | Date | |
|---|---|---|
| Tickets go up | **Fri 2 Oct** | day 70 |
| The gala is announced | **Tue 6 Oct** | day 75 |
| All four crews RSVP | **Mon 12 Oct** | day 82 — *put money here*, the heist frame finally lands |
| The Combination | **Thu 19 Nov** | day 120 — *put money here*, the payoff |
| Pick your colour | **Fri 20 Nov** | day 121 — last identity push before doors |
| **Doors** | **Sat 21 Nov** | day 122 |

### The reserve bench

122 posts were written; there are 113 days. The 9 that didn't fit are **not deleted** — they're
benched, undated, marked `reserve: true`, and they're deliberately the cheapest to shoot:

`35 Is It A Rave Or A Show` · `42 Can I Come Alone` · `46 Doo-Wop And Menace` ·
`49 Timings` · `56 Photos` · `60 Double Nostalgia` · `67 Cold Rooms` · `74 The Scanner` ·
`81 State Broadcast`

Four HOUSE RULES and five THE DIAL — all shootable in an afternoon, none load-bearing for the
plot. **When a shoot day gets away from you, drop one of these in instead of skipping a day.**
That's what they're for. If the date moves later, they go back into the run.

## 122 posts is not 122 shoots

Seven recurring formats, so you **batch**. One lighting setup, one wardrobe, twenty `RAP SHEET`s
in an afternoon. Always be a month ahead.

| Format | What it is |
|---|---|
| **TRANSMISSION** | TJ to camera about the night itself. The only format that sells — use it for offers and asks. |
| **CITY RECORDS** | A piece of the fifty-year history, over archive-feel b-roll. VO only, no face needed. |
| **RAP SHEET** | One character, one file. The most batchable format you have. |
| **OVERHEARD** | One line somebody said, then what it meant. Shortest, highest share rate. |
| **THE DIAL** | The music. Your natural territory — shoot these behind the decks. |
| **EVIDENCE** | McGraw's case. This is the format that carries the myth. |
| **HOUSE RULES** | Practical. Kills objections, drives tickets, gets saved. |

A weekly rotation gives the audience a ritual: they learn that Tuesday is a character and
Saturday moves the mystery, and they come back for the one they like.

## After the first show — 3 a week

Once the tour starts, live footage exists and the job changes from *building a world* to
*proving it happened*. Drop to three, and make them count:

| Slot | What | Why |
|---|---|---|
| **Mon · PROOF** | The last show's best 30 seconds. Real crowd, real noise. No narration — let it be loud. | Nothing you can write beats a wide of 800 phones going up at once. |
| **Thu · TRANSMISSION** | TJ to camera. Lore, a character, or the next city's story. | The voice is the brand. Losing it between dates costs you what you spent four months building. |
| **Sat · THE ASK** | Next city, next date, tickets — cut over a clip from the last one. | A date announced over footage converts several times better than a poster. |

Everything in the calendar that isn't tied to the first event is **evergreen**. A new city gets
the run-up again, compressed to six weeks, with proof clips from the shows you've already done
cut in. And once there's a crowd, they shoot the PROOF slot for you.

## How you get people to share

Nobody shares an advert for a party. They share something that **says something about them**,
something that **settles an argument**, or something they **can't believe**. Every post is built
on one of six triggers:

**1 · Identity — pick a colour.** Choosing a faction is a self-description, and self-descriptions
get posted. Four crews means four tribes recruiting on your behalf for free. *Days 26 and 121 are the
most shareable posts in the run — a personality quiz with a door on the end. Re-run that format
whenever engagement dips; it always works.*

**2 · Argument — my crew beats your crew.** Every crew post is written to bait the other three.
The Firm posts exist partly to be disliked; a villain faction is a gift.

**3 · Secret — never explain the myth.** Sharing a mystery signals you're on the inside. The
moment the man with no face is explained, he stops moving. He is never explained before the
night — not in a caption, not in a reply, not to anybody.

**4 · Tag-a-friend — the characters are people they know.** Vinnie is somebody's cousin. Lil'
Problem is somebody's mate. Kayleigh is holding somebody's office together right now. These are
the posts that leave your audience and reach people who've never heard of the night.

**5 · Disbelief — the tiger.** Sugar robbing a summit of the two most dangerous men in the city
while neither notices is the most forwardable thing in this world. Deliberately run twice — day 86
frames her as a legend ("by weight, she's stolen more than anyone in this story"), day 110 tells
the incident itself. Don't overthink it and don't over-explain it.

**6 · Flex — you're made now.** The crew card, the member number and the leaderboard are proof
you were there. After the night the audience makes the recap content for you, which is the
thesis of the show anyway: the score was the room.

## Rules that don't bend

- **Hook in three seconds or it's dead.** Start mid-sentence. Never "hey guys", never "welcome
  to", never name the format. Lead with a number, a name, or a contradiction.
- **One idea per post.** If it needs two, it's two posts. There are 122 days — you never have to
  cram.
- **On-screen text is not the spoken line.** It's the punch underneath it.
- **Burned-in captions, always.** Most of this is watched on mute.
- **Brand at the end or nowhere.** A logo sting on the front of a 30-second video costs you the
  only three seconds that matter.
- **TJ replies in character. Always.** A comment answered by the Handler gets screenshotted, and
  that's worth more than the impression.
- **Never spoil the vault.** The film's ending is the one thing the room has to be there for.
