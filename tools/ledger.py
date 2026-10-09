"""The Ledger: centre-spread timeline of species lost and found again (SVG, mm units)."""

ROWS = [  # name, place, last seen, found again, note
    ('Bermuda petrel (cahow)', 'Bermuda', 1620, 1951, ''),
    ('Takahē', 'Fiordland, NZ', 1898, 1948, ''),
    ('Magenta petrel (tāiko)', 'Chatham Islands, NZ', 1867, 1978, ''),
    ('Jerdon’s courser', 'Andhra Pradesh, India', 1900, 1986, ''),
    ('Night parrot', 'Queensland, Australia', 1912, 1990, 'found dead'),
    ('Lord Howe Island stick insect', 'Ball’s Pyramid', 1920, 2001, ''),
    ('New Zealand storm petrel', 'Hauraki Gulf, NZ', 1850, 2003, ''),
    ('South Island kōkako', 'Reefton, NZ', 1967, 2007, 'sighting disputed'),
    ('Wallace’s giant bee', 'North Moluccas, Indonesia', 1981, 2019, 'also lost 1858–1981'),
    ('Silver-backed chevrotain', 'Vietnam', 1990, 2019, ''),
    ('Fernandina Island tortoise', 'Galápagos', 1906, 2019, ''),
    ('Attenborough’s echidna', 'Cyclops Mountains, New Guinea', 1961, 2023, ''),
    ('De Winton’s golden mole', 'Northern Cape, South Africa', 1937, 2023, ''),
]
MISSING = [
    ('Huia', 'North Island, NZ', 1907),
    ('Thylacine', 'Tasmania', 1936),
    ('Ivory-billed woodpecker', 'Louisiana, USA', 1944),
]
DEEP = [
    ('66,000,000', 'Coelacanth', 'Absent from the fossil record since the Cretaceous. Caught off South Africa, 1938.'),
    ('11,000,000', 'Laotian rock rat', 'Its family was known only from fossils. Found in a Laotian market and described in 2005.'),
    ('70', 'Mountain pygmy possum', 'Described from fossil bones in 1896. Found alive at a ski resort on Mount Hotham, 1966.'),
    ('45', 'Chacoan peccary', 'Described from fossils in 1930. Recognised alive in the Paraguayan Chaco in the 1970s.'),
]

def ledger_svg(W, HT, B):
    SW, SH = 2 * W + 2 * B, HT + 2 * B
    o = B  # trim origin inside svg
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{SW}mm" height="{SH}mm" viewBox="0 0 {SW} {SH}">']
    s.append(f'<rect x="0" y="0" width="{SW}" height="{SH}" fill="#0f2427"/>')
    def t(x, y, txt, size, fam, fill='#ece6da', anchor='start', extra=''):
        s.append(f'<text x="{x:.2f}" y="{y:.2f}" font-family="{fam}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" {extra}>{txt}</text>')
    pt = 0.3528  # mm per point
    # title block (left page)
    t(o + 15, o + 22, 'THE LEDGER', 7.4 * pt, 'Mono', '#e2a383', extra='letter-spacing="0.9" font-weight="500"')
    t(o + 15, o + 46, 'Lost, and found again', 50 * pt, 'FD Light', '#ffffff')
    for i, line in enumerate(['Each line runs from the last record of a species to the day',
                              'someone found it again. Hollow circle: last seen. Solid: found.',
                              'Dashed lines at the bottom are still running.']):
        t(o + 15, o + 58 + i * 5.6, line, 11.5 * pt, 'ND', '#d9d2c4')
    # deep time block (right page)
    x0 = o + W + 22; y0 = o + 18
    t(x0, y0 + 4, 'DEEP TIME', 7.4 * pt, 'Mono', '#e2a383', extra='letter-spacing="0.9" font-weight="500"')
    t(x0 + 60, y0 + 4, 'YEARS MISSING FROM THE RECORD', 6.4 * pt, 'Mono', '#9fb3b0', extra='letter-spacing="0.6"')
    for i, (num, name, note) in enumerate(DEEP):
        y = y0 + 15 + i * 13.5
        s.append(f'<line x1="{x0}" y1="{y-8}" x2="{x0+165}" y2="{y-8}" stroke="#34504f" stroke-width="0.25"/>')
        t(x0, y, num, 19 * pt, 'FD Light', '#ffffff')
        t(x0 + 60, y - 3.2, name, 9 * pt, 'FT SemiBold', '#ffffff')
        t(x0 + 60, y + 1.2, note, 7.6 * pt, 'ND', '#c9c2b4')
    # chart
    L, R = o + 78, o + 2 * W - 18
    Y0, Y1 = 1600, 2030
    X = lambda yr: L + (yr - Y0) * (R - L) / (Y1 - Y0)
    top = o + 98
    rows = len(ROWS) + len(MISSING) + 1
    rh = (o + 266 - top) / rows
    for yr in range(1600, 2031, 50):
        x = X(yr); major = yr % 100 == 0
        s.append(f'<line x1="{x:.2f}" y1="{top-6}" x2="{x:.2f}" y2="{o+268}" stroke="{"#3d5a59" if major else "#24403f"}" stroke-width="{0.3 if major else 0.2}"/>')
        if major or yr == 2030:
            t(x, top - 8, str(yr), 6.6 * pt, 'Mono', '#9fb3b0', 'middle')
            t(x, o + 272.5, str(yr), 6.6 * pt, 'Mono', '#9fb3b0', 'middle')
    gutter = o + W
    def label(y, name, place, fill='#ffffff'):
        t(o + 15, y - 0.4, name, 8.4 * pt, 'FT SemiBold', fill)
        t(o + 15, y + 3.0, place.upper(), 5.6 * pt, 'Mono', '#9fb3b0', extra='letter-spacing="0.3"')
    for i, (name, place, a, b, note) in enumerate(ROWS):
        y = top + (i + 0.5) * rh
        label(y, name, place)
        dash = ' stroke-dasharray="1.2 0.8"' if 'disputed' in note else ''
        s.append(f'<line x1="{X(a):.2f}" y1="{y}" x2="{X(b):.2f}" y2="{y}" stroke="#e2a383" stroke-width="0.9"{dash}/>')
        s.append(f'<circle cx="{X(a):.2f}" cy="{y}" r="1.25" fill="#0f2427" stroke="#e2a383" stroke-width="0.5"/>')
        s.append(f'<circle cx="{X(b):.2f}" cy="{y}" r="1.35" fill="#e2a383"/>')
        gap = b - a
        lab = f'{gap} years' + (f' · {note}' if note else '')
        lx = X(b) + 3
        t(lx, y + 1.1, f'{b}', 6.6 * pt, 'Mono', '#ffffff', extra='font-weight="600"')
        t(lx + 7.5, y + 1.1, lab, 6.6 * pt, 'Mono', '#c9c2b4')
        t(X(a) - 2.5, y + 1.1, str(a), 6.0 * pt, 'Mono', '#9fb3b0', 'end')
    y = top + (len(ROWS) + 0.5) * rh
    t(o + 15, y + 1, 'STILL MISSING', 6.6 * pt, 'Mono', '#e2a383', extra='letter-spacing="0.8"')
    for j, (name, place, a) in enumerate(MISSING):
        y = top + (len(ROWS) + 1 + j + 0.5) * rh
        label(y, name, place, '#d9d2c4')
        s.append(f'<line x1="{X(a):.2f}" y1="{y}" x2="{X(2026):.2f}" y2="{y}" stroke="#8aa09d" stroke-width="0.6" stroke-dasharray="1.4 1"/>')
        s.append(f'<circle cx="{X(a):.2f}" cy="{y}" r="1.25" fill="#0f2427" stroke="#8aa09d" stroke-width="0.5"/>')
        t(X(a) - 2.5, y + 1.1, str(a), 6.0 * pt, 'Mono', '#9fb3b0', 'end')
        t(X(2026) + 3, y + 1.1, f'{2026 - a} years and counting', 6.6 * pt, 'Mono', '#c9c2b4')
    s.append('</svg>')
    return ''.join(s)
