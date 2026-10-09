# Decision log

A record of the main decisions behind this magazine: what was chosen, what else was considered, and why the alternatives lost. Newest entries are appended at the bottom of each section; the log is written as the work happens, not reconstructed afterwards.

Brief (from the commissioner): full creative control over a print magazine — subject, name, writing, images, design. One printed copy, NZ$100 maximum including shipping to New Zealand. File finished by 6pm NZT, Tuesday 13 October 2026. No help or decisions from the commissioner.

Work started: Friday 9 October 2026, 23:40 NZDT.

---

## 1. Printer and format

**Decision: Lulu (lulu.com), Magazine product, A4, saddle stitch, Premium Colour, 70# (≈104 gsm) coated interior, matte cover, 48 interior pages + 4-page printed cover.**
Lulu package ID `0827X1169.FC.PRE.SS.070CW460.MIX`.

Prices were taken from Lulu's own public pricing API (the one the lulu.com/pricing calculator calls) on 9 Oct 2026, not from third-party blogs:

| Item | USD |
|---|---|
| Print, 1 copy, 48 pages, A4 SS premium colour, matte | 14.99 |
| Shipping to NZ — "Mail" (tracked, 15–17 business days) | 11.93 |
| Shipping to NZ — "Express" (tracked, 8–10 business days) | 18.88 |

At USD→NZD 1.7855 (open.er-api.com, 9 Oct 2026). Lulu's help pages list the tax regimes it collects for and NZ is not among them, so GST may not be charged at all (and NZ Customs doesn't collect at the border on a parcel this small). As a worst case I've added 15% GST anyway:
- Mail: (14.99 + 11.93) × 1.15 = US$30.96 ≈ **NZ$55**
- Express: (14.99 + 18.88) × 1.15 = US$38.95 ≈ **NZ$70**

Both are well under the NZ$100 ceiling even allowing ~3% for card currency conversion fees. See `PRINTING.md` for the exact order steps.

Options considered and rejected:

- **Blurb magazine (8.5×11 in).** Premium option has heavier 118 gsm matte paper, which is genuinely nicer than Lulu's. Rejected because Blurb magazines are now *perfect bound*: on a 48-page book the gutter swallows the middle of any image that crosses the spread, and this magazine leans on double-page spreads (the centre spread especially). Blurb also uses US Letter only, and I could not get an exact NZ-delivered quote as reliably as Lulu's API gave one.
- **Lulu perfect-bound A4 magazine** (cheaper: US$12.78 at 48 pp). Same gutter problem; the saddle stitch costs US$2.21 more and lets spreads open flat.
- **Lulu US Letter magazine.** Same price. A4 chosen because the reader is in New Zealand, where A4 is the native magazine/paper size.
- **Lulu "Book" saddle-stitch A4 on 80# coated** (US$14.68). Marginally heavier paper, but it is not the magazine product: no printed inside covers. The magazine product prints the inside front and back covers, which this design uses.
- **NZ local digital printers** (Copybooth, PrintOnline, Print Depot, Bedirect). Attractive because local = fast and no import. Rejected: Copybooth/PrintOnline premium "printed to edge" booklets cap at 40 pages and are self-cover (cover on the same paper as the inside); PrintOnline's quantity selector starts at 100; Bedirect's minimum is 10; Print Depot doesn't publish a single-copy price. None offers a separate cover stock at quantity 1 with a published price.
- **MagCloud (Blurb-owned, still trading).** Quoted on its calculator, 9 Oct 2026: 8.25 × 10.75 in saddle-stitched magazine, US$0.20/page × 52 pages (cover counted in the pages, self-cover) = US$10.40. To NZ: US$12.92 by post (3–5 weeks, **no tracking**) or US$42.85 by FedEx (tracked). Cheapest untracked, but an untracked one-off copy is a real risk; tracked it costs ~US$53, more than Lulu tracked express. Its odd trim size also suits a US reader, not an NZ one. Rejected.
- **Mixam / Cloudprinter.** Not quoted. I couldn't confirm Mixam delivers to NZ. Cloudprinter is a B2B API that needs an account. Lulu already met every requirement with a verifiable quote.

Format consequences: 48 interior pages is Lulu's saddle-stitch maximum, so the issue is designed to exactly 48 + cover. Page size with bleed: interior 8.52 × 11.94 in (216.4 × 303.3 mm, i.e. A4 + 3.175 mm bleed each side); cover spreads 16.79 × 11.94 in. Lulu's official cover template for this configuration is saved in `printer/`.

---

## 2. Subject and name

**Decision: a magazine called *LAZARUS*, about species declared extinct that turned up alive. Issue One: "Presumed Lost".**

"Lazarus taxon" is the real biologists' term for a species that vanishes from the record and then reappears. Every rediscovery is a ready-made story with a shape readers love (loss, doubt, a stubborn person, a moment of proof), and the subject carries a serious idea underneath: extinction is a judgement made on incomplete evidence, and the edges of what we know are closer than they look.

Why this subject beat the others:

- **It's true and checkable.** Each story has dates, names and places that can be verified against primary and reputable secondary sources. A magazine I can't fact-check isn't good, however well it reads.
- **The pictures exist and are free to use.** Nineteenth-century natural-history plates (J. G. Keulemans for Buller's *Birds of New Zealand*, Audubon, etc.) are public domain, beautiful and high-resolution; modern photographs of most of the species are on Wikimedia Commons under open licences. A natural-history magazine can look superb without a single generated image.
- **It's local without being parochial.** New Zealand has some of the best rediscovery stories on Earth (takahē 1948, Chatham Island tāiko 1978, NZ storm petrel 2003), and a live national argument (the 2025 announcement of a project to "de-extinct" the moa). The reader is in NZ; the magazine meets them there but travels.
- **It has range.** Birds, a fish, an insect, a tree; triumph, near-miss and failure. That gives the issue pace, not 48 pages of one note.

Alternatives considered and rejected:

- **AI and society** (the commissioner's own field). Rejected: I'd be writing their own subject back at them, and it photographs badly (stock servers, glowing brains). A magazine should show the reader something they don't already have.
- **A general-interest NZ magazine** (food, travel, people). Rejected: needs reporting, interviews and original photography I can't do from here; it would be thin, generic copy.
- **A fiction/poetry anthology.** Rejected: possible, but a one-voice anthology is a book, not a magazine, and design has less to work with.
- **The deep sea / clouds / maps / lighthouses.** All visually strong. Rejected because they're catalogues rather than stories; "lost and found" gives every page a narrative engine.
- **Extinct species generally.** Rejected as too mournful and too familiar. Rediscovery is the hopeful, surprising inverse, with the failures (huia, thylacine) kept in as counterweight.

Names considered: *Presumed* (good, but reads as an adjective in search of a noun), *Second Sighting* (too long for a masthead), *Not Extinct* (flat), *Relict* (accurate, too obscure). *LAZARUS* is short, strong on a cover, and is the field's own word.
