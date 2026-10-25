"""Loads Insights articles from content/insights/*.md (YAML front matter + Markdown body)."""
import os, glob, datetime, yaml, markdown

CONTENT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "insights")
COLORS = {"teal": "var(--teal)", "moss": "var(--moss)", "cocoa": "var(--cocoa)", "brass": "var(--brass)", "teal-deep": "var(--teal-deep)"}


def load():
    items = []
    for i, path in enumerate(sorted(glob.glob(os.path.join(CONTENT, "*.md")))):
        raw = open(path, encoding="utf-8").read()
        if not raw.startswith("---"):
            continue
        _, fm, body = raw.split("---", 2)
        m = yaml.safe_load(fm)
        if m.get("draft"):
            continue
        d = m.get("date")
        d = d if isinstance(d, datetime.date) else datetime.date.fromisoformat(str(d))
        words = len(body.split())
        items.append(dict(
            slug=m["slug"], title=m["title"], tag=m.get("tag", "Insights"), desc=m["description"], teaser=m.get("teaser", m["description"]),
            author=m.get("author", "CECai"), date=d, date_label=d.strftime("%B %Y"),
            minutes=max(2, round(words / 220)), color=COLORS.get(m.get("color", "teal"), "var(--teal)"),
            seed=1.2 + (sum(map(ord, m["slug"])) % 50) / 10, key=m.get("key_points", []),
            sources=[(s["title"], s["url"]) for s in m.get("sources", [])], image=m.get("image"),
            body=markdown.markdown(body.strip(), extensions=["extra", "sane_lists"]),
        ))
    items.sort(key=lambda a: a["date"], reverse=True)
    return items
