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
        'clips': clips,
    })

missing = [b['tag'] for b in beats if not b['clips']]
assert not missing, f'beats with no clips: {missing}'
counted = sum(len(b['clips']) for b in beats)
assert counted == len(SHEET['clips']), f'{counted} clips placed, sheet has {len(SHEET["clips"])}'

data = {
    'meta': {
        'beats': len(beats),
        'clips': counted,
        'seconds': SHEET['meta']['totalSeconds'],
        'minutes': round(SHEET['meta']['totalSeconds'] / 60, 1),
    },
    'beats': beats,
}
html = (HERE / '_hub_template.html').read_text().replace(
    '/*__DATA__*/null', json.dumps(data, ensure_ascii=False))
OUT.write_text(html)
print(f'{OUT.name} | {len(beats)} beats | {counted} clips | {round(len(html)/1024)} KB')
