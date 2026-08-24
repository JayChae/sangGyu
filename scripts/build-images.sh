#!/bin/bash
# Convert the artist's source photos (../sangyu/arts, one folder per work,
# named by the artist) to responsive WebP into public/img/.
# One folder per artwork: public/img/<slug>/{480,640,960,1200,1600}.webp
# (extra views get a prefix, e.g. the-stranger/view2-480.webp).
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
# the new file a version prefix and update the srcset. Overwriting in place
# strands returning visitors. The works below whose hero is a different photo
# (or a different crop) from the 2026-07 set carry "v2-" for exactly that
# reason; that first set is kept in ../sangyu/arts/_old-2026-07.
#
# Every photo the artist sent is used: the first line of a work is its hero,
# the rest are its views, in the order of the artist's folder.
set -e
cd "$(dirname "$0")/.."

SRC="../sangyu/arts"
OUT="public/img"
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

# A phone often stores a portrait photo landscape and adds an EXIF orientation
# tag saying to turn it. cwebp ignores that tag (and -metadata none drops it),
# so such a photo is baked in sideways — brave-new-world shipped three views
# that way. Rotate the pixels first instead, losslessly, with jpegtran (it
# comes with jpeg-turbo, which libwebp already depends on).
exif_orientation() { # $1=photo → its orientation tag, 1 when there is none
  python3 -c '
import struct, sys
d = open(sys.argv[1], "rb").read(300000)
i = d.find(b"Exif\x00\x00")
o = 1
if i >= 0:
    t = i + 6
    e = "<" if d[t:t + 2] == b"II" else ">"
    p = t + struct.unpack(e + "I", d[t + 4:t + 8])[0]
    for n in range(struct.unpack(e + "H", d[p:p + 2])[0]):
        f = p + 2 + 12 * n
        if struct.unpack(e + "H", d[f:f + 2])[0] == 0x0112:
            o = struct.unpack(e + "H", d[f + 8:f + 10])[0]
print(o)
' "$1"
}

upright() { # $1=photo → it, or an upright copy of it in $TMP
  local turn=()
  case "$(exif_orientation "$1")" in
    2) turn=(-flip horizontal);;
    3) turn=(-rotate 180);;
    4) turn=(-flip vertical);;
    5) turn=(-transpose);;
    6) turn=(-rotate 90);;
    7) turn=(-transverse);;
    8) turn=(-rotate 270);;
    *) echo "$1"; return;;
  esac
  local out="$TMP/upright.jpg"   # one at a time: convert() waits for its tiers
  jpegtran "${turn[@]}" -copy none "$1" > "$out"
  echo "$out"
}

convert() { # $1=source photo  $2=slug  $3=optional filename prefix (e.g. "view2-")
  mkdir -p "$OUT/$2"
  local photo src_w
  photo=$(upright "$SRC/$1")
  src_w=$(sips -g pixelWidth "$photo" | awk '/pixelWidth:/ { print $2 }')
  for w in 480 640 960 1200 1600; do
    local out="$OUT/$2/${3}${w}.webp"
    if [ "$w" -gt "$src_w" ]; then
      echo "  ! $2/${3}${w}.webp 건너뜀 — 원본이 ${src_w}px. srcset 에서도 뺄 것."
      continue
    fi
    if [ "$out" -nt "$SRC/$1" ]; then continue; fi
    cwebp -quiet -q 82 -metadata none -resize "$w" 0 "$photo" -o "$out" &
  done
  wait
  echo "→ $2/${3}* (원본 ${src_w}px)"
}


convert "폐허풍경(beyond the predetermined)/완성본 전경 복사본.jpg"                beyond-the-predetermined v2-
convert "폐허풍경(beyond the predetermined)/IMG_6226.jpg"                  beyond-the-predetermined view2-
convert "폐허풍경(beyond the predetermined)/IMG_6227.jpg"                  beyond-the-predetermined view3-
convert "폐허풍경(beyond the predetermined)/IMG_6235.jpg"                  beyond-the-predetermined view4-
convert "폐허풍경(beyond the predetermined)/IMG_6238.jpg"                  beyond-the-predetermined view5-
convert "폐허풍경(beyond the predetermined)/IMG_6242.jpg"                  beyond-the-predetermined view6-
convert "폐허풍경(beyond the predetermined)/IMG_6243.jpg"                  beyond-the-predetermined view7-
convert "폐허풍경(beyond the predetermined)/IMG_6248.jpg"                  beyond-the-predetermined view8-
convert "폐허풍경(beyond the predetermined)/IMG_6250.jpg"                  beyond-the-predetermined view9-
convert "폐허풍경(beyond the predetermined)/IMG_6531.jpg"                  beyond-the-predetermined view10-

convert "산화형상 #10/IMG_6110.jpg"                                        oxidized-figures-10
convert "산화형상 #10/IMG_6111.jpg"                                        oxidized-figures-10 view2-
convert "산화형상 #10/IMG_6112.jpg"                                        oxidized-figures-10 view3-
convert "산화형상 #10/IMG_6113.jpg"                                        oxidized-figures-10 view4-
convert "산화형상 #10/IMG_6114.jpg"                                        oxidized-figures-10 view5-
convert "산화형상 #10/IMG_6115.jpg"                                        oxidized-figures-10 view6-

convert "산화형상 #6/IMG_6056.jpg"                                         oxidized-figures-6
convert "산화형상 #6/IMG_6058.jpg"                                         oxidized-figures-6 view2-
convert "산화형상 #6/IMG_6059.jpg"                                         oxidized-figures-6 view3-
convert "산화형상 #6/IMG_6060.jpg"                                         oxidized-figures-6 view4-
convert "산화형상 #6/IMG_6062.jpg"                                         oxidized-figures-6 view5-
convert "산화형상 #6/IMG_6063.jpg"                                         oxidized-figures-6 view6-

convert "산화형상 #5/IMG_6104.jpg"                                         oxidized-figures-5
convert "산화형상 #5/IMG_6105.jpg"                                         oxidized-figures-5 view2-
convert "산화형상 #5/IMG_6106.jpg"                                         oxidized-figures-5 view3-
convert "산화형상 #5/IMG_6107.jpg"                                         oxidized-figures-5 view4-
convert "산화형상 #5/IMG_6108.jpg"                                         oxidized-figures-5 view5-
convert "산화형상 #5/IMG_6109.jpg"                                         oxidized-figures-5 view6-

convert "산화형상 #3/IMG_6092.jpg"                                         oxidized-figures-3
convert "산화형상 #3/IMG_6093.jpg"                                         oxidized-figures-3 view2-
convert "산화형상 #3/IMG_6094.jpg"                                         oxidized-figures-3 view3-
convert "산화형상 #3/IMG_6095.jpg"                                         oxidized-figures-3 view4-
convert "산화형상 #3/IMG_6096.jpg"                                         oxidized-figures-3 view5-
convert "산화형상 #3/IMG_6097.jpg"                                         oxidized-figures-3 view6-

convert "산화형상 #2/IMG_6098.jpg"                                         oxidized-figures-2
convert "산화형상 #2/IMG_6099.jpg"                                         oxidized-figures-2 view2-
convert "산화형상 #2/IMG_6100.jpg"                                         oxidized-figures-2 view3-
convert "산화형상 #2/IMG_6101.jpg"                                         oxidized-figures-2 view4-
convert "산화형상 #2/IMG_6102.jpg"                                         oxidized-figures-2 view5-
convert "산화형상 #2/IMG_6103.jpg"                                         oxidized-figures-2 view6-

convert "응시/IMG_5780.jpg"                                              collective-gaze v2-
convert "응시/IMG_5769.jpg"                                              collective-gaze view2-
convert "응시/IMG_5772.jpg"                                              collective-gaze view3-
convert "응시/IMG_5778.jpg"                                              collective-gaze view4-
convert "응시/IMG_5783.jpg"                                              collective-gaze view5-
convert "응시/IMG_8646.jpeg"                                             collective-gaze view6-
convert "응시/IMG_8650.jpeg"                                             collective-gaze view7-
convert "응시/IMG_8651.jpeg"                                             collective-gaze view8-
convert "응시/IMG_8654.jpeg"                                             collective-gaze view9-

convert "이방인/IMG_9172.jpeg"                                            the-stranger v2-
convert "이방인/IMG_9166.jpeg"                                            the-stranger view2-
convert "이방인/IMG_9171.jpeg"                                            the-stranger view3-

convert "자소상/IMG_8988.jpeg"                                            self-portrait
convert "자소상/IMG_8985.jpeg"                                            self-portrait view2-
convert "자소상/IMG_8987.jpeg"                                            self-portrait view3-
convert "자소상/IMG_8990.jpeg"                                            self-portrait view4-

convert "나한들 - 작은 존재들/IMG_8620.jpeg"                                   arhats-little-beings
convert "나한들 - 작은 존재들/IMG_8621.jpeg"                                   arhats-little-beings view2-
convert "나한들 - 작은 존재들/IMG_8622.jpeg"                                   arhats-little-beings view3-
convert "나한들 - 작은 존재들/IMG_8623.jpeg"                                   arhats-little-beings view4-
convert "나한들 - 작은 존재들/IMG_8627.jpeg"                                   arhats-little-beings view5-

convert "손/IMG_8608.jpeg"                                              a-hand
convert "손/IMG_8609.jpeg"                                              a-hand view2-
convert "손/IMG_8610.jpeg"                                              a-hand view3-

convert "두 세개의 연못/IMG_9095.jpg"                                        the-pool-of-two-worlds
convert "두 세개의 연못/IMG_9093.jpg"                                        the-pool-of-two-worlds view2-
convert "두 세개의 연못/1.png"                                               the-pool-of-two-worlds view3-
convert "두 세개의 연못/2.png"                                               the-pool-of-two-worlds view4-
convert "두 세개의 연못/스크린샷 2026-08-20 12.41.38.png"                        the-pool-of-two-worlds view5-
convert "두 세개의 연못/스크린샷 2026-08-20 12.41.51.png"                        the-pool-of-two-worlds view6-

convert "얼굴/IMG_9086.jpeg"                                             a-face
convert "얼굴/IMG_8594.jpeg"                                             a-face view2-
convert "얼굴/IMG_8598.jpeg"                                             a-face view3-

convert "멋진 신세계/IMG_3208.jpeg"                                         brave-new-world
convert "멋진 신세계/IMG_2581.jpeg"                                         brave-new-world view2-v2-
convert "멋진 신세계/IMG_3209.jpeg"                                         brave-new-world view3-
convert "멋진 신세계/IMG_3210.jpeg"                                         brave-new-world view4-v2-
convert "멋진 신세계/IMG_3211.jpeg"                                         brave-new-world view5-
convert "멋진 신세계/IMG_3212.jpeg"                                         brave-new-world view6-
convert "멋진 신세계/IMG_3213.jpeg"                                         brave-new-world view7-
convert "멋진 신세계/IMG_3214.jpeg"                                         brave-new-world view8-v2-

convert "생태/IMG_3150.jpeg"                                             ecology
convert "생태/IMG_3143.jpeg"                                             ecology view2-
convert "생태/IMG_3144.jpeg"                                             ecology view3-
convert "생태/IMG_3145.jpeg"                                             ecology view4-
convert "생태/IMG_3146.jpeg"                                             ecology view5-
convert "생태/IMG_3147.jpeg"                                             ecology view6-

convert "연소/연소.jpg"                                                    combustion

convert "무제/제목_없는_아트워크.jpg"                                            untitled v2-

convert "해골/IMG_0979.jpeg"                                             skull
convert "해골/IMG_0980.jpeg"                                             skull view2-
convert "해골/IMG_0961.jpeg"                                             skull view3-
convert "해골/IMG_0962.jpeg"                                             skull view4-
convert "해골/IMG_0963.jpeg"                                             skull view5-
convert "해골/IMG_0964.jpeg"                                             skull view6-
convert "해골/IMG_0965.jpeg"                                             skull view7-

convert "쿠션/IMG_8093.jpeg"                                             a-cushion
convert "쿠션/IMG_8092.jpeg"                                             a-cushion view2-
convert "쿠션/IMG_8094.jpeg"                                             a-cushion view3-

convert "추상인체/1.正面-1.jpg"                                              abstract-body-3
convert "추상인체/2正面-2.jpg"                                               abstract-body-3 view2-
convert "추상인체/5.局部-1.jpg"                                              abstract-body-3 view3-
