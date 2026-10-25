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
    var to = form.getAttribute('data-contact');
    var key = form.getAttribute('data-key');
    var esc = function (s) { return String(s).replace(/[<>&"]/g, ''); };
    var show = function (eyebrow, title, body) {
      var box = document.createElement('div');
      box.className = 'form'; box.setAttribute('role', 'status');
      box.innerHTML = '<div class="eyebrow">' + eyebrow + '</div><h2 style="font-size:1.8rem">' + title + '</h2><p class="muted">' + body + '</p>';
      form.replaceWith(box);
    };
    var mail = '<a href="mailto:' + to + '"><b>' + to + '</b></a>';
    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var d = new FormData(form);
      var first = esc((d.get('name') || '').toString().split(' ')[0]);
      if (!key) {
        show('One more step', 'Please email us directly.', 'Our online form is being connected. Email ' + mail + ' and Stephanie will reply within one business day.');
        return;
      }
      var btn = form.querySelector('button[type="submit"]');
      btn.disabled = true; btn.textContent = 'Sending…';
      var payload = {
        access_key: key,
        subject: 'Website enquiry: ' + (d.get('org') || d.get('name') || 'cecai.ca'),
        from_name: 'cecai.ca contact form',
        name: d.get('name'), email: d.get('email'), replyto: d.get('email'),
        organization: d.get('org'), role: d.get('role'), size: d.get('size'),
        interested_in: d.getAll('topic').join(', '), message: d.get('message'),
        botcheck: d.get('botcheck') ? true : ''
      };
      fetch('https://api.web3forms.com/submit', { method: 'POST', headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' }, body: JSON.stringify(payload) })
        .then(function (r) { return r.json(); })
        .then(function (res) {
          if (res && res.success) { show('Thank you' + (first ? ', ' + first : ''), 'We\'ll be in touch within one business day.', 'Your note is on its way to Stephanie. If it\'s urgent, email ' + mail + '.'); }
          else { throw new Error('send failed'); }
        })
        .catch(function () {
          btn.disabled = false; btn.textContent = 'Request a conversation';
          var err = form.querySelector('.form-error') || document.createElement('p');
          err.className = 'form-error'; err.setAttribute('role', 'alert');
          err.innerHTML = 'Sorry, your message didn’t send. Please try again, or email ' + mail + '.';
          btn.insertAdjacentElement('afterend', err);
        });
    });
  }
  var y = document.getElementById('year'); if (y) y.textContent = new Date().getFullYear();
})();
