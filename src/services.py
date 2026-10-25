from common import *

SVC = {
"fractional-hr-leadership": dict(
  meta="Fractional CHRO, interim HR leadership and strategic HR advisory for CEOs and owners in Atlantic Canada and North America. Senior HR judgment without a full-time hire.",
  h1="Senior HR leadership, <em class='accent'>without</em> the full-time hire.",
  lede="You need someone at the leadership table who has done this before: built HR functions, handled the difficult conversations, steadied teams through change. We give you that person, for the days and decisions that matter.",
  signals=["You've outgrown an HR generalist, but a full-time CHRO isn't in the budget yet.",
           "Your HR leader just left, and the work can't wait for a six-month search.",
           "You're scaling, acquiring or restructuring and need HR to keep pace.",
           "A sensitive employee or labour relations issue needs experienced judgment, now.",
           "Your policies, systems and practices were built for a much smaller company."],
  do=["People strategy aligned to your business plan", "Advice to the CEO and leadership team on organization, talent and leadership decisions",
      "HR infrastructure: policies, handbook, HRIS, employment standards compliance", "Employee and labour relations, including union environments",
      "Workplace investigations and HR risk management", "Compensation, benefit plan design and total rewards",
      "Building, coaching and right-sizing your HR team", "HR process redesign and smart automation"],
  offers=[("Ongoing", "Fractional CHRO", "A senior HR executive on your leadership team, two to eight days a month. Board-ready advice, hands-on delivery and a steady presence your people can trust.", [("Format", "Monthly retainer"), ("Best for", "20 to 500 employees"), ("Term", "6 months, renewable")]),
          ("Gap cover", "Interim HR Leadership", "We step in quickly when your HR leader leaves or a crisis hits, keep the function stable and moving, and help you hire the right permanent leader.", [("Format", "Part- or full-time"), ("Start", "Within days"), ("Term", "3 to 9 months")]),
          ("Build", "HR Foundations", "For organizations building HR for the first time. Policies, onboarding, performance, records and compliance, set up properly and sized for where you are going.", [("Format", "Fixed-scope project"), ("Best for", "First HR function"), ("Term", "8 to 12 weeks")])],
  outcomes=["A senior HR voice in every major people decision", "Fewer surprises: lower risk in relations, compliance and turnover", "An HR function that scales with you, not behind you", "Leaders who handle hard conversations with confidence"],
  people=["stephanie"],
  faqs=[("What does a fractional CHRO cost compared to a full-time hire?", "A fractional engagement typically costs a fraction of a full-time senior HR executive's salary, benefits and recruiting fees, because you pay only for the days you use. We scope a monthly retainer to your size and priorities and adjust it as you grow."),
        ("How quickly can you start?", "For interim leadership we can usually be working with you within days. Fractional retainers typically start within two weeks of our first conversation."),
        ("Do you work with unionized organizations?", "Yes. Our team has supported employee and labour relations in unionized municipal, industrial and public sector environments, including collective agreement interpretation, grievances and sensitive workplace matters."),
        ("Will you replace our existing HR person?", "No. Most often we lead and develop the people you have. We act as their senior leader and coach, take on the strategic and high-risk work, and help them grow into bigger roles.")]),

"talent-succession": dict(
  meta="Succession planning, talent reviews, critical role assessment and recruitment strategy for owners and CEOs. Business succession support for Atlantic Canadian owner-led companies.",
  h1="Know who leads <em class='accent'>next.</em> Before you have to.",
  lede="The value of your business lives in its people. We help you see your talent clearly, build the next generation of leaders, and hire the roles that will shape the next five years.",
  signals=["You're thinking about stepping back, selling or passing the business on.",
           "One or two people hold knowledge your business can't afford to lose.",
           "Your best people are leaving for opportunities you could have offered.",
           "Key hires keep taking too long, or not working out.",
           "You're not sure whether AI changes who you should hire next."],
  do=["Owner and leadership succession planning", "Talent reviews and nine-box calibration with your leadership team",
      "Critical role and key-person risk assessment", "High-potential identification and development plans",
      "Strategic workforce planning for the next three to five years", "Recruitment strategy, role design and selection for key hires",
      "Performance management that leaders actually use", "Leadership pipeline and early-career programs"],
  offers=[("For owners", "Owner Succession Program", "A people-first succession plan for owner-led businesses: who can lead, what they need to be ready, how to transfer relationships and knowledge, and a timeline you can trust. Works alongside your accountant and lawyer.", [("Format", "Facilitated program"), ("Best for", "Owner-led businesses"), ("Term", "3 to 6 months")]),
          ("Diagnostic", "Talent Review & Critical Role Assessment", "A clear picture of your bench in weeks: your critical roles, key-person risks, ready-now successors and the gaps to close first.", [("Format", "Project"), ("Output", "Board-ready talent map"), ("Term", "6 to 8 weeks")]),
          ("Hiring", "Key Role Hiring Strategy", "For the hires that matter most. We define the role for the work ahead, including how AI changes it, design the selection process and sit on the panel with you.", [("Format", "Per role"), ("Best for", "Senior and pivotal roles"), ("Term", "4 to 10 weeks")])],
  outcomes=["A named successor and readiness plan for every critical role", "Lower key-person and knowledge risk", "Higher retention of the people you most want to keep", "Hiring decisions grounded in the work you'll need done, not the job you had"],
  people=["stephanie"],
  faqs=[("When should a business owner start succession planning?", "Ideally three to five years before you plan to step back. Developing a leader, transferring relationships and preparing a business for sale or transfer all take longer than most owners expect."),
        ("Is succession planning only for large companies?", "No. Smaller organizations often carry more key-person risk, because a few people hold most of the knowledge and relationships. A simple, honest plan protects the business and its value."),
        ("Do you run executive searches?", "We focus on hiring strategy rather than traditional search: defining the role, building the selection process and assessing finalists with you. Where a full search makes sense, we can work alongside a search partner."),
        ("How does AI affect workforce planning?", "AI changes what many roles contain, so planning by job title alone is no longer enough. We plan around the work, the skills that differentiate you and where people and AI each add the most value.")]),

"executive-coaching": dict(
  meta="Certified executive coaching and leadership development for CEOs, senior leaders and managers. Leadership transitions, performance coaching and leading teams through AI and change.",
  h1="Better leaders build <em class='accent'>better</em> organizations.",
  lede="Leadership has never been more demanding. We coach leaders to think clearly under pressure, lead people through change, and grow into the role the business needs from them next.",
  signals=["A strong leader has stepped into a much bigger role.",
           "A talented executive is getting in their own way, and their team feels it.",
           "Your managers are being asked to lead through AI with no playbook.",
           "Your leadership team works hard but doesn't work as a team.",
           "You want to develop future leaders from within, not hire from outside."],
  do=["One-to-one executive coaching", "Leadership transition and first-100-days coaching",
      "Performance coaching with clear goals and stakeholder feedback", "Leadership team effectiveness",
      "Emerging leader development programs", "Manager capability: coaching, feedback and difficult conversations",
      "Leading through AI: modelling, experimentation and change", "360-degree feedback and development planning"],
  offers=[("1:1", "Executive Coaching", "Six months of structured coaching with a Certified Executive Coach, anchored to goals agreed with you and your sponsor, with confidential sessions and measurable progress.", [("Format", "Bi-weekly sessions"), ("Includes", "360 input, goals, review"), ("Term", "6 months")]),
          ("Cohort", "Leading Through AI", "A practical program for leaders and managers, co-led by our HR and AI advisors. Leaders learn to model AI use, coach experimentation and talk honestly with teams about what's changing.", [("Format", "Cohort of 8 to 16"), ("Delivery", "In person or virtual"), ("Term", "8 weeks")]),
          ("Transition", "First 100 Days", "For newly promoted or newly hired senior leaders. A focused plan to build relationships, read the culture, make early decisions well and avoid the common traps.", [("Format", "Intensive coaching"), ("Best for", "New senior roles"), ("Term", "3 to 4 months")])],
  outcomes=["Leaders who make clearer decisions, faster", "Smoother leadership transitions and fewer costly derailments", "Managers confident leading teams through AI and change", "A stronger internal bench for future roles"],
  people=["stephanie", "stuart"],
  faqs=[("What credentials does your coach hold?", "Stephanie Abbott is a Certified Executive Coach (CEC) through Royal Roads University and a Chartered Professional in Human Resources (CPHR), with more than 25 years leading HR and coaching senior leaders."),
        ("Is coaching confidential?", "Yes. Coaching conversations are confidential. We agree goals and progress measures with the leader and their sponsor at the start, and share only what the leader agrees to share."),
        ("Why should leaders learn to model AI?", "Research from Microsoft found that when managers actively model AI use, the value employees recognize from AI rises significantly. Leaders set the tone for experimentation, so we build that capability into our leadership work."),
        ("Can you coach virtually?", "Yes. We coach leaders across Canada and the United States by video, and in person across Atlantic Canada.")]),

"transformation-ai-readiness": dict(
  meta="Organizational design, workforce planning, change management and AI readiness. Redesign roles and structures for human and AI agent teams. Prosci-certified change leadership.",
  h1="Redesign how work gets done, <em class='accent'>with</em> your people.",
  lede="AI, growth and restructuring all end up in the same place: your structure, your roles and your people's willingness to change. We bring deep HR and org design expertise together with hands-on enterprise AI experience, so the change actually sticks.",
  signals=["You've bought AI tools, but the way work gets done hasn't changed.",
           "Your org chart reflects history more than strategy.",
           "Leaders disagree about who is accountable for what, including the AI.",
           "A merger, acquisition or reorganization is coming, and people are anxious.",
           "You need a workforce plan that accounts for what AI will and won't do."],
  do=["Organizational design and operating model redesign", "Human and AI agent role design, accountability and supervision models",
      "Strategic workforce planning and workforce impact assessment", "Change strategy and change management (Prosci and ACMP-certified)",
      "AI adoption, enablement and value realization", "Stakeholder engagement and leadership alignment",
      "Merger, acquisition and integration people workstreams", "HR operating model and HR technology transformation"],
  offers=[("Diagnostic", "Frontier Readiness Diagnostic", "In four to six weeks: where AI will change work in your organization, how ready your leaders, structure and HR systems are, and a prioritized 12-month roadmap. People first, technology second.", [("Format", "Project"), ("Output", "Roadmap and readout"), ("Term", "4 to 6 weeks")]),
          ("Design", "Human + Agent Org Design Sprint", "Redesign a function or value stream for people and AI agents working together: who does what, who owns each agent, how decisions are made, and what roles and skills you'll need.", [("Format", "Facilitated sprint"), ("Best for", "One function at a time"), ("Term", "6 to 10 weeks")]),
          ("Deliver", "Change & Adoption Leadership", "Experienced change leadership for your transformation, from reorganizations and ERP to AI rollouts, with sponsorship, communication, enablement and measurement that proves value.", [("Format", "Embedded or advisory"), ("Method", "Prosci, ACMP, ValueOS"), ("Term", "Program length")])],
  outcomes=["A structure built for your strategy, not your history", "Clear human accountability for every AI agent and workflow", "Faster adoption and measurable value from your AI investment", "People who understand the change and choose to support it"],
  people=["stuart", "stephanie"],
  faqs=[("Why should an HR firm lead AI readiness?", "Because AI changes jobs, structures, skills and accountability, which is HR and organizational design work. Technology firms can deploy tools; adoption and value depend on redesigning work around people. We do both, with HR leadership and enterprise AI experience in one team."),
        ("What is a human and AI agent team?", "It's a team where AI agents take on defined tasks or processes under human direction. People set goals, judge quality and stay accountable. Designing these teams well means deciding which work agents do, who owns each agent, and how roles and skills change."),
        ("What change management methods do you use?", "Our team holds Prosci, ACMP (CCMP and MCMP) and CPHR credentials and uses established methods including ADKAR and the ACMP Standard, adapted to the size and pace of your organization, plus value realization methods built for the AI era."),
        ("Do you help with mergers and acquisitions?", "Yes. We lead or support the people side of integration: org design, role mapping, culture, communication, retention of key people and harmonizing HR programs.")]),

"career-transition": dict(
  meta="Outplacement, career transition coaching and redeployment support. Help employees through restructuring with dignity and protect your culture and reputation. Atlantic Canada and North America.",
  h1="When roles change, lead it <em class='accent'>with</em> dignity.",
  lede="How you treat people on their way out is how your remaining people will judge you. We help you plan restructuring carefully, redeploy talent where you can, and support every person who leaves with real, senior-level help.",
  signals=["You're planning a restructuring and want to get the people side right.",
           "AI or automation is changing roles, and you'd rather redeploy than release.",
           "A senior leader is leaving and deserves a thoughtful transition.",
           "Your managers dread delivering difficult news, and it shows.",
           "You're worried about how a reduction will land with your remaining team and community."],
  do=["Restructuring planning and people risk review", "Redeployment and internal mobility before reductions",
      "Manager preparation for notification conversations", "Individual and group outplacement",
      "Executive and senior leader transition coaching", "Career development and reskilling pathways, including AI-era skills",
      "Communication planning for affected and remaining employees", "Support for leaders and HR teams through the process"],
  offers=[("Plan", "Respectful Transitions", "Before any announcement: role and impact analysis, redeploy-first options, manager preparation, communications and a day-of plan that treats people well and keeps the business running.", [("Format", "Advisory project"), ("Best for", "Any size reduction"), ("Term", "2 to 6 weeks")]),
          ("Support", "Individual & Group Outplacement", "Practical, human support for departing employees: career assessment, resume and LinkedIn, interview preparation, job search strategy and AI-era reskilling guidance.", [("Format", "Packages by level"), ("Delivery", "In person or virtual"), ("Term", "1 to 6 months")]),
          ("Senior", "Leader Transition Coaching", "One-to-one coaching for executives and senior leaders, from a coach who has sat on both sides of the table, to land well and land soon.", [("Format", "1:1 coaching"), ("Best for", "Senior leaders"), ("Term", "3 to 6 months")])],
  outcomes=["Fewer departures than first planned, through redeployment", "People who leave feeling respected, and say so", "Managers prepared for the hardest conversations", "A remaining team that trusts leadership through change"],
  people=["stephanie"],
  faqs=[("What is included in outplacement support?", "Typically a career assessment, resume and LinkedIn support, interview coaching, job search strategy and regular coaching sessions. We tailor packages to the person's level and the support you want to offer."),
        ("Why consider redeployment first?", "Rehiring and severance are often more expensive than moving capable people into new roles. Research from LHH found most employers who track the costs say rehiring costs more than redeployment, and redeployment protects trust and knowledge."),
        ("Can you support a single senior leader rather than a group?", "Yes. Many engagements are for one executive or senior leader, often combined with transition coaching."),
        ("How do you protect our reputation during restructuring?", "By planning carefully, preparing managers, communicating honestly with affected and remaining employees, and giving departing people real support. People remember how they were treated, and so does your community.")]),
}

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
                  "description": d["meta"], "provider": {"@id": f"{SITE}/#org"}, "url": f"{SITE}/{path}",
                  "areaServed": ["Atlantic Canada", "Canada", "United States"],
                  "hasOfferCatalog": {"@type": "OfferCatalog", "name": s["title"],
                                      "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": o[1], "description": o[2]}} for o in d["offers"]]}}
    body = head(f"{s['title']} | CECai", d["meta"], path, R, [svc_schema, faq_schema(d["faqs"]), crumb_schema(trail)])
    body += header(R, "services.html")
    signals = "".join(f"<li>{x}</li>" for x in d["signals"])
    dos = "".join(f"<li>{x}</li>" for x in d["do"])
    offers = ""
    for k, n, t, dl in d["offers"]:
        dlh = "".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in dl)
        offers += f'<article class="offer reveal"><div class="kicker">{k}</div><h3>{n}</h3><p>{t}</p><dl>{dlh}</dl></article>'
    outs = "".join(f"<li>{x}</li>" for x in d["outcomes"])
    ppl = ""
    for p in d["people"]:
        nm, cr, role, mono, tone, href = PEOPLE[p]
        ppl += f'<a class="card link-card" href="{R}{href}" style="display:grid;grid-template-columns:96px 1fr;gap:22px;align-items:center"><div class="portrait {tone}" style="border-radius:60px 60px 4px 4px"><span class="mono" style="font-size:1.8rem">{mono}</span></div><div><h3 style="margin-bottom:2px">{nm}</h3><div class="creds">{cr}</div><p style="margin:6px 0 0">{role}</p></div></a>'
    nxt = SERVICES[(idx + 1) % len(SERVICES)]
    body += f"""
<section class="page-hero">
  {tides(cls="tides", lines=12, seed=idx * 1.3)}
  <div class="wrap" style="position:relative;z-index:2">
    {crumbs(R, trail)}
    <div class="eyebrow">Practice 0{idx + 1} &middot; {s['title']}</div>
    <h1>{d['h1']}</h1>
    <p class="lede mt2">{d['lede']}</p>
    <div class="hero-ctas mt2"><a class="btn btn-primary" href="{R}contact.html">Talk to us about this</a><a class="btn btn-ghost" href="#offers">See how we help</a></div>
  </div>
</section>

<section class="section bg-white">
  <div class="wrap split">
    <div><div class="eyebrow">Is this you?</div><h2>You might be ready for this if&hellip;</h2><p class="muted">Most clients come to us with one of these on their mind. If any of them ring true, it's worth a conversation.</p></div>
    <ul class="signals reveal">{signals}</ul>
  </div>
</section>

<section class="section">
  <div class="wrap split rev">
    <div><div class="eyebrow">What we do</div><h2>The work, in plain terms.</h2><ul class="check reveal">{dos}</ul></div>
    <div class="card" style="background:var(--teal);color:var(--cloud);border:0"><div class="eyebrow" style="color:#CDE0DE">What changes</div><h3 class="serif" style="color:var(--cloud);font-weight:400;font-size:1.6rem">Outcomes our clients look for</h3><ul class="check mt2" style="margin-bottom:0">{outs}</ul></div>
  </div>
</section>

<section class="section bg-paper" id="offers">
  <div class="wrap">
    <div class="section-head"><div class="eyebrow">Signature offers</div><h2>Clear starting points, shaped around you.</h2><p class="lede">Every engagement is scoped to your situation. These are the ways clients most often begin.</p></div>
    <div class="grid g3">{offers}</div>
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
    <div><div class="eyebrow">Who you'll work with</div><h2>Senior people. Every time.</h2><p class="muted">You work directly with our principals, supported by specialists from the <a href="{R}collective.html">CECai Collective</a> when your work calls for it.</p></div>
    <div class="grid" style="gap:16px">{ppl}</div>
  </div>
</section>
"""
    body += faq_block(d["faqs"])
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
            "Five people and organizational advisory practices for CEOs and owners: fractional HR leadership, talent and succession, executive coaching, transformation and AI readiness, and career transition.",
            "services.html", R0, [ORG, listsch, crumb_schema(trail)])
body += header(R0, "services.html")
body += f"""
<section class="page-hero">{tides(lines=12, seed=4)}<div class="wrap" style="position:relative;z-index:2">
{crumbs(R0, trail)}
<div class="eyebrow">Services</div>
<h1>Everything your people strategy needs. <em class="accent">Nothing it doesn't.</em></h1>
<p class="lede mt2">Five connected practices, led by senior people who have done the work inside organizations like yours. Start with one. Add others as your needs change.</p>
</div></section>
<section class="section tight"><div class="wrap grid" style="gap:18px">{cards}</div></section>
<section class="section bg-white"><div class="wrap split even">
  <div><div class="eyebrow">Connected by design</div><h2>Why one firm for all five?</h2></div>
  <div><p class="lede">Because people problems don't arrive one at a time. A succession gap becomes a hiring question. A reorganization becomes a coaching need. An AI rollout becomes a role redesign, and sometimes a transition. When one partner understands your whole picture, nothing falls between the cracks.</p><a class="textlink" href="approach.html">How we work</a></div>
</div></section>
"""
body += cta(R0)
body += footer(R0)
write("services.html", body)
print("services ok")
