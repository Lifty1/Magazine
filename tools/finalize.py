"""Check the rendered PDFs against Lulu's spec, add TrimBox/BleedBox, and copy them to print/.

Lulu magazine, A4 saddle stitch: interior = 48 single pages of 8.52 x 11.94 in (A4 + 0.125 in bleed);
cover = 2 pages (outside, inside) of 16.79 x 11.94 in. Fonts must be embedded."""
import os, subprocess, shutil, sys
from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
PT = 72.0
SPEC = {'interior': (48, 8.52, 11.94), 'cover': (2, 16.79, 11.94)}
OUT = {'interior': 'LAZARUS-01-interior.pdf', 'cover': 'LAZARUS-01-cover.pdf'}
ok = True
os.makedirs(os.path.join(ROOT, 'print'), exist_ok=True)
for name, (n, w, h) in SPEC.items():
    src = os.path.join(ROOT, 'build', name + '.pdf')
    r = PdfReader(src)
    if len(r.pages) != n:
        print(f'FAIL {name}: {len(r.pages)} pages, expected {n}'); ok = False
    wr = PdfWriter()
    for i, p in enumerate(r.pages):
        mb = p.mediabox
        pw, ph = float(mb.width) / PT, float(mb.height) / PT
        if abs(pw - w) > 0.02 or abs(ph - h) > 0.02:
            print(f'FAIL {name} p{i+1}: {pw:.3f} x {ph:.3f} in, expected {w} x {h}'); ok = False
        x0, y0 = float(mb.left), float(mb.bottom)
        # Chromium rounds the page to its pixel grid (up to ~0.5 pt off); set the exact Lulu size.
        p.mediabox = RectangleObject([x0, y0, x0 + w * PT, y0 + h * PT])
        b = 0.125 * PT
        p.trimbox = RectangleObject([x0 + b, y0 + b, x0 + w * PT - b, y0 + h * PT - b])
        p.bleedbox = RectangleObject([x0, y0, x0 + w * PT, y0 + h * PT])
        p.cropbox = RectangleObject([x0, y0, x0 + w * PT, y0 + h * PT])
        wr.add_page(p)
    wr.add_metadata({'/Title': f'LAZARUS No. 1 — {name}', '/Author': 'LAZARUS', '/Subject': 'Issue One: Presumed Lost (October 2026)'})
    dst = os.path.join(ROOT, 'print', OUT[name])
    with open(dst, 'wb') as f: wr.write(f)
    fonts = subprocess.run(['pdffonts', dst], capture_output=True, text=True).stdout.splitlines()[2:]
    bad = [l for l in fonts if l.split()[-5:-4] != ['yes']]   # 'emb' column
    for l in fonts:
        cols = l.split()
        if 'no' in cols[-5:-2]:
            print(f'FAIL {name}: font not embedded: {l}'); ok = False
        if 'DejaVu' in l or 'Liberation' in l:
            print(f'FAIL {name}: fallback font used: {cols[0]}'); ok = False
        if 'Type 3' in l:
            print(f'FAIL {name}: Type 3 font: {cols[0]}'); ok = False
    size = os.path.getsize(dst) / 1e6
    print(f'{name}: {len(r.pages)} pages, {w} x {h} in, {len(fonts)} fonts, {size:.1f} MB -> print/{OUT[name]}')
print('ALL CHECKS PASSED' if ok else 'CHECKS FAILED'); sys.exit(0 if ok else 1)
