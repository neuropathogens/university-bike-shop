/* WBI7 — tests for portable deal files (serializeDeal / parseDealFile / dealFilename).
   Loads the page in jsdom and exercises the exported functions. Covers: the versioned
   wrapper shape, an EXACT round-trip (parse(serialize(m)).model deep-equals m) across
   several presets, acceptance of legacy/raw models, rejection of every malformed input
   (bad JSON, non-object, array, non-deal object, empty/wrapped-but-invalid model),
   filename sanitization and date stamping, and a full import-into-the-app round-trip
   via importDealText + collectModel. */
const fs=require('fs'),path=require('path');
const {JSDOM}=require('jsdom');
const HTML=process.env.WBI7_PATH||path.resolve(__dirname,'index.html');
const html=fs.readFileSync(HTML,'utf8');
let pass=0,fail=0;
const ok=(n,c,x)=>{c?pass++:fail++;console.log((c?'  PASS  ':'  FAIL  ')+n+(c?'':'  -> '+x));};

const dom=new JSDOM(html,{runScripts:"dangerously",pretendToBeVisual:true,url:"http://localhost/"});
setTimeout(()=>{
  const w=dom.window.__wbi7;
  if(!w){ok('window.__wbi7 is available',false,'no export');return finish();}
  ok('serializeDeal / parseDealFile / dealFilename exported',
    typeof w.serializeDeal==="function"&&typeof w.parseDealFile==="function"&&typeof w.dealFilename==="function",'');

  const m=JSON.parse(JSON.stringify(w.PRESETS["off-sf-fidi"]));

  // wrapper shape
  const txt=w.serializeDeal(m);let wrap=null;try{wrap=JSON.parse(txt);}catch(e){}
  ok('serializeDeal emits a versioned wrapper',!!wrap&&wrap.format==="wbi7-deal"&&wrap.appVersion==="wbi7-1"&&!!wrap.exported&&!!wrap.model,JSON.stringify(wrap&&Object.keys(wrap)));
  ok('wrapper carries the deal name',!!wrap&&typeof wrap.name==="string"&&wrap.name.length>0,'');

  // exact round-trip across several presets
  let allExact=true,which="";
  ["mf-sd-48","ind-oak-multi","off-sf-fidi","ret-grocery","spec-selfstore"].forEach(k=>{
    const src=JSON.parse(JSON.stringify(w.PRESETS[k]));
    const r=w.parseDealFile(w.serializeDeal(src));
    if(!r.ok||JSON.stringify(r.model)!==JSON.stringify(src)){allExact=false;which=k;}
  });
  ok('round-trip is exact for all sampled presets',allExact,which?('failed on '+which):'');

  // acceptance of legacy / raw models
  ok('a legacy raw model (version wbi7-1) is accepted',w.parseDealFile(JSON.stringify(m)).ok===true,'');
  const noVer=JSON.parse(JSON.stringify(m));delete noVer.version;
  ok('a raw model without version but with deal sections is accepted',w.parseDealFile(JSON.stringify(noVer)).ok===true,'');

  // rejection of malformed input
  ok('malformed JSON is rejected with a message',(()=>{const r=w.parseDealFile("{not json");return r.ok===false&&!!r.error;})(),'');
  ok('null is rejected',w.parseDealFile("null").ok===false,'');
  ok('an empty string is rejected',w.parseDealFile("").ok===false,'');
  ok('an array is rejected',w.parseDealFile("[1,2,3]").ok===false,'');
  ok('a non-deal object is rejected',w.parseDealFile('{"foo":1}').ok===false,'');
  ok('a wrapper with an invalid model is rejected',w.parseDealFile('{"format":"wbi7-deal","model":{"x":1}}').ok===false,'');

  // filename safety
  const dirty=JSON.parse(JSON.stringify(m));dirty.project='Acme / Tower: 100% "A" <test>';
  const fn=w.dealFilename(dirty);
  ok('filename is sanitized of path/illegal characters',/^WBI7_[A-Za-z0-9_]+_\d{4}-\d{2}-\d{2}\.json$/.test(fn),fn);
  ok('filename includes a date stamp and .json extension',/\d{4}-\d{2}-\d{2}\.json$/.test(fn),fn);
  ok('filename falls back to "deal" when unnamed',/^WBI7_deal_/.test(w.dealFilename({})),w.dealFilename({}));

  // full import-into-the-app round-trip
  if(typeof w.importDealText==="function"){
    const src=JSON.parse(JSON.stringify(w.PRESETS["ind-oak-multi"]));
    const before=w.computeDeal(src).irrL;
    const r=w.importDealText(w.serializeDeal(src));
    const loaded=w.collectModel();
    const after=w.computeDeal(loaded).irrL;
    ok('importDealText loads a deal that recomputes to the same IRR',r.ok===true&&Math.abs(before-after)<1e-9,String(before-after));
  } else { ok('importDealText exported',false,'missing'); }

  finish();
},450);
function finish(){console.log('\n'+pass+' passed, '+fail+' failed.');process.exit(fail?1:0);}
