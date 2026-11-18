/* WBI7 — analytic tests for the pre-mortem / kill-zone (E_killzone). Pure overlay:
   for each driver bisect the adverse move that hits the failure threshold (the kill
   point), and stress-test driver pairs to find combinations that lose money. These
   check: kill-point correctness (IRR ~ threshold at the reported move, bracketed),
   robustness detection, the core "combinations matter" property (a pair fails when
   neither single move does), already-failing detection, and base-model immutability. */
const fs=require('fs'),vm=require('vm');
const html=fs.readFileSync(__dirname+'/index.html','utf8');
const a=html.indexOf('/* ===================== WBI7 ENGINE START');
const b=html.indexOf('WBI7 ENGINE END ===================== */');
const ctx={console};vm.createContext(ctx);
vm.runInContext(html.slice(a,b+'WBI7 ENGINE END ===================== */'.length),ctx);
const {computeDeal,E_killzone}=ctx;
let pass=0,fail=0;
const ok=(n,c,x)=>{c?pass++:fail++;console.log((c?'  PASS  ':'  FAIL  ')+n+(c?'':'  -> '+x));};
const near=(a,b,t)=>Math.abs(a-b)<=t;

// healthy deal: strong going-in spread + cap compression => comfortably positive IRR
function mkHealthy(over){const m=Object.assign({version:'wbi7-1',
  analysis:{holdMonths:84,discountRate:0.072,creditLoss:0.01,inflation:0},
  acquisition:{price:15000000,closingPct:0},capex:[],
  property:{suites:[{id:'S1',name:'U1',sf:100000}]},
  mlas:[{id:'M1',name:'flex',marketRent:1.25,rentGrowth:0.03,termMonths:60,renewalProb:0.7,downtimeMonths:6,
    freeNew:1,freeRenew:0,tiNew:3,tiRenew:1,lcNew:0.05,lcRenew:0.025,escalation:{type:'fixedPct',value:0.03},recMethod:'net',recParam:100}],
  rentRoll:[{id:'L1',tenant:'A',suiteId:'S1',sf:100000,startMonth:-12,termMonths:60,baseRent:1.2,escalation:{type:'fixedPct',value:0.03},freeMonths:0,recMethod:'net',recParam:100,mlaId:'M1',uponExpiry:'market'}],
  absorption:[],expenses:[{name:'CAM',basis:'psf',amount:1.2,growth:0.03,recoverable:true,varOcc:true},
    {name:'Tax',basis:'fixed',amount:170000,growth:0.02,recoverable:true,varOcc:false}],
  recoverySettings:{grossUpOn:false,grossUpPct:0.95,adminFee:0},otherIncome:{amount:0,growth:0},
  debt:{type:'ltv',ltv:0.6,amount:0,rate:0.062,ioMonths:0,amortMonths:360},
  exit:{exitCap:0.055,sellCostPct:0.02},equity:{lpShare:1,pref:0,promote:0}},over);return m;}

// thin deal: high price (low going-in yield), no cap compression, flat growth, levered
// => modest IRR, so single notches may survive but pairs can sink it
function mkThin(){return mkHealthy({acquisition:{price:21000000,closingPct:0},
  mlas:[{id:'M1',name:'flex',marketRent:1.2,rentGrowth:0.005,termMonths:60,renewalProb:0.7,downtimeMonths:6,
    freeNew:1,freeRenew:0,tiNew:3,tiRenew:1,lcNew:0.05,lcRenew:0.025,escalation:{type:'fixedPct',value:0.005},recMethod:'net',recParam:100}],
  exit:{exitCap:0.064,sellCostPct:0.02},debt:{type:'ltv',ltv:0.6,amount:0,rate:0.065,ioMonths:0,amortMonths:360}});}

console.log('--- Pre-mortem / kill-zone ---');

// 1) returns a result for a healthy deal that clears the 0% bar
{const R=E_killzone(mkHealthy(),{targetIrr:0});
 ok('K1 ok and not already-failing',R.ok===true&&!R.alreadyFails,String(R.ok));
 ok('K1 base IRR is above the threshold',R.baseIrr>0,R.baseIrr);
 ok('K1 has a breakeven entry per driver (9)',R.breakevens.length===9,R.breakevens.length);}

// 2) single-factor kill point: at the reported adverse move, IRR ~ threshold; and it
//    brackets. Use a bar at half the base IRR so exit cap (high impact) has a finite point.
{const base=computeDeal(mkHealthy()).irrL,T=base-0.05;
 const R=E_killzone(mkHealthy(),{targetIrr:T});
 const ec=R.breakevens.find(x=>x.key==='exitCap');
 ok('K2 exit cap has a finite kill point at a near-base bar',!ec.robust&&ec.mag>0,JSON.stringify(ec));
 const at=mag=>{const m=mkHealthy();m.exit.exitCap=m.exit.exitCap+mag;const v=computeDeal(m).irrL;return v==null?-1:v;};
 ok('K2 IRR ~ threshold at the kill point',near(at(ec.mag),T,0.01),at(ec.mag)+' vs '+T);
 ok('K2 brackets: just inside clears, just past fails',at(ec.mag*0.7)>T&&at(ec.mag*1.4)<T,at(ec.mag*0.7)+' / '+at(ec.mag*1.4));}

// 3) robustness: against a high bar a tiny move can't be required... and against a deal
//    that already fails, alreadyFails is set
{const R=E_killzone(mkHealthy(),{targetIrr:0.50}); // 50% bar — the deal is below it at base
 ok('K3 already-failing flagged when base IRR < threshold',R.alreadyFails===true,JSON.stringify(R).slice(0,40));}

// 4) robustness label: with a generous threshold (-100%), nothing can sink it -> robust
{const R=E_killzone(mkHealthy(),{targetIrr:-0.99});
 ok('K4 drivers are robust against an extreme-low bar',R.breakevens.every(x=>x.robust)===true,'');}

// 5/6) Combinations matter. Pick a bar just below the WORST single-notch move, so no
//      single driver fails there — then any failing pair proves combinations matter.
{const R0=E_killzone(mkHealthy(),{targetIrr:-1});  // unfiltered: read single-notch IRRs
 const singles=Object.keys(R0.single).map(k=>R0.single[k].irr);
 const minSingle=Math.min.apply(null,singles),T=minSingle-0.005;
 const R=E_killzone(mkHealthy(),{targetIrr:T});
 ok('K5 kill pairs exist at a bar just below the worst single notch',R.killPairs.length>0,R.killPairs.length);
 ok('K5 every kill pair is below the threshold',R.killPairs.every(p=>p.irr<T),'');
 ok('K5 kill pairs sorted worst-first',R.killPairs.every((p,i)=>i===0||R.killPairs[i-1].irr<=p.irr),'');
 ok('K6 no single driver fails at this bar (so a pair failing => combinations matter)',
    Object.keys(R.single).every(k=>R.single[k].irr>=T),'');
 const p=R.killPairs[0];
 ok('K6 the failing pair is worse than either of its single moves',
    p.irr<R.single[p.aKey].irr&&p.irr<R.single[p.bKey].irr,p.irr+' vs '+R.single[p.aKey].irr+'/'+R.single[p.bKey].irr);}

// 7) overlay safety: base model + computeDeal output untouched
{const m=mkHealthy();const before=computeDeal(m).irrL;
 E_killzone(m,{targetIrr:0});
 ok('K7 base model not mutated (IRR identical after kill-zone)',near(before,computeDeal(m).irrL,1e-12),'');
 ok('K7 model.exit.exitCap unchanged by the search',m.exit.exitCap===0.055,m.exit.exitCap);}

console.log('\n'+pass+' passed, '+fail+' failed.');
process.exit(fail?1:0);
