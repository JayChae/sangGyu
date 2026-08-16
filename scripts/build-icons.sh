#!/usr/bin/env bash
#
# The app icon → public/icon-{192,512}.png
#
# The home-screen icon is the landing page's name, cropped to its initials and
# hung on the same warm-white wall: system sans 600, tracked 0.14em, ink on
# #f7f6f3 — the treatment of `.landing h1` in css/site.css. Keep the two in
# step; if the landing's type changes, this file changes with it.
#
# PNG, not the SVG favicon: Android requires raster manifest icons, and iOS
# reads only <link rel="apple-touch-icon">.
#
# Every size is set at its own type size, centred in one 512px window, and cut
# out of the middle of that window afterwards. The detour is Chrome's minimum
# window width of ~500px (see the gotcha in CLAUDE.md): a 192px window silently
# becomes a 500px viewport cropped to its top-left corner, which throws the
# letters off-centre, and --force-device-scale-factor cannot make up the
# difference either — it clamps at 0.5. Cropping keeps each icon rasterised
# from vectors at its final size, so the small one is not a resampled big one.
#
# The manifest gives both icons `purpose: "any maskable"`, so the letters must
# stay inside the maskable safe zone — the centred circle of 80% diameter;
# everything outside it is Android's to crop. At the size below the furthest
# ink sits ~184px from the centre of the 512 icon against a 204.8px budget, so
# there is one notch of headroom and no more: enlarge the type and the corners
# of the P and the G are what Android shaves off.
#
# The bytes are cached for a month by _headers (see /*.png), not a year: unlike
# an artwork photo these are not renamed when they change.
#
# Needs Chrome (any recent version); set $CHROME to point at another binary.
set -euo pipefail

cd "$(dirname "$0")/.."
CHROME=${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}
[ -x "$CHROME" ] || { echo "Chrome not found at: $CHROME" >&2; exit 1; }

tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT

# SIZE is substituted per icon below. 0.322 of the icon is as large as the
# initials can be set and still clear the maskable safe zone.
cat > "$tmp/icon.tpl" <<'HTML'
<!doctype html>
<meta charset="utf-8" />
<style>
  html, body { margin: 0; padding: 0; }
  body {
    width: 100vw; height: 100vh; background: #f7f6f3;
    display: grid; place-content: center;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  }
  b {
    font-size: calc(SIZE * 0.322); font-weight: 600; letter-spacing: 0.14em;
    color: #1a1a1a; line-height: 1;
    /* The line box centres; the letters do not. Tracking hangs off the right
       of the last G (half of it, 0.07em, is the horizontal debt) and caps sit
       low in the em box. Corrected in em, so it holds at every size — the same
       optical recentring `.landing h1` does with its margin-left. */
    transform: translate(0.07em, -0.02em);
  }
</style>
<b>PSG</b>
HTML

for size in 192 512; do
  sed "s/SIZE/${size}px/" "$tmp/icon.tpl" > "$tmp/icon-$size.html"
  "$CHROME" --headless --disable-gpu --hide-scrollbars \
    --force-device-scale-factor=1 --window-size=512,512 \
    --screenshot="$tmp/shot-$size.png" "file://$tmp/icon-$size.html" 2>/dev/null
  sips -c "$size" "$size" "$tmp/shot-$size.png" --out "public/icon-$size.png" >/dev/null
  echo "public/icon-$size.png"
done
