"""Structured case-study data, mirroring 03-Case-Studies/*.md in the parent repo.

Anywhere the source markdown has a `[confirm]` placeholder, the field here is
`None`, never placeholder text. Templates must render each optional field
conditionally so an unconfirmed fact simply doesn't appear on the live site.
When a fact is confirmed (e.g. the Impossible Transformations testimonial),
update it here; no template changes needed.
"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Testimonial:
    quote: str
    name: str
    role: str


@dataclass
class CaseStudy:
    slug: str
    client: str
    sector: str
    pillar: int  # 1 or 2
    pillar_label: str
    tag_label: str
    engagement_type: str
    challenge: str
    what_we_did: list[str]
    outcome: list[str]
    one_liner: str
    teaser: str
    tech: list[str] | None = None
    testimonial: Testimonial | None = None
    card_list: list[str] = field(default_factory=list)  # short tags for the Home teaser card
    live_url: str | None = None  # the real product, when there is one, used for the card image


CASE_STUDIES: list[CaseStudy] = [
    CaseStudy(
        slug="impossible-transformations",
        client="A CXO leadership-coaching firm",
        sector="Leadership & self-transformation programs for CXOs",
        pillar=1,
        pillar_label="Content, Design & Digital Operations",
        tag_label="PILLAR 1",
        engagement_type="Flagship SR engagement, ongoing",
        challenge=(
            "A coaching business at this level needs its brand presence and content to feel "
            "as premium and considered as the programs themselves: consistent social media, "
            "strong written content, professional design, and a podcast that carries their "
            "voice, without an in-house content/design/marketing-ops team to run it."
        ),
        what_we_did=[
            "Content writing: program and brand content across their digital channels.",
            "Social media: planning and producing posts to keep pace with their programs.",
            "Design: visual assets and brand collateral.",
            "Podcast production.",
            "UI/UX consultation on their app, advising on how the app's UI/UX should work "
            "for participants. Consultation only: SR did not build or develop the app itself.",
        ],
        outcome=[
            "A single, trusted partner running the client's content, design and digital operations.",
        ],
        tech=None,
        testimonial=None,
        one_liner=(
            "SR runs content, design and digital operations, including UI/UX consultation "
            "on their app, for a CXO leadership-transformation firm."
        ),
        teaser=(
            "Content writing, social media, design and podcast production, plus UI/UX "
            "consultation on their app. An ongoing engagement."
        ),
        card_list=["Content", "Social media", "Design", "Podcast production", "UX consulting"],
        live_url="https://www.impossibletransformations.com/",
    ),
    CaseStudy(
        slug="proctor-hire",
        client="Proctor Hire",
        sector="HR Tech / Recruitment",
        pillar=2,
        pillar_label="Product & Platform Development",
        tag_label="PILLAR 2",
        engagement_type="SR-linked product, co-founded & built by SR's founding team",
        challenge=(
            "Most hiring software is expensive and heavyweight, overkill (and over-priced) "
            "for many companies that simply need a practical way to run their hiring. The "
            "goal: an affordable hiring platform that genuinely helps move candidates through "
            "the hiring process, without enterprise-tool cost or bloat."
        ),
        what_we_did=[
            "Built end-to-end in a ~2-week span: design and development.",
            "Delivered part-time, by the founders.",
            "Put into real production use inside an enterprise group's own hiring, not a "
            "demo but an actual operating tool.",
        ],
        outcome=[
            "A functional, affordable hiring platform shipped in two weeks, part-time.",
            "In production today, validated against a real hiring use-case (not a prototype).",
            "Solves the original brief: cost-effective hiring that actually helps the process.",
        ],
        tech=None,
        testimonial=None,
        one_liner=(
            "Designed and built Proctor Hire, an affordable hiring platform, in ~2 weeks, "
            "part-time, now in real production use."
        ),
        teaser=(
            "An affordable hiring platform, designed and built solo, part-time, in ~2 weeks. "
            "Live in production today."
        ),
        card_list=["Web app", "Solo build", "In production"],
        live_url="https://proctorhire.com",
    ),
    CaseStudy(
        slug="audit-rail",
        client="Auditrail",
        sector="Compliance & Audit Software",
        pillar=2,
        pillar_label="Product & Platform Development",
        tag_label="PILLAR 2",
        engagement_type="SR-linked product, built by SR's founding team",
        challenge=(
            "Teams that get audited a lot end up re-answering the same compliance "
            "questions for every framework and every auditor: the same controls, the "
            "same evidence, retyped into a new spreadsheet each time, with no single "
            "place holding the controls, evidence, policies and attestations that back "
            "each answer."
        ),
        what_we_did=[
            "Built a compliance and audit workspace around one canonical control "
            "library, where a control is tagged with the framework clauses it satisfies, so "
            "one control answers ISO 27001, SOC 2, and RBI-ITO at once instead of a "
            "separate set per framework.",
            "Seven modules in one tenant-scoped workspace: Audits (import a "
            "customer's checklist, map it to controls, answer it, give auditors "
            "scoped guest access), Controls, Documents (policies and registers "
            "authored and versioned in-app), Evidence (with validity windows so "
            "nothing goes stale unnoticed), Tasks (recurring reviews generated on a "
            "schedule), Registers (risks, assets, third parties, incidents), and "
            "People (access and policy attestation via a magic link, no account "
            "needed).",
        ],
        outcome=[
            "95 canonical controls across 16 domains, mapped to ISO 27001:2022, "
            "SOC 2, and RBI-ITO.",
            "In early use with 100+ users.",
        ],
        tech=None,
        testimonial=None,
        one_liner=(
            "Auditrail is a compliance and audit workspace that lets teams answer a "
            "control once and reuse it across every framework and audit."
        ),
        teaser=(
            "A compliance and audit workspace, with one control library mapped across "
            "ISO 27001, SOC 2, and RBI-ITO. In early use today."
        ),
        card_list=["Compliance workspace", "Multi-framework", "Solo build", "In early use"],
        live_url="https://auditrail.srassociates.co/",
    ),
]


def get_case_study(slug: str) -> CaseStudy | None:
    return next((cs for cs in CASE_STUDIES if cs.slug == slug), None)
