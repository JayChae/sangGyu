// Live search + tag filter for the works list. Progressive enhancement:
// the bar is hidden in CSS and only revealed here, once it is wired up —
// without this file (or if it fails to load) the full gallery simply shows.
(() => {
  const bar = document.querySelector(".searchbar");
  if (!bar) return;

  const input = bar.querySelector("input[type=search]");
  const chips = [...bar.querySelectorAll(".chip")];
  const cards = [...document.querySelectorAll(".gallery > li")];
  const empty = document.querySelector(".gallery-empty");
  const pressed = chips.find((c) => c.getAttribute("aria-pressed") === "true");
  let tag = pressed ? pressed.dataset.tag : "all";

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

  // On back-navigation the browser restores the typed query, so filter once
  // before revealing the bar — otherwise the box and the gallery disagree.
  apply();
  document.body.classList.add("search-ready");
})();
