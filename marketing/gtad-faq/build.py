#!/usr/bin/env python3
"""Generate GTAD FAQ infographic HTML files (one per FAQ category)."""
import base64, pathlib

HERE = pathlib.Path(__file__).parent
OUT = HERE / "html"; OUT.mkdir(exist_ok=True)
LOGO = base64.b64encode((HERE / "gtad-logo-alpha.png").read_bytes()).decode()

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{background:#000;-webkit-font-smoothing:antialiased}
.canvas{width:1080px;position:relative;background:#000;overflow:hidden;
  padding:56px 60px 44px;font-family:Inter,sans-serif}
.canvas::before{content:"";position:absolute;inset:0;pointer-events:none;
  background:radial-gradient(900px 520px at 12% -6%,rgba(255,20,147,.20),transparent 62%),
             radial-gradient(760px 520px at 96% 4%,rgba(0,229,229,.13),transparent 60%),
             radial-gradient(900px 700px at 50% 112%,rgba(255,194,61,.09),transparent 62%)}
.canvas::after{content:"";position:absolute;inset:0;pointer-events:none;opacity:.30;
  background:repeating-linear-gradient(0deg,rgba(255,255,255,.045) 0 1px,transparent 1px 4px)}
.inner{position:relative;z-index:2}

/* ---------- header ---------- */
.head{display:flex;align-items:center;gap:28px;padding-bottom:26px;
  border-bottom:2px solid rgba(255,255,255,.13)}
.logo{width:124px;height:124px;object-fit:contain;flex:none}
.head-txt{flex:1}
.kicker{font-family:'JetBrains Mono',monospace;font-size:16px;font-weight:700;
  letter-spacing:.30em;color:#00E5E5;text-transform:uppercase;margin-bottom:9px}
h1{font-family:Oswald,sans-serif;font-weight:700;font-size:74px;line-height:.92;
  letter-spacing:-.005em;color:#fff;text-transform:uppercase}
h1 em{font-style:normal;color:#FF1493}
.filetag{flex:none;text-align:right;font-family:'JetBrains Mono',monospace}
.filetag .n{font-family:Oswald,sans-serif;font-weight:700;font-size:88px;line-height:.8;
  color:transparent;-webkit-text-stroke:2px rgba(255,255,255,.30)}
.filetag .of{font-size:14px;letter-spacing:.24em;color:#8a8a94;margin-top:10px}

/* ---------- primitives ---------- */
main{padding-top:34px;display:flex;flex-direction:column;gap:22px}
.lab{font-family:'Barlow Condensed',sans-serif;font-weight:700;font-size:23px;
  letter-spacing:.20em;text-transform:uppercase;color:#00E5E5}
.lab.p{color:#FF1493}.lab.g{color:#ffc23d}
.card{position:relative;border:1px solid rgba(255,255,255,.11);padding:30px 32px;
  background:linear-gradient(170deg,rgba(255,255,255,.062),rgba(255,255,255,.016))}
.card::before,.card::after{content:"";position:absolute;width:15px;height:15px;
  border-color:rgba(255,20,147,.85);border-style:solid}
.card::before{top:-1px;left:-1px;border-width:2px 0 0 2px}
.card::after{bottom:-1px;right:-1px;border-width:0 2px 2px 0}
.card.cy::before,.card.cy::after{border-color:rgba(0,229,229,.85)}
p{font-size:25px;line-height:1.48;color:#c8c8d2;font-weight:400}
p b,p strong{color:#fff;font-weight:600}
.q{font-family:Oswald,sans-serif;font-weight:600;font-size:31px;color:#fff;
  text-transform:uppercase;letter-spacing:.005em;line-height:1.12;margin-bottom:11px}
.q::before{content:"Q ";color:#FF1493}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:22px}
.grid2.top{align-items:start}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.stat{font-family:Oswald,sans-serif;font-weight:700;font-size:76px;line-height:.9;color:#FF1493}
.stat.cy{color:#00E5E5}.stat.g{color:#ffc23d}
.sub{font-size:20px;line-height:1.42;color:#9a9aa6;margin-top:9px}
.hair{height:1px;background:rgba(255,255,255,.12)}

/* chips */
.chips{display:flex;gap:12px;flex-wrap:wrap}
.chip{font-family:'Barlow Condensed',sans-serif;font-weight:700;font-size:22px;
  letter-spacing:.13em;text-transform:uppercase;color:#e8e8ee;padding:10px 18px;
  border:1px solid rgba(255,255,255,.20);background:rgba(255,255,255,.05)}
.chip.p{color:#FF1493;border-color:rgba(255,20,147,.5);background:rgba(255,20,147,.10)}
.chip.cy{color:#00E5E5;border-color:rgba(0,229,229,.5);background:rgba(0,229,229,.10)}
.chip.g{color:#ffc23d;border-color:rgba(255,194,61,.5);background:rgba(255,194,61,.10)}

/* timeline */
.tl{display:flex;position:relative;padding-top:30px}
.tl::before{content:"";position:absolute;top:36px;left:6%;right:6%;height:2px;
  background:linear-gradient(90deg,#FF1493,#ffc23d,#00E5E5)}
.tl .node{flex:1;text-align:center;position:relative}
.tl .dot{width:15px;height:15px;background:#000;border:3px solid #fff;border-radius:50%;
  margin:0 auto 20px;position:relative;z-index:2}
.tl .t{font-family:Oswald,sans-serif;font-weight:700;font-size:41px;color:#fff;line-height:1}
.tl .d{font-family:'Barlow Condensed',sans-serif;font-weight:700;font-size:20px;
  letter-spacing:.13em;text-transform:uppercase;color:#00E5E5;margin-top:8px}

/* acts */
.act{border:1px solid rgba(255,255,255,.12);padding:26px 24px;
  background:linear-gradient(180deg,rgba(255,20,147,.13),rgba(255,255,255,.02))}
.act.a2{background:linear-gradient(180deg,rgba(255,194,61,.13),rgba(255,255,255,.02))}
.act.a3{background:linear-gradient(180deg,rgba(0,229,229,.13),rgba(255,255,255,.02))}
.act .n{font-family:'JetBrains Mono',monospace;font-size:15px;letter-spacing:.24em;
  color:#8a8a94;margin-bottom:12px}
.act .t{font-family:Oswald,sans-serif;font-weight:700;font-size:35px;color:#fff;
  line-height:1.02;text-transform:uppercase}
.act .s{font-size:19px;color:#9a9aa6;margin-top:10px;line-height:1.4}

/* rank ladder */
.rank{display:flex;align-items:center;gap:24px;padding:17px 22px;
  border-left:5px solid var(--c);background:linear-gradient(90deg,var(--bg),transparent 78%)}
.rank .stars{font-size:19px;letter-spacing:3px;color:var(--c);width:118px;flex:none}
.rank .nm{font-family:Oswald,sans-serif;font-weight:700;font-size:37px;color:#fff;
  text-transform:uppercase;width:238px;flex:none;line-height:1}
.rank .nt{font-family:'JetBrains Mono',monospace;font-size:16px;color:var(--c);
  letter-spacing:.05em;margin-top:6px;font-weight:700}
.rank .rw{font-size:22px;color:#c8c8d2;line-height:1.36;flex:1}

/* feature cells */
.feat{border:1px solid rgba(255,255,255,.11);padding:18px 20px;
  background:linear-gradient(170deg,rgba(255,255,255,.05),rgba(255,255,255,.014));
  border-top:3px solid var(--c,#00E5E5)}
.feat .k{font-family:'JetBrains Mono',monospace;font-size:13px;letter-spacing:.22em;
  color:var(--c,#00E5E5);margin-bottom:9px;font-weight:700}
.feat .h{font-family:Oswald,sans-serif;font-weight:700;font-size:26px;color:#fff;
  text-transform:uppercase;line-height:1.06}
.feat .b{font-size:19px;color:#a4a4b0;margin-top:9px;line-height:1.4}

/* routing rows */
.route{display:flex;align-items:center;gap:22px;padding:20px 0}
.route .ico{width:60px;height:60px;flex:none;border:2px solid var(--c);
  display:flex;align-items:center;justify-content:center;
  font-family:Oswald,sans-serif;font-weight:700;font-size:27px;color:var(--c)}
.route .txt{flex:1}
.route .h{font-family:Oswald,sans-serif;font-weight:600;font-size:28px;color:#fff;
  text-transform:uppercase;line-height:1.1}
.route .b{font-size:21px;color:#a8a8b4;margin-top:7px;line-height:1.42}
.mono{font-family:'JetBrains Mono',monospace;font-size:19px;color:#ffc23d;font-weight:700}

/* ---------- footer ---------- */
footer{margin-top:34px;padding-top:22px;border-top:2px solid rgba(255,255,255,.13);
  display:flex;justify-content:space-between;align-items:flex-end;gap:30px}
footer .site{font-family:Oswald,sans-serif;font-weight:700;font-size:27px;color:#fff;
  letter-spacing:.02em;text-transform:uppercase}
footer .hs{font-family:'Barlow Condensed',sans-serif;font-weight:700;font-size:21px;
  letter-spacing:.13em;color:#FF1493;margin-top:5px}
footer .legal{font-size:14px;line-height:1.45;color:#6e6e79;max-width:520px;text-align:right}
"""

HEAD = """<meta charset="utf-8"><style>%s</style>""" % CSS

LEGAL = ("Independent fan tribute event. Not affiliated with, endorsed by, or sponsored by "
         "Rockstar Games, Take-Two Interactive, or any related entity.")


def page(num, title_html, body, total=6):
    return f"""<!doctype html><html><head>{HEAD}</head><body>
<div class="canvas"><div class="inner">
  <header class="head">
    <img class="logo" src="data:image/png;base64,{LOGO}">
    <div class="head-txt">
      <div class="kicker">Frequently Asked &middot; The Dossier</div>
      <h1>{title_html}</h1>
    </div>
    <div class="filetag"><div class="n">{num:02d}</div><div class="of">OF {total:02d}</div></div>
  </header>
  <main>{body}</main>
  <footer>
    <div><div class="site">grandtheftafterdark.com</div>
         <div class="hs">#GRANDTHEFTAFTERDARK</div></div>
    <div class="legal">{LEGAL}</div>
  </footer>
</div></div></body></html>"""


# ============================== 01 — THE BASICS ==============================
b1 = """
<div class="card">
  <div class="lab p">What is Grand Theft After-Dark?</div>
  <p style="font-size:33px;color:#fff;line-height:1.32;margin-top:14px">
    A cinematic immersive nightlife event series &mdash;
    <b style="color:#FF1493">a night out crossed with a heist film.</b></p>
  <p style="margin-top:14px">A cinematic video story, a live game app in your hand, neon lighting,
    and custom DJ sets across four decades of crime-fiction soundtracks.</p>
</div>

<div class="grid2">
  <div class="card cy">
    <div class="lab">Do I need to play the games?</div>
    <div class="stat cy" style="margin-top:12px">NO</div>
    <p class="sub">Not at all. If you love nightlife and music, you'll have an incredible night.
      Fans of the genre catch deeper layers &mdash; but the production speaks for itself.</p>
  </div>
  <div class="card">
    <div class="lab p">An official game event?</div>
    <div class="stat" style="margin-top:12px">NO</div>
    <p class="sub">We're an independent fan tribute event &mdash; just fans of the genre throwing
      the kind of party we always wanted.</p>
  </div>
</div>

<div class="card" style="padding-bottom:34px">
  <div class="lab g">How long is the night? &mdash; ~3 hours of programming</div>
  <div class="tl">
    <div class="node"><div class="dot"></div><div class="t">8:00</div><div class="d">Doors Open</div></div>
    <div class="node"><div class="dot"></div><div class="t">8:30</div><div class="d">Crew Assembles</div></div>
    <div class="node"><div class="dot"></div><div class="t">10:00</div><div class="d">The Score Goes Down</div></div>
    <div class="node"><div class="dot"></div><div class="t">11&ndash;12</div><div class="d">Wrap</div></div>
  </div>
  <div style="margin-top:26px;padding:15px 20px;border:1px solid rgba(255,194,61,.42);
              background:rgba(255,194,61,.09);display:flex;align-items:center;gap:16px">
    <div class="lab g" style="flex:none;font-size:20px">Heads Up</div>
    <p class="sub" style="margin:0;font-size:20px;color:#d8d8e0">
      <b style="color:#ffc23d">Start times are subject to change based on location.</b>
      Always check the Tour Dates page for your city before you head out.</p>
  </div>
  <p class="sub" style="margin-top:16px;text-align:center">
    About three hours of programming &mdash; but the energy holds longer. Close times vary by venue.</p>
</div>
"""

# ========================= 02 — TICKETS & ENTRY =========================
b2 = """
<div class="grid2">
  <div class="card" style="text-align:center;padding:26px 24px;display:flex;
       flex-direction:column;justify-content:center">
    <div class="lab p">Age Requirement</div>
    <div class="sub" style="letter-spacing:.22em;font-size:17px;margin:10px 0 0">TYPICALLY</div>
    <div class="stat" style="font-size:112px;margin:0 0 4px">21+</div>
    <p style="font-size:23px;color:#fff;font-weight:600;line-height:1.34">
      Set by the venue &mdash; it varies by city.</p>
    <p class="sub" style="margin-top:9px">Check your city's listing on the
      <b style="color:#fff">Tour Dates</b> page before you buy.</p>
    <div style="margin-top:18px;padding-top:16px;border-top:1px solid rgba(255,255,255,.15)">
      <p style="font-size:22px;color:#fff;font-weight:600">Bring valid ID either way.</p>
      <p class="sub" style="color:#FF1493;font-weight:600;letter-spacing:.05em;margin-top:4px">
        NO EXCEPTIONS.</p>
    </div>
  </div>
  <div class="card cy">
    <div class="lab">How much are tickets?</div>
    <p style="margin-top:14px"><b>Tier pricing per city.</b></p>
    <div style="margin-top:16px;display:flex;flex-direction:column;gap:11px">
      <div style="display:flex;gap:14px;align-items:center">
        <div style="width:8px;height:34px;background:#00E5E5;flex:none"></div>
        <div><div style="color:#fff;font-size:22px;font-weight:600">The Crew list</div>
             <div style="color:#8a8a94;font-size:18px">Early-bird access, lowest prices</div></div>
      </div>
      <div style="display:flex;gap:14px;align-items:center">
        <div style="width:8px;height:34px;background:#FF1493;flex:none"></div>
        <div><div style="color:#fff;font-size:22px;font-weight:600">General admission</div>
             <div style="color:#8a8a94;font-size:18px">Opens after</div></div>
      </div>
    </div>
    <p class="sub" style="margin-top:16px">Join the Crew list on the homepage, then watch the
      Tour Dates page for drops.</p>
  </div>
</div>

<div class="card">
  <div class="lab g">What's the dress code? &mdash; "Look like you belong."</div>
  <div class="grid2" style="margin-top:18px;gap:26px">
    <div>
      <div class="chip cy" style="margin-bottom:13px">&#10003;&nbsp; YES</div>
      <p style="font-size:23px">Modern, sharp, cinematic. The wardrobe of a
        <b>heist-movie character.</b></p>
    </div>
    <div style="border-left:1px solid rgba(255,255,255,.14);padding-left:26px">
      <div class="chip p" style="margin-bottom:13px">&#10007;&nbsp; NO</div>
      <p style="font-size:23px">Halloween costume. And if you're trying too hard,
        <b>you're trying too hard.</b></p>
    </div>
  </div>
</div>

<div class="grid2">
  <div class="card">
    <div class="lab p">Refunds</div>
    <p style="margin-top:12px;font-size:23px"><b>All sales final</b> &mdash; unless we cancel or
      reschedule. If we cancel, your full refund is automatic.</p>
  </div>
  <div class="card cy">
    <div class="lab">If it sells out</div>
    <p style="margin-top:12px;font-size:23px">Yes, there's a waiting list. Join the
      <b>Crew list</b> on the homepage &mdash; first to hear if capacity opens.</p>
  </div>
</div>
"""

# ========================== 03 — THE EXPERIENCE ==========================
b3 = """
<div class="lab p">What happens at the event? &mdash; Three things, every night.</div>
<div class="grid3">
  <div class="act"><div class="n">01</div><div class="t">The<br>Video</div>
    <div class="s">The story runs on screen &mdash; the crew, the plan, the score.</div></div>
  <div class="act a2"><div class="n">02</div><div class="t">The<br>Game App</div>
    <div class="s">One QR at the door, no download. Your phone plays all night.</div></div>
  <div class="act a3"><div class="n">03</div><div class="t">The<br>Music</div>
    <div class="s">Custom DJ sets across four decades of crime-fiction soundtracks.</div></div>
</div>

<div class="card cy">
  <div class="lab">Inside the game app &mdash; scan once, play all night</div>
  <div class="grid3" style="margin-top:16px">
    <div class="feat" style="--c:#FF1493"><div class="k">01</div><div class="h">Get Made</div>
      <div class="b">Scan at the door, drop in an email, pick a
        <b style="color:#fff">player nickname</b> &mdash; you're in the crew.</div></div>
    <div class="feat" style="--c:#ffc23d"><div class="k">02</div><div class="h">Wanted Level</div>
      <div class="b">The room's heat, live on your screen &mdash; from
        <b style="color:#fff">On The Radar</b> up to <b style="color:#fff">Most Wanted</b>.</div></div>
    <div class="feat" style="--c:#00E5E5"><div class="k">03</div><div class="h">Missions &amp;<br>Mini Games</div>
      <div class="b">The Handler drops a mission and the whole room plays it
        <b style="color:#fff">from their phones</b>, at the same time.</div></div>
  </div>
  <div class="grid2" style="margin-top:20px">
    <div class="feat" style="--c:#ff7ac0"><div class="k">04</div><div class="h">Points &amp; Leaderboard</div>
      <div class="b">Every mission you play scores you points. The live board goes up on the big
        screen between rounds.</div></div>
    <div class="feat" style="--c:#00E5E5"><div class="k">05</div><div class="h">The Photo Booth</div>
      <div class="b">A branded camera built into the app. Shoot, save, share &mdash; and add it to
        the GTAD gallery if you want it up.</div></div>
  </div>
</div>

<div class="card">
  <div class="lab g">Can I play before the night? &mdash; The Arcade</div>
  <p style="font-size:29px;color:#fff;line-height:1.3;margin-top:12px">
    Play anytime. <b style="color:#FF1493">The score that counts is earned in the room.</b></p>
  <div class="grid2" style="margin-top:18px;gap:0">
    <div style="padding-right:28px">
      <div class="chip cy" style="margin-bottom:12px">THE ARCADE &mdash; ANYTIME</div>
      <p style="font-size:22px;line-height:1.42">Take a run at the
        <b>global rankings</b> from anywhere, on your own time.</p>
      <div class="mono" style="margin-top:11px;font-size:17px;color:#00E5E5">
        grandtheftafterdark.com/arcade</div>
    </div>
    <div style="padding-left:28px;border-left:1px solid rgba(255,255,255,.16)">
      <div class="chip p" style="margin-bottom:12px">AFTER-DARK &mdash; ONE NIGHT</div>
      <p style="font-size:22px;line-height:1.42">The score you put up
        <b>in the world of After-Dark</b> is the one that means something &mdash; live, on the
        floor, with the room watching.</p>
    </div>
  </div>
</div>

<div class="card">
  <div class="lab g">Everything else is a bonus</div>
  <p style="font-size:29px;color:#fff;line-height:1.32;margin-top:12px">
    Video, app, music &mdash; that's the night we promise.
    <b style="color:#ffc23d">Anything on top of it is a surprise.</b></p>
  <p class="sub" style="margin-top:14px;font-size:22px">Some nights bring extras &mdash; interactive
    moments, special guests, things we won't spoil here. None of it is announced in advance and none
    of it is guaranteed. <b style="color:#fff">Show up and find out.</b></p>
</div>

<div class="grid2 top">
  <div class="card cy">
    <div class="lab">Do I have to participate?</div>
    <div class="stat cy" style="font-size:56px;margin-top:12px">OPTIONAL</div>
    <p class="sub">Play the app as hard or as little as you like. If a bonus moment calls for
      volunteers, get up front. <b style="color:#fff">Otherwise the dance floor is the main
      event.</b></p>
  </div>
  <div class="card">
    <div class="lab p">Know before you go</div>
    <div style="margin-top:14px;display:flex;flex-direction:column;gap:13px">
      <div><span class="chip cy">BRING YOUR PHONE</span>
        <div class="sub" style="margin-top:7px">The app runs in your browser &mdash; nothing to
          download. Come charged; a battery pack isn't a bad call.</div></div>
      <div><span class="chip p">IT'S LOUD</span>
        <div class="sub" style="margin-top:7px">It's a club night. Bring earplugs if you're
          sensitive &mdash; most pros do.</div></div>
      <div><span class="chip g">PHOTOS: YES</span>
        <div class="sub" style="margin-top:7px">Tag <b style="color:#fff">@grandtheftafterdark</b>.
          Some reveals are "phones down, eyes up" &mdash; we'll tell you.</div></div>
    </div>
  </div>
</div>
"""

# =========================== 04 — THE CREW CARD ===========================
b4 = """
<div class="card">
  <div class="lab p">What's the Crew Card?</div>
  <p style="font-size:31px;color:#fff;line-height:1.32;margin-top:12px">
    Your identity inside the game app &mdash;
    <b style="color:#FF1493">and your seat in the crew.</b></p>
  <p style="margin-top:12px">One scan at the door and the card is yours for the night. It's how the
    Handler knows you're in the room, and how the room plays back.</p>
</div>

<div class="card cy">
  <div class="lab">Getting in &mdash; three steps, about ten seconds</div>
  <div class="grid3" style="margin-top:16px">
    <div class="feat" style="--c:#00E5E5"><div class="k">STEP 01</div><div class="h">Scan</div>
      <div class="b">One QR at the door. It opens in your browser &mdash; nothing to
        download.</div></div>
    <div class="feat" style="--c:#ffc23d"><div class="k">STEP 02</div><div class="h">Email &amp;<br>Nickname</div>
      <div class="b">Drop in your email and pick a <b style="color:#fff">player nickname</b> &mdash;
        the name you'll play under all night.</div></div>
    <div class="feat" style="--c:#FF1493"><div class="k">STEP 03</div><div class="h">You're Made</div>
      <div class="b">You're in the crew, the card goes live, and you're on the board.</div></div>
  </div>
</div>

<div class="card">
  <div class="lab g">What's on your card, live, all night</div>
  <div class="chips" style="margin-top:16px">
    <div class="chip g">Your Player Nickname</div>
    <div class="chip">Tonight's Job</div>
    <div class="chip">The Handler's Transmission</div>
    <div class="chip cy">Live Wanted Level</div>
    <div class="chip cy">Tonight's Missions &amp; Mini Games</div>
    <div class="chip p">Your Points &amp; Rank</div>
    <div class="chip">Into The Photo Booth</div>
  </div>
  <p class="sub" style="margin-top:18px">The Handler drives the room from the console &mdash; change
    the chapter or the wanted level and <b style="color:#fff">every card in the venue updates within
    seconds.</b> You don't refresh anything.</p>
</div>

<div class="grid2 top">
  <div class="card">
    <div class="lab p">What do I need to play?</div>
    <div class="stat" style="font-size:46px;margin:10px 0 4px;line-height:1.05">AN EMAIL<br>&amp; A NAME</div>
    <p class="sub">That's the whole signup. <b style="color:#fff">No app to download,
      nothing to carry.</b></p>
  </div>
  <div class="card cy">
    <div class="lab">Ranks, patches &amp; rewards?</div>
    <div class="stat cy" style="font-size:50px;margin:10px 0 4px">IN THE WORKS</div>
    <p class="sub">The loyalty programme &mdash; what you earn for putting in nights &mdash; isn't
      locked yet. <b style="color:#fff">We'll announce it when it is.</b> Points and rank already
      run inside the app tonight.</p>
  </div>
</div>
"""

# The five-rank loyalty ladder (Associate -> Boss) lived here. Removed: the programme
# is not locked. Card 04 now covers only the shipped in-app Crew Card mechanic.

b5 = """
<div class="card">
  <div class="lab p">Where is the next event?</div>
  <p style="font-size:31px;color:#fff;line-height:1.32;margin-top:12px">
    Check the <b style="color:#FF1493">Tour Dates</b> page.</p>
  <div style="display:flex;align-items:center;gap:20px;margin-top:20px;flex-wrap:wrap">
    <div class="chip cy">1 &nbsp;&mdash;&nbsp; EMAIL LIST FIRST</div>
    <div style="color:#8a8a94;font-size:26px">&rarr;</div>
    <div class="chip">2 &nbsp;&mdash;&nbsp; SOCIAL SECOND</div>
  </div>
  <p class="sub" style="margin-top:16px">Updates always hit the list before they hit the feed.</p>
</div>

<div class="card cy">
  <div class="lab">Are you coming to my city?</div>
  <p style="margin-top:12px;font-size:26px">Drop your email on the
    <b>"Not In A City We're Hitting?"</b> form.</p>
  <p class="sub" style="margin-top:12px;font-size:22px">We use those signups to decide where we
    expand. <b style="color:#fff">If your city has demand, we'll find a way.</b></p>
</div>

<div class="card">
  <div class="lab g">Bring the show to you</div>
  <div style="margin-top:6px">
    <div class="route" style="--c:#FF1493">
      <div class="ico">V</div>
      <div class="txt"><div class="h">Can my venue host an event?</div>
        <div class="b">Yes &mdash; we're actively booking. Email with the subject line:
          <div class="mono" style="margin-top:6px">VENUE INQUIRY: [Your City]</div></div></div>
    </div>
    <div class="hair"></div>
    <div class="route" style="--c:#00E5E5">
      <div class="ico">P</div>
      <div class="txt"><div class="h">Can I host a private event?</div>
        <div class="b">Yes. Corporate events, private parties, festivals &mdash; we build custom
          versions of the concept.</div></div>
    </div>
  </div>
  <div style="margin-top:20px;padding-top:18px;border-top:1px solid rgba(255,255,255,.12);
              display:flex;align-items:center;gap:16px">
    <div class="lab g" style="font-size:20px">BOTH GO TO</div>
    <div class="mono" style="font-size:27px;color:#fff">tj@harriseventgroup.com</div>
  </div>
</div>
"""

# ============================ 06 — THE HANDLER ============================
b6 = """
<div class="card" style="text-align:center;padding:38px 32px">
  <div class="lab p">Who is the Handler?</div>
  <p style="font-family:Oswald,sans-serif;font-weight:600;font-size:52px;color:#fff;
            line-height:1.14;text-transform:uppercase;margin-top:16px">
    The voice on the phone.<br>
    <span style="color:#FF1493">The one who put this together.</span></p>
  <p class="sub" style="font-size:24px;margin-top:16px">
    He doesn't show his face. He doesn't take meetings. He just runs the crew.</p>
</div>

<div class="grid2">
  <div class="card cy">
    <div class="lab">Is he a real person?</div>
    <p style="margin-top:12px;font-size:23px">He's the spirit of every shadowy mastermind from every
      crime film and crime novel ever written.</p>
    <p class="sub" style="margin-top:10px">He's also voiced and embodied in real life by someone
      &mdash; <b style="color:#fff">but that's not the question.</b></p>
  </div>
  <div class="card">
    <div class="lab p">Why call his number?</div>
    <p style="font-family:Oswald,sans-serif;font-weight:600;font-size:34px;color:#fff;
              line-height:1.14;text-transform:uppercase;margin-top:12px">
      He doesn't pick&nbsp;up.</p>
    <p class="sub" style="margin-top:10px">But the voicemail is worth your time. New message every
      few weeks &mdash; it's how we stay in touch.</p>
  </div>
</div>

<div class="card">
  <div class="lab g">Will the SMS spam me?</div>
  <div style="display:flex;align-items:center;gap:34px;margin-top:16px">
    <div style="text-align:center;flex:none">
      <div class="stat g" style="font-size:92px">2&ndash;4</div>
      <div class="sub" style="margin-top:2px;letter-spacing:.14em;font-size:17px">MSGS / MONTH MAX</div>
    </div>
    <div style="width:1px;align-self:stretch;background:rgba(255,255,255,.14)"></div>
    <div style="flex:1">
      <p style="font-size:26px;color:#fff;font-weight:600">The Handler doesn't have time for spam.</p>
      <div class="chips" style="margin-top:14px">
        <div class="chip cy">Event Drops</div>
        <div class="chip cy">Voicemail Alerts</div>
        <div class="chip cy">Cryptic Intel</div>
      </div>
      <p class="sub" style="margin-top:14px">Reply <b style="color:#fff">STOP</b> anytime.</p>
    </div>
  </div>
</div>
"""

# ====================== 07 — GUESTS & PARTNERSHIPS ======================
b7 = """
<div class="card">
  <div class="lab p">Will there be guest DJs &amp; artists?</div>
  <p style="font-size:29px;color:#fff;line-height:1.32;margin-top:12px">
    Selected events feature special guests &mdash;
    <b style="color:#FF1493">and we don't always announce in advance.</b></p>
  <p class="sub" style="margin-top:12px;font-size:22px">The surprise is part of the night.
    Follow <b style="color:#fff">@grandtheftafterdark</b> for drops.</p>
</div>

<div class="card cy">
  <div class="lab">Get in touch &mdash; use the subject line, it routes you faster</div>
  <div style="margin-top:8px">
    <div class="route" style="--c:#FF1493">
      <div class="ico">1</div>
      <div class="txt"><div class="h">Can I DJ at one of your events?</div>
        <div class="b">Send a mix and your booking info. We curate carefully.<br>
          Subject: <span class="mono">TALENT INQUIRY</span></div></div>
    </div>
    <div class="hair"></div>
    <div class="route" style="--c:#ffc23d">
      <div class="ico">2</div>
      <div class="txt"><div class="h">Are you looking for sponsors?</div>
        <div class="b">Yes &mdash; brands aligned with the aesthetic: premium spirits, automotive,
          streetwear, gaming-adjacent.</div></div>
    </div>
    <div class="hair"></div>
    <div class="route" style="--c:#00E5E5">
      <div class="ico">3</div>
      <div class="txt"><div class="h">Can I work an event?</div>
        <div class="b">Door, photographer, mission staff &mdash; crew positions are city-by-city.
          Tell us your city and what you do.</div></div>
    </div>
  </div>
</div>

<div class="card" style="text-align:center;padding:28px">
  <div class="lab g">All inquiries</div>
  <div class="mono" style="font-size:38px;color:#fff;margin-top:10px">tj@harriseventgroup.com</div>
</div>
"""

# NOTE: card 04 covers only the shipped in-app Crew Card mechanic (scan -> get made ->
# member number, live card contents). The five-rank loyalty ladder is deliberately NOT
# here — that programme is unresolved and must not be published as fact.
PAGES = [
    ("basics",              "The <em>Basics</em>",             b1),
    ("tickets-entry",       "Tickets &amp; <em>Entry</em>",    b2),
    ("experience",          "The <em>Experience</em>",         b3),
    ("crew-card",           "The <em>Crew Card</em>",          b4),
    ("venues-tour",         "Venues &amp; <em>Tour</em>",      b5),
    ("handler",             "The <em>Handler</em>",            b6),
    ("guests-partnerships", "Guests &amp; <em>Partnerships</em>", b7),
]

for old in OUT.glob("*.html"):
    old.unlink()
total = len(PAGES)
for i, (slug, t, b) in enumerate(PAGES, 1):
    f = OUT / f"gtad-faq-{i:02d}-{slug}.html"
    f.write_text(page(i, t, b, total))
    print("wrote", f.name)
