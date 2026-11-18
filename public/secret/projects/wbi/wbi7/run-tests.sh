#!/usr/bin/env bash
# ============================================================================
# WBI7 — run all test suites in one command.
#
#   ./run-tests.sh
#
# Requires: node (>=18).
#  - Pure-Node suites run always.
#  - The DOM suites (dom_golden, ui_features) need jsdom:  npm i jsdom
#  - The optional puppeteer browser harness inside wbi7_test.js runs only when
#    CHROME_PATH is set (npm i puppeteer-core); it is skipped otherwise.
#
#   CHROME_PATH=/path/to/chrome ./run-tests.sh   # also run the browser harness
# ============================================================================
set -u
cd "$(dirname "$0")"

# Auto-detect a local Chrome if CHROME_PATH not provided (best-effort).
if [ -z "${CHROME_PATH:-}" ]; then
  for c in \
    "$HOME/.cache/puppeteer/chrome/"*/chrome-linux64/chrome \
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
    "/usr/bin/google-chrome" "/usr/bin/chromium" "/usr/bin/chromium-browser"; do
    [ -x "$c" ] && export CHROME_PATH="$c" && break
  done
fi

WBI7_PATH="${WBI7_PATH:-./index.html}"
export WBI7_PATH
fail=0
run () { # <label> <cmd...>
  local label="$1"; shift
  printf '\n=== %s ===\n' "$label"
  if "$@"; then :; else fail=1; fi
}

# Pure-Node suites (no browser, no jsdom)
run "engine analytic (Part A)"  node wbi7_test.js
run "after-tax"                 node aftertax_tests.js
run "new features (engine)"     node feature_tests.js
run "portfolio roll-up"         node portfolio_tests.js
run "development pro forma"      node development_tests.js
run "hold-period analysis"       node holdperiod_tests.js
run "scenario compare"           node compare_tests.js
run "mezzanine overlay"          node mezz_tests.js
run "floating-rate (ARM)"        node floating_tests.js
run "prepayment penalty"         node prepay_tests.js
run "assumption confidence"      node confidence_tests.js
run "capital-structure optimizer" node optimize_tests.js
run "pre-mortem / kill-zone"     node killzone_tests.js
run "two-way sensitivity table"  node senstable_tests.js
run "model health check"         node health_tests.js
run "value-creation bridge"      node valuebridge_tests.js
run "break-even / margin"        node breakeven_tests.js
run "monthly ledger"             node ledger_tests.js
run "prop 13 reassessment"       node prop13_tests.js
run "loan maturity / balloon"    node maturity_tests.js
run "gp catch-up / clawback"     node waterfall_catchup_tests.js
run "sponsor fees"               node fees_tests.js
run "stepped rent schedules"     node steprent_tests.js
run "version diff / attribution" node versiondiff_tests.js
run "actuals vs underwriting"    node actuals_tests.js
run "climate / insurance stress" node climate_tests.js

# DOM suites — browser-free golden + UI smoke, via jsdom
if node -e "require('jsdom')" >/dev/null 2>&1; then
  run "DOM golden (jsdom)"      node dom_golden.js
  run "UI features (jsdom)"     node ui_features.js
  run "deal file I/O (jsdom)"   node fileio_tests.js
  run "market data (jsdom)"     node marketdata_tests.js
else
  printf '\n=== DOM suites: SKIPPED (run `npm i jsdom` to enable) ===\n'
fi

printf '\n----------------------------------------\n'
if [ "$fail" -eq 0 ]; then
  printf 'ALL SUITES PASSED \xE2\x9C\x93\n'; exit 0
else
  printf 'SOME SUITES FAILED \xE2\x9C\x97\n'; exit 1
fi
