#!/usr/bin/env python3
"""A QR code for any page of the site, ready to print.

    python3 scripts/build-qr.py                        # the exhibition page
    python3 scripts/build-qr.py /works/ecology/ko      # any page, by path…
    python3 scripts/build-qr.py https://sanggyu.pages.dev/cv/   # …or full URL
    python3 scripts/build-qr.py / /ko /works/          # several at once

Each page becomes print/qr-<path>.svg (vector — use this for print) and
print/qr-<path>.png (a ~1200 px preview / fallback): /works/ecology/ko →
print/qr-works-ecology-ko.{svg,png}; / → print/qr-home.

The path is checked against public/ the way Cloudflare would serve it — a
printed code cannot be corrected, so a typo is refused rather than encoded.
Error correction H: a third of the code can be smudged, glared or covered
and it still scans. The pages.dev URL keeps working after a custom domain
is added, so a printed code never goes stale.

Needs segno (pure Python). The first run installs it into scripts/.venv-qr
(git-ignored) and re-runs itself from there; nothing touches the system
Python.
"""
import os
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
VENV = HERE / ".venv-qr"

try:
    import segno
except ImportError:
    python = VENV / "bin" / "python"
    if Path(sys.prefix) == VENV:
        sys.exit("segno is missing from scripts/.venv-qr — delete the folder and rerun")
    if not python.exists():
        print("first run: installing segno into scripts/.venv-qr …", file=sys.stderr)
        subprocess.run([sys.executable, "-m", "venv", str(VENV)], check=True)
        subprocess.run([str(python), "-m", "pip", "install", "-q", "segno"], check=True)
    os.execv(str(python), [str(python), *sys.argv])

from pages import ORIGIN, exists, route  # noqa: E402

OUT = HERE.parent / "print"
DEFAULT = ["/exhibitions/origin-seoul-2026/"]


def page_path(arg: str) -> str:
    """'/works/ecology/ko' from either that or the full URL on ORIGIN."""
    path = arg[len(ORIGIN):] if arg.startswith(ORIGIN) else arg
    if not path.startswith("/"):
        sys.exit(f"{arg}: give a path starting with / or a URL on {ORIGIN}")
    if not exists(route(path)) or route(path).name == "404.html":
        sys.exit(f"{arg}: no such page — nothing printed")
    return path


def main(args):
    OUT.mkdir(exist_ok=True)
    for path in map(page_path, args or DEFAULT):
        url = ORIGIN + path
        name = "qr-" + (path.strip("/").replace("/", "-") or "home")
        qr = segno.make(url, error="h")
        modules = qr.symbol_size(border=4)[0]
        qr.save(OUT / f"{name}.svg", scale=10, border=4, dark="#0e0e0e")
        qr.save(OUT / f"{name}.png", scale=1200 // modules, border=4, dark="#0e0e0e")
        print(f"{url}\n  → print/{name}.svg + .png  (version {qr.version}-H, "
              f"{qr.symbol_size()[0]} modules)")


if __name__ == "__main__":
    main(sys.argv[1:])
