# Works — single source of truth

Order below = the artist's own order, newest first — the rows of their sheet
*작품들의 연결성* (2026-11-08) read bottom to top ("최신순, 관련작업에 쓰인
순서의 역순").
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
artist's own phrase for it in the Roadkill note of 2026-11-08 ("life imprinted
in negative" — a note since taken down), the other four plain
translations — and their medium is not known yet, so
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
- `mowing-the-lawn` leads with the artist's third photo, the hole seen from
  above (the owner, 2026-11-15); its hero and the two photos it moved down
  (`view2-v2-`, `view3-v2-`) carry v2-, since the first names had already
  gone out under the year-long cache.
- `a-new-number` is a PDF, not a photo: sixteen A4 pages of one number,
  "0.111…". Its page hangs the first page as the image and links the whole
  PDF under it (`public/works/a-new-number/a-new-number.pdf`, as sent).
- The artist's CV (`../proposal/arts/작가약력.pdf`) is `public/cv/` and the CV
  section of the exhibition page. The Korean CV the artist sent on 2026-11-27
  is `/cv/ko`, as sent (one misspelling corrected: 앤트워트 → 앤트워프), with
  the ORIGIN SEOUL 2026 line first as on the English page. The exhibition
  page's CV stays English in both languages: that page is the record of an
  exhibition that is over.

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
there and nowhere else on the list; the rest follow in the order above.
`check-links.py` holds the list to this table.

| pinned |
|---|
| beyond-the-predetermined |
| highway-vanishing-point |
| brave-new-world |
| the-narrow-gate |
| ecology |

## Themes

The artist's seven themes, sent through the owner on 2026-11-27 (*웹 사이트
희망 수정 방안*: the sheet *작품들의 연결성* redrawn, the notes rewritten, a
hand-drawn map of how the themes hang together). They replace the five of
2026-11-22 and every tag before them ("기존 작품들 테그들은 삭제하기"):
기본 기하적 형태와 유기적 형태 is gone, 부정성, 흔적 and 폐허와 잔해 are new.

The themes are a tree, as the artist drew it (the "under" column). The rows
below are that tree read top to bottom in the hand-drawn order, which puts
소실점 above 부정성 where the typed list beside it has them the other way
round (the owner chose the drawing, 2026-11-27). Each theme is three things,
all in this order:

- a branch of the tree on `/notes/`, named as its "tag", linking to
- the theme's own page (`/notes/<theme>/`): the artist's note under the
  "note" heading, and under the text the works the sheet marks with the
  theme, as the list's cards, newest first as in the works table — the pins
  are the list's alone ("각 항목 밑에 작품 네모 사진 있어서 클릭하면 작품으로
  이동");
- a tag on each work page it marks, under the tombstone, named as in the
  "tag" columns, linking to the note's page.

`check-links.py` holds the tree, the tags and each note's works to the two
tables below. The names are the artist's headings; the one tag shorter than
its note is 부정성 (the note is 부정성과 동일성), and its English, *Negativity*,
is that shortening of *Negativity and Identity* (TODO.md).

| theme | under | tag (EN) | tag (KO) | note (EN) | note (KO) |
|---|---|---|---|---|---|
| residual-sensation | | Residual Sensation | 잔여적 감각 | Residual Sensation | 잔여적 감각 |
| vanishing-point | residual-sensation | Vanishing Point | 소실점 | Vanishing Point | 소실점 |
| negativity | residual-sensation | Negativity | 부정성 | Negativity and Identity | 부정성과 동일성 |
| trace | negativity | Trace | 흔적 | Trace | 흔적 |
| intaglio | negativity | Intaglio | 음각 | Intaglio | 음각 |
| oxidation | negativity | Oxidation | 산화 | Oxidation | 산화 |
| ruins-and-remnants | negativity | Ruins and Remnants | 폐허와 잔해 | Ruins and Remnants | 폐허와 잔해 |

The marks are the sheet's of 2026-11-27 (● only), its columns put in the
order above. It marks no work with 흔적 or 음각 — not even 음각된 — so those
two notes stand alone; that is the artist's to fill (TODO.md), not ours.

| work | residual-sensation | vanishing-point | negativity | trace | intaglio | oxidation | ruins-and-remnants |
|---|---|---|---|---|---|---|---|
| highway-vanishing-point | ● | ● | | | | ● | |
| imprinted-in-negative | ● | | ● | | | | ● |
| the-narrow-gate | ● | ● | ● | | | ● | ● |
| beyond-the-predetermined | ● | | ● | | | ● | ● |
| oxidized-figures-10 | ● | | ● | | | ● | ● |
| oxidized-figures-6 | ● | | ● | | | ● | ● |
| oxidized-figures-5 | ● | | ● | | | ● | ● |
| oxidized-figures-3 | ● | | ● | | | ● | ● |
| oxidized-figures-2 | ● | | ● | | | ● | ● |
| self-portrait | ● | | | | | | |
| mowing-the-lawn | ● | | ● | | | | |
| a-face | ● | | | | | | |
| collective-gaze | ● | | | | | | |
| the-stranger | ● | | | | | | |
| arhats-little-beings | ● | | | | | | |
| the-pool-of-two-worlds | ● | | | | | | |
| a-new-number | ● | | | | | | |
| brave-new-world | ● | | | | | | |
| ecology | ● | | ● | | | | |
| combustion | ● | | ● | | | | |
| untitled | ● | | | | | | |
| a-cushion | ● | | | | | | |

How the sheet's rows map onto the site:

- "산화연작#, 2026" is one row for the five *Open Lack – Oxidized Figures*.
- The sheet names some works differently from the site: 집단응시 is
  `collective-gaze` (응시), 작은 존재–나한들 is `arhats-little-beings`,
  고속도로 소실점 is `highway-vanishing-point` (고속도로 위 소실점 — the
  artist's folder and message). It has The Stranger as "이방인, 2023" again
  — see TODO.md.
- Three works on the site are not on the sheet and carry no theme: `a-hand`,
  `skull`, `abstract-body-3`. Cock and Imagine 재구성, on the sheet of
  2026-11-08 but never sent, are not on this one either (TODO.md).

## Notes

`/notes/` is the artist's own writing: the seven notes as the tree above, each
branch its own page — in English on the English pages and in Korean on the
Korean ones, the artist wrote both — and the title of their thesis last, with
the thesis itself as a PDF under it
(`public/notes/the-sacred-in-a-godless-age.pdf` — the file the artist sent,
2026-11-13, published as sent at the owner's word: its cover carries the
student number, and its declaration pages the signatures of the artist and
three advisors). The artist asked for a page per note (2026-11-09) and for the
map that leads to them (2026-11-27: "마인드맵 같은 느낌으로 … 글자 누르면 안으로
들어가서 작가노트 보이게"). A note's page is its text, then the works the
sheet marks with its theme (see "Themes"). It is the one place on the site
with the artist's words about the work; a work page still says only title,
year, medium and size, with its themes as links to these notes.

The text is the artist's, as sent on 2026-11-27 (a blank line in it is a new
paragraph). Only plain misspellings are corrected — two missing or doubled
word spaces in the Korean, 흔적: "왔다간" → "왔다 간", "제시하지않고" →
"제시하지 않고" — and anything less certain stays as written and goes to
TODO.md. The notes they replaced are in the git history (before 2026-11-27).
