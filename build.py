"""Render the Jinja templates to a static site in ./dist for Cloudflare Pages.

Usage:  python build.py
Output: dist/index.html, dist/thanks.html, dist/static/...

Run this after editing anything under app/templates or app/static, then commit dist/.
"""
from __future__ import annotations

import shutil
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

BASE = Path(__file__).resolve().parent
TEMPLATES = BASE / "app" / "templates"
STATIC = BASE / "app" / "static"
DIST = BASE / "dist"

env = Environment(
    loader=FileSystemLoader(str(TEMPLATES)),
    autoescape=select_autoescape(["html", "xml"]),
)


def _write(page: str, **context) -> None:
    html = env.get_template("index.html").render(**context)
    (DIST / page).write_text(html, encoding="utf-8")
    print(f"  • {page}")


def main() -> None:
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True)

    print("Building static site → dist/")
    _write("index.html", sent=False)   # form shown
    _write("thanks.html", sent=True)    # post-submit success page

    shutil.copytree(STATIC, DIST / "static")
    print("  • static/ (assets + css)")
    print("Done.")


if __name__ == "__main__":
    main()
