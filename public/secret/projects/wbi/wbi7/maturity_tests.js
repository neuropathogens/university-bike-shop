/* WBI7 — tests for loan maturity / balloon as a forced event. A loan has a term
   (debt.termMonths) distinct from its amortization. If the term is shorter than the
   hold, the balloon comes due before sale and must be refinanced — so rather than
   silently carrying the original loan to sale at the original rate, the engine forces
   a refinance at maturity using the refinance-section terms (re-sized to then-current
   value at the new rate, with a cash-in if value softened). termMonths of 0 (or >= the
   hold) means maturity at or beyond the hold — the original behavior — so the shipped
   presets, which carry no termMonths, are byte-identical. */
const fs=require('fs'),vm=require('vm');
const html=fs.readFileSync(__dirname+'/index.html','utf8');
const a=html.indexOf('/* ===================== WBI7 ENGINE START');
const b=html.indexOf('WBI7 ENGINE END ===================== */');
const ctx={console};vm.createContext(ctx);
vm.runInContext(html.slice(a,b+'WBI7 ENGINE END ===================== */'.length),ctx);
const {computeDeal}=ctx;
let pass=0,fail=0;
const ok=(n,c,x)=>{c?pass++:fail++;console.log((c?'  PASS  ':'  FAIL  ')+n+(c?'':'  -> '+x));};
const near=(a,b,e)=>Math.abs(a-b)<=(e==null?1:e);

function mkDeal(over){const debt=Object.assign({type:'ltv',ltv:0.6,amount:0,rate:0.06,ioMonths:0,amortMonths:360,termMonths:0,
    refiOn:false,refiMonth:0,refiSizing:'ltv',refiCap:0.07,refiLtv:0.6,refiRate:0.08,refiCostPct:0.01,refiIoMonths:0,refiAmortMonths:360,
    mezz:{amount:0,rate:0}},(over&&over.__debt)||{});
  const m=Object.assign({version:'wbi7-1',
  analysis:{holdMonths:120,discountRate:0.08,creditLoss:0,inflation:0.025},
  acquisition:{price:20000000,closingPct:0.02,reassess:false,taxRate:0.0115},
  capex:[],property:{suites:[{id:'S1',name:'U1',sf:100000}]},
  mlas:[{id:'M1',name:'flex',marketRent:1.6,rentGrowth:0.03,termMonths:180,renewalProb:0.7,downtimeMonths:6,
    freeNew:0,freeRenew:0,tiNew:0,tiRenew:0,lcNew:0,lcRenew:0,escalation:{type:'fixedPct',value:0.03},recMethod:'net',recParam:100}],
  rentRoll:[{id:'L1',tenant:'A',suiteId:'S1',sf:100000,startMonth:-6,termMonths:180,baseRent:1.6,escalation:{type:'fixedPct',value:0.03},freeMonths:0,recMethod:'net',recParam:100,mlaId:'M1',uponExpiry:'market'}],
  absorption:[],expenses:[{name:'Opex',basis:'psf',amount:3,growth:0.03,recoverable:false,varOcc:false}],
  recoverySettings:{grossUpOn:false,grossUpPct:0.95,adminFee:0},otherIncome:{amount:0,growth:0},
  exit:{exitCap:0.07,sellCostPct:0.02},equity:{lpShare:1,pref:0,promote:0}},over);
  m.debt=debt;delete m.__debt;return m;}

console.log('--- loan maturity / balloon forced refinance ---');

// 1. no term -> no maturity event, loan carried to sale
{const d=computeDeal(mkDeal());
 ok('termMonths 0 -> no maturity event (loan carried to sale)',d.loanMatures===false&&d.refiForced===false,JSON.stringify({m:d.loanMatures,f:d.refiForced}));}

// 2. term >= hold -> no maturity event
{const d=computeDeal(mkDeal({__debt:{termMonths:120}}));
 ok('termMonths >= hold -> no maturity event',d.loanMatures===false,'');}
{const d=computeDeal(mkDeal({__debt:{termMonths:200}}));
 ok('termMonths beyond hold -> no maturity event',d.loanMatures===false,'');}

// 3. term < hold and no user refi -> forced refinance at maturity
{const d=computeDeal(mkDeal({__debt:{termMonths:60}}));
 ok('term < hold forces a refinance at the maturity month',d.loanMatures===true&&d.refiForced===true&&d.refiMonth===60&&d.newLoan>0,
    JSON.stringify({m:d.loanMatures,f:d.refiForced,rf:d.refiMonth,nl:Math.round(d.newLoan)}));}

// 4. byte-identical: term 0 vs term=hold vs no-term all equal (no refi in any)
{const a0=computeDeal(mkDeal({__debt:{termMonths:0}}));
 const aH=computeDeal(mkDeal({__debt:{termMonths:120}}));
 const m=mkDeal();delete m.debt.termMonths;const aU=computeDeal(m);
 ok('term 0, term=hold and absent term give identical IRR/value (no forced refi)',
    near(a0.irrL,aH.irrL,1e-9)&&near(a0.irrL,aU.irrL,1e-9)&&near(a0.value,aU.value,1e-6),'');}

// 5. debt service changes after maturity, identical before
{const d0=computeDeal(mkDeal()); // carried at 6%
 const dM=computeDeal(mkDeal({__debt:{termMonths:60,refiRate:0.10}})); // refi at 10%
 const ds0=d0.annual.map(a=>Math.round(a.ds)),dsM=dM.annual.map(a=>Math.round(a.ds));
 ok('pre-maturity debt service is unchanged',JSON.stringify(ds0.slice(0,5))===JSON.stringify(dsM.slice(0,5)),'');
 ok('post-maturity debt service rises with a higher take-out rate',dsM[6]>ds0[6],dsM[6]+' vs '+ds0[6]);}

// 6. higher take-out rate lowers levered IRR vs silently carrying
{const d0=computeDeal(mkDeal());
 const dM=computeDeal(mkDeal({__debt:{termMonths:60,refiRate:0.11}}));
 ok('a higher forced take-out rate lowers levered IRR vs carrying at the original rate',dM.irrL<d0.irrL,(d0.irrL*100).toFixed(2)+'% -> '+(dM.irrL*100).toFixed(2)+'%');}

// 7. forced refi rate defaults to the current loan rate when refi rate is unset
{const dDef=computeDeal(mkDeal({__debt:{termMonths:60,refiRate:0,rate:0.06}}));
 const dSame=computeDeal(mkDeal({__debt:{termMonths:60,refiRate:0.06,rate:0.06}}));
 ok('forced refi with no refi rate falls back to the current loan rate',near(dDef.annual[7].ds,dSame.annual[7].ds,1),'');}

// 8. forced refi with no refi LTV re-levers at the original LTV
{const d=computeDeal(mkDeal({__debt:{termMonths:60,refiLtv:0,ltv:0.6}}));
 // newLoan should be ~ refiValue * 0.60
 ok('forced refi with no refi LTV re-levers at the original LTV',near(d.newLoan,d.refiValue*0.6,2),Math.round(d.newLoan)+' vs '+Math.round(d.refiValue*0.6));}

// 9. user refinance at/before maturity takes precedence (not forced)
{const d=computeDeal(mkDeal({__debt:{termMonths:60,refiOn:true,refiMonth:36}}));
 ok('a user refinance at or before maturity takes precedence (not forced)',d.refiMonth===36&&d.refiForced===false,JSON.stringify({rf:d.refiMonth,f:d.refiForced}));}
// user refi AFTER maturity -> still forced at maturity
{const d=computeDeal(mkDeal({__debt:{termMonths:60,refiOn:true,refiMonth:96}}));
 ok('a user refinance scheduled after maturity is overridden by the forced take-out at maturity',d.refiMonth===60&&d.refiForced===true,JSON.stringify({rf:d.refiMonth,f:d.refiForced}));}

// 10. soft value at maturity forces a cash-in (refiNet < 0)
{const d=computeDeal(mkDeal({__debt:{termMonths:60,refiCap:0.13,refiLtv:0.6},exit:{exitCap:0.13,sellCostPct:0.02}}));
 ok('a soft value at maturity forces a cash-in (refiNet < 0)',d.refiNet<0,'refiNet '+Math.round(d.refiNet));}

// 11. immutability
{const m=mkDeal({__debt:{termMonths:60}});const before=JSON.stringify(m);computeDeal(m);computeDeal(m);
 ok('computing the deal never mutates the model',JSON.stringify(m)===before,'model changed');}

console.log('\n'+pass+' passed, '+fail+' failed.');
process.exit(fail?1:0);
