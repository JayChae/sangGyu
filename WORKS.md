# Works — single source of truth

Order below = the artist's own order, newest first — the rows of their sheet
*작품들의 연결성* (2026-11-08) read bottom to top, which is how each note's
page under `/notes/` hangs its works ("최신순, 관련작업에 쓰인 순서의 역순").
Works the sheet leaves out sit at the end of their year. The one exception is
the 2024 study, which sits last — the list's columns fill top to bottom, so a
work from late in the order heads a column on a desktop, and a study should
not. The list page shows the same order with the artist's pinned works taken
out and hung first (see "Pinned" below). A work page links back to that list
and nowhere else, so this file is the only place the order is kept.

Titles, years, media and sizes are the artist's captions on Instagram
(@s_an9_9_artworksofarts), checked against the photo folders the artist sent
in August 2026 (`../proposal/arts/<Korean folder name>/`). The Korean titles are
the artist's folder names. Work pages carry only title, year, medium and size —
no descriptions, by the artist's request.

The five works sent on 2026-11-13 are not on Instagram (its newest twelve
posts, April–June 2026, are other works, and older posts no longer show
without logging in), so for them the sources are the artist's own: the year in
their folder name, the size in the artist's message of that day, the Korean
title from the sheet. Their English titles are **drafts** — 음각된's is the
artist's own phrase for it in the Roadkill note ("life imprinted in negative"),
the other four plain translations — and their medium is not known yet, so
their pages leave it out (— below). Both wait for the artist (TODO.md).

| slug | title (EN) | title (KO) | year | medium | size | photos |
|---|---|---|---|---|---|---|
| highway-vanishing-point | Highway Vanishing Point | 고속도로 위 소실점 | 2026 | — | 60 × 4 × 30 cm | 2 |
| imprinted-in-negative | Imprinted in Negative | 음각된 | 2026 | — | Dimensions variable | 3 |
| the-narrow-gate | The Narrow Gate | 좁은 문 | 2026 | — | 50 × 15 × 200 cm, 70 × 70 × 70 cm | 4 |
| beyond-the-predetermined | Beyond the Predetermined | 폐허풍경 | 2026 | Plaster, metal powder | 200 × 200 × 200 cm | 10 |
| oxidized-figures-10 | Open Lack – Oxidized Figures #10 | 산화형상 #10 | 2026 | Plaster, metal powder | 17 × 15 × 77 cm | 6 |
| oxidized-figures-6 | Open Lack – Oxidized Figures #6 | 산화형상 #6 | 2025 | Plaster, metal powder | 10 × 10 × 30 cm | 6 |
| oxidized-figures-5 | Open Lack – Oxidized Figures #5 | 산화형상 #5 | 2025 | Plaster, metal powder | 15 × 10 × 34 cm | 6 |
| oxidized-figures-3 | Open Lack – Oxidized Figures #3 | 산화형상 #3 | 2025 | Plaster, metal powder | 8 × 9 × 30 cm | 6 |
| oxidized-figures-2 | Open Lack – Oxidized Figures #2 | 산화형상 #2 | 2025 | Plaster, metal powder | 7 × 9 × 20 cm | 6 |
| self-portrait | Self-Portrait | 자소상 | 2025 | Plaster, animal horn | 40 × 20 × 40 cm | 4 |
| mowing-the-lawn | Mowing the Lawn | 잔디 자르기 | 2025 | — | 20 × 20 × 10 cm | 4 |
| a-face | A Face | 얼굴 | 2025 | Ceramic | 20 × 20 × 20 cm | 3 |
| collective-gaze | Collective Gaze | 응시 | 2025 | Glazed ceramic | 40 × 40 × 80 cm | 9 |
| the-stranger | The Stranger | 이방인 | 2025 | Glazed ceramic | 30 × 20 cm | 3 |
| arhats-little-beings | Arhats – Little Beings | 나한들 – 작은 존재들 | 2025 | Glazed ceramic | Dimensions variable | 5 |
| the-pool-of-two-worlds | The Pool of Two Worlds | 두 세개의 연못 | 2025 | Plaster on wood panel | 30 × 30 × 50 cm | 6 |
| a-hand | A Hand | 손 | 2025 | Ceramic | 25 × 9 × 4 cm | 3 |
| a-new-number | A New Number | 새로운 수 | 2024 | — | Dimensions variable | PDF |
| brave-new-world | Brave New World | 멋진 신세계 | 2023 | Plastic resin, acrylic | Dimensions variable | 8 |
| ecology | Ecology | 생태 | 2023 | Ceramic | 30 × 30 × 25 cm | 6 |
| combustion | Combustion | 연소 | 2023 | Etching | 21 × 15 cm | 1 |
| untitled | Untitled | 무제 | 2023 | Lithograph | 20 × 20 cm | 1 |
| skull | Skull | 해골 | 2023 | Lithograph | 30 × 40 cm | 7 |
| a-cushion | A Cushion | 쿠션 | 2022 | Granite, marble | 22 × 22 × 10 cm | 3 |
| abstract-body-3 | Study of Abstract Body #3 | 추상인체 | 2024 | Wood panel, plaster, acrylic | 60 × 90 × 55 cm | 3 |

Notes:

- Every photo the artist sent is on the site: the hero plus `view2-`,
  `view3-`… in `public/img/<slug>/`, in the order of the artist's folder
  (the "photos" column). `scripts/build-images.sh` says which source photo
  each file is.
- `beyond-the-predetermined`, `collective-gaze`, `the-stranger` and
  `untitled` kept their slug but their hero is a different photo or crop
  from the 2026-07 set, so those hero files are `v2-*.webp` (`/img/*` is
  cached immutable — see CLAUDE.md). `brave-new-world`, `ecology` and
  `a-cushion` kept the same hero photo, re-encoded from the larger original.
- `brave-new-world`'s 2nd, 4th and 8th photos are portrait shots the phone
  stored landscape, with an EXIF orientation tag saying to turn them — a tag
  cwebp ignores, so they first shipped sideways. `build-images.sh` now turns
  the pixels itself; the upright files are `view{2,4,8}-v2-*.webp`.
- Renamed in that update: the head with the tongue was "Untitled" and is now
  **A Face** (`a-face`); `untitled` is now the 2023 lithograph. The
  "산화형상" series is titled *Open Lack – Oxidized Figures #N*. "The Stranger
  (Triptych)" is now just *The Stranger* (three glazed ceramic reliefs, 2025 —
  Instagram also lists a 2023 plaster relief of the same name, 34 × 24 cm,
  which is not on the site). *A Cushion* is granite and marble (2022), not
  ceramic.
- `oxidized-figures-2`'s photos are 1546/1506 px wide, so it has no 1600 tier.
- The 2026-11-13 works came as folders named "<title>-<year>"
  (`../proposal/arts/고속도로 위 소실점-2026/` …), kept as sent. 음각된's
  folder is "로드킬-2026" — the theme's name; the work's title is the sheet's
  (the owner, 2026-11-13). `the-narrow-gate` is two pieces, the arch
  (50 × 15 × 200 cm) and the cube (70 × 70 × 70 cm); its first photo came
  with a white band along the top and bottom, which `build-images.sh` trims
  off (the band only, not the room).
- `a-new-number` is a PDF, not a photo: sixteen A4 pages of one number,
  "0.111…". Its page hangs the first page as the image and links the whole
  PDF under it (`public/works/a-new-number/a-new-number.pdf`, as sent).
- The artist's CV (`../sangyu/arts/작가약력.pdf`) is `public/cv/` and the CV
  section of the exhibition page. It is English on the Korean pages too —
  the owner's choice — so there is nothing to translate.

## ORIGIN SEOUL 2026 (exhibition mini-site)

`/exhibitions/origin-seoul-2026/` is the page behind the single QR code
(`print/qr-exhibitions-origin-seoul-2026.svg`, made by `scripts/build-qr.py`,
pointing at the English page) printed next to the works at ORIGIN SEOUL 2026 (Aug 31 – Sep 2, 2026, Seoul —
originseoulbtc.com). One QR → artist intro (name, bio, link to this site) + both featured works
(Ecology and The Stranger) + a "Collect" section that links to Telegram
(@TH4NK_YOU) + the CV last.
Everything on it is written through a Bitcoin lens: peer to peer, bitcoin
only, no prices anywhere. The two work descriptions there are the exhibition's
wall texts and stay — the work pages themselves carry none.
The Stranger is three reliefs, so it is shown there as three plates: on a
phone one swipeable strip with arrows and dots, wider the first leading
with the other two side by side under it.

The exhibition is over, so the list carries no card for it: it is the first
of the CV's group exhibitions, linking the mini-site, and the QR printed for
it still lands there (the artist, 2026-11-10).

## Pinned

The artist's pinned works, first on the list page in this order, before
everything else (the artist, 2026-11-13: "위에 맨 먼저 보이게 고정"). They hang
there and nowhere else on the list; the rest follow in the order above. A
note's page keeps the order above — pinning is the list's alone.
`check-links.py` holds the list to this table.

| pinned |
|---|
| beyond-the-predetermined |
| highway-vanishing-point |
| brave-new-world |
| the-narrow-gate |
| ecology |

## Themes

The artist's eight themes are the headings of their notes, from *작품들의
연결성* (2026-11-08), which replaces the four-theme sheet of 2026-09-11. Each
theme is two things, both in the order below — the artist's order of the
notes:

- a note: a bar on `/notes/` named by the "note" heading, leading to the
  theme's own page (`/notes/<theme>/`) — the artist's text under that
  heading, then the works it marks that are on the site, as cards in the list
  order above;
- a tag on each work page it marks, under the tombstone, named as in the
  "tag" columns, linking to the note's page.

`check-links.py` holds tags and notes to the two tables below. The English
tag names are the artist's headings except *Geometric & Organic*, a short
form of the longest (a draft — TODO.md).

| theme | tag (EN) | tag (KO) | note (EN) | note (KO) |
|---|---|---|---|---|
| geometric-and-organic-forms | Geometric & Organic | 기하와 유기 형태 | Basic Geometric Forms and Organic Forms | 기본 기하적 형태와 유기적 형태 |
| vanishing-point | Vanishing Point | 소실점 | Vanishing Point | 소실점 |
| roadkill | Roadkill | 로드킬 | Roadkill | 로드킬 |
| oxidation | Oxidation | 산화 | Oxidation | 산화 |
| residual-sensation | Residual Sensation | 잔여적 감각 | Residual Sensation | 잔여적 감각 |
| irreducibility | Irreducibility | 환원불가능성 | Irreducibility | 환원불가능성 |
| analysis-and-deconstruction | Analysis and Deconstruction | 분석, 해체 | Analysis and Deconstruction | 분석, 해체 |
| systems | Systems | 시스템 | Systems | 시스템 |

The sheet, for the works on the site (● only — it has no "related" mark):

| work | geometric-and-organic-forms | vanishing-point | roadkill | oxidation | residual-sensation | irreducibility | analysis-and-deconstruction | systems |
|---|---|---|---|---|---|---|---|---|
| highway-vanishing-point | ● | ● | | | ● | ● | | |
| imprinted-in-negative | ● | | ● | | ● | ● | | |
| the-narrow-gate | ● | ● | | ● | ● | ● | | |
| beyond-the-predetermined | | | | ● | ● | ● | | |
| oxidized-figures-10 | | | | ● | | | | |
| oxidized-figures-6 | | | | ● | | | | |
| oxidized-figures-5 | | | | ● | | | | |
| oxidized-figures-3 | | | | ● | | | | |
| oxidized-figures-2 | | | | ● | | | | |
| self-portrait | | | | | ● | ● | ● | ● |
| mowing-the-lawn | | | | | | ● | ● | ● |
| a-face | | | | | ● | ● | | |
| collective-gaze | | | | | | ● | ● | ● |
| the-stranger | | | | | | | ● | ● |
| arhats-little-beings | | | | | ● | | | ● |
| the-pool-of-two-worlds | | | | | ● | | | |
| a-new-number | | | | | | | ● | ● |
| brave-new-world | | | | | | ● | ● | ● |
| ecology | | | | | | ● | ● | ● |
| combustion | | | | | ● | ● | | |
| untitled | | | | | ● | | ● | |
| a-cushion | | | | | | ● | ● | |

How the sheet's rows map onto the site:

- "산화연작#, 2026" is one row for the five *Open Lack – Oxidized Figures*.
- The sheet names some works differently from the site: 집단응시 is
  `collective-gaze` (응시), 작은 존재–나한들 is `arhats-little-beings`,
  고속도로 소실점 is `highway-vanishing-point` (고속도로 위 소실점 — the
  artist's folder and message). It has
  The Stranger as "이방인, 2023" again — see TODO.md.
- 작은 존재–나한들 is ● under 시스템 on the sheet but missing from the 시스템
  note's own list of related works; the site follows the sheet (TODO.md).
- Three works on the site are not on the sheet — `a-hand`, `skull`,
  `abstract-body-3` — so they carry no theme and are on no note's page.

Works on the sheet that are not on the site yet — the artist has not sent
their photos. Each becomes a row of both tables above once it has a page.
Titles here are the sheet's; the English ones, and media and sizes, come from
the Instagram captions as for every other work. `check-links.py` holds the
themes column to the theme keys above.

| 작품 (not on the site yet) | year | themes |
|---|---|---|
| Cock | 2025 | irreducibility, analysis-and-deconstruction, systems |
| Imagine 재구성 | 2023 | residual-sensation, irreducibility, analysis-and-deconstruction, systems |

## Notes

`/notes/` is the artist's own writing, from the same file: the eight notes in
the order above, as bars, each its own page — in English on the English pages
and in Korean on the Korean ones, the artist wrote both — and the title of
their thesis last, with the thesis itself as a PDF under it
(`public/notes/the-sacred-in-a-godless-age.pdf` — the file the artist sent,
2026-11-13, published as sent at the owner's word: its cover carries the
student number, and its declaration pages the signatures of the artist and
three advisors). The artist asked for the bars
and the pages, with each note's works shown as photos like the list
(2026-11-09). It is the one place on the site with the artist's words
about the work; a work page still says only title, year, medium and size, with
its themes as links to these notes. The text is the artist's, line for line
(a blank line in the file is a new paragraph, a line break inside one is a
`<br>`); only plain misspellings are corrected — 맡닿음 → 맞닿음, 엔디 워홀 →
앤디 워홀 — and anything less certain stays as written and goes to TODO.md.
