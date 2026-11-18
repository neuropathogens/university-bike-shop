/* WBI7 — analytic tests for assumption confidence + risk-weighted sensitivity
   (E_confidence). It is a pure overlay: deep-clone + re-run computeDeal, never
   mutating the base. These check the ranking, the confidence band scaling
   (Low widens, High tightens), the adverse downside sign, and that the base
   model and computeDeal are untouched by the confidence metadata. */
const fs=require('fs'),vm=require('vm');
const html=fs.readFileSync(__dirname+'/index.html','utf8');
const a=html.indexOf('/* ===================== WBI7 ENGINE START');
const b=html.indexOf('WBI7 ENGINE END ===================== */');
const ctx={console};vm.createContext(ctx);
vm.runInContext(html.slice(a,b+'WBI7 ENGINE END ===================== */'.length),ctx);
const {computeDeal,E_confidence}=ctx;
let pass=0,fail=0;
const ok=(n,c,x)=>{c?pass++:fail++;console.log((c?'  PASS  ':'  FAIL  ')+n+(c?'':'  -> '+x));};
const near=(a,b,t)=>Math.abs(a-b)<=t;

function mk(over){const m=Object.assign({version:'wbi7-1',
  analysis:{holdMonths:84,discountRate:0.072,creditLoss:0.02,inflation:0},
  acquisition:{price:15000000,closingPct:0.02},capex:[],
  property:{suites:[{id:'S1',name:'U1',sf:100000}]},
  mlas:[{id:'M1',name:'flex',marketRent:1.25,rentGrowth:0.03,termMonths:60,renewalProb:0.7,downtimeMonths:6,
    freeNew:1,freeRenew:0,tiNew:3,tiRenew:1,lcNew:0.05,lcRenew:0.025,escalation:{type:'fixedPct',value:0.03},recMethod:'net',recParam:100}],
  rentRoll:[{id:'L1',tenant:'A',suiteId:'S1',sf:100000,startMonth:-12,termMonths:60,baseRent:1.2,escalation:{type:'fixedPct',value:0.03},freeMonths:0,recMethod:'net',recParam:100,mlaId:'M1',uponExpiry:'market'}],
  absorption:[],expenses:[{name:'CAM',basis:'psf',amount:1.2,growth:0.03,recoverable:true,varOcc:true},
    {name:'Tax',basis:'fixed',amount:170000,growth:0.02,recoverable:true,varOcc:false}],
  recoverySettings:{grossUpOn:false,grossUpPct:0.95,adminFee:0},otherIncome:{amount:0,growth:0},
  debt:{type:'ltv',ltv:0.6,amount:0,rate:0.062,ioMonths:12,amortMonths:360},
  exit:{exitCap:0.06,sellCostPct:0.02},equity:{lpShare:0.9,pref:0.08,promote:0.2}},over);return m;}

console.log('--- Assumption confidence + risk-weighted sensitivity ---');

// 1) returns a ranked set of drivers for a normal leveraged deal
{const R=E_confidence(mk({}));
 ok('C1 ok with a measurable base IRR',R.ok===true&&R.baseIrr!=null,String(R.ok));
 ok('C1 produces a row per key driver (9)',R.rows.length===9,R.rows.length);
 ok('C1 rows sorted by risk-weighted swing (desc)',R.rows.every((r,i)=>i===0||R.rows[i-1].riskRange>=r.riskRange),'');}

// 2) at medium confidence, risk-weighted == reference sensitivity (mult 1)
{const R=E_confidence(mk({}));   // no confidence set -> all medium
 ok('C2 medium confidence: risk-weighted equals sensitivity',R.rows.every(r=>near(r.riskRange,r.sens,1e-12)),'');}

// 3) Low confidence widens the band; High tightens it (same factor)
{const lo=E_confidence(mk({confidence:{exitCap:'low'}}));
 const hi=E_confidence(mk({confidence:{exitCap:'high'}}));
 const md=E_confidence(mk({}));
 const get=(R,k)=>R.rows.find(r=>r.key===k);
 ok('C3 Low confidence > Medium risk-weighted (exit cap)',get(lo,'exitCap').riskRange>get(md,'exitCap').riskRange,
    get(lo,'exitCap').riskRange+' vs '+get(md,'exitCap').riskRange);
 ok('C3 High confidence < Medium risk-weighted (exit cap)',get(hi,'exitCap').riskRange<get(md,'exitCap').riskRange,
    get(hi,'exitCap').riskRange+' vs '+get(md,'exitCap').riskRange);
 ok('C3 Low does NOT change a different factor (rentGrowth) vs medium',
    near(get(lo,'rentGrowth').riskRange,get(md,'rentGrowth').riskRange,1e-12),'');}

// 4) downside is adverse (<= 0) for an impactful driver
{const R=E_confidence(mk({confidence:{exitCap:'low'}}));
 const ec=R.rows.find(r=>r.key==='exitCap');
 ok('C4 downside IRR is non-positive (adverse move)',ec.downside!=null&&ec.downside<=1e-12,String(ec.downside));}

// 5) overlay safety: base model + computeDeal output untouched by E_confidence
{const m=mk({});const before=computeDeal(m).irrL;
 E_confidence(m);
 const after=computeDeal(m).irrL;
 ok('C5 base model not mutated (IRR identical after overlay)',near(before,after,1e-12),before+' vs '+after);}

// 6) confidence metadata is ignored by the core engine
{const a=computeDeal(mk({})).irrL;
 const b=computeDeal(mk({confidence:{exitCap:'low',price:'high',downtime:'low'}})).irrL;
 ok('C6 computeDeal ignores model.confidence (IRR identical)',near(a,b,1e-12),a+' vs '+b);}

console.log('\n'+pass+' passed, '+fail+' failed.');
process.exit(fail?1:0);
