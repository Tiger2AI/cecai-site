(function () {
  document.documentElement.classList.add('js');
  var header = document.querySelector('.site-header');
  var toggle = document.querySelector('.nav-toggle');
  if (toggle) {
    toggle.addEventListener('click', function () {
      var open = document.body.classList.toggle('nav-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    document.querySelectorAll('.nav-links a').forEach(function (a) {
      a.addEventListener('click', function () { document.body.classList.remove('nav-open'); toggle.setAttribute('aria-expanded', 'false'); });
    });
  }
  function onScroll() { if (header) header.classList.toggle('scrolled', window.scrollY > 8); }
  window.addEventListener('scroll', onScroll, { passive: true }); onScroll();

  var items = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });
    items.forEach(function (el) { io.observe(el); });
  } else { items.forEach(function (el) { el.classList.add('in'); }); }

  var form = document.querySelector('form[data-contact]');
  if (form) {
    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      var d = new FormData(form);
      var name = (d.get('name') || '').toString().split(' ')[0];
      var box = document.createElement('div');
      box.setAttribute('role', 'status');
      box.innerHTML = '<div class="eyebrow">Thank you' + (name ? ', ' + name.replace(/[<>&"]/g, '') : '') + '</div><h2 style="font-size:1.8rem">We\'ll be in touch within one business day.</h2><p class="muted">If it\'s urgent, email <b>' + form.getAttribute('data-contact') + '</b> directly.</p>';
      form.replaceWith(box);
      box.className = 'form';
    });
  }
  document.querySelectorAll('[data-copy]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var t = btn.getAttribute('data-copy'), label = btn.textContent;
      var done = function () { btn.textContent = 'Copied'; setTimeout(function () { btn.textContent = label; }, 1800); };
      if (navigator.clipboard) navigator.clipboard.writeText(t).then(done, function () { window.prompt('Copy this address:', t); });
      else window.prompt('Copy this address:', t);
    });
  });
  var y = document.getElementById('year'); if (y) y.textContent = new Date().getFullYear();
})();
