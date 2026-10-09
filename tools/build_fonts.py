"""Instantiate static font files from the variable Google Fonts sources.
WeasyPrint is most reliable with static instances, so each weight/optical size
used in the design gets its own file in fonts/static/."""
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
import os, shutil
SRC = os.path.join(os.path.dirname(__file__), '..', 'fonts', 'src')
OUT = os.path.join(os.path.dirname(__file__), '..', 'fonts', 'static')
os.makedirs(OUT, exist_ok=True)

def inst(src, out, family, style, **axes):
    f = TTFont(os.path.join(SRC, src))
    f = instantiateVariableFont(f, axes, inplace=False)
    # rename so each instance is a distinct family in the PDF
    for rec in f['name'].names:
        if rec.nameID in (1, 16): rec.string = family
        if rec.nameID in (2, 17): rec.string = style
        if rec.nameID in (4,): rec.string = f'{family} {style}'
        if rec.nameID in (6,): rec.string = f'{family}-{style}'.replace(' ', '')
    f.save(os.path.join(OUT, out)); print('wrote', out)

FR = 'fraunces_Fraunces[SOFT,WONK,opsz,wght].ttf'
FRI = 'fraunces_Fraunces-Italic[SOFT,WONK,opsz,wght].ttf'
NR = 'newsreader_Newsreader[opsz,wght].ttf'
NRI = 'newsreader_Newsreader-Italic[opsz,wght].ttf'
for w, name in [(300, 'Light'), (400, 'Regular'), (600, 'SemiBold'), (900, 'Black')]:
    inst(FR, f'FrauncesDisplay-{name}.ttf', 'Fraunces Display ' + name, 'Regular', opsz=144, wght=w, SOFT=0, WONK=0)
for w, name in [(300, 'Light'), (400, 'Regular')]:
    inst(FRI, f'FrauncesDisplay-{name}Italic.ttf', 'Fraunces Display ' + name + ' Italic', 'Italic', opsz=144, wght=w, SOFT=0, WONK=1)
for w, name in [(400, 'Regular'), (600, 'SemiBold')]:
    inst(FR, f'FrauncesText-{name}.ttf', 'Fraunces Text ' + name, 'Regular', opsz=24, wght=w, SOFT=50, WONK=0)
inst(FRI, 'FrauncesText-Italic.ttf', 'Fraunces Text Italic', 'Italic', opsz=24, wght=400, SOFT=50, WONK=0)
for w, name in [(400, 'Regular'), (500, 'Medium'), (650, 'SemiBold')]:
    inst(NR, f'Newsreader-{name}.ttf', 'Newsreader Text ' + name, 'Regular', opsz=10, wght=w)
for w, name in [(400, 'Italic'), (600, 'SemiBoldItalic')]:
    inst(NRI, f'Newsreader-{name}.ttf', 'Newsreader Text ' + name, 'Italic', opsz=10, wght=w)
inst(NR, 'NewsreaderDeck-Light.ttf', 'Newsreader Deck Light', 'Regular', opsz=36, wght=300)
inst(NRI, 'NewsreaderDeck-LightItalic.ttf', 'Newsreader Deck Light Italic', 'Italic', opsz=36, wght=300)
for f in os.listdir(SRC):
    if f.startswith('ibmplexmono_') and f.endswith('.ttf'):
        shutil.copy(os.path.join(SRC, f), os.path.join(OUT, f.replace('ibmplexmono_', '')))
