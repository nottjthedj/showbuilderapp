# 01 — The season (24 nights)

**Frozen at:** commit `24d59ff` — the last state before GTAD pivoted to The Score.
**Status:** archived — not in use. Fully restorable.

## What this version is

A **24-night residency season**. Every night is one chapter of a three-act story, and
the room plays physical games on stage between the story beats.

- **24 chapters** — each with a codename, an act, the night's job, its `endsOn`
  cliffhanger, and a bespoke Handler transmission. Every night opens on the previous
  night's cliffhanger, so the season reads as one arc from THE RECRUITMENT to THE LEGEND.
- **11 missions** — physical prop games (the lineup, balloon chase, Nerf gallery, dead
  drop, wristband rat hunt, beach-ball vault, streamer laser grid, memory grid, key
  bucket, tug of war, cup stack). Each carries props, how-it-runs, the win condition,
  and a full **8-beat scene script**: cue → 4th wall → story driver (keyed by act) →
  rules → call-up → ad-libs → win → out.
- **`rotation`** — three pre-picked mission sets (first night / returning city / small room).

TJ is the star Handler throughout, hero-host, no con.

## How it differs from The Score

|  | This version | The Score |
|---|---|---|
| Shape | 24 nights, a season | 1 night, a film |
| Games | 11 physical, on stage | 12 digital, on phones |
| Props | Nerf, balloons, cups, rope, buckets | none — everything is in the app |
| Who talks to the room | TJ, every time | the characters own their own turns |
| Run order | pick a chapter + 3 missions per night | locked, Intro → Finale |

## Restore

```bash
cp capsule/01-season-24-nights/gtad.show.json         brands/gtad.show.json
cp capsule/01-season-24-nights/templates/handler.html templates/handler.html
cp capsule/01-season-24-nights/templates/crew.html    templates/crew.html
python3 make_booth.py brands/gtad.json     # -> handler console (24 chapters · 11 missions)
```

The console must come with the show file — The Score's console cannot render chapters
or missions, and this console cannot render film beats.

## Also on the shelf

A draft lore campaign was built from these 24 transmissions —
see [`campaign/`](../../campaign/README.md). It is **not in use either**. This capsule is
the *runnable show*; that folder is the same writing reworked as social drops. Both are
archived: the only show in use is The Score.
