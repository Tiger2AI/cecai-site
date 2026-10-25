import html
import datetime
from common import *
from services import SVC
from home import faqs as home_faqs

# ---------------- INSIGHTS ----------------
from articles import load as load_articles
ARTICLES = load_articles()

R = ""
trail = [("insights.html", "Insights")]
posts = "".join(f'<a class="post reveal" href="insights/{a["slug"]}.html"><div class="art" style="background:{a["color"]}">{photo(a["image"], "", "(max-width: 960px) 90vw, 360px") if a["image"] else tides(400,150,7,seed=a["seed"],stroke="#F0EEE9",cls="",opacity_base=.25)}</div><div class="body"><div class="meta">{a["tag"]}</div><h3>{a["title"]}</h3><p>{a["desc"]}</p><span class="textlink" style="margin-top:auto">Read</span></div></a>' for a in ARTICLES)
body = head("Insights | HR, Succession, AI and Change for CEOs & Executive Teams | CECai", "Practical thinking for CEOs, owners and executive teams on fractional HR, succession, AI and organization design, leadership and restructuring, from CECai in Atlantic Canada.", "insights.html", R, [ORG, crumb_schema(trail)])
body += header(R, "insights.html")
body += f"""<section class="page-hero">{tides(lines=12, seed=16)}<div class="wrap" style="position:relative;z-index:2">{crumbs(R, trail)}<div class="eyebrow">Insights</div><h1>Practical thinking for <em class="accent">the year ahead.</em></h1><p class="lede mt2">Short, useful pieces for CEOs, owners and executive teams on the people questions that matter most right now.</p></div></section>
<section class="section tight"><div class="wrap grid g3">{posts}</div></section>
<section class="section bg-white"><div class="wrap split even"><div><div class="eyebrow">Coming soon</div><h2>The CECai Briefing</h2></div><div><p class="lede">A short monthly note on people, leadership and AI for Atlantic Canadian CEOs, owners and executive teams. One idea, one statistic, one thing to try.</p><a class="btn btn-primary" href="mailto:{EMAIL}?subject=Subscribe%20to%20the%20CECai%20Briefing">Subscribe by email</a></div></div></section>"""
body += cta(R)
body += footer(R)
write("insights.html", body)

R = "../"
for a in ARTICLES:
    path = f"insights/{a['slug']}.html"
    tr = [("insights.html", "Insights"), (path, a["tag"])]
    art = {"@context": "https://schema.org", "@type": "Article", "headline": a["title"], "description": a["desc"], "datePublished": a["date"].isoformat(),
           "author": [{"@type": "Person", "name": n.strip()} for n in a["author"].split("&")], "publisher": {"@id": f"{SITE}/#org"},
           "mainEntityOfPage": f"{SITE}/{path}", "about": a["tag"], "inLanguage": "en-CA"}
    if a["image"]: art["image"] = photo_url(a["image"])
    b = head(f"{a['title']} | CECai Insights", a["desc"], path, R, [art, crumb_schema(tr)], og_type="article", og_image=photo_url(a["image"]) if a["image"] else None)
    b += header(R, "insights.html")
    key = "".join(f"<li>{k}</li>" for k in a["key"])
    src = "".join(f'<li><a href="{u}" rel="noopener">{t}</a></li>' for t, u in a["sources"])
    b += f"""<section class="page-hero" style="padding-bottom:40px">{tides(lines=10, seed=a['seed'])}<div class="wrap" style="position:relative;z-index:2;max-width:860px">{crumbs(R, tr)}<div class="eyebrow">{a['tag']}</div><h1 style="font-size:clamp(2rem,4.2vw,3rem)">{a['title']}</h1><p class="muted mt2">By {a['author']} &middot; {a['date_label']} &middot; {a['minutes']} minute read</p></div></section>
<section class="section bg-white" style="padding-top:64px">{('<div class="article-hero">' + photo(a["image"], R, "(max-width: 1000px) 95vw, 1000px", eager=True) + '</div>') if a["image"] else ""}<article class="wrap article" style="margin-top:56px">
<div class="key"><h3>Key points</h3><ul>{key}</ul></div>
{a['body']}
<div class="sources"><b>Sources</b><ul>{src}</ul></div>
</article></section>"""
    b += cta(R)
    b += footer(R)
    write(path, b)
print("insights ok")

# ---------------- FAQ ----------------
R = ""
allfaq = list(home_faqs)
for s in SERVICES:
    allfaq += SVC[s["slug"]]["faqs"]
trail = [("faq.html", "Questions")]
body = head("Questions | Fractional HR, Coaching, AI Readiness & Outplacement | CECai", "Answers to common questions about CECai's fractional HR, succession planning, executive coaching, AI readiness, change management and outplacement services.", "faq.html", R, [ORG, faq_schema(allfaq), crumb_schema(trail)])
body += header(R, "")
groups = [("About CECai", home_faqs)] + [(s["title"], SVC[s["slug"]]["faqs"]) for s in SERVICES]
gh = ""
for t, fs in groups:
    items = "".join(f'<details><summary>{esc(q)}</summary><div class="ans"><p>{a}</p></div></details>' for q, a in fs)
    gh += f'<div class="split" style="margin-bottom:64px"><div><h2 style="font-size:1.6rem">{t}</h2></div><div class="faq">{items}</div></div>'
body += f"""<section class="page-hero">{tides(lines=12, seed=18)}<div class="wrap" style="position:relative;z-index:2">{crumbs(R, trail)}<div class="eyebrow">Questions</div><h1>Straight answers to <em class="accent">good questions.</em></h1></div></section>
<section class="section bg-white"><div class="wrap">{gh}</div></section>"""
body += cta(R)
body += footer(R)
write("faq.html", body)

# ---------------- CONTACT ----------------
trail = [("contact.html", "Contact")]
cp = {"@context": "https://schema.org", "@type": "ContactPage", "name": "Contact CECai", "url": f"{SITE}/contact.html", "about": {"@id": f"{SITE}/#org"}}
body = head("Contact | Book a Conversation | CECai, Atlantic Canada", "Book a free 30-minute conversation with CECai about fractional HR, succession, coaching, AI readiness or restructuring. Serving Atlantic Canada and North America.", "contact.html", R, [ORG, cp, crumb_schema(trail)])
body += header(R, "")
body += f"""<section class="page-hero">{tides(lines=12, seed=20)}<div class="wrap" style="position:relative;z-index:2">{crumbs(R, trail)}
<div class="split" style="align-items:start">
<div>
  <div class="eyebrow">Book a conversation</div>
  <h1 style="font-size:clamp(2.2rem,4.6vw,3.4rem)">Let's talk about <em class="accent">what's next.</em></h1>
  <p class="lede mt2">Thirty minutes, no pitch. Tell us what's happening and we'll tell you honestly how we can help, or who can.</p>
  <ul class="reach mt3">
    <li><b>Stephanie</b><span>HR leadership, talent, coaching and transitions<br><a href="mailto:{EMAIL}">{EMAIL}</a></span></li>
    <li><b>Stuart</b><span>AI, transformation and change<br><a href="mailto:{AI_EMAIL}">{AI_EMAIL}</a></span></li>
    <li><b>Where</b><span>Across Atlantic Canada, in person, and virtually across North America. Serving Saint John, Moncton, Fredericton, Halifax, Charlottetown, St. John's and communities in between.</span></li>
    <li><b>Reply</b><span>Within one business day.</span></li>
  </ul>
</div>
<div class="form email-card">
  <div class="eyebrow">Email Stephanie</div>
  <h2 style="font-size:clamp(1.6rem,3vw,2.1rem)">The quickest way to start is a short email.</h2>
  <p class="email-big"><a href="mailto:{EMAIL}?subject=Conversation%20request">{EMAIL}</a></p>
  <div class="hero-ctas"><a class="btn btn-primary" href="mailto:{EMAIL}?subject=Conversation%20request">Email Stephanie</a><button class="btn btn-ghost" type="button" data-copy="{EMAIL}">Copy address</button></div>
  <p class="muted mt3 mb0" style="font-weight:600;color:var(--ink)">A few lines is plenty. It helps to include:</p>
  <ul class="check mt2">
    <li>Your name, role and organization</li>
    <li>Roughly how many people work there</li>
    <li>What's happening, and what you'd like help with</li>
    <li>A couple of times that suit you for a 30-minute call</li>
  </ul>
  <p class="small muted mb0">Stephanie replies within one business day. Everything you share is kept confidential.</p>
</div>
</div></div></section>"""
body += footer(R)
write("contact.html", body)

# ---------------- PRIVACY / 404 ----------------
trail = [("privacy.html", "Privacy")]
body = head("Privacy | CECai", "How CECai collects, uses and protects personal information.", "privacy.html", R, [crumb_schema(trail)])
body += header(R, "")
body += f"""<section class="page-hero" style="padding-bottom:30px"><div class="wrap">{crumbs(R, trail)}<h1>Privacy</h1></div></section>
<section class="section bg-white" style="padding-top:48px"><div class="wrap article">
<p>CECai (Change Execution Consulting AI Inc.) respects your privacy. We collect only the personal information you choose to share with us, such as your name, organization and contact details when you email us, and use it only to respond to you and provide our services.</p>
<p>We do not sell personal information. We handle client and employee information confidentially, in line with Canada's Personal Information Protection and Electronic Documents Act (PIPEDA) and applicable provincial law. This site does not use advertising or tracking cookies.</p>
<p>Questions about privacy? Email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<p class="small muted">Draft for review by legal counsel before publication.</p>
</div></section>"""
body += footer(R)
write("privacy.html", body)

body = head("Page not found | CECai", "The page you were looking for isn't here.", "404.html", R)
body += header(R, "")
body += f"""<section class="hero" style="min-height:60vh">{tides()}<div class="wrap"><div class="eyebrow">404</div><h1>This page has <em class="accent">moved on.</em></h1><p class="lede mt2">Let's get you somewhere useful.</p><div class="hero-ctas"><a class="btn btn-primary" href="index.html">Home</a><a class="btn btn-ghost" href="services.html">Services</a></div></div></section>"""
body += footer(R)
write("404.html", body)

# ---------------- LLMS / SEO FILES ----------------
pages = ["index.html", "services.html"] + [f"services/{s['slug']}.html" for s in SERVICES] + ["people-and-ai.html", "approach.html", "team.html", "people/stephanie-abbott.html", "people/stuart-macmillan.html", "collective.html", "insights.html"] + [f"insights/{a['slug']}.html" for a in ARTICLES] + ["faq.html", "contact.html", "privacy.html"]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for p in pages:
    loc = SITE + "/" if p == "index.html" else f"{SITE}/{p}"
    sm += f"  <url><loc>{loc}</loc><lastmod>{datetime.date.today().isoformat()}</lastmod></url>\n"
sm += "</urlset>\n"
write("sitemap.xml", sm)
write("robots.txt", f"""User-agent: *
Allow: /

# AI and answer engines are welcome to read and cite this site.
User-agent: GPTBot
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Google-Extended
Allow: /

Sitemap: {SITE}/sitemap.xml
""")

svc_lines = ""
for s in SERVICES:
    d = SVC[s["slug"]]
    offers = "; ".join(html.unescape(o[1]) for o in d["offers"])
    svc_lines += f"- [{s['title']}]({SITE}/services/{s['slug']}.html): {s['card']} Signature offers: {offers}.\n"
llms = f"""# CECai

> CECai (Change Execution Consulting AI Inc.) is an Atlantic Canadian people and organizational advisory practice. It gives CEOs, owners and executive teams senior HR leadership without a full-time hire: strategic HR advisory, fractional and interim HR leadership, talent and succession planning, executive coaching, organizational transformation and AI readiness, and career transition and outplacement. CECai works in person across Atlantic Canada (New Brunswick, Nova Scotia, Prince Edward Island, Newfoundland and Labrador) and remotely across Canada and the United States. Tagline: People First. Future Ready.

## Key facts
- Principal & Managing Partner: Stephanie Abbott, CPHR, CEC. 25+ years leading HR at Canadian and multinational organizations including Lockheed Martin, JPMorgan Chase and Amazon. Certified Executive Coach (Royal Roads University).
- Partner, AI & Transformation: Stuart MacMillan, MCMP, CCMP, PCACP, CPHR, P.BPM. 23+ years and 22 enterprise transformation engagements; advises enterprise AI programs above 100,000 users; Prosci's Canadian AI Change Principal.
- The CECai Collective: senior partner network in AI, digital, ERP, workplace protection and compliance, and organizational transformation (Darcy Daoust, Carol Kotacka, Steve Wakeham, Michael McConachie, Paul Bellavance).
- Engagement models: Advise (retainer), Lead (fractional or interim), Build (fixed-scope projects), Coach (leaders and teams).
- First step: a free 30-minute conversation. Contact: {EMAIL}
- Languages: English and French.

## Services
{svc_lines}
## Pages
- [Home]({SITE}/)
- [People & AI: the people side of AI]({SITE}/people-and-ai.html): helping organizations move to human and AI agent teams, with role redesign, agent accountability and adoption.
- [How We Work]({SITE}/approach.html)
- [Team]({SITE}/team.html)
- [Stephanie Abbott]({SITE}/people/stephanie-abbott.html)
- [Stuart MacMillan]({SITE}/people/stuart-macmillan.html)
- [The CECai Collective]({SITE}/collective.html)
- [Questions and answers]({SITE}/faq.html)
- [Contact]({SITE}/contact.html)

## Insights
""" + "".join(f"- [{a['title']}]({SITE}/insights/{a['slug']}.html): {a['desc']}\n" for a in ARTICLES)
write("llms.txt", llms)

write("assets/img/favicon.svg", '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#1F5C63"/><text x="32" y="43" text-anchor="middle" font-family="Georgia,serif" font-size="30" fill="#F0EEE9">C<tspan font-style="italic" fill="#B08D57">ai</tspan></text></svg>')
print("more ok")
