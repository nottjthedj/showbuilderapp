#!/usr/bin/env python3
"""Every script document, generated from the live show file and the prompt sheet.

Nothing here is hand-written. The show file is the source for the story, the
master sheet is the source for the shots, and the recording script is the source
for the voices — so a document can never quietly disagree with what gets built.
Run _build_all.py in marketing/ to regenerate everything in order.
"""
import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
HERE = ROOT / 'documents'
SHOW = json.load(open(ROOT / 'brands/gtad.show.json'))
SHEET = json.load(open(ROOT / 'marketing/shot-sheet.json'))
VOICE = json.load(open(ROOT / 'marketing/voice-script.json'))
EDIT = json.load(open(ROOT / 'marketing/edit-list.json'))

STAMP = ("> Generated from `brands/gtad.show.json` — do not edit by hand. "
         "Run `python3 documents/_build_documents.py` after changing the show file.\n")
FOOT = ("\n---\n\nGrand Theft After-Dark · “The Score”. Independent fan tribute event. "
        "Not affiliated with, endorsed by, or sponsored by Rockstar Games, Take-Two "
        "Interactive, or any related entity.\n")


def film_script():
    """The screenplay. What is said, in what order, and what the room does about it."""
    games = {g['n']: g for g in SHOW['games']}
    out = ["# The Score — film script\n", STAMP,
           "\nFourteen beats, locked in order. Every beat is the same shape: the world, the "
           "characters talking to each other, the turn to camera, and the game that turn hands "
           "to the room.\n"]
    for b in SHOW['film']:
        out.append(f"\n## {b['tag']} · {b['title']}\n")
        meta = [f"**{b['dur']}**", b['energy']]
        if b.get('satire'):
            meta.append(f"_{b['satire']}_")
        out.append(' · '.join(meta) + '\n')
        if b.get('vo'):
            out.append("\n**HANDLER (V.O.)**\n")
            for para in b['vo'].split('\n'):
                out.append(f"\n> {para}\n")
        for line in b.get('dialogue', []):
            if line.get('action'):
                out.append(f"\n_{line['action']}_\n")
            else:
                out.append(f"\n**{line['who']}**\n\n> {line['line']}\n")
        if b.get('turn'):
            out.append(f"\n### ◆ The turn — {(b.get('owner') or 'handler').upper()} to camera\n")
            for para in b['turn'].split('\n'):
                out.append(f"\n> {para}\n")
        if b.get('gameCard'):
            out.append(f"\n### ▮ {b['gameCard']}\n")
            g = games.get(b.get('game'))
            if g:
                out.append(f"\n{g['howItPlays']} **{g['win']}** ({g['time']})\n")
        if b.get('assembly'):
            out.append("\n**Assembly**\n\n")
            out += [f"{i}. **{step}** — {what}\n" for i, (step, what) in enumerate(b['assembly'], 1)]
        m = b.get('music') or {}
        if m:
            bits = [f"_{v}_" if k == 'bed' else v for k, v in m.items() if v]
            out.append("\n**Music** — " + ' · '.join(bits) + "\n")
    return ''.join(out) + FOOT


def voice_script():
    """The same lines, grouped by who says them, for the recording session."""
    m = VOICE['meta']
    out = ["# The Score — voice-over script\n",
           "> Generated from `marketing/voice-script.json`, which is generated from the master "
           "prompt sheet — the words here are the words in the generation prompts.\n",
           f"\n**{m['lines']} lines · {m['words']} words · ~{m['minutes']} minutes of finished "
           f"audio across {m['parts']} parts.** Grouped by voice, not by scene: record one part "
           "until it's done, then move to the next.\n",
           "\n## How to record it\n\n"]
    out += [f"{i}. {t}\n" for i, t in enumerate(VOICE['howToRecord'], 1)]
    out.append("\n| Part | Lines | Words | Time | Needs picture |\n|---|---|---|---|---|\n")
    for p in VOICE['parts']:
        out.append(f"| {p['name']} | {p['lineCount']} | {p['words']} | ~{p['minutes']} min | "
                   f"{'no — pure voice-over' if p['allVO'] else 'yes'} |\n")
    for p in VOICE['parts']:
        out.append(f"\n---\n\n## {p['name']}\n")
        out.append(f"\n**The voice** — {p['delivery']}\n")
        out.append(f"\n{p['lineCount']} line{'s' if p['lineCount'] != 1 else ''} · "
                   f"~{p['minutes']} min"
                   + (" · every line is voice-over, so none of it needs picture to record against"
                      if p['allVO'] else "") + "\n")
        for l in p['lines']:
            out.append(f"\n### {l['slate']} · {l['clip']} · {l['beat']} {l['beatTitle']}\n")
            out.append(f"\n> {l['line']}\n")
            out.append(f"\n_{l['direction']}_\n")
            out.append(f"\n`{l['words']} words · target {l['targetSeconds']}s · "
                       f"the shot is {l['clipSeconds']}s`\n")
            out.append(f"\nOver: {l['picture']}\n")
    return ''.join(out) + FOOT


def shooting_script():
    """The bridge: the script in shot order, so the page you read matches the clip you generate."""
    out = ["# The Score — shooting script\n",
           "> Generated from `marketing/shot-sheet.json` — the same clips, in film order, "
           "written to be read rather than pasted. The prompts themselves are in the shot sheet "
           "and the shot list.\n",
           f"\n**{SHEET['meta']['clips']} clips · {SHEET['meta']['totalSeconds']}s of generated "
           f"material.** Every clip is 15 seconds or less and holds one idea and one camera move. "
           "Every fourth-wall turn is three clips — APPROACH, TURN, HOLD.\n"]
    beat = None
    for c in SHEET['clips']:
        if c['beat'] != beat:
            beat = c['beat']
            out.append(f"\n## {c['beat']} · {c['beatTitle']}\n")
        picture = c['prompt'].split('. SPOKEN')[0].split('. NO DIALOGUE')[0]
        picture = picture.rsplit(', ' + c['camera'], 1)[0]
        out.append(f"\n**{c['id']} · {c['role']} · {c['seconds']}s** — {c['camera']}"
                   + (f" · subject: {c['subject']}" if c['subject'] != '—' else "") + "\n")
        out.append(f"\n{picture}\n")
        for l in c['dialogue']['lines']:
            tag = {'on': '', 'off': ' (off-screen)', 'vo': ' (V.O.)'}[l['placement']]
            out.append(f"\n**{l['speaker'].upper()}{tag}**\n\n> {l['line']}\n")
        if c['dialogue']['kind'] == 'silent' and c['subject'] not in ('—', 'handler'):
            out.append("\n_No line — the prompt holds the mouth closed._\n")
        if '→' in c['audio'] or '◆' in c['audio']:
            out.append(f"\n`{c['audio']}`\n")
    return ''.join(out) + FOOT


def edit_assembly():
    """The cut order with a running clock — what goes on the timeline, and how long."""
    m = EDIT['meta']
    out = ["# The Score — the assembly\n",
           "> Generated from `marketing/edit-list.json`. Cut order, not shooting order.\n",
           f"\n**{m['clips']} cuts · {m['runtimeText']} finished · shooting {m['shootRatio']}x "
           f"what gets used.** The order is the film's and it is locked — the app fires the games "
           f"in this sequence, so a beat moved in the edit is a beat moved in the room. The "
           f"lengths are a first pass: each beat's on-screen duration from the show file, shared "
           f"across its clips by what the shot is doing. The edit decides.\n",
           "\n## How to assemble it\n\n"]
    out += [f"{i}. {t}\n" for i, t in enumerate(EDIT['howToAssemble'], 1)]
    beat = None
    for r in EDIT['timeline']:
        if r.get('marker'):
            if r.get('card'):
                out.append(f"\n**▮ {r['card']}** — card goes on in post.\n")
            mus = r.get('music') or {}
            if mus:
                out.append("\n" + ' · '.join(f"**{k.title()}:** {v}" for k, v in mus.items() if v)
                           + "\n")
            out.append(f"\n`{r['beat']} runs {r['length']}s against a {r['target']}s target · "
                       f"clock now {r['tc']}`\n")
            continue
        if r['beat'] != beat:
            beat = r['beat']
            out.append(f"\n## {r['beat']} · {r['beatTitle']}\n")
            out.append("\n| At | Clip | Role | Cut | Of | Sound |\n|---|---|---|---|---|---|\n")
        out.append(f"| {r['tc']} | **{r['id']}** | {r['role']} | **{r['cut']}s** | {r['generated']}s "
                   f"| {r['audio'].replace('|', '/')} |\n")
    return ''.join(out) + FOOT


def index():
    m, v, s = SHOW['meta'], VOICE['meta'], SHEET['meta']
    turns = sum(1 for c in SHEET['clips'] if c['role'] in ('APPROACH', 'TURN', 'HOLD'))
    return f"""# Documents — the script files

Everything readable about **“The Score”** in one place. All of it is generated; the sources are
the live show file and the prompt sheets, so nothing here can drift out of step with what gets
built or shot.

| Document | What it is |
|---|---|
| [`the-film-script.md`](the-film-script.md) | **The screenplay.** All {len(SHOW['film'])} beats in locked order — voice-over, dialogue, the turn to camera, the game card it hands to the room, the assembly and the music under it. |
| [`voice-over-script.md`](voice-over-script.md) | **The recording script.** All {v['lines']} spoken lines grouped by voice with delivery, direction and target length. ~{v['minutes']} minutes of audio for the whole cast. |
| [`edit-assembly.md`](edit-assembly.md) | **The assembly.** The cut order with a running clock — every clip, how long it runs in the film, what sound is on it, and where each game card lands. {EDIT['meta']['runtimeText']} finished. |
| [`shooting-script.md`](shooting-script.md) | **The shooting script.** The same film in {s['clips']} generatable clips, in film order, written to read — picture, camera, line. |
| [`the-story.md`](the-story.md) | **The story told straight.** The narration script — no format, no game cards, just what happens and why. |

## The show files these come from

| File | What it is |
|---|---|
| [`../brands/gtad.show.json`](../brands/gtad.show.json) | **The show.** The single source of truth — {len(SHOW['film'])} film beats, {len(SHOW['games'])} games, {len(SHOW['characters'])} characters, {len(SHOW['stations'])} stations, the locked run of show. |
| [`../marketing/shot-sheet.json`](../marketing/shot-sheet.json) | The master prompt sheet — {s['clips']} clips of ≤15s with prompts, negatives and dialogue. |
| [`../marketing/shot-list.json`](../marketing/shot-list.json) | The same clips regrouped by subject for generation. |
| [`../marketing/voice-script.json`](../marketing/voice-script.json) | The recording script as data. |
| [`../marketing/edit-list.json`](../marketing/edit-list.json) | The assembly as data, plus `edit-list.csv` to keep open while cutting. |
| [`../marketing/`](../marketing/) | The campaign — {len(SHOW['film'])}-beat film aside, this is the 122-post run-up to the first show. |

## The numbers

- **{len(SHOW['film'])} beats**, {s['clips']} clips, {s['totalSeconds']}s ({round(s['totalSeconds']/60, 1)} min) of generated material for a film that cuts to about nine minutes.
- **{turns} of those clips are turn sequences** — every fourth-wall break is APPROACH → TURN → HOLD, never one clip.
- **{v['lines']} spoken lines**, {v['words']} words, ~{v['minutes']} minutes of finished voice across {v['parts']} parts.
- **{len(SHOW['games'])} games**, one per beat after the intro, in a locked order.

## Regenerating

```
python3 marketing/_build_all.py      # sheet → list → voices → these documents
```

Or on its own, once the JSON is current:

```
python3 documents/_build_documents.py
```

Edit the show file or the sheet builders — never these documents. They get overwritten.
{FOOT}"""


STORY = ROOT / 'capsule/02-the-score/THE_STORY.md'
files = {
    'README.md': index(),
    'the-film-script.md': film_script(),
    'voice-over-script.md': voice_script(),
    'shooting-script.md': shooting_script(),
    'edit-assembly.md': edit_assembly(),
    'the-story.md': STORY.read_text() if STORY.exists() else None,
}
HERE.mkdir(exist_ok=True)
for name, text in files.items():
    if text is None:
        print(f'  skipped {name} — source missing')
        continue
    (HERE / name).write_text(text)
    print(f'  {name:26} {len(text.split()):6} words')
print(f'documents/: {sum(1 for t in files.values() if t)} files')
