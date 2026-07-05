# sr-site

The **SR Associates** marketing website.
Source is templated (FastAPI + Jinja2 for local dev); it builds to a **static site** in `dist/` that is deployed on **Cloudflare Pages**.

> Tagline: **COMPLEXITY. SIMPLIFIED.** · Domain: [srassociates.co](https://srassociates.co)

## How it fits together

- **Author** in `app/templates/` (a `base.html` + section partials) and `app/static/` (CSS + assets).
- **Preview locally** with FastAPI (live reload), or by serving `dist/`.
- **Build** with `python build.py` → renders `dist/index.html`, `dist/thanks.html`, and copies `dist/static/`.
- **Deploy**: Cloudflare Pages serves the committed `dist/` folder. The contact form posts to **Web3Forms** (no backend needed).

```
app/
├── main.py                 # FastAPI dev server (optional, for local preview)
├── templates/              # base.html, index.html, partials/*
└── static/                 # css/, assets/ (favicon, hero placeholder)
build.py                    # renders templates → dist/  (run before committing)
dist/                       # generated static site (committed; Cloudflare serves this)
requirements.txt
```

## Local preview

Templated dev server (live reload):
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload          # http://127.0.0.1:8000
```

Or preview the built static output:
```bash
python build.py
cd dist && python -m http.server 8000  # http://127.0.0.1:8000
```

## Build

```bash
python build.py     # regenerate dist/ after ANY change to templates or static assets
```
Then commit `dist/` so Cloudflare publishes the update.

## Contact form (Web3Forms)

The form in `app/templates/partials/contact.html` posts to Web3Forms (free, no backend).
1. Sign up at **https://web3forms.com** with the email that should receive enquiries (e.g. `hello@srassociates.co`).
2. Copy your **Access Key** and replace `YOUR_WEB3FORMS_ACCESS_KEY` in `contact.html`.
3. `python build.py` and commit. Submissions redirect to `/thanks`.

## Deploy — Cloudflare Pages

1. Push this repo to GitHub (`CodeColla/sr-site`).
2. Cloudflare dashboard → **Workers & Pages → Create → Pages → Connect to Git** → pick `sr-site`.
3. Build settings: **Framework preset: None**, **Build command: _(leave empty)_**, **Build output directory: `dist`**.
4. Deploy. You get a `*.pages.dev` URL immediately.
5. **Custom domain**: Pages → your project → **Custom domains → Set up** → `srassociates.co` (and `www`). Cloudflare adds the DNS + TLS automatically (fastest if the domain's nameservers are on Cloudflare).

> Optional (auto-build instead of committing `dist/`): set Build command to
> `pip install -r requirements.txt && python build.py` and gitignore `dist/`.

## Assets still to add

- `static/assets/og-image.png` — 1200×630 social share image.
- `static/assets/apple-touch-icon.png` — 180×180 icon.
- `static/assets/sr-hero-concept.svg` — on-brand **placeholder**; swap for the final hero render and update `partials/hero.html`.
