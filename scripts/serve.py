#!/usr/bin/env python3
"""Local preview for public/ that mimics Cloudflare Pages clean URLs:
/works/ecology/ko is served from ko.html, just like production.

Usage: python3 scripts/serve.py [port]   (default 8000)
"""
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
        if not os.path.exists(self.translate_path(path)):
            candidate = path.rstrip("/") + ".html"
            if os.path.isfile(self.translate_path(candidate)):
                self.path = candidate
        return super().send_head()


port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
print(f"serving public/ at http://localhost:{port}")
HTTPServer(("", port), Handler).serve_forever()
