#!/usr/bin/env node
/* =====================================================================
   WBI6 — Golden-Master Regression Test Harness
   ---------------------------------------------------------------------
   Loads wbi6.html in a headless browser, drives the real engine, and
   asserts (a) locked "golden" output values for both built-in presets and
   (b) structural invariants that must hold for any valid deal. Catches the
   class of silent regression (e.g. a render/translate bug blanking every
   output cell) that manual spot-checking misses.

   USAGE:
     CHROME_PATH=/path/to/chrome  node wbi6.test.js
     (optional)  WBI6_PATH=./wbi6.html
   On macOS, CHROME_PATH is typically:
     "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
   Requires:  npm i puppeteer-core
   Exit code 0 = all pass, 1 = any failure (CI-friendly).
   ===================================================================== */
const path=require('path');
let puppeteer; try{puppeteer=require('puppeteer-core');}catch(e){
  console.error('Missing dependency: run  npm i puppeteer-core');process.exit(2);}
const CHROME=process.env.CHROME_PATH;
const HTML=process.env.WBI6_PATH||path.resolve(__dirname,'wbi6.html');
if(!CHROME){console.error('Set CHROME_PATH to your Chrome/Chromium binary.');process.exit(2);}
const URL='file://'+path.resolve(HTML);
const sleep=ms=>new Promise(r=>setTimeout(r,ms));

// ---- golden values (locked from a verified build) ----
const DISPLAY_GOLDENS={
  evans:{goinCapVal:'7.8%',irrVal:'14.2%',uIrrVal:'10.2%',emVal:'3.37×',
         dyStabVal:'12.1%',mirrVal:'13.2%',lpIrrVal:'13.6%',gpIrrVal:'18.2%',dealIrrVal:'14.2%'},
  elder:{goinCapVal:'7.3%',irrVal:'12.2%',uIrrVal:'9.7%',emVal:'2.46×',
         dy1Val:'15.0%',mirrVal:'11.1%',lpIrrVal:'11.8%',gpIrrVal:'15.2%',capShiftVal:'+20 bps'}
};
const RAW_GOLDENS={  // [expected, absoluteTolerance]
  evans:{goinCap:[0.07813,5e-4],stabOpex:[923241.92,1],stabNOI:[668399.68,1],irr:[0.14179,1e-3]},
  elder:{goinCap:[0.072966,5e-4],stabOpex:[146016,1],stabNOI:[511056,1],irr:[0.122152,1e-3]}
};

let pass=0,fail=0;
const ok=(name,cond,extra)=>{cond?pass++:fail++;console.log((cond?'  PASS  ':'  FAIL  ')+name+(extra&&!cond?'  -> '+extra:''));};

(async()=>{
  const b=await puppeteer.launch({executablePath:CHROME,headless:'new',
    args:['--no-sandbox','--disable-setuid-sandbox','--disable-dev-shm-usage']});
  const p=await b.newPage();
  await p.evaluateOnNewDocument(()=>{try{localStorage.clear()}catch(e){}});
  await p.goto(URL,{waitUntil:'domcontentloaded'});

  // gate: wrong key must NOT destroy the page; right key opens app
  await p.type('#gatekey','nope'); await p.click('#gatego'); await sleep(250);
  ok('gate: wrong key leaves page intact', await p.evaluate(()=>!!document.getElementById('gatekey')));
  await p.evaluate(()=>{document.getElementById('gatekey').value='';});
  await p.type('#gatekey','wbi6'); await p.click('#gatego'); await sleep(700);
  ok('gate: correct key opens app', await p.evaluate(()=>{const a=document.getElementById('app');return a&&!a.classList.contains('hidden');}));

  const txt=(id)=>p.evaluate(i=>{const e=document.getElementById(i);return e?e.textContent:null;},id);

  for(const preset of Object.keys(DISPLAY_GOLDENS)){
    console.log('\n--- preset: '+preset+' ---');
    await p.select('#presetSel',preset); await sleep(500);
    // (a) display goldens
    for(const [id,want] of Object.entries(DISPLAY_GOLDENS[preset])){
      const got=await txt(id); ok(`${preset}.${id} == "${want}"`, got===want, `got "${got}"`);
    }
    // (b) raw goldens + invariants via exposed engine
    const d=await p.evaluate(()=>{const r=window.__wbi6.runDeal(window.__wbi6.baseParams());
      return {goinCap:r.goinCap,irr:r.irr,uIrr:r.uIrr,mirr:r.mirr,dy1:r.dy1,lpIrr:r.lpIrr,gpIrr:r.gpIrr,
        stabOpex:r.stabOpex,stabNOI:r.stabNOI,profit:r.profit,lpProfit:r.lpProfit,gpProfit:r.gpProfit};});
    for(const [k,[exp,tol]] of Object.entries(RAW_GOLDENS[preset])){
      ok(`${preset}.${k} ≈ ${exp}`, Math.abs(d[k]-exp)<=tol, `got ${d[k]}`);
    }
    ok(`${preset}: unlevered IRR < levered IRR (positive leverage)`, d.uIrr<d.irr, `${d.uIrr} vs ${d.irr}`);
    ok(`${preset}: LP IRR < deal IRR < GP IRR (promote)`, d.lpIrr<d.irr && d.irr<d.gpIrr, `${d.lpIrr}/${d.irr}/${d.gpIrr}`);
    ok(`${preset}: MIRR always defined`, d.mirr!==null && isFinite(d.mirr));
    ok(`${preset}: waterfall conserves cash (LP+GP profit == deal profit)`, Math.abs(d.lpProfit+d.gpProfit-d.profit)<1, `Δ=${(d.lpProfit+d.gpProfit-d.profit).toFixed(2)}`);
  }

  await b.close();
  console.log(`\n${pass} passed, ${fail} failed.`);
  process.exit(fail?1:0);
})().catch(e=>{console.error('Harness error:',e.message);process.exit(2);});
