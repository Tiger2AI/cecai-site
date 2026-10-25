from common import *
import html, re

from service_content import SVC

SVC_PHOTO = {"fractional-hr-leadership": "fractional", "talent-succession": "succession", "executive-coaching": "coaching",
             "transformation-ai-readiness": "transformation", "career-transition": "transition"}

PEOPLE = {
    "stephanie": ("Stephanie Abbott", "CPHR, CEC", "Principal & Managing Partner", "SA", "", "people/stephanie-abbott.html"),
    "stuart": ("Stuart MacMillan", "MCMP, CCMP, CPHR", "Partner, AI & Transformation", "SM", "brass", "people/stuart-macmillan.html"),
}

R = "../"
for idx, s in enumerate(SERVICES):
    d = SVC[s["slug"]]
    path = f"services/{s['slug']}.html"
    trail = [("services.html", "Services"), (path, s["short"])]
    svc_schema = {"@context": "https://schema.org", "@type": "Service", "name": s["title"], "serviceType": s["title"],
                  "description": d["meta"], "image": photo_url(SVC_PHOTO[s["slug"]]), "provider": {"@id": f"{SITE}/#org"}, "url": f"{SITE}/{path}",
                  "areaServed": ["Atlantic Canada", "Canada", "United States"],
                  "hasOfferCatalog": {"@type": "OfferCatalog", "name": s["title"],
                                      "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": html.unescape(o[1]), "description": html.unescape(re.sub("<[^>]+>", "", o[2]))}} for o in d["offers"]]}}
    body = head(f"{s['title']} | CECai", d["meta"], path, R, [svc_schema, faq_schema(d["faqs"]), crumb_schema(trail)], og_image=photo_url(SVC_PHOTO[s["slug"]]))
    body += header(R, "services.html")
    signals = "".join(f"<li>{x}</li>" for x in d["signals"])
    dos = "".join(f"<li>{x}</li>" for x in d["do"])
    offers = ""
    for k, n, t, dl in d["offers"]:
        dlh = "".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in dl)
        offers += f'<article class="offer reveal"><div class="kicker">{k}</div><h3>{n}</h3><p>{t}</p><dl>{dlh}</dl></article>'
    outs = "".join(f"<li>{x}</li>" for x in d["outcomes"])
    grid = "g2" if len(d["offers"]) == 4 else "g3"
    nxt = SERVICES[(idx + 1) % len(SERVICES)]
    body += f"""
<section class="page-hero">
  {tides(cls="tides", lines=12, seed=idx * 1.3)}
  <div class="wrap" style="position:relative;z-index:2">
    {crumbs(R, trail)}
    <div class="hero-split"><div>
    <div class="eyebrow">Practice 0{idx + 1} &middot; {s['title']}</div>
    <h1>{d['h1']}</h1>
    <p class="lede mt2">{d['lede']}</p>
    <div class="hero-ctas mt2"><a class="btn btn-primary" href="{R}contact.html">Talk to us about this</a><a class="btn btn-ghost" href="#offers">See how we help</a></div>
    </div>{arch(SVC_PHOTO[s["slug"]], R)}</div>
  </div>
</section>

<section class="section bg-white">
  <div class="wrap split">
    <div><div class="eyebrow">Is this you?</div><h2>{d["signals_h2"]}</h2><p class="muted">{d["signals_intro"]}</p></div>
    <ul class="signals reveal">{signals}</ul>
  </div>
</section>

<section class="section">
  <div class="wrap split rev">
    <div><div class="eyebrow">What we do</div><h2>{d["do_h2"]}</h2><ul class="check reveal">{dos}</ul></div>
    <div class="card" style="background:var(--teal);color:var(--cloud);border:0"><div class="eyebrow" style="color:#CDE0DE">What changes</div><h3 class="serif" style="color:var(--cloud);font-weight:400;font-size:1.6rem">{d["outcomes_h3"]}</h3><ul class="check mt2" style="margin-bottom:0">{outs}</ul></div>
  </div>
</section>

<section class="section bg-paper" id="offers">
  <div class="wrap">
    <div class="section-head"><div class="eyebrow">Signature offers</div><h2>{d["offers_h2"]}</h2><p class="lede">{d["offers_lede"]}</p></div>
    <div class="grid {grid}">{offers}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head"><div class="eyebrow">How it works</div><h2>From first conversation to lasting change.</h2></div>
    <div class="steps reveal">
      <div class="step"><h3>Listen</h3><p>A candid conversation about what's happening, what's at stake and what good looks like for you.</p></div>
      <div class="step"><h3>Diagnose</h3><p>We look at the facts, talk to the right people and tell you plainly what we see.</p></div>
      <div class="step"><h3>Act</h3><p>We roll up our sleeves alongside your leaders, with clear milestones and no surprises.</p></div>
      <div class="step"><h3>Sustain</h3><p>We build your team's capability so the change holds long after we step back.</p></div>
    </div>
  </div>
</section>

<section class="section bg-white">
  <div class="wrap split">
    <div><div class="eyebrow">Who you'll work with</div><h2>{d["team_h2"]}</h2></div>
    <div><p class="lede">{d["team_p"]}</p><a class="textlink" href="{R}team.html">Meet the team</a></div>
  </div>
</section>
"""
    body += faq_block(d["faqs"], d["faq_h2"])
    body += f'<section class="section tight bg-paper"><div class="wrap" style="display:flex;justify-content:space-between;align-items:center;gap:20px;flex-wrap:wrap"><div><div class="eyebrow">Next practice</div><h3 class="serif" style="font-weight:400;font-size:1.6rem;margin:0">{nxt["title"]}</h3></div><a class="btn btn-ghost" href="{nxt["slug"]}.html">Explore <span class="arrow"></span></a></div></section>'
    body += cta(R)
    body += footer(R)
    write(path, body)

# services hub
R0 = ""
trail = [("services.html", "Services")]
cards = ""
for i, s in enumerate(SERVICES, 1):
    d = SVC[s["slug"]]
    offers = "".join(f'<span class="tag brass">{o[1]}</span>' for o in d["offers"])
    cards += f"""<a class="card link-card reveal" href="services/{s['slug']}.html" style="display:grid;grid-template-columns:80px 1fr auto;gap:28px;align-items:start;padding:40px">
<span class="serif" style="font-size:2.6rem;color:var(--brass);line-height:1">0{i}</span>
<div><h3 class="serif" style="font-weight:400;font-size:1.65rem">{s['title']}</h3><p style="max-width:44em">{s['card']}</p><div class="tags" style="display:flex;flex-wrap:wrap;gap:6px">{offers}</div></div>
<span class="go" style="width:46px;height:46px;border-radius:50%;border:1px solid var(--line);display:grid;place-items:center;color:var(--teal)" aria-hidden="true">&rarr;</span></a>"""
listsch = {"@context": "https://schema.org", "@type": "ItemList", "name": "CECai services",
           "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": f"{SITE}/services/{s['slug']}.html", "name": s["title"]} for i, s in enumerate(SERVICES)]}
body = head("Services | Fractional HR, Succession, Coaching, AI Readiness & Outplacement | CECai",
            "Five people and organizational advisory practices for CEOs, owners and executive teams: fractional HR leadership, talent and succession, executive coaching, transformation and AI readiness, and career transition.",
            "services.html", R0, [ORG, listsch, crumb_schema(trail)])
body += header(R0, "services.html")
body += f"""
<section class="page-hero">{tides(lines=12, seed=4)}<div class="wrap" style="position:relative;z-index:2">
{crumbs(R0, trail)}
<div class="eyebrow">Services</div>
<h1>Everything your organization needs. <em class="accent">Exactly when it needs it.</em></h1>
<p class="lede mt2">Senior HR and organizational expertise across five connected practices, from your most urgent people challenge to the ones you can see coming. Led by people who have done the work inside organizations like yours.</p>
</div></section>
<section class="section tight"><div class="wrap grid" style="gap:18px">{cards}</div></section>
<section class="section bg-white"><div class="wrap split even">
  <div><div class="eyebrow">Connected by design</div><h2>Why one organization for all five?</h2></div>
  <div><p class="lede">Because people problems don't arrive one at a time. A succession gap becomes a hiring question. A reorganization becomes a coaching need. An AI rollout becomes a role redesign, and sometimes a transition. When one partner understands your whole picture, nothing falls between the cracks.</p><a class="textlink" href="approach.html">How we work</a></div>
</div></section>
"""
body += cta(R0)
body += footer(R0)
write("services.html", body)
print("services ok")
