# cecai.ca

Website for CECai, people and organizational advisory in Greater Saint John, New Brunswick.

## Edit something

- **Write an article:** copy `content/templates/article-template.md` into `content/insights/`, rename it `YYYY-MM-DD-your-slug.md`, write it, and remove `draft: true`.
- **Change page wording:** page copy is in `src/` (`home.py`, `services.py`, `pages.py`, `more.py`).
- You can edit any file directly on github.com: open it, click the pencil icon, then **Commit changes**. Choose **Create a new branch and start a pull request** if you want someone to review first.

## Publishing

Every change merged into `main` publishes automatically in about a minute (see the **Actions** tab). Every previous version is kept in the history.

## Build locally (optional)

```
pip install markdown pyyaml
python src/build.py
```

The site is written to `_site/`. Open `_site/index.html` in a browser.
