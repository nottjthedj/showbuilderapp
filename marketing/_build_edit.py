#!/usr/bin/env python3
"""The assembly — the same clips in cut order, with a target length and a running timecode.

The shot sheet says what to generate; this says what to lay on the timeline and in
what order. Generated material runs about 2.5x the finished film, so every clip
carries a target cut length: the beat's on-screen duration from the show file,
shared out across its clips in proportion to how long each one was generated.
Targets, not gospel — the edit decides. But it turns 135 loose clips into a
timeline with a running clock on it.
"""
import json, math, re, pathlib
from collections import OrderedDict as O

ROOT = pathlib.Path(__file__).resolve().parent.parent
SHOW = json.load(open(ROOT / 'brands/gtad.show.json'))
SHEET = json.load(open(ROOT / 'marketing/shot-sheet.json'))
OUT = ROOT / 'marketing/edit-list.json'

BEATS = {b['tag']: b for b in SHOW['film']}
MIN_CUT = 1.5          # nothing on the timeline is shorter than this
# What each kind of shot is worth on the timeline. A fourth-wall turn is the point of
# the beat; an establishing shot has done its job the moment the place reads.
WEIGHT = {'ESTABLISH': 0.7, 'BUILD': 1.0, 'INSERT': 0.75, 'APPROACH': 1.15,
          'TURN': 1.6, 'HOLD': 1.35, 'OUT': 0.9, 'POST-CREDIT': 1.2}
ROLE_NOTE = {
    'ESTABLISH': 'Set the place. Cut out the moment it reads — these run long by design.',
    'BUILD': 'The scene. Carry the line; trim to the words plus a breath.',
    'INSERT': 'A cutaway. Short. It exists to hide a join or land a joke.',
    'APPROACH': 'He registers you. Cut INTO the turn on the matching head angle — this join '
                'should be invisible.',
    'TURN': 'The fourth wall. Do not trim the head of this one; the rotation is the shot.',
    'HOLD': 'He lands it. Hold past comfortable, then cut on the card.',
    'OUT': 'The exit. Cut on the hit — the music is doing the work here.',
    'POST-CREDIT': 'After everything. Let the room empty a little first.',
}


def target_seconds(tag):
    """The beat's on-screen length from the show file — '~40s', '~75s (longest…)'."""
    m = re.search(r'(\d+)\s*s', BEATS[tag]['dur'])
    return int(m.group(1)) if m else 40


clips_by_beat = O()
for c in SHEET['clips']:
    clips_by_beat.setdefault(c['beat'], []).append(c)

rows, t = [], 0.0
for tag, clips in clips_by_beat.items():
    b = BEATS[tag]
    target = target_seconds(tag)
    # A turn is not an establishing shot. Weight the share by what the role is doing,
    # then hold every clip above its own floor — a clip with a line must be at least
    # long enough to say it — and rescale whatever is still free to hit the target.
    weights = [WEIGHT.get(c['role'], 1.0) * c['seconds'] for c in clips]
    floors = [max(MIN_CUT, round((c['dialogue']['spokenSeconds'] + 0.8) * 2) / 2)
              for c in clips]
    cuts = [w / sum(weights) * target for w in weights]
    for _ in range(24):                       # settles in two or three
        under = [i for i, c in enumerate(cuts) if c < floors[i]]
        if not under:
            break
        for i in under:
            cuts[i] = floors[i]
        free = [i for i in range(len(cuts)) if i not in under]
        spare = target - sum(floors[i] for i in under)
        if not free or spare <= 0:
            break
        k = spare / sum(cuts[i] for i in free)
        for i in free:
            cuts[i] *= k
    cuts = [max(floors[i], round(c * 2) / 2) for i, c in enumerate(cuts)]
    beat_start = t
    for c, cut in zip(clips, cuts):
        line = next((l for l in c['dialogue']['lines'] if l['placement'] == 'on'), None)
        vo = next((l for l in c['dialogue']['lines'] if l['placement'] != 'on'), None)
        rows.append(O([
            ("tc", f"{int(t // 60)}:{t % 60:04.1f}"),
            ("at", round(t, 1)),
            ("id", c['id']), ("beat", tag), ("beatTitle", c['beatTitle']),
            ("role", c['role']),
            ("cut", cut), ("generated", c['seconds']),
            ("trim", round(c['seconds'] - cut, 1)),
            ("camera", c['camera']),
            ("subject", c['subject']),
            ("audio", ("dialogue: " + line['line']) if line else
                      (("V.O.: " + vo['line']) if vo else c['audio'])),
            ("note", ROLE_NOTE.get(c['role'], '')),
        ]))
        t += cut
    beats_music = b.get('music') or {}
    rows[-1] = rows[-1]  # readability: the marker below closes the beat
    rows.append(O([
        ("marker", True),
        ("tc", f"{int(t // 60)}:{t % 60:04.1f}"),
        ("at", round(t, 1)),
        ("beat", tag), ("beatTitle", b['title']),
        ("card", b.get('gameCard')),
        ("length", round(t - beat_start, 1)),
        ("target", target),
        ("music", beats_music),
    ]))

total = t
doc = O([
 ("meta", O([
   ("name", "The Score — assembly / edit list"),
   ("what", "Every clip in cut order with a target length and a running timecode. The order is "
            "the film's, locked. The lengths are a first pass — the beat's on-screen duration "
            "from the show file, shared across its clips in proportion to how long each was "
            "generated."),
   ("clips", sum(1 for r in rows if not r.get('marker'))),
   ("markers", sum(1 for r in rows if r.get('marker'))),
   ("runtime", round(total, 1)),
   ("runtimeText", f"{int(total // 60)}m {int(total % 60)}s"),
   ("generatedSeconds", SHEET['meta']['totalSeconds']),
   ("shootRatio", round(SHEET['meta']['totalSeconds'] / total, 2)),
 ])),
 ("howToAssemble", [
   "Lay the beats down in this order and do not reorder them. The run of show is locked to the "
   "app — the film and the games fire in sequence, so a beat moved in the edit is a beat moved "
   "in the room.",
   "Assemble at these lengths first, then loosen. It is far easier to let a good clip breathe "
   "than to find thirty seconds you don't have on the night.",
   "The APPROACH → TURN join is the one cut that has to be invisible. Match the head angle "
   "across it and the turn reads as one continuous move — that join is the whole fix.",
   "Never trim the head of a TURN. The rotation is the shot; losing its first frames is exactly "
   "the failure the three-clip structure exists to prevent.",
   "Game cards go on in post, over the last clip of the beat. Nothing is generated with text in "
   "it, so the card is yours to time.",
   "Cut picture first, then drop the recorded voices, then the music bed. The beat's music note "
   "says where to duck and where the drop lands.",
 ]),
 ("timeline", rows),
])
OUT.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + '\n')

# a plain CSV to keep next to the timeline while assembling
csv = ["timecode,clip,beat,role,cut_seconds,generated_seconds,trim_seconds,subject,note"]
for r in rows:
    if r.get('marker'):
        csv.append(f"{r['tc']},— MARKER —,{r['beat']},CARD,,,,,"
                   f"\"{(r['card'] or 'end of beat').replace(chr(34), '')}\"")
        continue
    csv.append(f"{r['tc']},{r['id']},{r['beat']},{r['role']},{r['cut']},{r['generated']},"
               f"{r['trim']},{r['subject']},\"{r['note']}\"")
(ROOT / 'marketing/edit-list.csv').write_text('\n'.join(csv) + '\n')

print(f"assembly: {doc['meta']['clips']} clips + {doc['meta']['markers']} beat markers | "
      f"runtime {doc['meta']['runtimeText']} | shooting {doc['meta']['shootRatio']}x what you cut")
short = [r['id'] for r in rows if not r.get('marker') and r['cut'] < MIN_CUT]
print('clips under the floor:', short or 'none')
over = [r['id'] for r in rows if not r.get('marker') and r['cut'] > r['generated']]
print('cuts longer than the material:', over or 'none')
