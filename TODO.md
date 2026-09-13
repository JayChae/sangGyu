# TODO

사이트 주인이 채워 줘야 진행되는 항목들.

## 콘텐츠

- [ ] **한국어 작품 제목 확인** — 작가가 보낸 폴더 이름을 그대로 썼음.
      인스타 영문 제목과 다른 것들: 폐허풍경 (Beyond the Predetermined),
      산화형상 #N (Open Lack – Oxidized Figures #N), 추상인체 (Study of
      Abstract Body #3), 두 세개의 연못 (The Pool of Two Worlds).
      작가의 주제 분류표(2026-09-11)에는 또 다르게 적혀 있음: 두 개의 못
      (사이트: 두 세개의 연못), 집단응시 (응시), 작은 존재–나한들
      (나한들 – 작은 존재들).
- [ ] **주제·연작 영문 이름** — 목록 페이지 필터가 된 작가의 네 주제를 영어로
      옮긴 건 초안 (WORKS.md): Social Structure · Logic · Discipline,
      Dismantling, Residue · Sense · Spirit, Irreducibility · Contradiction ·
      Ambivalence. 산화연작 칩은 Oxidized Figures.
- [ ] **이방인 연도** — 분류표에는 "이방인, 2023"인데 사이트의 이방인은 2025년
      도자 부조 세 점 (2023년 석고 부조는 사이트에 없음). 일단 사이트의
      이방인에 분류표의 주제를 붙였음 — 어느 작품을 말한 건지 확인.
- [ ] **연소 (Combustion)** — 인스타 캡션은 "에칭, 21 × 15 cm"인데 보내준 사진은
      동판 원판으로 보임. 이 사진을 쓰는 게 맞는지 확인.
- [ ] **두 세개의 연못** — 폴더에 있던 건축 렌더링·다이어그램 PNG 4장은 UI가
      찍힌 화면 캡처라 싣지 않았음. 싣고 싶으면 깨끗한 이미지로 다시 받을 것.
- [ ] **전시장 내 정확한 위치** — ORIGIN SEOUL 2026 안 몇 층/어느 공간인지

## 설정

- [ ] **커스텀 도메인** — 지금은 `https://sanggyu.pages.dev` 기준으로
      canonical/hreflang/og:url/og:image/sitemap 이 모두 절대경로임. 도메인이
      바뀌면 `scripts/pages.py` 의 `ORIGIN` 을 고치고 `public/` 전체에서
      옛 주소를 새 주소로 일괄 치환 (전시 페이지 작가 소개의 링크 문구 포함).
