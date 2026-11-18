/* WBI7 — analytic tests for the capital-structure optimizer (E_optimize). It is a
   pure overlay: grid-search senior+mezz leverage, re-run the engine per candidate,
   keep the feasible structure with the best levered IRR. These check feasibility of
   the optimum, that positive leverage helps and negative leverage doesn't, that a
   tighter DSCR floor reduces optimal leverage, and that the base model is untouched. */
const fs=require('fs'),vm=require('vm');
const html=fs.readFileSync(__dirname+'/index.html','utf8');
const a=html.indexOf('/* ===================== WBI7 ENGINE START');
const b=html.indexOf('WBI7 ENGINE END ===================== */');
const ctx={console};vm.createContext(ctx);
vm.runInContext(html.slice(a,b+'WBI7 ENGINE END ===================== */'.length),ctx);
const {computeDeal,E_optimize}=ctx;
let pass=0,fail=0;
const ok=(n,c,x)=>{c?pass++:fail++;console.log((c?'  PASS  ':'  FAIL  ')+n+(c?'':'  -> '+x));};
const near=(a,b,t)=>Math.abs(a-b)<=t;

// A deal whose going-in yield comfortably beats the debt rate => positive leverage.
// price 15.0M, NOI ~1.34M (≈8.9% going-in) vs 6% debt.
function mk(over){const m=Object.assign({version:'wbi7-1',
  analysis:{holdMonths:84,discountRate:0.072,creditLoss:0,inflation:0},
  acquisition:{price:15000000,closingPct:0},capex:[],
  property:{suites:[{id:'S1',name:'U1',sf:100000}]},
  mlas:[{id:'M1',name:'flex',marketRent:1.2,rentGrowth:0.03,termMonths:120,renewalProb:1,downtimeMonths:0,
    freeNew:0,freeRenew:0,tiNew:0,tiRenew:0,lcNew:0,lcRenew:0,escalation:{type:'fixedPct',value:0.03},recMethod:'none',recParam:0}],
  rentRoll:[{id:'L1',tenant:'A',suiteId:'S1',sf:100000,startMonth:0,termMonths:120,baseRent:1.2,escalation:{type:'fixedPct',value:0.03},freeMonths:0,recMethod:'none',recParam:0,mlaId:'M1',uponExpiry:'renew'}],
  absorption:[],expenses:[{name:'CAM',basis:'psf',amount:1.0,growth:0.03,recoverable:false,varOcc:false}],
  recoverySettings:{grossUpOn:false,grossUpPct:0.95,adminFee:0},otherIncome:{amount:0,growth:0},
  debt:{type:'ltv',ltv:0.5,amount:0,rate:0.06,ioMonths:0,amortMonths:360},
  exit:{exitCap:0.06,sellCostPct:0.02},equity:{lpShare:1,pref:0,promote:0}},over);return m;}

console.log('--- Capital-structure optimizer ---');

// 1) returns a feasible optimum + an all-equity baseline
{const R=E_optimize(mk({}),{maxSeniorLtv:0.7,maxTotalLtv:0.8,minDscr:1.2,minDebtYield:0.07,mezzRate:0.11});
 ok('O1 ok with a best structure',R.ok===true&&R.best!=null,String(R.ok));
 ok('O1 all-equity baseline present (zero debt)',R.allEquity!=null&&R.allEquity.totalDebt<1,'');
 ok('O1 optimum is marked feasible',R.best.feasible===true,'');}

// 2) the optimum respects every constraint
{const cons={maxSeniorLtv:0.7,maxTotalLtv:0.8,minDscr:1.25,minDebtYield:0.075,mezzRate:0.11};
 const R=E_optimize(mk({}),cons);const bt=R.best;
 ok('O2 optimum total LTV <= max',bt.totalLtv<=cons.maxTotalLtv+1e-6,bt.totalLtv);
 ok('O2 optimum all-in DSCR >= floor',bt.dscr===Infinity||bt.dscr>=cons.minDscr-1e-6,bt.dscr);
 ok('O2 optimum debt yield >= floor',bt.dy===Infinity||bt.dy>=cons.minDebtYield-1e-9,bt.dy);}

// 3) positive leverage: with a healthy spread, the optimum out-returns all-equity
{const R=E_optimize(mk({}),{maxSeniorLtv:0.7,maxTotalLtv:0.7,minDscr:1.1,minDebtYield:0.06,mezzRate:0.10});
 ok('O3 leveraged optimum beats all-equity IRR',R.best.irr>R.allEquity.irr+1e-6,R.best.irr+' vs '+R.allEquity.irr);
 ok('O3 leveraged optimum actually uses debt',R.best.totalDebt>1,R.best.totalLtv);}

// 4) a tighter DSCR floor reduces the optimal leverage (constraint bites)
{const loose=E_optimize(mk({}),{maxSeniorLtv:0.8,maxTotalLtv:0.8,minDscr:1.10,minDebtYield:0,mezzRate:0.10});
 const tight=E_optimize(mk({}),{maxSeniorLtv:0.8,maxTotalLtv:0.8,minDscr:1.60,minDebtYield:0,mezzRate:0.10});
 ok('O4 tighter DSCR => less optimal leverage',tight.best.totalLtv<loose.best.totalLtv,
    tight.best.totalLtv+' vs '+loose.best.totalLtv);
 ok('O4 tight-DSCR optimum still meets its floor',tight.best.dscr===Infinity||tight.best.dscr>=1.60-1e-6,tight.best.dscr);}

// 5) negative leverage: if debt costs far more than the deal yields, optimum ~ all-equity
{const R=E_optimize(mk({debt:{type:'ltv',ltv:0.5,amount:0,rate:0.20,ioMonths:0,amortMonths:360}}),
    {maxSeniorLtv:0.7,maxTotalLtv:0.8,minDscr:0,minDebtYield:0,mezzRate:0.22});
 ok('O5 dilutive debt => optimum carries little/no leverage',R.best.totalLtv<0.10,R.best.totalLtv);
 ok('O5 optimum IRR ~ all-equity when leverage is dilutive',near(R.best.irr,R.allEquity.irr,0.01),R.best.irr+' vs '+R.allEquity.irr);}

// 6) overlay safety: the base model + computeDeal output are untouched
{const m=mk({});const before=computeDeal(m).irrL;
 E_optimize(m,{maxSeniorLtv:0.7,maxTotalLtv:0.85,minDscr:1.25,minDebtYield:0.07,mezzRate:0.11});
 const after=computeDeal(m).irrL;
 ok('O6 base model not mutated (IRR identical after optimize)',near(before,after,1e-12),before+' vs '+after);
 ok('O6 model.debt.ltv unchanged by the search',m.debt.ltv===0.5,m.debt.ltv);}

console.log('\n'+pass+' passed, '+fail+' failed.');
process.exit(fail?1:0);
