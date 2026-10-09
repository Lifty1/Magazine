# LAZARUS

*A magazine of things presumed lost.* Issue One: **Presumed Lost** (October 2026). 48 pages + cover, A4, print run of one.

LAZARUS is about species that were declared extinct and then turned up alive: the takahē in Fiordland, the coelacanth off South Africa, the Lord Howe Island stick insect on Ball's Pyramid, the Bermuda cahow, the Chatham Island tāiko, the New Zealand storm petrel, the Wollemi pine and the black-footed ferret. It also covers the ones that never came back (huia, South Island kōkako, thylacine, ivory-billed woodpecker), and argues about whether a moa should be made in a lab.

- **To print it:** see [`PRINTING.md`](PRINTING.md). Printer: Lulu. Files: `print/LAZARUS-01-interior.pdf` and `print/LAZARUS-01-cover.pdf`.
- **To read it on screen:** `print/LAZARUS-01-preview-spreads.pdf`.
- **Why it is the way it is:** [`DECISIONS.md`](DECISIONS.md).

## Contents

| Page | |
|---|---|
| 1 | Contents |
| 2 | Presumed (editor's letter) |
| 3 | How to Declare Something Extinct |
| 4 | The Footprint: the takahē |
| 10 | The Most Beautiful Fish: the coelacanth |
| 16 | The Tree Lobsters of Ball's Pyramid |
| 20 | The Tree in the Canyon: the Wollemi pine |
| 22 | The Plates: Keulemans' birds |
| 24 | The Ledger: centre-spread timeline |
| 26 | Night Voices of the Isle of Devils: the cahow |
| 29 | Counting: recovery charts |
| 30 | Hiding at Sea: tāiko and NZ storm petrel |
| 34 | Made, Not Found: essay on the moa and de-extinction |
| 38 | What the Dog Brought Home: the black-footed ferret |
| 40 | The Ones That Haven't Come Back |
| 44 | Nearly: the kākāpō |
| 46 | How Lost Things Are Found Now: field notes |
| 48 | The Whistle: coda |

## Repository layout

```
content/        the articles, in Markdown (front matter: kicker, title, standfirst; > lines become pull quotes)
src/style.css   the print stylesheet (type, colour, components)
tools/          build pipeline (see below)
fonts/          Fraunces, Newsreader, IBM Plex Mono (SIL OFL) + static instances
assets/raw/     source images as downloaded, with credits.json (source, author, licence)
assets/print/   colour-managed print copies of the images
printer/        Lulu's official cover template for this exact product
print/          FINAL FILES
research/       independent fact-check output
DECISIONS.md    decision log
PRINTING.md     what to order and how
```

## Building

Requirements: Python 3 with `markdown`, `pyphen`, `pypdf`, `Pillow`, `fonttools`; Node with Playwright and Chromium; poppler-utils.

```sh
python3 tools/build_fonts.py      # static font instances (once)
python3 tools/prep_images.py      # sRGB print copies of images
python3 tools/build.py            # compose build/interior.html (layouts: tools/pages.py, ledger.py, recovery.py)
python3 tools/cover.py            # compose build/cover.html (credits are collected from the interior)
node tools/render.js              # Chromium: thread text into frames, report overflow and image ppi, print PDFs
python3 tools/finalize.py         # check page count/size/fonts, set Trim/BleedBox, write print/*.pdf
python3 tools/preview_pdf.py      # reading copy in spreads
```

`render.js` prints one line per story: whether the text overflowed its frames, and how full the last frame is. `finalize.py` fails if the page count or size is wrong, a font is not embedded, a fallback font slipped in, or any Type 3 font is present.
