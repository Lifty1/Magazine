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
    await page.pdf({ path: path.join(root, 'build', name + '.pdf'), preferCSSPageSize: true, printBackground: true });
    console.log('wrote', name + '.pdf');
  }
  await browser.close();
})();
