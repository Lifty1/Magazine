"""Compose LAZARUS No. 1 as two HTML documents (interior + cover) for Chromium to print.

Coordinates are millimetres relative to the trim box (A4: 210 x 297); negative values or
values beyond the trim reach into the 3.175 mm bleed. Body text is poured into linked
frames by tools/thread.js at render time.
"""
import os, re, json, html as H
import markdown, pyphen

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
B = 3.175            # bleed, mm
W, HT = 210.058, 296.926  # trim, mm (8.27 x 11.69 in)
IMG = '../assets/print/'
DIC = pyphen.Pyphen(lang='en_GB', left=2, right=3)

# ---------------------------------------------------------------- text helpers
def hyphenate(html):
    def fix(seg):
        return re.sub(r"(?<![&#\w])([a-zāēīōū]{6,})", lambda m: DIC.inserted(m.group(1), hyphen='­'), seg)
    parts = re.split(r'(<[^>]+>|&[a-z]+;)', html)
    return ''.join(p if (p.startswith('<') or p.startswith('&')) else fix(p) for p in parts)

def load(name):
    raw = open(os.path.join(ROOT, 'content', name), encoding='utf8').read()
    meta = {}
    m = re.match(r'---\n(.*?)\n---\n', raw, re.S)
    if m:
        for line in m.group(1).splitlines():
            k, v = line.split(':', 1); meta[k.strip()] = v.strip()
        raw = raw[m.end():]
    body = markdown.markdown(raw, extensions=['smarty'])
    pulls = re.findall(r'<blockquote>\s*<p>(.*?)</p>\s*</blockquote>', body, re.S)
    body = re.sub(r'<blockquote>.*?</blockquote>', '', body, flags=re.S)
    body = body.replace('<p>', '<p class="first">', 1)
    last = body.rfind('<p')
    seg = body[last:]
    seg = seg.replace('<p class="', '<p class="end ', 1) if seg.startswith('<p class="') else seg.replace('<p', '<p class="end"', 1)
    body = body[:last] + seg
    body = hyphenate(body)
    for k in ('title', 'standfirst', 'kicker'):
        if k in meta: meta[k] = markdown.markdown(meta[k], extensions=['smarty'])[3:-4]
    return meta, body, pulls

# ---------------------------------------------------------------- page model
class Page:
    def __init__(self, n, cls=''):
        self.n, self.cls, self.items = n, cls, []
    @property
    def side(self): return 'right' if self.n % 2 == 1 else 'left'
    def add(self, s): self.items.append(s); return self
    def html(self):
        return f'<section class="page {self.side} {self.cls}" data-n="{self.n}"><div class="trim">{"".join(self.items)}</div></section>'

def st(x, y, w, h, extra=''):
    return f'left:{x:.2f}mm;top:{y:.2f}mm;width:{w:.2f}mm;height:{h:.2f}mm;{extra}'

def img(x, y, w, h, src, pos='50% 50%', extra='', fit='cover', cls=''):
    return f'<div class="img {cls}" style="{st(x,y,w,h,extra)}"><img src="{IMG}{src}.jpg" style="object-position:{pos};object-fit:{fit}"></div>'

def full(src, pos='50% 50%'):
    return img(-B, -B, W + 2 * B, HT + 2 * B, src, pos)

def spread(side, src, pos='50% 50%'):
    x = -B if side == 'left' else -W - B
    return img(x, -B, 2 * W + 2 * B, HT + 2 * B, src, pos)

def box(x, y, w, h, inner, cls='', extra=''):
    return f'<div class="box {cls}" style="{st(x,y,w,h,extra)}">{inner}</div>'

def flow(fid, x, y, w, h):
    return f'<div class="flow" data-flow="{fid}" style="{st(x,y,w,h)}"></div>'

# grid
TOP, BOT = 18.0, 273.0
def colx(side, n=3, gap=5.0):
    x0 = 20.0 if side == 'right' else 15.0
    w = (175.0 - gap * (n - 1)) / n
    return [x0 + i * (w + gap) for i in range(n)], w

def cols(p, fid, y=TOP, h=None, n=3, which=None, ys=None, hs=None):
    xs, w = colx(p.side, n)
    for i, x in enumerate(xs):
        if which is not None and i not in which: continue
        yy = ys[i] if ys and ys.get(i) is not None else y
        hh = hs[i] if hs and hs.get(i) is not None else (h if h is not None else BOT - yy)
        p.add(flow(fid, x, yy, w, hh))
    return p

def folio(p, label, light=False):
    cls = 'folio light' if light else 'folio'
    if p.side == 'left':
        inner = f'<span class="pn">{p.n}</span>&nbsp;&nbsp;&nbsp;Lazarus No.&nbsp;1 &nbsp;·&nbsp; {label}'
        p.add(box(15, 280.5, 120, 4, inner, cls))
    else:
        inner = f'{label} &nbsp;·&nbsp; Lazarus No.&nbsp;1&nbsp;&nbsp;&nbsp;<span class="pn">{p.n}</span>'
        p.add(box(75, 280.5, 120, 4, inner, cls, 'text-align:right'))
    return p

def cap(x, y, w, h, text, cls='caption', extra=''):
    return box(x, y, w, h, text, cls, extra)

def template(fid, body):
    return f'<template data-src="{fid}">{body}</template>'

# ---------------------------------------------------------------- content
A = {k: load(f) for k, f in [
    ('letter', '01-letter.md'), ('rules', '02-rules.md'), ('takahe', '03-takahe.md'),
    ('coel', '04-coelacanth.md'), ('phasmid', '05-phasmid.md'), ('cahow', '06-cahow.md'),
    ('sea', '07-seabirds.md'), ('wollemi', '08-wollemi.md'), ('moa', '09-moa.md'),
    ('missing', '10-missing.md'), ('kakapo', '11-kakapo.md'), ('field', '12-fieldnotes.md'),
    ('coda', '13-coda.md'), ('plates', '14-plates.md'), ('ferret', '15-ferret.md')]}
CREDITS = json.load(open(os.path.join(ROOT, 'assets', 'raw', 'credits.json')))

from pages import build_pages   # noqa: E402  (page layouts live in tools/pages.py)

def main():
    pages, templates = build_pages(globals())
    doc = ['<!doctype html><html lang="en-NZ"><head><meta charset="utf-8"><title>LAZARUS No. 1 — interior</title>',
           '<link rel="stylesheet" href="../src/style.css"><script src="../tools/thread.js"></script></head><body>']
    doc += [p.html() for p in pages]
    doc += templates
    doc.append('</body></html>')
    os.makedirs(os.path.join(ROOT, 'build'), exist_ok=True)
    open(os.path.join(ROOT, 'build', 'interior.html'), 'w', encoding='utf8').write('\n'.join(doc))
    print('pages:', len(pages))

if __name__ == '__main__':
    main()
