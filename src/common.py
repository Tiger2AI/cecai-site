import json, math, os, html

SITE = "https://cecai.ca"
OUT = os.environ.get("CECAI_OUT", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_site"))
EMAIL = "stephanie@cecai.ca"
AI_EMAIL = "stuart@cecai.ca"

NAV = [
    ("services.html", "Services"),
    ("people-and-ai.html", "People & AI"),
    ("approach.html", "How We Work"),
    ("team.html", "Team"),
    ("insights.html", "Insights"),
]

SERVICES = [
    {"slug": "fractional-hr-leadership", "short": "Strategic HR & Fractional Leadership",
     "title": "Strategic HR Advisory & Fractional HR Leadership",
     "card": "Senior HR leadership that flexes with your business, from an ongoing partner to an interim lead through a gap or a trusted advisor.",
     "tags": ["HR assessment", "Fractional CHRO", "Interim HR", "HR foundations", "HR team mentoring"]},
    {"slug": "talent-succession", "short": "Talent & Succession",
     "title": "Talent Strategy, Recruitment & Succession Planning",
     "card": "Know who your critical people are, who comes next, and how to hire the roles that will shape the next five years.",
     "tags": ["Owner succession", "Talent reviews", "Key hires"]},
    {"slug": "executive-coaching", "short": "Executive Coaching",
     "title": "Executive Coaching & Leadership Development",
     "card": "Certified executive coaching for whatever leadership asks of you: a new role, a hard decision, a team that's scaling, navigating change or growing into what's next.",
     "tags": ["1:1 coaching", "Team coaching", "Transitions", "Change & AI"]},
    {"slug": "transformation-ai-readiness", "short": "Transformation & AI Readiness",
     "title": "Organizational Transformation, Change & AI Readiness",
     "card": "Organization design, workforce planning and change leadership for the shift to human and AI teams. People First. Future Ready.",
     "tags": ["Organization design", "AI readiness", "Change"]},
    {"slug": "career-transition", "short": "Career Transition",
     "title": "Career Transition & Outplacement",
     "card": "When roles change or end, we help you lead the process with dignity, finding new paths where possible and supporting people with care.",
     "tags": ["Outplacement", "Respectful transitions", "Leader transitions"]},
]


def esc(s):
    return html.escape(s, quote=True)


def tides(width=900, height=640, lines=14, seed=0.0, stroke="#1F5C63", accent="#B08D57", cls="tides", opacity_base=0.18):
    paths = []
    for i in range(lines):
        y0 = 40 + i * (height - 80) / (lines - 1)
        amp = 18 + 26 * math.sin((i + seed) * 0.55) ** 2
        freq = 0.0062 + 0.0009 * math.cos(i * 0.8 + seed)
        phase = i * 0.42 + seed
        pts = []
        for x in range(-60, width + 80, 12):
            y = y0 + amp * math.sin(x * freq + phase) + 8 * math.sin(x * freq * 2.3 + phase * 1.7)
            pts.append((x, y))
        d = "M" + " L".join(f"{x:.0f},{y:.1f}" for x, y in pts)
        col = accent if i == lines // 2 - 1 else stroke
        op = 0.9 if col == accent else opacity_base + 0.5 * (1 - abs(i - lines / 2) / (lines / 2)) * 0.6
        sw = 1.6 if col == accent else 1.1
        paths.append(f'<path class="t" fill="none" d="{d}" stroke="{col}" stroke-opacity="{op:.2f}" stroke-width="{sw}"/>')
    return f'<svg class="{cls}" viewBox="0 0 {width} {height}" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false">{"".join(paths)}</svg>'


def head(title, desc, path, root, schema=None, og_type="website"):
    canon = f"{SITE}/{path}" if path != "index.html" else f"{SITE}/"
    sch = ""
    for s in (schema or []):
        sch += f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>\n'
    return f"""<!doctype html>
<html lang="en-CA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canon}">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
<meta name="theme-color" content="#1F5C63">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="CECai">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE}/assets/img/og-cecai.png">
<meta property="og:locale" content="en_CA">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{root}assets/img/favicon.svg" type="image/svg+xml">
<link rel="alternate" type="text/plain" href="{root}llms.txt" title="LLM summary">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Lora:ital,wght@0,400;0,500;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}assets/css/site.css">
{sch}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""


def header(root, current):
    items = ""
    for href, label in NAV:
        cur = ' aria-current="page"' if current == href else ""
        items += f'<li><a href="{root}{href}"{cur}>{label}</a></li>'
    return f"""<header class="site-header">
  <div class="wrap nav">
    <a class="logo" href="{root}index.html" aria-label="CECai home">CEC<span class="ai">ai</span><small>People &amp; Organization<br>Advisory</small></a>
    <button class="nav-toggle" aria-label="Menu" aria-expanded="false" aria-controls="nav-links"><span></span><span></span><span></span></button>
    <ul class="nav-links" id="nav-links">{items}<li><a class="btn btn-primary" href="{root}contact.html">Book a conversation</a></li></ul>
  </div>
</header>
<main id="main">
"""


def footer(root):
    svc = "".join(f'<li><a href="{root}services/{s["slug"]}.html">{s["short"]}</a></li>' for s in SERVICES)
    return f"""</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <a class="logo" href="{root}index.html">CEC<span class="ai">ai</span></a>
        <p class="mt2" style="max-width:24em">People and organizational advisory for CEOs, owners and executive teams. Rooted in Saint John, New Brunswick. Working across Atlantic Canada and North America.</p>
        <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      </div>
      <div><h4>Services</h4><ul>{svc}</ul></div>
      <div><h4>Organization</h4><ul>
        <li><a href="{root}people-and-ai.html">People &amp; AI</a></li>
        <li><a href="{root}approach.html">How We Work</a></li>
        <li><a href="{root}team.html">Team</a></li>
        <li><a href="{root}collective.html">The CECai Collective</a></li>
        <li><a href="{root}insights.html">Insights</a></li>
      </ul></div>
      <div><h4>Connect</h4><ul>
        <li><a href="{root}contact.html">Book a conversation</a></li>
        <li><a href="{root}faq.html">Questions</a></li>
        <li><a href="https://www.linkedin.com/" rel="noopener">LinkedIn</a></li>
        <li><a href="{root}privacy.html">Privacy</a></li>
      </ul></div>
    </div>
    <div class="foot-base">
      <span>&copy; <span id="year">2026</span> Change Execution Consulting AI Inc. (CECai). Greater Saint John, New Brunswick, Canada.</span>
      <span>Proudly Atlantic Canadian</span>
    </div>
  </div>
</footer>
<script src="{root}assets/js/site.js" defer></script>
</body>
</html>
"""


def cta(root, title="Let's start with a conversation.", text="Thirty minutes, no pitch. Tell us what's happening in your organization and we'll tell you honestly how we can help, or who can."):
    return f"""<section class="section tight"><div class="wrap"><div class="cta-band reveal">
  {tides(700, 400, 9, seed=2.0, stroke="#F0EEE9", accent="#B08D57", cls="", opacity_base=0.3)}
  <div><h2>{title}</h2><p>{text}</p></div>
  <div class="actions"><a class="btn btn-light" href="{root}contact.html">Book a conversation</a><a class="btn btn-line-light" href="mailto:{EMAIL}">Email Stephanie</a></div>
</div></div></section>
"""


def faq_block(faqs, title="Questions leaders ask us"):
    items = "".join(f'<details><summary>{esc(q)}</summary><div class="ans"><p>{a}</p></div></details>' for q, a in faqs)
    return f"""<section class="section"><div class="wrap split">
  <div><div class="eyebrow">FAQ</div><h2>{title}</h2></div>
  <div class="faq">{items}</div>
</div></section>
"""


def faq_schema(faqs):
    import re
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}} for q, a in faqs]}


def crumbs(root, trail):
    parts = [f'<a href="{root}index.html">Home</a>']
    for href, label in trail[:-1]:
        parts.append(f'<a href="{root}{href}">{label}</a>')
    parts.append(f'<span aria-current="page" style="color:var(--ink);margin:0">{trail[-1][1]}</span>')
    return '<nav class="crumbs" aria-label="Breadcrumb">' + '<span>/</span>'.join(parts) + '</nav>'


def crumb_schema(trail):
    items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"}]
    for i, (href, label) in enumerate(trail, start=2):
        items.append({"@type": "ListItem", "position": i, "name": label, "item": f"{SITE}/{href}"})
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}


ORG = {'@context': 'https://schema.org',
 '@type': 'ProfessionalService',
 '@id': 'https://cecai.ca/#org',
 'name': 'CECai',
 'legalName': 'Change Execution Consulting AI Inc.',
 'url': 'https://cecai.ca/',
 'email': 'stephanie@cecai.ca',
 'logo': 'https://cecai.ca/assets/img/favicon.svg',
 'description': 'CECai is an Atlantic Canadian people and organizational advisory practice. It provides strategic HR advisory, fractional '
                'and interim HR leadership, talent and succession planning, executive coaching, organizational transformation and AI '
                'readiness, and career transition and outplacement to CEOs, owners and executive teams across Atlantic Canada and North '
                'America.',
 'address': {'@type': 'PostalAddress', 'addressRegion': 'NB', 'addressCountry': 'CA'},
 'areaServed': [{'@type': 'City', 'name': 'Saint John'},
                {'@type': 'City', 'name': 'Moncton'},
                {'@type': 'City', 'name': 'Fredericton'},
                {'@type': 'City', 'name': 'Halifax'},
                {'@type': 'City', 'name': 'Charlottetown'},
                {'@type': 'City', 'name': "St. John's"},
                {'@type': 'AdministrativeArea', 'name': 'New Brunswick'},
                {'@type': 'AdministrativeArea', 'name': 'Nova Scotia'},
                {'@type': 'AdministrativeArea', 'name': 'Prince Edward Island'},
                {'@type': 'AdministrativeArea', 'name': 'Newfoundland and Labrador'},
                {'@type': 'AdministrativeArea', 'name': 'Canada'},
                {'@type': 'AdministrativeArea', 'name': 'United States'}],
 'knowsAbout': ['Fractional HR leadership',
                'Interim HR leadership',
                'Organizational design',
                'Succession planning',
                'Executive coaching',
                'Change management',
                'AI readiness',
                'Human and AI agent teams',
                'Workforce planning',
                'Outplacement',
                'Employee and labour relations'],
 'employee': [{'@id': 'https://cecai.ca/people/stephanie-abbott.html#person'},
              {'@id': 'https://cecai.ca/people/stuart-macmillan.html#person'}]}


def write(path, content):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)


# ---- Team portraits: drop a square JPG into static/assets/img/team/<slug>.jpg and it replaces the monogram ----
TEAM_SLUGS = {"SA": "stephanie-abbott", "SM": "stuart-macmillan", "MM": "michael-mcconachie", "SW": "steve-wakeham",
              "PB": "paul-bellavance", "DD": "darcy-daoust", "CK": "carol-kotacka"}
TEAM_NAMES = {"SA": "Stephanie Abbott", "SM": "Stuart MacMillan", "MM": "Michael McConachie", "SW": "Steve Wakeham",
              "PB": "Paul Bellavance", "DD": "Darcy Daoust", "CK": "Carol Kotacka"}
_STATIC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "static")


def face(initials, root, tone="", style="", note=True, eager=False):
    slug = TEAM_SLUGS.get(initials, "")
    if slug and os.path.exists(os.path.join(_STATIC, "assets", "img", "team", slug + ".jpg")):
        name = TEAM_NAMES[initials]
        load = 'fetchpriority="high"' if eager else 'loading="lazy"'
        return (f'<div class="portrait has-photo" style="{style}"><picture>'
                f'<source srcset="{root}assets/img/team/{slug}.webp" type="image/webp">'
                f'<img src="{root}assets/img/team/{slug}.jpg" alt="{name}, CECai" width="800" height="800" {load} decoding="async"></picture></div>')
    n = '<span class="note">Portrait to come</span>' if note else ""
    return f'<div class="portrait {tone}" style="{style}"><span class="mono">{initials}</span>{n}</div>'
