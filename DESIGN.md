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

The one dark surface is the exhibition mini-site: it re-points
`--bg/--ink/--muted` at the three dark tokens. Nothing else changes — same
components, inverted room. Exhibition styles live inside the exhibition's own folder, named after it
(`exhibitions/origin-seoul-2026/origin-seoul-2026.css`, and any script beside
it) — one of each per exhibition, so future exhibitions stay self-contained.
The one component with no equivalent on a work page is `.exh-plates`, a work
that is more than one photo: below 560px a scroll-snap strip swiped a photo at
a time, with arrows (the script's, hidden until it wires them) and one dot per
photo; above, the set is simply hung — first plate leading, the rest side by
side under it.

## Type

- Body: 16px / 1.7 sans. Korean pages add `letter-spacing: -0.01em`.
- Kicker: 11px serif, uppercase, `letter-spacing: .22em`, muted.
- Captions / tombstones / years: serif italic, 13–14px, muted. The trio
  (serif + italic + muted) is one grouped rule per stylesheet; a component
  adds only its own size and box.
- Headings: sans 600. h1 24px on detail pages; the landing name scales with
  `clamp()`. The exhibition's wall label is one line at every width, so it is
  sized off the column instead (`--title` in the mini-site's stylesheet, with
  `--sub` keeping every heading under it smaller — on a phone the label lands
  around 18px and nothing may outgrow it). No font is ever loaded over the
  network.
- No orphans, ever: body text gets `text-wrap: pretty` + `word-break:
  keep-all` (Korean wraps between words, never inside one), headings get
  `text-wrap: balance`. A lone syllable on its own line is a bug.

## Layout

- Mobile first. One shared header (`.site-header`), one footer.
- Landing: the name, centred, on the artist's own drawing of a vanishing point
  (`vanishing-point.svg`, 2026-11-08) — the one wall on the site that is not
  plain `--bg`. The drawing is stretched to the screen's shape, corner to
  corner, so the name always stands where the tunnel ends, on a phone held
  upright as on a desk: a one-point tunnel stretched along one axis is still
  an exact one-point tunnel. Its strokes are drawn in screen pixels, so the
  stretch never thickens one axis' lines. It moves once: as the page arrives
  it settles back from two frames deep, the tunnel flowing inward toward the
  point (only a `scale` animates — see `site.css`). Then nothing moves.
- Gallery: CSS multi-columns (2 columns, 3 from 760px) — pure-CSS masonry that
  absorbs any aspect ratio. `break-inside: avoid` on items, and the air under
  each is `padding-bottom`, never a margin: WebKit carries a margin over a
  column break, so on an iPhone every column after the first started 20px
  low. The tops of the columns are one line (the artist, 2026-11-10).
- Detail pages: image first, full column width (max 880px), then a
  `border-top` rule, title, serif tombstone — and nothing else in words: a
  work page is title, year, medium, size, then its themes as a second
  tombstone line, each a link to the page of the artist's note on it (the
  artist asked for the tags, 2026-11-08). Every other photo of the work hangs
  below the tombstone as a `.work-view` plate, in the artist's order, with a
  short serif caption where one says something (detail, installation view,
  side) and none otherwise.
- Spacing rhythm: multiples of ~6px (6 / 12 / 18 / 26 / 40). Eyeball it; do not
  invent a spacing framework.

## Components (all in `site.css`)

- `.site-header` — exactly two things: wordmark left, language toggle right.
- `.site-footer` — the header's mirror: one ruled line in the same container,
  how to reach the artist on the left (an `<address>`: the email and
  *Telegram* — the handle is never printed, only the word, linked) and the ©
  line with the build credit on the right, as `<small>` print in the muted
  serif italic. 13px muted sans, links to ink on hover, no underlines but the
  hairline under the credit. On a phone the two simply stack, left. After a
  `.work-nav` the rule is already drawn, so the footer drops its own and keeps
  the air. The landing has no footer: it is only the name on the drawing.
- `.back` — muted "← Works / ← 작품" link, first element inside a detail
  page's `<main>`.
- `.gallery` — `<ul>` masonry of `<figure>` cards; caption = title + serif year.
  No hover state: the photograph never dims under the pointer.
- `.bars` — the artist's ways in, as long boxes ruled in ink, one under the
  other, each the name alone in sans 600. Across the top of the list, above
  the "Works" title, the CV and the notes, in the order of the artist's
  sketch; on `/notes/`, one per theme. The artist asked for long boxes rather
  than cards (2026-11-09), and for nothing in them but the name (2026-11-10).
- `.work-hero` / `.work-view` — the image plates on a detail page. `site.css`
  centres them; a page's own `<style>` sets only the `max-width` it wants.
- `.tombstone` — serif muted "year · medium · size" line; also the line of a
  work's themes. A link in it carries a hairline, no louder than the line.
- `.notes` — the artist's notes. `/notes/` is the themes as `.bars`, then the
  thesis title. Each theme has its own page (`/notes/<theme>/`), set like a
  work page without the photo: the note's title as the `<h1>` under the ink
  rule, the text at the reading measure (the artist's line breaks kept as
  `<br>`), then, ruled in hairline like a CV section, the works it names — the
  list's own `.gallery`, the same cards in the same order, photos and all
  (the artist asked for it, 2026-11-09). A note no work on the site carries
  yet is the text alone.
- `.cv` — the CV: a `<dl>` per section, the year in the caption serif beside
  its line. Built from tokens only, so it sits on the white wall (`/cv/`) and
  in the dark room (the exhibition page) unchanged. It is English on the
  Korean pages too (`lang="en"`, no Korean tracking) — the owner's choice.
- `.work-nav` — the one way out of a work: a single centred "All works /
  전체 작품" link under a hairline. No prev/next; the list holds the order.

## Per-page character

Each artwork page may add **one `<style>` block, ≤ 40 lines**, to fit the work
(e.g. a narrow column for a tall piece, a hairline case, extra air). Layout
only — every artwork page stays on the light tokens; the exhibition mini-site
is the sole dark room, with its own stylesheet inside its folder.
It must keep the shared header, `.back` link, tombstone, `.work-nav`, and
Microdata.

## Motion

Motion happens **three times, and nowhere else**. It is one continuous idea —
light crosses a wall, the name carries you over, the works are hung — and the
list below is closed. Everything else on the site, every other navigation
included, is a plain cut.

**1 · The name arrives** (landing). Raking light crossing a gallery wall: a
soft lit edge — a `mask` gradient 3× the width of the line, slid across it —
travels left to right in 1.8s while the tracking settles from `.26em` to
`.14em` and a `.18em` blur clears in 1.4s. Two curves, so a letter is still
resolving as the light reaches it. No JS and no per-letter markup: the mask
gives the letter-by-letter reading while the `<h1>` stays one selectable,
screen-readable string. Tracking and `margin-left` always move together or the
name drifts off centre. Hovering the name itself (pointer only — the hover is
on the `<h1>`, whose box is exactly the line of text, not on the full-screen
link around it) steps it back to `.6` opacity and opens the tracking to
`.17em`.

**2 · The name carries you across** (landing → works, 1.1s, one way only). The
name *is* the landing and it *is* the header of the list, so both carry
`view-transition-name: wordmark` and the browser glides one into the other
instead of blinking. This is the only crossing that animates. A cross-document
transition needs **both** documents to opt in, and that is exactly what keeps
it scoped: `@view-transition { navigation: auto }` sits in a `<style>` block on
those four pages alone — landing and works, EN and KO. Do not move it into
`site.css`; that would animate every navigation on the site. The page under the
name changes hands in 0.3s, because moment 3 is the part meant to be watched.

Coming back is a plain cut, and deliberately so: a document styles only the
crossings that *end* in it, so the landing's own `<style>` cancels them —
otherwise the glide would land on top of moment 1 and you would never see the
name arrive. Two rules, and both are needed. `animation: none` on the group and
the new snapshot stops the glide; `display: none` on the **old** snapshot
matters just as much, because a cancelled transition still paints one frame,
and that frame would otherwise carry the list you came from with the header
wordmark blown up to the landing's geometry — read as the name blinking before
its own arrival. No JS: `@view-transition` cannot be made one-directional, but
what the crossing paints is entirely CSS's to decide. Measured in Chrome
(screencast, frame by frame): out 1.1s; back 14ms with the frame after the list
already the empty wall, and `name-settle` / `name-light` running from there.

**3 · The works are hung** (list, and under a note — the same `.gallery`,
0.7s). Every card lifts 14px and resolves
at once, so the top edge of the list is one straight line from the first
frame — the artist asked for it (2026-09-11). It used to be staggered, 45ms a
card, but the columns are filled one after another, so the top of the second
column comes from the middle of the source order and rose last: for about
0.6s the top of the list was a step, not a line.

At rest, nothing moves, ever: every one of these fills `backwards` only, so a
settled page is exactly its plain rules — full ink, no mask dimming, no loop,
no repaint. `prefers-reduced-motion` drops all travel and leaves a plain fade
(and, on the landing, keeps the hover dim as the affordance).

## App icon

The home-screen icon is the landing name cropped to its initials — `PSG`, ink
on the plain `--bg` wall (not the landing's drawing), set the way
`.landing h1` is set (sans 600, tracked `.14em`). Rendered, never hand-drawn: `scripts/build-icons.sh`, which also
holds the maskable safe-zone budget that caps how large the letters may go. If
the landing's type ever changes, rebuild the icon with it.

## Rules

- No shadows. No border radius except `.exh-plates`'s arrows and dots — round because the shape is
  the affordance, on top of a photo that offers no edge to align to. No
  animation except `opacity`/`color` transitions ≤ 200ms — and the three
  moments above, which are deliberate and closed. `.exh-plates` glides when an
  arrow is tapped, and that is not a fourth moment: nothing on the page
  animates, only how far the tap carries a scroller the reader could just as
  well have swiped by hand, and `prefers-reduced-motion` drops it to `auto`. A
  fourth animated thing anywhere on the site is still a bug.
- Never crop an artwork. Never place text over an artwork. (The landing's
  drawing is not a work on the list: the artist made it to stand behind the
  name.)
- Alt text describes the artwork plainly, in the page language.
- If a page needs more than this document offers, the page is too complicated.
