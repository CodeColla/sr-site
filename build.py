"""Render the Jinja templates to a static site in ./dist for Cloudflare Pages.

Usage:  python build.py
Output: dist/index.html, dist/services/index.html, dist/work/index.html,
        dist/work/<slug>/index.html, dist/about/index.html, dist/blog/index.html,
        dist/blog/<slug>/index.html, dist/contact/index.html, dist/thanks.html
        (rendered from the contact page template, since that's where the form lives),
        dist/static/...

Run this after editing anything under app/templates or app/static, then commit dist/.
"""
from __future__ import annotations

import shutil
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

from app.content.blog_posts import BLOG_POSTS
from app.content.case_studies import CASE_STUDIES
from app.pages import PAGES, get_page

BASE = Path(__file__).resolve().parent
TEMPLATES = BASE / "app" / "templates"
STATIC = BASE / "app" / "static"
DIST = BASE / "dist"

env = Environment(
    loader=FileSystemLoader(str(TEMPLATES)),
    autoescape=select_autoescape(["html", "xml"]),
)


def _write(template_name: str, dist_path: str, **context) -> None:
    html = env.get_template(template_name).render(**context)
    out = DIST / dist_path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(f"  • {dist_path}")


def main() -> None:
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True)

    print("Building static site → dist/")
    for page in PAGES:
        _write(
            page.template, page.dist_path, page=page, sent=False,
            case_studies=CASE_STUDIES, blog_posts=BLOG_POSTS, **page.context,
        )

    contact = get_page("/contact")
    _write(
        contact.template, "thanks.html", page=contact, sent=True,
        case_studies=CASE_STUDIES, blog_posts=BLOG_POSTS, **contact.context,
    )

    shutil.copytree(STATIC, DIST / "static")
    print("  • static/ (assets + css + js)")
    print("Done.")


if __name__ == "__main__":
    main()
