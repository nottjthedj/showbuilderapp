# Time Capsule

Frozen records of the **known-good working models** of Show Builder. If anything ever
breaks, these are the states to restore to.

## Both versions of the show — [`capsule/`](capsule/README.md)

GTAD has had two completely different shows, and **both are kept runnable**:

| | Version | The show | Games |
|---|---|---|---|
| [`capsule/01-season-24-nights/`](capsule/01-season-24-nights/NOTE.md) | **The season** | 24 nights, one story beat each, a season-long arc | 11 physical prop games on stage |
| [`capsule/02-the-score/`](capsule/02-the-score/NOTE.md) | **The Score** *(current)* | one night, a 14-beat cutaway film | 12 games on the crowd's phones |

Each capsule carries the three files that **have to move together** — `gtad.show.json`
plus `templates/handler.html` and `templates/crew.html`. A show is not just its JSON:
each console is built around the shape it renders, so restoring one show file onto the
other's templates gives you a blank console. Swap all three and regenerate:

```bash
cp capsule/<version>/gtad.show.json         brands/gtad.show.json
cp capsule/<version>/templates/handler.html templates/handler.html
cp capsule/<version>/templates/crew.html    templates/crew.html
python3 make_booth.py brands/gtad.json
```

The generator detects the shape either way — it reports `24 chapters · 11 missions` for
the season and `14 beats · 12 games` for The Score. Nothing else in the repo is
version-specific.

**Verified 2026-07-30:** both versions restored into a clean workspace and rebuilt from
scratch — 18 files each, no unresolved tokens, all 9 functions pass `node --check`, and
each console renders *its own* show headlessly with no page errors (the season's
24-chapter picker with 11 missions and their scene scripts; The Score's 14-beat run with
the ◆ turn and 5-step assembly).

---

# The 2026-07-16 snapshot

A frozen record of the known-good working model as of that date.

## The snapshot
- **Commit:** `55eba3d` (the migration into this repo) — the first full, verified build here.
- **Release:** [`v1.0.0`](../../releases/tag/v1.0.0) — the immutable copy. It carries the
  desktop apps (Windows `.exe`, macOS `.app` zip, Linux binary) **and** an auto-attached
  source archive (`Source code (zip)`). Release assets do not expire.
- Both together = today's complete, working Show Builder (code + built apps).

## What works as of today
One config (+ optional logo) generates a complete, deployable branded event system:
- **Crew Card** (`index.html` / `crew.html`) — the guest front door: get made, member number,
  tonight's Job + Handler transmission, live Wanted Level, missions, live votes, score line,
  and a link into the booth.
- **Photo Booth** (`booth.html`, `gallery.html`, `setup.html`) — branded camera, overlay,
  gallery admin, event-QR maker.
- **Handler Console** (`handler.html`) — chapter picker, VO teleprompter, mission picker,
  **Go Live**, **Poll** (live crowd voting), **Board** (leaderboard + made-member/poll/vote stats),
  crew-QR generator, per-event keys.
- **Netlify functions** — secure Backblaze-B2 upload, live `show-state` (per-event), `vote`,
  `score` (points + leaderboard), `crew` (presence/stats). No paid extras; reuses one B2 bucket.
- **Show data** — `brands/gtad.show.json`: the GTAD season (24 chapters, 11 missions).
  *(Superseded — the live show is now “The Score”. The season is preserved runnable at
  [`capsule/01-season-24-nights/`](capsule/01-season-24-nights/NOTE.md) and its writing
  lives on as the lore campaign in [`campaign/`](campaign/README.md).)*
- **Desktop app** — `show_builder.py` + `show-builder.spec` (Tkinter GUI → PyInstaller),
  built for all three OSes by `.github/workflows/build-show-builder.yml`.

Verified 2026-07-16: generates with no unresolved tokens; all functions pass `node --check`;
crew card, handler console, poll, leaderboard and dashboard render correctly headless; the
booth reproduces in the locked brand palette (#FF1493 / #00E5E5).

## How to restore this exact state
```bash
git clone <this repo> show-builder
cd show-builder
git checkout 55eba3d        # or: git checkout v1.0.0
python3 make_booth.py brands/gtad.json    # regenerate the reference show
```
Or just download the app from the `v1.0.0` release and run it.

## Make a new capsule later
Re-run the **Build Show Builder** workflow with a `release_tag` like `capsule-YYYY-MM-DD`
(Actions tab → Run workflow). It publishes a dated, permanent release with the apps + source.

**When the show itself changes shape**, add a new folder under [`capsule/`](capsule/README.md)
with the show file *and* both templates, plus a `NOTE.md` saying what the version is and
how it differs. That is what keeps an old show restorable rather than merely readable in
the git history.
