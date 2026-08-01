#!/usr/bin/env python3
"""Build the 30-day TJ transmission series."""
import json
from collections import OrderedDict as O

OUT = '/home/user/showbuilderapp/marketing/daily-transmissions.json'

# day, phase, title, hook(0-3s), onScreen, script, shots, caption, cta, share, colour
P = [
 (1,"The World","What After-Dark Is",
  "There's a vault in this city with eight figures in it, and in fifty years nobody's opened it.",
  "8 FIGURES. 50 YEARS. STILL LOCKED.",
  "There's a vault in this city with eight figures in it, and in fifty years nobody has opened it.\n"
  "Not because they can't find it. Everybody knows where it is.\n"
  "Because of how it locks — and I'll get to that.\n"
  "My name's TJ. Four gangs run this city and all four of them want what's in that room. On the night, "
  "they're all going to be in the same building trying to take it.\n"
  "So are you.\n"
  "That's Grand Theft After-Dark. Follow this, because from here I'm telling you the whole thing — who "
  "they are, how it works, and how you end up in the middle of it.",
  ["gloved hand on wet glass, neon", "aerial over four glowing districts", "a vault door, one hard light"],
  "Fifty years. Nobody's opened it. That changes on one night. #GrandTheftAfterDark",
  "Follow — the whole story drops daily.","Curiosity gap: a locked thing with a reason nobody's guessed yet.","#9a9ab0"),

 (2,"The World","The Vault",
  "Everybody asks me what's actually in the vault. Wrong question.",
  "WRONG QUESTION.",
  "Everybody asks me what's actually in the vault. That's the wrong question.\n"
  "The right question is why nobody's ever got it out.\n"
  "It's eight figures. It's been eight figures the whole time. It sits under a building downtown that "
  "nobody photographs, and the men who put it there are fifty years dead.\n"
  "They didn't trust each other. Not one of them, not for a second. So they didn't build a safe — they "
  "built an argument, and they made it out of steel.\n"
  "Tomorrow I'll show you what that means.",
  ["macro: steel vault door seams", "dust in a hard overhead beam", "an empty concrete chamber, distant"],
  "It's not a safe. It's an argument made out of steel.","Come back tomorrow.","Cliffhanger — a promise with a date on it.","#e0e0ea"),

 (3,"The World","Four Keys",
  "The vault takes four keys. That's the whole problem.",
  "FOUR KEYS. ONE MINUTE.",
  "The vault takes four keys.\n"
  "Four colours, four turns, and every one of them has to happen inside the same minute. Miss the window "
  "and the whole thing re-locks for another day.\n"
  "One key each went to the four families that built this city. Gold. Pink. Cyan. Violet.\n"
  "Which means no crew in this city can open that vault alone. Not the oldest one, not the richest one, "
  "not the one with the tiger.\n"
  "They need each other.\n"
  "They have never hated anything more in their lives.",
  ["four coloured key-turns, macro, no faces","four lit windows in four districts","a four-colour lock ring glowing"],
  "Four keys. Four crews. Nobody gets it alone. Which one are you? #GTAD",
  "Gold, pink, cyan or violet — comment your colour.","Identity + argument: people pick a side and defend it.","#ffd36b"),

 (4,"The World","Why Tonight",
  "The President is throwing a party in the same building as the vault. Nobody thinks that's an accident.",
  "ONE ROOM. FOUR KEYS.",
  "The President is throwing a gala. He's calling it a night of unity — a city standing together against "
  "crime. There'll be a podium, a banner, and a man in a navy suit telling a room full of criminals how "
  "tough he is on criminals.\n"
  "The gala is in the building. The vault is in that building.\n"
  "Every crew got an invitation. And every crew knows the other three got one too.\n"
  "One night. One room. All four keys in the same place for the first time in fifty years.\n"
  "Nobody thinks that's an accident. Nobody can prove it isn't.",
  ["WAR ON CRIME banner over a podium","four-colour ballroom, distant blurred crowd","a motorcade gliding past, distant"],
  "A night of unity, he's calling it. In the same building as the vault. Sure.",
  "Tickets in bio.","Conspiracy hook — invites the audience to spot the setup.","#ffd36b"),

 (5,"The World","Why You",
  "Four crews are recruiting off the floor that night. That's not a metaphor.",
  "THEY'RE SHORT ON HANDS.",
  "Here's the part the four of them don't advertise.\n"
  "A key gets you a turn. It doesn't get you the room.\n"
  "Four crews, one night, and not one of them has enough hands — not enough people to hold a floor, run "
  "a job, move a package, or crack a four-colour code while three other crews are doing the same thing.\n"
  "So all four of them are recruiting. In that building. Off that floor. From whoever shows up.\n"
  "That's you. You pick a colour at the door and you're theirs for the night.\n"
  "You're not watching this one. You're in it.",
  ["a crowded neon floor, faces out of focus","a hand taking a coloured wristband","four colour-lit crowd pockets"],
  "You don't watch this one. You get recruited.","Pick your colour at the door.","Participation promise — the reason to bring people.","#00e5ff"),

 (6,"The World","The Two Rules",
  "There are two rules that night and I'm only saying them once.",
  "TWO RULES.",
  "There are two rules that night. I'm only saying them once.\n"
  "Don't get wasted.\n"
  "Don't get busted.\n"
  "That's it. That's the list.\n"
  "And I know how simple that sounds. Every single night, somebody in that building manages to break "
  "both of them before midnight, and every single night it's the one who told me they wouldn't.\n"
  "Everything else — the crews, the keys, the vault, the games — all of that is going to be explained to "
  "you by people who are lying to you.\n"
  "The only voice in that room you can trust is coming out of the booth.\n"
  "That's me.",
  ["TJ to camera, hard key, black three-piece","booth silhouette, magenta rim light","crowd, hands up, motion blur"],
  "Don't get wasted. Don't get busted. That's the whole list.",
  "Say it back to me.","A chantable catchphrase — the room repeats it, the comments repeat it.","#ff2d9b"),

 (7,"The World","The Man With No Face",
  "Ask any of the four who really runs this city and watch what happens to their face.",
  "THEY GO QUIET.",
  "Ask any of the four crews who really runs this city. Watch what happens.\n"
  "They go quiet.\n"
  "Then, if they like you, they'll tell you about a man in a black three-piece suit who has never been "
  "photographed. Black gloves. Always turned away.\n"
  "The Corvettis are certain he takes a cut. Rico swears he's been inside the house. The Firm has a file "
  "on him with nothing in it.\n"
  "Four crews. Four keys. And every one of them looking over their shoulder at a man none of them can name.\n"
  "I'd tell you what I know.\n"
  "You should probably hear that part in person.",
  ["black-gloved hand, extreme close, wet neon","CCTV static over a dark lobby","a lit penthouse window from far below"],
  "Four crews. Not one of them will say his name out loud.",
  "Who do you think he is?","Secret-keeping — sharing signals you're in on something.","#8f8fa6"),

 (8,"The Crews","The Corvettis",
  "The oldest crew in this city has never raised its voice. Not once.",
  "GOLD. THE CORVETTIS.",
  "The Corvettis got here first. Off the boats, onto the docks, into the restaurants, and eventually into "
  "everything — quietly, over three generations, one favour at a time.\n"
  "Don Salvatore Corvetti runs them the way his father did. Nothing written down. Nothing said twice. A "
  "back room behind a restaurant where the light is always warm and the conversation is always short.\n"
  "Their whole economy is respect. The money is just how they keep score.\n"
  "They hold the gold key. They've held it for fifty years.\n"
  "And they have never once had to ask for anything twice.",
  ["gold-lit waterfront, wet cobbles, fog","warm gold back room, checkered cloth","a gold pinky ring, macro"],
  "Three generations. Nothing written down. GOLD — the Corvettis. #GTAD",
  "Gold crew, say something.","Faction recruitment — the first of four; people start claiming.","#f5c542"),

 (9,"The Crews","The Don",
  "He was asked what the drop was. He ate a cannoli and thought about it for a full ten seconds.",
  "\"…RESPECT. AND ALSO THE DROP.\"",
  "Don Salvatore Corvetti. Sally Cufflinks. Past seventy-five, and he has never once raised his voice, "
  "because he has never had to.\n"
  "His son Vinnie sweats through every shirt he owns and asks questions the Don finds exhausting.\n"
  "So the Don tells him: take the product. Don't look at the product. Don't talk about the product. Move "
  "it, and make the drop.\n"
  "And Vinnie — God help him — asks what the drop is.\n"
  "The old man eats a cannoli. Thinks about it. Long enough that it gets uncomfortable.\n"
  "And he says: respect. And also the drop.",
  ["elderly don at a table, gold light, quiet menace","a cannoli, macro, warm","a sweating man in an open collar"],
  "\"Pop… what's the drop?\" — a question you only ask once.",
  "Tag the Vinnie in your crew.","Tag-a-friend: the character is a person everyone knows.","#f5c542"),

 (10,"The Crews","Los Halcóns",
  "This crew has never hidden anything in their lives and they're not going to start now.",
  "PINK. LOS HALCÓNS.",
  "Los Halcóns came up through the marina in the eighties, and they did not come up quietly.\n"
  "Where the Corvettis hide, the Halcóns announce. White suits. Neon on the water. A mansion you can see "
  "from the bridge and a tiger in the front room.\n"
  "Rico Delgado believes the loudest crew wins, and for twenty years he's been proven right often enough "
  "to never seriously consider the alternative.\n"
  "If you have to ask whether something in this city is theirs — it isn't.\n"
  "They hold the pink key.\n"
  "They'd like everyone to know that.",
  ["hot-pink neon marina, black yachts, palms","mirrored mansion glowing through rain","a gold falcon medallion, macro"],
  "If you have to ask whether it's theirs, it isn't. PINK — Los Halcóns.",
  "Pink crew — make some noise.","Faction rivalry: directly baits the gold crew.","#ff2d9b"),

 (11,"The Crews","Rico",
  "Somebody shot at Rico Delgado in his own house and he did not blink. He was insulted.",
  "NOT SCARED. INSULTED.",
  "Rico Delgado. El Halcón. What happens when confidence stops asking permission.\n"
  "White linen suit open to the middle of his chest. A gold falcon on a chain. A scar over one eyebrow. "
  "And a full-grown Bengal tiger named Sugar who lies on the white couch and does not care about any of this.\n"
  "Somebody sent targets to his house. A round went past his cheek — close enough to feel it — and he "
  "did not blink.\n"
  "He wasn't frightened. He was insulted.\n"
  "He turned to the tiger and said: you believe this? After everything I do for this city?",
  ["white suit inside a storm of neon tracer fire","tiger on a white couch, unbothered","mirrors and muzzle-flash, no faces"],
  "\"You believe this, Sugar? After everything I do for this city?\"",
  "Which crew would you actually survive in?","Disbelief + humour — the tiger does the sharing.","#ff2d9b"),

 (12,"The Crews","The Street Kings",
  "Everyone gets this crew wrong. They never wanted the city.",
  "CYAN. THE STREET KINGS.",
  "Everybody gets the Street Kings wrong.\n"
  "They never wanted the city. That's the part the other three can't process.\n"
  "Marcus Wells wanted the block — and the block is what he has. Every corner of it. Loyal. And nobody "
  "had to be frightened into it.\n"
  "They're the only crew in this whole story that people join because they actually want to.\n"
  "Cars, corners, hydraulics and the coolest three minutes of music in any room they walk into.\n"
  "They hold the cyan key.\n"
  "And if this whole thing goes wrong, they're the crew you want standing next to you.",
  ["cyan-lit block, chrome lowrider on hydraulics","murals, corner-store glow, wet asphalt","a convoy pulling into neon night"],
  "The only crew people join because they want to. CYAN.",
  "Cyan crew — where you at?","Underdog identity: the sympathetic pick, easy to champion.","#00e5ff"),

 (13,"The Crews","Marcus",
  "Four cop cars in the mirror and this man's only problem is his passenger.",
  "\"PROBLEM. PUT THE TACO DOWN.\"",
  "Marcus Wells. Big Deal. The calmest man in this entire story.\n"
  "Fresh fade. One gold chain. A chrome-and-cyan lowrider sitting on hydraulics. Marcus has never needed "
  "to prove anything to anybody, which is exactly why nobody tries him.\n"
  "One cop in the mirror. Then four. Then a helicopter.\n"
  "And riding shotgun is Lil' Problem, who has not noticed any of this, because he is deep into a plan "
  "for a taco empire funded entirely by money nobody has stolen yet.\n"
  "Marcus doesn't raise his voice either. He just says: Problem. Put the taco down and drive.",
  ["POV windshield, neon rushing, police lights behind","lowrider peeling out, low tracking","rear-view mirror full of red-blue"],
  "One cop. Then four. Then a helicopter. And Problem's still talking about tacos.",
  "Tag your Lil' Problem.","Relatable duo — the comedy travels further than the lore.","#00e5ff"),

 (14,"The Crews","The Firm",
  "The newest crew in this city bought their way in, and nobody has forgiven them for it.",
  "VIOLET. THE FIRM.",
  "The Firm bought their way in.\n"
  "No history. No neighbourhood. No bodies. Just a glass tower, a great deal of other people's money, "
  "and a founder who will tell you at length that he has reinvented theft.\n"
  "They're the newest crew, the richest crew, and by a considerable margin the least liked.\n"
  "The other three call them tourists. The Firm calls the other three legacy infrastructure.\n"
  "They hold the violet key. They also have a slide deck about the violet key.\n"
  "And here's the uncomfortable part: they're not wrong about very much.",
  ["cold violet glass towers, one lit floor high up","a wall of surveillance monitors, screen glow","a business card straightened, macro"],
  "The other three call them tourists. They call the other three legacy infrastructure.",
  "Violet crew — defend yourselves.","Villain faction: people love picking the hated one.","#a06bff"),

 (15,"The Crews","Preston",
  "He's reinvented theft. No masks, no guns. He calls it a proprietary infiltration solution.",
  "IT'S IN PRIVATE BETA.",
  "Preston Ashford Sterling the Third has reinvented theft.\n"
  "No masks. No guns. Just — his words — a proprietary infiltration solution. He calls it Breach. It is "
  "currently in private beta.\n"
  "He demoed it once. It shrieked in his hands, the room went emergency red, and his analyst Kayleigh — "
  "standing on the other side of the bench already holding a defused one — did not look up.\n"
  "He called it a soft launch.\n"
  "And when he asked her who in this city was leaking, she said: it's you, Preston. You post everything.\n"
  "He took that as engagement.",
  ["black turtleneck fumbling a wired device","violet room flipping emergency red","an analyst with a tablet, bored, unbothered"],
  "\"That was a soft launch.\" #GTAD",
  "Every office has one. Name them.","Recognition humour — everyone has worked for this man.","#a06bff"),

 (16,"The People","Vinnie the Veal",
  "This man has one job and he has already asked three questions about it.",
  "ONE JOB. THREE QUESTIONS.",
  "Vinnie the Veal. The Don's son. Slicked hair, open collar, gold chain, and a shirt he is sweating "
  "through in real time.\n"
  "Vinnie has one job on the night: move the product, make the drop, don't ask what it is.\n"
  "So far Vinnie has asked what it is three times.\n"
  "His father has explained it to him twice, and the second explanation was worse than the first.\n"
  "I want to be clear that the Corvettis are the most feared crew in this city, and their succession plan "
  "is this guy.",
  ["a sweating man in an open collar, gold light","a briefcase on a checkered tablecloth","the don's hand, dismissive, macro"],
  "The most feared crew in the city. This is the succession plan.",
  "Every family's got a Vinnie.","Family-tag humour — the most re-shareable format there is.","#f5c542"),

 (17,"The People","Lil' Problem",
  "He's already spent the vault money. In his head. On tacos.",
  "A TACO *EMPIRE*.",
  "Lil' Problem. Cyan tracksuit, gold rope, permanently mid-sentence, permanently eating.\n"
  "Problem has already spent the vault money. In his head. On tacos.\n"
  "Not a taco truck — he wants that on record. A fleet. A taco empire.\n"
  "He has done no maths on this. He has, however, already picked the name and thought about the logo.\n"
  "And when someone suggested he might boost the getaway car himself — that it might be his origin story "
  "— Marcus had to explain to him, gently, that it's a Honda.\n"
  "Problem's response: a legendary Honda.",
  ["cyan corner, a man mid-laugh holding food","a beat-up Honda under neon, hero angle","hands gesturing a plan, no face"],
  "\"…A *legendary* Honda.\"","Tag whoever's already spending it.","Pure comedy clip — the one that escapes the fanbase.","#00e5ff"),

 (18,"The People","Sugar",
  "During a fifty-fifty handshake between two crime families, the tiger robbed both of them.",
  "NOBODY NOTICED.",
  "Two crews. One table. A fifty-fifty split, agreed like brothers, with a handshake neither man was "
  "willing to let go of first.\n"
  "The Don is watching Rico. Rico is watching the Don. Both of them are absolutely certain they're the "
  "one doing the outsmarting.\n"
  "And behind them — completely unnoticed, in no hurry whatsoever — Sugar picks up a bag of money off "
  "the table and walks out of the building with it.\n"
  "A tiger.\n"
  "Robbed a summit of the two most dangerous men in this city.\n"
  "Neither of them has noticed yet. I'm not going to be the one to tell them.",
  ["two bosses shaking hands, gold vs pink light","a tiger padding out of frame with a gold bag","an empty spot on a table where a bag was"],
  "The tiger robbed both crime families and nobody has noticed yet.",
  "Send this to someone who'd get away with it.","The single most shareable image in the world — an animal outsmarting everyone.","#ff2d9b"),

 (19,"The People","Kayleigh",
  "She ended her boss's entire investigation in one sentence and went back to her tablet.",
  "\"THE RAT IS YOU, PRESTON.\"",
  "Kayleigh works for The Firm. Sleek low bun, wireless headset, tablet, entirely unbothered.\n"
  "Preston decided somebody in this city was leaking, and ordered a full loyalty audit. Every crew. "
  "Cross-referenced. He wanted to know — and I want to be accurate here — whether they could gamify it. "
  "Whether the rat could be a subscription.\n"
  "Kayleigh looked up exactly once and said: the rat is you, Preston. You post everything.\n"
  "Then went back to her tablet.\n"
  "She is paid a fraction of what he is.\n"
  "She is the only reason that tower is still standing.",
  ["analyst at a monitor wall, violet glow","a red target box snapping onto a blurred face","a tablet, one raised eyebrow, no full face"],
  "Ended the whole investigation in one sentence. Went back to work.",
  "Tag the Kayleigh holding your workplace together.","Workplace recognition — huge crossover outside the nightlife audience.","#a06bff"),

 (20,"The People","McGraw",
  "Twenty years chasing one man, and he has been wrong every single time.",
  "20 YEARS. 0 ARRESTS.",
  "Detective Dutch McGraw. Twenty years, one trench coat, a toothpick, and a wall of faces.\n"
  "He's hunting a man with no face and a vault with no bottom, and every single year he almost has him.\n"
  "He'll put five people in a lineup — one from each crew, and one civilian who wandered in off the dance "
  "floor holding his booking number upside down — and he will point, with total confidence, at the wrong one.\n"
  "He always points at the wrong one.\n"
  "Here's the thing about McGraw, though.\n"
  "He's the only honest man in this entire story. And it's cost him everything.",
  ["venetian blinds, red-blue siren light","a lineup wall in silhouette","a toothpick, a tired face, hard key"],
  "Twenty years. Every year he almost has him. #GTAD",
  "Is he ever going to get it right?","Sympathy + prediction — people theorise in the comments.","#ff5a6e"),

 (21,"The People","President Diamante",
  "He says he knows all the criminals personally. That's not a slip. He means it as a boast.",
  "\"GREAT PEOPLE. TOTAL WINNERS.\"",
  "President Maximillian Diamante will tell you this city is safer than it has ever been.\n"
  "Believe him. He'll say it under a banner that reads WAR ON CRIME, in a room where every single crew "
  "in this story is holding a drink.\n"
  "He says nobody's tougher on crime than him, because he knows all the criminals personally. Great "
  "people. Total winners.\n"
  "That's not a slip of the tongue. He means it as a boast.\n"
  "And while he's saying it, four envelopes — one gold, one pink, one cyan, one violet — go into his "
  "jacket at the same time.\n"
  "He has never, ever taken a dollar from any of these fine… patrons.",
  ["podium under a WAR ON CRIME banner","four coloured envelopes into a jacket, neck-down","a grid of storefront TVs on a wet street"],
  "\"I know all the criminals personally. Great people.\"",
  "Four more years?","Satire — political comedy travels beyond the event audience.","#ffd36b"),

 (22,"The People","The Myth, Again",
  "The Firm has a file on him. I've seen it. There's nothing in it.",
  "THE FILE IS EMPTY.",
  "I told you about the man with no face. Here's what I've learned since.\n"
  "The Corvettis are certain he takes a cut of everything — they've been paying something to somebody for "
  "three generations and the Don won't say to who.\n"
  "Rico swears he's been inside the house. Rico has changed the locks four times.\n"
  "And The Firm has a file on him. I've seen the file.\n"
  "There is nothing in it.\n"
  "No photograph. No name. No record of a man who four crews will not make a move without thinking about.\n"
  "Four keys. Four crews. And all of them frightened of the same empty folder.",
  ["a manila file opening on nothing","a black-gloved hand tipping a glass off a podium","a single lit window, rain, very high up"],
  "An empty file. Four terrified crime families. Explain that one.",
  "Theories below. I'll read them.","Mystery participation — comments become the content.","#8f8fa6"),

 (23,"The Games","How It Actually Works",
  "You don't watch this. Your phone is the controller and you're playing for a gang.",
  "PHONE UP. PICK A COLOUR.",
  "Let me tell you how the night actually runs, because people keep asking.\n"
  "You get in. You pick a colour at the door — gold, pink, cyan or violet. That's your crew now.\n"
  "Through the night, the story plays on the screens. It stops. Somebody looks straight down the lens "
  "and hands you a job.\n"
  "And then everybody's phone lights up at once and you play it. Right there. On the floor. Against every "
  "other crew in the building.\n"
  "There's nothing to download at the door and nothing to carry. No props, no lines, no getting picked "
  "on stage.\n"
  "Twelve games. One night. Your colour's on the board the whole time.",
  ["a floor of raised phones glowing four colours","a game card hitting the screens","a leaderboard flipping over"],
  "Phone up. Pick a colour. Twelve games. #GTAD","Full how-to-play in bio.","Removes the #1 objection: 'do I have to get on stage?'","#00e5ff"),

 (24,"The Games","The Interrogation",
  "The first game of the night is eight questions and a detective who can tell when you're lying.",
  "DON'T CRACK.",
  "First game of the night. McGraw's got five of you in a lineup and the whole room watching.\n"
  "Eight questions. Fast. On your phone.\n"
  "Answer straight, answer quick, and do not crack — because he's been doing this twenty years and the "
  "whole city sees your answer.\n"
  "It's the easiest game of the night and it's the one people lose, because they get clever.\n"
  "Top score talks first.\n"
  "And whoever talks first sets the tone for their crew for the rest of the night.",
  ["five suspects in silhouette at a height marker","phones lighting up in the dark","a toothpick jabbed at the lens"],
  "Eight questions. Don't get clever. #GTAD",
  "How fast are you under pressure?","Low-stakes challenge — invites a self-assessment reply.","#ff5a6e"),

 (25,"The Games","The Joyride",
  "Your phone is a getaway car and this city has dogs in it.",
  "COPS. PEOPLE. DOGS.",
  "The Joyride.\n"
  "Your phone is the getaway car. Grab the cash, keep it on the road, and dodge everything this city "
  "throws at you — cops, people, dogs.\n"
  "Every hit you take is a wanted star. Rack up too many and you're done, and your crew feels it.\n"
  "The whole room is driving at once. You can hear it happen — the noise the floor makes when everybody "
  "loses at the same corner is genuinely one of my favourite sounds.\n"
  "Furthest run takes it.\n"
  "And Problem, if you're watching — put the taco down and drive.",
  ["POV windshield, wet neon, speed","a wall of police lights flooding a street","a floor of phones tilting in unison"],
  "Cops, people, dogs. Every hit is a star.","Who's driving? Tag your wheelman.","Callback to day 13 — rewards followers who've been there.","#00e5ff"),

 (26,"The Games","Crossfire",
  "The whole city is shooting at you and you get three lives.",
  "THREE LIVES. THAT'S ALL.",
  "Crossfire.\n"
  "Rico's house. Somebody sent targets and now the whole city is shooting at you.\n"
  "Three lives, that's all you get. Drag, weave, don't get hit. Last one standing in the crossfire owns "
  "the night.\n"
  "This is the loudest the room gets all evening — it's the pink station, it's the hottest music we play, "
  "and there is always a moment where four hundred people all flinch at the same time.\n"
  "Last one standing.\n"
  "Say goodnight to the bad guy.",
  ["neon tracer streaks through pink haze","a white suit unflinching in the storm","a crowd flinching in unison, wide"],
  "Three lives. Last one standing owns the night.",
  "Are you surviving this one?","Competitive callout — people tag whoever they'd beat.","#ff2d9b"),

 (27,"The Games","The Blueprint",
  "You get ten seconds to memorise the vault. Then it's gone.",
  "TEN SECONDS. ONE LOOK.",
  "The Blueprint.\n"
  "Two plans go up on the screens. Ten seconds each. Burn every icon into your head — and then they're "
  "gone, and you have to call them back.\n"
  "Miss one and the whole job's blown for your crew.\n"
  "Now — Rico doesn't need the paper. Rico remembers every face that ever crossed him. Rico has told us "
  "all repeatedly that his memory is perfect.\n"
  "Rico cannot remember the first icon.\n"
  "It's always the falcon. It has been the falcon every single time.\n"
  "Ten. Nine.",
  ["glowing blueprint icons on frosted glass","a falcon icon tapped, macro","phones held up in a dark room"],
  "It's always the falcon. Every time. #GTAD",
  "How many can you hold for 10 seconds?","Testable skill — people want to prove they'd win.","#c07ad0"),

 (28,"The Games","The Combination",
  "Everything all night has been building to one code, and it takes all four colours.",
  "ONE CODE. FOUR COLOURS.",
  "This is what the whole night has been for.\n"
  "The Combination. The vault, in the middle of the room, and one four-colour code that opens it.\n"
  "Pick your colour. Pick your corner. Black dot means right colour, right spot. White dot means right "
  "colour, wrong spot. Crack it before the other three crews do.\n"
  "It is the loudest, fastest, most unhinged five minutes of the night, and the whole building is "
  "screaming numbers at each other.\n"
  "A glass goes off the podium in slow motion.\n"
  "And when it hits the floor — every phone in that building starts cracking.",
  ["a giant four-colour lock ring glowing","a champagne glass falling, extreme slow-mo","four-colour ballroom, everyone lit up"],
  "One code. Four colours. Whoever cracks it first takes the whole thing.",
  "What colour are you cracking for?","The payoff post — the one to boost paid.","#ffd36b"),

 (29,"The Games","Pick Your Colour",
  "There are four crews and you're going to be in one of them. Choose now.",
  "GOLD. PINK. CYAN. VIOLET.",
  "Four crews. You're going to be in one of them.\n"
  "Gold — the Corvettis. Old money, quiet rooms, nothing written down. You join gold if you think power "
  "should be polite.\n"
  "Pink — Los Halcóns. Loudest crew wins. You join pink if you've never once been the quietest person "
  "in a room.\n"
  "Cyan — the Street Kings. The block, the beat, the bounce. You join cyan if your friends actually like you.\n"
  "Violet — The Firm. You join violet if you've read the terms and conditions and found a way through them.\n"
  "Choose now. Because at the door, it's final.",
  ["four colour-lit crowd pockets, wide","four wristbands on four wrists","a door, four coloured lights above it"],
  "Gold, pink, cyan or violet. At the door it's final. Which one? #GTAD",
  "Comment your colour. I'm counting.","THE identity post — the single most shareable format on any platform.","#ff2d9b"),

 (30,"The Games","Doors",
  "Fifty years that vault's been shut. Tonight all four keys are in the same building.",
  "TONIGHT.",
  "Fifty years that vault has been shut.\n"
  "Tonight, for the first time, all four keys are in the same building — and so are all four crews, and "
  "so are you.\n"
  "You know the crews now. You know the vault. You know what it takes to open it.\n"
  "So here's the last thing I'll say before the doors.\n"
  "Don't get wasted. Don't get busted. Pick your colour and hold it all night.\n"
  "And when this city starts lying to you — and it will, from the moment you walk in — the only voice in "
  "that room you can trust is coming out of the booth.\n"
  "That's me. See you tonight.",
  ["doors opening onto a neon floor","TJ to camera, hard key, black three-piece","a crowd surging, motion blur"],
  "Tonight. All four keys, one building. Don't be late.",
  "Doors at [TIME]. Last tickets in bio.","Urgency + the catchphrase the audience already knows.","#ff2d9b"),
]

WEEKS = {"The World":"Week 1 — the world (what is this, why should I care)",
         "The Crews":"Week 2 — the crews (pick a side)",
         "The People":"Week 3 — the people (fall in love with them)",
         "The Games":"Week 4 — the games and the ask (now buy a ticket)"}

posts = []
for (day, phase, title, hook, on, script, shots, caption, cta, share, col) in P:
    words = len(script.split())
    posts.append(O([
        ("day", day), ("phase", phase), ("title", title), ("colour", col),
        ("hook", hook), ("onScreenText", on),
        ("script", script),
        ("runtimeSec", round(words / 2.5)),     # ~150 wpm delivery
        ("words", words),
        ("shots", shots), ("caption", caption), ("cta", cta), ("shareTrigger", share),
    ]))

doc = O([
 ("meta", O([
   ("name", "Grand Theft After-Dark — the daily transmissions"),
   ("what", "A 30-day daily lore series narrated by TJ (the Handler), the show's marketing face. "
            "One post a day, 30–60 seconds, shot to camera. Each one teaches exactly one thing and "
            "ends with one ask."),
   ("arc", [WEEKS[k] for k in ("The World","The Crews","The People","The Games")]),
   ("ladders", "Every post seeds something the room meets on the night — see brands/gtad.show.json"),
 ])),
 ("format", O([
   ("shape", ["0:00–0:03  HOOK — TJ already mid-thought. One line that opens a question.",
              "0:03–0:20  THE LORE — exactly one fact about the world. Never two.",
              "0:20–0:45  THE TURN — tie it to the room, the night, or the viewer.",
              "0:45–0:60  THE ASK — one action. Never two."]),
   ("hookRules", ["Start mid-sentence. Never 'hey guys', never 'welcome to', never say the format's name.",
                  "Lead with a number, a name, or a contradiction.",
                  "Say the thing that sounds like it shouldn't be said out loud.",
                  "The on-screen text is NOT the spoken line — it's the punch under it.",
                  "If the first frame needs context to make sense, it's not a hook."]),
   ("craft", ["Shot to camera, TJ lit hard against black with one neon rim in the crew's colour.",
              "Hard cut in — no logo sting at the front. Brand at the END or nowhere.",
              "Burned-in captions always: most of this is watched on mute.",
              "9:16, one idea per post. If it needs two, it's two posts.",
              "Period film look for the world b-roll (1977–1983); TJ himself is present-day."]),
 ])),
 ("shareEngine", O([
   ("principle", "Nobody shares an advert for a party. They share a thing that says something about them, "
                 "a thing that settles an argument, or a thing they can't believe."),
   ("mechanisms", [
     O([("name","Identity — pick a colour"),
        ("why","Choosing a faction is a self-description, and self-descriptions get posted. Four crews means "
               "four tribes recruiting for you, for free."),
        ("posts",[3,8,10,12,14,29])]),
     O([("name","Argument — my crew beats your crew"),
        ("why","Rivalry is the cheapest engagement there is. Every crew post is written to bait the other three."),
        ("posts",[10,12,14,26,29])]),
     O([("name","Secret — never explain the myth"),
        ("why","Sharing a mystery signals you're on the inside. The moment it's explained, it stops moving."),
        ("posts",[7,22])]),
     O([("name","Tag-a-friend — the characters are people they know"),
        ("why","Vinnie, Problem and Kayleigh exist to be someone's mate, someone's cousin, someone's colleague. "
               "This is the format that escapes your own audience."),
        ("posts",[9,16,17,19])]),
     O([("name","Disbelief — the tiger"),
        ("why","An animal outsmarting two crime families is the single most forwardable thing in this world. "
               "Do not overthink it, do not over-explain it."),
        ("posts",[11,18])]),
     O([("name","Flex — you're made now"),
        ("why","The crew card, the member number and the leaderboard are post-event proof. The audience makes "
               "the recap content for you."),
        ("posts",[23,28,30])]),
   ]),
   ("cadence", "One post a day for 30 days, timed to land on the event. Day 15 and day 28 are the two to put "
               "money behind — 15 because the crews are all established by then, 28 because it's the payoff."),
   ("reply", "TJ replies in character, always. Never break it. A comment answered by the Handler is worth more "
             "than a hundred impressions, and people screenshot it."),
   ("ugc", "After the night: repost the room's own footage under the same voice. The crowd becomes the cast, "
           "which is the whole thesis of the show anyway."),
 ])),
 ("posts", posts),
])

open(OUT, 'w').write(json.dumps(doc, indent=2, ensure_ascii=False) + '\n')
rt = [p['runtimeSec'] for p in posts]
print(f'posts: {len(posts)}')
print(f'runtime: min {min(rt)}s · max {max(rt)}s · mean {sum(rt)/len(rt):.0f}s')
print('all within 30-60s:', all(28 <= r <= 62 for r in rt), '| outliers:',
      [(p['day'], p['runtimeSec']) for p in posts if not 28 <= p['runtimeSec'] <= 62] or 'none')
print('distinct hooks:', len({p['hook'] for p in posts}) == len(posts))
print('phases:', {k: sum(1 for p in posts if p['phase'] == k) for k in WEEKS})
