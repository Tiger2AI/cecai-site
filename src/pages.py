from common import *
from services import SVC
import datetime

# ---------------- FRONTIER ----------------
R = ""
trail = [("people-and-ai.html", "People & AI")]
faqs = [
  ("What is a Frontier Firm?", "It's Microsoft's term for an organization that uses AI to advance its business strategy and redesign how work gets done, rather than adopting AI for its own sake. Its research describes a progression from people with AI assistants, to human and agent teams, to human-led, agent-operated processes."),
  ("Is this only for large enterprises?", "No. Small and mid-sized organizations can move faster because they have fewer layers. The people questions are the same at any size: which work changes, who is accountable, and how you bring your team with you."),
  ("Will AI mean we need fewer people?", "Sometimes it changes how many people a process needs, and often it changes what those people do. Leading organizations are pushing past efficiency toward growth and better service, and they avoid automating away the entry-level roles that build their future leaders. We help you make these choices deliberately and communicate them honestly."),
  ("Do you sell or implement AI software?", "No. We are vendor-neutral on the people side. We work alongside your technology partners, or recommend them, and focus on roles, structure, skills, accountability, adoption and measurement."),
]
body = head("People & AI | The People Side of AI | CECai", "Get your organization ready for human and AI agent teams. Role redesign, agent accountability, workforce planning, leadership and adoption, from an HR-led team with enterprise AI experience.", "people-and-ai.html", R, [ORG, faq_schema(faqs), crumb_schema(trail)], og_image=photo_url("centre"))
body += header(R, "people-and-ai.html")
body += f"""
<section class="page-hero bg-deep" style="color:var(--cloud)">{tides(stroke="#F0EEE9", lines=14, seed=6, opacity_base=.15)}<div class="wrap" style="position:relative;z-index:2">
<nav class="crumbs" aria-label="Breadcrumb" style="color:rgba(240,238,233,.7)"><a href="index.html" style="color:rgba(240,238,233,.7)">Home</a><span>/</span>People &amp; AI</nav>
<div class="hero-split"><div>
<div class="eyebrow" style="color:#CDE0DE">People &amp; AI &middot; The people side of AI</div>
<h1 style="color:var(--cloud)">AI changes the work. <em class="accent" style="color:var(--brass)">People</em> change the organization.</h1>
<p class="lede mt2" style="color:rgba(240,238,233,.85)">The organizations getting real value from AI aren't the ones with the most tools. They're the ones that redesigned roles, structures and leadership around a new way of working. That's people work, and it's what we do.</p>
<div class="hero-ctas mt2"><a class="btn btn-light" href="contact.html">Book a People &amp; AI Readiness conversation</a></div>
</div>{arch("centre", R)}</div>
</div></section>

<section class="section bg-white"><div class="wrap split">
  <div><div class="eyebrow">The gap</div><h2>Tools are easy. Changing how work gets done is not.</h2></div>
  <div>
    <p class="lede">Leaders everywhere are under pressure to show returns from AI. Gartner reports that 63% of CEOs and senior executives are radically redesigning their operating models to get there, yet only 24% of leadership teams agree on who is accountable for AI agents.</p>
    <p>Microsoft's own research on becoming a Frontier Firm reaches a similar conclusion: tools alone don't change work. The system around them does. Clear goals owned by named executives. Workflows redesigned before agents are added. Managers who model AI use and coach their teams. Honest communication. And critical people decisions kept in human hands.</p>
    <p class="mb0">Every one of those is an HR and organizational design question.</p>
  </div>
</div></section>

<section class="section bg-deep"><div class="wrap">
  <div class="section-head"><div class="eyebrow" style="color:#CDE0DE">Three levels of change</div><h2>Where are you today? Where do you need to be?</h2></div>
  <div class="levels reveal">
    <div class="level"><div class="lv">Level 1</div><h3>Human with assistant</h3><p>Every person has an AI assistant. The work speeds up inside existing roles. We help leaders model use, build confidence and skills, and communicate honestly about what's changing.</p><div class="bar"><i style="width:33%"></i></div></div>
    <div class="level"><div class="lv">Level 2</div><h3>Human and agent teams</h3><p>Agents take on defined tasks under human direction. We redesign roles, name an owner for every agent, set supervision and escalation, and update how you hire and develop people.</p><div class="bar"><i style="width:66%"></i></div></div>
    <div class="level"><div class="lv">Level 3</div><h3>Human-led, agent-operated</h3><p>People set direction while agents run processes end to end. We redesign structure around value streams, create new career paths and keep critical decisions human.</p><div class="bar"><i style="width:100%"></i></div></div>
  </div>
  <p class="small" style="opacity:.55;margin-top:18px">Framework adapted from Microsoft, Becoming a Frontier Firm (second edition, 2026).</p>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><div class="eyebrow">What we help with</div><h2>Six people questions every AI strategy has to answer.</h2></div>
  <div class="grid g3">
    <div class="card reveal"><span class="num">01</span><h3>Which work changes?</h3><p>Map roles and workflows to find where AI adds the most value, and where human judgment must stay.</p></div>
    <div class="card reveal"><span class="num">02</span><h3>Who is accountable?</h3><p>Name an owner for every agent, define supervision and escalation, and make decision rights clear.</p></div>
    <div class="card reveal"><span class="num">03</span><h3>How should we be structured?</h3><p>Redesign teams, spans and layers around end-to-end value rather than legacy functions.</p></div>
    <div class="card reveal"><span class="num">04</span><h3>What skills matter now?</h3><p>Focus on the few skills that differentiate you: judgment, quality control, learning agility and delegating work to agents.</p></div>
    <div class="card reveal"><span class="num">05</span><h3>How do we bring people with us?</h3><p>Communicate honestly, equip managers to coach, and build learning into the flow of work.</p></div>
    <div class="card reveal"><span class="num">06</span><h3>How do we prove value?</h3><p>Measure from adoption to process change to business outcomes, at 90, 180 and 360 days.</p></div>
  </div>
</div></section>

<section class="section bg-white"><div class="wrap split">
  <div class="portrait-frame reveal" style="max-width:360px">{face("SM", R, "brass")}</div>
  <div>
    <div class="eyebrow">Your AI and transformation partner</div>
    <h2>Enterprise AI experience, applied to your scale.</h2>
    <p class="lede">Stuart MacMillan leads our AI and transformation work. He advises enterprise AI programs with more than 100,000 users, and has led change across 22 transformation engagements in 23 years.</p>
    <p>He designs which work agents take on, how humans and agents split the job, who owns and supervises each agent, and how to measure value. Paired with Stephanie's HR leadership, you get both halves of the problem in one team: the technology change and the people change.</p>
    <div class="hero-ctas mt2"><a class="btn btn-primary" href="people/stuart-macmillan.html">About Stuart</a><a class="btn btn-ghost" href="services/transformation-ai-readiness.html">Transformation &amp; AI readiness</a></div>
  </div>
</div></section>

<section class="section bg-paper"><div class="wrap">
  <div class="section-head"><div class="eyebrow">Where to start</div><h2>People &amp; AI Readiness</h2><p class="lede">In four to six weeks we assess where AI will change work in your organization, how ready your leaders, structure and HR systems are, and what to do first. You leave with a 12-month people roadmap your leadership team can act on.</p></div>
  <div class="steps reveal">
    <div class="step"><h3>Ambition</h3><p>Anchor AI to your business goals, with a named executive owner for each.</p></div>
    <div class="step"><h3>Work</h3><p>Map priority roles and workflows. Lean the process before adding agents.</p></div>
    <div class="step"><h3>People</h3><p>Assess leadership, skills, structure, HR policy and change readiness.</p></div>
    <div class="step"><h3>Roadmap</h3><p>Prioritized actions, accountabilities and measures for the next 12 months.</p></div>
  </div>
</div></section>
"""
body += faq_block(faqs, "Questions about AI and your people")
body += cta(R, "Ready to lead the people side of AI?", "Start with a conversation about where you are, where you want to be, and what's standing in the way.")
body += footer(R)
write("people-and-ai.html", body)

# ---------------- APPROACH ----------------
trail = [("approach.html", "How We Work")]
body = head("How We Work | Engagement Models & Principles | CECai", "How CECai works with CEOs, owners and executive teams: advisory retainers, fractional and interim leadership, fixed-scope projects and coaching. Senior people, plain language, practical results.", "approach.html", R, [ORG, crumb_schema(trail)], og_image=photo_url("approach"))
body += header(R, "approach.html")
body += f"""
<section class="page-hero">{tides(lines=12, seed=8)}<div class="wrap" style="position:relative;z-index:2">
{crumbs(R, trail)}
<div class="hero-split"><div>
<div class="eyebrow">How we work</div>
<h1>Warm in how we work. <em class="accent">Clear</em> in what we deliver.</h1>
<p class="lede mt2">We build trust quickly, tell you what we really see, and do the work alongside your leaders. Here's what you can expect from us.</p>
</div>{arch("approach", R)}</div>
</div></section>

<section class="section bg-white"><div class="wrap">
  <div class="section-head"><div class="eyebrow">Our principles</div><h2>Five promises we make to every client.</h2></div>
  <div class="grid g3">
    <div class="card reveal"><span class="num">01</span><h3>Senior people, every time</h3><p>You work with our principals directly. When we bring in a specialist, you'll know who and why.</p></div>
    <div class="card reveal"><span class="num">02</span><h3>Plain language, honest advice</h3><p>We say what we see, kindly and clearly, even when it's not what you hoped to hear.</p></div>
    <div class="card reveal"><span class="num">03</span><h3>Practical over perfect</h3><p>Frameworks that fit your size and pace, built to be used on Monday morning, not admired on a shelf.</p></div>
    <div class="card reveal"><span class="num">04</span><h3>People decisions stay human</h3><p>We use AI to work faster and smarter. Judgment about people stays with people.</p></div>
    <div class="card reveal"><span class="num">05</span><h3>We leave you stronger</h3><p>Every engagement builds your own team's capability, so you need us less over time, not more.</p></div>
    <div class="card reveal" style="background:var(--teal);border-color:var(--teal)"><span class="num" style="color:#E3CFA8">And</span><h3 style="color:var(--cloud)">Discretion, always</h3><p style="color:rgba(240,238,233,.85)">People matters are sensitive. We handle confidential information with care and keep it that way.</p></div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><div class="eyebrow">Engagement models</div><h2>Four ways to work together.</h2></div>
  <div class="models reveal">
    <div class="model"><div class="verb">Advise</div><h3>Strategic HR advisory</h3><p>Monthly retainer. Regular time with you and your executive team, on-call support for urgent issues, and a quarterly people review.</p></div>
    <div class="model"><div class="verb">Lead</div><h3>Fractional &amp; interim</h3><p>We lead your HR function, part-time or full-time through a gap, as a member of your leadership team.</p></div>
    <div class="model"><div class="verb">Build</div><h3>Fixed-scope projects</h3><p>Organization design, succession, HR foundations, AI readiness or restructuring, with a clear scope, timeline and fee.</p></div>
    <div class="model"><div class="verb">Coach</div><h3>Leaders &amp; teams</h3><p>One-to-one executive coaching, leadership team work and manager cohorts, in person or virtual.</p></div>
  </div>
</div></section>

<section class="section bg-paper"><div class="wrap">
  <div class="section-head"><div class="eyebrow">What to expect</div><h2>From hello to results.</h2></div>
  <div class="steps reveal">
    <div class="step"><h3>Conversation</h3><p>Thirty minutes, free. We listen first and tell you honestly whether and how we can help.</p></div>
    <div class="step"><h3>Proposal</h3><p>Within a few days: scope, approach, timeline, team and fee on two pages. No surprises.</p></div>
    <div class="step"><h3>Delivery</h3><p>Regular check-ins, visible progress and early warning if anything needs to change.</p></div>
    <div class="step"><h3>Handover</h3><p>Tools, training and a sustainment plan so your team owns the result.</p></div>
  </div>
</div></section>

<section class="section bg-white"><div class="wrap split even">
  <div><div class="eyebrow">How we use AI</div><h2>AI-powered. Human-led.</h2></div>
  <div><p class="lede">We practise what we advise. We use secure AI tools to research faster, analyze data more deeply and draft more efficiently, which means more of your budget goes to senior judgment and less to busywork.</p><p>Client information is handled confidentially, and no decision about a person is ever made by AI.</p></div>
</div></section>
"""
body += cta(R)
body += footer(R)
write("approach.html", body)
print("frontier/approach ok")

# ---------------- TEAM ----------------
COLLECTIVE = [
  ("Michael McConachie", "Digital, AI & Automation", "PMI CPMAI, MBA", "MM", "moss",
   "A senior technology executive who has led enterprise digital transformation from planning through implementation for Fortune 500 and mid-market organizations in retail, healthcare and finance. Michael brings AI and automation assessments, enterprise platform implementation (ERP, CRM, LIMS, MarTech), integration and global rollout experience, guided by what he calls the Art of Practical AI: accountable results and speed to value. MIT education in AI, digital transformation and AI product design."),
  ("Steve Wakeham", "Digital Change & ERP Transformation", "MEd, PMP, PSM I, Prosci", "SW", "",
   "A business transformation and change leader with more than 20 years of experience, including senior roles at EY, Deloitte and PwC. Steve takes a people-first approach to digital, cloud and Tier-1 ERP transformations across North America and internationally, with expertise in change strategy, operating model and process design, workforce readiness and training, and leadership alignment. Master of Education, McGill University."),
  ("Paul Bellavance", "AI Strategy & People Transformation", "25+ years", "PB", "cocoa",
   "An AI strategy and people transformation expert who helps organizations align their workforce with AI-driven strategies. Paul's experience spans organizational transformation, executive coaching and strategic HR, including large post-merger integrations in Canadian telecom and IT, and government excellence and transformation work across the Gulf region. Partners with CECai and Ryelle Strategy Group."),
  ("Darcy Daoust", "Workplace Protection & Compliance", "Former labour & employment lawyer", "DD", "cocoa",
   "Darcy helps employers prevent, manage and resolve workplace issues involving employment compliance, employee relations, investigations, workplace safety, accommodation and organizational risk. Drawing on his prior experience practising labour and employment law, he brings a legally informed, practical and risk-aware perspective. As Founder and Principal of D&amp;DCPD Workplace Protection &amp; Compliance Group, he provides fractional and on-demand support: policies and workforce documentation, investigations and early resolution, accommodation, WSIB and return to work, and coaching for managers facing difficult decisions. He fills the gap between HR administration and external legal counsel, and knows when a matter needs specialized legal advice. Bilingual English and French, based in Ottawa."),
  ("Carol Kotacka", "Organizational Transformation", "EMBA, Smith School of Business", "CK", "brass",
   "A results-oriented leader in strategy, performance and transformational change across industry, healthcare and not-for-profit organizations in North America, Europe, the Middle East and South America. Managing Director of Ryelle Strategy Group, Adjunct Lecturer at the University of Toronto's Institute of Health Policy, Management and Evaluation, and Lead Facilitator for Queen's University IRC's Organizational Transformation program."),
]

trail = [("team.html", "Team")]
body = head("Our Team | Stephanie Abbott, Stuart MacMillan & the CECai Collective", "Meet CECai's principals, Stephanie Abbott (CPHR, CEC) and Stuart MacMillan (MCMP, CPHR), and the senior specialists of the CECai Collective.", "team.html", R, [ORG, crumb_schema(trail)])
body += header(R, "team.html")
coll = "".join(f'<article class="person reveal">{face(m, R, t, note=False)}<h3 style="margin-bottom:4px">{n}</h3><div class="role">{r}</div><div class="creds" style="margin-bottom:10px">{c}</div><p>{b}</p></article>' for n, r, c, m, t, b in COLLECTIVE)
body += f"""
<section class="page-hero">{tides(lines=12, seed=10)}<div class="wrap" style="position:relative;z-index:2">
{crumbs(R, trail)}
<div class="eyebrow">Our team</div>
<h1>People who have done the work <em class="accent">from the inside.</em></h1>
<p class="lede mt2">Two principals with nearly 50 years of combined HR, change and transformation leadership, backed by a Collective of senior specialists.</p>
</div></section>

<section class="section bg-white"><div class="wrap">
  <div class="grid g2" style="gap:56px">
    <article class="person reveal">
      {face("SA", R, "", "max-width:340px")}
      <h2 style="font-size:2rem;margin-bottom:4px">Stephanie Abbott</h2>
      <div class="creds" style="margin-bottom:8px">CPHR &middot; CEC</div>
      <div class="role">Principal &amp; Managing Partner</div>
      <p>Strategic HR partner, fractional and interim HR leader and Certified Executive Coach. Stephanie has spent 25+ years leading HR at Canadian and multinational organizations, including Lockheed Martin, JPMorgan Chase and Amazon, and advises CEOs, owners and executive teams on organizational design, talent, succession and leadership.</p>
      <a class="textlink" href="people/stephanie-abbott.html">Full profile</a>
    </article>
    <article class="person reveal">
      {face("SM", R, "brass", "max-width:340px")}
      <h2 style="font-size:2rem;margin-bottom:4px">Stuart MacMillan</h2>
      <div class="creds" style="margin-bottom:8px">MCMP &middot; CCMP &middot; CPHR &middot; P.BPM</div>
      <div class="role">Partner, AI &amp; Transformation</div>
      <p>Organizational change and AI adoption leader with 23+ years and 22 enterprise transformation engagements. Stuart advises enterprise AI programs with more than 100,000 users and designs how people and AI agents work together.</p>
      <a class="textlink" href="people/stuart-macmillan.html">Full profile</a>
    </article>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><div class="eyebrow">The CECai Collective</div><h2>Senior specialists, ready when you need them.</h2><p class="lede">Our Collective partners bring Big 4, Fortune 500, legal and global experience in AI, digital, ERP, workplace compliance and organizational transformation. <a href="collective.html">How the Collective works</a>.</p></div>
  <div class="grid g3">{coll}</div>
</div></section>
"""
body += cta(R)
body += footer(R)
write("team.html", body)

# ---------------- PEOPLE ----------------
R = "../"
def person_page(slug, name, creds, role, mono, tone, desc, intro, sections, schema_extra):
    path = f"people/{slug}.html"
    trail = [("team.html", "Team"), (path, name)]
    p = {"@context": "https://schema.org", "@type": "Person", "@id": f"{SITE}/{path}#person", "name": name, "jobTitle": role,
         "worksFor": {"@id": f"{SITE}/#org"}, "url": f"{SITE}/{path}", "address": {"@type": "PostalAddress", "addressRegion": "NB", "addressCountry": "CA"}}
    p.update(schema_extra)
    b = head(f"{name}, {creds} | {role} | CECai", desc, path, R, [p, crumb_schema(trail)], og_type="profile")
    b += header(R, "team.html")
    secs = "".join(f'<div class="reveal" style="margin-bottom:48px"><div class="eyebrow">{h}</div>{c}</div>' for h, c in sections)
    b += f"""
<section class="page-hero">{tides(lines=12, seed=12 if tone else 3)}<div class="wrap" style="position:relative;z-index:2">
{crumbs(R, trail)}
<div class="split" style="align-items:center">
  <div class="portrait-frame" style="max-width:340px">{face(mono, R, tone, eager=True)}</div>
  <div><div class="eyebrow">{role}</div><h1 style="font-size:clamp(2.4rem,5vw,3.6rem)">{name}</h1><div class="creds" style="font-size:.9rem">{creds}</div><p class="lede mt2">{intro}</p></div>
</div>
</div></section>
<section class="section bg-white"><div class="wrap" style="max-width:860px">{secs}</div></section>
"""
    b += cta(R, f"Talk with {name.split()[0]}.", "Start with a 30-minute conversation about what's on your mind.")
    b += footer(R)
    write(path, b)

ul = lambda xs: '<ul class="check">' + "".join(f"<li>{x}</li>" for x in xs) + "</ul>"
person_page("stephanie-abbott", "Stephanie Abbott", "CPHR, CEC", "Principal & Managing Partner", "SA", "",
  "Stephanie Abbott, CPHR, CEC, is CECai's Principal: a strategic HR partner, fractional and interim HR leader and Certified Executive Coach with 25+ years leading HR at Lockheed Martin, JPMorgan Chase, Amazon and more.",
  "Stephanie helps CEOs, owners and executive teams turn strategy into results by building the organizational, leadership and people capability behind it.",
  [("Overview", "<p>Stephanie has spent more than 25 years leading Human Resources at Canadian and multinational organizations, including Lockheed Martin, JPMorgan Chase and Amazon, with 15+ years leading HR functions across multi-region and global organizations. She now brings that experience to organizations that need senior HR leadership without a full-time hire, or that need support quickly.</p><p>Organizations typically bring Stephanie in when they are scaling quickly, integrating an acquisition, restructuring, building HR for the first time, or strengthening an existing HR function. Clients value her ability to build trust quickly, cut through complexity, deliver practical solutions and coach leaders through challenges and change.</p>"),
   ("In her words", '<blockquote class="pull" style="font-size:1.6rem">High-impact Human Resources transforms organizations by building trust, inspiring collaboration and deepening engagement, turning people strategy into sustained performance.</blockquote>'),
   ("How Stephanie works with clients", ul(["<b>Strategic HR advisory.</b> An ongoing advisor to you and your executive team on people, organizational design and leadership decisions.", "<b>Fractional HR leadership.</b> Senior HR leadership, part-time, for organizations that need a strategic HR executive, but not a full-time one.", "<b>Interim HR leadership.</b> Steps in quickly during a leadership gap, restructuring or period of rapid change, keeping the function stable and moving.", "<b>Project-based consulting.</b> Organizational design and effectiveness, workforce and succession planning, talent strategy, leadership development and HR transformation.", "<b>Executive coaching.</b> Certified coaching for senior leaders, leadership transitions and teams."])),
   ("Career highlights", ul(["Head of Human Resources for a Lockheed Martin Canada division and member of its Canadian senior leadership team; led the HR workstream of a multi-phased national reorganization and division-wide succession and workforce planning.", "HR Director across Canada, the U.S. and U.K. for a global safety equipment manufacturer; built a business case that moved U.S. recruitment in-house for $132K in annual savings, and led a market wage strategy that improved recruitment and retention.", "HR Site Lead at an Amazon Canada fulfillment centre, leading a 12-person HR team in a high-volume, complex operation.", "HR Manager and corporate leadership team member for a growing Alberta municipality; rebuilt the HR team and processes and led the people side of a utility acquisition.", "HR and safety leader for a Newell Rubbermaid manufacturing site, with global health and safety audit scores of 97% and 98%, tied for highest worldwide.", "Fractional Head of Global HR for a high-growth technology company, and Director-level HR advisor to municipal and not-for-profit clients through CECai."])),
   ("Experience across sectors", "<p>Defence, energy, financial services, technology, e-commerce, manufacturing, municipal government, and the public and not-for-profit sectors.</p>"),
   ("Credentials", ul(["Chartered Professional in Human Resources (CPHR), CPHR New Brunswick", "Certified Executive Coach (CEC) and Graduate Certificate in Executive Coaching, Royal Roads University", "Bachelor of Business Administration (HR major), Husson University", "Diploma in Business Administration (HR major), Algonquin College"])),
   ("Contact", f'<p><a href="mailto:{EMAIL}">{EMAIL}</a></p>')],
  {"honorificSuffix": "CPHR, CEC", "email": EMAIL, "knowsAbout": ["Fractional HR leadership", "Organizational design", "Succession planning", "Executive coaching", "Workforce planning", "Employee and labour relations", "HR transformation"],
   "hasCredential": [{"@type": "EducationalOccupationalCredential", "name": "Chartered Professional in Human Resources (CPHR)"}, {"@type": "EducationalOccupationalCredential", "name": "Certified Executive Coach (CEC), Royal Roads University"}],
   "alumniOf": [{"@type": "CollegeOrUniversity", "name": "Husson University"}, {"@type": "CollegeOrUniversity", "name": "Royal Roads University"}, {"@type": "CollegeOrUniversity", "name": "Algonquin College"}]})

person_page("stuart-macmillan", "Stuart MacMillan", "MCMP, CCMP, PCACP, CPHR, P.BPM", "Partner, AI & Transformation", "SM", "brass",
  "Stuart MacMillan is CECai's Partner for AI and Transformation: an organizational change and AI adoption leader with 23+ years, 22 enterprise transformations and current enterprise AI programs above 100,000 users.",
  "Stuart helps organizations redesign work for people and AI agents, and makes sure the change actually sticks.",
  [("Overview", "<p>Stuart is an organizational change management and AI adoption leader with more than 23 years leading change and enterprise-scale adoption across the Government of Canada and Fortune-scale private sector organizations, delivered across 22 transformation engagements and user populations from 5,000 to 120,000.</p><p>He currently advises enterprise AI transformation programs for a global industrial conglomerate and a Fortune 20 automotive manufacturer, with 120,000 and 100,000 Microsoft 365 Copilot licences and AI agents in production. His work defines which work agents take on, how humans and agents split the job, who owns and supervises each agent, and the enablement and measurement that make new ways of working stick.</p>"),
   ("What Stuart brings to CECai clients", ul(["<b>Work reinvention, not just tools.</b> Future-state roles, human and agent operating models and AI-enabled workflows tied to business goals.", "<b>Hands-on AI fluency.</b> Designs and builds agentic workflows and AI advisory systems, and turns adoption data into business insight.", "<b>The HR machinery agents collide with.</b> Job analysis, organizational design, staffing, labour relations and performance systems.", "<b>Measurement that holds up.</b> Adoption analytics, business OKRs and cost-per-outcome measurement at 90, 180 and 360 days.", "<b>Bilingual delivery.</b> Facilitates and writes fully in English and French."])),
   ("Selected experience", ul(["Canadian AI Change Principal for Prosci (North America), and author of ValueOS, a value realization operating system for the agentic era.", "Lead AI change consultant for the Microsoft 365 Copilot Pathfinder at the Department of National Defence and Canadian Armed Forces, where 77% of users reported time savings.", "Change lead for a $150M SAP modernization at the Canada Revenue Agency serving 60,000+ employees.", "Lead change consultant for a $50M military HR transformation affecting 100,000+ members, including a 700-member national support network.", "Independent change management assurance, via KPMG, on one of Canada's largest federal transformations.", "Senior advisor to Ceridian (now Dayforce) on its Government of Canada NextGen HR and Pay bid."])),
   ("Credentials and education", ul(["Master Change Management Professional (MCMP) and Certified Change Management Professional (CCMP), ACMP", "Prosci Certified Advanced Change Practitioner (PCACP)", "Chartered Professional in Human Resources (CPHR)", "Business Process Management Professional (P.BPM); Scrum.org PSM, PSPO, PAL-E", "B.B.A., University of New Brunswick; Master Practitioner, Applied Organizational Development, Queen's University IRC", "Executive education in AI strategy: MIT Sloan, INSEAD, Stanford, Cornell and Vanderbilt"])),
   ("Contact", f'<p><a href="mailto:{AI_EMAIL}">{AI_EMAIL}</a></p>')],
  {"honorificSuffix": "MCMP, CCMP, CPHR", "email": AI_EMAIL, "knowsAbout": ["AI adoption", "Organizational change management", "Human and AI agent operating models", "AI value realization", "Prosci ADKAR", "Organizational design"],
   "alumniOf": [{"@type": "CollegeOrUniversity", "name": "University of New Brunswick"}, {"@type": "CollegeOrUniversity", "name": "Queen's University"}]})
print("team/people ok")

# ---------------- COLLECTIVE ----------------
R = ""
trail = [("collective.html", "The CECai Collective")]
body = head("The CECai Collective | Senior Partner Network | CECai", "The CECai Collective is a network of senior specialists in AI, digital, ERP and organizational transformation who extend CECai's HR advisory practice. One trusted lead, a bench of experts.", "collective.html", R, [ORG, crumb_schema(trail)], og_image=photo_url("collective"))
body += header(R, "team.html")
coll = "".join(f'<article class="person reveal">{face(m, R, t, note=False)}<h3 style="margin-bottom:4px">{n}</h3><div class="role">{r}</div><div class="creds" style="margin-bottom:10px">{c}</div><p>{b}</p></article>' for n, r, c, m, t, b in COLLECTIVE)
body += f"""
<section class="page-hero">{tides(lines=12, seed=14)}<div class="wrap" style="position:relative;z-index:2">
{crumbs(R, trail)}
<div class="hero-split"><div>
<div class="eyebrow">The CECai Collective</div>
<h1>One trusted lead. <em class="accent">A bench</em> of senior specialists.</h1>
<p class="lede mt2">Big challenges rarely fit inside one discipline. The Collective lets us bring the right senior expertise to your work, without the overhead of a large organization.</p>
</div>{arch("collective", R)}</div>
</div></section>
<section class="section bg-white"><div class="wrap">
  <div class="grid g3">
    <div class="card reveal"><span class="num">01</span><h3>One relationship</h3><p>Your CECai principal stays your lead and point of accountability for the whole engagement.</p></div>
    <div class="card reveal"><span class="num">02</span><h3>The right expert</h3><p>We bring in Collective partners only when their expertise adds real value, and we tell you why.</p></div>
    <div class="card reveal"><span class="num">03</span><h3>Shared standards</h3><p>Every partner works to the same principles: senior delivery, plain language and confidentiality.</p></div>
  </div>
</div></section>
<section class="section"><div class="wrap">
  <div class="section-head"><div class="eyebrow">Collective partners</div><h2>Meet the specialists.</h2></div>
  <div class="grid g3">{coll}</div>
</div></section>
<section class="section bg-paper"><div class="wrap split even">
  <div><div class="eyebrow">Join the Collective</div><h2>Are you a senior practitioner?</h2></div>
  <div><p class="lede">We're growing the Collective across North America in HR specialties, total rewards, learning, HR technology, AI and change. If you share our standards and want to work on meaningful engagements, we'd like to hear from you.</p><a class="btn btn-primary" href="mailto:{EMAIL}?subject=CECai%20Collective">Introduce yourself</a></div>
</div></section>
"""
body += cta(R)
body += footer(R)
write("collective.html", body)
print("collective ok")
