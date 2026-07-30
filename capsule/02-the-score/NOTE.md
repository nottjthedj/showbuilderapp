# 02 — The Score (current)

**Status:** the only show in use.
**Built from:** the five production bibles (Master Production Bible, Sound & Music
Bible, Character Breakdown, B-Roll Action List, DaVinci creative handoff).

## What this version is

**One night.** A cutaway film in **14 beats** — Intro + 12 scenes + Finale — cut with
**12 games the whole room plays on their phones**. No props, nothing to hand out.

Every beat runs the same five-step shape:

`OPEN` establisher → `BUILD` the scene → **`TURN ◆`** the character looks down the lens
and hands the room its game → **`CARD ▮`** the game opens on every phone → `OUT` the
music slams back in.

- **`film[]`** — 14 beats: owner, station, energy, Handler VO, dialogue, the ◆ turn,
  the ▮ game card, the assembly and the bed/duck/slam music cue.
- **`games[]`** — the 12 app games, one per scene.
- **`characters[]`** — 7 leads with look, casting notes, sidekick and the turns they own.
  **Turns belong to the characters:** McGraw owns S1, Marcus 2/9/11, Rico 3/8, the Don 4,
  Preston 5/7; the Handler takes Intro, S12 and the Finale.
- **`stations[]`** — the room's radio dial: 4 gang sound-worlds + Law and State.
- **`energyArc[]` / `runOfShow`** — the curve peaking at S12, and the locked order.

## The one canon decision worth remembering

The production bibles ended on a **long con** — the Handler emptied the vault before the
doors opened and played all four gangs. That was dropped so **TJ stays the hero-host**.

The reframe: the faceless kingpin the four gangs fear is a **myth**. TJ is the real host,
and the vault is empty because *there was never money in it* — not because he emptied it.
Everything the bibles specify still works: the empty-vault reveal, the "— H." note on the
floor, McGraw's post-credit phone, the four bosses' "where's the money" round. The Finale
lands on *"the money was never the score — you were."*

**Never explain the myth.** He never appears, because he doesn't exist.

## Restore

```bash
cp capsule/02-the-score/gtad.show.json         brands/gtad.show.json
cp capsule/02-the-score/templates/handler.html templates/handler.html
cp capsule/02-the-score/templates/crew.html    templates/crew.html
python3 make_booth.py brands/gtad.json     # -> handler console (14 beats · 12 games)
```

## Also in here

`campaign/` — a copy of the **archived** lore-campaign draft, kept only because it was
snapshotted alongside this version. It is **not in use** and not part of the show or the
generated site: this capsule restores fine without it. Its home is
[`campaign/`](../../campaign/README.md) in the repo root.
