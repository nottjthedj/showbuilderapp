#!/usr/bin/env python3
"""Bridges — the cheap material that makes the cuts work.

Three tiers, deliberately in this order:

  1. Editorial fixes that cost nothing. Most abrupt joins are fixed in Resolve
     with a punch-in or a different cut point, not with another render.
  2. A tiny element library. Six people-free clips, generated once, reused at
     every join in the film and tinted per crew on the colour page.
  3. Textures per beat. Two each, no people in frame — so no character
     reference, no continuity risk, and nothing for a content filter to catch.

It also works out which joins actually need help: two locked shots of the same
person in a row is a jump cut waiting to happen, and the film has plenty.
"""
import json, pathlib
from collections import OrderedDict as O

ROOT = pathlib.Path(__file__).resolve().parent.parent
SHEET = json.load(open(ROOT / 'marketing/shot-sheet.json'))
SHOW = json.load(open(ROOT / 'brands/gtad.show.json'))
OUT = ROOT / 'marketing/bridge-shots.json'
B = SHEET['blocks']
NEG_PLATE = ", ".join([B['NEG'], B['NEG_PERIOD'], B['NEG_MOTION'],
                       "people, human figure, face, hands, crowd"])

FREE = [
 ("Punch in on every other shot.", "Three locked shots of the same man at the same size will "
  "always cut badly. Scale the middle one up 12–18% in Resolve and the size changes, which is "
  "the thing that makes a cut read. Costs nothing, needs no render, and it is what a second "
  "camera would have given you anyway."),
 ("Cut on the word, not the pause.", "Land the cut mid-phrase and the ear carries the join. "
  "Cutting in a silence puts all the weight on the picture, which is exactly where the seam is."),
 ("Never bridge the APPROACH → TURN join.", "That one is meant to be invisible — match the head "
  "angle across it and it reads as one continuous rotation. Putting a flare or a cutaway in there "
  "destroys the only thing the three-clip structure buys you."),
 ("Let the outgoing shot run under the incoming audio.", "Start the next line two or three frames "
  "before you cut to it. A J-cut hides a hard join better than any transition element."),
 ("Use the insert you already generated.", "Every beat has an INSERT clip that exists for exactly "
  "this. If a join is ugly, the cutaway usually belongs there rather than where the list puts it."),
]

# People-free, location-free, reusable everywhere. Generate once.
ELEMENTS = [
 ("BR-01", "Flare pass", 3,
  "a single bright anamorphic lens flare streaking horizontally across a black frame, "
  "volumetric haze, halation bloom, heavy organic 35mm film grain, no subject, no text",
  "The workhorse. Tint it gold, pink, cyan or violet on the colour page — one render covers "
  "all four crews. Two to four frames over a cut hides almost anything."),
 ("BR-02", "Film burn", 3,
  "an orange-white 35mm film burn flash blooming and dying, halation, dust and hair in the gate, "
  "sprocket flicker, on black, no subject, no text",
  "For beat-to-beat transitions rather than shot-to-shot. This is the one that makes the whole "
  "thing feel like it came off a projector."),
 ("BR-03", "Smoke pass", 4,
  "thick cigar smoke curling slowly across frame, lit hard from one side, deep black background, "
  "volumetric, shallow depth of field, no subject, no text",
  "A foreground wipe. Lay it over the tail of one shot and the head of the next at 60% opacity "
  "and the join disappears under it."),
 ("BR-04", "Mirror glint", 3,
  "a hard specular glint sweeping across a mirrored surface, fragmented neon reflections, "
  "shallow focus, deep shadow, no subject, no text",
  "Scene 3 and Scene 12 specifically — mirrored mansion, four-colour ballroom. It carries the "
  "set's own texture across the cut."),
 ("BR-05", "Streak whip", 2,
  "streaks of neon light whipping horizontally past camera in extreme motion blur, rain-slick "
  "reflections, night, no subject, no text",
  "The fastest option — under half a second on the timeline. Use it where the energy is already "
  "high and you want the cut to feel like impact rather than a transition."),
 ("BR-06", "CRT roll", 3,
  "extreme macro of CRT phosphor scanlines rolling and breaking into static, green-white glow, "
  "curved glass, no subject, no text",
  "The Firm, the broadcasts, the surveillance beats. Also the honest way into and out of any "
  "shot that is meant to be footage of footage."),
]

# Two per beat, no people, matched to that beat's set.
TEXTURES = O([
 ("INTRO", [("Rain on glass", "rain running down a floor-to-ceiling penthouse window at night, "
             "a rain-soaked neon skyline thrown out of focus behind it"),
            ("Ice and crystal", "a crystal tumbler of amber spirit on a black marble ledge, neon "
             "edge light through the glass, condensation")]),
 ("SCENE 1", [("Blinds and siren", "venetian blinds throwing red and blue siren light across an "
               "empty precinct wall, dust turning in the beams"),
              ("The file", "a battered manila case file on a scratched metal desk under one hard "
               "lamp, coffee ring, paper edges curling")]),
 ("SCENE 2", [("Mirror lights", "a rear-view mirror at night filling with red and blue light, "
               "out-of-focus street beyond, wet glass"),
              ("Hydraulics", "extreme close-up of a chrome lowrider wheel and hydraulic strut "
               "bouncing on wet asphalt, cyan neon reflection")]),
 ("SCENE 3", [("Cigar ash", "extreme macro of a cigar burning down in a heavy crystal ashtray, "
               "ash falling, hot-pink neon rim light, smoke curling"),
              ("Mirrors doubling", "a mirrored mansion wall reflecting hot-pink neon into infinity, "
               "shallow focus, drifting haze, no people")]),
 ("SCENE 4", [("Cannoli and cloth", "a plate of cannoli on a red checkered tablecloth under a low "
               "warm lamp, crumbs, an espresso cup at the edge"),
              ("The rotary phone", "macro of a black rotary telephone on dark wood, gold lamp light "
               "raking across the dial")]),
 ("SCENE 5", [("Monitor wall", "a wall of CRT surveillance monitors flickering through four "
               "different night streets, violet glow, scan lines"),
              ("Cold water", "a bottle of water sweating on a black glass desk under cold violet "
               "light, server LEDs bokeh behind")]),
 ("SCENE 6", [("Gold meets pink", "an empty warehouse interior where warm gold light from one side "
               "meets hot pink from the other, dust turning in the seam between them"),
              ("Crates and worklights", "stacked wooden crates under a hanging worklight swinging "
               "very slightly, long shadows moving across the floor")]),
 ("SCENE 7", [("Wires", "macro of a tangle of coloured wires and a ticking countdown readout on "
               "pure black, faint flicker"),
              ("Red wash", "an empty steel workbench as the whole room flips to emergency red, "
               "violet fighting the red, haze")]),
 ("SCENE 8", [("Blueprint glow", "glowing blue-cyan schematic icons projected on frosted glass in "
               "a dark room, thin lines, drifting dust"),
              ("Projector beam", "a projector beam cutting through haze in a dark planning room, "
               "the lens flaring, no people")]),
 ("SCENE 9", [("Chrome line", "a line of chrome lowriders parked under cyan neon on wet asphalt, "
               "reflections stretching toward camera"),
              ("Corner store", "a cyan-lit corner store window at night, steam from a grate "
               "crossing frame, hand-painted signage out of focus")]),
 ("SCENE 10", [("Five lights", "five drag-strip starting lights glowing above a rain-soaked pier, "
                "rain streaking through the beams, harbour fog"),
               ("Wet boards", "rain hammering wet reflective pier boards at night, gold and pink "
                "light bleeding across the water")]),
 ("SCENE 11", [("Searchlight sweep", "a searchlight beam sweeping across a wet brick alley wall, "
                "steam rising, the beam passing off into darkness"),
               ("Spray can", "macro of a spray can nozzle releasing a fine mist of cyan paint in "
                "cold night air, backlit")]),
 ("SCENE 12", [("Four-colour lock", "a giant four-colour combination vault lock glowing gold, hot "
                "pink, cyan and violet in a dark ballroom, slow dust"),
               ("Champagne wall", "a tower of champagne coupes catching four colours of light, "
                "shallow focus, bokeh behind")]),
 ("FINALE", [("Dust in the beam", "dust turning slowly in one hard overhead beam inside a bare "
              "concrete vault chamber, nothing on the floor"),
             ("Wake at night", "the churned wake of a boat at night, a neon city burning gold, "
              "pink, cyan and violet reflected and receding on the water")]),
])


def plate(body, cam):
    return (f"{body}, {cam}. {B['STYLE']}. {B['PERIOD']}")


elements = [O([("id", i), ("name", n), ("seconds", s),
               ("prompt", plate(p, "locked camera, element moves only")),
               ("negative", NEG_PLATE), ("use", use)])
            for i, n, s, p, use in ELEMENTS]

textures, n = [], 0
for tag, rows in TEXTURES.items():
    for j, (name, body) in enumerate(rows, 1):
        n += 1
        textures.append(O([
            ("id", f"TX-{tag.replace('SCENE ', 'S').replace('INTRO','IN').replace('FINALE','FIN')}-{j}"),
            ("beat", tag), ("name", name), ("seconds", 6),
            ("prompt", plate(body, "very slow drift, locked otherwise")),
            ("negative", NEG_PLATE),
        ]))

# Where two locked shots of the same person butt together — a jump cut waiting to happen.
by_beat = O()
for c in SHEET['clips']:
    by_beat.setdefault(c['beat'], []).append(c)
joins = []
for tag, cl in by_beat.items():
    for a, b in zip(cl, cl[1:]):
        if a['subject'] == '—' or a['subject'] != b['subject']:
            continue
        if 'locked' not in a['camera'].lower() or 'locked' not in b['camera'].lower():
            continue
        seam = a['role'] == 'APPROACH' and b['role'] == 'TURN'
        joins.append(O([
            ("beat", tag), ("from", a['id']), ("to", b['id']),
            ("roles", f"{a['role']} → {b['role']}"),
            ("subject", a['subject']),
            ("seamless", seam),
            ("fix", "LEAVE IT ALONE. Match the head angle across this cut so the rotation reads as "
                    "one continuous move. No flare, no cutaway, no dissolve." if seam else
                    "Punch in 12–18% on one of the two so the shot size changes, or drop a texture "
                    "or a flare pass between them."),
        ]))

doc = O([
 ("meta", O([
   ("name", "The Score — bridges, textures and transitions"),
   ("what", "The cheap material that makes the cuts work: editorial fixes that need no render, "
            "six reusable elements, and two people-free textures per beat."),
   ("elements", len(elements)), ("textures", len(textures)),
   ("joins", len(joins)),
   ("seamless", sum(1 for j in joins if j['seamless'])),
   ("needHelp", sum(1 for j in joins if not j['seamless'])),
   ("extraSeconds", sum(e['seconds'] for e in elements) + sum(t['seconds'] for t in textures)),
 ])),
 ("free", [O([("rule", r), ("why", w)]) for r, w in FREE]),
 ("order", [
   "Try the free fixes first. Most of these joins are a punch-in away from working and a render "
   "you don't make is a render you don't pay for.",
   "Then generate the six elements. They are people-free, so no character reference, no continuity "
   "risk and nothing for a content filter to object to — and one flare pass tinted four ways "
   "covers every crew in the film.",
   "Then textures, only for the beats you have actually cut. Two per beat is plenty; you will find "
   "you reuse three or four of them across the whole film.",
 ]),
 ("elementList", elements),
 ("textureList", textures),
 ("joinList", joins),
])
OUT.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + '\n')
m = doc['meta']
print(f"bridges: {m['elements']} elements + {m['textures']} textures = "
      f"{m['extraSeconds']}s more to generate")
print(f"joins where the same person sits on two locked shots in a row: {m['joins']} "
      f"({m['seamless']} are turn joins that must stay untouched, {m['needHelp']} want help)")
