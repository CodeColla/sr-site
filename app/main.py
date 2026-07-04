"""SR Associates — marketing site (FastAPI + Jinja2 + plain HTML/CSS)."""
from __future__ import annotations

import os
import smtplib
from email.message import EmailMessage
from pathlib import Path

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="SR Associates", docs_url=None, redoc_url=None, openapi_url=None)
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request, sent: bool = False):
    return templates.TemplateResponse(request, "index.html", {"sent": sent})


@app.post("/contact")
async def contact(
    name: str = Form(...),
    email: str = Form(...),
    message: str = Form(...),
    company: str = Form(""),
    website: str = Form(""),  # honeypot — real users never fill this
):
    # Bots tend to fill every field; if the honeypot has content, drop it silently.
    if website.strip():
        return RedirectResponse("/?sent=1#contact", status_code=303)

    _deliver(name=name, email=email, company=company, message=message)
    return RedirectResponse("/?sent=1#contact", status_code=303)


@app.get("/health")
async def health():
    return {"status": "ok"}


def _deliver(*, name: str, email: str, company: str, message: str) -> None:
    """Email the enquiry. If SMTP isn't configured, log it so nothing is lost."""
    host = os.getenv("SMTP_HOST")
    to_addr = os.getenv("CONTACT_TO", "hello@srassociates.co")

    if not host:
        print(f"[contact] {name} <{email}> ({company or '—'}): {message}", flush=True)
        return

    user = os.getenv("SMTP_USER")
    password = os.getenv("SMTP_PASS")
    from_addr = os.getenv("SMTP_FROM", user or to_addr)

    msg = EmailMessage()
    msg["Subject"] = f"New enquiry from {name}"
    msg["From"] = from_addr
    msg["To"] = to_addr
    msg["Reply-To"] = email
    msg.set_content(
        f"Name:    {name}\n"
        f"Email:   {email}\n"
        f"Company: {company or '—'}\n\n"
        f"{message}\n"
    )

    try:
        with smtplib.SMTP(host, int(os.getenv("SMTP_PORT", "587"))) as server:
            server.starttls()
            if user and password:
                server.login(user, password)
            server.send_message(msg)
    except Exception as exc:  # never 500 the visitor because email failed
        print(f"[contact] email send failed: {exc}")
