#!/usr/bin/env python3
"""The production hub — script and prompts in film order, with a progress tick per clip.

Joins the show file (what the beat is) to the master sheet (what to generate) so
there is one page to work from instead of three.
"""
import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
HERE = ROOT / 'marketing'
SHOW = json.load(open(ROOT / 'brands/gtad.show.json'))
SHEET = json.load(open(ROOT / 'marketing/shot-sheet.json'))
GAMES = {g['n']: g for g in SHOW['games']}
LIST = json.load(open(ROOT / 'marketing/shot-list.json'))
BRIDGE = json.load(open(ROOT / 'marketing/bridge-shots.json'))
BROLL = {}
for t in BRIDGE['textureList']:
    if t['required']:
        BROLL[t['beat']] = BROLL.get(t['beat'], 0) + 1
OUT = HERE / 'production-hub.html'

by_beat = {}
for c in SHEET['clips']:
    by_beat.setdefault(c['beat'], []).append({
        k: c[k] for k in ('id', 'role', 'seconds', 'camera', 'subject', 'full', 'fullSafe',
                          'fullSafest', 'negative', 'dialogue')
    })

beats = []
for b in SHOW['film']:
    clips = by_beat.get(b['tag'], [])
    game = GAMES.get(b.get('game'))
    beats.append({
        'tag': b['tag'], 'title': b['title'],
        'slug': b['tag'].replace(' ', ''),
        'colour': b.get('color') or '#8f8fa6',
        'dur': b['dur'], 'energy': b['energy'],
        'vo': b.get('vo'), 'dialogue': b.get('dialogue', []), 'turn': b.get('turn'),
        'gameCard': b.get('gameCard'),
        'game': {k: game[k] for k in ('howItPlays', 'win', 'time')} if game else None,
        'seconds': sum(c['seconds'] for c in clips),
        'broll': BROLL.get(b['tag'], 0),
        'plates': sum(1 for c in clips if c['subject'] == '—'),
        'clips': clips,
    })

missing = [b['tag'] for b in beats if not b['clips']]
assert not missing, f'beats with no clips: {missing}'
counted = sum(len(b['clips']) for b in beats)
assert counted == len(SHEET['clips']), f'{counted} clips placed, sheet has {len(SHEET["clips"])}'

# --- for anyone who didn't write it -----------------------------------------
# A page a teammate can open cold. The synopsis is the whole film including the
# ending, because whoever is cutting it needs to know what they are building
# toward; the marketing never says it.
STORY = [
 ("The pitch", "Four crews. One city. One vault with eight figures in it, and one night when "
  "all four of them try to open it. The film plays in " + str(len(SHOW['film'])) + " beats "
  "between the music, and every beat ends with a character turning to the lens and handing the "
  "room a game.", False),
 ("Why they are all in one building", "The vault takes four keys — one per family, four colours, "
  "all turned inside the same minute. No crew can open it alone. That single rule explains the "
  "alliances, the betrayals, and why all four are recruiting off the floor: a key buys a crew a "
  "turn, it doesn't buy them the room.", False),
 ("The crews", "The Corvettis think it's about respect. Los Halcóns think it's about power. The "
  "Street Kings think it's about loyalty. The Firm thinks it's a spreadsheet. Each owns a colour, "
  "a district and a station on the room's radio dial — gold, hot pink, cyan, violet.", False),
 ("The man they're all afraid of", "Every crew believes a faceless kingpin runs this city. He is "
  "a myth: what a room invents when it can't explain a good night. Detective Dutch McGraw has "
  "spent twenty years hunting him. Never explain him — not in a caption, not in a reply, not "
  "before the night.", False),
 ("What the audience actually does", "Nobody gets pulled on stage. Everyone plays on their own "
  "phone. Twelve games, one per beat after the intro, in a locked order — a beat moved in the "
  "edit is a beat moved in the room.", False),
 ("How every beat is shaped", "The world, then the characters talking to each other, then the "
  "◆ turn to camera, then the ▮ card that opens the game. The turn is the frame the live show "
  "cannot run without, which is why it is generated as three clips — approach, turn, hold — "
  "instead of one.", False),
 ("The ending", "The vault is empty. Not emptied — empty. There was never money in it, because "
  "the man who was supposed to have filled it never existed. All four bosses stand in the "
  "doorway asking the same question. McGraw bursts in and arrests the President, who is "
  "delighted. A folded note on the floor is signed “— H.” The score was the room.", True),
]

SUPPORT = {
 "vinnie": "The Don's son. Sweats through every shirt he owns and asks the questions the Don "
           "finds exhausting.",
 "problem": "Marcus's passenger. Always eating, always talking, currently founding a taco empire "
            "with money nobody has stolen yet.",
 "kayleigh": "The Firm's analyst. Watched the entire founder demo and has notes — chiefly that "
             "the leak is Preston, because Preston posts everything.",
 "sugar": "Rico's Bengal tiger. Furniture that happens to be alive, and by weight the most "
          "successful thief in the film.",
}
STATION_OF = {c['id']: c.get('station') for c in SHOW['characters']}
LEAD = {c['id']: c for c in SHOW['characters']}
CREW = {"gold": "The Corvettis", "pink": "Los Halcóns", "cyan": "The Street Kings",
        "violet": "The Firm", "law": "The Law", "state": "The State", "—": ""}

cast = []
for ch in LIST['characters']:
    if ch['key'] == 'none':
        continue
    lead = LEAD.get(ch['key'])
    cast.append({
        'key': ch['key'], 'name': ch['name'], 'colour': ch['colour'],
        'crew': CREW.get(STATION_OF.get(ch['key'], '—'), ''),
        'role': (lead or {}).get('role') or SUPPORT.get(ch['key'], ''),
        'look': ch['lock'],
        'voice': SHEET['voices'].get(ch['key']),
        'clips': ch['clipCount'],
        'beats': ch['beats'],
        'note': (lead or {}).get('note'),
    })

data = {
    'story': [{'h': h, 'p': t, 'spoiler': sp} for h, t, sp in STORY],
    'cast': cast,
    'meta': {
        'beats': len(beats),
        'clips': counted,
        'seconds': SHEET['meta']['totalSeconds'],
        'minutes': round(SHEET['meta']['totalSeconds'] / 60, 1),
        'tagline': SHOW['meta']['sub'],
        'format': SHOW['meta']['format'],
        'games': len(SHOW['games']),
        'cast': len(cast),
    },
    'beats': beats,
}
html = (HERE / '_hub_template.html').read_text().replace(
    '/*__DATA__*/null', json.dumps(data, ensure_ascii=False))
OUT.write_text(html)
print(f'{OUT.name} | {len(beats)} beats | {counted} clips | {round(len(html)/1024)} KB')
