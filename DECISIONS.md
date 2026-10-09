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

---

## 3. What goes in the issue

**Decision: eight rediscovery stories of different lengths, one long argumentative essay, one section on species that stayed lost, a data centre spread, and short framing pieces.** Final running order is in `README.md`.

- **Stories chosen:** takahē (NZ, the anchor story), coelacanth (the most famous Lazarus taxon), Lord Howe Island stick insect (the strangest), cahow (the longest gap, ~330 years, and a boy who devoted his life to it), Chatham Island tāiko and NZ storm petrel (NZ, seabirds, found at night and at sea), Wollemi pine (a plant, for range), black-footed ferret (found because a dog killed one, which echoes the takahē, and links to cloning).
- **Counterweight:** "The Ones That Haven't Come Back" (huia, South Island kōkako, thylacine, ivory-bill) and the coda about the only recording of a huia call. Without these the issue would be falsely cheerful.
- **The essay:** the 2025 Colossal/Ngāi Tahu Research Centre moa project is the live argument in this field and it is local to the reader. I took a position (rediscovery and resurrection are different things, and the money should go to the living first), but gave the case for it a fair hearing.
- **Considered and left out:** night parrot (the 2013 rediscovery is tangled up with later retracted records, too messy to tell cleanly in two pages), Jerdon's courser, La Gomera giant lizard, Laotian rock rat, mountain pygmy possum, Chacoan peccary (these appear only in the Ledger timeline), Attenborough's echidna and De Winton's golden mole (used in Field Notes instead of features).
- **Page-count adjustment.** The first full layout showed the text running about six pages short of 48. I didn't pad, enlarge type or leave blank columns. Instead I (a) added a 2-page ferret story, which also strengthens the moa essay's argument; (b) added a short descriptive section to the takahē piece, which needed a picture of the bird itself; (c) added data pages built from facts already researched: "Coelacanth by the numbers", "Counting" (recovery charts), and timelines and fact boxes; (d) gave photographs more room where their resolution allowed.

## 4. Writing and accuracy

- **Every factual claim was checked against a source while writing** (mostly Wikipedia's articles cross-checked with primary or institutional sources: DOC, NZ Birds Online, the Smithsonian, Nonsuch Expeditions, RNZ, AP, US Fish and Wildlife Service notices). The sources are listed inside the back cover.
- **Where sources disagreed or I could not confirm a detail, I cut it rather than guess.** Examples: the name of the Comorian fisherman who caught the 1952 coelacanth (sources give two different names), the wording of J. L. B. Smith's leaflet beyond its first line, whether the 1909 huia expedition meant to capture birds, the exact date of the huia recording (given as "about 1949"), the ivory-bill's current legal status (described as deferred, which is the last formal word I could find), whether the Lord Howe insects have yet been released (described as not yet, "at the time of writing").
- **Independent check:** I ran each article past a second model via OpenRouter (`tools/factcheck.py`). The account's credit ran out after the first article (`research/factcheck/01-letter.md`), and all four of its points were valid and were fixed. The remaining articles got a second line-by-line pass from me against the sources. Several claims were softened as a result: "declared extinct" became "written off" for the coelacanth, the takahē-feeding detail was limited to what the sources say, the Dakota became an "aeroplane", not a "bomber", and so on.
- **Authorship is disclosed** in the editor's letter and the colophon. A reader of a nonfiction magazine should know an AI wrote it.

## 5. Images

**Decision: no AI-generated images. All pictures are public domain or openly licensed, credited inside the back cover with author and licence.**

- **Why no generated images:** this is a nonfiction natural-history magazine. A generated takahē or coelacanth would be a fake specimen, subtly wrong anatomically and impossible to caption honestly. The real archive (Keulemans' 1888 lithographs, museum specimens, field photographs) is more beautiful and true.
- **Sources used:** National Library of New Zealand (Buller/Keulemans plates, "no known copyright restrictions"), Flickr originals under CC BY / BY-SA / CC0 (found via Openverse), Pexels (landscapes), Wellcome Collection (the 1877 Owen and moa photograph), Archives New Zealand (1949 Notornis Expedition), US Fish and Wildlife Service and USGS (ferrets).
- **Wikimedia Commons** was the first choice, but it rate-limited this machine's shared IP (HTTP 429) for the whole session. I didn't try to evade the limit. Most Commons photos originate on Flickr, so I fetched originals there instead. Images that existed only on Commons were mostly dropped (the stick-insect portraits, the 1933 thylacine photo). A slow background downloader that respected the limits eventually got one through, the public-domain photo of Marjorie Courtenay-Latimer with the mounted coelacanth, and it was added to page 13 at 199 ppi. Te Papa's API was unreachable (502).
- **Resolution:** every placed image was measured at render time. Anything printing below ~190 ppi was resized or moved (Ball's Pyramid went from a full-width bleed at 143 ppi to an inset at 265 ppi). The lowest in the final file is 193 ppi, a photograph that will print acceptably on Lulu's digital press.

## 6. Design

- **Typography:** *Fraunces* for display (soft, old-style, with an optical-size axis that keeps it delicate at 90 pt), *Newsreader* for body text (designed for long reading at small sizes), *IBM Plex Mono* for kickers, captions and data (a specimen-label feel). Rejected: Playfair Display (over-used, too high-contrast for coated paper), EB Garamond (too small on the body at 9 pt in narrow columns), Inter or another grotesque for captions (too corporate for natural history). All three chosen families are SIL Open Font License.
- **Grid and colour:** A4, 3-column grid (55 mm columns, 5 mm gutters), generous margins kept outside Lulu's 0.5 in safety zone. A warm "paper" tint for archival and editorial pages, white for features, deep teal-black for the data spread and coda, and one rust accent taken from the takahē's beak.
- **Cover:** Keulemans' 1888 takahē plate, full bleed, with a black masthead. It is the issue's anchor story, it is a New Zealand image for a New Zealand reader, and it looks like nothing on a newsstand. Rejected: the coelacanth holotype (a dark museum photo, weaker at thumbnail size) and a purely typographic cover (cold). **Back cover:** the huia, "Last confirmed sighting: 28 December 1907", so the outside of the magazine is a found bird on the front and a lost one on the back.
- **Charts:** the Ledger (centre spread) is a timeline of gaps between last record and rediscovery. "Counting" uses small multiples (one panel per species, each with its own count) rather than one chart with three different units, which would mislead.

## 7. Production

- **Layout engine:** HTML/CSS rendered by headless Chromium, with a small script (`tools/thread.js`) that pours text through linked column frames like InDesign's threaded text boxes, splitting paragraphs, keeping headings with their text and avoiding stretched last lines. Rejected: WeasyPrint (better paged-media support, but no linked frames, so the magazine-style fixed layouts would have needed hacks), ReportLab (too low-level for this much typography), and Scribus or InDesign (not available headless here, and not reproducible from source).
- **Fixes found in testing:** headings were being set in a synthetic bold that Chromium embeds as Type 3 fonts, so I forced normal weight. An end-of-article glyph missing from the body font was pulling in a fallback font, so I replaced it with a CSS square. Chromium's page size was ~0.5 pt off Lulu's spec, so `finalize.py` sets exact MediaBox/TrimBox/BleedBox. The final check fails on any of these.
- **Colour:** files are sRGB. Lulu's print pipeline accepts RGB and converts to CMYK itself. Doing my own conversion without Lulu's press profile would more likely harm than help.

## 8. Ordering choices

- **Shipping: Express** (US$18.88, 8–10 business days, tracked) over Mail (US$11.93, 15–17 business days). Both are well under budget; Express is about NZ$15 more and halves the wait for a one-off copy. Total ≈ NZ$70 worst case, including GST.
- **Matte cover** rather than gloss. It suits the lithograph and the natural-history tone, and doesn't glare.

## 9. Known limitations

- The independent model fact-check covered only the editor's letter before the OpenRouter credit ran out. The rest was double-checked by me against sources, not by a second model.
- A few Commons-only images could not be obtained because of the rate limit (see §5); the layouts use the best available alternatives. The background downloader also overwrote the image-credits file with a stale copy before it stopped. This was caught when the cover build failed and fixed by restoring the committed version.
- I could not see a physical proof. Colour on Lulu's press will be somewhat less saturated than on screen, especially in the dark spreads.
