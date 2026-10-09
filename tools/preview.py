"""Render spread previews (PNG) of build/interior.pdf + cover for visual checking."""
import os, subprocess, sys, glob
from PIL import Image, ImageDraw
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, 'build', 'preview')
dpi = int(sys.argv[2]) if len(sys.argv) > 2 else 40
os.makedirs(out, exist_ok=True)
for f in glob.glob(os.path.join(out, 'p-*.png')): os.remove(f)
subprocess.run(['pdftoppm', '-r', str(dpi), '-png', os.path.join(ROOT, 'build', 'interior.pdf'), os.path.join(out, 'p')], check=True)
files = sorted(glob.glob(os.path.join(out, 'p-*.png')))
pages = [Image.open(f) for f in files]
w, h = pages[0].size
bl = round(0.125 * dpi)
def crop(im): return im.crop((bl, bl, w - bl, h - bl))
tw, th = w - 2 * bl, h - 2 * bl
blank = Image.new('RGB', (tw, th), '#bbb')
spreads = [(None, 0)] + [(i, i + 1) for i in range(1, len(pages), 2)]
for k, (a, b) in enumerate(spreads):
    im = Image.new('RGB', (2 * tw + 2, th), '#444')
    im.paste(blank if a is None else crop(pages[a]), (0, 0))
    if b is not None and b < len(pages): im.paste(crop(pages[b]), (tw + 2, 0))
    else: im.paste(blank, (tw + 2, 0))
    im.save(os.path.join(out, f'spread-{k:02d}.png'))
print(len(spreads), 'spreads')
