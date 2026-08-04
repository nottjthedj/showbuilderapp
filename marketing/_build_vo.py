#!/usr/bin/env python3
"""The recording script — every spoken line in the film, batched by voice.

Same principle as the shot list: you don't record a film in film order, you
record one voice until it's done and then move to the next. Pulled straight
from the master sheet so the lines can never drift out of sync with the prompts.
"""
import json
from collections import OrderedDict as O

SRC = json.load(open('/home/user/showbuilderapp/marketing/shot-sheet.json'))
LIST = json.load(open('/home/user/showbuilderapp/marketing/shot-list.json'))
OUT = '/home/user/showbuilderapp/marketing/voice-script.json'

NAMES = {c['key']: c['name'] for c in LIST['characters']}
NAMES['both'] = 'Don + Rico (in unison)'
COLOUR = {c['key']: c['colour'] for c in LIST['characters']}
COLOUR['both'] = '#f5c542'
ORDER = ["handler", "rico", "don", "marcus", "preston", "mcgraw", "president",
         "problem", "vinnie", "kayleigh", "both"]

DIRECTION = {
 ("on", "turn"): "Straight down the lens. This is the fourth-wall break — he is talking to "
                 "the room, not to another character.",
 ("on", "scene"): "In scene. He's talking to someone in the shot, not to you. Lower, faster, "
                  "less presentational.",
 "off": "Off-screen — the mouth is never visible, so this one is free. It still has to sound "
        "like it's coming from that room.",
 "vo": "Voice-over, over picture. No lip to match, so pace it to the length of the shot rather "
       "than the other way round.",
}

def direction(placement, role):
    if placement != 'on':
        return DIRECTION[placement]
    return DIRECTION[("on", "turn" if role in ('TURN', 'HOLD') else "scene")]

def picture(clip):
    """One line of what's on screen, so the read has something to sit against.

    The prompt opens with the character's physical description, which the person
    doing the voice already knows — strip it and keep the part that says where
    they are and what they're doing."""
    body = clip['prompt'].split('. SPOKEN')[0].split('. NO DIALOGUE')[0]
    body = body.rsplit(', ' + clip['camera'], 1)[0]
    for seed in SRC['seeds'].values():
        if body.startswith(seed):
            body = body[len(seed):].lstrip(', ')
            break
    return (body[:112].rsplit(' ', 1)[0] + '…') if len(body) > 112 else body

speakers = O()
for clip in SRC['clips']:
    for line in clip['dialogue']['lines']:
        k = line['speaker']
        speakers.setdefault(k, []).append(O([
            ("clip", clip['id']),
            ("beat", clip['beat']), ("beatTitle", clip['beatTitle']),
            ("role", clip['role']),
            ("placement", line['placement']),
            ("line", line['line']),
            ("words", len(line['line'].split())),
            ("clipSeconds", clip['seconds']),
            ("targetSeconds", round(len(line['line'].split()) / 2.3, 1)),
            ("direction", direction(line['placement'], clip['role'])),
            ("picture", picture(clip)),
            ("cue", clip['audio']),
        ]))

parts = []
for k in ORDER:
    rows = speakers.get(k)
    if not rows:
        continue
    for i, r in enumerate(rows, 1):
        r['slate'] = f"{k.upper()}-{i:02d}"
        r.move_to_end('slate', last=False)
    words = sum(r['words'] for r in rows)
    parts.append(O([
        ("key", k), ("name", NAMES.get(k, k)), ("colour", COLOUR.get(k, '#8f8fa6')),
        ("delivery", SRC['voices'].get(k) or ("both voices at once, in unison and flat — "
                                          "recorded separately and laid on top of each other, "
                                          "never performed together")),
        ("lineCount", len(rows)), ("words", words),
        ("minutes", round(words / 2.3 / 60, 1)),
        ("allVO", all(r['placement'] == 'vo' for r in rows)),
        ("lines", rows),
    ]))

doc = O([
 ("meta", O([
   ("name", "The Score — recording script"),
   ("what", "Every spoken line in the film, grouped by voice and ordered so one part can be "
            "recorded in a single sitting. Generated from the same master sheet as the prompts, "
            "so the words on the page are the words in the prompt."),
   ("parts", len(parts)),
   ("lines", sum(p['lineCount'] for p in parts)),
   ("words", sum(p['words'] for p in parts)),
   ("minutes", round(sum(p['words'] for p in parts) / 2.3 / 60, 1)),
 ])),
 ("howToRecord", [
   "Generate the picture first. The prompt already contains the line, so the clip comes back "
   "with a mouth saying those words — you are replacing the voice, not inventing the timing.",
   "Then record to picture, ADR-style, one part at a time. Play the clip, speak with the mouth "
   "on screen, and you get a sync that a blind read will never give you.",
   "Keep the delivery. It's on every part's card and it's written into the prompt the picture "
   "was generated from — a different read will fight the performance on screen.",
   "Record three takes of every line while the voice is warm: one as written, one faster and "
   "flatter, one bigger. The edit will want the choice and you will not want to come back.",
   "The target time is the words at a natural pace. It is not a limit — the clip is longer than "
   "the line on purpose, so there is air on both sides to cut on.",
   "Voice-over parts have no lip to match, so they can be recorded before anything exists. The "
   "Handler's 28 lines are the whole spine of the film and none of them need picture.",
 ]),
 ("parts", parts),
])

open(OUT, 'w').write(json.dumps(doc, indent=2, ensure_ascii=False) + '\n')
print(f"{doc['meta']['parts']} parts | {doc['meta']['lines']} lines | "
      f"{doc['meta']['words']} words | ~{doc['meta']['minutes']} min of finished voice")
for p in parts:
    print(f"  {p['name'][:34]:36} {p['lineCount']:3} lines  {p['minutes']:>4} min"
          + ("   (all voice-over — no picture needed)" if p['allVO'] else ""))
missing = [p['key'] for p in parts if not p['delivery']]
print('parts with no delivery note:', missing or 'none')
