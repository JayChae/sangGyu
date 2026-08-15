# parksanggyu — personal website of the artist Park Sang Gyu

Static site. No build step, no framework. Deployed on Cloudflare Pages with
`public/` as the output directory.

## Principles (non-negotiable)

- **Simple is best.** If a feature can be dropped, drop it.
- **Mobile first.** Design and test at phone width before desktop.
- **Clean, simple code.** No abstractions that a static site does not need.
- **Speed matters.** Every page must be fast on a slow phone at a gallery.
- **CSS stays minimal.** One shared stylesheet (`public/css/site.css`). Each
  exhibition mini-site is self-contained: everything specific to it, including
  its stylesheet, lives inside its own folder and is named after it
  (`public/exhibitions/origin-seoul-2026/origin-seoul-2026.css`). A page may
  add its own `<style>` block of at most ~40 lines for page-specific character.
- **A (very simple) design system** lives in `DESIGN.md`. Follow it.
- **English and Korean.** English is the default. Korean is a `ko.html` file
  next to each page's `index.html`, served at a clean `…/ko` URL by Cloudflare
  Pages (`/works/ecology/` ↔ `/works/ecology/ko`; the Korean landing is
  `/ko`). Every page links its counterpart (`hreflang` alternates + the header
  language toggle) and carries a self-referencing `rel=canonical` (relative
  for now — make absolute once the domain exists).
- **Hypermedia philosophy.** HATEOAS: every page reachable by links, navigation
  is plain `<a>`. Semantic HTML5 (`<article>`, `<figure>`, `<time>`, `<search>`,
  `rel="prev/next"`). Schema.org via Microdata (`VisualArtwork`, `Person`,
  `ExhibitionEvent`).
- **Use HTML to the fullest.** Prefer an HTML element or attribute over CSS,
  and CSS over JS. JS is a progressive enhancement only (currently only the
  gallery search/filter; the site works without it).
- **Images are always WebP**, responsive (`srcset` 480/960/1600) with explicit
  `width`/`height` (no layout shift), `loading="lazy"` below the fold.
- **HTTP caching** is configured in `public/_headers`: immutable for `/img/*`,
  a week for CSS/JS, revalidate for HTML.
- **Web performance**: no webfonts (system stack), no external requests, tiny
  CSS/JS, `fetchpriority="high"` on hero images only.

## Structure

```
public/                     ← Cloudflare Pages output directory
  index.html                landing — only the centered name, linking to /works/
  ko.html                   landing (KO), served at /ko
  works/index.html          gallery list (EN) — masonry + bottom search/filter bar
  works/ko.html             gallery list (KO), served at /works/ko
  works/<slug>/index.html   one hand-made page per artwork (EN)
  works/<slug>/ko.html                                      (KO)
  exhibitions/origin-seoul-2026/   self-contained exhibition mini-site:
    index.html, ko.html            EN + KO pages
    origin-seoul-2026.css          its styles (dark, bitcoin orange)
  css/site.css              shared styles (design system)
  js/gallery.js             search + tag filter for the list page (~50 lines)
  img/<slug>/{480,960,1600}.webp   one folder per artwork
                                   (extra views: collective-gaze/view2-*.webp)
  _headers                  Cache-Control rules
  404.html, robots.txt
scripts/build-images.sh     JPEG (../sangyu/arts) → WebP (public/img)
scripts/serve.py            local preview with Cloudflare-style clean URLs
DESIGN.md                   the design system
TODO.md                     open items waiting on the owner (in Korean)
```

## Works (single source of truth)

Order below = curated order on the list page and the `rel=prev/next` chain.

| slug | title (EN) | title (KO) | year | medium | tags |
|---|---|---|---|---|---|
| the-stranger | The Stranger (Triptych) | 이방인 (삼면화) | 2025 | Ceramic, 30 × 20 cm | ceramic |
| ecology | Ecology | 생태 | 2023 | Ceramic, 30 × 30 × 25 cm | ceramic |
| collective-gaze | Collective Gaze | — | TBD | Ceramic | ceramic |
| brave-new-world | Brave New World | — | TBD | Mixed-media installation | installation |
| beyond-the-predetermined | Beyond the Predetermined | — | TBD | Mixed-media installation | installation |
| a-cushion | A Cushion | — | TBD | Ceramic | ceramic |
| untitled | Untitled | 무제 | TBD | Ceramic | ceramic |

Notes: `collective-gaze` has a second view, `collective-gaze-2-*.webp`.
The source file "A Cusion.jpg" is a typo; the site spells it "A Cushion".
The ORIGIN SEOUL 2026 exhibition (Aug 31 – Sep 2, 2026, Seoul) appears as the
first card on the list page and features Ecology and The Stranger.

## Exhibition mini-site

`/exhibitions/origin-seoul-2026/` is the page behind the single QR code printed
next to the works at ORIGIN SEOUL 2026 (originseoulbtc.com). One QR → artist
intro + both works + "Collect (Bitcoin only)" section that links to Telegram.
Everything on it is written through a Bitcoin lens. No prices are shown.

## TODO

Open items waiting on the owner live in `TODO.md` (kept in Korean). Notably:
every artwork page has a "to be written" description placeholder on purpose —
do not invent descriptions, years, or dimensions.

## Local preview

```
./serve.sh        # → http://localhost:8000 (wraps scripts/serve.py)
```

Plain `python3 -m http.server` 404s on the clean `…/ko` URLs (the `.html`
resolution is Cloudflare's job in production); `scripts/serve.py` adds the
same fallback locally. `npx wrangler pages dev public` also works and
additionally emulates `_headers`.
