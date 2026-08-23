// Highlights the primary-nav link matching whichever section is
// currently dominant in the viewport. Plain IntersectionObserver,
// no framework — consistent with the rest of the site.
(function () {
  var navLinks = Array.prototype.slice.call(
    document.querySelectorAll('.primary-nav a[href^="#"]')
  );
  if (!navLinks.length) return;

  var sections = navLinks
    .map(function (link) {
      var id = link.getAttribute('href').slice(1);
      var section = document.getElementById(id);
      return section ? { link: link, section: section } : null;
    })
    .filter(Boolean);
  if (!sections.length) return;

  var current = null;

  function setActive(link) {
    if (current === link) return;
    navLinks.forEach(function (l) { l.classList.remove('active'); });
    if (link) link.classList.add('active');
    current = link;
  }

  var observer = new IntersectionObserver(
    function (entries) {
      // Pick the intersecting entry closest to the top of the viewport
      // so only one section is ever "active" at a time.
      var visible = entries
        .filter(function (e) { return e.isIntersecting; })
        .sort(function (a, b) { return a.boundingClientRect.top - b.boundingClientRect.top; });

      if (visible.length) {
        var match = sections.find(function (s) { return s.section === visible[0].target; });
        if (match) setActive(match.link);
      }
    },
    {
      // A horizontal band roughly matching where a reader's eye sits
      // just under the sticky header — triggers a change right as a
      // section takes over the screen, not the instant it peeks in.
      rootMargin: '-84px 0px -60% 0px',
      threshold: 0,
    }
  );

  sections.forEach(function (s) { observer.observe(s.section); });
})();
