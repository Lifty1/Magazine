// Text threading: pours each <template data-src="id"> into its .flow[data-flow="id"] frames,
// in document order, splitting paragraphs between frames like linked text boxes.
// Returns a report of overflow (text that didn't fit) and underflow per story.
window.flowAll = function () {
  const report = [];
  const fits = f => f.scrollHeight <= f.clientHeight + 0.5;
  const lineH = el => parseFloat(getComputedStyle(el).lineHeight) || 13;

  function tokenize(html) {
    const re = /(<[^>]+>)|([^<\s]+\s*)|(\s+)/g; const out = []; let m;
    while ((m = re.exec(html))) out.push(m[0]);
    return out;
  }
  function stackAt(tokens, k) {
    const st = [];
    for (let i = 0; i < k; i++) {
      const t = tokens[i];
      if (/^<\//.test(t)) st.pop();
      else if (/^<[a-z]/i.test(t) && !/\/>$/.test(t) && !/^<br/i.test(t)) st.push(t);
    }
    return st;
  }
  function splitAt(tokens, k) {
    const st = stackAt(tokens, k);
    const close = st.slice().reverse().map(t => '</' + t.match(/^<([a-z0-9]+)/i)[1] + '>').join('');
    return [tokens.slice(0, k).join('') + close, st.join('') + tokens.slice(k).join('')];
  }
  const isWord = t => !/^</.test(t) && /\S/.test(t);

  document.querySelectorAll('template[data-src]').forEach(t => {
    const id = t.dataset.src;
    const frames = [...document.querySelectorAll(`.flow[data-flow="${id}"]`)];
    let nodes = [...t.content.children].map(n => n.cloneNode(true));
    let fi = 0;
    while (nodes.length && fi < frames.length) {
      const f = frames[fi];
      const n = nodes.shift();
      f.appendChild(n);
      if (fits(f)) {
        // keep headings with at least two lines of what follows
        if (/^H[2-4]$/.test(n.tagName) && nodes.length) {
          const probe = nodes[0].cloneNode(true);
          f.appendChild(probe);
          const ok = fits(f) || (f.scrollHeight - f.clientHeight) < 0 ;
          let roomy = ok;
          if (!ok && probe.tagName === 'P') {
            // allow if at least two lines of the paragraph fit
            const lh = lineH(probe);
            const avail = f.clientHeight - probe.offsetTop + f.offsetTop * 0;
            roomy = (f.getBoundingClientRect().bottom - probe.getBoundingClientRect().top) >= 2.2 * lh;
          }
          f.removeChild(probe);
          if (!roomy) { f.removeChild(n); nodes.unshift(n); fi++; }
        }
        continue;
      }
      // overflow
      if (n.tagName === 'P' && !n.classList.contains('nosplit')) {
        const html = n.innerHTML; const tokens = tokenize(html);
        let lo = 0, hi = tokens.length, best = 0;
        while (lo <= hi) {
          const mid = (lo + hi) >> 1;
          n.innerHTML = splitAt(tokens, mid)[0];
          if (fits(f)) { best = mid; lo = mid + 1; } else hi = mid - 1;
        }
        // back off to a word boundary
        while (best > 0 && !isWord(tokens[best - 1])) best--;
        const lh = lineH(n);
        n.innerHTML = splitAt(tokens, best)[0];
        const firstLines = Math.round(n.getBoundingClientRect().height / lh);
        let restWords = tokens.slice(best).filter(isWord).length;
        if (best === 0 || firstLines < 2) {
          n.innerHTML = html; f.removeChild(n); nodes.unshift(n); fi++; continue;
        }
        if (restWords > 0 && restWords < 7) {
          // avoid a widow: pull a few more words over
          let moved = 0;
          while (best > 0 && moved < 8) { best--; if (isWord(tokens[best])) moved++; }
        }
        const [a, b] = splitAt(tokens, best);
        n.innerHTML = a; const wasEnd = n.classList.contains('end'); n.classList.remove('end');
        { // justify the column's last line only if it is nearly full
          const mk = document.createElement('span'); n.appendChild(mk);
          const pr = n.getBoundingClientRect(), mr = mk.getBoundingClientRect();
          if (mr.left - pr.left > 0.8 * pr.width) n.classList.add('split');
          n.removeChild(mk);
        }
        const cont = n.cloneNode(false); cont.className = (n.className.replace(/\b(split|first)\b/g, '') + ' cont').trim();
        cont.innerHTML = b; if (wasEnd) cont.classList.add('end');
        nodes.unshift(cont);
        fi++;
        continue;
      }
      // headings, quotes, lists etc. move whole to next frame
      f.removeChild(n); nodes.unshift(n); fi++;
    }
    const left = nodes.map(n => n.textContent).join(' ');
    const last = frames[Math.min(fi, frames.length - 1)];
    let fill = null;
    if (last && last.lastElementChild) {
      fill = (last.lastElementChild.getBoundingClientRect().bottom - last.getBoundingClientRect().top) / last.clientHeight;
    }
    const unused = frames.slice(fi + 1).filter(f => !f.children.length).length;
    report.push({ id, frames: frames.length, overflowChars: left.length, overflowStart: left.slice(0, 80), lastFrame: fi, lastFill: fill, emptyFrames: unused });
  });
  return report;
};
