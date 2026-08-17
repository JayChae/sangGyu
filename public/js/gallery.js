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

  const apply = () => {
    // the pressed chip *is* the state — never mirrored into a variable that
    // could disagree with the pill the reader can see
    const tag = bar.querySelector('.chip[aria-pressed="true"]')?.dataset.tag;
    const q = input.value.trim().toLowerCase();
    let shown = 0;
    for (const card of cards) {
      const hit =
        (!tag || tag === "all" || card.dataset.tags.split(" ").includes(tag)) &&
        (!q || card.dataset.search.includes(q));
      if (card.hidden === hit) card.hidden = !hit;
      if (hit) shown++;
    }
    empty.hidden = shown > 0;
  };

  // The bar is fixed to the bottom of the phone, but the results start at the
  // top of the page: filter from halfway down the list and the matches land
  // above the fold, leaving the reader looking at the gap the hidden cards
  // left. So every filter the reader triggers also takes them to the first
  // result. Not on the initial apply() below — that one must not overwrite the
  // scroll position the browser restores on back-navigation.
  const filter = () => {
    apply();
    window.scrollTo({ top: 0 });
  };

  for (const chip of chips) {
    chip.addEventListener("click", () => {
      for (const c of chips)
        c.setAttribute("aria-pressed", String(c === chip));
      filter();
    });
  }
  input.addEventListener("input", filter);

  // On back-navigation the browser restores the typed query, so filter once
  // before revealing the bar — otherwise the box and the gallery disagree.
  apply();
  document.body.classList.add("search-ready");
})();
