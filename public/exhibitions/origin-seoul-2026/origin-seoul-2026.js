// The arrows, and the lit dot, for a work that is more than one photo (The
// Stranger is three reliefs). The strip and the dots under it are CSS and are
// drawn whether or not this file arrives, so a reader who never gets it still
// sees that there are three and can still swipe them. This adds only what
// needs a script. check-links.py holds the dots to the photos they mark.
(() => {
  for (const fig of document.querySelectorAll(".exh-plates")) {
    const strip = fig.querySelector(".plates");
    const dots = [...fig.querySelectorAll(".plates-dots span")];
    const arrows = [...fig.querySelectorAll(".plates-arrow")];
    const last = strip.children.length - 1;
    if (last < 1) continue;

    // The lit dot *is* where we are — never mirrored into a variable that
    // could disagree with the mark the reader can see. mark() lights it on the
    // tap, while the strip is still gliding there, so a second tap counts from
    // the plate being flown to and not the one already being left behind.
    const at = () => dots.findIndex((d) => d.classList.contains("on"));
    const mark = (i) => {
      if (i === at()) return;
      dots.forEach((d, n) => d.classList.toggle("on", n === i));
      for (const a of arrows) {
        const to = i + Number(a.dataset.dir);
        // aria-disabled, not disabled: an arrow tapped to the end of the strip
        // must not go unfocusable under the keyboard that is still on it. The
        // clamp in goTo is what makes the tap itself a no-op.
        a.setAttribute("aria-disabled", String(to < 0 || to > last));
      }
    };

    // one photo per step, and the photo is exactly as wide as the strip
    const goTo = (i) => {
      i = Math.min(Math.max(i, 0), last);
      mark(i);
      strip.scrollTo({ left: i * strip.clientWidth });
    };

    // a swipe fires scroll by the ten but changes the photo once or twice; the
    // rest stop at the early return in mark()
    const under = () => Math.round(strip.scrollLeft / strip.clientWidth);
    strip.addEventListener("scroll", () => mark(under()), { passive: true });

    for (const a of arrows)
      a.addEventListener("click", () => goTo(at() + Number(a.dataset.dir)));

    mark(under());
    fig.classList.add("plates-ready");
  }
})();
