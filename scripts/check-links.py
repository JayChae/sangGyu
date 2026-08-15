#!/usr/bin/env python3
"""Static integrity check: every internal href/src/srcset in public/**/*.html
must resolve to a file (directories resolve to index.html), matching how
Cloudflare Pages serves them. Exits 1 on any failure."""
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "public"
errors = []


def resolves(target: Path) -> bool:
    """Path.is_file(), but case-sensitive even on macOS's default filesystem.

    Cloudflare serves from a case-sensitive store while this check normally
    runs on a Mac, where /img/Ecology/480.webp would otherwise pass here and
    404 in production. Confirm every component against the real directory
    listing instead of trusting the filesystem's own comparison."""
    target = target.resolve()
    if ROOT not in target.parents or not target.is_file():
        return False
    part = target
    while part != ROOT:
        if part.name not in os.listdir(part.parent):
            return False
        part = part.parent
    return True

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
        if path.endswith("/") or target.is_dir():
            target = target / "index.html"
        elif not target.suffix:
            # Cloudflare Pages clean URLs: /works/ecology/ko serves ko.html.
            # Only without a trailing slash — /works/ko/ is not a URL any page
            # declares, so do not quietly accept it here either.
            target = target.with_name(target.name + ".html")
        if not resolves(target):
            errors.append(f"{page.relative_to(ROOT)}: broken {url}")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"OK — all internal links resolve ({len(list(ROOT.rglob('*.html')))} pages checked)")
