"""Page registry — single source of truth for every route.

Both build.py (static generation) and app/main.py (FastAPI dev server) import
this so rendering, routing, and per-page SEO metadata (title/description/
canonical) never have to be hand-duplicated per page.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from app.content.blog_posts import BLOG_POSTS
from app.content.case_studies import CASE_STUDIES

SITE_URL = "https://srassociates.co"


@dataclass
class Page:
    path: str  # URL path, e.g. "/", "/services", "/work/proctor-hire"
    template: str  # template name under app/templates/, e.g. "pages/home.html"
    title: str
    description: str
    context: dict[str, Any] = field(default_factory=dict)

    @property
    def url(self) -> str:
        return f"{SITE_URL}{self.path}"

    @property
    def dist_path(self) -> str:
        """Output path under dist/ — folder + index.html for every page except
        the homepage, so URLs stay clean and a page never collides with a
        same-named directory holding its own children (e.g. /work vs
        /work/proctor-hire)."""
        if self.path == "/":
            return "index.html"
        return f"{self.path.strip('/')}/index.html"


PAGES: list[Page] = [
    Page(
        path="/",
        template="pages/home.html",
        title="SR Associates — Complexity. Simplified.",
        description=(
            "SR is a boutique digital agency & growth partner — content, marketing and "
            "design on one side; custom apps and websites that actually ship on the other."
        ),
    ),
    Page(
        path="/services",
        template="pages/services.html",
        title="Services — SR Associates",
        description=(
            "Two pillars, one senior team: Content, Design & Digital Operations, and "
            "Product & Platform Development. The full SR service catalog."
        ),
    ),
    Page(
        path="/work",
        template="pages/work.html",
        title="Selected Work — SR Associates",
        description="Real engagements, not slideware — case studies from SR's two pillars.",
    ),
    Page(
        path="/about",
        template="pages/about.html",
        title="About — SR Associates",
        description=(
            "SR is a boutique studio founded in 2026, based in Pune, India, serving "
            "clients across India and Australia."
        ),
    ),
    Page(
        path="/blog",
        template="pages/blog.html",
        title="Blog — SR Associates",
        description="Notes on content, marketing, and building software — from the SR team.",
    ),
    Page(
        path="/contact",
        template="pages/contact.html",
        title="Contact — SR Associates",
        description="Have something to build, grow, or tell the world about? Let's talk — the first conversation is free.",
    ),
]

# One page per case study, generated from the single content source so a new
# case study only ever needs an entry in case_studies.py, never a page edit.
for _cs in CASE_STUDIES:
    PAGES.append(
        Page(
            path=f"/work/{_cs.slug}",
            template="pages/case_study.html",
            title=f"{_cs.client} — SR Associates",
            description=_cs.one_liner,
            context={"cs": _cs},
        )
    )

# Same pattern for blog posts — a new post only ever needs an entry in
# blog_posts.py, never a page edit.
for _post in BLOG_POSTS:
    PAGES.append(
        Page(
            path=f"/blog/{_post.slug}",
            template="pages/blog_post.html",
            title=f"{_post.title} — SR Associates",
            description=_post.excerpt,
            context={"post": _post},
        )
    )


def get_page(path: str) -> Page | None:
    return next((p for p in PAGES if p.path == path), None)
