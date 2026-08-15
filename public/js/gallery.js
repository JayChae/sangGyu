// Live search + tag filter for the works list. Progressive enhancement:
// without this file the full gallery simply shows (search bar is hidden
// via <noscript>).
(() => {
  const bar = document.querySelector(".searchbar");
  if (!bar) return;

  const input = bar.querySelector("input[type=search]");
  const chips = [...bar.querySelectorAll(".chip")];
  const cards = [...document.querySelectorAll(".gallery > li")];
  const empty = document.querySelector(".gallery-empty");
  let tag = "all";

  const apply = () => {
    const q = input.value.trim().toLowerCase();
    let shown = 0;
    for (const card of cards) {
      const hit =
        (tag === "all" || card.dataset.tags.split(" ").includes(tag)) &&
        (!q || card.dataset.search.includes(q));
      card.hidden = !hit;
      if (hit) shown++;
    }
    empty.hidden = shown > 0;
  };

  for (const chip of chips) {
    chip.addEventListener("click", () => {
      tag = chip.dataset.tag;
      for (const c of chips)
        c.setAttribute("aria-pressed", String(c === chip));
      apply();
    });
  }
  input.addEventListener("input", apply);
})();
