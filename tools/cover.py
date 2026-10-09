"""Build build/cover.html: Lulu magazine cover, 2 pages of 16.79 x 11.94 in.
Page 1 (outside): back cover | front cover.  Page 2 (inside): inside front | inside back.
Run after build.py (credits are collected from the rendered interior HTML)."""
import os, re, json
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
B, W, HT = 3.175, 210.058, 296.926
IMG = '../assets/print/'

def st(x, y, w, h, extra=''):
    return f'left:{x:.2f}mm;top:{y:.2f}mm;width:{w:.2f}mm;height:{h:.2f}mm;{extra}'
def img(x, y, w, h, src, pos='50% 50%', fit='cover'):
    return f'<div class="img" style="{st(x,y,w,h)}"><img src="{IMG}{src}.jpg" style="object-position:{pos};object-fit:{fit}"></div>'
def box(x, y, w, h, inner, cls='', extra=''):
    return f'<div class="box {cls}" style="{st(x,y,w,h,extra)}">{inner}</div>'

LIC = {
    'creativecommons.org/licenses/by/2.0': 'CC BY 2.0', 'creativecommons.org/licenses/by-sa/2.0': 'CC BY-SA 2.0',
    'creativecommons.org/licenses/by/4.0': 'CC BY 4.0', 'creativecommons.org/publicdomain/zero/1.0': 'CC0',
}
NAMES = {'Bernard DUPONT': 'Bernard Dupont', 'Bernard Spragg. NZ': 'Bernard Spragg', 'Duncan': 'Duncan (angrysunbird)',
         'patrickkavanagh': 'Patrick Kavanagh', 'Merryjack': 'JC Merriman', 'Free Public Domain Illustrations by rawpixel': 'John James Audubon (via rawpixel)',
         'National Library NZ on The Commons': 'J. G. Keulemans, from W. L. Buller, A History of the Birds of New Zealand (1888); National Library of New Zealand',
         'Department of Conservation': 'NZ Department of Conservation', 'USFWS Mountain-Prairie': 'US Fish and Wildlife Service, Mountain-Prairie Region',
         'U.S. Geological Survey': 'US Geological Survey', 'Festive Coquette': 'Festive Coquette', 'n88n88': 'n88n88'}

def credits_html():
    c = json.load(open(os.path.join(ROOT, 'assets', 'raw', 'credits.json')))
    doc = open(os.path.join(ROOT, 'build', 'interior.html'), encoding='utf8').read()
    use = {}
    for m in re.finditer(r'<section class="page[^"]*" data-n="(\d+)">(.*?)</section>', doc, re.S):
        for s in re.findall(r'assets/print/([a-z0-9_]+)\.jpg', m.group(2)):
            use.setdefault(s, []).append(int(m.group(1)))
    use.setdefault('takahe_plate_1888', []).insert(0, 'Cover')
    use.setdefault('huia_plate_1888', []).insert(0, 'Back cover')
    rows = []
    def key(item):
        p = item[1][0]
        return -1 if p == 'Cover' else (99 if p == 'Back cover' else p)
    for slug, pgs in sorted(use.items(), key=key):
        v = c[slug]
        who = NAMES.get(v.get('artist', ''), v.get('artist', ''))
        lic = LIC.get(v.get('license', ''), v.get('license', ''))
        if v.get('source') == 'Pexels': lic = 'Pexels License'
        pg = ', '.join(str(x) for x in dict.fromkeys(pgs))
        rows.append(f'<div class="cr"><span class="pg">{pg}</span> {who}. <i>{lic}</i></div>')
    return ''.join(rows)

SOURCES = [
    ('Takahē', 'Wikipedia: “Takahē”, “Geoffrey Orbell”. NZ Department of Conservation blog, “Happy hatch-day, takahē” (1 Oct 2025). DOC and news reports on the Greenstone and Rees Valley releases (2023–25).'),
    ('Coelacanth', 'Wikipedia: “Coelacanth”, “Marjorie Courtenay-Latimer”, “J. L. B. Smith”, “Latimeria menadoensis”. Financial Mail, “The coelacanth: apartheid’s fishy tale” (2022). Mahé et al., <i>Current Biology</i> (2021).'),
    ('Tree lobsters', 'Wikipedia: “Dryococelus australis”, “Ball’s Pyramid”. Earth.com (Jan 2025).'),
    ('Wollemi pine', 'Wikipedia: “Wollemia”.'),
    ('Cahow', 'Wikipedia: “Bermuda petrel”, “David B. Wingate”. Nonsuch Expeditions season reports (2023, 2025).'),
    ('Seabirds', 'NZ Birds Online, “Chatham Island tāiko”. Wikipedia: “Magenta petrel”, “New Zealand storm petrel”. ACAP obituary of David Crockett (2023).'),
    ('Moa', 'Wikipedia: “Moa”, “Colossal Biosciences”. AP and Business Wire (8 July 2025). RNZ reports on the artificial egg and <i>Our Changing World</i> (2026).'),
    ('Ferret', 'Wikipedia: “Black-footed ferret”. Smithsonian’s National Zoo, “Black-footed ferrets: top milestones”. Science Friday; Cody Yellowstone.'),
    ('Still missing', 'Wikipedia: “Huia”, “South Island kōkako”, “Thylacine”, “Ivory-billed woodpecker”. US Fish and Wildlife Service notices (2021–23). NZ Geographic and Ngā Taonga on the huia recording. Wilderness magazine on the kōkako reward.'),
    ('Kākāpō', 'Wikipedia: “Kākāpō”.'),
    ('Field notes', 'Wikipedia articles on each species. Re:wild. Good Good Good, on the Search for Lost Birds (Apr 2026).'),
    ('Rules', 'IUCN Red List Categories and Criteria (definition of Extinct).'),
]

def main():
    css = '''<style>@page { size: 16.79in 11.94in; margin: 0; }
    .cpage { width: 16.79in; height: 11.94in; position: relative; overflow: hidden; break-after: page; }
    .ctrim { position: absolute; left: 0.125in; top: 0.125in; width: 16.54in; height: 11.69in; }
    .cr { font-family: 'Mono'; font-size: 5.9pt; line-height: 7.6pt; margin-bottom: 1.1pt; }
    .cr .pg { font-weight: 600; color: var(--rust); }
    .src { font-family: 'NT'; font-size: 7.4pt; line-height: 9.6pt; margin-bottom: 2.4pt; }
    .src b { font-family: 'Mono'; font-weight: 600; font-size: 6.4pt; letter-spacing: .06em; text-transform: uppercase; color: var(--rust); }
    .mast { font-family: 'FD Black'; letter-spacing: -0.01em; line-height: 0.8; }
    </style>'''
    FX = W  # front cover trim origin x (relative to cover trim)
    # ---- outside: back (left) | front (right)
    out = []
    out.append(img(-B, -B, W + B, HT + 2 * B, 'huia_plate_1888', '50% 42%'))
    out.append(box(16, 18, 120, 40, '<div class="kicker" style="color:#17191a">Huia &nbsp;·&nbsp; <i style="text-transform:none;font-family:\'Mono\';font-style:italic">Heteralocha acutirostris</i></div>'
                   '<div style="font-family:\'FD LightItalic\';font-size:24pt;line-height:27pt;margin-top:3mm;color:#17191a">Last confirmed sighting:<br>28 December 1907.</div>'))
    out.append(box(16, 44, 58, 30, '<div style="font-family:\'Mono\';font-size:6.6pt;line-height:9pt;color:#17191a">LAZARUS is a magazine about living things that were lost and found again, and some that were not. Issue One, October 2026. Print run: one.</div>'))
    # front
    out.append(img(FX, -B, W + B, HT + 2 * B, 'takahe_plate_1888', '50% 72%'))
    out.append(box(FX + 14, 13.5, W - 28, 6, '<div style="display:flex;justify-content:space-between" class="kicker"><span style="color:#17191a">No. 1</span><span style="color:#17191a">Presumed Lost</span><span style="color:#17191a">October 2026</span></div>'))
    out.append(box(FX + 12, 17, W - 24, 40, '<div class="mast" style="font-size:86pt;color:#17191a;text-align:center">LAZARUS</div>'))
    out.append(box(FX + 14, 266.5, 60, 20, '<div style="font-family:\'FD LightItalic\';font-size:13pt;line-height:15pt;color:#17191a">The bird that walked back from extinction</div>'
                   '<div class="kicker" style="margin-top:1.5mm;color:#7a2e1b;font-size:6.2pt">Takahē · Fiordland · 1948</div>'))
    out.append(box(FX + 138, 266.5, 58, 20, '<div style="font-family:\'ND\';font-size:8.6pt;line-height:11pt;color:#17191a;text-align:right">The fish from the Cretaceous<br>Twenty-four insects on a rock<br>A bird missing for 300 years<br>Should we make a moa?</div>'))
    page1 = f'<section class="cpage"><div class="ctrim">{"".join(out)}</div></section>'
    # ---- inside: inside front (left) | inside back (right)
    ins = [box(-B, -B, W + B, HT + 2 * B, '', extra='background:var(--deep)')]
    ins.append(box(22, 40, 160, 160, '<div style="color:#ece6da">'
               '<div style="font-family:\'FD Regular\';font-size:30pt;line-height:34pt;color:#fff">Lazarus taxon</div>'
               '<div style="font-family:\'Mono\';font-size:8pt;margin:2mm 0 6mm;color:#9fb3b0">noun &nbsp;·&nbsp; plural <i>Lazarus taxa</i></div>'
               '<div style="font-family:\'ND\';font-size:15pt;line-height:20pt">A species, or other group of living things, that disappears from the fossil or historical record and is presumed extinct, only to be found alive later.</div>'
               '<div style="font-family:\'ND\';font-style:italic;font-size:12pt;line-height:16pt;margin-top:6mm;color:#c9c2b4">After Lazarus of Bethany, who in the Gospel of John has been four days in the tomb when he is called out alive.</div></div>'))
    ins.append(box(22, 222, 160, 60, '<div style="font-family:\'Mono\';font-size:6.6pt;line-height:9.4pt;color:#c9c2b4">'
               '<span style="color:#fff;font-weight:600">LAZARUS No. 1 &nbsp;·&nbsp; Presumed Lost &nbsp;·&nbsp; October 2026</span><br>'
               'Researched, written, edited and designed by Claude, an AI model made by Anthropic, from published sources listed inside the back cover. '
               'Printed on demand by Lulu. Print run: one copy, for a reader in Aotearoa New Zealand.<br>'
               'Set in Fraunces, Newsreader and IBM Plex Mono (SIL Open Font License). Images are public domain or openly licensed; credits inside the back cover.</div>'))
    # inside back: credits + sources
    ins.append(box(FX, -B, W + B, HT + 2 * B, '', extra='background:var(--paper)'))
    ib = box(FX + 15, 16, 85, 270, '<div class="kicker" style="margin-bottom:3mm">Picture credits</div>' + credits_html())
    srcs = ''.join(f'<div class="src"><b>{k}</b> {v}</div>' for k, v in SOURCES)
    ib2 = box(FX + 108, 16, 87, 270, '<div class="kicker" style="margin-bottom:3mm">Sources</div>' + srcs +
              '<div class="src" style="margin-top:3mm;color:var(--muted)">Facts were checked against these sources in October 2026. Where sources disagree, the text says so or leaves the detail out. Errors are the editor’s.</div>')
    ins.append(box(FX + 15, 200, 180, 80, '<div style="border-top:0.6pt solid var(--rule);padding-top:5mm;display:grid;grid-template-columns:1fr 1fr;column-gap:8mm">'
        '<div><div class="kicker">Seen something?</div><div style="font-family:\'FD Light\';font-size:22pt;line-height:25pt;margin-top:2mm">Most rediscoveries start with someone who reported what they saw.</div></div>'
        '<div style="font-family:\'NT\';font-size:8.6pt;line-height:12pt;padding-top:1mm">In Aotearoa New Zealand, report sightings of threatened species to your local Department of Conservation office; for emergencies, such as wildlife being harmed, DOC’s 24-hour line is <b>0800 DOC HOT</b> (0800 362 468). '
        'A photograph, a recording, a feather or a footprint, with the date and the place, is worth far more than a description. Note it, photograph it, and leave it where it is.</div></div>'))
    ins += [ib, ib2]
    page2 = f'<section class="cpage"><div class="ctrim">{"".join(ins)}</div></section>'
    html = ('<!doctype html><html lang="en-NZ"><head><meta charset="utf-8"><title>LAZARUS No. 1 — cover</title>'
            f'<link rel="stylesheet" href="../src/style.css">{css}</head><body>{page1}{page2}</body></html>')
    open(os.path.join(ROOT, 'build', 'cover.html'), 'w', encoding='utf8').write(html)
    print('cover written')

if __name__ == '__main__':
    main()
