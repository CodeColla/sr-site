# sr-site

The **SR Associates** marketing website — FastAPI + Jinja2 + plain HTML/CSS.

> Tagline: **COMPLEXITY. SIMPLIFIED.** · Live domain (target): [srassociates.co](https://srassociates.co)

## Stack

- **FastAPI** (serves the page + handles the contact form)
- **Jinja2** templates (a `base.html` + section partials)
- **Plain CSS** (one stylesheet, CSS variables for the palette). Mobile nav is CSS-only.

## Project layout

```
app/
├── main.py                 # FastAPI app: routes, static mount, /contact handler
├── templates/
│   ├── base.html           # <head>, meta/SEO, nav + footer includes
│   ├── index.html          # includes the section partials
│   └── partials/           # nav, hero, intro, services, why, industries, work, about, contact, footer
└── static/
    ├── css/styles.css
    └── assets/             # favicon.svg, sr-hero-concept.svg (+ og-image / apple-touch-icon to add)
requirements.txt
.env.example                # copy to .env for SMTP (optional)
```

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
# open http://127.0.0.1:8000
```

## Contact form

`POST /contact` validates the fields (with a honeypot for spam) and emails the enquiry.

- If **`SMTP_HOST` is unset**, submissions are **logged to stdout** — nothing is sent. Safe for launch before email is set up.
- To enable email, copy `.env.example` → `.env` and fill the SMTP values (Google Workspace / Zoho), then run with an env loader or export the vars.

## Deploy (production)

Any Python host works. Recommended: **self-host** behind nginx.

```bash
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
# reverse-proxy 80/443 → 8000 with nginx + Let's Encrypt (TLS)
# run under systemd (or a process manager) to keep it alive
```

Point `srassociates.co` DNS at the host. `GET /health` returns `{"status":"ok"}` for uptime checks.

## Assets still to add

- `static/assets/og-image.png` — 1200×630 social share image (navy bg + reversed wordmark + tagline).
- `static/assets/apple-touch-icon.png` — 180×180 icon tile.
- `static/assets/sr-hero-concept.svg` — currently an on-brand **placeholder**; swap for the final hero render (PNG/SVG) when ready and update the `<img>` in `templates/partials/hero.html`.
