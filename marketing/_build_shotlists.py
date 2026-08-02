#!/usr/bin/env python3
"""Split the master sheet into per-character batches + a separate ensemble list.

Solo clips group by character so a whole part can be generated in one sitting.
Every clip with two or more established subjects in frame is pulled out and
re-prompted with explicit frame positions, per-subject lighting and a continuity
lock, because that is where identity drift and side-swapping happen.
"""
import json
from collections import OrderedDict as O, Counter

SRC = json.load(open('/home/user/showbuilderapp/marketing/shot-sheet.json'))
OUT = '/home/user/showbuilderapp/marketing/shot-list.json'
S = SRC['seeds']; L = SRC['locations']

NAMES = O([
 ("rico", "Rico “El Halcón” Delgado"), ("don", "Don Salvatore Corvetti"),
 ("marcus", "Marcus “Big Deal” Wells"), ("preston", "Preston Ashford Sterling III"),
 ("mcgraw", "Detective Dutch McGraw"), ("president", "President Diamante"),
 ("vinnie", "Vinnie the Veal"), ("problem", "Lil' Problem"), ("kayleigh", "Kayleigh"),
 ("sugar", "Sugar (the tiger)"), ("handler", "The Handler / TJ"),
 ("none", "World & inserts — no cast"),
])
COLOR = {"rico":"#ff2d9b","don":"#f5c542","marcus":"#00e5ff","preston":"#a06bff",
         "mcgraw":"#ff5a6e","president":"#ffd36b","vinnie":"#f5c542","problem":"#00e5ff",
         "kayleigh":"#a06bff","sugar":"#ff2d9b","handler":"#8f8fa6","none":"#5c5c72"}

# What each lead must never change between clips — the lock you check every render against.
LOCK = {
 "rico": "White linen suit, worn open to mid-chest — never buttoned. Large gold falcon medallion on a "
         "heavy chain, sitting outside the shirt. Thin scar over the RIGHT eyebrow, roughly 3cm, "
         "vertical. Slicked-back black hair, no parting. Cigar in the right hand or mouth. Gold rings "
         "on both hands.",
 "don": "Charcoal three-piece — waistcoat always visible. Gold silk pocket square, folded flat, not "
        "puffed. Red carnation in the left lapel. Gold pinky ring, LEFT hand. Thin silver hair combed "
        "straight back, no parting. Never raises his voice, never gestures above chest height.",
 "marcus": "Clean black bomber, zipped halfway. ONE gold chain, thin, short. Sharp fresh fade with a "
           "clean edge-up. Neat short beard, no moustache separation. Never holds anything.",
 "preston": "Black turtleneck under a charcoal suit jacket — no shirt, no tie, ever. Slicked hair, hard "
            "side parting. Pale, no colour in the face. Always holding something small: a device, a "
            "bottle of water, a remote.",
 "mcgraw": "Wrinkled trench coat over a cheap tie, knot always loose and off-centre. Grey stubble, "
           "three days. A toothpick in the mouth in every single shot. Never wears the coat closed.",
 "president": "Gold-accented navy suit, overlong red tie hanging below the belt. Absurd orange fake tan "
              "with a pale line at the jaw. Flag pins on the left lapel. Permanently mid-gesture.",
 "vinnie": "Open-collar white shirt, visibly sweated through at the collar and underarms. Thick gold "
           "chain outside the shirt. Slicked black hair, heavy stubble. Always slightly too close to "
           "whoever he's talking to.",
 "problem": "Cyan-and-black tracksuit, zipped to the chest. Gold rope chain, thick. Always holding food "
            "— the same food within a scene. Never still.",
 "kayleigh": "Sleek low bun, not a single loose strand. Minimalist dark blazer. Wired headset with the "
             "mic arm on the LEFT. Holding a clipboard. Never looks up unless she's speaking.",
 "sugar": "Full-grown Bengal tiger, thin gold collar. Always calm, always unbothered, never snarling, "
          "never mid-roar. She is furniture that happens to be alive.",
 "handler": "Black three-piece, black leather gloves, never removed. FACE IS NEVER VISIBLE — back to "
            "lens, three-quarter away, silhouette, or reflection only. If a face appears, rerender.",
}

# Clips with two or more established subjects in frame, re-prompted for continuity.
# id -> (cast, rewritten prompt body, continuity note)
ENS = {
 "S3-04": (["rico","sugar"],
   "FRAME RIGHT: {rico}, seated forward on a white leather couch, turning his head LEFT to speak to the "
   "animal beside him, cigar in his right hand, hot-pink neon on his face. FRAME LEFT: {sugar}, lying "
   "full-length on the same white couch, head up, completely unbothered, not reacting to him. {mansion}. "
   "Both subjects stay on these sides of frame for the whole shot",
   "Feed BOTH reference frames. The tiger must not react, turn, or open its mouth — she is indifferent, "
   "that's the joke. Rico's medallion stays outside the shirt."),

 "S6-02": (["don","rico"],
   "FRAME LEFT: {don}, lit warm gold from frame-left, seated. FRAME RIGHT: {rico}, lit hot pink from "
   "frame-right, seated opposite. The two men are gripping a handshake across a crate table and neither "
   "is letting go; both are smiling and neither smile reaches the eyes. {warehouse}. The older man is "
   "visibly forty years older and a head shorter. They hold these exact positions for the entire shot",
   "Feed BOTH reference frames. Gold light on the left man only, pink on the right man only — the colour "
   "separation is what stops the model blending them. Do not let them swap sides between takes."),

 "S6-04": (["sugar","don","rico"],
   "FOREGROUND: {sugar}, padding unhurried left-to-right across frame with a gold money-bag in her jaws, "
   "not looking at anyone. BACKGROUND, SOFT FOCUS: two seated men still gripping a handshake across a "
   "table — one elderly in a charcoal three-piece under warm gold light on the left, one in a white linen "
   "suit under hot pink light on the right, neither reacting to the animal. {warehouse}",
   "The two men are deliberately soft and small — this is the tiger's shot. Nobody in frame reacts to "
   "her. If either man looks at the tiger, rerender."),

 "S6-05": (["don","rico"],
   "FRAME LEFT: {don}, lit warm gold from frame-left. FRAME RIGHT: {rico}, lit hot pink from frame-right. "
   "Both men are slowly turning their heads away from each other and toward the lens at the same moment, "
   "still gripping the handshake between them. {warehouse}. STATIC LOCKED CAMERA. Neither man changes "
   "side of frame",
   "Feed BOTH reference frames. This is the APPROACH — they have not spoken yet. Turn the heads only; "
   "the bodies and the handshake do not move."),

 "S6-06": (["don","rico"],
   "FRAME LEFT: {don}, lit warm gold from frame-left, addressing the lens directly. FRAME RIGHT: {rico}, "
   "lit hot pink from frame-right, also addressing the lens directly. Both men are facing camera and "
   "speaking to the viewer, still holding the handshake between them. {warehouse}. STATIC LOCKED CAMERA — "
   "no push, no drift. Neither man changes side of frame",
   "The money shot of Scene 6. Both faces must be identifiable and must match their solo reference "
   "frames. Shoot this one more times than you think you need."),

 "S6-07": (["don","rico"],
   "FRAME LEFT: {don}, lit warm gold, silent, watching the lens. FRAME RIGHT: {rico}, lit hot pink, "
   "taking over the sentence, gesturing at the viewer with a cigar in his right hand. {warehouse}. STATIC "
   "LOCKED CAMERA. Neither man changes side of frame",
   "Only the right-hand man moves. Keeping the left man still is what makes the handover read."),

 "S6-08": (["don","rico"],
   "FRAME LEFT: {don}, lit warm gold. FRAME RIGHT: {rico}, lit hot pink. Both men speak the same words "
   "at the same moment into the lens, then turn their heads a few degrees toward each other with genuine "
   "irritation at having agreed. {warehouse}. STATIC LOCKED CAMERA",
   "Two beats in one clip, which is normally forbidden — allowed here only because the second beat is a "
   "head turn of a few degrees. If it rushes, split it into two clips."),

 "S10-02": (["don","rico"],
   "FRAME LEFT: {don}, lit warm gold from frame-left, coat dark with rain, entirely still. FRAME RIGHT: "
   "{rico}, lit hot pink from frame-right, white suit soaked through, agitated. The two men square off "
   "either side of a staging line on {pier} in heavy rain, crews behind each of them in silhouette. Five "
   "starting lights glow above. They hold these positions for the entire shot",
   "Feed BOTH reference frames. Rain and reflection will fight the colour separation — push the gold and "
   "pink keys harder than you would indoors."),

 "S10-05": (["don","rico"],
   "FRAME LEFT: {don}, lit warm gold, rain running off him. FRAME RIGHT: {rico}, lit hot pink, rain "
   "running off him. Both men turn their heads from each other toward the lens at the same moment as the "
   "five starting lights begin to come on above them. {pier}. STATIC LOCKED CAMERA. Neither man changes "
   "side of frame",
   "The APPROACH for the pier. Heads only — the standoff stance does not break."),

 "S10-08": (["don","rico"],
   "FRAME LEFT: {don}, lit warm gold. FRAME RIGHT: {rico}, lit hot pink. Both men hold a direct look into "
   "the lens in heavy rain as the last of five starting lights flares on above them. {pier}. STATIC "
   "LOCKED CAMERA",
   "The HOLD. Nobody speaks. Let the light do the work — the flare is the cut point."),

 "FIN-09": (["president","mcgraw"],
   "FRAME RIGHT: {president}, wrists together in handcuffs, immediately turning to address a television "
   "camera off frame-right, delighted rather than alarmed. FRAME LEFT, PARTIALLY OUT OF FRAME: {mcgraw}, "
   "gripping the cuffed man's arm, only his shoulder, coat sleeve and jaw in shot. A concrete vault "
   "doorway, hard TV camera light flaring from frame-right",
   "The detective is deliberately three-quarters out of frame — one subject to hold, not two. Keep the "
   "toothpick visible in his jaw for continuity with his solo clips."),

 "FIN-11": (["handler","sugar"],
   "CENTRE FRAME, BACK TO LENS: {handler}, raising a champagne glass toward the camera in a toast, face "
   "never visible. FRAME RIGHT, SEATED: {sugar}, calm and unbothered, looking out at the water not at "
   "him. The deck of a black yacht at night, a neon city burning gold, pink, cyan and violet in the wake "
   "behind. STATIC LOCKED CAMERA",
   "FACE NEVER VISIBLE — keep §NEG-HANDLER on. The tiger anchors the frame; if she moves the eye goes to "
   "her and the toast is lost."),

 "FIN-12": (["handler","sugar"],
   "CENTRE FRAME, BACK TO LENS: {handler}, holding the raised toast completely still, face never visible. "
   "FRAME RIGHT: {sugar}, seated, motionless. The deck of a black yacht at night, the neon city receding "
   "to a glow on the horizon behind them. STATIC LOCKED CAMERA",
   "Absolute stillness in both subjects. This is the last frame of the film — hold it long."),
}

# Solo clips whose subject isn't captured by a seed token (literal phrasing in the master sheet).
SOLO_FIX = {"S10-06": "don", "S1-02": "none", "S12-04": "none"}

def fill(t):
    for table in (L, S):
        for k, v in table.items():
            tok = '{' + k + '}'
            t = t.replace(tok + ',', v + ',').replace(tok + '.', v + '.').replace(tok, v + ',')
    return t

clips = []
for c in SRC['clips']:
    c = dict(c)
    if c['id'] in ENS:
        cast, body, note = ENS[c['id']]
        c['cast'] = cast
        c['ensemble'] = True
        c['continuity'] = note
        c['prompt'] = f"{fill(body)}, {c['camera']}"
        c['full'] = f"{fill(body)}, {c['camera']}. {SRC['blocks']['STYLE']}. {SRC['blocks']['PERIOD']}"
        negs = [SRC['blocks']['NEG'], SRC['blocks']['NEG_PERIOD'], SRC['blocks']['NEG_MOTION'],
                "the two subjects swapping sides, subjects merging, identical faces, twins, "
                "one subject's clothing appearing on the other"]
        if 'handler' in cast:
            negs.append(SRC['blocks']['NEG_HANDLER'])
        c['negative'] = ", ".join(negs)
    else:
        subj = SOLO_FIX.get(c['id'], c['subject'] if c['subject'] != '—' else 'none')
        c['cast'] = [subj]
        c['ensemble'] = False
        c['continuity'] = None
    clips.append(c)

solo = [c for c in clips if not c['ensemble']]
ens = [c for c in clips if c['ensemble']]

# per-character batches, ordered by location so a locked set gets reused
chars = []
for key, name in NAMES.items():
    mine = [c for c in solo if c['cast'][0] == key]
    if not mine:
        continue
    mine.sort(key=lambda c: (c['beat'], c['n']))
    chars.append(O([
        ("key", key), ("name", name), ("colour", COLOR[key]),
        ("seed", S.get(key)), ("lock", LOCK.get(key)),
        ("clipCount", len(mine)), ("seconds", sum(c['seconds'] for c in mine)),
        ("beats", sorted({c['beat'] for c in mine}, key=lambda b: [x['beat'] for x in SRC['clips']].index(b))),
        ("clips", mine),
    ]))

doc = O([
 ("meta", O([
   ("name", "The Score — shot list by subject"),
   ("what", "The master sheet regrouped for generation. Every clip with a single subject sits in that "
            "character's batch so a whole part can be generated in one sitting; every clip with two or "
            "more established subjects in frame is pulled into its own list and re-prompted."),
   ("soloClips", len(solo)), ("ensembleClips", len(ens)),
   ("totalSeconds", sum(c['seconds'] for c in clips)),
 ])),
 ("howToBatch", [
   "Generate the character's SEED first. Pick the best frame. That frame is the image reference for "
   "every other clip in their batch — do not re-seed mid-batch.",
   "Work down the batch in order. It's grouped by beat, so the set stays locked as long as possible.",
   "Check every render against the LOCK list before you accept it. Wardrobe drift is the thing you "
   "won't notice until the edit.",
   "Do the ensemble list LAST, once every solo reference frame exists — you need both locked faces "
   "before you can put two people in one frame.",
 ]),
 ("ensembleRules", [
   "Feed BOTH reference frames. One is not enough; the model will average the two faces.",
   "State the frame position explicitly — FRAME LEFT and FRAME RIGHT — in every prompt, and never let "
   "them swap between takes. A swapped pair is unusable in the edit.",
   "Light each subject in their own crew colour: gold on the Corvettis, pink on the Halcóns. The colour "
   "separation is doing as much continuity work as the reference frames are.",
   "Say the contrast out loud — 'forty years older and a head shorter' — so the model has a reason to "
   "keep them distinct.",
   "The negative block for these clips adds subjects swapping sides, subjects merging, identical faces "
   "and one subject's clothing appearing on the other.",
   "Shoot ensemble clips more times than solo ones. They fail more often and they fail in ways you only "
   "see at full size.",
 ]),
 ("blocks", SRC['blocks']),
 ("characters", chars),
 ("ensemble", ens),
])

open(OUT, 'w').write(json.dumps(doc, indent=2, ensure_ascii=False) + '\n')
print(f"solo {len(solo)} + ensemble {len(ens)} = {len(clips)} (master has {len(SRC['clips'])})")
print('characters:', {c['key']: c['clipCount'] for c in chars})
print('every ensemble has continuity note:', all(c['continuity'] for c in ens))
print('every ensemble has 2+ cast:', all(len(c['cast']) >= 2 for c in ens))
print('unassigned solo:', [c['id'] for c in solo if c['cast'][0] not in NAMES] or 'none')
