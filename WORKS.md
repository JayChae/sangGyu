# Works — single source of truth

Order below = curated order on the list page: the artist's own order (newest
first, as on Instagram), except that the 2024 study sits last — the list's
three columns fill top to bottom, so the work about two-thirds down the order
heads the third column on a desktop, and a study should not. A work page links back to that list and nowhere else,
so this file is the only place the order is kept.

Titles, years, media and sizes are the artist's captions on Instagram
(@s_an9_9_artworksofarts), checked against the photo folders the artist sent
in August 2026 (`../sangyu/arts/<Korean folder name>/`). The Korean titles are
the artist's folder names. Work pages carry only title, year, medium and size —
no descriptions, by the artist's request.

| slug | title (EN) | title (KO) | year | medium | size | tags | photos |
|---|---|---|---|---|---|---|---|
| beyond-the-predetermined | Beyond the Predetermined | 폐허풍경 | 2026 | Plaster, metal powder | 200 × 200 × 200 cm | installation | 10 |
| oxidized-figures-10 | Open Lack – Oxidized Figures #10 | 산화형상 #10 | 2026 | Plaster, metal powder | 17 × 15 × 77 cm | sculpture | 6 |
| oxidized-figures-6 | Open Lack – Oxidized Figures #6 | 산화형상 #6 | 2025 | Plaster, metal powder | 10 × 10 × 30 cm | sculpture | 6 |
| oxidized-figures-5 | Open Lack – Oxidized Figures #5 | 산화형상 #5 | 2025 | Plaster, metal powder | 15 × 10 × 34 cm | sculpture | 6 |
| oxidized-figures-3 | Open Lack – Oxidized Figures #3 | 산화형상 #3 | 2025 | Plaster, metal powder | 8 × 9 × 30 cm | sculpture | 6 |
| oxidized-figures-2 | Open Lack – Oxidized Figures #2 | 산화형상 #2 | 2025 | Plaster, metal powder | 7 × 9 × 20 cm | sculpture | 6 |
| collective-gaze | Collective Gaze | 응시 | 2025 | Glazed ceramic | 40 × 40 × 80 cm | ceramic | 9 |
| the-stranger | The Stranger | 이방인 | 2025 | Glazed ceramic | 30 × 20 cm | ceramic | 3 |
| self-portrait | Self-Portrait | 자소상 | 2025 | Plaster, animal horn | 40 × 20 × 40 cm | sculpture | 4 |
| arhats-little-beings | Arhats – Little Beings | 나한들 – 작은 존재들 | 2025 | Glazed ceramic | Dimensions variable | ceramic | 5 |
| a-hand | A Hand | 손 | 2025 | Ceramic | 25 × 9 × 4 cm | ceramic | 3 |
| the-pool-of-two-worlds | The Pool of Two Worlds | 두 세개의 연못 | 2025 | Plaster on wood panel | 30 × 30 × 50 cm | sculpture | 6 |
| a-face | A Face | 얼굴 | 2025 | Ceramic | 20 × 20 × 20 cm | ceramic | 3 |
| brave-new-world | Brave New World | 멋진 신세계 | 2023 | Plastic resin, acrylic | Dimensions variable | installation | 8 |
| ecology | Ecology | 생태 | 2023 | Ceramic | 30 × 30 × 25 cm | ceramic | 6 |
| combustion | Combustion | 연소 | 2023 | Etching | 21 × 15 cm | print | 1 |
| untitled | Untitled | 무제 | 2023 | Lithograph | 20 × 20 cm | print | 1 |
| skull | Skull | 해골 | 2023 | Lithograph | 30 × 40 cm | print | 7 |
| a-cushion | A Cushion | 쿠션 | 2022 | Granite, marble | 22 × 22 × 10 cm | sculpture | 3 |
| abstract-body-3 | Study of Abstract Body #3 | 추상인체 | 2024 | Wood panel, plaster, acrylic | 60 × 90 × 55 cm | sculpture | 3 |

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
printed next to the works at ORIGIN SEOUL 2026 (Aug 31 – Sep 2, 2026, Seoul —
originseoulbtc.com). One QR → artist intro (name, bio, link to this site) + both featured works
(Ecology and The Stranger) + the CV + a "Collect" section that links to Telegram.
Everything on it is written through a Bitcoin lens: peer to peer, bitcoin
only, no prices anywhere. The two work descriptions there are the exhibition's
wall texts and stay — the work pages themselves carry none.

The artist's CV card is the first card on the works list page, the exhibition
the second; the works follow.
