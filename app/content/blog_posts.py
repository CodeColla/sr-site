"""Blog post content, structured the same way as case_studies.py: real,
verified content only, no client-specific or fabricated claims. These first
two posts are about SR's own positioning and process, not any client's work,
so they carry none of the [confirm]-gap risk the case studies do.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class BlogPost:
    slug: str
    title: str
    excerpt: str
    date: str
    read_time: str
    body: list[str]  # paragraphs, rendered one per <p>


BLOG_POSTS: list[BlogPost] = [
    BlogPost(
        slug="how-we-work-discovery-to-handover",
        title="How we work: from discovery call to handover",
        excerpt=(
            "What actually happens when you work with SR, from the first call to the "
            "day your team owns the result."
        ),
        date="September 2026",
        read_time="4 min read",
        body=[
            "Most engagements go wrong before any work starts: a vague brief, an "
            "open-ended scope, a vendor who bills by the hour and has no reason to "
            "hurry. We run a deliberately small number of steps, each with a clear "
            "output, so you always know what happens next and what it costs.",

            "Discovery. A free 30–45 minute call. We're not selling on this call, "
            "we're mapping the problem: what you're trying to achieve, what's "
            "constraining you (budget, timeline, an existing system we have to work "
            "around), and what \"done\" actually looks like, which is the question "
            "that matters most. Half of scoping failures come from two people "
            "picturing a different finish line.",

            "Proposal & SoW. A clear scope, timeline, and fixed price, in writing, "
            "before anything begins. We favor fixed-scope sprints and milestoned "
            "projects over open-ended staffing because it keeps the incentive aligned: "
            "we get paid for a defined outcome, not for hours on a clock. If the scope "
            "changes mid-flight, that's a conversation and a new line item, not a "
            "silent overrun.",

            "Delivery. We build in the open, in regular working increments, with "
            "demos along the way, not a single reveal at the end. If something's "
            "drifting off-target, you see it in week two, not week six.",

            "Handover & support. Code, docs, training, and a runway so your team "
            "actually owns what we built, not a black box only we can touch. Where "
            "it makes sense, that rolls into an optional retainer to keep it running, "
            "but that's a choice you make afterward, not a default we lock you into.",

            "None of this is exotic. It's just the version of \"scoped, senior, "
            "no surprises\" that we'd want if we were the client, which, running our "
            "own content and our own site on the same playbook, we effectively are.",
        ],
    ),
    BlogPost(
        slug="why-we-do-both-content-and-code",
        title="Why we do both content and code",
        excerpt=(
            "Most agencies pick a lane: marketing or development. Here's why SR "
            "runs both, and why that's not a compromise."
        ),
        date="September 2026",
        read_time="3 min read",
        body=[
            "Most agencies specialize narrowly on purpose: a content and marketing "
            "shop, or a development shop, rarely both under one roof. There's a good "
            "reason: the skill sets are genuinely different, and doing either one "
            "well takes real focus.",

            "But for a founder running a growing brand, that specialization becomes "
            "your problem, not theirs. The marketing agency writes the launch copy "
            "and can't touch the landing page it's meant to go on. The dev shop "
            "ships the product and has no view on how anyone finds out it exists. "
            "You end up as the integration layer between two vendors who've never "
            "spoken to each other, chasing updates, translating between them, "
            "owning the gaps neither one is responsible for.",

            "SR runs on two pillars instead: Content, Design & Digital Operations "
            "on one side, Product & Platform Development on the other, one "
            "accountable team across both. Not because either pillar is a "
            "side-hustle to the other (each is a real, fully staffed practice) "
            "but because for a founder-led business, the story and the software "
            "that carries it are rarely separable problems. The site has to say the "
            "right thing and actually work. The campaign has to land somewhere that "
            "converts.",

            "It also means we're not choosing between \"the specialists\" and "
            "\"the generalists.\" You get senior people on both sides, working from "
            "the same brief, without a handoff meeting in between.",

            "We run our own content, our own marketing, and our own site the same "
            "way, same playbook, same two pillars. If it doesn't hold up for us, "
            "we wouldn't offer it to you.",
        ],
    ),
]


def get_blog_post(slug: str) -> BlogPost | None:
    return next((p for p in BLOG_POSTS if p.slug == slug), None)
