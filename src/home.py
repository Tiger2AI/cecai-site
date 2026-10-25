from common import *
from articles import load as load_articles
latest_posts = "".join(f'<a class="post reveal" href="insights/{a["slug"]}.html"><div class="art" style="background:{a["color"]}">{tides(400,150,7,seed=a["seed"],stroke="#F0EEE9",cls="",opacity_base=.25)}</div><div class="body"><div class="meta">{a["tag"]}</div><h3>{a["title"]}</h3><p>{a["teaser"]}</p></div></a>' for a in load_articles()[:3])

R = ""
faqs = [
    ("What does CECai do?",
     "CECai is a people and organizational advisory firm. We give CEOs and business owners senior HR leadership without a full-time hire: strategic HR advice, fractional and interim HR leadership, talent and succession planning, executive coaching, organizational design and AI readiness, and career transition support."),
    ("Who do you work with?",
     "Founders, CEOs, owners and leadership teams of growing, changing and established organizations. That includes owner-led businesses, scale-ups, municipalities, not-for-profits and divisions of national and global companies. Our team has led HR and change in defence, energy, financial services, technology, e-commerce, manufacturing and the public sector."),
    ("What is fractional HR leadership?",
     "Fractional HR leadership means a senior HR executive works with you part-time, often two to eight days a month, as a real member of your leadership team. You get strategic HR judgment and hands-on help at a fraction of the cost of a full-time hire, and you can scale it up or down as you grow."),
    ("Do you only work in New Brunswick?",
     "No. We are based in Greater Saint John and work in person across New Brunswick, Nova Scotia, Prince Edward Island and Newfoundland and Labrador. We support clients across Canada and the United States through hybrid and remote engagements."),
    ("How does AI fit into an HR firm?",
     "AI is changing what jobs contain, how teams are structured and what leaders need to be good at. We help you redesign roles, structures and ways of working for teams of people and AI agents, and we keep the decisions that matter in human hands. Our AI and transformation partner, Stuart MacMillan, advises enterprise AI programs at North American scale."),
    ("How do engagements start?",
     "With a free 30-minute conversation. If there is a fit, we propose a clear scope, timeline and fee, usually within a few days. Many clients start with a short diagnostic or a monthly advisory retainer before moving into a larger piece of work."),
]

schema = [ORG, {"@context": "https://schema.org", "@type": "WebSite", "name": "CECai", "url": SITE + "/", "publisher": {"@id": f"{SITE}/#org"}}, faq_schema(faqs)]

asks = [
    ("We're growing faster than our HR can keep up.", "Fractional HR leadership", "fractional-hr-leadership"),
    ("I need to know who leads when I step back.", "Succession planning", "talent-succession"),
    ("My leaders are capable. They're also running on empty.", "Executive coaching", "executive-coaching"),
    ("Everyone's talking about AI. What does it mean for our people?", "Transformation & AI readiness", "transformation-ai-readiness"),
    ("We have to restructure, and I want to do it right.", "Career transition", "career-transition"),
    ("Our HR is one person and a lot of spreadsheets.", "HR foundations", "fractional-hr-leadership"),
]
ask_html = "".join(f'<a class="ask" href="services/{s}.html"><div><q>{q}</q><small>{l}</small></div><span class="go" aria-hidden="true">&rarr;</span></a>' for q, l, s in asks)

cards = ""
for i, s in enumerate(SERVICES, 1):
    tags = "".join(f'<span class="tag">{t}</span>' for t in s["tags"])
    cards += f'<a class="card link-card practice-card reveal" href="services/{s["slug"]}.html"><span class="num">0{i}</span><h3>{s["title"]}</h3><div class="tags">{tags}</div><p>{s["card"]}</p><span class="textlink">Explore</span></a>'
cards += '<a class="card link-card reveal" href="contact.html" style="background:var(--teal);border-color:var(--teal);color:var(--cloud)"><span class="num" style="color:#E3CFA8">Start here</span><h3 style="color:var(--cloud)">The People Check-Up</h3><p style="color:rgba(240,238,233,.85)">Not sure where to begin? In one focused session we look at your structure, leadership bench, HR basics and AI exposure, and leave you with three clear priorities. No obligation.</p><span class="textlink" style="color:#fff">Book a check-up</span></a>'

body = head("CECai | Fractional HR, Org Design, Coaching & AI Readiness | Saint John, NB",
            "Senior HR leadership for CEOs and business owners. Fractional and interim HR, succession, executive coaching, org design and AI readiness, and career transition. Based in Saint John, serving Atlantic Canada and North America.",
            "index.html", R, schema)
body += header(R, "index.html")
body += f"""
<section class="hero">
  {tides()}
  <div class="wrap">
    <div class="eyebrow">People &amp; organizational advisory &middot; Saint John, New Brunswick</div>
    <h1>The future of work is still <em class="accent">human.</em></h1>
    <p class="lede">CECai helps CEOs and business owners build the leaders, teams and organizations they need for growth, change and the age of AI. Senior HR leadership, exactly when and how you need it.</p>
    <div class="hero-ctas"><a class="btn btn-primary" href="contact.html">Book a conversation</a><a class="btn btn-ghost" href="services.html">Explore our services</a></div>
    <div class="hero-meta"><span>25+ years of senior HR leadership</span><span>Atlantic roots, North American reach</span><span>People first. Frontier ready.</span></div>
  </div>
</section>

<section class="section tight bg-white">
  <div class="wrap">
    <p class="center small muted mb0" style="letter-spacing:.12em;text-transform:uppercase">Our team's experience was built leading HR and change at</p>
    <p class="center serif" style="font-size:clamp(1.1rem,2vw,1.45rem);color:var(--ink-2);margin:14px 0 0;line-height:1.7">Lockheed Martin &nbsp;&middot;&nbsp; JPMorgan Chase &nbsp;&middot;&nbsp; Amazon &nbsp;&middot;&nbsp; Big 4 consulting &nbsp;&middot;&nbsp; Government of Canada &nbsp;&middot;&nbsp; Global defence, energy &amp; manufacturing</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head"><div class="eyebrow">What leaders bring to us</div><h2>Every organization has a people question it can't put off much longer.</h2><p class="lede">Here's what CEOs and owners are telling us right now. If one of these sounds familiar, you're in the right place.</p></div>
    <div class="asks reveal">{ask_html}</div>
  </div>
</section>

<section class="section bg-paper">
  <div class="wrap">
    <div class="section-head"><div class="eyebrow">Our services</div><h2>Five practices. One senior partner who knows your business.</h2><p class="lede">You work with one trusted lead who brings in the right specialists from our network when you need them. No hand-offs to junior teams, no generic playbooks.</p></div>
    <div class="grid g3">{cards}</div>
  </div>
</section>

<section class="section bg-teal">
  <div class="wrap">
    <div class="section-head"><div class="eyebrow">The year ahead</div><h2>2027 will reward organizations that get the people side right.</h2><p style="opacity:.85">CEOs are being asked to grow, adopt AI and manage risk all at once. The research is clear about where that pressure lands: on structure, leadership and trust.</p></div>
    <div class="stats reveal">
      <div class="stat"><b>63%</b><p>of CEOs and senior executives are radically redesigning their operating model to get returns from AI.</p><cite>Gartner, 2026</cite></div>
      <div class="stat"><b>24%</b><p>of leadership teams agree on who is accountable for the AI agents now doing work in their business.</p><cite>Gartner, 2026</cite></div>
      <div class="stat"><b>87%</b><p>of HR leaders have conducted or plan layoffs, and most now see restructuring as a regular event.</p><cite>LHH, 2026</cite></div>
      <div class="stat"><b>25,000</b><p>Atlantic Canadian small businesses are expected to change hands or close as owners retire.</p><cite>APEC</cite></div>
    </div>
  </div>
</section>

<section class="section bg-deep" style="position:relative;overflow:hidden">
  <div class="wrap">
    <div class="split even" style="align-items:end;margin-bottom:56px">
      <div><div class="eyebrow" style="color:#CDE0DE">Frontier work</div><h2>People first.<br><em class="accent" style="color:var(--brass)">Frontier ready.</em></h2></div>
      <div><p style="opacity:.88">Most AI advice starts with the technology. Ours starts with your people. Leading companies are moving from employees using AI assistants, to people working alongside AI agents, to people directing whole processes that agents run. Each step changes job design, structure, accountability and what great leadership looks like. That is HR's work, and it is ours.</p><a class="btn btn-light" href="frontier.html">See how we help</a></div>
    </div>
    <div class="levels reveal">
      <div class="level"><div class="lv">Level 1</div><h3>Every person has an assistant</h3><p>Leaders model AI use. Roles stay the same, the work inside them speeds up. The people task: confidence, skills and honest communication.</p><div class="bar"><i style="width:33%"></i></div></div>
      <div class="level"><div class="lv">Level 2</div><h3>People and agents as teammates</h3><p>Agents take on defined tasks under human direction. The people task: redesign roles, name an accountable owner for every agent, rethink how you hire and develop.</p><div class="bar"><i style="width:66%"></i></div></div>
      <div class="level"><div class="lv">Level 3</div><h3>Human-led, agent-operated</h3><p>People set direction and judge quality while agents run processes end to end. The people task: new structures, new career paths, and critical decisions kept firmly human.</p><div class="bar"><i style="width:100%"></i></div></div>
    </div>
    <p class="small" style="opacity:.55;margin-top:18px">Levels adapted from Microsoft's Frontier Firm research (2026).</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head"><div class="eyebrow">How we engage</div><h2>Four ways to work together. Pick one, or move between them as you grow.</h2></div>
    <div class="models reveal">
      <div class="model"><div class="verb">Advise</div><h3>Strategic HR advisory</h3><p>A monthly retainer that puts a senior HR advisor at the CEO's table for the decisions that matter.</p></div>
      <div class="model"><div class="verb">Lead</div><h3>Fractional &amp; interim</h3><p>We step in as your head of HR, part-time or through a leadership gap, and run the function.</p></div>
      <div class="model"><div class="verb">Build</div><h3>Projects</h3><p>Focused work with a clear end: org design, succession, HR foundations, AI readiness, restructuring.</p></div>
      <div class="model"><div class="verb">Coach</div><h3>Leaders &amp; teams</h3><p>Certified executive coaching for individuals, leadership teams and managers leading through change.</p></div>
    </div>
    <p class="mt2"><a class="textlink" href="approach.html">How our engagements work</a></p>
  </div>
</section>

<section class="section bg-white">
  <div class="wrap split">
    <div class="portrait-frame reveal" style="max-width:380px"><div class="portrait"><span class="mono">SA</span><span class="note">Portrait to come</span></div></div>
    <div>
      <div class="eyebrow">Meet our principal</div>
      <blockquote class="pull">High-impact Human Resources transforms organizations by building trust, inspiring collaboration and deepening engagement, turning people strategy into sustained performance.</blockquote>
      <p class="attrib"><b>Stephanie Abbott, CPHR, CEC</b>Principal &amp; Managing Partner, CECai</p>
      <p class="mt2 muted">Stephanie has spent more than 25 years leading HR at Canadian and multinational organizations, including Lockheed Martin, JPMorgan Chase and Amazon. CEOs bring her in when they are scaling quickly, integrating an acquisition, restructuring, or building HR for the first time. Clients say she builds trust quickly, cuts through complexity and coaches leaders through the hard parts.</p>
      <div class="hero-ctas mt2"><a class="btn btn-primary" href="people/stephanie-abbott.html">Read Stephanie's story</a><a class="btn btn-ghost" href="team.html">Meet the team</a></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap region">
    <div>
      <div class="eyebrow">Where we work</div>
      <h2>Rooted in Saint John. Built for North America.</h2>
      <p class="lede">We know what it takes to lead in Atlantic Canada: tight-knit communities, family-owned businesses, unionized workplaces, bilingual teams and talent that is hard to replace. We bring that understanding, plus global experience, to every client.</p>
    </div>
    <ul class="reach reveal">
      <li><b>Atlantic Canada</b><span>In person across New Brunswick, Nova Scotia, Prince Edward Island and Newfoundland and Labrador.</span></li>
      <li><b>Across Canada</b><span>Hybrid engagements with private, public and not-for-profit organizations from Iqaluit to Ottawa to Alberta.</span></li>
      <li><b>United States</b><span>Remote and on-site work, with experience leading HR across Canadian, U.S. and U.K. operations.</span></li>
      <li><b>Bilingual</b><span>Advisory and facilitation available in English and French.</span></li>
    </ul>
  </div>
</section>

<section class="section bg-paper">
  <div class="wrap">
    <div class="split even" style="align-items:end">
      <div><div class="eyebrow">The CECai Collective</div><h2>One trusted lead. A bench of senior specialists.</h2></div>
      <div><p class="lede">When your needs go beyond HR, we bring in partners with Big 4, Fortune 500 and global transformation experience in AI, digital, ERP, workplace compliance and organizational change. You keep one relationship and one point of accountability.</p><a class="textlink" href="collective.html">Meet the Collective</a></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head"><div class="eyebrow">Insights</div><h2>Practical thinking for the year ahead.</h2></div>
    <div class="grid g3">
{latest_posts}
    </div>
  </div>
</section>
"""
body += faq_block(faqs)
body += cta(R)
body += footer(R)
write("index.html", body)
print("home ok")
