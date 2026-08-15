# Design system

One idea: **a white gallery wall.** The site recedes; the work is the color.
The exhibition mini-site is the single inversion: a dark room with one accent.

## Tokens (defined once in `css/site.css`)

| token | value | use |
|---|---|---|
| `--bg` | `#f7f6f3` | page background — warm gallery white |
| `--ink` | `#1a1a1a` | text, rules, active states |
| `--muted` | `#6e6e6e` | secondary text, captions |
| `--hair` | `#dcdcdc` | hairline borders |
| `--accent` | `#f7931a` | bitcoin orange — **exhibition context only** |
| `--dark-bg` / `--dark-ink` / `--dark-muted` | `#0e0e0e` / `#f2f2f2` / `#9b9b9b` | the dark room |
| `--sans` | system sans (incl. Apple SD Gothic Neo, Malgun Gothic) | body |
| `--serif` | Iowan Old Style / Palatino / Georgia | captions, years, kickers |
| `--pad` | `20px` | page side padding |
| `--max` | `1080px` | page max width |
| `--measure` | `34em` | body-text line length |

There are two dark surfaces — the exhibition mini-site and `.card--exhibition`
on the list page — and they must read as the same room, so the three dark
values are tokens in `site.css` and both surfaces re-point `--bg/--ink/--muted`
at them. Nothing else changes — same components, inverted room.
Exhibition styles live inside the exhibition's own folder, named after it
(`exhibitions/origin-seoul-2026/origin-seoul-2026.css`) — one file per
exhibition, so future exhibitions stay self-contained.

## Type

- Body: 16px / 1.7 sans. Korean pages add `letter-spacing: -0.01em`.
- Kicker: 11px serif, uppercase, `letter-spacing: .22em`, muted.
- Captions / tombstones / years: serif italic, 13–14px, muted. The trio
  (serif + italic + muted) is one grouped rule per stylesheet; a component
  adds only its own size and box.
- Headings: sans 600. h1 24px on detail pages; the landing name scales with
  `clamp()`. No font is ever loaded over the network.
- No orphans, ever: body text gets `text-wrap: pretty` + `word-break:
  keep-all` (Korean wraps between words, never inside one), headings get
  `text-wrap: balance`. A lone syllable on its own line is a bug.

## Layout

- Mobile first. One shared header (`.site-header`), one footer.
- Gallery: CSS multi-columns (2 columns, 3 from 760px) — pure-CSS masonry that
  absorbs any aspect ratio. `break-inside: avoid` on items.
- Detail pages: image first, full column width (max 880px), then a
  `border-top` rule, title, serif tombstone, body text at `max-width: 34em`.
- Spacing rhythm: multiples of ~6px (6 / 12 / 18 / 26 / 40). Eyeball it; do not
  invent a spacing framework.

## Components (all in `site.css`)

- `.site-header` — exactly two things: wordmark left, language toggle right.
- `.back` — muted "← Works / ← 작품" link, first element inside a detail
  page's `<main>`.
- `.gallery` — `<ul>` masonry of `<figure>` cards; caption = title + serif year.
- `.card--exhibition` — the one dark card in the white gallery; orange kicker.
- `.searchbar` — fixed bottom, AI-chat-style panel: rounded 16px, hairline
  border, blur, soft shadow. It is one box, only as wide as the panel, so taps
  beside it reach the gallery underneath. Input on top, filter chips below
  (like a model picker). Chips are `<button aria-pressed>`; active chip = ink
  pill, and that pressed chip *is* the filter state — `gallery.js` reads it
  rather than keeping its own copy.
- `.work-hero` / `.work-view` — the image plates on a detail page. `site.css`
  centres them; a page's own `<style>` sets only the `max-width` it wants.
- `.tombstone` — serif muted "year · medium · size" line.
- `.todo` — dashed hairline box, serif italic, for not-yet-written text.
- `.work-nav` — footer prev / all / next links with `rel="prev/next"`.

## Per-page character

Each artwork page may add **one `<style>` block, ≤ 40 lines**, to fit the work
(e.g. a narrow column for a tall piece, a hairline case, extra air). Layout
only — every artwork page stays on the light tokens; the exhibition mini-site
is the sole dark room, with its own stylesheet inside its folder.
It must keep the shared header, `.back` link, tombstone, `.todo` placeholder,
`.work-nav`, and Microdata.

## Rules

- No shadows except the search bar. No border radius except the search bar and
  chips. No animation except `opacity`/`color` transitions ≤ 200ms.
- Never crop an artwork. Never place text over an artwork.
- Alt text describes the artwork plainly, in the page language.
- If a page needs more than this document offers, the page is too complicated.
