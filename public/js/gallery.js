// Live search + theme and series filter for the works list. Progressive enhancement:
// the bar is hidden in CSS and only revealed here, once it is wired up —
// without this file (or if it fails to load) the full gallery simply shows.
(() => {
  const bar = document.querySelector(".searchbar");
  if (!bar) return;

  const input = bar.querySelector("input[type=search]");
  const chips = [...bar.querySelectorAll(".chip")];
  const gallery = document.querySelector(".gallery");
  const rule = gallery.querySelector(".gallery-related");
  const cards = [...gallery.children].filter((li) => li !== rule);
  const empty = document.querySelector(".gallery-empty");

  // the pressed chip *is* the state — never mirrored into a variable that
  // could disagree with the pill the reader can see
  const theme = () =>
    bar.querySelector('.chip[aria-pressed="true"]').dataset.tag;
  // does the artist's sheet mark this card ● (data-main) or ○ (data-related)
  // for the theme? A series' works carry it in data-main: all main, none
  // related. Both are in WORKS.md; check-links.py holds the cards to it.
  const marked = (card, key, tag) =>
    (card.dataset[key] || "").split(" ").includes(tag);

  const apply = () => {
    const tag = theme();
    const q = input.value.trim().toLowerCase();
    let shown = 0;
    let related = 0;
    for (const card of cards) {
      const rel = marked(card, "related", tag);
      const hit =
        (tag === "all" || rel || marked(card, "main", tag)) &&
        (!q || card.dataset.search.includes(q));
      if (card.hidden === hit) card.hidden = !hit;
      if (hit) shown++;
      if (hit && rel) related++;
    }
    rule.hidden = related === 0;
    empty.hidden = shown > 0;
  };

  // A theme hangs its main works first and its related ones under the rule,
  // each group in the list's own order; the rest are hidden, so they stay put.
  // Moving a card hangs it afresh, entrance and all — which is why this runs
  // when a new chip is pressed, and never while the reader types.
  const hang = () => {
    const tag = theme();
    const main = cards.filter((c) => tag === "all" || marked(c, "main", tag));
    const related = cards.filter((c) => marked(c, "related", tag));
    gallery.append(...main, rule, ...related);
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
      const fresh = chip.getAttribute("aria-pressed") !== "true";
      for (const c of chips)
        c.setAttribute("aria-pressed", String(c === chip));
      if (fresh) hang();
      filter();
    });
  }
  input.addEventListener("input", filter);

  // On back-navigation the browser restores the typed query, so filter once
  // before revealing the bar — otherwise the box and the gallery disagree.
  apply();
  document.body.classList.add("search-ready");
})();
