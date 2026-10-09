"""Page-by-page layout of LAZARUS No. 1 (48 interior pages)."""
import os

def build_pages(g):
    Page, img, full, spread, box, flow, cols, folio, cap, template = (g[k] for k in
        'Page img full spread box flow cols folio cap template'.split())
    A, W, HT, B, TOP, BOT, colx, ROOT = g['A'], g['W'], g['HT'], g['B'], g['TOP'], g['BOT'], g['colx'], g['ROOT']

    def have(slug): return os.path.exists(os.path.join(ROOT, 'assets', 'print', slug + '.jpg'))
    def pic(*slugs):
        for s in slugs:
            if have(s): return s
        return slugs[-1]

    pages, T = {}, []
    def P(n, cls=''):
        pages[n] = Page(n, cls); return pages[n]

    def opener(p, key, x, y, w, size=66, sf_w=None, gap=6, light=False, sf_size=None):
        meta = A[key][0]
        out = f'<div class="kicker">{meta.get("kicker","")}</div>'
        out += f'<h1 class="headline" style="font-size:{size}pt;margin-top:4mm">{meta["title"]}</h1>'
        if meta.get('standfirst'):
            fs = f'font-size:{sf_size}pt;line-height:{sf_size*1.3:.1f}pt;' if sf_size else ''
            out += f'<p class="standfirst" style="margin-top:{gap}mm;{fs}{"max-width:%smm" % sf_w if sf_w else ""}">{meta["standfirst"]}</p>'
        p.add(box(x, y, w, 150, out, 'light' if light else ''))

    def pull(p, key, i, x, y, w, h, size=None):
        q = A[key][2][i]
        style = f'font-size:{size}pt;line-height:{size*1.18:.1f}pt' if size else ''
        p.add(box(x, y, w, h, f'<div class="pull" style="{style}">{q}</div>'))

    def datelines(body):
        body = body.replace('<p class="first"><strong>', '<p class="dateline"><strong>')
        return body.replace('<p><strong>', '<p class="dateline"><strong>')

    # ------------------------------------------------------------ 1 contents
    p = P(1)
    p.add(img(-B, -B, 70 + B, HT + 2 * B, 'manapouri_mist', '38% 50%'))
    p.add(box(84, 18, 111, 30, '<div class="kicker">Issue One &nbsp;·&nbsp; Presumed Lost &nbsp;·&nbsp; October 2026</div>'
              '<div class="headline" style="font-size:44pt;margin-top:5mm">Contents</div>'))
    toc = [
        (2, 'Presumed', 'A letter from the editor'),
        (3, 'How to Declare Something Extinct', 'The rules, and why they keep changing'),
        (4, 'The Footprint', 'The takahē, Fiordland, 1948'),
        (10, 'The Most Beautiful Fish', 'The coelacanth, South Africa, 1938'),
        (16, 'The Tree Lobsters of Ball’s Pyramid', 'Lord Howe Island, 2001'),
        (20, 'The Tree in the Canyon', 'The Wollemi pine, 1994'),
        (22, 'The Plates', 'Keulemans’ birds, 1888'),
        (24, 'The Ledger', 'Lost, and found again: a timeline'),
        (26, 'Night Voices of the Isle of Devils', 'The cahow, Bermuda, 1951'),
        (30, 'Hiding at Sea', 'The tāiko and the New Zealand storm petrel'),
        (34, 'Made, Not Found', 'An essay on the moa and de-extinction'),
        (38, 'What the Dog Brought Home', 'The black-footed ferret, Wyoming, 1981'),
        (40, 'The Ones That Haven’t Come Back', 'Huia, kōkako, thylacine, ivory-bill'),
        (44, 'Nearly', 'The kākāpō'),
        (46, 'How Lost Things Are Found Now', 'Field notes'),
        (48, 'The Whistle', 'Coda'),
    ]
    rows = ''.join(f'<div style="display:flex;gap:5mm;padding:1.6mm 0 1.7mm;border-top:0.5pt solid var(--rule)">'
                   f'<div class="mono" style="font-size:8pt;font-weight:600;width:8mm;padding-top:1.1mm;color:var(--rust)">{n:02d}</div>'
                   f'<div><div style="font-family:\'FT SemiBold\';font-size:11.2pt;line-height:13.4pt">{t}</div>'
                   f'<div style="font-family:\'ND\';font-style:italic;font-size:9.4pt;line-height:11.6pt;color:var(--muted)">{d}</div></div></div>'
                   for n, t, d in toc)
    p.add(box(84, 60, 111, 202, rows))
    p.add(cap(84, 265, 111, 12, '<b>Cover</b> Takahē, from W. L. Buller’s <i>A History of the Birds of New Zealand</i>, 2nd ed., 1888; lithograph by J. G. Keulemans. <b>Left</b> Lake Manapōuri, Fiordland.'))
    folio(p, 'Contents')

    # ------------------------------------------------------------ 2 letter
    p = P(2, 'paper big')
    meta, body, _ = A['letter']
    p.add(box(15, 18, 175, 40, f'<div class="kicker">{meta["kicker"]}</div><h1 class="headline" style="font-size:58pt;margin-top:4mm">{meta["title"]}</h1>'))
    cols(p, 'letter', y=62, h=186, n=2)
    p.add(box(105, 254, 85, 16, '<div style="font-family:\'FD Italic\';font-size:15pt">— Claude</div><div class="caption">Editor</div>', extra='text-align:right'))
    T.append(template('letter', body))
    folio(p, 'From the editor')

    # ------------------------------------------------------------ 3 rules
    p = P(3, 'big')
    meta, body, _ = A['rules']
    p.add(box(20, 18, 175, 30, f'<div class="kicker">{meta["kicker"]}</div><h1 class="headline" style="font-size:40pt;margin-top:4mm">{meta["title"]}</h1>'))
    p.add(box(20, 50, 175, 50, '<div style="font-family:\'FD LightItalic\';font-size:25pt;line-height:29pt;color:var(--rust)">“There is no reasonable doubt that the last individual has died.”</div>'
              '<div class="caption" style="margin-top:3mm">The IUCN Red List’s definition of <b>Extinct</b></div>'))
    cols(p, 'rules', y=104, h=BOT - 104, n=2)
    T.append(template('rules', body.replace('<p class="first">', '<p class="first noindent">')))
    folio(p, 'The rules')

    # ------------------------------------------------------------ 4-9 takahe
    meta, body, pulls = A['takahe']
    p = P(4); p.add(full('dusky_sound', '50% 60%'))
    p.add(box(15, 262, 60, 4, '', extra='border-top:0.6pt solid rgba(255,255,255,.6)'))
    p.add(cap(15, 265, 110, 12, '<b>Tamatea / Dusky Sound, Fiordland.</b> Sealers working here caught a takahē around 1849, and ate it. Photograph: Liisa Tervinen.', 'caption light'))
    p = P(5)
    opener(p, 'takahe', 20, 18, 175, size=92, sf_w=140)
    xs, w = colx('right', 3)
    for x in xs: p.add(flow('takahe', x, 132, w, 141))
    folio(p, 'Takahē')
    p = P(6)
    p.add(img(-B, -B, W + B, 140 + B, 'takahe_spragg', '50% 45%'))
    p.add(cap(15, 142, 175, 8, '<b>Takahē,</b> <i>Porphyrio hochstetteri</i>, the largest living rail. Photograph: Bernard Spragg.'))
    cols(p, 'takahe', y=153, h=BOT - 153)
    folio(p, 'Takahē')
    p = P(7)
    xs, w = colx('right', 3)
    p.add(flow('takahe', xs[0], TOP, w, 150)); p.add(flow('takahe', xs[1], TOP, w, 150))
    p.add(img(xs[0], 174, 2 * w + 5, 99, 'takahe_greg', '50% 50%'))
    p.add(cap(xs[0], 168, 2 * w + 5, 5, '<b>Greg, a takahē on Tiritiri Matangi Island,</b> Hauraki Gulf. Photograph: Tim Dawson.'))
    pull(p, 'takahe', 0, xs[2], TOP, w, 80)
    p.add(img(xs[2], 104, w, 41, 'archnz_falla', '50% 50%'))
    p.add(cap(xs[2], 147, w, 24, '<b>Takahe Valley, c. 1949.</b> Robert Falla (right), leader of the Notornis Expedition, examines finds from a moa hunters’ cave. Archives New Zealand.'))
    p.add(flow('takahe', xs[2], 176, w, BOT - 176))
    folio(p, 'Takahē')
    p = P(8); p.add(full('fiord_moody', '30% 50%'))
    p.add(cap(15, 268, 110, 10, '<b>Fiordland:</b> the steep, wet, empty country where the takahē survived. Photograph: Gilberto Olimpio.', 'caption light'))
    p = P(9)
    p.add(img(0, -B, W + B, 140 + B, 'takahe_tewahi', '50% 60%'))
    p.add(cap(20, 142, 175, 8, '<b>Takahē in tussock.</b> Photograph: Harald Selke.'))
    xs, w = colx('right', 3)
    p.add(flow('takahe', xs[0], 153, w, BOT - 153)); p.add(flow('takahe', xs[1], 153, w, BOT - 153))
    fact = ('<div class="factbox" style="height:100%"><h3>Four dead birds</h3>'
            '<div class="row"><span class="y">1849</span><span>Caught by sealers’ dogs, Dusky Sound. Eaten.</span></div>'
            '<div class="row"><span class="y">1851</span><span>Taken by Māori, Secretary Island.</span></div>'
            '<div class="row"><span class="y">1879</span><span>Caught by a rabbiter’s dog, Lake Te Anau. Later destroyed in Dresden.</span></div>'
            '<div class="row"><span class="y">1898</span><span>Caught by a dog called Rough, Lake Te Anau.</span></div>'
            '<div class="row"><span class="y">1948</span><span>Found alive, Murchison Mountains.</span></div>'
            '<div class="row"><span class="y">2024</span><span>About 529 birds.</span></div></div>')
    p.add(box(xs[2], 153, w, BOT - 153, fact))
    folio(p, 'Takahē')
    T.append(template('takahe', body))

    # ------------------------------------------------------------ 10-15 coelacanth
    meta, body, pulls = A['coel']
    for side, n in (('left', 10), ('right', 11)):
        p = P(n, 'black')
        x = -B if side == 'left' else -W - B
        p.add(img(x, 78, 2 * W + 2 * B, 158, 'coel_holotype', '50% 50%', fit='contain'))
    pages[10].add(box(15, 18, 190, 70, f'<div class="kicker">{meta["kicker"]}</div><h1 class="headline" style="font-size:64pt;margin-top:4mm;color:#fff">The Most Beautiful Fish</h1>'))
    pages[10].add(cap(15, 244, 110, 14, '<b>The holotype.</b> The fish Marjorie Courtenay-Latimer saved in 1938, mounted, East London Museum. Photograph: Bernard Dupont.', 'caption light'))
    pages[11].add(box(100, 241, 95, 40, f'<p class="standfirst" style="color:#fff;font-size:12.6pt;line-height:16.4pt">{meta["standfirst"]}</p>'))
    p = P(12)
    cols(p, 'coel')
    folio(p, 'Coelacanth')
    p = P(13)
    xs, w = colx('right', 3)
    p.add(img(xs[1], TOP, 2 * w + 5, 82, pic('courtenay_latimer', 'coel_head'), '50% 40%'))
    p.add(cap(xs[1], 102, 2 * w + 5, 10, '<b>Head of a coelacanth,</b> Smithsonian National Museum of Natural History. Photograph: Tim Evanson.' if not have('courtenay_latimer') else '<b>Marjorie Courtenay-Latimer</b> with the coelacanth, East London, 1938.'))
    p.add(flow('coel', xs[0], TOP, w, BOT - TOP))
    pull(p, 'coel', 0, xs[1], 116, 2 * w + 5, 38, size=19)
    p.add(flow('coel', xs[1], 158, w, BOT - 158)); p.add(flow('coel', xs[2], 158, w, BOT - 158))
    folio(p, 'Coelacanth')
    p = P(14, 'paper')
    stats = [('400,000,000', 'years of coelacanths in the fossil record'),
             ('66,000,000', 'years they were thought to have been extinct'),
             ('14', 'years between the first specimen and the second'),
             ('£100', 'the reward on J. L. B. Smith’s leaflets'),
             ('84', 'coelacanths caught and recorded, 1938–1975'),
             ('2', 'living species, nearly 9,000 km apart'),
             ('~100', 'years a coelacanth may live'),
             ('~55', 'years before it is ready to breed'),
             ('5', 'years of pregnancy, the longest known')]
    grid = ''.join(f'<div style="border-top:0.6pt solid var(--rule);padding:3mm 0 0;height:58mm">'
                   f'<div class="bignum" style="font-size:{30 if len(n) > 6 else 52}pt;color:var(--ink)">{n}</div>'
                   f'<div style="font-family:\'ND\';font-size:11pt;line-height:14pt;margin-top:3mm;max-width:50mm">{d}</div></div>' for n, d in stats)
    p.add(box(15, 18, 175, 30, '<div class="kicker">Coelacanth</div><div class="headline" style="font-size:40pt;margin-top:3mm">By the numbers</div>'))
    p.add(box(15, 56, 175, 220, f'<div style="display:grid;grid-template-columns:1fr 1fr 1fr;column-gap:6mm">{grid}</div>'))
    folio(p, 'Coelacanth')
    p = P(15, 'black'); p.add(full('coel_plougmann', '42% 50%'))
    p.add(cap(20, 262, 110, 14, '<b>A coelacanth in preservative,</b> museum display. Photograph: Lars Plougmann.', 'caption light'))
    T.append(template('coel', body))

    # ------------------------------------------------------------ 16-19 phasmid
    meta, body, pulls = A['phasmid']
    p = P(16, 'paper')
    p.add(box(15, 18, 175, 200, '<div class="kicker">Lord Howe Island · 2001</div>'
              '<div class="bignum" style="font-size:330pt;margin-top:2mm;color:var(--ink)">24</div>'))
    p.add(box(15, 200, 120, 60, '<p class="standfirst" style="font-size:16pt;line-height:20pt">insects. One bush. One rock. The entire wild population of a species, counted by torchlight in February 2001.</p>'))
    folio(p, 'Tree lobsters')
    p = P(17)
    p.add(img(20, 18, 115, 85, 'balls_kav2', '50% 45%'))
    p.add(cap(140, 18, 55, 40, '<b>Ball’s Pyramid</b>, 20 km south-east of Lord Howe Island, with a flesh-footed shearwater. Photograph: Patrick Kavanagh.'))
    opener(p, 'phasmid', 20, 120, 175, size=44, sf_w=165, gap=5, sf_size=13)
    xs, w = colx('right', 3)
    for x in xs: p.add(flow('phasmid', x, 190, w, BOT - 190))
    folio(p, 'Tree lobsters')
    p = P(18)
    xs, w = colx('left', 3)
    p.add(flow('phasmid', xs[0], TOP, w, BOT - TOP)); p.add(flow('phasmid', xs[1], TOP, w, 170))
    pic18 = pic('phasmid_prague', 'phasmid_granite', 'lordhowe_aerial')
    p.add(img(xs[2], -B, W - xs[2] + B, 250 + B, pic18, '50% 50%'))
    p.add(cap(xs[2], 253, w, 20, {'phasmid_prague': '<b>Lord Howe Island stick insect</b>, <i>Dryococelus australis</i>, Prague Zoo. Photograph: Miroslav Bobek / Zoo Praha.',
                                  'phasmid_granite': '<b>Lord Howe Island stick insect</b>, <i>Dryococelus australis</i>. Photograph: Granitethighs.',
                                  'lordhowe_aerial': '<b>Lord Howe Island,</b> where rats arrived in 1918 and the tree lobsters vanished. Photograph: Jocelyn.'}[pic18]))
    pull(p, 'phasmid', 0, xs[1], 192, w, 80, size=17)
    folio(p, 'Tree lobsters')
    p = P(19)
    xs, w = colx('right', 3)
    p.add(flow('phasmid', xs[0], TOP, w, BOT - TOP))
    p.add(img(xs[1], TOP, 2 * w + 5, 170, 'balls_1965', '50% 50%'))
    p.add(cap(xs[1], 190, 2 * w + 5, 10, '<b>Ball’s Pyramid from a boat at its base, 1965</b>, the year it was first climbed. Photograph: John Game.'))
    fb = ('<div class="factbox" style="height:100%"><h3><i style="text-transform:none">Dryococelus australis</i></h3>'
          '<div class="row"><span class="y">Size</span><span>Up to about 20 cm long; wingless</span></div>'
          '<div class="row"><span class="y">Young</span><span>Hatch green and active by day; turn black and nocturnal as they grow</span></div>'
          '<div class="row"><span class="y">Trick</span><span>Females can reproduce without males</span></div></div>')
    p.add(box(xs[1], 204, 2 * w + 5, 69, fb))
    folio(p, 'Tree lobsters')
    T.append(template('phasmid', body))

    # ------------------------------------------------------------ 20-21 wollemi
    meta, body, pulls = A['wollemi']
    p = P(20)
    p.add(full('wollemi_tann', '50% 50%'))
    p.add(cap(15, 268, 120, 10, '<b>Wollemi pine foliage and a young cone.</b> Photograph: John Tann.', 'caption light'))
    p = P(21)
    opener(p, 'wollemi', 20, 18, 175, size=56, sf_w=150, sf_size=13)
    xs, w = colx('right', 3)
    for x in xs: p.add(flow('wollemi', x, 102, w, BOT - 102))
    folio(p, 'Wollemi pine')
    T.append(template('wollemi', body))

    # ------------------------------------------------------------ 22-23 plates gallery
    meta, body, _ = A['plates']
    p = P(22, 'paper')
    p.add(img(15, 14, 175, 222, 'laughingowl_plate_1888', '50% 45%', fit='contain'))
    p.add(box(15, 240, 175, 36, f'<div class="kicker">{meta["kicker"]}</div><div class="headline" style="font-size:40pt;margin-top:2mm">{meta["title"]}</div>'))
    p.add(cap(120, 248, 70, 20, '<b>Morepork and laughing owl,</b> J. G. Keulemans, 1888.'))
    folio(p, 'Gallery')
    p = P(23, 'paper')
    p.add(img(20, 14, 175, 160, 'piopio_plate_1888', '50% 40%', fit='contain'))
    p.add(cap(20, 176, 175, 6, '<b>North and South Island piopio,</b> J. G. Keulemans, 1888.', extra='text-align:center'))
    xs, w = colx('right', 3)
    for x in xs: p.add(flow('plates', x, 188, w, BOT - 188))
    folio(p, 'Gallery')
    T.append(template('plates', body.replace('the morepork, below left,', 'the morepork, opposite,')))

    # ------------------------------------------------------------ 24-25 ledger (centre spread)
    from ledger import ledger_svg
    p = P(24, 'dark'); p.add(box(-B, -B, 2 * W + 2 * B, HT + 2 * B, ledger_svg(W, HT, B)))
    folio(p, 'The ledger', light=True)
    p = P(25, 'dark'); p.add(box(-W - B, -B, 2 * W + 2 * B, HT + 2 * B, ledger_svg(W, HT, B)))
    folio(p, 'The ledger', light=True)

    # ------------------------------------------------------------ 26-29 cahow
    meta, body, pulls = A['cahow']
    p = P(26, 'dark')
    p.add(full('cahow_festive', '30% 50%'))
    p.add(cap(15, 266, 120, 12, '<b>A Bermuda petrel, or cahow, over the Atlantic.</b> Photograph: Festive Coquette.', 'caption light'))
    p = P(27)
    opener(p, 'cahow', 20, 18, 175, size=54, sf_w=160, sf_size=13)
    xs, w = colx('right', 3)
    for x in xs: p.add(flow('cahow', x, 118, w, BOT - 118))
    folio(p, 'Cahow')
    p = P(28)
    xs, w = colx('left', 3)
    p.add(flow('cahow', xs[0], TOP, w, BOT - TOP))
    p.add(img(xs[1], TOP, 2 * w + 5, 120, 'cahow_n88', '50% 45%'))
    p.add(cap(xs[1], 140, 2 * w + 5, 8, '<b>Cahow,</b> <i>Pterodroma cahow</i>, at sea. Photograph: n88n88.'))
    p.add(flow('cahow', xs[1], 152, w, BOT - 152)); p.add(flow('cahow', xs[2], 152, w, BOT - 152))
    folio(p, 'Cahow')
    p = P(29, 'paper')
    from recovery import recovery_svg
    p.add(box(20, 18, 175, 40, '<div class="kicker">The long middle</div><div class="headline" style="font-size:40pt;margin-top:3mm">Counting</div>'
              '<p class="standfirst small" style="margin-top:4mm;max-width:160mm">Finding a species is the start. These are the counts that followed, for three birds in this issue. Dots are published counts; lines simply join them.</p>'))
    p.add(box(20, 72, 175, 200, recovery_svg(175, 200)))
    p.add(cap(20, 270, 175, 8, 'Sources: NZ Department of Conservation (takahē); Kākāpō Recovery (kākāpō); Bermuda Department of Environment and Natural Resources (cahow pairs).'))
    folio(p, 'Counting')
    T.append(template('cahow', body))

    # ------------------------------------------------------------ 30-33 seabirds
    meta, body, pulls = A['sea']
    p = P(30); p.add(spread('left', 'nzsp_side', '50% 50%'))
    p = P(31); p.add(spread('right', 'nzsp_side', '50% 50%'))
    p.add(box(110, 196, 85, 80, f'<div class="kicker" style="color:#fff">{meta["kicker"]}</div><h1 class="headline" style="font-size:54pt;margin-top:3mm;color:#fff">{meta["title"]}</h1>'))
    p.add(cap(20, 268, 80, 12, '<b>New Zealand storm petrels,</b> Hauraki Gulf. Photograph: Duncan (angrysunbird).', 'caption light'))
    p = P(32)
    p.add(box(15, 18, 175, 34, f'<p class="standfirst" style="font-size:14pt;line-height:18.4pt">{meta["standfirst"]}</p>'))
    cols(p, 'sea', y=58, h=142)
    prof = ('<div class="factbox" style="height:100%;display:grid;grid-template-columns:1fr 1fr;column-gap:8mm">'
            '<div><h3>Chatham Island tāiko</h3><div class="row"><span class="y">Name</span><span><i>Pterodroma magentae</i>, the Magenta petrel</span></div>'
            '<div class="row"><span class="y">Size</span><span>About 38 cm long; around 450 g</span></div>'
            '<div class="row"><span class="y">Lost</span><span>1867 to 1978</span></div>'
            '<div class="row"><span class="y">Now</span><span>Fewer than 200 birds; about 20 known breeding burrows</span></div></div>'
            '<div><h3>New Zealand storm petrel</h3><div class="row"><span class="y">Name</span><span><i>Fregetta maoriana</i></span></div>'
            '<div class="row"><span class="y">Size</span><span>Sparrow-sized; feeds by pattering over the sea</span></div>'
            '<div class="row"><span class="y">Lost</span><span>About 1850 to 2003</span></div>'
            '<div class="row"><span class="y">Now</span><span>Breeds on Te Hauturu-o-Toi; first nest site found in 2013</span></div></div></div>')
    p.add(box(15, 206, 175, 67, prof))
    folio(p, 'Seabirds')
    p = P(33)
    p.add(img(0, -B, W + B, 150 + B, 'nzsp_angry', '50% 60%'))
    p.add(cap(20, 152, 175, 8, '<b>“Walking on water”:</b> a New Zealand storm petrel pattering over the Hauraki Gulf. Photograph: Duncan (angrysunbird).'))
    cols(p, 'sea', y=164, h=BOT - 164)
    folio(p, 'Seabirds')
    T.append(template('sea', body))

    # ------------------------------------------------------------ 34-37 moa essay
    meta, body, pulls = A['moa']
    p = P(34, 'paper'); p.add(img(15, 16, 180, 248, 'owen_moa', '50% 50%', fit='contain'))
    p.add(cap(15, 267, 180, 8, extra='text-align:center', text= '<b>Richard Owen and the skeleton of a giant moa,</b> about 1877. Wellcome Collection.'))
    p = P(35)
    opener(p, 'moa', 20, 18, 175, size=74, sf_w=160, sf_size=13.4)
    xs, w = colx('right', 3)
    for x in xs: p.add(flow('moa', x, 150, w, BOT - 150))
    folio(p, 'Essay')
    p = P(36)
    xs, w = colx('left', 3)
    p.add(flow('moa', xs[0], TOP, w, BOT - TOP)); p.add(flow('moa', xs[1], TOP, w, BOT - TOP))
    pull(p, 'moa', 0, xs[2], TOP, w, 80, size=19)
    p.add(flow('moa', xs[2], 104, w, BOT - 104))
    folio(p, 'Essay')
    p = P(37)
    xs, w = colx('right', 3)
    p.add(img(xs[0], TOP, 2 * w + 5, 84, 'archnz_moabones', '50% 50%'))
    p.add(cap(xs[0], 104, 2 * w + 5, 10, '<b>Moa bones at the Notornis Expedition camp, Te Anau, c. 1949.</b> The expedition that went to study the rediscovered takahē also dug in a moa hunters’ cave. Archives New Zealand.'))
    p.add(flow('moa', xs[0], 120, w, BOT - 120)); p.add(flow('moa', xs[1], 120, w, BOT - 120))
    pull(p, 'moa', 1, xs[2], TOP, w, 80, size=19)
    p.add(img(xs[2], 120, w, 80, 'moa_legbone', '40% 50%'))
    p.add(cap(xs[2], 202, w, 30, '<b>Moa leg bone,</b> Dinornithidae. In 1839 Richard Owen was shown a fragment of a bone like this and concluded it came from a giant bird. Photograph: JC Merriman.'))
    folio(p, 'Essay')
    T.append(template('moa', body))

    # ------------------------------------------------------------ 38-39 ferret
    meta, body, pulls = A['ferret']
    p = P(38)
    p.add(img(-B, -B, W + B, 150 + B, 'bff_kits', '50% 50%'))
    p.add(cap(15, 152, 175, 8, '<b>Black-footed ferret kits.</b> Photograph: US Fish and Wildlife Service, Mountain-Prairie Region.'))
    opener(p, 'ferret', 15, 166, 175, size=46, sf_w=170, gap=4, sf_size=12.6)
    tl = [('1979', 'Declared extinct'), ('1981', 'Shep’s find, Meeteetse'), ('1987', 'Last 18 wild ferrets taken into care'),
          ('1991', 'First release, Shirley Basin'), ('2020', 'Elizabeth Ann, a clone of Willa'), ('2024', 'A clone has kits of her own')]
    cells = ''.join(f'<div style="border-top:1.2pt solid var(--rust);padding-top:2mm"><div class="mono" style="font-weight:600;font-size:8pt">{y}</div>'
                    f'<div style="font-family:\'NT\';font-size:8.4pt;line-height:11pt;margin-top:1mm">{t}</div></div>' for y, t in tl)
    p.add(box(15, 236, 175, 34, f'<div style="display:grid;grid-template-columns:repeat(6,1fr);column-gap:3mm">{cells}</div>'))
    folio(p, 'Ferret')
    p = P(39)
    xs, w = colx('right', 3)
    p.add(flow('ferret', xs[0], TOP, w, BOT - TOP)); p.add(flow('ferret', xs[1], TOP, w, BOT - TOP))
    p.add(img(xs[2], TOP, w, 66, 'bff_usgs', '50% 40%'))
    p.add(cap(xs[2], 86, w, 14, '<b>A ferret leaves its carrier at a release site.</b> Photograph: USGS.'))
    p.add(flow('ferret', xs[2], 104, w, BOT - 104))
    folio(p, 'Ferret')
    T.append(template('ferret', body))

    # ------------------------------------------------------------ 40-43 still missing
    meta, body, pulls = A['missing']
    p = P(40, 'paper'); p.add(img(-B, -B, W + B, HT + 2 * B, 'kokako_plate_1888', '50% 40%'))
    p.add(cap(15, 266, 120, 14, '<b>Kōkako, North and South Island,</b> J. G. Keulemans, 1888. The South Island bird, with orange wattles, has not been reliably seen since 2007.', 'caption'))
    p = P(41)
    opener(p, 'missing', 20, 18, 175, size=48, sf_w=150, sf_size=12.6)
    p.add(img(20, 98, 175, 70, 'huia_plate_1888', '50% 62%'))
    p.add(cap(20, 170, 175, 6, '<b>Huia, female (left) and male,</b> J. G. Keulemans, 1888.'))
    cols(p, 'missing', y=180)
    folio(p, 'Still missing')
    p = P(42)
    xs, w = colx('left', 3)
    p.add(flow('missing', xs[0], TOP, w, BOT - TOP)); p.add(flow('missing', xs[1], TOP, w, BOT - TOP))
    p.add(img(xs[2], TOP, w, 70, 'thyl_skull', '30% 50%'))
    p.add(cap(xs[2], 90, w, 16, '<b>Thylacine skull.</b> Photograph: JC Merriman.'))
    p.add(flow('missing', xs[2], 108, w, BOT - 108))
    folio(p, 'Still missing')
    p = P(43, 'paper'); p.add(img(0, -B, W + B, HT + 2 * B, 'ibw_audubon', '50% 35%'))
    p.add(cap(120, 270, 75, 10, '<b>Ivory-billed woodpeckers,</b> John James Audubon, <i>The Birds of America</i>.', extra='text-align:right'))
    T.append(template('missing', datelines(body)))

    # ------------------------------------------------------------ 44-45 kakapo
    meta, body, pulls = A['kakapo']
    p = P(44); p.add(img(-B, -B, W + B, HT + 2 * B, 'kakapo_plate_1888', '50% 45%'))
    p.add(cap(15, 268, 120, 10, '<b>Kākāpō,</b> J. G. Keulemans, 1888.', 'caption'))
    p = P(45)
    opener(p, 'kakapo', 20, 18, 175, size=64, sf_w=150, sf_size=13)
    p.add(img(20, 70, 175, 52, 'kakapo_sirocco', '50% 45%'))
    p.add(cap(20, 124, 175, 6, '<b>Sirocco,</b> the best-known kākāpō. Photograph: NZ Department of Conservation.'))
    xs, w = colx('right', 3)
    for x in xs: p.add(flow('kakapo', x, 133, w, BOT - 133))
    folio(p, 'Kākāpō')
    T.append(template('kakapo', body))

    # ------------------------------------------------------------ 46-47 field notes
    meta, body, pulls = A['field']
    p = P(46, 'paper')
    opener(p, 'field', 15, 18, 175, size=40, sf_w=160, gap=4, sf_size=12.4)
    xs, w = colx('left', 3)
    for x in xs: p.add(flow('field', x, 82, w, BOT - 82))
    folio(p, 'Field notes')
    p = P(47, 'black'); p.add(full('trailcam', '58% 50%'))
    p.add(cap(20, 266, 110, 12, '<b>A camera trap on a tree</b> in Jasper National Park, Canada. Most rediscoveries now begin with a device like this. Photograph: Ali Kazal.', 'caption light'))
    T.append(template('field', datelines(body)))

    # ------------------------------------------------------------ 48 coda
    meta, body, pulls = A['coda']
    p = P(48, 'dark big')
    p.add(box(15, 18, 175, 40, f'<div class="kicker">{meta["kicker"]}</div><h1 class="headline" style="font-size:58pt;margin-top:4mm;color:#fff">{meta["title"]}</h1>'))
    p.add(flow('coda', 15, 66, 120, BOT - 66))
    folio(p, 'Coda', light=True)
    T.append(template('coda', body))

    out = [pages[n] for n in sorted(pages)]
    assert [p.n for p in out] == list(range(1, 49)), [p.n for p in out]
    return out, T
