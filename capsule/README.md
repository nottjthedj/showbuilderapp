# Capsule — both versions of the show, kept runnable

GTAD has had two completely different shows. Both are frozen here, and **both still
generate a working site**. This is the drawer you open when you want the other one back.

| | Version | The show | Games |
|---|---|---|---|
| [`01-season-24-nights/`](01-season-24-nights/) | **The season** | 24 nights, one story beat each, a season-long arc | 11 physical prop games run on stage |
| [`02-the-score/`](02-the-score/) | **The Score** *(current)* | one night, a 14-beat cutaway film | 12 games on the crowd's phones |

## Why the templates are in here too

A show is **not** just its `.show.json`. The Handler Console and Crew Card are built
around the shape of the show they render — the season's console picks a chapter and
three missions, The Score's console steps a locked run of 14 beats. Restoring one show
file onto the other's templates gives you a blank console.

So each capsule carries all three files that have to move together:

```
<version>/
  gtad.show.json          the show
  templates/handler.html  the console that knows how to render it
  templates/crew.html     the guest card that knows how to render it
```

## Restoring a version

```bash
cp capsule/<version>/gtad.show.json         brands/gtad.show.json
cp capsule/<version>/templates/handler.html templates/handler.html
cp capsule/<version>/templates/crew.html    templates/crew.html
python3 make_booth.py brands/gtad.json
```

The generator reads whichever shape it finds — it reports `24 chapters · 11 missions`
for the season and `14 beats · 12 games` for The Score — so no other file needs touching.

Nothing else in the repo is version-specific: the booth, the Netlify functions, the
brand config, the colours and the logo are shared by both.

## Verified

Both versions were restored into a clean workspace and rebuilt from scratch. Each one
generates 18 files with no unresolved template tokens, all 9 functions pass
`node --check`, and each console renders **its own** show headlessly with no page
errors — the season's 24-chapter picker with 11 missions and their scene scripts, and
The Score's 14-beat run with the ◆ turn and 5-step assembly intact.
