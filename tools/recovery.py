"""'Counting' page: small multiples of recovery counts (one series per panel, shared time axis)."""
PT = 0.3528
SERIES = [
    ('Takahē', 'estimated birds', [(1982, 118), (2013, 263), (2016, 306), (2017, 347), (2019, 418), (2024, 529)], 600),
    ('Kākāpō', 'known birds', [(1995, 51), (2026, 325)], 400),
    ('Cahow', 'breeding pairs', [(1951, 18), (1960, 18), (2019, 132), (2020, 135), (2021, 142), (2023, 164)], 200),
]
INK, MUTED, RULE, MARK = '#17191a', '#6d6a62', '#c9c1b2', '#b0452a'

def recovery_svg(w, h):
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}mm" height="{h}mm" viewBox="0 0 {w} {h}">']
    def t(x, y, txt, size, fam, fill=INK, anchor='start', extra=''):
        s.append(f'<text x="{x:.2f}" y="{y:.2f}" font-family="{fam}" font-size="{size*PT:.3f}" fill="{fill}" text-anchor="{anchor}" {extra}>{txt}</text>')
    L, R = 22, w - 14
    X = lambda yr: L + (yr - 1945) * (R - L) / (2030 - 1945)
    ph = (h - 14) / 3
    for i, (name, unit, pts, ymax) in enumerate(SERIES):
        top = i * ph + 6; bot = top + ph - 16
        Y = lambda v: bot - v * (bot - top) / ymax
        t(0, top - 1, name, 15, 'FD Regular')
        t(0, top + 3.6, unit.upper(), 6.2, 'Mono', MUTED, extra='letter-spacing="0.4"')
        for v in range(0, ymax + 1, ymax // 4):
            y = Y(v)
            s.append(f'<line x1="{L}" y1="{y:.2f}" x2="{R}" y2="{y:.2f}" stroke="{RULE}" stroke-width="{0.35 if v == 0 else 0.18}"/>')
            t(L - 2, y + 1, str(v), 6.2, 'Mono', MUTED, 'end')
        for yr in range(1950, 2031, 10):
            t(X(yr), bot + 4.5, str(yr), 6.2, 'Mono', MUTED, 'middle')
        d = ' '.join(f'{"M" if j == 0 else "L"}{X(a):.2f},{Y(b):.2f}' for j, (a, b) in enumerate(pts))
        s.append(f'<path d="{d}" fill="none" stroke="{MARK}" stroke-width="0.7" stroke-linejoin="round"/>')
        for j, (a, b) in enumerate(pts):
            s.append(f'<circle cx="{X(a):.2f}" cy="{Y(b):.2f}" r="1.15" fill="{MARK}" stroke="#f4eee3" stroke-width="0.5"/>')
            if j in (0, len(pts) - 1):
                anchor = 'end' if j == len(pts) - 1 else 'start'
                dx = -2.2 if anchor == 'end' else 2.2
                t(X(a) + dx, Y(b) - 2.2, f'{b} <tspan fill="{MUTED}" font-size="{6*PT:.3f}">in {a}</tspan>', 9, 'FT SemiBold', INK, anchor)
    s.append('</svg>')
    return ''.join(s)
