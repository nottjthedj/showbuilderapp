# Time Capsule — 2026-07-16

A frozen record of the **known-good working model** of Show Builder as of this date.
If anything ever breaks, this is the state to restore to.

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
