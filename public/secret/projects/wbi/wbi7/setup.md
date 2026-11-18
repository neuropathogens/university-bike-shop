# WBI7 — Backend Setup (cloud sync, sharing, live rates)

WBI7 runs as a **single standalone HTML file** with no backend. Everything below is
**optional** and only needed if you want: sign-in, deals saved to the cloud and
reachable from any device, sharing deals with colleagues (with real permissions),
and live benchmark interest rates.

When the cloud block is left blank (the default), the file behaves exactly as the
standalone app: scenarios live in your browser's `localStorage`, and the Cloud /
Live-rates buttons stay hidden.

> **Verification note.** The app engine and UI are tested in a real browser
> (200+ assertions). The cloud/server pieces below talk to Supabase and Netlify,
> which can't be exercised from where this was built — the function's data
> transform and the standalone fallback are unit-tested, but the live Supabase
> auth/sync path is exercised for the first time by **you** during setup. You'll
> create the accounts and paste the keys yourself (I can't enter credentials on
> your behalf).

---

## What each piece does

| Need | Solved by |
|---|---|
| Real login / sessions | **Supabase Auth** (magic-link email sign-in) |
| Deals saved + reachable from any device | **Supabase** `deals` table |
| Share deals with permissions (viewer/editor) | **Supabase** `deal_shares` + Row-Level Security |
| Live interest rates without leaking an API key | **Netlify Function** proxy to FRED |

True CRE **transaction comps** (CoStar, etc.) are paid/gated and are intentionally
not included — the rates proxy returns Treasuries, SOFR, Fed funds, and the Freddie
30Y mortgage rate, which are free via FRED.

---

## Part A — Supabase (auth + cloud deals + sharing)

1. Create a free project at <https://supabase.com> (Dashboard → New project).
2. In the project, open **SQL Editor → New query**, paste the entire contents of
   `backend/supabase/schema.sql`, and **Run**. This creates the `deals` and
   `deal_shares` tables, the RLS policies, and helper functions. It's safe to re-run.
3. Get your project's public keys: **Project Settings → API**:
   - **Project URL** (looks like `https://abcd1234.supabase.co`)
   - **anon public** key (a long JWT). This key is *designed to be public* and
     safe to ship in the browser — RLS is what protects the data.
4. (Email) By default Supabase sends magic-link emails via its built-in service,
   which is fine for testing. For production, set up your own SMTP under
   **Authentication → Providers → Email**. Also add your site's URL under
   **Authentication → URL Configuration → Redirect URLs** (e.g.
   `https://your-site.netlify.app` and `http://localhost:8888` for local dev).

### Turn it on in WBI7
Open `index.html`, find this line near the top of the `<script>` (search for
`WBI7_CLOUD`):

```js
const WBI7_CLOUD={url:"",anonKey:"",marketDataUrl:""};
```

Fill it in:

```js
const WBI7_CLOUD={
  url:"https://abcd1234.supabase.co",
  anonKey:"eyJhbGciOi...your anon public key...",
  marketDataUrl:"/api/market-data"   // leave "" if you aren't deploying the rates proxy
};
```

Reload. A **☁ Cloud** button appears in the top bar → sign in with your email →
"Save current to cloud", load any saved deal, and share by email.

> **Important — serve it over http(s), not `file://`.** Magic-link sign-in
> redirects back to the page's URL, and Supabase only allows real
> `http(s)` redirect URLs. So cloud login won't work if you just double-click
> `index.html` (a `file://` path). Run it from `http://localhost:8888`
> (`netlify dev`, see Part B) or any hosted URL, and add that URL under
> **Authentication → URL Configuration → Redirect URLs** in Supabase. The
> standalone app (no cloud) still works fine straight from `file://`.

**Sharing:** the person you share with must have signed into the app at least once
(so their account exists). Enter their email, pick Viewer or Editor, Share. RLS
enforces it server-side: viewers can open but not overwrite; editors can save
changes; only the owner can delete.

---

## Part B — Netlify (hosting + live-rates proxy)

You can skip this and still use cloud sync (just set `marketDataUrl:""`). Do this
part if you want the **Live rates** button and a hosted URL. *(The
`market-data.mjs` proxy file isn't included in this bundle — ask for it or supply
your own; it's a ~30-line function that calls FRED with a server-side key.)*

1. Get a free FRED API key: <https://fredaccount.stlouisfed.org/apikeys>.
2. Put your files in a folder like:
   ```
   your-repo/
     public/index.html
     netlify/functions/market-data.mjs
     netlify.toml
   ```
   (Copy `index.html` into `public/`. `netlify.toml` already points `publish` there.)
3. Deploy: connect the repo at <https://app.netlify.com>, **or** run locally:
   ```
   npm i -g netlify-cli
   netlify dev          # serves site + functions at http://localhost:8888
   ```
4. Set the server-only key: **Site settings → Environment variables** →
   `FRED_API_KEY = your_key`. (Locally, `export FRED_API_KEY=your_key` before
   `netlify dev`, or put it in a `.env` file.)
5. The function is exposed at `/api/market-data` (via the redirect in
   `netlify.toml`). With `marketDataUrl:"/api/market-data"` set in `index.html`,
   the **Live rates** button will populate current Treasury/SOFR/mortgage rates.

### Verify the proxy
```
curl http://localhost:8888/api/market-data
```
Returns JSON like `{"rates":{"ust10y":{"label":"10-Year Treasury","value":0.0425,...}}}`
(values are decimals: 0.0425 = 4.25%).

---

## Files in this bundle

```
backend/
  supabase/schema.sql   -- run once in the Supabase SQL editor (cloud save + sharing)
SETUP.md                -- this file
```

The optional **live-rates proxy** (a tiny Netlify Function over FRED, Part B) is
*not* included in this bundle — it's only needed for the "Live rates" button, not
for cloud save. The app already calls `marketDataUrl` if you set it; ask for the
`netlify.toml` + `market-data.mjs` proxy files (or write your own) when you want
that feature.

## Security notes
- The **anon key is public by design**; never put the Supabase *service-role* key
  in the browser. All access control is via RLS (already in `schema.sql`).
- The **FRED key is server-only** — it lives in a Netlify env var and is never sent
  to the browser, which is the whole reason the proxy exists.
- Signed out or offline, WBI7 silently falls back to `localStorage`; your data
  stays on your machine and the app keeps working.
