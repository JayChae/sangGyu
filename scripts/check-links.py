#!/usr/bin/env python3
"""The test suite. It asserts the invariants this hand-written site rests on:

1. every internal href/src/srcset resolves to a real file, the way Cloudflare
   Pages would serve it;
2. every page claims its own URL as canonical and points its hreflang
   alternates and its language toggle at itself and its counterpart;
3. WORKS.md really is the source of truth — the works on disk are exactly the
   works in the table, and both list pages walk them in the table's order. A
   work page leads back to the list and nowhere else: no prev/next chain.

Checks 2 and 3 exist because the only authoring method here is copy-paste-then-
translate, whose usual failure is a stale-but-valid URL: it resolves, so check 1
alone reports OK while the Korean page canonicalises to a different artwork.
Nothing is generated — the pages stay hand-written; this only refuses to let
the copies drift. Exits 1 on any failure.
"""
import re
import sys
from pathlib import Path

from pages import ROOT, counterpart, exists, route, url_of

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

    check(page, exists(counterpart(page)), f"no counterpart {counterpart(page).name}")
    check(page, attr(html, r'<html lang="([^"]+)"') ==
          ("ko" if page.name == "ko.html" else "en"), "wrong <html lang>")
    check(page, attr(html, r'<link rel="canonical" href="([^"]+)"') == own,
          f"canonical must be {own}")
    check(page, attr(html, r'<link rel="alternate" hreflang="en" href="([^"]+)"') == en,
          f"hreflang=en must be {en}")
    check(page, attr(html, r'<link rel="alternate" hreflang="ko" href="([^"]+)"') == ko,
          f"hreflang=ko must be {ko}")
    toggle = attr(html, r'<a class="lang"[^>]*?href="([^"]+)"')
    check(page, toggle is None or toggle == other,
          f"language toggle must point at {other}")

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

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"OK — {len(pages)} pages: links resolve, EN/KO pairs agree, "
      f"{len(rows)} works match WORKS.md order")
