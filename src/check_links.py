"""Fails the build if any page links to a local file that doesn't exist."""
import os, re, glob, sys
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_site")
bad = []
for f in glob.glob(os.path.join(OUT, "**", "*.html"), recursive=True):
    base = os.path.dirname(f)
    for h in re.findall(r'(?:href|src)="([^"#?]+)', open(f, encoding="utf-8").read()):
        if h.startswith(("http", "mailto:", "tel:")):
            continue
        if not os.path.exists(os.path.normpath(os.path.join(base, h))):
            bad.append(f"{os.path.relpath(f, OUT)} -> {h}")
if bad:
    print("Broken links:\n" + "\n".join(bad)); sys.exit(1)
print("All internal links OK")
