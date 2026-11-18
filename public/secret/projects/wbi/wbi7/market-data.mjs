/* WBI7 — market-data rates proxy (optional)
 *
 * A tiny serverless function that fetches REAL benchmark rates from FRED
 * (Federal Reserve Economic Data) server-side and returns clean JSON to the app.
 * Why a proxy: FRED requires an API key (which must not live in the browser) and
 * browser calls to FRED are blocked by CORS. This runs server-side, keeps the key
 * private, and adds the CORS header the browser needs.
 *
 * It returns exactly the shape the app's MD_parseRates() reads:
 *   { tenYear, twoYear, mortgage30, asOf }
 *
 * --- Deploy (Netlify example) ---
 *   1. Get a free FRED API key: https://fred.stlouisfed.org/docs/api/api_key.html
 *   2. Put this file at  netlify/functions/market-data.mjs
 *   3. In netlify.toml add a redirect:  /api/market-data -> /.netlify/functions/market-data
 *   4. Set the env var  FRED_API_KEY  in your Netlify site settings.
 *   5. In index.html set  WBI7_CLOUD.marketDataUrl = "/api/market-data"
 *
 * Any Node serverless host works; only the handler signature differs.
 *
 * HONEST SCOPE: FRED is free public macro data (Treasuries, mortgage index). It is
 * NOT licensed CRE data — it does not provide submarket cap rates or comparable
 * rents. Those feeds (CoStar, Green Street, RCA, Trepp) are paid and contractual.
 */

const SERIES = { tenYear: "DGS10", twoYear: "DGS2", mortgage30: "MORTGAGE30US" };

async function latestObservation(seriesId, key) {
  const url = "https://api.stlouisfed.org/fred/series/observations"
    + "?series_id=" + seriesId
    + "&api_key=" + key
    + "&file_type=json&sort_order=desc&limit=8"; // last few; skip "." (no value) days
  const r = await fetch(url);
  if (!r.ok) throw new Error("FRED " + seriesId + " HTTP " + r.status);
  const j = await r.json();
  const obs = (j.observations || []).find(o => o.value && o.value !== ".");
  return obs ? { value: Number(obs.value), date: obs.date } : null;
}

async function buildPayload() {
  const key = process.env.FRED_API_KEY;
  if (!key) throw new Error("FRED_API_KEY is not set on the server");
  const out = { asOf: null };
  await Promise.all(Object.entries(SERIES).map(async ([field, id]) => {
    try {
      const o = await latestObservation(id, key);
      if (o) { out[field] = o.value; if (!out.asOf || o.date > out.asOf) out.asOf = o.date; }
    } catch (e) { /* leave the field absent; the app degrades gracefully */ }
  }));
  return out;
}

const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET, OPTIONS",
  "Content-Type": "application/json",
  "Cache-Control": "public, max-age=3600"
};

/* Netlify / AWS-Lambda-style handler */
export async function handler() {
  try {
    const body = await buildPayload();
    return { statusCode: 200, headers: CORS, body: JSON.stringify(body) };
  } catch (e) {
    return { statusCode: 500, headers: CORS, body: JSON.stringify({ error: String(e.message || e) }) };
  }
}

/* Optional: Web-standard (Cloudflare/Deno/Vercel Edge) entry point */
export default async function (request) {
  if (request && request.method === "OPTIONS") return new Response("", { headers: CORS });
  try {
    const body = await buildPayload();
    return new Response(JSON.stringify(body), { headers: CORS });
  } catch (e) {
    return new Response(JSON.stringify({ error: String(e.message || e) }), { status: 500, headers: CORS });
  }
}
