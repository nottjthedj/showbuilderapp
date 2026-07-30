# Show Builder — event platform edition

Recreate the **Grand Theft After-Dark** event system for any brand from a single set
of config files. Fill in the blanks, drop in your logo + show data, run one command,
and get a complete, deployable multi-module site — the same proven formula every time.

> **What GTAD is:** a live, lore-driven interactive game-show. Guests scan a QR on
> arrival, get "made" into the crew, and play a night of games run by the host
> ("the Handler"). The current show is **"The Score"** — a cutaway film in 14 beats
> (Intro + 12 scenes + Finale) cut with 12 games the whole room plays on their phones.
> This tool stamps out that whole experience — booth, crew card, and host console —
> re-skinned for a new brand.

---

## Modules it generates

| Module | File(s) | Who uses it | What it does |
|--------|---------|-------------|--------------|
| **Crew Card** *(player, front door)* | `index.html` / `crew.html` | guests | The **front door** — one scan of the domain lands here: scan-to-get-made card with member number, **what's on screen now** + the live **game card**, live **Wanted Level**, tonight's 12-game run, live **votes**, and a button into the booth. |
| **Photo Booth** | `booth.html`, `gallery.html`, `setup.html`, `netlify/` | guests + operator | Branded camera → photo/video with your overlay → save/share/opt-in. Includes the **gallery admin** (approve/delete) and the secure **Backblaze-B2 → NAS** pipeline. |
| **Handler Console** *(admin)* | `handler.html` | the host | The **run-of-show**: step the 14 beats in locked order and each one gives you the Handler VO, the **◆ turn** teleprompter, the **▮ game card**, the OPEN→OUT assembly and the music cue. Plus the 12-game reference, Wanted-Level control, and a **QR generator** that hands guests a crew card pre-loaded with what's live. Links to the gallery. |

The Booth ships for every brand. The **Crew Card + Handler Console** are generated only
when the config includes a **`show`** (your film beats + games) — see below.

---

## Desktop app — Show Builder (share this with people)

**Show Builder** is a double-click app (no terminal, no Python) for making branded
sites. Fill in the blanks, pick colours, drop in a logo, click **Generate site…** →
out comes a ready-to-deploy folder. It starts pre-loaded with the GTAD preset, and
you can **Save config…** / **Open config…** to share brand setups as small JSON files.

**Get the app:** the GitHub Actions **“Build Show Builder”** workflow builds it for
**Windows (.exe)**, **macOS (.app)** and **Linux** — download from the run's *Artifacts*
(or attach them to a `v*` release). To build it yourself:

```bash
pip install pyinstaller
cd show-builder-app
pyinstaller show-builder.spec        # -> dist/"Show Builder"(.exe / .app)
```

First-launch note (unsigned app): **Windows** → “More info → Run anyway”;
**macOS** → right-click the app → **Open** the first time.

Prefer the command line? The generator underneath is `make_booth.py`:

## Quick start (CLI)

```bash
# reproduce the real show (booth + crew card + handler console)
python3 make_booth.py brands/gtad.json

# a booth-only brand (no show data)
python3 make_booth.py brands/example-midnight-arcade.json
```

Output lands in `build/<projectSlug>/`. Drag that folder onto **app.netlify.com/drop**,
then follow the generated `SETUP.md`. No dependencies — just Python 3.10+.

---

## What you change (per brand)

| File | Controls |
|------|----------|
| `brands/<brand>.json` | Branding (name, logo lockup, kicker, hashtag, CTA, **legal line**), the **colour scheme**, socials, web/deploy info, and a pointer to the show file. |
| `brands/<brand>.show.json` | The **show**: the film (beats, owners, VO, the **◆ turn**, the **▮ game card**, assembly, music), the **games**, the **characters** who own the turns, the **stations** (the room's radio dial), the energy arc and the locked run order + vocabulary and Wanted-Level labels. |
| your logo image | White-on-transparent PNG, embedded + burned into captures. Optional (text lockup fallback). |

Everything the formula keeps fixed — the camera flow, the three photo frames, the
crew-card mechanics, the console's run-of-show/teleprompter/QR tooling — stays put.

---

## Brand config reference (`brands/*.json`)

★ = required. Everything else has a sensible default.

```jsonc
{
  "brand": {
    "name": "Grand Theft After-Dark",   // ★ full name
    "short": "GTAD",                     // ★ short code
    "lineOne": "Grand Theft",            // ★ logo top line
    "lineTwo": "After-Dark",             // ★ logo bottom line
    "kicker": "★ Presents ★",
    "tagline": "Tap below to strike a pose.",
    "followLabel": "Follow the movement",
    "hashtag": "#GrandTheftAfterDark",
    "galleryCta": "Add to GTAD Gallery",
    "galleryDone": "Added to Gallery",
    "legal": "Independent fan tribute event. Not affiliated with …",  // footer disclaimer
    "logo": "gtad-logo.png"              // optional; text lockup if omitted
  },

  "show": "gtad.show.json",              // path (or inline object). Omit → booth-only.

  "colors": {                            // any #hex; darker shades are derived
    "bg": "#000000", "primary": "#FF1493", "primaryBright": "#ff4faf",
    "secondary": "#00E5E5", "accent": "#ffc23d", "ink": "#ffffff", "dim": "#8a8a94"
  },

  "socials": {
    "instagram": "https://instagram.com/grandtheftafterdark",
    "facebook":  "https://facebook.com/grandtheftafterdark",
    "tiktok":    "https://tiktok.com/@grandtheftafterdark",
    "igHandle":  "grandtheftafterdark"
  },

  "web": {
    "storagePrefix": "gtad",             // ★ namespace for saved settings/filenames
    "netlifyName": "gtad",
    "primaryDomain": "booth.grandtheftafterdark.com",
    "rootDomain": "grandtheftafterdark.com",
    "bucketName": "gtad-booth-inbox",
    "projectSlug": "gtad-photobooth",
    "corsRuleName": "gtadBooth",
    "corsOrigins": ["https://gtad.netlify.app", "https://booth.grandtheftafterdark.com"]
  }
}
```

## Show config reference (`brands/*.show.json`)

```jsonc
{
  "meta":     { "name": "…", "show": "The Score", "filmEra": "1977–1983", "legal": "…" },
  "vocabulary": { "crew": "the attendees", "handler": "…", "turn": "the ◆ line", … },
  "wantedLevels": [ { "stars": 1, "label": "ON THE RADAR" }, … 5 ],
  "crewCard": { "madeHeadline": "YOU'RE MADE", "appCta": "PHONE UP", … },
  "stations": [   // the room's radio dial — one sound-world per gang, plus Law + State
    { "id": "gold", "gang": "The Corvettis", "station": "GOLD STANDARD RADIO",
      "era": "…", "genre": "…", "tempo": "…", "bumper": "…", "use": "…" }  // … 6
  ],
  "characters": [ // who owns which turn; casting notes travel with the character
    { "id": "rico", "name": "Rico “El Halcón” Delgado", "station": "pink",
      "look": "…", "casting": "…", "sidekick": "…", "owns": ["s3","s6","s8","s10"] }  // … 7
  ],
  "film": [       // the locked run — Intro + 12 scenes + Finale
    { "n": 4, "tag": "SCENE 3", "title": "Crossfire", "owner": "rico",
      "station": "pink", "energy": "High, hot", "game": 3,
      "vo": "…",                      // the Handler's narration over the scene
      "dialogue": [ { "who": "RICO", "line": "…" }, { "action": "…" } ],
      "turn": "…",                    // ◆ the fourth-wall line that hands over the game
      "gameCard": "…",                // ▮ the card that lands and opens every phone
      "assembly": [ ["OPEN","…"], ["BUILD","…"], ["TURN","…"], ["CARD","…"], ["OUT","…"] ],
      "music": { "station": "…", "bed": "…", "duck": "…", "slam": "…", "cuts": "…", "tip": "…" } }
  ],
  "games": [      // the 12 app games, one per scene
    { "n": 3, "name": "CROSSFIRE", "scene": "SCENE 3", "station": "pink",
      "launchedBy": "rico", "howItPlays": "…", "win": "…", "time": "~3 min" }
  ],
  "energyArc": [ { "beat": "S12", "level": 100 } ],
  "runOfShow": { "locked": true, "order": ["INTRO","SCENE 1"], "note": "…" }
}
```

`brands/gtad.show.json` is the real GTAD bible — **"The Score"**: 14 film beats,
12 app games, 7 characters and 6 stations, extracted from the production bibles.
Copy it to start a new show.

### How a beat works

All 14 beats run the same five-step shape, and the console reads it straight off the
show file:

| Step | | |
|---|---|---|
| **OPEN** | establisher | the world, a vehicle, atmos — music ducks −8/−12 dB, Handler VO in |
| **BUILD** | the scene | the character, the comedy, the action inserts |
| **TURN ◆** | *the money frame* | the character stops, looks **down the lens** and hands the room its game |
| **CARD ▮** | the game card | lands on a stinger; the game opens on every phone |
| **OUT** | release | music slams back in on that gang's station |

**The ◆ turn is the one thing the live show cannot run without.** Shoot those first —
if a production window collapses you can generate everything else and still have a
night. The console renders the turn as the largest, brightest block on the beat for
exactly that reason.

**Turns belong to characters, not to the host.** McGraw owns Scene 1, Marcus owns
2/9/11, Rico owns 3/8, the Don owns 4, Preston owns 5/7; the Handler takes the Intro,
Scene 12 and the Finale. `characters[].owns` is the index and `film[].owner` points
back at it.

### The dial

The room is a **radio dial**: four gangs, four stations, each locked to its own era.
The Handler is the pirate signal cutting across all of them — his transmission ducks
the room into story, then the game slams back in on that gang's station. `stations[]`
carries the era, genre, texture, tempo and bumper voice for each; `film[].music` gives
the per-beat bed → duck → slam. Note the deliberate split: the **film** is period-locked
(1977–1983), the **music** is not — the screen is 1980, the floor is tonight.

### The run is locked

There is no per-night picking in The Score: one night, one film, twelve games, in order.
Stepping the beat in the console sets the live game and pushes it to every crew card, so
guests always see what's on screen now. Acts run I Setup (Intro–S4) · II The Jobs
(S5–S11) · III The Vault (S12→Finale) — and the dips at S5, S8 and S11 are what make the
S12 peak land.

### Two voices

A show has two distinct speaking layers, and the console keeps them apart:

| | Where | What it is |
|---|---|---|
| **Transmission** *(cinematic)* | `chapters[].transmission` | The story beat that opens the night. In-fiction, no winking — the host is the character. One per night; each opens on the previous night's `endsOn` so the season reads as one arc. |
| **Scene** *(4th wall → the game)* | `missions[].scene` | The bridge from story to gameplay. The host steps **out** of the fiction, names the real room, then hands the crowd the rules — which is what gives them permission to commit. |

Scene beats run in order and are read straight off the console:

`cue` (stage direction, not spoken) → `fourthWall` (the step-out) → `driver`
(why this game, *tonight*) → `rules` → `callUp` (get bodies up) → `underscore`
(ad-libs while it runs) → `win` → `out` (hand back to the story).

`driver` is keyed by act — `actI` / `actII` / `actIII` — because the same game
carries different stakes while you're recruiting a crew than it does after the
score has gone down. The console reads the act off tonight's chapter and shows
the matching driver automatically, so a mission can be re-run across the season
without the story going stale. **Copy** lifts the whole scene, act-correct, as a
plain-text script.

---

## Files

```

├─ show_builder.py             the desktop app (Tkinter GUI over the generator)
├─ show-builder.spec           PyInstaller build (Windows/macOS/Linux)
├─ make_booth.py               the generator (stdlib only)
├─ booth_config.schema.json    machine-readable brand-config schema
├─ brands/
│  ├─ gtad.json                the show — reproduces every module
│  ├─ gtad.show.json           “The Score” — 14 film beats + 12 games (the GTAD bible)
│  ├─ gtad-logo.png            the GTAD logo
│  └─ example-midnight-arcade.json   a booth-only rebrand (no show)
└─ templates/                  the tokenized masters (source of truth)
   ├─ booth.html  gallery.html  setup.html      (photo booth)
   ├─ crew.html                                  (player: crew card — also emitted as index.html when a show exists)
   ├─ handler.html                               (admin: handler console)
   ├─ netlify.toml  DEPLOY.md  SETUP.md
   └─ netlify/functions/…                        (secure B2 upload + gallery API)
```

To evolve a module for **every** brand, edit `templates/`. To change **one** brand,
edit its `brands/*.json` (+ `*.show.json`). Regenerate and redeploy. New brand = new
config = the whole system, re-skinned. Expand infinitely.

---

## Notes

- **Colour scheme** flows everywhere — CSS, neon glows, the photo overlay, the crew
  card and console — from seven base colours; darker shades are derived automatically.
- **Live host→crowd sync is built in.** In the Handler Console, tap **Go Live** (enter
  your `GALLERY_TOKEN` once) and every crew phone follows the current chapter, Wanted
  Level and missions within a few seconds — change them on the Show/Missions tabs and
  the whole room updates. Guests scan **one static QR**; live state overrides whatever
  the QR encoded, and falls back to the QR's values when the show isn't live.
  - It reuses the booth's Backblaze B2 (state lives in `state/<event>.json`) via the
    `show-state` function — **no new service or config.** `GET /api/show-state?event=<key>`
    is public (phones poll it); `POST` requires the `GALLERY_TOKEN`.
  - **Per-event keys** — each room/city runs its own live channel. Set an **Event key**
    in the console (e.g. `chicago`, `detroit`); its crew QR carries `?e=<key>` and only
    that room follows it. Multiple shows run simultaneously without colliding. A bare
    `crew.html` (no `?e`) follows the default `main` channel, so single-room stays simple.
- **Live crowd voting — every phone is a buzzer.** In the console's **Poll** tab, pick a
  template (Most Wanted, Find the Rat, Best Crew, Pull the job?) or write your own, tap
  **Open poll** → every crew phone shows the question and buttons; the tally rolls in live
  and **Close & reveal** pushes the winner back to the room. Votes are anonymous, one per
  member. A vote is a single tiny object whose *key* holds the option, so the whole room
  tallies with one list call — no per-vote reads. `POST /api/vote` casts; `GET /api/vote`
  tallies; no new config (same B2).
- **Points + leaderboard.** Closing a poll awards points (everyone who voted earns a little,
  whoever backed the winner earns more). The console's **Board** tab shows the live ranked
  leaderboard (put it on the big screen between rounds), and each crew card shows the
  member's own rank + points. Same list-only trick: points live in the object key
  (`points/<event>/<poll>/<member>__<pts>`), so the whole board tallies in one list call.
  `POST /api/score` awards (operator token); `GET /api/score` returns the board.
- **Operator dashboard.** The Board tab also shows tonight's numbers — **made members**,
  **polls run**, **votes cast**, plus the current chapter and wanted level. Crew check in
  when they get made (`POST /api/crew`); `GET /api/crew` returns the counts (one list each).

## Downloads (permanent)

Tagged releases attach the Show Builder apps as **Release assets, which don't expire**
(the per-run Actions artifacts are cleaned up after ~90 days). Cut one by pushing a
`v*` tag (e.g. `git tag v1.0.0 && git push origin v1.0.0`); the build workflow publishes a
GitHub Release with the Windows, macOS and Linux apps attached.
- The booth's own backend (Backblaze B2 + NAS) is unchanged and documented in the
  generated `SETUP.md`.
```
