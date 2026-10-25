"""Builds the CECai site into ../_site. Run: python src/build.py"""
import os, shutil, sys, runpy
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from common import OUT
if os.path.exists(OUT):
    shutil.rmtree(OUT)
shutil.copytree(os.path.join(HERE, "..", "static"), OUT)
for mod in ["home", "services", "pages", "more"]:
    runpy.run_path(os.path.join(HERE, mod + ".py"), run_name="__main__")
open(os.path.join(OUT, ".nojekyll"), "w").close()
print("Built to", os.path.abspath(OUT))
