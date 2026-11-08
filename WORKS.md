# Works — single source of truth

Order below = curated order on the list page: the artist's own order, newest
first — the rows of their sheet *작품들의 연결성* (2026-11-08) read bottom to
top, which is also how each note on `/notes/` hangs its works ("최신순, 관련작업에
쓰인 순서의 역순"). Works the sheet leaves out sit at the end of their year. The
one exception is the 2024 study, which sits last — the list's three columns
fill top to bottom, so the work about two-thirds down the order heads the third
column on a desktop, and a study should not. A work page links back to that
list and nowhere else, so this file is the only place the order is kept.

Titles, years, media and sizes are the artist's captions on Instagram
(@s_an9_9_artworksofarts), checked against the photo folders the artist sent
in August 2026 (`../sangyu/arts/<Korean folder name>/`). The Korean titles are
the artist's folder names. Work pages carry only title, year, medium and size —
no descriptions, by the artist's request.

| slug | title (EN) | title (KO) | year | medium | size | photos |
|---|---|---|---|---|---|---|
| beyond-the-predetermined | Beyond the Predetermined | 폐허풍경 | 2026 | Plaster, metal powder | 200 × 200 × 200 cm | 10 |
| oxidized-figures-10 | Open Lack – Oxidized Figures #10 | 산화형상 #10 | 2026 | Plaster, metal powder | 17 × 15 × 77 cm | 6 |
| oxidized-figures-6 | Open Lack – Oxidized Figures #6 | 산화형상 #6 | 2025 | Plaster, metal powder | 10 × 10 × 30 cm | 6 |
| oxidized-figures-5 | Open Lack – Oxidized Figures #5 | 산화형상 #5 | 2025 | Plaster, metal powder | 15 × 10 × 34 cm | 6 |
| oxidized-figures-3 | Open Lack – Oxidized Figures #3 | 산화형상 #3 | 2025 | Plaster, metal powder | 8 × 9 × 30 cm | 6 |
| oxidized-figures-2 | Open Lack – Oxidized Figures #2 | 산화형상 #2 | 2025 | Plaster, metal powder | 7 × 9 × 20 cm | 6 |
| self-portrait | Self-Portrait | 자소상 | 2025 | Plaster, animal horn | 40 × 20 × 40 cm | 4 |
| a-face | A Face | 얼굴 | 2025 | Ceramic | 20 × 20 × 20 cm | 3 |
| collective-gaze | Collective Gaze | 응시 | 2025 | Glazed ceramic | 40 × 40 × 80 cm | 9 |
| the-stranger | The Stranger | 이방인 | 2025 | Glazed ceramic | 30 × 20 cm | 3 |
| arhats-little-beings | Arhats – Little Beings | 나한들 – 작은 존재들 | 2025 | Glazed ceramic | Dimensions variable | 5 |
| the-pool-of-two-worlds | The Pool of Two Worlds | 두 세개의 연못 | 2025 | Plaster on wood panel | 30 × 30 × 50 cm | 6 |
| a-hand | A Hand | 손 | 2025 | Ceramic | 25 × 9 × 4 cm | 3 |
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

The list page opens with three text cards, in the order of the artist's
sketch (2026-11-08): the CV, the notes (`/notes/`), then the exhibition; the
works follow.

## Themes

The artist's eight themes are the headings of their notes, from *작품들의
연결성* (2026-11-08). It replaces the four-theme sheet of 2026-09-11, and its
산화 takes over from the 산화연작 series chip, which found the same works (the
owner, 2026-11-08). Each theme is three things, all in the order below — the
artist's order of the notes:

- a note on `/notes/` (`<article id="<theme>">`), the artist's text under the
  "note" heading, followed by the works it marks that are on the site, in the
  list order above;
- a filter chip on the list page, named as in the "chip" columns. A chip is
  offered only once the theme marks a work on the site — one that finds
  nothing is not a filter;
- a tag on each work page it marks, under the tombstone, with the chip's name,
  linking to the note.

Cards carry their themes as `data-themes`, by hand in both locales;
`check-links.py` holds cards, chips, tags and notes to the two tables below.
The English chip names are the artist's headings except *Geometric & Organic*,
a short form of the longest (a draft — TODO.md).

| theme | chip (EN) | chip (KO) | note (EN) | note (KO) |
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
| beyond-the-predetermined | | | | ● | ● | ● | | |
| oxidized-figures-10 | | | | ● | | | | |
| oxidized-figures-6 | | | | ● | | | | |
| oxidized-figures-5 | | | | ● | | | | |
| oxidized-figures-3 | | | | ● | | | | |
| oxidized-figures-2 | | | | ● | | | | |
| self-portrait | | | | | ● | ● | ● | ● |
| a-face | | | | | ● | ● | | |
| collective-gaze | | | | | | ● | ● | ● |
| the-stranger | | | | | | | ● | ● |
| arhats-little-beings | | | | | ● | | | ● |
| the-pool-of-two-worlds | | | | | ● | | | |
| brave-new-world | | | | | | ● | ● | ● |
| ecology | | | | | | ● | ● | ● |
| combustion | | | | | ● | ● | | |
| untitled | | | | | ● | | ● | |
| a-cushion | | | | | | ● | ● | |

How the sheet's rows map onto the site:

- "산화연작#, 2026" is one row for the five *Open Lack – Oxidized Figures*.
- The sheet names some works differently from the site: 집단응시 is
  `collective-gaze` (응시), 작은 존재–나한들 is `arhats-little-beings`. It has
  The Stranger as "이방인, 2023" again — see TODO.md.
- 작은 존재–나한들 is ● under 시스템 on the sheet but missing from the 시스템
  note's own list of related works; the site follows the sheet (TODO.md).
- Three works on the site are not on the sheet — `a-hand`, `skull`,
  `abstract-body-3` — so they carry no theme and show under All only. 불상 and
  돌도끼 만들기, on the old sheet, are not on this one.

Works on the sheet that are not on the site yet — the artist is sending their
photos. Each becomes a row of both tables above once it has a page; the
themes no site work marks yet (기하와 유기 형태, 소실점, 로드킬) get their chips
with them. Titles here are the sheet's; the English ones, and media and sizes,
come from the Instagram captions as for every other work.

| 작품 (not on the site yet) | year | themes |
|---|---|---|
| 고속도로 소실점 | 2026 | geometric-and-organic-forms, vanishing-point, residual-sensation, irreducibility |
| 음각된 | 2026 | geometric-and-organic-forms, roadkill, residual-sensation, irreducibility |
| 좁은 문 | 2026 | geometric-and-organic-forms, vanishing-point, oxidation, residual-sensation, irreducibility |
| Cock | 2025 | irreducibility, analysis-and-deconstruction, systems |
| 잔디 자르기 | 2025 | irreducibility, analysis-and-deconstruction, systems |
| 새로운 수 | 2024 | analysis-and-deconstruction, systems |
| Imagine 재구성 | 2023 | residual-sensation, irreducibility, analysis-and-deconstruction, systems |

## Notes

`/notes/` is the artist's own writing, from the same file: the eight notes in
the order above, each in English on the English page and in Korean on the
Korean page — the artist wrote both — and the title of their thesis last (its
PDF is still to come). It is the one place on the site with the artist's words
about the work; a work page still says only title, year, medium and size, with
its themes as links to these notes. The text is the artist's, line for line
(a blank line in the file is a new paragraph, a line break inside one is a
`<br>`); only plain misspellings are corrected — 맡닿음 → 맞닿음, 엔디 워홀 →
앤디 워홀 — and anything less certain stays as written and goes to TODO.md.
