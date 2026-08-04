#!/usr/bin/env python3
"""Bridges — the cheap material that makes the cuts work.

Three tiers, deliberately in this order:

  1. Editorial fixes that cost nothing. Most abrupt joins are fixed in Resolve
     with a punch-in or a different cut point, not with another render.
  2. A tiny element library. Six people-free clips, generated once, reused at
     every join in the film and tinted per crew on the colour page.
  3. Textures per beat, on a quota. Production finding from the first two beats:
     you need about as many people-free clips as you have clips with dialogue in
     them, and usually more. Every beat therefore gets (dialogue clips + 2) of
     b-roll, counting the plates already in the shot sheet, and the pool carries
     spares past that. No people in frame — so no character reference, no
     continuity risk, and nothing for a content filter to catch.

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


EXTRA = O([
 ("INTRO", [
   ("Neon sign", "a hand-painted neon sign buzzing and flickering above a wet street, sodium-vapour glow, rain crossing the beam"),
   ("Car passing", "a boxy 1970s black sedan sliding past camera on a wet street at night, taillights smearing, no people"),
   ("Weather over the city", "rain sheeting across a neon skyline seen from high above, cloud drifting through tower lights"),
   ("Smoke in the shaft", "an empty penthouse room at night, cigar smoke hanging in a shaft of neon light from the window"),
 ]),
 ("SCENE 1", [
   ("Swinging lamp", "a bare overhead lamp swinging in an empty interrogation room, its shadow sweeping a scratched steel table"),
   ("Toothpick", "macro of a chewed toothpick rolling to a stop on a scratched metal desk under one hard lamp"),
   ("The board", "a corkboard of pinned photographs and red string in a dark precinct office, one desk lamp burning"),
   ("Cold coffee", "steam rising from a chipped coffee cup on a windowsill, venetian blind shadows across it"),
 ]),
 ("SCENE 2", [
   ("Dashboard", "the dashboard of a 1970s lowrider at night, chrome dials glowing, cyan neon washing across the windscreen"),
   ("Road under speed", "wet asphalt rushing under a car at speed, streetlight streaks, very low angle"),
   ("Spotlight sweep", "a helicopter spotlight sweeping across rooftops and a chain-link fence at night"),
   ("Hydraulics", "a chrome wheel dropping onto wet asphalt as hydraulic suspension releases, spray lifting"),
 ]),
 ("SCENE 3", [
   ("Empty couch", "a white leather couch alone in an empty mirrored room, hot-pink neon crawling across it"),
   ("The medallion", "a gold falcon medallion resting on black marble, hard pink light raking across the metal"),
   ("Marina window", "rain on a floor-to-ceiling window over a night marina, black yachts out of focus below"),
   ("Pink haze", "haze drifting slowly through a hot-pink beam in an empty mirrored hall"),
 ]),
 ("SCENE 4", [
   ("The plate", "steam rising from a plate of pasta under a low warm lamp, velvet banquette out of focus behind"),
   ("The briefcase", "a black briefcase sitting closed on a red checkered tablecloth, gold lamp light, no people"),
   ("Ring and silk", "macro of a gold pinky ring beside a folded silk pocket square on dark polished wood"),
   ("Beaded curtain", "a beaded curtain swaying in the doorway of a warm gold-lit back room, kitchen glow beyond"),
 ]),
 ("SCENE 5", [
   ("Rain on the tower", "rain running down a glass tower window at night, violet server glow reflected, city far below"),
   ("The camera pans", "a security camera panning slowly on its bracket, red indicator LED, cold violet corridor"),
   ("Tape reels", "reels of magnetic tape turning on a rack of period computers, indicator lights blinking"),
   ("Channel flip", "a wall of CRT monitors flipping through channels of empty night streets, scan lines rolling"),
 ]),
 ("SCENE 6", [
   ("Worklight", "a hanging worklight swinging over stacked wooden crates, shadows sweeping the floor"),
   ("The seam", "dust turning in the seam where warm gold light meets hot pink light in an empty warehouse"),
   ("Chain hoist", "a chain hoist swinging gently in an empty warehouse, cold steel, deep shadow"),
   ("The bag", "a gold carry-bag sitting alone on a crate under one hanging worklight"),
 ]),
 ("SCENE 7", [
   ("Countdown", "a countdown readout ticking down on a steel bench, red emergency light pulsing across it"),
   ("Sparks", "sparks falling in slow motion from a cut wire onto a steel workbench"),
   ("Oscilloscope", "an oscilloscope trace jumping on a period CRT, green phosphor glow, dark room"),
   ("Red rotator", "an emergency red light rotating on a bare wall, haze, empty room"),
 ]),
 ("SCENE 8", [
   ("Projector fan", "a slide projector fan turning, dust swirling in the lens beam, dark room"),
   ("Icons drifting", "schematic icons drifting across frosted glass, blue-cyan glow, shallow focus"),
   ("Surveillance wall", "a pin board of surveillance photographs lit only by projector spill"),
   ("Tracing paper", "a hand-drawn floor plan on tracing paper under a desk lamp, pencil lines sharp"),
 ]),
 ("SCENE 9", [
   ("Hubcaps", "chrome hubcaps stacked against a garage wall under cyan neon"),
   ("Engine bay", "an open engine bay lit by a hanging drop light, chrome and rising steam, no people"),
   ("Headlights on the mural", "a painted wall mural lit by the headlights of a passing car, cyan night"),
   ("Pegboard keys", "rows of keys hanging on a garage pegboard, cyan glow, shallow focus"),
 ]),
 ("SCENE 10", [
   ("Black water", "rain hammering black water beside a pier at night, harbour lights smearing on the surface"),
   ("Rope and fog", "a mooring rope creaking on a bollard as fog rolls past pier lights"),
   ("Lights in the puddle", "five starting lights reflected in a puddle on wet boards, rain rings breaking them"),
   ("Foghorn", "fog rolling across an empty pier, a distant light pulsing through it"),
 ]),
 ("SCENE 11", [
   ("Grate steam", "steam pouring from a street grate in a dim alley, hard backlight through it"),
   ("Paint running", "fresh paint running down a brick wall under a single work light"),
   ("Fire escape", "a fire escape ladder above a wet alley, a searchlight beam crossing it"),
   ("Cans on the ledge", "spray cans lined up on a wall ledge in the dark, cyan rim light"),
 ]),
 ("SCENE 12", [
   ("Confetti", "confetti falling slowly through four colours of light in a grand ballroom"),
   ("Empty podium", "an empty podium under a huge banner, four-colour light crossing it, no people"),
   ("Chandelier", "a crystal chandelier refracting gold, hot pink, cyan and violet"),
   ("Buffet", "a long buffet table of period canapés lit in four colours, no people"),
 ]),
 ("FINALE", [
   ("The door opens", "a massive steel vault door swinging slowly open at the end of an empty concrete corridor"),
   ("Drag marks", "a bare concrete floor with a single set of drag marks through the dust, one hard overhead light"),
   ("Hull and water", "black water sliding past a yacht hull at night, neon glow breaking on the wake"),
   ("Empty deck", "an empty deck chair and a champagne bucket on a dark yacht deck, city glow receding"),
 ]),
])


def plate(body, cam):
    return (f"{body}, {cam}. {B['STYLE']}. {B['PERIOD']}")


elements = [O([("id", i), ("name", n), ("seconds", s),
               ("prompt", plate(p, "locked camera, element moves only")),
               ("negative", NEG_PLATE), ("use", use)])
            for i, n, s, p, use in ELEMENTS]

# Production finding from the first two beats: b-roll is not garnish. You need about
# as many people-free clips as clips with dialogue in them, and usually more — the
# cutaways are what let a cut breathe, hide a join and cover a take that half worked.
# So every beat gets a quota rather than a token two.
speak, plates = {}, {}
for c in SHEET['clips']:
    speak[c['beat']] = speak.get(c['beat'], 0) + (c['dialogue']['kind'] == 'speaks')
    plates[c['beat']] = plates.get(c['beat'], 0) + (c['subject'] == '—')

textures, n = [], 0
for tag, rows in TEXTURES.items():
    rows = list(rows) + list(EXTRA.get(tag, []))
    for j, (name, body) in enumerate(rows, 1):
        n += 1
        textures.append(O([
            ("id", f"TX-{tag.replace('SCENE ', 'S').replace('INTRO','IN').replace('FINALE','FIN')}-{j}"),
            ("beat", tag), ("name", name), ("seconds", 6),
            ("prompt", plate(body, "very slow drift, locked otherwise")),
            ("negative", NEG_PLATE),
            # required up to the beat's quota; anything past it is a spare to reach for
            ("required", j <= max(0, max(3, speak.get(tag, 0) + 2) - plates.get(tag, 0))),
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
   ("required", sum(1 for t in textures if t['required'])),
   ("spares", sum(1 for t in textures if not t['required'])),
   ("dialogueClips", sum(speak.values())),
   ("platesInSheet", sum(plates.values())),
   ("brollTotal", sum(plates.values()) + sum(1 for t in textures if t['required'])),
   ("brollRatio", round((sum(plates.values()) + sum(1 for t in textures if t['required']))
                        / max(1, sum(speak.values())), 2)),
   ("quota", O((tag, max(3, speak.get(tag, 0) + 2)) for tag in TEXTURES)),
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
   "Generate a beat's b-roll in the same session as its characters, not months later. You are "
   "already in that set with that look locked, and the first two beats proved the b-roll is not "
   "optional — it is roughly one clip for every clip with dialogue in it, and usually more.",
   "The quota per beat is its dialogue clips plus two, counting the plates already in the shot "
   "sheet. Anything past the quota is a spare — generate those only when the cut asks for them.",
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
