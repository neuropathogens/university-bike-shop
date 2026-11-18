/* WBI7 — tests for the live-market-data processing logic, with FIXTURE API
   responses (the live network fetch is user-verified on first run; these lock the
   parsing + suggestion logic that turns raw API JSON into market context). Loads
   index.html in jsdom and exercises the exported MD_* pure functions. */
const fs=require('fs'),path=require('path');
const {JSDOM}=require('jsdom');
const HTML=process.env.WBI7_PATH||path.resolve(__dirname,'index.html');
const html=fs.readFileSync(HTML,'utf8');
let pass=0,fail=0;
const ok=(n,c,x)=>{c?pass++:fail++;console.log((c?'  PASS  ':'  FAIL  ')+n+(c?'':'  -> '+x));};
const near=(a,b,t)=>Math.abs(a-b)<=t;

const dom=new JSDOM(html,{runScripts:"dangerously",url:"http://localhost/",pretendToBeVisual:true});
const {window}=dom;
window.requestAnimationFrame=cb=>setTimeout(cb,0);

function run(){
  const w=window.__wbi7;
  if(!w){ok('window.__wbi7 present',false,'missing');return finish();}

  console.log('--- Live market data (parsers) ---');

  // a realistic US Census ACS5 response: [headers, values]
  const censusFixture=[
    ["NAME","B01003_001E","B19013_001E","B25064_001E","B25003_002E","B25003_003E","state","county"],
    ["Alameda County, California","1648556","112879","1845","320000","260000","06","001"]];

  // 1) Census parsing extracts the right fields and derives renter share
  {const m=w.MD_parseCensus(censusFixture);
   ok('census: county name parsed',m&&m.name==="Alameda County, California",m&&m.name);
   ok('census: population parsed',m.population===1648556,m.population);
   ok('census: median household income parsed',m.medianHouseholdIncome===112879,m.medianHouseholdIncome);
   ok('census: median gross rent parsed',m.medianGrossRent===1845,m.medianGrossRent);
   ok('census: renter share derived = renter/(owner+renter)',near(m.renterShare,260000/580000,1e-9),m.renterShare);}

  // 2) Census null sentinels (large negatives) become null, not garbage numbers
  {const f=[["NAME","B01003_001E","B19013_001E","B25064_001E","B25003_002E","B25003_003E"],
            ["Loving County, Texas","64","-666666666","-666666666","20","5"]];
   const m=w.MD_parseCensus(f);
   ok('census: suppressed income (-666666666) -> null',m.medianHouseholdIncome===null,String(m.medianHouseholdIncome));
   ok('census: suppressed rent -> null',m.medianGrossRent===null,String(m.medianGrossRent));
   ok('census: valid population still parsed alongside nulls',m.population===64,m.population);}

  // 3) Census malformed / empty input -> null (graceful)
  {ok('census: empty array -> null',w.MD_parseCensus([])===null,'');
   ok('census: header only -> null',w.MD_parseCensus([["NAME"]])===null,'');
   ok('census: non-array -> null',w.MD_parseCensus(null)===null&&w.MD_parseCensus({})===null,'');}

  // 4) Rates parsing accepts the proxy shape and FRED-style keys
  {const r=w.MD_parseRates({tenYear:4.31,twoYear:4.78,mortgage30:6.85});
   ok('rates: proxy shape parsed',r&&near(r.tenYear,4.31,1e-9)&&near(r.mortgage30,6.85,1e-9),JSON.stringify(r));
   const r2=w.MD_parseRates({DGS10:"4.10",DGS2:"4.60"});
   ok('rates: FRED-style keys parsed (strings ok)',r2&&near(r2.tenYear,4.10,1e-9)&&near(r2.twoYear,4.60,1e-9),JSON.stringify(r2));
   ok('rates: empty object -> null',w.MD_parseRates({})===null,'');
   ok('rates: null -> null',w.MD_parseRates(null)===null,'');}

  // 5) Suggestions turn metrics+rates into honest context strings
  {const m=w.MD_parseCensus(censusFixture);
   const notes=w.MD_suggest(m,{tenYear:4.30},{exit:{exitCap:0.065}});
   ok('suggest: mentions median gross rent',notes.some(n=>/median gross rent/i.test(n)),'');
   ok('suggest: labels rent as coarse, not a comp',notes.some(n=>/not a comp/i.test(n)),'');
   ok('suggest: computes the exit-cap spread over the 10-yr',notes.some(n=>/bps spread/i.test(n)&&/20 bps/.test(n)),JSON.stringify(notes));
   ok('suggest: handles null metrics gracefully',Array.isArray(w.MD_suggest(null,null,{}))&&w.MD_suggest(null,null,{}).length===0,'');}

  finish();
}
function finish(){console.log('\n'+pass+' passed, '+fail+' failed.');process.exit(fail?1:0);}
setTimeout(run,150);
