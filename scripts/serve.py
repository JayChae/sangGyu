#!/usr/bin/env python3
"""Local preview for public/ that mimics Cloudflare Pages: clean URLs
(/works/ecology/ko is served from ko.html) and 404.html for anything missing.

Usage: python3 scripts/serve.py [port]   (default 8000)
"""
import io
import os
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

ROOT = str(Path(__file__).resolve().parent.parent / "public")


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def send_head(self):
        path = self.path.split("?")[0].split("#")[0]
        # Clean URLs only apply without a trailing slash, matching
        # check-links.py: /works/ko serves ko.html, /works/ko/ does not.
        if not path.endswith("/") and not os.path.exists(self.translate_path(path)):
            candidate = path + ".html"
            if os.path.isfile(self.translate_path(candidate)):
                self.path = candidate
        target = self.translate_path(self.path.split("?")[0].split("#")[0])
        if os.path.isdir(target):
            target = os.path.join(target, "index.html")
        if not os.path.isfile(target):
            return self.send_404()
        return super().send_head()

    def send_404(self):
        """Production serves public/404.html with a 404 status — do the same,
        so that page is reachable locally instead of only in production."""
        page = os.path.join(ROOT, "404.html")
        if not os.path.isfile(page):
            self.send_error(404)
            return None
        with open(page, "rb") as fh:
            body = fh.read()
        self.send_response(404)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        return io.BytesIO(body)


port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
print(f"serving public/ at http://localhost:{port}")
# Loopback only: a preview of unpublished work has no business on the LAN.
HTTPServer(("127.0.0.1", port), Handler).serve_forever()
