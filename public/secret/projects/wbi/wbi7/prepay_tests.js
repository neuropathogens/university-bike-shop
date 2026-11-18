/* WBI7 — analytic tests for the step-down prepayment penalty. The no-penalty path
   is already proven byte-identical by the golden suite; these check the penalty
   itself: off == none, the penalty equals rate x payoff balance exactly, it steps
   down with loan year, it hits only levered returns (not unlevered), it expires,
   and it applies at a refinance too. */
const fs=require('fs'),vm=require('vm');
const html=fs.readFileSync(__dirname+'/index.html','utf8');
const a=html.indexOf('/* ===================== WBI7 ENGINE START');
const b=html.indexOf('WBI7 ENGINE END ===================== */');
const ctx={console};vm.createContext(ctx);
vm.runInContext(html.slice(a,b+'WBI7 ENGINE END ===================== */'.length),ctx);
const {computeDeal}=ctx;
let pass=0,fail=0;
const ok=(n,c,x)=>{c?pass++:fail++;console.log((c?'  PASS  ':'  FAIL  ')+n+(c?'':'  -> '+x));};
const near=(a,b,t)=>Math.abs(a-b)<=t;

// 3-year hold so a 5-4-3-2-1 schedule is a live 3% at exit; amortizing senior loan
function mk(over){const m=Object.assign({version:'wbi7-1',
  analysis:{holdMonths:36,discountRate:0.071,creditLoss:0,inflation:0},
  acquisition:{price:15000000,closingPct:0},capex:[],
  property:{suites:[{id:'S1',name:'U1',sf:100000}]},
  mlas:[{id:'M1',name:'flex',marketRent:1.2,rentGrowth:0.03,termMonths:120,renewalProb:1,downtimeMonths:0,
    freeNew:0,freeRenew:0,tiNew:0,tiRenew:0,lcNew:0,lcRenew:0,escalation:{type:'fixedPct',value:0.03},recMethod:'none',recParam:0}],
  rentRoll:[{id:'L1',tenant:'A',suiteId:'S1',sf:100000,startMonth:0,termMonths:120,baseRent:1.2,escalation:{type:'fixedPct',value:0.03},freeMonths:0,recMethod:'none',recParam:0,mlaId:'M1',uponExpiry:'renew'}],
  absorption:[],expenses:[{name:'CAM',basis:'psf',amount:1.0,growth:0.03,recoverable:false,varOcc:false}],
  recoverySettings:{grossUpOn:false,grossUpPct:0.95,adminFee:0},otherIncome:{amount:0,growth:0},
  debt:{type:'ltv',ltv:0.6,amount:0,rate:0.06,ioMonths:0,amortMonths:360},
  exit:{exitCap:0.06,sellCostPct:0.02},equity:{lpShare:1,pref:0,promote:0}},over);return m;}
const STEP={on:true,startPct:0.05,declinePct:0.01};   // 5-4-3-2-1-0...

console.log('--- Prepayment penalty (step-down) ---');

// 1) off == none: prepay.on=false reproduces the no-penalty deal exactly
{const base=mk({});const off=mk({});off.debt.prepay={on:false,startPct:0.05,declinePct:0.01};
 const d0=computeDeal(base),d1=computeDeal(off);
 ok('PP1 prepay off == none: proceeds identical',near(d0.proceeds,d1.proceeds,1e-9),d0.proceeds+' vs '+d1.proceeds);
 ok('PP1 prepay off == none: IRR identical',near(d0.irrL,d1.irrL,1e-12),d0.irrL+' vs '+d1.irrL);
 ok('PP1 prepay off: penalty field is 0',d1.prepaySale===0,String(d1.prepaySale));}

// 2) penalty equals rate x balance at sale, and reduces proceeds by exactly that
{const base=computeDeal(mk({}));const m=mk({});m.debt.prepay=STEP;const d=computeDeal(m);
 const yr=Math.ceil(36/12), rate=0.05-(yr-1)*0.01;   // year 3 -> 3%
 ok('PP2 penalty rate at exit is the year-3 step (3%)',near(d.prepaySale/d.balSale,rate,1e-9),(d.prepaySale/d.balSale)+' vs '+rate);
 ok('PP2 penalty == rate x balance at sale',near(d.prepaySale,rate*d.balSale,1e-6),d.prepaySale);
 ok('PP2 proceeds drop by exactly the penalty',near(base.proceeds-d.proceeds,d.prepaySale,1e-6),(base.proceeds-d.proceeds)+' vs '+d.prepaySale);}

// 3) step-down: the penalty rate declines the longer you hold
{const rateAt=hm=>{const m=mk({analysis:{holdMonths:hm,discountRate:0.071,creditLoss:0,inflation:0}});m.debt.prepay=STEP;
   const d=computeDeal(m);return d.balSale>0?d.prepaySale/d.balSale:0;};
 ok('PP3 year-1 exit -> 5% penalty',near(rateAt(12),0.05,1e-9),rateAt(12));
 ok('PP3 year-3 exit -> 3% penalty',near(rateAt(36),0.03,1e-9),rateAt(36));
 ok('PP3 penalty strictly declines with a longer hold',rateAt(12)>rateAt(36)&&rateAt(36)>rateAt(60),rateAt(12)+','+rateAt(36)+','+rateAt(60));}

// 4) penalty hits levered returns only; unlevered is untouched
{const base=computeDeal(mk({}));const m=mk({});m.debt.prepay=STEP;const d=computeDeal(m);
 ok('PP4 penalty lowers the levered IRR',d.irrL<base.irrL,d.irrL+' vs '+base.irrL);
 ok('PP4 penalty leaves the unlevered IRR unchanged',near(d.irrU,base.irrU,1e-12),d.irrU+' vs '+base.irrU);}

// 5) schedule expires: past 5-4-3-2-1 the penalty is 0
{const m=mk({analysis:{holdMonths:72,discountRate:0.071,creditLoss:0,inflation:0}});m.debt.prepay=STEP; // year 6
 const d=computeDeal(m);
 ok('PP5 year-6 exit -> penalty fully stepped down to 0',near(d.prepaySale,0,1e-9),d.prepaySale);}

// 6) penalty applies at a refinance too (on the old-loan balance at refi)
{const noP=mk({});noP.debt.refiOn=true;noP.debt.refiMonth=24;noP.debt.refiSizing='ltv';noP.debt.refiLtv=0.65;
   noP.debt.refiCap=0.06;noP.debt.refiRate=0.06;noP.debt.refiAmortMonths=360;noP.debt.refiCostPct=0;
 const wP=JSON.parse(JSON.stringify(noP));wP.debt.prepay=STEP;
 const d0=computeDeal(noP),d1=computeDeal(wP);
 const yr=Math.ceil(24/12),rate=0.05-(yr-1)*0.01;   // year 2 -> 4%
 ok('PP6 refi net drops by the penalty on the balance at refi',
    near(d0.refiNet-d1.refiNet,rate*d1.balAtRefi,1e-3),(d0.refiNet-d1.refiNet)+' vs '+(rate*d1.balAtRefi));
 ok('PP6 refi prepay reduces the levered IRR',d1.irrL<d0.irrL,d1.irrL+' vs '+d0.irrL);}

console.log('\n'+pass+' passed, '+fail+' failed.');
process.exit(fail?1:0);
