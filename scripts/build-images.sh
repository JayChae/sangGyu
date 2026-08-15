#!/bin/bash
# Convert source JPEGs (../sangyu/arts) to responsive WebP into public/img/.
# One folder per artwork: public/img/<slug>/{480,640,960,1200,1600}.webp
# (extra views get a prefix, e.g. collective-gaze/view2-480.webp).
# Quality 82. Rerunnable — outputs newer than their source are left alone, so
# a rerun after adding one artwork re-encodes only that artwork.
#
# The tiers exist because a candidate that is merely "big enough" is the one
# that gets downloaded, so a missing size means the next one up is paid for:
#   640  — the gallery list renders thumbnails ~170px wide, so a 3x phone
#          needs ~510px and would otherwise take the 960 file (~530KB extra
#          on the site's entry page).
#   1200 — a detail hero renders ~350px wide, so a 3x phone needs ~1050px and
#          would otherwise take the 1600 file (~30% extra per artwork).
# 1600 stays: a retina desktop needs up to 1680px and nothing smaller covers
# it. Keep quality at 82 — those pages paint the 1600 file at roughly 1:1, so
# it is the size, not the compression, that should absorb the savings.
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
  for w in 480 640 960 1200 1600; do
    local out="$OUT/$2/${3}${w}.webp"
    if [ "$w" -gt "$src_w" ]; then
      echo "  ! $2/${3}${w}.webp 건너뜀 — 원본이 ${src_w}px. srcset 에서도 뺄 것."
      continue
    fi
    if [ "$out" -nt "$SRC/$1" ]; then continue; fi
    cwebp -quiet -q 82 -resize "$w" 0 "$SRC/$1" -o "$out" &
  done
  wait
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
