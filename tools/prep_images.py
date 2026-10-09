"""Prepare print copies of source images: convert to sRGB, cap size, save as JPEG.
Source: assets/raw/, output: assets/print/. Re-runnable."""
import os, io, sys
from PIL import Image, ImageCms, ImageOps
Image.MAX_IMAGE_PIXELS = None
ROOT = os.path.join(os.path.dirname(__file__), '..')
RAW, OUT = os.path.join(ROOT, 'assets', 'raw'), os.path.join(ROOT, 'assets', 'print')
SRGB = ImageCms.createProfile('sRGB')
MAXSIDE = 5100  # enough for a 300 ppi double-page spread
for f in sorted(os.listdir(RAW)):
    if not f.lower().endswith(('.jpg', '.jpeg', '.png', '.tif', '.tiff')): continue
    slug = os.path.splitext(f)[0]; dst = os.path.join(OUT, slug + '.jpg')
    if os.path.exists(dst) and os.path.getmtime(dst) > os.path.getmtime(os.path.join(RAW, f)): continue
    im = Image.open(os.path.join(RAW, f)); im = ImageOps.exif_transpose(im)
    icc = im.info.get('icc_profile')
    if icc:
        try:
            im = ImageCms.profileToProfile(im, ImageCms.ImageCmsProfile(io.BytesIO(icc)), SRGB, outputMode='RGB')
        except Exception as e:
            print('icc fail', f, e)
    im = im.convert('RGB')
    if max(im.size) > MAXSIDE: im.thumbnail((MAXSIDE, MAXSIDE), Image.LANCZOS)
    im.save(dst, quality=90, subsampling=0, dpi=(300, 300))
    print(slug, im.size)
