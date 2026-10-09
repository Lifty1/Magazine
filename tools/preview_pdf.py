"""Make print/LAZARUS-01-preview-spreads.pdf: a small on-screen reading copy, trimmed, in spreads."""
import os, subprocess, glob, tempfile
from PIL import Image
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DPI = 80
tmp = tempfile.mkdtemp()
subprocess.run(['pdftoppm', '-r', str(DPI), '-jpeg', os.path.join(ROOT, 'print', 'LAZARUS-01-interior.pdf'), os.path.join(tmp, 'i')], check=True)
subprocess.run(['pdftoppm', '-r', str(DPI), '-jpeg', os.path.join(ROOT, 'print', 'LAZARUS-01-cover.pdf'), os.path.join(tmp, 'c')], check=True)
bl = round(0.125 * DPI)
def trim(im): return im.crop((bl, bl, im.width - bl, im.height - bl)).convert('RGB')
inner = [trim(Image.open(f)) for f in sorted(glob.glob(os.path.join(tmp, 'i-*.jpg')))]
c1, c2 = [trim(Image.open(f)) for f in sorted(glob.glob(os.path.join(tmp, 'c-*.jpg')))]
pw, ph = inner[0].size
half = lambda im, side: im.crop((0, 0, im.width // 2, im.height)) if side == 0 else im.crop((im.width // 2, 0, im.width, im.height))
front, back = half(c1, 1).resize((pw, ph)), half(c1, 0).resize((pw, ph))
ifc, ibc = half(c2, 0).resize((pw, ph)), half(c2, 1).resize((pw, ph))
seq = [ifc] + inner + [ibc]
spreads = [front]
for i in range(0, len(seq), 2):
    s = Image.new('RGB', (2 * pw, ph), 'white'); s.paste(seq[i], (0, 0)); s.paste(seq[i + 1], (pw, 0)); spreads.append(s)
spreads.append(back)
out = os.path.join(ROOT, 'print', 'LAZARUS-01-preview-spreads.pdf')
spreads[0].save(out, save_all=True, append_images=spreads[1:], resolution=DPI, quality=72)
print(out, len(spreads), 'views', round(os.path.getsize(out) / 1e6, 1), 'MB')
