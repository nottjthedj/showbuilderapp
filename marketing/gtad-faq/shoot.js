const { chromium } = require('playwright-core');
const fs = require('fs'), path = require('path');
const SP = __dirname, SRC = path.join(SP, 'html'), OUT = path.join(SP, 'png');
fs.mkdirSync(OUT, { recursive: true });

(async () => {
  // Point CHROME_PATH at any Chromium/Chrome build; falls back to playwright-core's own lookup.
  const exe = process.env.CHROME_PATH || '/opt/pw-browsers/chromium';
  const b = await chromium.launch({
    ...(fs.existsSync(exe) ? { executablePath: exe } : {}),
    args: ['--no-sandbox'],
  });
  const ctx = await b.newContext({ viewport: { width: 1080, height: 1000 }, deviceScaleFactor: 2 });
  const p = await ctx.newPage();
  for (const f of fs.readdirSync(SRC).filter(x => x.endsWith('.html')).sort()) {
    await p.goto('file://' + path.join(SRC, f));
    await p.evaluate(() => document.fonts.ready);
    const h = await p.evaluate(() => document.querySelector('.canvas').getBoundingClientRect().height);
    const out = path.join(OUT, f.replace('.html', '.png'));
    await p.locator('.canvas').screenshot({ path: out });
    console.log(f.replace('.html', '.png'), '→ 1080 x', Math.round(h), 'css px |',
      (fs.statSync(out).size / 1024).toFixed(0) + ' KB');
  }
  await b.close();
})();
