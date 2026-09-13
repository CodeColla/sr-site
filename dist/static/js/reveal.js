// Fades `.reveal-up` elements up into view as they enter the viewport.
// Progressive enhancement: the CSS only hides these elements once
// `document.documentElement` carries the `js` class (set synchronously in
// base.html's <head>), so a no-JS visitor always sees full content
// immediately — nothing depends on this script running to be visible.
(function () {
  var targets = document.querySelectorAll('.reveal-up');
  if (!targets.length) return;

  if (!('IntersectionObserver' in window)) {
    targets.forEach(function (el) { el.classList.add('is-revealed'); });
    return;
  }

  var observer = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-revealed');
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12, rootMargin: '0px 0px -60px 0px' }
  );

  targets.forEach(function (el) { observer.observe(el); });
})();
