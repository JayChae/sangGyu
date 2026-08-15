#!/bin/bash
# Convert source JPEGs (../sangyu/arts) to responsive WebP into public/img/.
# One folder per artwork: public/img/<slug>/{480,960,1600}.webp
# (extra views get a prefix, e.g. collective-gaze/view2-480.webp).
# Sizes are never upscaled. Quality 82. Rerunnable.
set -e
cd "$(dirname "$0")/.."

SRC="../sangyu/arts"
OUT="public/img"

convert() { # $1=source jpg  $2=slug  $3=optional filename prefix (e.g. "view2-")
  mkdir -p "$OUT/$2"
  for w in 480 960 1600; do
    cwebp -quiet -q 82 -resize "$w" 0 "$SRC/$1" -o "$OUT/$2/${3}${w}.webp"
  done
  echo "→ $2/${3}*"
}

convert "A Cusion.jpg"                 a-cushion
convert "Beyond the Predetermined.jpg" beyond-the-predetermined
convert "Brave new world.jpg"          brave-new-world
convert "Collective Gaze.jpg"          collective-gaze
convert "Collective Gaze2.jpg"         collective-gaze view2-
convert "Ecology.jpg"                  ecology
convert "The Stranger.jpg"             the-stranger
convert "무제.jpg"                      untitled
