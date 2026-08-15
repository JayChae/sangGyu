#!/usr/bin/env python3
"""Static integrity check: every internal href/src/srcset in public/**/*.html
must resolve to a file (directories resolve to index.html). Also verifies
hreflang pairs point at existing pages. Exits 1 on any failure."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "public"
errors = []

for page in sorted(ROOT.rglob("*.html")):
    html = page.read_text(encoding="utf-8")
    urls = re.findall(r'(?:href|src)="([^"]+)"', html)
    for srcset in re.findall(r'srcset="([^"]+)"', html):
        urls += [part.strip().split()[0] for part in srcset.split(",") if part.strip()]
    for url in urls:
        if url.startswith(("http://", "https://", "data:", "mailto:", "#")):
            continue
        path = url.split("#")[0].split("?")[0]
        if not path:
            continue
        target = ROOT / path.lstrip("/") if path.startswith("/") else page.parent / path
        if target.is_dir():
            target = target / "index.html"
        if not target.is_file() and not target.suffix:
            # Cloudflare Pages clean URLs: /works/ecology/ko serves ko.html
            target = target.with_name(target.name + ".html")
        if not target.is_file():
            errors.append(f"{page.relative_to(ROOT)}: broken {url}")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"OK — all internal links resolve ({len(list(ROOT.rglob('*.html')))} pages checked)")
