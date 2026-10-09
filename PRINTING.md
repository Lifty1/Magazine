# How to print LAZARUS No. 1

**Printer:** [Lulu](https://www.lulu.com), print on demand.
**Product:** Magazine · A4 (8.27 × 11.69 in / 210 × 297 mm) · Saddle stitch · Premium Colour · 70# coated white interior · Matte cover · 48 interior pages.
**Files:**

| File | What it is | Spec |
|---|---|---|
| `print/LAZARUS-01-interior.pdf` | The 48 inside pages, in order, single pages (not spreads) | 8.52 × 11.94 in per page (A4 + 0.125 in bleed all round); fonts embedded |
| `print/LAZARUS-01-cover.pdf` | The cover: page 1 = outside (back cover left, front cover right); page 2 = inside (inside front cover left, inside back cover right) | 16.79 × 11.94 in per page, built on Lulu's own template for this product (`printer/lulu_cover_template_A4_SS_48.pdf`) |
| `print/LAZARUS-01-preview-spreads.pdf` | A small reading copy in spreads. **Not for printing.** | — |

## Order steps

1. Go to **lulu.com → Create → Magazine** (or lulu.com/create/magazines → "Start a magazine"). Sign in or create a free account.
2. Project details: title **LAZARUS No. 1**, any author name. When asked about distribution / goal, choose the private option (print for yourself; **no ISBN, no retail distribution**). This keeps the back cover free of a barcode.
3. Upload **`LAZARUS-01-interior.pdf`** as the interior.
4. Choose the print options exactly:
   - Trim size: **A4 (8.27" × 11.69")**
   - Binding: **Saddle stitch**
   - Interior colour: **Premium Colour**
   - Paper: **70# Coated White** (the only paper offered for the magazine product)
   - Cover finish: **Matte**
5. For the cover choose **upload your own cover** and upload **`LAZARUS-01-cover.pdf`** (two pages: outside, then inside). Lulu's preview should show the takahē on the front and the huia on the back.
6. Check Lulu's preview. Lulu's file checker may warn that a few photographs are below 300 ppi. That's expected: the lowest is 193 ppi. Accept the warning.
7. Order **1 copy**. Shipping address: your NZ address. Shipping method: **Express** (tracked, 8–10 business days after printing). **Mail** (tracked, 15–17 business days) also fits the budget if you'd rather save NZ$15.

## What it should cost

Quoted from Lulu's own pricing API on 9 October 2026 (USD):

| | Mail | Express |
|---|---|---|
| Print (48 pp, A4, saddle stitch, premium colour) | 14.99 | 14.99 |
| Shipping to New Zealand | 11.93 | 18.88 |
| Subtotal | 26.92 | 33.87 |
| + 15% NZ GST *if Lulu charges it* | 30.96 | 38.95 |
| **≈ NZD** (at 1.7855) | **≈ NZ$55** | **≈ NZ$70** |

Even with a card's foreign-exchange fee (~2–3%), Express comes in under **NZ$72**, comfortably inside the NZ$100 budget. Lulu prints in 3–5 business days, before shipping. Lulu sometimes runs discount codes, so check the checkout page for one.

## If something goes wrong

- **Lulu rejects the page size.** Interior pages are exactly 613.44 × 859.68 pt (8.52 × 11.94 in) with TrimBox set to A4. If Lulu still complains, it is almost certainly because a different trim size or the US Letter product was selected. Re-select A4.
- **Lulu asks for a one-page cover.** You are in the Book flow, not the Magazine flow. Start again from Create → Magazine. Only the Magazine product prints inside covers.
- **You want to rebuild the files.** See `README.md`.
