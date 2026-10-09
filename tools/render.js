// Render build/interior.html (and build/cover.html) to PDF with Chromium; thread text first.
const path = require('path');
const { chromium } = require('/opt/node-tools/node_modules/playwright');
(async () => {
  const root = path.resolve(__dirname, '..');
  const which = process.argv.slice(2).length ? process.argv.slice(2) : ['interior', 'cover'];
  const browser = await chromium.launch();
  for (const name of which) {
    const page = await browser.newPage();
    await page.emulateMedia({ media: 'print' });
    await page.goto('file://' + path.join(root, 'build', name + '.html'), { waitUntil: 'load' });
    await page.evaluate(() => document.fonts.ready);
    const report = await page.evaluate(() => window.flowAll ? window.flowAll() : []);
    for (const r of report) console.log(JSON.stringify(r));
    // overflow check on fixed boxes
    const over = await page.evaluate(() => [...document.querySelectorAll('.box')].filter(b => b.scrollHeight > b.clientHeight + 1 && b.clientHeight > 0)
      .map(b => ({ page: b.closest('.page').dataset.n, text: b.textContent.trim().slice(0, 50), over: b.scrollHeight - b.clientHeight })));
    if (over.length) console.log('BOX OVERFLOW', JSON.stringify(over));
    const ppi = await page.evaluate(() => [...document.querySelectorAll('.img img')].map(im => {
      const r = im.parentElement.getBoundingClientRect(); const fit = im.style.objectFit || 'cover';
      const sx = r.width / im.naturalWidth, sy = r.height / im.naturalHeight;
      const scale = fit === 'contain' ? Math.min(sx, sy) : Math.max(sx, sy);   // CSS px per image px
      return { page: im.closest('section').dataset.n || 'cover', src: im.getAttribute('src').split('/').pop(), ppi: Math.round(96 / scale) };
    }));
    require('fs').writeFileSync(path.join(root, 'build', name + '-ppi.json'), JSON.stringify(ppi, null, 1));
    const low = ppi.filter(x => x.ppi < 200);
    if (low.length) console.log('LOW PPI (<200):', JSON.stringify(low));
    await page.pdf({ path: path.join(root, 'build', name + '.pdf'), preferCSSPageSize: true, printBackground: true });
    console.log('wrote', name + '.pdf');
  }
  await browser.close();
})();
