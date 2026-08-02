#!/usr/bin/env python3
"""Master prompt sheet — the whole film decomposed into <=15s generatable clips."""
import json
from collections import OrderedDict as O

OUT = '/home/user/showbuilderapp/marketing/shot-sheet.json'
SHOW = json.load(open('/home/user/showbuilderapp/brands/gtad.show.json'))
GAMES = {g['n']: g for g in SHOW['games']}

STYLE = ("cinematic film still, anamorphic 40mm lens, matte black and charcoal palette with saturated "
         "neon accents, deep low-key shadows, volumetric haze, rain-slick reflections, luxury "
         "crime-drama noir, shallow depth of field, hyper-detailed, photographic, no text")
PERIOD = ("late-1970s to early-1980s (1977–1983), shot on 35mm film, warm Kodak color science, heavy "
          "organic film grain, subtle gate weave, halation bloom on highlights, gentle anamorphic "
          "flares, period-correct wardrobe and hairstyles, boxy 1970s–80s automobiles, analog "
          "technology only — rotary and pay phones, CRT televisions, chrome and brushed steel, early "
          "neon and sodium-vapor streetlight; NOT clean modern digital")
NEG = ("text, watermark, logo, caption, subtitles, cartoon, illustration, 3d render, cgi, video-game "
       "UI, HUD, low quality, oversaturated, deformed hands, extra fingers, plastic skin")
NEG_PERIOD = ("smartphone, cell phone, flat-screen TV, LED screen, laptop, modern car, modern "
              "skyscraper glass, contemporary streetwear, modern signage, clean digital look")
NEG_HANDLER = "clear identifiable face, visible face, portrait of the man"
NEG_MOTION = ("cut to another shot, scene change, location change, background change, teleporting "
              "subject, multiple camera angles, jump cut, morphing face")

SEEDS = O([
 ("rico", "a Latin cartel kingpin in his late 30s, intense dark eyes, slicked-back black hair, a thin "
          "scar over his right eyebrow, open-chested white linen suit, large gold falcon medallion, gold rings"),
 ("don", "an elderly Italian-American crime patriarch in his late 70s, heavy jowls, hooded eyes, thin "
         "silver hair combed straight back, charcoal three-piece suit, gold silk pocket square, gold "
         "pinky ring, red carnation in the lapel"),
 ("vinnie", "a hot-tempered Italian-American man in his mid-30s, slicked black hair, heavy stubble, "
            "open-collar white shirt, thick gold chain, visibly sweating"),
 ("marcus", "a calm commanding Black man in his early 30s, sharp fresh fade, neat short beard, a single "
            "gold chain, clean black bomber jacket"),
 ("problem", "a heavyset likeable Black man in his late 20s, cyan-and-black tracksuit, gold rope chain, "
             "mid-sentence, holding food"),
 ("preston", "a cold corporate executive in his late 30s, pale, slicked hair, sharp jaw, black turtleneck "
             "under a charcoal suit"),
 ("kayleigh", "a sharp unbothered woman in her early 30s, sleek low bun, headset, holding a clipboard, "
              "minimalist dark blazer"),
 ("mcgraw", "a rumpled world-weary detective in his 50s, grey stubble, tired eyes, a toothpick in his "
            "mouth, wrinkled trench coat over a cheap tie"),
 ("president", "a bombastic head of state in his 60s, absurd fake tan, jowly, exaggerated grin, "
               "gold-accented navy suit with an overlong red tie and flag pins"),
 ("sugar", "a calm full-grown Bengal tiger with a thin gold collar, regal and unbothered"),
 ("handler", "a figure in a flawless tailored black three-piece suit and black leather gloves, always "
             "turned away from camera, face never visible"),
])

# How each part sounds. The line alone gets you a mouth moving; the delivery is what
# makes it that character saying it.
VOICES = O([
 ("rico", "a hoarse rising Cuban accent, quiet and coiled before it detonates"),
 ("don", "an old whispered New York-Italian rasp, slow, never raised"),
 ("vinnie", "a loud sweaty New York-Italian bark, always a half-step too eager"),
 ("marcus", "a low unhurried West Coast calm, never raised, entirely certain"),
 ("problem", "an eager overlapping delivery, mouth half full, no pauses"),
 ("preston", "a flat clipped tech-founder cadence with a rehearsed upward lilt"),
 ("kayleigh", "a dry bored perfectly level delivery, no emphasis anywhere"),
 ("mcgraw", "a gravelled tired American drawl, talking around a toothpick"),
 ("president", "a booming self-satisfied stump-speech delivery, stressing the wrong words"),
 ("handler", "a calm close unhurried baritone, speaking directly to one person"),
])
SPEAKERS = O([("HANDLER","handler"), ("VO","handler"), ("RICO","rico"), ("DON","don"),
              ("VINNIE","vinnie"), ("MARCUS","marcus"), ("PROBLEM","problem"),
              ("PRESTON","preston"), ("KAYLEIGH","kayleigh"), ("MCGRAW","mcgraw"),
              ("PRESIDENT","president"), ("BOTH","both")])

# Words per second of delivered dialogue. These parts are all slow — menace, whisper,
# stump speech — so this is deliberately under the ~2.8 of ordinary conversation.
WPS = 2.3
AIR = 2.0  # seconds of silence a clip needs around the line to be cuttable

NEG_SILENT = "talking, mouth moving, lip flap, speaking, shouting"
NEG_SPEAKING = "closed mouth, mismatched lip sync, muted, silent performance"

LOCS = O([
 ("mansion", "a mirrored hot-pink neon mansion interior, mirrored walls, white leather couches, floor-to-ceiling windows over a night marina"),
 ("backroom", "a warm gold-lit restaurant back room, checkered tablecloth, velvet banquettes, low hanging lamp"),
 ("block", "a cyan-lit inner-city street corner at night, murals, corner-store glow, wet asphalt, steam from a grate"),
 ("tower", "a cold violet-lit glass office tower interior at night, a wall of CRT surveillance monitors"),
 ("precinct", "a gritty precinct lineup room at night, height-marker wall, venetian blinds throwing red and blue siren light"),
 ("warehouse", "a neutral warehouse interior at night, half lit warm gold and half lit hot pink, crates and hanging worklights"),
 ("pier", "a rain-soaked wooden pier at night, harbour fog, five drag-strip starting lights glowing above, wet reflective boards"),
 ("alley", "a dim neon alley at four in the morning, brick wall, a single searchlight sweeping"),
 ("ballroom", "a grand ballroom lit in four colours — gold, hot pink, cyan and violet — a podium under a huge banner, a giant four-colour vault lock glowing at the centre"),
 ("vault", "a bare concrete vault chamber, a massive steel door standing open, one hard overhead light, dust in the beam"),
 ("city", "a rain-slicked noir megacity at night seen from the air, four districts glowing gold, hot pink, cyan and violet"),
])

# beat -> clips. role, seconds, camera (ONE move), subject key or '', prompt, audio
BEATS = [

("INTRO", "The Transmission", "handler", "city", [
 ("ESTABLISH", 15, "slow aerial descent, no other movement", "", "{city}, headlights and neon threading the wet streets, a single black luxury car crossing the lower third", "Handler VO — 'Every city tells a story about itself.'"),
 ("ESTABLISH", 12, "slow push in, locked otherwise", "", "a gold-lit old-world waterfront district at night, wet cobbles, hanging bistro lights, fog off the harbour, no people", "VO — 'The old family thinks it's about respect.'"),
 ("ESTABLISH", 12, "slow drift right", "", "a hot-pink neon marina at night, black yachts, palms, a mirrored mansion glowing on the rise beyond, rain-slick", "VO — 'The cartel thinks it's about power.'"),
 ("ESTABLISH", 12, "slow dolly left", "", "a cyan-lit inner-city block at night, murals, a chrome lowrider parked at the kerb, steam from a grate", "VO — 'The kings on the block think it's about loyalty.'"),
 ("ESTABLISH", 12, "slow tilt up", "", "a cluster of cold violet glass towers at night, one lit floor high up, rain, drifting cloud", "VO — 'And the suits downtown think it's a spreadsheet.'"),
 ("BUILD", 12, "locked camera, subject moves only", "president", "{president} grinning and waving behind a podium under a huge WAR ON CRIME banner, seen playing on a grid of glowing CRT storefront televisions on a wet neon street", "President — 'this city is SAFER than it has ever been.'"),
 ("INSERT", 10, "extreme close-up, locked", "handler", "extreme close-up of a black-gloved hand lowering a car window one inch at night, neon reflecting on wet glass, the suggestion of a suited figure inside, no face", "VO — 'It was never about them.'"),
 ("APPROACH", 10, "slow push in, locked otherwise", "handler", "{handler} standing at floor-to-ceiling penthouse windows over a rain-soaked neon skyline, back to camera, cigar smoke curling, absolutely still", "VO — 'Name's TJ. I run this room.'"),
 ("TURN", 15, "STATIC LOCKED CAMERA — no push, no drift", "handler", "{handler} slowly turning his head a quarter toward the lens and stopping — the face stays out of the light, only the jaw and the gloved hand catching magenta rim light, addressing the viewer directly", "◆ THE TURN — 'And you. Everybody in this room tonight.'"),
 ("HOLD", 10, "STATIC LOCKED CAMERA", "handler", "{handler} holding completely still, half-turned toward the lens, face still unlit, neon breathing behind him", "◆ '…the only voice in this room you can trust is coming out of that booth.'"),
 ("OUT", 12, "slow push, locked otherwise", "", "a black car pulling into a private marina at night, a boat idling in the dark, no people", "Title slam → the opener drops."),
]),

("SCENE 1", "The Interrogation", "mcgraw", "precinct", [
 ("ESTABLISH", 12, "slow push in, no other movement", "", "{precinct}, empty, dust turning in one hard overhead lamp beam, no people", "Handler VO — 'Twenty years, McGraw's been lining up the wrong men.'"),
 ("BUILD", 15, "slow handheld drift along the line", "", "five mismatched suspects in silhouette against a height-marker wall — one in a gold tie, one in a pink suit, one in cyan streetwear, one in a violet corporate suit, one confused civilian in club clothes, each holding a booking number upside down", "Room tone, a chair scraping."),
 ("BUILD", 15, "locked camera, subject paces through frame", "mcgraw", "{mcgraw} pacing slowly through the foreground of {precinct}, chewing a toothpick, not looking at the men behind him", "McGRAW — 'Somewhere in this city there's a man with no face…'"),
 ("BUILD", 12, "locked camera", "mcgraw", "{mcgraw} stopping and pointing flatly at someone off-frame, deadpan, red and blue light crossing his face", "McGRAW — 'And ONE of you knows him.' (points at a busboy)"),
 ("APPROACH", 10, "STATIC LOCKED CAMERA", "mcgraw", "{mcgraw} standing still in {precinct}, slowly taking the toothpick out of his mouth, eyes drifting off the suspects and settling toward the lens, not yet speaking", "beat of silence — the room notices him notice you"),
 ("TURN", 15, "STATIC LOCKED CAMERA — no push, no drift", "mcgraw", "{mcgraw} turning his whole body to face the lens and holding, jabbing the toothpick toward the viewer, red-blue siren light across his tired face, addressing the room directly", "◆ 'Twenty years I been askin' the wrong questions to the wrong guys. Not tonight.'"),
 ("TURN", 12, "STATIC LOCKED CAMERA", "mcgraw", "{mcgraw} continuing to speak directly into the lens, leaning in slightly, unblinking", "◆ 'Eight questions, comin' fast. Answer straight, answer quick, and do NOT crack.'"),
 ("HOLD", 8, "STATIC LOCKED CAMERA", "mcgraw", "{mcgraw} finishing, holding the stare into the lens, absolutely still, one eyebrow slightly raised", "◆ 'Let's see who talks.' → ▮ THE INTERROGATION"),
 ("OUT", 10, "locked, light change only", "", "venetian blinds throwing red and blue siren light across an empty precinct wall, dust in the beam, no people", "stinger → the game opens."),
]),

("SCENE 2", "The Joyride", "marcus", "block", [
 ("ESTABLISH", 12, "low slow tracking shot", "", "a chrome-and-cyan lowrider bouncing on hydraulics on {block}, no people visible, motion blur", "Handler VO — 'The kings only ever wanted three things.'"),
 ("BUILD", 15, "locked interior camera", "problem", "{problem} in the passenger seat of a lowrider at night, mid-sentence, gesturing with food in one hand, cyan neon washing through the windscreen", "PROBLEM — 'A taco empire. Big Deal, you listenin' to the vision?'"),
 ("BUILD", 12, "locked on the mirror", "", "a rear-view mirror at night filling with police lights — first one car, then four, then a helicopter spotlight sweeping down, no faces", "sirens climbing under the dialogue"),
 ("BUILD", 12, "locked interior camera", "marcus", "{marcus} at the wheel of a lowrider at night, glancing once at the mirror, completely unbothered, cyan light across his face", "MARCUS — '…Ah, sh— here we go again.'"),
 ("APPROACH", 10, "STATIC LOCKED CAMERA", "marcus", "{marcus} at the wheel, slowly turning his head from the road toward the lens and holding, calm, no expression change yet", "beat — he clocks you"),
 ("TURN", 15, "STATIC LOCKED CAMERA — no push, no drift", "marcus", "{marcus} looking directly into the lens through the windscreen, deadly calm, talking to the viewer, cyan neon and police lights strobing behind him", "◆ 'Every one of you is behind the wheel now. Phone up — that's your getaway car.'"),
 ("TURN", 12, "STATIC LOCKED CAMERA", "marcus", "{marcus} still looking into the lens, one hand loose on the wheel, the chase visible but out of focus behind him", "◆ 'Every hit's a wanted star. Rack up too many and you're done.'"),
 ("HOLD", 8, "STATIC LOCKED CAMERA", "marcus", "{marcus} holding the look into the lens, then the smallest flick of the eyes to his passenger", "◆ '…Problem, put the taco down and drive.' → ▮ THE JOYRIDE"),
 ("OUT", 12, "low tracking, accelerating", "", "a cyan lowrider peeling out on a wet neon street as police lights swallow the frame, helicopter spotlight sweeping, no faces", "slam — the chase cut drops."),
]),

("SCENE 3", "Crossfire", "rico", "mansion", [
 ("ESTABLISH", 12, "slow drift, locked otherwise", "", "{mansion}, empty, mirrored walls doubling the pink neon, a white leather couch, no people", "Handler VO — 'The cartel thinks power is how loud you can be.'"),
 ("BUILD", 12, "locked camera", "sugar", "{sugar} lying on a white leather couch in {mansion}, completely unbothered, tail moving slowly", "room tone, distant music"),
 ("BUILD", 15, "slow push in, locked otherwise", "rico", "{rico} standing calm and still inside {mansion} as neon tracer rounds streak past behind him and muzzle flashes reflect in the mirrors, he does not flinch", "RICO — 'They send targets. To my house. To Rico Delgado's house.'"),
 ("BUILD", 12, "locked camera", "rico", "{rico} turning his head to speak to the tiger on the couch, cigar in hand, genuinely wounded rather than afraid", "RICO — 'You believe this, Sugar? After everything I do for this city?'"),
 ("INSERT", 8, "extreme close-up, locked", "", "extreme close-up of neon tracer streaks slicing through hot-pink haze past mirrored walls, muzzle-flash flicker, no people", "a round goes past his cheek"),
 ("APPROACH", 12, "STATIC LOCKED CAMERA", "rico", "{rico} in profile in {mansion}, a tracer round passing his cheek — he does not blink, does not duck, slowly lowers the cigar from his mouth and begins to rotate his head toward the lens, still quiet", "no line — he is insulted, not frightened. HOLD THE SILENCE."),
 ("TURN", 15, "STATIC LOCKED CAMERA — no push, no drift, no cut", "rico", "{rico} completing a slow deliberate turn from profile to face the lens directly, eyes locking on the viewer, quiet at first then building, hot-pink neon on his sweating face", "◆ 'You think you can survive in MY world? EH?'"),
 ("TURN", 12, "STATIC LOCKED CAMERA", "rico", "{rico} leaning into the lens, manic joy taking over, tracer fire still streaking past him unremarked", "◆ 'Three lives, that's all. Drag, weave, don't get hit.'"),
 ("HOLD", 8, "STATIC LOCKED CAMERA", "rico", "{rico} arms wide, holding the stare into the lens, grinning, mirrors doubling him infinitely behind", "◆ 'Say goodnight to the bad guy!' → ▮ CROSSFIRE"),
 ("OUT", 10, "locked, glass shattering", "", "mirrored walls shattering into hot-pink haze in slow motion, neon fragments, no people", "slam — the hottest cut of the night."),
]),

("SCENE 4", "The Drop-Off", "don", "backroom", [
 ("ESTABLISH", 12, "slow push in", "", "{backroom}, empty, one lamp low over a checkered tablecloth, cannoli on a plate, no people", "Handler VO — 'The old man thinks he's moving a fortune across town.'"),
 ("BUILD", 15, "locked camera", "don", "{don} sitting at the table in {backroom}, whispering across the checkered cloth, a black briefcase sitting as dressing beside him", "DON — 'You don't look at the product. You don't talk about the product.'"),
 ("BUILD", 12, "locked camera", "vinnie", "{vinnie} sitting opposite in {backroom}, sweating through his shirt, leaning in, genuinely confused", "VINNIE — 'Pop… what's the drop?'"),
 ("BUILD", 15, "locked camera, no movement at all", "don", "{don} slowly eating a cannoli in {backroom}, taking his time, saying nothing, hooded eyes fixed on his son", "SILENCE. Let this run uncomfortably long."),
 ("APPROACH", 10, "STATIC LOCKED CAMERA", "don", "{don} setting the cannoli down, dabbing his mouth once, and slowly beginning to turn his head toward the lens, unhurried", "DON — '…Respect. And also the drop.'"),
 ("TURN", 15, "STATIC LOCKED CAMERA — no push, no drift", "don", "{don} turning fully to face the lens and holding, a knowing half-smile, kissing his fingertips toward the viewer, warm gold velvet room behind him", "◆ 'Somebody's gotta move the product tonight — and tonight that's all of you.'"),
 ("TURN", 12, "STATIC LOCKED CAMERA", "don", "{don} speaking quietly and directly into the lens, one hand turning over on the tablecloth", "◆ 'Hop the traffic, make the drop, get back, go again.'"),
 ("HOLD", 8, "STATIC LOCKED CAMERA", "don", "{don} finishing, holding the look into the lens, then the smallest shrug", "◆ '…Move it like it was never born.' → ▮ THE DROP-OFF"),
 ("OUT", 8, "macro, locked", "", "macro of a rotary telephone and a lit dial lamp on a dim restaurant table, gold light, no faces", "drop-ping SFX → swing slams in."),
]),

("SCENE 5", "The Stakeout", "preston", "tower", [
 ("ESTABLISH", 12, "slow lateral drift", "", "{tower}, a wall of glowing CRT surveillance monitors showing four different districts, no people", "Handler VO — 'Everybody's huntin' the rat.'"),
 ("BUILD", 15, "locked camera", "preston", "{preston} standing before the monitor wall in {tower}, sipping bottled water, watching four gangs at once, smug", "PRESTON — 'Someone in this city is leaking. I want a full loyalty audit.'"),
 ("BUILD", 12, "locked camera", "kayleigh", "{kayleigh} seated beside him in {tower}, not looking up from her clipboard, entirely unbothered", "KAYLEIGH — 'The rat is you, Preston. You post everything.'"),
 ("BUILD", 10, "locked camera", "preston", "{preston} absorbing that, wounded for exactly one beat, then recovering completely", "PRESTON — '…That's engagement.'"),
 ("APPROACH", 10, "STATIC LOCKED CAMERA", "preston", "{preston} turning slowly from the monitor wall and stepping toward the camera until he is too close, violet server glow over-lighting his face from below", "he leans into the lens like it's a webcam"),
 ("TURN", 15, "STATIC LOCKED CAMERA — no push, no drift", "preston", "{preston} facing the lens directly, far too close, over-lit and unblinking, addressing the viewer with corporate menace", "◆ 'Statistically, someone in your feed is a wire right now.'"),
 ("TURN", 12, "STATIC LOCKED CAMERA", "preston", "{preston} still too close to the lens, gesturing precisely, violet glow flickering across his turtleneck", "◆ 'Red faces are perps: tap 'em, fast. Touch a guest and YOU'RE the leak.'"),
 ("HOLD", 8, "STATIC LOCKED CAMERA", "preston", "{preston} holding the stare into the lens, a small satisfied smile, monitors flickering behind him", "◆ 'Especially the person you came with.' → ▮ THE STAKEOUT"),
 ("OUT", 8, "locked, graphic element", "", "a red target box snapping onto a blurred face on a CRT surveillance monitor, scan lines, violet glow", "synthetic ding → the tap game opens."),
]),

("SCENE 6", "Smash & Grab", "don", "warehouse", [
 ("ESTABLISH", 12, "slow push in", "", "{warehouse}, empty, half lit warm gold and half lit hot pink, dust turning in worklight beams, no people", "Handler VO — 'Two crews, one vault, and not one ounce of trust.'"),
 ("BUILD", 15, "slow push in on the handshake", "", "an elderly gold-suited don and a white-suited cartel kingpin shaking hands across a crate table in {warehouse}, neither letting go, gold light on one and pink on the other", "RICO — 'Fifty-fifty. Like brothers.'"),
 ("BUILD", 12, "locked camera", "don", "{don} leaning aside to speak quietly to someone off-frame while still gripping the handshake, eyes never leaving the other man", "DON (aside) — 'Cain and Abel were brothers. You remember how that ended.'"),
 ("INSERT", 10, "locked wide, background action", "sugar", "{sugar} padding unhurried out of frame in {warehouse} with a gold money-bag in her jaws, completely unnoticed, two men in the background still shaking hands", "nobody reacts. That's the joke."),
 ("APPROACH", 10, "STATIC LOCKED CAMERA", "", "an elderly gold-suited don and a white-suited cartel kingpin both slowly turning their heads from each other toward the lens at the same time, still gripping hands", "the two of them realise you're there"),
 ("TURN", 15, "STATIC LOCKED CAMERA — no push, no drift", "", "an elderly gold-suited don and a white-suited cartel kingpin facing the lens together in {warehouse}, gold-lit and pink-lit, addressing the viewer, still not letting go of the handshake", "◆ DON 'The vault's open. My crew and his crew—' RICO '—and every one of YOU—'"),
 ("TURN", 12, "STATIC LOCKED CAMERA", "", "the same two bosses to lens, the cartel kingpin taking over the sentence, gesturing at the viewer with his cigar", "◆ RICO 'Bounce the ball, break the glass, don't leave a dollar, mang.'"),
 ("HOLD", 8, "STATIC LOCKED CAMERA", "", "both men holding the look into the lens, saying the same words at the same time, then glaring at each other for having agreed", "◆ BOTH '…Don't leave a dollar.' → ▮ SMASH & GRAB"),
 ("OUT", 10, "locked, slow motion", "", "a wrecking ball smashing through a neon storefront window in slow motion, glass and loot flying, no people", "slam — gold × pink mashup."),
]),

("SCENE 7", "The Device", "preston", "tower", [
 ("ESTABLISH", 12, "slow push in", "", "a violet-lit vault workroom at night, a steel bench, a glowing tangle of coloured wires and a countdown readout, no people", "Handler VO — 'The suit spent a fortune on a vault a nine-year-old could crawl under.'"),
 ("BUILD", 15, "locked camera", "preston", "{preston} presenting a glowing wired device on the bench like a keynote demo, arms wide, entirely confident", "PRESTON — 'I've reinvented theft. We call it Breach. Private beta.'"),
 ("BUILD", 12, "handheld, slight shake", "preston", "{preston} fumbling the shrieking device as the whole room flips to emergency red, dignified panic, still trying to present", "alarm shriek — the room goes red"),
 ("BUILD", 10, "locked camera", "kayleigh", "{kayleigh} on the far side of the bench holding an already-defused identical device, bored, waiting", "KAYLEIGH says nothing. That's the joke."),
 ("APPROACH", 10, "STATIC LOCKED CAMERA", "preston", "{preston} straightening his turtleneck, composing himself, and craning slowly toward the lens still holding the device", "PRESTON — '…That was a soft launch.'"),
 ("TURN", 15, "STATIC LOCKED CAMERA — no push, no drift", "preston", "{preston} facing the lens holding the wired countdown device up beside his face, violet and emergency-red light alternating, deadpan, addressing the viewer", "◆ 'You. You think you can crack it?'"),
 ("TURN", 12, "STATIC LOCKED CAMERA", "preston", "{preston} still to lens, holding the device dead steady, hand visibly tense", "◆ 'Cut the wires in the right order, dial the code, then hold your hand DEAD steady.'"),
 ("HOLD", 8, "STATIC LOCKED CAMERA", "preston", "{preston} holding the look and the device, absolutely motionless, red light pulsing", "◆ 'Take your time. Don't. Drop it.' → ▮ THE DEVICE"),
 ("OUT", 8, "macro, locked", "", "macro of a glowing tangle of coloured wires and a ticking countdown readout on pure black, slight flicker", "silence, then the alarm cuts dead."),
]),

("SCENE 8", "The Blueprint", "rico", "tower", [
 ("ESTABLISH", 12, "slow drift", "", "a dark planning room at night, two glowing blue-cyan heist blueprints of icons projected on frosted glass, thin schematic lines, no people", "Handler VO — 'They think if they memorize the vault, they own it.'"),
 ("BUILD", 15, "locked camera", "preston", "{preston} standing beside the projected blueprints in the dark planning room, tapping the glass, insufferably pleased with himself", "PRESTON — 'Photographic memory is a skill, Rico. I did a course. Two courses.'"),
 ("BUILD", 12, "locked camera", "rico", "{rico} in the same dark planning room, arms folded, refusing to look at the paper, pink rim light on his white suit", "RICO — 'I don't need the paper, mang.'"),
 ("BUILD", 10, "locked camera", "rico", "{rico} in the dark planning room after the projection has blinked out, faltering for the first time, genuinely searching", "RICO — '…What was the first icon?'"),
 ("APPROACH", 10, "STATIC LOCKED CAMERA", "rico", "{rico} recovering instantly, stepping toward the lens and reaching back to tap a glowing falcon icon on the frosted glass without looking at it", "PRESTON (off) — 'The falcon.' RICO — '…It's always the falcon.'"),
 ("TURN", 15, "STATIC LOCKED CAMERA — no push, no drift", "rico", "{rico} facing the lens directly with two glowing blueprints projected on frosted glass behind him, one finger raised, addressing the viewer", "◆ 'Ten seconds. Phone up. Two blueprints comin'.'"),
 ("TURN", 12, "STATIC LOCKED CAMERA", "rico", "{rico} still to lens, counting down on his fingers, the projection behind him beginning to fade", "◆ 'Burn every icon into your head, then they're gone.'"),
 ("HOLD", 8, "STATIC LOCKED CAMERA", "rico", "{rico} holding the look, tapping his temple once, the blueprint gone entirely behind him", "◆ 'Eyes up. Ten… nine…' → ▮ THE BLUEPRINT"),
 ("OUT", 8, "locked, element only", "", "a glowing blue-cyan blueprint of icons on frosted glass blinking out to black, thin schematic lines, no people", "the loop tightens."),
]),

("SCENE 9", "Chop Shop", "marcus", "block", [
 ("ESTABLISH", 12, "slow dolly along the line", "", "a line of chrome rides parked on {block}, hydraulics settling, no people", "Handler VO — 'Half the cars in this city have been stolen twice.'"),
 ("BUILD", 15, "locked camera", "problem", "{problem} leaning on a chrome lowrider on {block}, mid-pitch, gesturing enormously, entirely serious", "PROBLEM — 'What if this is my origin story, Big Deal?'"),
 ("BUILD", 10, "locked camera", "marcus", "{marcus} beside the lowrider on {block}, unimpressed, not even turning his head", "MARCUS — 'It's a Honda, Problem.'"),
 ("INSERT", 8, "locked hero angle", "", "a battered 1970s Honda parked under cyan neon shot like a hero car, low angle, wet asphalt", "PROBLEM — '…A legendary Honda.'"),
 ("APPROACH", 10, "STATIC LOCKED CAMERA", "marcus", "{marcus} pushing off the chrome lowrider and stepping directly toward the camera on {block}, calm, until he fills frame", "he's handing you a job"),
 ("TURN", 15, "STATIC LOCKED CAMERA — no push, no drift", "marcus", "{marcus} facing the lens on {block}, completely calm, cyan neon behind him, addressing the viewer like an equal", "◆ 'By now you're all drivin' for me. Phone up.'"),
 ("TURN", 12, "STATIC LOCKED CAMERA", "marcus", "{marcus} still to lens, one hand indicating the line of cars behind him without looking", "◆ 'Grab every stolen ride you can — just don't cross your own tail.'"),
 ("HOLD", 8, "STATIC LOCKED CAMERA", "marcus", "{marcus} holding the look into the lens, the smallest amused nod", "◆ 'Everybody else — you drove a Honda. It's okay.' → ▮ CHOP SHOP"),
 ("OUT", 12, "low tracking", "", "a convoy of chrome lowriders pulling out into the neon night on a wet street, taillights, no faces", "the bounce drops."),
]),

("SCENE 10", "The Getaway", "don", "pier", [
 ("ESTABLISH", 12, "slow push through the rain", "", "{pier}, empty, five drag-strip starting lights glowing above wet reflective boards, harbour fog, no people", "Handler VO — 'Two crews, one light.'"),
 ("BUILD", 15, "locked wide", "", "an elderly gold-suited don and a white-suited cartel kingpin squaring off at a staging line on {pier} in the rain, gold-lit against pink-lit, crews behind each of them in silhouette", "RICO — 'This is MY city, old man!'"),
 ("BUILD", 12, "locked camera", "don", "{don} standing in the rain on {pier}, unbothered, looking up past the younger man at something high above the water", "DON — 'It's-a nobody's city, boy. We just rent it.'"),
 ("INSERT", 10, "slow tilt up", "handler", "a single lit penthouse window high above a rain-soaked pier, one black-gloved hand resting flat against the glass, no face, seen from far below", "DON — '…From him.'"),
 ("APPROACH", 10, "STATIC LOCKED CAMERA", "", "an elderly gold-suited don and a white-suited cartel kingpin on {pier} both turning from each other toward the lens in the rain, the five lights beginning to come on above them", "they both remember you're there"),
 ("TURN", 15, "STATIC LOCKED CAMERA — no push, no drift", "", "an elderly gold-suited don facing the lens on {pier} in the rain, gold-lit, addressing the viewer, five starting lights glowing above him", "◆ DON 'You want turf in this city? You gotta be FAST for it.'"),
 ("TURN", 15, "STATIC LOCKED CAMERA — no push, no drift", "rico", "{rico} facing the lens on {pier} in the rain, pink-lit, taking over the briefing, rain running off him", "◆ RICO 'Five lights. The second they all go green, punch it. Thirty seconds. Don't blink.'"),
 ("HOLD", 8, "STATIC LOCKED CAMERA", "", "both bosses to lens on {pier}, holding, the last of the five lights flaring on above them", "◆ → ▮ THE GETAWAY"),
 ("OUT", 10, "locked, lights change", "", "five drag-strip starting lights above a rain-soaked pier snapping from red to green all at once, wet boards flaring, no people", "green — everything moves."),
]),

("SCENE 11", "Throw Up", "marcus", "alley", [
 ("ESTABLISH", 12, "slow drift down the alley", "", "{alley}, empty, brick wall, a searchlight beginning its sweep, steam, no people", "Handler VO — 'Every crew leaves a mark.'"),
 ("BUILD", 15, "locked camera", "problem", "{problem} crouched in {alley} holding a stopwatch upside down, whispering, entirely confident", "PROBLEM — 'Lookout's asleep. Also I ate the lookout's nachos.'"),
 ("BUILD", 10, "locked camera", "marcus", "{marcus} in {alley}, pausing mid-work, turning his head very slowly", "MARCUS — 'We never *had* a lookout, Problem.'"),
 ("INSERT", 8, "locked, light sweep", "", "a searchlight beam sweeping across a brick alley wall revealing a glowing neon graffiti piece, no people", "PROBLEM — '…RIP the nachos, then.'"),
 ("APPROACH", 10, "STATIC LOCKED CAMERA", "marcus", "{marcus} stepping back from a fresh glowing graffiti piece in {alley}, looking at his work, then turning his head toward the lens", "he hands the job over"),
 ("TURN", 15, "STATIC LOCKED CAMERA — no push, no drift", "marcus", "{marcus} facing the lens in {alley}, dim cyan light, a glowing graffiti piece behind him, addressing the viewer quietly", "◆ 'You gotta tag the wall without the light catchin' you.'"),
 ("TURN", 12, "STATIC LOCKED CAMERA", "marcus", "{marcus} still to lens, the searchlight beam crossing behind him mid-sentence, he doesn't flinch", "◆ 'Spray while it's dark, lift off the second the searchlight sweeps.'"),
 ("HOLD", 8, "STATIC LOCKED CAMERA", "marcus", "{marcus} holding the look into the lens, calm, the light passing off him into darkness", "◆ '…We move when you're ready.' → ▮ THROW UP"),
 ("OUT", 8, "locked", "", "a searchlight sweeping a brick wall clean, the glowing graffiti piece left behind in the dark, no people", "boom-bap drops."),
]),

("SCENE 12", "The Combination", "handler", "ballroom", [
 ("ESTABLISH", 15, "slow push into the room", "", "{ballroom}, a giant four-colour combination vault lock glowing at the centre, guests in period black tie blurred and distant", "PEAK — all four stations bleeding together"),
 ("BUILD", 15, "locked camera", "president", "{president} at a podium in {ballroom} under a huge WAR ON CRIME banner, mid-speech, arms wide, national flags behind", "PRESIDENT — 'Tonight this city stands UNITED against crime—'"),
 ("INSERT", 10, "locked, neck-down only", "", "four colour envelopes — gold, hot pink, cyan and violet — sliding into a navy suit jacket at the same moment, shot neck-down, no face", "'—and I have never, EVER taken a dollar from any of these fine… patrons.'"),
 ("BUILD", 12, "slow lateral drift", "", "four crews in period black tie filing into {ballroom} behind a podium, each group lit in its own colour, distant and blurred", "all four crews are in the room"),
 ("INSERT", 8, "locked camera", "mcgraw", "{mcgraw} at a buffet table in {ballroom}, a shrimp halfway to his mouth, entirely oblivious, four gangs sweeping in behind him", "he has no idea"),
 ("APPROACH", 12, "STATIC LOCKED CAMERA", "handler", "a black-gloved hand at the edge of a podium in {ballroom} slowly tipping a champagne glass toward the edge, no face, the four-colour lock glowing beyond", "the room goes quiet"),
 ("TURN", 15, "STATIC LOCKED CAMERA — no push, no drift", "handler", "{handler} standing before the glowing four-colour vault lock in {ballroom}, back three-quarters to camera, head turned just enough to address the lens, face never lit", "◆ 'Pick your colour. Pick your corner. One code opens it.'"),
 ("TURN", 12, "STATIC LOCKED CAMERA", "handler", "{handler} in {ballroom}, still turned away, one gloved hand raised, the four-colour lock pulsing behind him", "◆ 'Black dot, right colour right spot. White dot, right colour wrong spot.'"),
 ("HOLD", 10, "extreme slow motion, locked", "", "a champagne glass falling and shattering in extreme slow motion on a ballroom floor over dark four-colour neon bokeh, no people", "◆ 'When this glass hits the floor— CRACK IT.' → ▮ THE COMBINATION"),
 ("OUT", 10, "locked, whole room", "", "{ballroom} erupting, four-colour light flaring across a packed crowd in period black tie, confetti rising, faces blurred", "the biggest drop of the night."),
]),

("FINALE", "The Empty Vault", "handler", "vault", [
 ("ESTABLISH", 15, "very slow push toward the door", "", "a massive steel vault door groaning open in slow motion at the end of a concrete corridor, one hard overhead light, dust, no people", "Handler VO — 'You made it.'"),
 ("ESTABLISH", 12, "slow push through the doorway", "", "{vault}, completely empty, bare concrete, one hard overhead light, nothing on the floor but dust", "VO — 'Not emptied. Empty.'"),
 ("BUILD", 10, "locked camera", "don", "{don} standing in the doorway of {vault}, staring into the empty chamber, genuinely lost for the first time", "DON — '…Where's-a the money.'"),
 ("BUILD", 10, "locked camera", "rico", "{rico} in the doorway of {vault}, white suit, staring at nothing, quiet for once", "RICO — '…Where's the money.'"),
 ("BUILD", 10, "locked camera", "marcus", "{marcus} in the doorway of {vault}, hands in his bomber pockets, almost amused", "MARCUS — 'Man — where's the *money?*'"),
 ("BUILD", 10, "locked camera", "preston", "{preston} in {vault} looking down at a device in his hand, refreshing it, unbothered", "PRESTON — 'The money is… *pending.*'"),
 ("INSERT", 10, "slow push to macro", "", "a single folded note lying on a bare concrete floor under one hard overhead light, dust in the beam, no people", "add '— H.' in post. Nobody ever finds out who."),
 ("BUILD", 12, "handheld burst in", "mcgraw", "{mcgraw} bursting through the vault doorway with a revolver raised, twenty years of certainty on his face, TV camera light flaring", "McGRAW — 'TWENTY YEARS! I finally caught the Handler!'"),
 ("BUILD", 10, "locked camera", "president", "{president} being handcuffed in the vault doorway, immediately turning to address a television camera that has appeared from nowhere, delighted", "PRESIDENT — 'This is a historic night for justice, and I *personally* led the—'"),
 ("APPROACH", 12, "slow push, locked otherwise", "handler", "{handler} standing on the deck of a black yacht at night beside a tiger, back to camera, a neon city burning gold-pink-cyan-violet in the wake behind", "VO — 'The money was never the score.'"),
 ("TURN", 15, "STATIC LOCKED CAMERA — no push, no drift", "handler", "{handler} on the yacht deck slowly raising a champagne glass toward the lens in a toast, gloved hand, face never visible, neon water behind", "◆ 'The score was the room. You danced, you played, you got made.'"),
 ("HOLD", 12, "STATIC LOCKED CAMERA", "handler", "{handler} holding the toast toward the lens, absolutely still, the tiger beside him unbothered, city glow receding", "◆ '…Welcome to After-Dark. You're made now.'"),
 ("OUT", 12, "low tracking across the water", "", "a black superyacht cutting through dark water at night, a neon city burning gold, pink, cyan and violet in its wake, wet deck sheen, no people", "release into the sing-along."),
 ("POST-CREDIT", 15, "STATIC LOCKED CAMERA", "mcgraw", "{mcgraw} alone in {vault}, crouching to pick up a single glowing telephone handset left on the concrete, turning it over, then looking up directly into the lens", "the myth was a player the whole time. ★★★★★★"),
]),
]

def fill(t):
    # Seeds and locations are long noun phrases. Dropping one straight in front of a
    # participle reads as a run-on ("gold rings completing a slow turn"), so close the
    # phrase with a comma unless the template already punctuated it.
    for table in (LOCS, SEEDS):
        for k, v in table.items():
            tok = '{' + k + '}'
            t = t.replace(tok + ',', v + ',').replace(tok + '.', v + '.').replace(tok, v + ',')
    return t

# --- dialogue ---------------------------------------------------------------
# The audio column was only ever a note to the editor. The generator never saw it,
# so every clip came back with a mouth doing something approximate. These lines are
# the film — they belong in the prompt.

import re

# The two clips where the line genuinely changes hands mid-shot, plus the one line
# with no speaker label on it. Everything else parses.
HAND_OFF = {
 "S8-05": [("preston", "The falcon.", "off"), ("rico", "…It's always the falcon.", "on")],
 "S6-06": [("don", "The vault's open. My crew and his crew—", "on"),
           ("rico", "—and every one of YOU—", "on")],
 "S12-03": [("president", "—and I have never, EVER taken a dollar from any of these "
                          "fine… patrons.", "off")],
}
LABEL = re.compile(r"^\s*(?:◆\s*)?(?:THE TURN\s*—\s*)?"
                   r"(Handler VO|VO|McGRAW|[A-Z][A-Za-z']+)?\s*(\(off\))?\s*(?:—\s*)?'")

def strip_marks(a):
    a = a.split('→')[0]
    return re.sub(r"\s*\([^)]*\)\s*$", "", a).strip()

# Clips with no single subject key that still have people in frame — the two-hander
# beats. Everywhere else a blank subject means an empty plate, so a line over it is
# somebody talking off-screen, not a mouth to sync.
IN_FRAME_NO_SUBJ = {"S6-02", "S6-03", "S6-06", "S6-07", "S6-08", "S10-02", "S10-06"}

def parse_line(clip_id, audio, subj):
    """(speaker_key, line, placement) list. placement: on | off | vo."""
    if clip_id in HAND_OFF:
        return HAND_OFF[clip_id]
    a = strip_marks(audio)
    if a.count("'") < 2:
        return []
    m = LABEL.match(a)
    if not m and '◆' not in audio:
        return []                      # an editor's note that happens to contain an apostrophe
    label, off = (m.group(1), m.group(2)) if m else (None, None)
    line = a[a.index("'") + 1: a.rindex("'")].strip().replace('*', '')
    if len(line.split()) < 2:
        return []
    who = SPEAKERS.get((label or '').upper()) if label else None
    if not who:
        who = subj or 'handler'
    # The Handler's face is never in shot, so his lines can never be a lip-sync —
    # they are voice-over, recorded separately, every time.
    if who == 'handler' or (label or '').upper() in ('VO', 'HANDLER VO'):
        place = 'vo'
    elif off or (subj and who != subj) or (not subj and clip_id not in IN_FRAME_NO_SUBJ):
        place = 'off'
    else:
        place = 'on'
    return [(who, line, place)]

def speech_block(lines, role):
    """The bit the generator actually needs: who says what, how, and lips that match."""
    on = [l for l in lines if l[2] == 'on']
    if not on:
        return None
    to = ("directly into the lens, addressing the viewer" if role in ('TURN', 'HOLD')
          else "in scene, not to camera")
    if len(on) == 1:
        who, line, _ = on[0]
        subject = 'both subjects speak in unison' if who == 'both' else f'the subject speaks {to}'
        body = f'SPOKEN LINE — {subject}: "{line}"' + (
            f' — delivered in {VOICES[who]}' if who in VOICES else '')
    else:
        body = 'SPOKEN LINES — ' + ' then '.join(
            f'the {"first" if i == 0 else "second"} subject speaks {to}: "{line}"'
            + (f' (delivered in {VOICES[who]})' if who in VOICES else '')
            for i, (who, line, _) in enumerate(on))
    sep = ' ' if body.endswith(('."', '?"', '!"', '—"')) else '. '
    return (body + sep + 'Lip movement matches these exact words. Clean audible dialogue, '
                         'no subtitles, no on-screen text')

NO_LINE = ("NO DIALOGUE — the subject does not speak in this clip; mouth closed and still, "
           "the performance is in the eyes")
NO_ROAR = ("NO DIALOGUE — the animal does not roar, snarl, or open its mouth; she is calm "
           "and indifferent throughout")

clips, n = [], 0
for tag, title, owner, loc, rows in BEATS:
    code = tag.replace('SCENE ', 'S').replace('INTRO', 'IN').replace('FINALE', 'FIN')
    for i, (role, sec, cam, subj, prompt, audio) in enumerate(rows, 1):
        n += 1
        cid = f"{code}-{i:02d}"
        negs = [NEG, NEG_PERIOD, NEG_MOTION]
        if subj == 'handler':
            negs.append(NEG_HANDLER)
        body = fill(prompt)

        lines = parse_line(cid, audio, subj)
        block = speech_block(lines, role)
        spoken = sum(len(l.split()) for _, l, p in lines if p == 'on')
        if block:
            negs.append(NEG_SPEAKING)
        elif subj == 'sugar':
            block = NO_ROAR
            negs.append(NEG_SILENT)
        elif subj and subj != 'handler':   # no face on the Handler, so nothing to hold still
            block = NO_LINE
            negs.append(NEG_SILENT)
        say = f" {block}." if block else ""
        dialogue = O([
            ("kind", "speaks" if spoken else ("voice-over" if lines else "silent")),
            ("lines", [O([("speaker", w), ("line", l), ("placement", p),
                          ("delivery", VOICES.get(w))]) for w, l, p in lines]),
            ("words", spoken),
            ("spokenSeconds", round(spoken / WPS, 1) if spoken else 0),
            ("fits", (spoken / WPS) + AIR <= sec if spoken else True),
        ])

        clips.append(O([
            ("id", cid),
            ("n", n),
            ("beat", tag), ("beatTitle", title), ("role", role),
            ("seconds", sec), ("subject", subj or "—"),
            ("camera", cam),
            ("prompt", f"{body}, {cam}.{say}"),
            ("full", f"{body}, {cam}.{say} {STYLE}. {PERIOD}"),
            ("negative", ", ".join(negs)),
            ("audio", audio),
            ("dialogue", dialogue),
            ("lockRef", bool(subj) and subj != '—'),
        ]))

doc = O([
 ("meta", O([
   ("name", "The Score — master prompt sheet"),
   ("what", "Every beat of the film broken into clips of 15 seconds or less, one idea and one camera "
            "move each. Built for a 15-second generation limit: you generate more than you need and "
            "cut it down."),
   ("ratio", "Shoot roughly 2–2.5x the finished length. A 40-second cutaway wants 90–110 seconds of "
             "generated material. That surplus is what lets you cut on the beat instead of using "
             "whatever the model gave you."),
   ("clips", len(clips)),
   ("totalSeconds", sum(c['seconds'] for c in clips)),
 ])),
 ("theFix", O([
   ("problem", "In the Rico test the fourth-wall turn happens between two frames — profile at 5.50s, "
               "full-face at 5.67s. That is not a turn, it is an internal jump cut. The model did it "
               "because one 15-second prompt asked for four things: establish the room, light a cigar, "
               "turn to camera, and deliver a rant."),
   ("alsoSeen", ["The location changes three times in the last five seconds — pink mirrored room, a "
                 "dark exterior with cars, a warehouse, back to the pink room. The set was never locked.",
                 "He shouts for about eight of the fifteen seconds. No dynamic range, so the explosion "
                 "has nothing to explode out of.",
                 "The scar drifts position between frames — the subject wasn't pinned to a reference."]),
   ("fix", "Every turn is now THREE clips: APPROACH (he registers you, still quiet), TURN (locked "
           "camera, the rotation is the only instruction), HOLD (he finishes and holds while the card "
           "lands). That is 30–35 seconds of material for a beat that was trying to happen in under a "
           "second."),
 ])),
 ("rules", [
   "One clip = one idea = one camera move. If a prompt contains 'and then', it is two clips.",
   "On every TURN clip the camera is STATIC AND LOCKED. The rotation of the head is the only motion "
   "in frame. Never combine a turn with a push-in — the model will drop one of them, and it drops the turn.",
   "Lock the subject before you roll: generate the character from their seed, pick the best frame, and "
   "feed that frame as an image reference on every subsequent clip of that character.",
   "Lock the location the same way. The negative block includes 'location change, background change' "
   "for exactly the drift seen in the test.",
   "Give the character somewhere to go. Quiet in APPROACH, build in TURN, land in HOLD. A character who "
   "starts at ten has nowhere left.",
   "Generate 3840x2160 at 23.976 where the model allows, and grade everything — generated and filmed — "
   "through the same house look so the sources match.",
   "No text in-gen. Banners, game cards, the '— H.' note and all titles go on in post.",
 ]),
 ("blocks", O([("STYLE", STYLE), ("PERIOD", PERIOD), ("NEG", NEG),
               ("NEG_PERIOD", NEG_PERIOD), ("NEG_HANDLER", NEG_HANDLER), ("NEG_MOTION", NEG_MOTION),
               ("NEG_SILENT", NEG_SILENT), ("NEG_SPEAKING", NEG_SPEAKING)])),
 ("voices", VOICES),
 ("seeds", SEEDS),
 ("locations", LOCS),
 ("clips", clips),
])

open(OUT, 'w').write(json.dumps(doc, indent=2, ensure_ascii=False) + '\n')

from collections import Counter
print(f'clips: {len(clips)} | total generated footage: {sum(c["seconds"] for c in clips)}s '
      f'({sum(c["seconds"] for c in clips)/60:.1f} min)')
print('all <= 15s:', all(c['seconds'] <= 15 for c in clips))
print('roles:', dict(Counter(c['role'] for c in clips)))
beats = Counter(c['beat'] for c in clips)
print('clips per beat:', dict(beats))
turns = Counter(c['beat'] for c in clips if c['role'] in ('APPROACH','TURN','HOLD'))
print('turn-sequence clips per beat:', dict(turns))
print('every beat has APPROACH+TURN+HOLD:', all(v >= 3 for v in turns.values()) and len(turns) == 14)
