#!/usr/bin/env python3
"""Local preview for public/ that mimics Cloudflare Pages: clean URLs
(/works/ecology/ko is served from ko.html) and 404.html for anything missing.

Routing and existence both come from pages.py — the same model check-links.py
tests against, so the preview cannot render a URL the checker calls broken.

Usage: python3 scripts/serve.py [port]   (default 8000)
"""
import io
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import quote, unquote

from pages import ROOT, exists, route


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def send_head(self):
        target = route(unquote(self.path))
        if not exists(target):
            return self.send_404()
        self.path = quote("/" + target.relative_to(ROOT).as_posix())
        return super().send_head()

    def send_404(self):
        """Production serves public/404.html with a 404 status — do the same,
        so that page is reachable locally instead of only in production."""
        body = (ROOT / "404.html").read_bytes()
        self.send_response(404)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        return io.BytesIO(body)


port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
print(f"serving public/ at http://localhost:{port}")
# Loopback only: a preview of unpublished work has no business on the LAN.
HTTPServer(("127.0.0.1", port), Handler).serve_forever()
