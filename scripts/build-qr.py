#!/usr/bin/env python3
"""A QR code for any page of the site, ready to print.

    python3 scripts/build-qr.py                        # the exhibition page
    python3 scripts/build-qr.py /works/ecology/ko      # any page, by path…
    python3 scripts/build-qr.py https://sanggyu.pages.dev/cv/   # …or full URL
    python3 scripts/build-qr.py / /ko /works/          # several at once
    python3 scripts/build-qr.py --mm 80 /              # a larger print
    python3 scripts/build-qr.py --clear                 # …-clear.png, no white

Each page becomes print/qr-<path>.svg (vector — use this for print) and
print/qr-<path>.png (a 600 dpi fallback): /works/ecology/ko →
print/qr-works-ecology-ko.{svg,png}; / → print/qr-home.

Both files carry their real size — 50 mm square by default, quiet zone
included — so a print shop places them without rescaling. Ink is plain
black on nothing: the paper, or the cloth, is the white half of the
contrast, and the printed square must keep its white margin.

The SVG has no background at all, which is what a transparent sticker on
white cloth needs — the cloth becomes the white half. The PNG paints that
white in, so for a shop that will not take vector, `--clear` writes it
background-free as print/qr-<path>-clear.png instead.

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
MM = 50          # printed edge, quiet zone included — `--mm N` for another
DPI = 600        # of the PNG fallback
INK = "#000"     # print black, not the site's ink token


def page_path(arg: str) -> str:
    """'/works/ecology/ko' from either that or the full URL on ORIGIN."""
    path = arg[len(ORIGIN):] if arg.startswith(ORIGIN) else arg
    if not path.startswith("/"):
        sys.exit(f"{arg}: give a path starting with / or a URL on {ORIGIN}")
    if not exists(route(path)) or route(path).name == "404.html":
        sys.exit(f"{arg}: no such page — nothing printed")
    return path


def take_mm(args: list) -> float:
    """The printed edge in millimetres: `--mm N`, taken out of the arguments."""
    if "--mm" not in args:
        return MM
    i = args.index("--mm")
    try:
        mm = float(args[i + 1])
    except (IndexError, ValueError):
        sys.exit("--mm wants millimetres, e.g. --mm 50")
    del args[i:i + 2]
    return mm


def main(args):
    OUT.mkdir(exist_ok=True)
    mm = take_mm(args)
    clear = "--clear" in args          # for transparent stickers: no white behind
    if clear:
        args.remove("--clear")
    for path in map(page_path, args or DEFAULT):
        url = ORIGIN + path
        name = "qr-" + (path.strip("/").replace("/", "-") or "home")
        qr = segno.make(url, error="h")
        modules = qr.symbol_size(border=4)[0]
        px = round(mm / 25.4 * DPI / modules)   # whole pixels per module
        png = f"{name}-clear.png" if clear else f"{name}.png"
        qr.save(OUT / f"{name}.svg", scale=mm / modules, unit="mm", border=4, dark=INK)
        qr.save(OUT / png, scale=px, border=4, dark=INK,
                light=None if clear else "#fff",
                dpi=round(px * modules / (mm / 25.4)))
        print(f"{url}\n  → print/{name}.svg + {png}  (version {qr.version}-H, "
              f"{modules} modules, {mm:g} mm square — {mm / modules:.2f} mm per module)")


if __name__ == "__main__":
    main(sys.argv[1:])
