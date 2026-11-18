/* WBI7 — analytic tests for the mezzanine overlay (E_mezz). Checks the no-mezz
   identity, positive- and negative-leverage direction on the equity return,
   blended cost, all-in coverage, amortization vs IO, immutability, and degenerate
   handling. Built on computeDeal's senior-levered stream (no engine surgery). */
const fs=require('fs'),vm=require('vm');
const html=fs.readFileSync(__dirname+'/index.html','utf8');
const a=html.indexOf('/* ===================== WBI7 ENGINE START');
const b=html.indexOf('WBI7 ENGINE END ===================== */');
const ctx={console};vm.createContext(ctx);
vm.runInContext(html.slice(a,b+'WBI7 ENGINE END ===================== */'.length),ctx);
const {computeDeal,E_mezz}=ctx;
let pass=0,fail=0;
const ok=(n,c,x)=>{c?pass++:fail++;console.log((c?'  PASS  ':'  FAIL  ')+n+(c?'':'  -> '+x));};
const near=(a,b,t)=>Math.abs(a-b)<=t;

// healthy deal: ~8% going-in yield, 60% senior at 6.4% -> room for positive-leverage mezz
function mk(over){const m=Object.assign({version:'wbi7-1',
  analysis:{holdMonths:84,discountRate:0.071,creditLoss:0.01,inflation:0},
  acquisition:{price:15000000,closingPct:0},capex:[],
  property:{suites:[{id:'S1',name:'U1',sf:100000}]},
  mlas:[{id:'M1',name:'flex',marketRent:1.1,rentGrowth:0.03,termMonths:120,renewalProb:1,downtimeMonths:0,
    freeNew:0,freeRenew:0,tiNew:0,tiRenew:0,lcNew:0,lcRenew:0,escalation:{type:'fixedPct',value:0.03},recMethod:'net',recParam:100}],
  rentRoll:[{id:'L1',tenant:'A',suiteId:'S1',sf:100000,startMonth:0,termMonths:120,baseRent:1.1,escalation:{type:'fixedPct',value:0.03},freeMonths:0,recMethod:'net',recParam:100,mlaId:'M1',uponExpiry:'renew'}],
  absorption:[],expenses:[{name:'CAM',basis:'psf',amount:1.2,growth:0.03,recoverable:true,varOcc:false}],
  recoverySettings:{grossUpOn:false,grossUpPct:0.95,adminFee:0},otherIncome:{amount:0,growth:0},
  debt:{type:'ltv',ltv:0.6,amount:0,rate:0.064,ioMonths:120,amortMonths:360},
  exit:{exitCap:0.06,sellCostPct:0.02},equity:{lpShare:1,pref:0,promote:0}},over);return m;}

console.log('--- Mezzanine overlay ---');

// 1) no-mezz identity: amount 0 reproduces the senior-only deal exactly
{const m=mk({});m.debt.mezz={amount:0,rate:0.12,ioMonths:120,amortMonths:360};
 const z=E_mezz(m);const d=computeDeal(m);
 ok('M1 mezz=0 -> equity IRR == senior IRR',near(z.irrL,d.irrL,1e-12),z.irrL+' vs '+d.irrL);
 ok('M1 mezz=0 -> EM == senior EM',near(z.emL,d.emL,1e-12),z.emL+' vs '+d.emL);
 ok('M1 mezz=0 -> equity unchanged',near(z.equityWithMezz,d.equity0,1e-6),z.equityWithMezz+' vs '+d.equity0);
 ok('M1 mezz=0 -> on=false',z.on===false,'');}

// 2) positive leverage: deal yield > mezz rate -> mezz lifts equity IRR, cuts equity
{const m=mk({});m.debt.mezz={amount:2000000,rate:0.10,ioMonths:120,amortMonths:360};
 const z=E_mezz(m);
 ok('M2 mezz reduces the equity check',z.equityWithMezz<z.equitySenior-1,z.equityWithMezz+' vs '+z.equitySenior);
 ok('M2 positive-leverage mezz lifts the equity IRR',z.irrL>z.seniorIrr,z.irrL+' vs '+z.seniorIrr);
 ok('M2 with-mezz EM exceeds senior EM (less equity, geared)',z.emL>z.seniorEm,z.emL+' vs '+z.seniorEm);}

// 3) negative leverage: very expensive mezz drags the equity IRR below senior
{const m=mk({});m.debt.mezz={amount:2000000,rate:0.30,ioMonths:120,amortMonths:360};
 const z=E_mezz(m);
 ok('M3 expensive mezz lowers the equity IRR',z.irrL<z.seniorIrr,z.irrL+' vs '+z.seniorIrr);}

// 4) blended rate is the debt-weighted average of senior and mezz
{const m=mk({});m.debt.mezz={amount:3000000,rate:0.12,ioMonths:120,amortMonths:360};
 const z=E_mezz(m);
 const exp=(z.seniorLoan*0.064+3000000*0.12)/(z.seniorLoan+3000000);
 ok('M4 total debt = senior + mezz',near(z.totalDebt,z.seniorLoan+3000000,1e-6),z.totalDebt);
 ok('M4 blended rate is the debt-weighted average',near(z.blendedRate,exp,1e-9),z.blendedRate+' vs '+exp);
 ok('M4 blended rate sits between senior and mezz rates',z.blendedRate>0.064-1e-9&&z.blendedRate<0.12+1e-9,z.blendedRate);}

// 5) all-in coverage tightens vs senior-only
{const m=mk({});m.debt.mezz={amount:2000000,rate:0.12,ioMonths:120,amortMonths:360};
 const z=E_mezz(m);
 const seniorDscr1=z.seniorDS1>0?z.noi1/z.seniorDS1:Infinity;
 ok('M5 mezz adds year-1 debt service',z.mezzDS1>0,z.mezzDS1);
 ok('M5 all-in DSCR is below senior-only DSCR',z.allInDscr1<seniorDscr1,z.allInDscr1+' vs '+seniorDscr1);
 ok('M5 all-in debt yield = NOI1 / total debt',near(z.allInDebtYield,z.noi1/z.totalDebt,1e-9),z.allInDebtYield);}

// 6) IO mezz keeps full balance to sale; amortizing mezz pays down
{const m=mk({});m.debt.mezz={amount:2000000,rate:0.12,ioMonths:9999,amortMonths:360};
 const io=E_mezz(m);
 ok('M6 full-term IO mezz: balloon at sale == original amount',near(io.mezzBalSale,2000000,1e-6),io.mezzBalSale);
 const m2=mk({});m2.debt.mezz={amount:2000000,rate:0.12,ioMonths:0,amortMonths:240};
 const amz=E_mezz(m2);
 ok('M6 amortizing mezz: balance at sale below original',amz.mezzBalSale<2000000,amz.mezzBalSale);}

// 7) immutability
{const m=mk({});m.debt.mezz={amount:2000000,rate:0.12,ioMonths:24,amortMonths:360};
 const snap=JSON.stringify(m);E_mezz(m);
 ok('M7 input model not mutated',JSON.stringify(m)===snap,'mutated');}

// 8) degenerate model -> graceful (senior IRR null, mezz overlay defined or null)
{const blank={version:"wbi7-1",analysis:{holdMonths:60,discountRate:0.075,creditLoss:0},
   acquisition:{price:0,closingPct:0},capex:[],property:{suites:[]},mlas:[],rentRoll:[],
   absorption:[],expenses:[],recoverySettings:{grossUpOn:false,grossUpPct:0.95,adminFee:0},
   otherIncome:{amount:0,growth:0},debt:{type:'ltv',ltv:0,amount:0,rate:0,ioMonths:0,amortMonths:360,mezz:{amount:0,rate:0.12,ioMonths:0,amortMonths:360}},
   exit:{exitCap:0.06,sellCostPct:0},equity:{lpShare:1,pref:0,promote:0}};
 let z;try{z=E_mezz(blank);}catch(e){z=null;}
 ok('M8 degenerate model does not throw',!!z,'threw');
 ok('M8 degenerate model: total debt 0, IRR null',z&&z.totalDebt===0&&z.irrL===null,JSON.stringify(z&&{td:z.totalDebt,irr:z.irrL}));}

console.log('\n'+pass+' passed, '+fail+' failed.');
process.exit(fail?1:0);
