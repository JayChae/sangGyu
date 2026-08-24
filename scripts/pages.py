#!/usr/bin/env python3
"""One model of how Cloudflare Pages serves public/.

Both the link checker and the local preview need to answer the same question —
"which file does this URL serve?" — so they answer it here, once. When they
each carried their own copy they had already drifted: the preview appended
.html to any missing path and trusted macOS's case-insensitive filesystem,
so a URL could render locally and 404 in production.
"""
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "public"

# The site's origin — the one place it is written down. canonical, hreflang,
# og:url, og:image and sitemap.xml all carry it, because crawlers and share
# previews need absolute URLs. To move to a custom domain: change it here,
# then search-and-replace the old value across public/ (the pages are
# hand-written, so nothing regenerates them).
ORIGIN = "https://sanggyu.pages.dev"


def route(url_path: str, base: Path = ROOT) -> Path:
    """The file Cloudflare Pages serves for a URL path.

    Absolute paths resolve against public/, relative ones against `base`.
    Directories serve index.html; an extensionless path without a trailing
    slash is a clean URL (/works/ecology/ko -> ko.html). A trailing slash is
    never a clean URL, so /works/ko/ stays a directory and fails.
    """
    path = url_path.split("#")[0].split("?")[0]
    target = ROOT / path.lstrip("/") if path.startswith("/") else base / path
    if path.endswith("/") or target.is_dir():
        return target / "index.html"
    if not target.suffix:
        return target.with_name(target.name + ".html")
    return target


def exists(target: Path) -> bool:
    """Path.is_file(), but case-sensitive even on macOS's default filesystem.

    Cloudflare serves from a case-sensitive store while this normally runs on
    a Mac, where /img/Ecology/480.webp would otherwise pass and 404 in
    production. Confirm every component against the real directory listing
    instead of trusting the filesystem's own comparison.
    """
    target = target.resolve()
    if ROOT not in target.parents or not target.is_file():
        return False
    part = target
    while part != ROOT:
        if part.name not in os.listdir(part.parent):
            return False
        part = part.parent
    return True


def url_of(page: Path) -> str:
    """The canonical URL a page is served at: index.html -> /dir/,
    ko.html -> /dir/ko."""
    rel = page.resolve().relative_to(ROOT).parent
    prefix = "/" if rel == Path(".") else f"/{rel.as_posix()}/"
    return prefix if page.name == "index.html" else prefix + page.stem


def counterpart(page: Path) -> Path:
    """The same page in the other language."""
    return page.with_name("ko.html" if page.name == "index.html" else "index.html")
