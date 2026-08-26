#!/usr/bin/env python3
"""The test suite. It asserts the invariants this hand-written site rests on:

1. every internal href/src/srcset resolves to a real file, the way Cloudflare
   Pages would serve it;
2. every page claims its own absolute URL as canonical and og:url, points
   its hreflang alternates and its language toggle at itself and its
   counterpart, and names an og:image that exists; sitemap.xml lists exactly
   the indexable pages;
3. WORKS.md really is the source of truth — the works on disk are exactly the
   works in the table, and both list pages walk them in the table's order. A
   work page leads back to the list and nowhere else: no prev/next chain.
4. a plates strip carries one dot per photo, in both locales.

Checks 2 and 3 exist because the only authoring method here is copy-paste-then-
translate, whose usual failure is a stale-but-valid URL: it resolves, so check 1
alone reports OK while the Korean page canonicalises to a different artwork.
Nothing is generated — the pages stay hand-written; this only refuses to let
the copies drift. Exits 1 on any failure.
"""
import re
import sys
from pathlib import Path

from pages import ORIGIN, ROOT, counterpart, exists, route, url_of

REPO = ROOT.parent
errors = []
pages = sorted(ROOT.rglob("*.html"))


def check(page, condition, message):
    if not condition:
        errors.append(f"{page.relative_to(ROOT)}: {message}")


def attr(html, pattern):
    """The single capture of `pattern`, or None if it is absent."""
    found = re.findall(pattern, html)
    return found[0] if len(found) == 1 else None


# ── 1. every internal link resolves ──────────────────────────────

for page in pages:
    html = page.read_text(encoding="utf-8")
    urls = re.findall(r'(?:href|src)="([^"]+)"', html)
    for srcset in re.findall(r'srcset="([^"]+)"', html):
        urls += [p.strip().split()[0] for p in srcset.split(",") if p.strip()]
    for url in urls:
        if url.startswith(ORIGIN + "/"):  # our own absolute URLs are internal
            url = url[len(ORIGIN):]
        if url.startswith(("http://", "https://", "data:", "mailto:", "#")):
            continue
        if not url.split("#")[0].split("?")[0]:
            continue
        check(page, exists(route(url, base=page.parent)), f"broken {url}")

# ── 2. each page points at itself and its counterpart ────────────

for page in pages:
    if page.name == "404.html":  # noindex, no counterpart, no alternates
        continue
    html = page.read_text(encoding="utf-8")
    own, other = url_of(page), url_of(counterpart(page))
    en, ko = (own, other) if page.name == "index.html" else (other, own)
    own, en, ko = ORIGIN + own, ORIGIN + en, ORIGIN + ko

    check(page, exists(counterpart(page)), f"no counterpart {counterpart(page).name}")
    check(page, attr(html, r'<html lang="([^"]+)"') ==
          ("ko" if page.name == "ko.html" else "en"), "wrong <html lang>")
    check(page, attr(html, r'<link rel="canonical" href="([^"]+)"') == own,
          f"canonical must be {own}")
    check(page, attr(html, r'<link rel="alternate" hreflang="en" href="([^"]+)"') == en,
          f"hreflang=en must be {en}")
    check(page, attr(html, r'<link rel="alternate" hreflang="ko" href="([^"]+)"') == ko,
          f"hreflang=ko must be {ko}")
    check(page, attr(html, r'<meta property="og:url" content="([^"]+)"') == own,
          f"og:url must be {own}")
    image = attr(html, r'<meta property="og:image" content="([^"]+)"')
    check(page, image and image.startswith(ORIGIN + "/img/")
          and exists(route(image[len(ORIGIN):])), f"og:image {image} must be ours")
    toggle = attr(html, r'<a class="lang"[^>]*?href="([^"]+)"')
    check(page, toggle is None or toggle == other,
          f"language toggle must point at {other}")

# sitemap.xml names every indexable page once, at its canonical URL, and
# nothing else — the 404 stays out
sitemap = ROOT / "sitemap.xml"
listed = sorted(re.findall(r"<loc>([^<]+)</loc>", sitemap.read_text(encoding="utf-8")))
indexable = sorted(ORIGIN + url_of(p) for p in pages if p.name != "404.html")
if listed != indexable:
    errors.append("sitemap.xml: lists %s, pages are %s"
                  % (sorted(set(listed) ^ set(indexable)), len(indexable)))

# ── 3. WORKS.md is the source of truth for the works ─────────────

rows = []
for line in (REPO / "WORKS.md").read_text(encoding="utf-8").splitlines():
    if not line.startswith("|"):
        continue
    slug = line.strip("|").split("|")[0].strip()
    if slug and slug != "slug" and not set(slug) <= set("-: "):
        rows.append(slug)

on_disk = sorted(d.name for d in (ROOT / "works").iterdir() if d.is_dir())
if sorted(rows) != on_disk:
    errors.append("WORKS.md: table lists %s, public/works/ holds %s"
                  % (sorted(rows), on_disk))
else:
    for name, suffix in (("index.html", "/"), ("ko.html", "/ko")):
        page = ROOT / "works" / name
        # each card names its slug twice — the <a href> and its itemprop="url"
        found = re.findall(r'href="/works/([a-z0-9-]+)/(?:ko)?"',
                           page.read_text(encoding="utf-8"))
        listed = [s for i, s in enumerate(found) if i == 0 or s != found[i - 1]]
        check(page, listed == rows, f"list order {listed} != WORKS.md order {rows}")

        # the one way out of a work is the list — the walk lives there alone,
        # so a copy-pasted prev/next must not creep back in
        for slug in rows:
            work = ROOT / "works" / slug / name
            html = work.read_text(encoding="utf-8")
            check(work, 'rel="prev"' not in html and 'rel="next"' not in html,
                  "work pages carry no rel=prev/next — only the list link")
            check(work, f'<a href="/works{suffix}">' in html,
                  f'must link back to /works{suffix}')

# ── 4. a plates strip is marked photo for photo ──────────────────

# The dots beside a multi-photo work are hand-written next to the photos they
# mark, in both locales, and the script reads its position off the lit one. A
# strip whose dots have drifted still renders and still resolves, so check 1
# would report OK while the reader is told there are two reliefs, not three.
for page in pages:
    html = page.read_text(encoding="utf-8")
    for fig in re.findall(r'<figure class="exh-plates">(.*?)</figure>', html, re.S):
        strip = re.search(r'<div class="plates">(.*?)</div>', fig, re.S)
        dots = re.search(r'<div class="plates-dots"[^>]*>(.*?)</div>', fig, re.S)
        photos = strip.group(1).count("<img") if strip else 0
        marks = dots.group(1).count("<span") if dots else 0
        check(page, photos > 1 and photos == marks,
              f"plates: {photos} photos but {marks} dots")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"OK — {len(pages)} pages: links resolve, EN/KO pairs agree, "
      f"sitemap complete, {len(rows)} works match WORKS.md order")
