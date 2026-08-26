# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

Personal website of the artist Park Sang Gyu. Static site: no build step, no
framework, no dependencies. Deployed on Cloudflare Pages with `public/` as the
output directory — files are served exactly as committed.

## Commands

```
./serve.sh [port]                 # local preview → http://localhost:8000
python3 scripts/check-links.py    # the test suite (exit 1 on failure)
scripts/build-images.sh           # source photos (../sangyu/arts/<work>/) → WebP in public/img/ (needs cwebp + jpegtran: brew install webp)
scripts/build-icons.sh            # the app icon → public/icon-{192,512}.png (needs Chrome)
python3 scripts/build-qr.py [--mm N] [--clear] [/path ...]   # print-ready QR for any page → print/qr-<path>.{svg,png} (default: the exhibition page, 50 mm square, black; --clear = no white behind the PNG)
```

- `check-links.py` asserts three things: every internal `href`/`src`/`srcset`
  resolves; every page's `canonical`, `og:url`, `hreflang` alternates and
  language toggle point at itself and its counterpart (absolute, on `ORIGIN`),
  its `og:image` exists, and `sitemap.xml` lists exactly the indexable pages;
  and the works on disk are exactly `WORKS.md`'s, walked in its order by both
  list pages, each work page leading back to the list and nowhere else (no
  `rel=prev/next`). Run it after adding, moving, renaming or reordering
  anything. There is no other lint/test tooling.
- `scripts/pages.py` holds the one model of how Cloudflare Pages maps a URL to
  a file (clean URLs, `index.html`, case-sensitivity) and the site's `ORIGIN`
  (`https://sanggyu.pages.dev`). Both `check-links.py` and `serve.py` import
  it — do not re-implement that routing in either.
- Plain `python3 -m http.server` 404s on the clean `…/ko` URLs (the `.html`
  resolution is Cloudflare's job in production); `serve.sh` wraps
  `scripts/serve.py`, which adds the same fallback locally.
  `npx wrangler pages dev public` also works and additionally emulates
  `_headers`.

## Principles (non-negotiable)

- **Simple is best.** If a feature can be dropped, drop it.
- **Mobile first.** Design and test at phone width before desktop.
- **Clean, simple code.** No abstractions that a static site does not need.
- **Speed matters.** Every page must be fast on a slow phone at a gallery.
- **CSS stays minimal.** One shared stylesheet (`public/css/site.css`). Each
  exhibition mini-site is self-contained: everything specific to it, including
  its stylesheet and any script, lives inside its own folder and is named
  after it (`public/exhibitions/origin-seoul-2026/origin-seoul-2026.css`,
  `…/origin-seoul-2026.js`). A page may add its own `<style>` block of at most
  ~40 lines for page-specific character.
- **A (very simple) design system** lives in `DESIGN.md`. Follow it.
- **English and Korean.** English is the default. Korean is a `ko.html` file
  next to each page's `index.html`, served at a clean `…/ko` URL by Cloudflare
  Pages (`/works/ecology/` ↔ `/works/ecology/ko`; the Korean landing is
  `/ko`). This layout is the owner's choice — do not restructure it into a
  `/ko/` directory tree. Every page links its counterpart (`hreflang`
  alternates + the header language toggle) and carries a self-referencing
  `rel=canonical` and `og:url`, absolute on `ORIGIN`. `og:image` is the page's
  own hero at the 1200 tier; pages without one (landing, list, CV) use the
  first work on the list, the exhibition page its first featured work.
  `sitemap.xml` is hand-written like everything else — add both URLs of a new
  page to it (`check-links.py` refuses to pass otherwise).
- **Hypermedia philosophy.** HATEOAS: every page reachable by links, navigation
  is plain `<a>`. Semantic HTML5 (`<article>`, `<figure>`, `<time>`, `<search>`,
  `rel="prev/next"`). Schema.org via Microdata (`VisualArtwork`, `Person`,
  `ExhibitionEvent`).
- **Use HTML to the fullest.** Prefer an HTML element or attribute over CSS,
  and CSS over JS. JS is a progressive enhancement only (the gallery
  search/filter, and the arrows and dots on the exhibition's phone photo strip
  — which swipes on its own, in CSS; the site works without either).
- **Images are always WebP**, responsive (`srcset` 480/640/960/1200/1600) with
  explicit `width`/`height` (no layout shift), `loading="lazy"` below the fold.
  `sizes` must state the *rendered* width, gutters subtracted — an overstated
  `sizes` silently ships the next tier up to every phone. When bytes need
  cutting, add a tier that fits rather than lowering quality: a retina desktop
  paints the 1600 file at roughly 1:1, so compression artefacts there are not
  hidden by downscaling. Quality stays at 82.
- **HTTP caching** is configured in `public/_headers`: immutable for a year on
  `/img/*`, a month for icons, an hour for CSS/JS, revalidate for HTML.
  Filenames are not fingerprinted, so the year on images is a promise —
  **replacing an artwork photo means a new filename**; the full warning lives
  in `scripts/build-images.sh`, where the replacing is done.
- **Web performance**: no webfonts (system stack), no external requests, tiny
  CSS/JS. `fetchpriority="high"` on a single hero image only — never on the
  masonry list, where the columns rebalance and no one item is the hero.
- **Installable, and no more than that.** A manifest and two PNG icons let a
  phone keep the site on its home screen and open it without browser chrome.
  That is the whole feature: no service worker, no offline cache, no JS — the
  site stays a set of pages the browser happens to be able to hold on to. There
  are two manifests for the same reason every page has a counterpart:
  installing from `/works/ko` must open at `/ko`, not at the English landing,
  so `ko.html` links `manifest.ko.webmanifest` and everything else links
  `manifest.webmanifest`. `theme_color`/`background_color` are the `--bg`
  token, matching each page's `theme-color` meta.

## Structure

```
public/                          ← Cloudflare Pages output directory
  index.html, ko.html            landing (EN/KO) — only the centered name, linking to /works/
  works/index.html, ko.html      gallery list — masonry + bottom search/filter bar
  works/<slug>/index.html, ko.html   one hand-made page per artwork
  cv/index.html, ko.html         the artist's CV (English on both pages) — also the first card on the list
  exhibitions/<name>/            self-contained exhibition mini-sites (see WORKS.md)
  css/site.css                   shared styles (design system)
  js/gallery.js                  search + tag filter for the list page (~50 lines)
  img/<slug>/{480,640,960,1200,1600}.webp  one folder per artwork (extra views: <slug>/view2-*.webp;
                                 a replaced photo carries a v2- version, <slug>/v2-*.webp for a hero and
                                 <slug>/view2-v2-*.webp for a view — see build-images.sh)
  manifest.webmanifest, manifest.ko.webmanifest   home-screen install (EN/KO)
  favicon.svg, icon-{192,512}.png   tab icon · app icon (scripts/build-icons.sh)
  sitemap.xml, robots.txt        every indexable page (EN + KO) with hreflang alternates
  _headers                       Cache-Control rules
scripts/                         pages.py (URL model) · build-images.sh · build-icons.sh · build-qr.py · serve.py · check-links.py
print/                           not served — QR codes for print (scripts/build-qr.py; SVG for print, PNG at 600 dpi, both 50 mm; -clear.png has no background)
```

## Content rules

- `WORKS.md` is the single source of truth for the works: slugs, titles,
  years, media, sizes, tags, and the curated order (= list-page order). It
  also documents the ORIGIN SEOUL 2026 exhibition mini-site.
- A work page says title, year, medium, size — **no descriptions**, by the
  artist's request (they live on Instagram), and **never invent a year, a
  title or a dimension**: the artist's Instagram captions are the source.
  Open items waiting on the owner live in `TODO.md` (kept in Korean,
  deliberately).
- Source photos live outside the repo in `../sangyu/arts`, one folder per
  work named by the artist in Korean (note the different spelling: `sangyu`,
  not `sangGyu`); the CV PDF is there too. `_old-2026-07/` holds the first
  photo set.

## Gotchas

- Desktop Chrome (including headless on this machine) enforces a ~500px
  minimum window width: a "390px mobile" screenshot silently renders a 500px
  viewport and can fake horizontal-overflow bugs. To verify real phone widths,
  load the page in a same-origin `<iframe>` of the target width instead.
