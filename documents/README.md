# Documents — the script files

Everything readable about **“The Score”** in one place. All of it is generated; the sources are
the live show file and the prompt sheets, so nothing here can drift out of step with what gets
built or shot.

| Document | What it is |
|---|---|
| [`the-film-script.md`](the-film-script.md) | **The screenplay.** All 14 beats in locked order — voice-over, dialogue, the turn to camera, the game card it hands to the room, the assembly and the music under it. |
| [`voice-over-script.md`](voice-over-script.md) | **The recording script.** All 99 spoken lines grouped by voice with delivery, direction and target length. ~5.7 minutes of audio for the whole cast. |
| [`shooting-script.md`](shooting-script.md) | **The shooting script.** The same film in 135 generatable clips, in film order, written to read — picture, camera, line. |
| [`the-story.md`](the-story.md) | **The story told straight.** The narration script — no format, no game cards, just what happens and why. |

## The show files these come from

| File | What it is |
|---|---|
| [`../brands/gtad.show.json`](../brands/gtad.show.json) | **The show.** The single source of truth — 14 film beats, 12 games, 7 characters, 6 stations, the locked run of show. |
| [`../marketing/shot-sheet.json`](../marketing/shot-sheet.json) | The master prompt sheet — 135 clips of ≤15s with prompts, negatives and dialogue. |
| [`../marketing/shot-list.json`](../marketing/shot-list.json) | The same clips regrouped by subject for generation. |
| [`../marketing/voice-script.json`](../marketing/voice-script.json) | The recording script as data. |
| [`../marketing/`](../marketing/) | The campaign — 14-beat film aside, this is the 122-post run-up to the first show. |

## The numbers

- **14 beats**, 135 clips, 1573s (26.2 min) of generated material for a film that cuts to about nine minutes.
- **54 of those clips are turn sequences** — every fourth-wall break is APPROACH → TURN → HOLD, never one clip.
- **99 spoken lines**, 787 words, ~5.7 minutes of finished voice across 11 parts.
- **12 games**, one per beat after the intro, in a locked order.

## Regenerating

```
python3 marketing/_build_all.py      # sheet → list → voices → these documents
```

Or on its own, once the JSON is current:

```
python3 documents/_build_documents.py
```

Edit the show file or the sheet builders — never these documents. They get overwritten.

---

Grand Theft After-Dark · “The Score”. Independent fan tribute event. Not affiliated with, endorsed by, or sponsored by Rockstar Games, Take-Two Interactive, or any related entity.
