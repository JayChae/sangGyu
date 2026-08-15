#!/bin/bash
# Convert source JPEGs (../sangyu/arts) to responsive WebP into public/img/.
# One folder per artwork: public/img/<slug>/{480,960,1600}.webp
# (extra views get a prefix, e.g. collective-gaze/view2-480.webp).
# Quality 82. Rerunnable.
#
# Widths larger than the source are skipped, not upscaled: cwebp -resize is a
# target, not a cap, and an upscaled file is blurrier AND heavier than the
# smaller one srcset would otherwise pick. When a width is skipped, drop that
# candidate from the page's srcset too.
#
# Replacing an artwork photo: /img/* is cached immutable for a year, so give
# the new file a version prefix (convert "Ecology.jpg" ecology "v2-") and
# update the srcset. Overwriting in place strands returning visitors.
set -e
cd "$(dirname "$0")/.."

SRC="../sangyu/arts"
OUT="public/img"

convert() { # $1=source jpg  $2=slug  $3=optional filename prefix (e.g. "view2-")
  mkdir -p "$OUT/$2"
  local src_w
  src_w=$(sips -g pixelWidth "$SRC/$1" | awk '/pixelWidth:/ { print $2 }')
  for w in 480 960 1600; do
    if [ "$w" -gt "$src_w" ]; then
      echo "  ! $2/${3}${w}.webp 건너뜀 — 원본이 ${src_w}px. srcset 에서도 뺄 것."
      continue
    fi
    cwebp -quiet -q 82 -resize "$w" 0 "$SRC/$1" -o "$OUT/$2/${3}${w}.webp"
  done
  echo "→ $2/${3}* (원본 ${src_w}px)"
}

convert "A Cusion.jpg"                 a-cushion
convert "Beyond the Predetermined.jpg" beyond-the-predetermined
convert "Brave new world.jpg"          brave-new-world
convert "Collective Gaze.jpg"          collective-gaze
convert "Collective Gaze2.jpg"         collective-gaze view2-
convert "Ecology.jpg"                  ecology
convert "The Stranger.jpg"             the-stranger
convert "무제.jpg"                      untitled
