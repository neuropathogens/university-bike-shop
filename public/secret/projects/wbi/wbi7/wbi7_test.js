#!/usr/bin/env node
/* =====================================================================
   WBI7 — Engine Analytic Tests + Golden-Master Regression Harness (v2)
   ---------------------------------------------------------------------
   Part A (always runs, no browser needed): extracts the pure engine from
   index.html and checks it against hand-computed analytic cases — lease
   streams, escalation timing, blended rollover, downtime/free rent,
   TI/LC events, IO->amortizing debt, waterfall conservation, and the
   Phase-2 recovery subsystem (net pro-rata, base-year stop with
   lookback, fixed CAM, occupancy gross-up), plus the Phase-7 Monte
   Carlo overlay (seeded determinism, zero-sigma collapse, correlation),
   the refinance module, the multi-tier IRR-hurdle waterfall, and the
   inflation factor (real returns, CPI escalation), and the after-tax
   module (depreciation shield, recapture, capital gains, after-tax IRR).
   Part B (runs when CHROME_PATH is set): loads the full app in headless
   Chrome, checks the gate, and locks both presets' displayed outputs to
   golden values, plus structural return invariants.

   USAGE:
     node wbi7.test.js                              # engine tests only
     CHROME_PATH=/path/to/chrome node wbi7.test.js  # engine + browser
     (optional) WBI7_PATH=./index.html
   Browser part requires:  npm i puppeteer-core
   Exit code 0 = all pass, 1 = any failure (CI-friendly).
   ===================================================================== */
const fs=require('fs'),vm=require('vm'),path=require('path');
const HTML=process.env.WBI7_PATH||path.resolve(__dirname,'index.html');
let pass=0,fail=0;
const ok=(n,c,x)=>{c?pass++:fail++;console.log((c?'  PASS  ':'  FAIL  ')+n+(c?'':'  -> '+x));};
const near=(a,b,tol)=>Math.abs(a-b)<=tol;

/* ---------------- Part A: pure-engine analytic tests ---------------- */
const html=fs.readFileSync(HTML,'utf8');
const A0=html.indexOf('/* ===================== WBI7 ENGINE START');
const A1=html.indexOf('WBI7 ENGINE END ===================== */');
const ctx={console};vm.createContext(ctx);
vm.runInContext(html.slice(A0,A1+'WBI7 ENGINE END ===================== */'.length),ctx);
const {computeDeal}=ctx;
function base(over){return Object.assign({version:'wbi7-1',
  analysis:{holdMonths:12,discountRate:0.075,creditLoss:0},
  acquisition:{price:3000000,closingPct:0},capex:[],
  property:{suites:[{id:'S1',name:'A',sf:10000}]},
  mlas:[],rentRoll:[],absorption:[],expenses:[],otherIncome:{amount:0,growth:0},
  debt:{type:'amount',amount:0,rate:0,ioMonths:0,amortMonths:360},
  exit:{exitCap:0.07,sellCostPct:0},equity:{lpShare:1,pref:0,promote:0}},over);}

console.log('--- Part A: engine analytic tests ---');
{const d=computeDeal(base({rentRoll:[{id:'L1',suiteId:'S1',sf:10000,startMonth:0,termMonths:60,baseRent:2,
   escalation:{type:'none'},freeMonths:0,recoveryPct:0,mlaId:'MX',uponExpiry:'renew'}],
   expenses:[{name:'op',basis:'fixed',amount:10000,growth:0,recoverable:false}]}));
 ok('T1 annual rent = 240,000',near(d.annual[0].rent,240000,0.01),d.annual[0].rent);
 ok('T1 annual NOI = 230,000',near(d.annual[0].noi,230000,0.01),d.annual[0].noi);
 ok('T1 forward NOI = 230,000',near(d.fwdNOI,230000,0.01),d.fwdNOI);
 ok('T1 exit value = fwd NOI / 7%',near(d.value,230000/0.07,0.5),d.value);
 ok('T1 unlevered EM = 1.171905',near(d.emU,1.171905,1e-4),d.emU);
 ok('T1 unlevered IRR in (15%,21%)',d.irrU>0.15&&d.irrU<0.21,d.irrU);}
{const d=computeDeal(base({analysis:{holdMonths:24,discountRate:0.075,creditLoss:0},
   property:{suites:[{id:'S1',name:'A',sf:1000}]},
   mlas:[{id:'M1',name:'X',marketRent:2,rentGrowth:0,termMonths:24,renewalProb:0.6,downtimeMonths:3,
     freeNew:2,freeRenew:0,tiNew:10,tiRenew:0,lcNew:0.05,lcRenew:0,escalation:{type:'none'},recoveryPct:0}],
   rentRoll:[{id:'L1',suiteId:'S1',sf:1000,startMonth:0,termMonths:6,baseRent:1,
     escalation:{type:'none'},freeMonths:0,recoveryPct:0,mlaId:'M1',uponExpiry:'vacate'}]}));
 const r=d.monthly.rent;
 ok('T2 forced-vacate: downtime months earn 0',near(r[6],0,1e-9)&&near(r[8],0,1e-9),[r[6],r[8]].join('/'));
 ok('T2 free-rent months earn 0',near(r[9],0,1e-9)&&near(r[10],0,1e-9),[r[9],r[10]].join('/'));
 ok('T2 first paying month = market 2,000',near(r[11],2000,1e-9),r[11]);
 ok('T2 yr-1 TI+LC = 12,400 at rollover',near(d.annual[0].cap,12400,1e-6),d.annual[0].cap);}
{const d=computeDeal(base({analysis:{holdMonths:24,discountRate:0.075,creditLoss:0},
   property:{suites:[{id:'S1',name:'A',sf:1000}]},
   rentRoll:[{id:'L1',suiteId:'S1',sf:1000,startMonth:0,termMonths:60,baseRent:1,
     escalation:{type:'fixedPct',value:0.10},freeMonths:0,recoveryPct:0,mlaId:'MX',uponExpiry:'renew'}]}));
 const r=d.monthly.rent;
 ok('T3 escalation bumps on anniversary',near(r[11],1000,1e-9)&&near(r[12],1100,1e-9),[r[11],r[12]].join('/'));}
{const d=computeDeal(base({analysis:{holdMonths:24,discountRate:0.075,creditLoss:0},
   property:{suites:[{id:'S1',name:'A',sf:1000}]},
   mlas:[{id:'M1',name:'X',marketRent:2,rentGrowth:0,termMonths:24,renewalProb:0.5,downtimeMonths:4,
     freeNew:0,freeRenew:0,tiNew:0,tiRenew:0,lcNew:0,lcRenew:0,escalation:{type:'none'},recoveryPct:0}],
   rentRoll:[{id:'L1',suiteId:'S1',sf:1000,startMonth:0,termMonths:6,baseRent:1,
     escalation:{type:'none'},freeMonths:0,recoveryPct:0,mlaId:'M1',uponExpiry:'market'}]}));
 const r=d.monthly.rent;
 ok('T4 blended rollover: p=0.5 downtime earns half',near(r[6],1000,1e-9)&&near(r[9],1000,1e-9)&&near(r[10],2000,1e-9),
    [r[6],r[9],r[10]].join('/'));}
{const d=computeDeal(base({rentRoll:[{id:'L1',suiteId:'S1',sf:10000,startMonth:0,termMonths:60,baseRent:2,
   escalation:{type:'none'},freeMonths:0,recoveryPct:0,mlaId:'MX',uponExpiry:'renew'}],
   equity:{lpShare:0.9,pref:0.08,promote:0.2}}));
 ok('T5 waterfall conserves cash (LP+GP = deal profit)',near(d.lpProfit+d.gpProfit,d.profit,1e-6),
    (d.lpProfit+d.gpProfit)+' vs '+d.profit);
 ok('T5 LP IRR < combined < GP IRR',d.lpIrr<d.irrL&&d.irrL<d.gpIrr,[d.lpIrr,d.irrL,d.gpIrr].join('/'));}
{const d=computeDeal(base({analysis:{holdMonths:24,discountRate:0.075,creditLoss:0},
   rentRoll:[{id:'L1',suiteId:'S1',sf:10000,startMonth:0,termMonths:60,baseRent:2,
     escalation:{type:'none'},freeMonths:0,recoveryPct:0,mlaId:'MX',uponExpiry:'renew'}],
   debt:{type:'amount',amount:1200000,rate:0.06,ioMonths:12,amortMonths:360}}));
 const ds=d.monthly.ds;
 ok('T6 IO payment 6,000/mo then PMT ~7,194.61',near(ds[1],6000,0.01)&&near(ds[13],7194.61,0.2),[ds[1],ds[13]].join('/'));
 ok('T6 balance amortizes below loan',d.balSale<1200000,d.balSale);}

console.log('--- Part A: recovery subsystem (Phase 2) ---');
{const d=computeDeal(base({analysis:{holdMonths:12,discountRate:0.075,creditLoss:0},
   property:{suites:[{id:'S1',name:'A',sf:1000},{id:'S2',name:'B',sf:1000}]},
   rentRoll:[{id:'L1',suiteId:'S1',sf:1000,startMonth:0,termMonths:60,baseRent:1,
     escalation:{type:'none'},freeMonths:0,recMethod:'net',recParam:100,mlaId:'MX',uponExpiry:'renew'}],
   expenses:[{name:'cam',basis:'fixed',amount:2400,growth:0,recoverable:true,varOcc:false}]}));
 ok('T8 net recovery = pro-rata share (1,200/yr of 2,400 pool)',near(d.annual[0].rec,1200,1e-6),d.annual[0].rec);}
{const d=computeDeal(base({analysis:{holdMonths:24,discountRate:0.075,creditLoss:0},
   property:{suites:[{id:'S1',name:'A',sf:1000},{id:'S2',name:'B',sf:1000}]},
   rentRoll:[{id:'L1',suiteId:'S1',sf:1000,startMonth:0,termMonths:60,baseRent:1,
     escalation:{type:'none'},freeMonths:0,recMethod:'baseYear',recParam:100,mlaId:'MX',uponExpiry:'renew'}],
   expenses:[{name:'cam',basis:'fixed',amount:2400,growth:0.12,recoverable:true,varOcc:false}]}));
 let expY1=0,expY2=0;
 for(let mm=0;mm<24;mm++){const pool=2400/12*Math.pow(1.12,mm/12);const r=0.5*Math.max(0,pool-200);
   if(mm<12)expY1+=r;else expY2+=r;}
 ok('T9 base-yr stop month-0 reimburses 0',near(d.monthly.recov[0],0,1e-9),d.monthly.recov[0]);
 ok('T9 base-yr stop yr-1 = share of increase only',near(d.annual[0].rec,expY1,1e-6),d.annual[0].rec+' vs '+expY1);
 ok('T9 base-yr stop yr-2 grows with pool',near(d.annual[1].rec,expY2,1e-6),d.annual[1].rec+' vs '+expY2);}
{const d=computeDeal(base({analysis:{holdMonths:12,discountRate:0.075,creditLoss:0},
   property:{suites:[{id:'S1',name:'A',sf:1000},{id:'S2',name:'B',sf:1000}]},
   rentRoll:[{id:'L1',suiteId:'S1',sf:1000,startMonth:-12,termMonths:72,baseRent:1,
     escalation:{type:'none'},freeMonths:0,recMethod:'baseYear',recParam:100,mlaId:'MX',uponExpiry:'renew'}],
   expenses:[{name:'cam',basis:'fixed',amount:2400,growth:0.12,recoverable:true,varOcc:false}]}));
 const expM0=0.5*(200-200/1.12);
 ok('T9b base-yr lookback: month-0 reimburses growth since lease start',near(d.monthly.recov[0],expM0,1e-9),
    d.monthly.recov[0]+' vs '+expM0);}
{const d=computeDeal(base({analysis:{holdMonths:24,discountRate:0.075,creditLoss:0},
   property:{suites:[{id:'S1',name:'A',sf:1000},{id:'S2',name:'B',sf:1000}]},
   rentRoll:[{id:'L1',suiteId:'S1',sf:1000,startMonth:0,termMonths:60,baseRent:1,
     escalation:{type:'fixedPct',value:0.10},freeMonths:0,recMethod:'fixed',recParam:1.2,mlaId:'MX',uponExpiry:'renew'}],
   expenses:[{name:'cam',basis:'fixed',amount:99999,growth:0,recoverable:true,varOcc:false}]}));
 ok('T10 fixed CAM yr-1 = $1.20/SF (1,200)',near(d.annual[0].rec,1200,1e-6),d.annual[0].rec);
 ok('T10 fixed CAM yr-2 escalates 10% (1,320)',near(d.annual[1].rec,1320,1e-6),d.annual[1].rec);}
{const d=computeDeal(base({analysis:{holdMonths:12,discountRate:0.075,creditLoss:0},
   property:{suites:[{id:'S1',name:'A',sf:1000},{id:'S2',name:'B',sf:1000}]},
   recoverySettings:{grossUpOn:true,grossUpPct:0.95,adminFee:0},
   rentRoll:[{id:'L1',suiteId:'S1',sf:1000,startMonth:0,termMonths:60,baseRent:1,
     escalation:{type:'none'},freeMonths:0,recMethod:'net',recParam:100,mlaId:'MX',uponExpiry:'renew'}],
   expenses:[{name:'jan',basis:'fixed',amount:2400,growth:0,recoverable:true,varOcc:true}]}));
 ok('T11 actual variable expense = 1,200 (50% occ)',near(d.annual[0].exp,1200,1e-6),d.annual[0].exp);
 ok('T11 grossed pool billed at 95% -> reimb 1,140',near(d.annual[0].rec,1140,1e-6),d.annual[0].rec);}

console.log('--- Part A: Monte Carlo overlay (Phase 7) ---');
const MCM={version:'wbi7-1',
  analysis:{holdMonths:60,discountRate:0.075,creditLoss:0.01},
  acquisition:{price:5000000,closingPct:0.02},capex:[],
  property:{suites:[{id:'S1',name:'A',sf:10000},{id:'S2',name:'B',sf:10000}]},
  mlas:[{id:'M1',name:'Std',marketRent:2.45,rentGrowth:0.03,termMonths:48,renewalProb:0.6,downtimeMonths:5,
    freeNew:2,freeRenew:1,tiNew:12,tiRenew:4,lcNew:0.05,lcRenew:0.02,
    escalation:{type:'fixedPct',value:0.03},recMethod:'baseYear',recParam:100}],
  rentRoll:[
   {id:'L1',suiteId:'S1',sf:10000,startMonth:-12,termMonths:36,baseRent:2.25,
    escalation:{type:'fixedPct',value:0.03},freeMonths:0,recMethod:'baseYear',recParam:100,mlaId:'M1',uponExpiry:'market'},
   {id:'L2',suiteId:'S2',sf:10000,startMonth:-30,termMonths:48,baseRent:2.35,
    escalation:{type:'fixedPct',value:0.03},freeMonths:0,recMethod:'baseYear',recParam:100,mlaId:'M1',uponExpiry:'market'}],
  absorption:[],
  expenses:[{name:'op',basis:'psf',amount:7,growth:0.03,recoverable:true,varOcc:true},
            {name:'tax',basis:'fixed',amount:60000,growth:0.02,recoverable:true,varOcc:false}],
  recoverySettings:{grossUpOn:true,grossUpPct:0.95,adminFee:0},
  otherIncome:{amount:0,growth:0},
  debt:{type:'ltv',ltv:0.6,amount:0,rate:0.06,ioMonths:12,amortMonths:360},
  exit:{exitCap:0.0675,sellCostPct:0.02},
  equity:{lpShare:0.9,pref:0.08,promote:0.2}};
const {computeMC}=ctx;
const withMC=mc=>Object.assign(JSON.parse(JSON.stringify(MCM)),{mc});
{const r1=computeMC(withMC({trials:400,seed:42}));
 const r2=computeMC(withMC({trials:400,seed:42}));
 ok('T12 same seed -> identical mean IRR',r1.irr.mean===r2.irr.mean,r1.irr.mean+' vs '+r2.irr.mean);
 ok('T12 same seed -> identical P(loss)',r1.pLoss===r2.pLoss,r1.pLoss+' vs '+r2.pLoss);
 const r3=computeMC(withMC({trials:400,seed:43}));
 ok('T12 different seed -> different mean',r1.irr.mean!==r3.irr.mean,r1.irr.mean);}
{const b=computeDeal(MCM);
 const r=computeMC(withMC({trials:60,seed:5,sdRentGrowth:0,sdCap:0,sdRenew:0,sdDowntime:0,sdRate:0}));
 ok('T13 zero-sigma mean == deterministic levered IRR',near(r.irr.mean,b.irrL,1e-12),r.irr.mean+' vs '+b.irrL);
 ok('T13 zero-sigma P5 == P95 (no dispersion)',r.irr.p5===r.irr.p95,r.irr.p5+' vs '+r.irr.p95);}
{const off=computeMC(withMC({trials:1500,seed:11,corrOn:false}));
 const on =computeMC(withMC({trials:1500,seed:11,corrOn:true}));
 const spOff=off.irr.p95-off.irr.p5,spOn=on.irr.p95-on.irr.p5;
 ok('T14 correlated draws widen P5-P95 spread',spOn>spOff,spOn.toFixed(4)+' vs '+spOff.toFixed(4));
 ok('T14 correlated left tail (P5) worse or equal',on.irr.p5<=off.irr.p5+1e-9,on.irr.p5+' vs '+off.irr.p5);}
{const r=computeMC(withMC({trials:800,seed:3}));
 ok('T15 trial count honored',r.N===800,r.N);
 ok('T15 P(loss) in [0,1]',r.pLoss>=0&&r.pLoss<=1,r.pLoss);
 ok('T15 P5 <= P50 <= P95',r.irr.p5<=r.irr.p50&&r.irr.p50<=r.irr.p95,[r.irr.p5,r.irr.p50,r.irr.p95].join('/'));
 ok('T15 histogram counts sum to IRR-defined trials',r.hist.counts.reduce((s,x)=>s+x,0)===r.N-r.nNull,
    r.hist.counts.reduce((s,x)=>s+x,0)+' vs '+(r.N-r.nNull));
 ok('T15 EM stats present',r.em.p50!=null&&isFinite(r.em.mean),JSON.stringify(r.em));}

console.log('--- Part A: Refinance module ---');
const {E_waterfall,E_waterfallTiered,E_irrM:IRRM,E_ann:ANN}=ctx;
function rbase(over){return Object.assign({version:'wbi7-1',
  analysis:{holdMonths:60,discountRate:0.075,creditLoss:0},
  acquisition:{price:5000000,closingPct:0},capex:[],
  property:{suites:[{id:'S1',name:'A',sf:50000}]},
  mlas:[],rentRoll:[{id:'L1',suiteId:'S1',sf:50000,startMonth:0,termMonths:120,baseRent:1.0,
    escalation:{type:'fixedPct',value:0.03},freeMonths:0,recMethod:'none',recParam:0,mlaId:'MX',uponExpiry:'renew'}],
  absorption:[],expenses:[{name:'op',basis:'psf',amount:3,growth:0.03,recoverable:false,varOcc:false}],
  otherIncome:{amount:0,growth:0},
  debt:{type:'ltv',ltv:0.6,amount:0,rate:0.06,ioMonths:0,amortMonths:360},
  exit:{exitCap:0.07,sellCostPct:0},equity:{lpShare:1,pref:0,promote:0}},over);}
{const noRefi=computeDeal(rbase({}));
 const d=computeDeal(rbase({debt:{type:'ltv',ltv:0.6,amount:0,rate:0.06,ioMonths:0,amortMonths:360,
   refiOn:true,refiMonth:36,refiSizing:'ltv',refiLtv:0.65,refiCap:0.07,refiRate:0.055,refiIoMonths:0,refiAmortMonths:360,refiCostPct:0.01}}));
 ok('T16 refi flagged on',d.refiOn===true,d.refiOn);
 ok('T16 refiNet = newLoan - payoff - costs',near(d.refiNet,d.newLoan-d.balAtRefi-d.newLoan*0.01,1e-6),d.refiNet);
 ok('T16 new loan = 65% of refi value',near(d.newLoan,d.refiValue*0.65,1e-6),d.newLoan);
 ok('T16 refi leaves unlevered IRR unchanged',near(d.irrU,noRefi.irrU,1e-9),d.irrU+' vs '+noRefi.irrU);
 ok('T16 refi changes levered IRR',Math.abs(d.irrL-noRefi.irrL)>1e-4,d.irrL+' vs '+noRefi.irrL);
 ok('T16 cash-out lands in equity at refi month',near(d.eq[36],noRefi.eq[36]+d.refiNet,1e-6),d.eq[36]);}
{const d=computeDeal(rbase({debt:{type:'ltv',ltv:0.6,amount:0,rate:0.06,ioMonths:0,amortMonths:360,
   refiOn:true,refiMonth:24,refiSizing:'dscr',refiDscr:1.25,refiCap:0.07,refiRate:0.06,refiIoMonths:0,refiAmortMonths:360,refiCostPct:0}}));
 const dd=computeDeal(rbase({}));let noiRefi=0;for(let mm=24;mm<36;mm++)noiRefi+=dd.monthly.noi[mm];
 const r2M=0.06/12,kconst=(r2M/(1-Math.pow(1+r2M,-360)))*12;
 ok('T17 DSCR-sized loan = NOI/(DSCR x constant)',near(d.newLoan,noiRefi/(1.25*kconst),1.0),d.newLoan);}
{const d=computeDeal(rbase({debt:{type:'ltv',ltv:0.6,amount:0,rate:0.07,ioMonths:0,amortMonths:360,
   refiOn:true,refiMonth:36,refiSizing:'amount',refiAmount:0,refiRate:0.05,refiIoMonths:0,refiAmortMonths:360,refiCostPct:0}}));
 ok('T18 zero new loan -> refiNet = -payoff',near(d.refiNet,-d.balAtRefi,1e-6),d.refiNet);
 ok('T18 zero new loan -> no balance at sale',near(d.balSale,0,1e-9),d.balSale);}

console.log('--- Part A: Multi-tier IRR-hurdle waterfall ---');
{const cf=[-1000];for(let t=1;t<60;t++)cf.push(18);cf.push(1500);
 const A=E_waterfall(cf,0.9,0.08,0.20),B=E_waterfallTiered(cf,0.9,[{hurdle:0.08,promote:0.20}]);
 const lpA=A.lp.reduce((s,x)=>s+x,0),lpB=B.lp.reduce((s,x)=>s+x,0);
 const gpA=A.gp.reduce((s,x)=>s+x,0),gpB=B.gp.reduce((s,x)=>s+x,0);
 ok('T20 tiered single-tier reduces to E_waterfall (LP profit <$1)',near(lpA,lpB,1.0),lpA.toFixed(2)+' vs '+lpB.toFixed(2));
 ok('T20 tiered single-tier reduces to E_waterfall (GP profit <$1)',near(gpA,gpB,1.0),gpA.toFixed(2)+' vs '+gpB.toFixed(2));
 ok('T20 tiered single-tier LP IRR matches (<2bps)',near(ANN(IRRM(A.lp)),ANN(IRRM(B.lp)),0.0002),'');}
{const cf=[-1000];for(let t=1;t<60;t++)cf.push(20);cf.push(2200);
 const W=E_waterfallTiered(cf,0.9,[{hurdle:0.08,promote:0.20},{hurdle:0.12,promote:0.30},{hurdle:0.15,promote:0.40}]);
 const tot=cf.reduce((s,x)=>s+x,0),lp=W.lp.reduce((s,x)=>s+x,0),gp=W.gp.reduce((s,x)=>s+x,0);
 ok('T21 3-tier conserves cash',near(lp+gp,tot,1e-6),(lp+gp).toFixed(2)+' vs '+tot.toFixed(2));
 ok('T21 LP IRR < deal < GP IRR',ANN(IRRM(W.lp))<ANN(IRRM(cf))&&ANN(IRRM(cf))<ANN(IRRM(W.gp)),'');}
{const cf=[-1000];for(let t=1;t<60;t++)cf.push(20);cf.push(2600);
 const single=E_waterfallTiered(cf,0.9,[{hurdle:0.08,promote:0.20}]);
 const multi =E_waterfallTiered(cf,0.9,[{hurdle:0.08,promote:0.20},{hurdle:0.12,promote:0.35},{hurdle:0.18,promote:0.50}]);
 ok('T22 higher promote tiers reduce LP profit',multi.lp.reduce((s,x)=>s+x,0)<single.lp.reduce((s,x)=>s+x,0),'');}

console.log('--- Part A: Inflation factor (real returns + CPI) ---');
{const d=computeDeal(rbase({analysis:{holdMonths:60,discountRate:0.075,creditLoss:0,inflation:0.025}}));
 ok('T24 real levered IRR = Fisher(nominal)',near(d.realIrrL,(1+d.irrL)/1.025-1,1e-12),d.realIrrL);
 ok('T24 real unlevered IRR = Fisher(nominal)',near(d.realIrrU,(1+d.irrU)/1.025-1,1e-12),d.realIrrU);
 ok('T24 real IRR below nominal at positive inflation',d.realIrrL<d.irrL,'');}
{const d=computeDeal(rbase({analysis:{holdMonths:60,discountRate:0.075,creditLoss:0,inflation:0}}));
 ok('T25 zero inflation -> real IRR == nominal',near(d.realIrrL,d.irrL,1e-12)&&near(d.realIrrU,d.irrU,1e-12),'');}
{const cpi=computeDeal(rbase({analysis:{holdMonths:60,discountRate:0.075,creditLoss:0,inflation:0.04},
   rentRoll:[{id:'L1',suiteId:'S1',sf:50000,startMonth:0,termMonths:120,baseRent:1.0,
     escalation:{type:'cpi'},freeMonths:0,recMethod:'none',recParam:0,mlaId:'MX',uponExpiry:'renew'}]}));
 const fix=computeDeal(rbase({analysis:{holdMonths:60,discountRate:0.075,creditLoss:0,inflation:0.04},
   rentRoll:[{id:'L1',suiteId:'S1',sf:50000,startMonth:0,termMonths:120,baseRent:1.0,
     escalation:{type:'fixedPct',value:0.04},freeMonths:0,recMethod:'none',recParam:0,mlaId:'MX',uponExpiry:'renew'}]}));
 ok('T26 CPI escalation == fixedPct at inflation rate',near(cpi.annual[0].noi,fix.annual[0].noi,1e-6)&&near(cpi.monthly.rent[12],52000,1e-6),cpi.monthly.rent[12]);}

console.log('--- Part A: After-tax module (depreciation, recapture, capital gains) ---');
const TAXON={enabled:true,landPct:0.20,depreciationYears:39,ordinaryRate:0.37,capGainsRate:0.20,recaptureRate:0.25};
{const d=computeDeal(rbase({tax:Object.assign({},TAXON)}));
 ok('T28 tax off by default -> afterTaxIrrL null',computeDeal(rbase({})).afterTaxIrrL===null,'');
 ok('T29 depreciable basis = allIn x (1-land)',near(d.depBasis,d.allIn*0.8,1e-6),d.depBasis);
 ok('T29 accum dep = (basis/(39*12)) x hold',near(d.accumDep,(d.allIn*0.8/(39*12))*d.M,1e-6),d.accumDep);
 ok('T29 adjusted basis = cost - accum dep',near(d.adjBasis,d.allIn-d.accumDep,1e-6),d.adjBasis);
 ok('T30 recapture = min(dep,gain) x 25%',near(d.recaptureTax,Math.min(d.accumDep,Math.max(0,d.totalGain))*0.25,1e-6),d.recaptureTax);
 ok('T30 cap-gains = remaining gain x 20%',near(d.capGainsTax,Math.max(0,d.totalGain-Math.min(d.accumDep,Math.max(0,d.totalGain)))*0.20,1e-6),d.capGainsTax);
 ok('T30 after-tax proceeds = proceeds - sale tax',near(d.afterTaxProceeds,d.proceeds-d.taxOnSale,1e-6),d.afterTaxProceeds);
 ok('T31 after-tax IRR below before-tax (positive tax)',d.afterTaxIrrL<d.irrL,(d.afterTaxIrrL*100).toFixed(2)+' vs '+(d.irrL*100).toFixed(2));}
{const sh=computeDeal(rbase({tax:Object.assign({},TAXON)}));
 const ns=computeDeal(rbase({tax:Object.assign({},TAXON,{landPct:1.0})}));
 ok('T31b depreciation shield raises after-tax IRR',sh.afterTaxIrrL>ns.afterTaxIrrL,'');}
{const d=computeDeal(rbase({tax:Object.assign({},TAXON,{ordinaryRate:0,capGainsRate:0,recaptureRate:0})}));
 ok('T32 zero tax rates -> after-tax == before-tax IRR',near(d.afterTaxIrrL,d.irrL,1e-9)&&near(d.taxOnSale,0,1e-9),'');}

/* ---------------- Part B: browser golden-master tests ---------------- */
/* Representative display goldens (one per asset class). Lock the render path. */
const DISPLAY_GOLDENS={
  "mf-sd-48":{rUIrr:'6.7%',rUEm:'1.71\u00d7',rLIrr:'7.4%',rLEm:'1.95\u00d7',rMirr:'7.4%',
    rPvTot:'$18,200,186',rValue:'$22,121,846',rDyF:'10.4%',rDcr:'1.10',
    suOcc:'100.0%',suWalt:'0.4 yrs',suGoin:'4.8%',wLpIrr:'7.4%',wGpIrr:'7.4%',totSF:'40,320 sf'},
  "ind-oak-multi":{rUIrr:'10.5%',rUEm:'1.80\u00d7',rLIrr:'14.7%',rLEm:'2.28\u00d7',rMirr:'13.5%',
    rPvTot:'$23,840,030',rValue:'$27,222,094',rDyF:'13.9%',rDcr:'1.78',
    suOcc:'100.0%',suWalt:'3.1 yrs',suGoin:'6.7%',wLpIrr:'14.1%',wGpIrr:'19.6%',totSF:'88,000 sf'},
  "off-sf-fidi":{rUIrr:'7.8%',rUEm:'1.75\u00d7',rLIrr:'8.3%',rLEm:'1.79\u00d7',rMirr:'8.2%',
    rPvTot:'$51,450,271',rValue:'$72,424,137',rDyF:'19.0%',rDcr:'1.61',
    suOcc:'80.0%',suWalt:'5.2 yrs',suGoin:'6.1%',wLpIrr:'8.2%',wGpIrr:'8.5%',totSF:'95,000 sf'},
  "ret-grocery":{rUIrr:'7.1%',rUEm:'1.71\u00d7',rLIrr:'7.6%',rLEm:'1.82\u00d7',rMirr:'7.6%',
    rPvTot:'$34,756,854',rValue:'$40,404,115',rDyF:'13.7%',rDcr:'1.60',
    suOcc:'100.0%',suWalt:'6.5 yrs',suGoin:'5.9%',wLpIrr:'7.6%',wGpIrr:'7.6%',totSF:'83,300 sf'},
  "spec-selfstore":{rUIrr:'15.7%',rUEm:'2.57\u00d7',rLIrr:'24.8%',rLEm:'4.26\u00d7',rMirr:'21.0%',
    rPvTot:'$20,404,730',rValue:'$23,446,766',rDyF:'19.5%',rDcr:'2.06',
    suOcc:'100.0%',suWalt:'0.7 yrs',suGoin:'8.2%',wLpIrr:'23.6%',wGpIrr:'32.6%',totSF:'88,000 sf'}
};
const EXPECT_CATS={Multifamily:5,Industrial:5,Office:5,Retail:5,Specialty:5};
async function browserTests(){
  const CHROME=process.env.CHROME_PATH;
  if(!CHROME){console.log('\n--- Part B skipped (set CHROME_PATH for browser golden tests) ---');return;}
  let puppeteer;try{puppeteer=require('puppeteer-core');}catch(e){
    console.log('\n--- Part B skipped (npm i puppeteer-core) ---');return;}
  console.log('\n--- Part B: browser golden-master tests ---');
  const sleep=ms=>new Promise(r=>setTimeout(r,ms));
  const b=await puppeteer.launch({executablePath:CHROME,headless:'new',
    args:['--no-sandbox','--disable-setuid-sandbox','--disable-dev-shm-usage']});
  const p=await b.newPage();
  const consoleErrs=[];
  p.on('pageerror',e=>consoleErrs.push(e.message));
  p.on('console',m=>{if(m.type()==='error'&&!/cdnjs|403|Failed to load resource|fonts.g/.test(m.text()))consoleErrs.push(m.text());});
  await p.goto('file://'+path.resolve(HTML),{waitUntil:'domcontentloaded'});
  await p.evaluate(()=>{try{localStorage.clear()}catch(e){}});
  await p.reload({waitUntil:'domcontentloaded'});
  await p.type('#gatekey','wrong');await p.click('#gatego');await sleep(250);
  ok('gate: wrong key leaves page intact',await p.evaluate(()=>!!document.getElementById('gatekey')));
  await p.type('#gatekey','wbi7');await p.click('#gatego');await sleep(900);
  ok('gate: correct key opens app',await p.evaluate(()=>{const a=document.getElementById('app');return a&&!a.classList.contains('hidden');}));
  const txt=id=>p.evaluate(i=>{const e=document.getElementById(i);return e?e.textContent:null;},id);

  // --- preset library shape: 25 presets, 5 per category, grouped menu ---
  const lib=await p.evaluate(()=>{
    const ps=window.__wbi7.PRESETS;const cats={};Object.keys(ps).forEach(k=>{cats[ps[k].cat]=(cats[ps[k].cat]||0)+1;});
    const groups={};document.querySelectorAll('#presetSel optgroup').forEach(o=>groups[o.label]=o.children.length);
    return{total:Object.keys(ps).length,cats,groups};});
  ok('library: 25 presets total',lib.total===25,lib.total);
  for(const c of Object.keys(EXPECT_CATS)){
    ok('library: '+c+' has '+EXPECT_CATS[c]+' presets',lib.cats[c]===EXPECT_CATS[c],lib.cats[c]);
    ok('menu: '+c+' optgroup shows '+EXPECT_CATS[c],lib.groups[c]===EXPECT_CATS[c],lib.groups[c]);
  }

  // --- structural invariants across ALL 25 presets (engine-level) ---
  const keys=await p.evaluate(()=>Object.keys(window.__wbi7.PRESETS));
  let cleanAll=true,saneAll=true,mxAll=true;
  for(const k of keys){
    const r=await p.evaluate(key=>{
      try{const m=JSON.parse(JSON.stringify(window.__wbi7.PRESETS[key]));
        const d=window.__wbi7.computeDeal(m);
        const lpOk=(d.lpIrr==null||d.irrL==null)?true:(d.lpIrr<=d.irrL+1e-9&&d.irrL<=d.gpIrr+1e-9);
        const cons=Math.abs(d.lpProfit+d.gpProfit-d.profit)<1;
        return{ok:true,sf:d.sfTot,allIn:d.allIn,occ:d.occ0,goin:d.goin,em:d.emL,irrL:d.irrL,lpOk,cons};
      }catch(e){return{ok:false,err:e.message};}
    },k);
    if(!r.ok){cleanAll=false;console.log('     compute FAIL '+k+': '+r.err);continue;}
    const sane=r.sf>0&&r.allIn>0&&r.occ>0&&r.goin>0.03&&r.goin<0.12&&r.em>0.7&&
      (r.irrL===null||(r.irrL>-0.15&&r.irrL<0.45))&&r.lpOk&&r.cons;
    if(!sane){saneAll=false;console.log('     sanity FAIL '+k+': '+JSON.stringify(r));}
  }
  ok('all 25 presets compute without error',cleanAll);
  ok('all 25 presets pass sanity (occ>0, going-in 3-12%, EM>0.7, LP<=deal<=GP, conservation)',saneAll);

  // --- representative display goldens + matrices + MC ---
  for(const preset of Object.keys(DISPLAY_GOLDENS)){
    await p.select('#presetSel',preset);await sleep(550);
    for(const [id,want] of Object.entries(DISPLAY_GOLDENS[preset])){
      const got=await txt(id);ok(preset+'.'+id+' == "'+want+'"',got===want,'got "'+got+'"');}
    const mx=await p.evaluate(()=>{
      const pvC=document.querySelectorAll('#mxPvWrap td.out').length;
      const irC=document.querySelectorAll('#mxIrrWrap td.out').length;
      const pvShaded=[...document.querySelectorAll('#mxPvWrap td.out')].filter(c=>/rgba/.test(c.getAttribute('style')||'')).length;
      const pvB=document.querySelector('#mxPvWrap td[style*="bold"]');
      const irB=document.querySelector('#mxIrrWrap td[style*="bold"]');
      return{pvC,irC,pvShaded,pvBold:pvB?pvB.textContent:null,irBold:irB?irB.textContent:null};});
    ok(preset+': PV matrix 25 cells',mx.pvC===25,mx.pvC);
    ok(preset+': IRR matrix 25 cells',mx.irC===25,mx.irC);
    ok(preset+': PV matrix heat-shaded',mx.pvShaded===25,mx.pvShaded);
    {const m=/^\$([\d.]+)M$/.exec(mx.pvBold||'');const val=m?parseFloat(m[1])*1e6:NaN;
     const pvTot=await p.evaluate(()=>window.__lastDeal.pvTot);
     ok(preset+': PV matrix center matches headline',isFinite(val)&&Math.abs(val-pvTot)<=5e4,mx.pvBold+' vs '+Math.round(pvTot));}
    ok(preset+': IRR matrix center matches headline',mx.irBold===(await txt('rLIrr')),mx.irBold+' vs '+(await txt('rLIrr')));
  }

  // --- Monte Carlo on one leveraged preset ---
  await p.select('#presetSel','ind-oak-multi');await sleep(550);
  await p.evaluate(()=>{const e=document.getElementById('mcTrials');e.value='500';e.dispatchEvent(new Event('input',{bubbles:true}));});
  await sleep(300);
  await p.click('#mcRun');
  await p.waitForFunction(()=>window.__lastMC&&document.querySelectorAll('#mcBody tr').length>=4,{timeout:60000});
  const mc=await p.evaluate(()=>{const r=window.__lastMC;return{rows:document.querySelectorAll('#mcBody tr').length,
    chart:document.querySelectorAll('#mcChart *').length,ord:r.irr.p5<=r.irr.p50&&r.irr.p50<=r.irr.p95,N:r.N};});
  ok('MC: 4 result rows',mc.rows===4,mc.rows);
  ok('MC: histogram rendered',mc.chart>0,mc.chart);
  ok('MC: percentiles ordered',mc.ord);
  ok('MC: honored trial count',mc.N===500,mc.N);

  // --- refinance UI: toggle on a value-add deal, verify card + cash-out, then revert ---
  await p.select('#presetSel','mf-hwd-16');await sleep(550);
  const irrPre=await txt('rLIrr');
  ok('refi: card hidden when off',await p.evaluate(()=>getComputedStyle(document.getElementById('refiCard')).display==='none'));
  await p.evaluate(()=>{const c=document.getElementById('refiOn');c.checked=true;c.dispatchEvent(new Event('change',{bubbles:true}));
    const set=(id,val)=>{const e=document.getElementById(id);e.value=val;e.dispatchEvent(new Event('input',{bubbles:true}));};
    set('refiMonth',24);set('refiSizing','ltv');set('refiCap',5.5);set('refiLtv',70);set('refiRate',5.75);set('refiIO',24);set('refiCost',1);});
  await sleep(550);
  ok('refi: card shows when on',await p.evaluate(()=>getComputedStyle(document.getElementById('refiCard')).display!=='none'));
  const rf=await p.evaluate(()=>{const d=window.__lastDeal;return{on:d.refiOn,net:d.refiNet,
    netOk:Math.abs(d.refiNet-(d.newLoan-d.balAtRefi-d.newLoan*0.01))<1,inEq:Math.abs(d.eq[24])>1};});
  ok('refi: engine reports refinance on',rf.on===true);
  ok('refi: net cash-out = newLoan - payoff - costs',rf.netOk,rf.net);
  await p.evaluate(()=>{const c=document.getElementById('refiOn');c.checked=false;c.dispatchEvent(new Event('change',{bubbles:true}));});
  await sleep(450);
  ok('refi: toggling off reverts IRR to baseline',(await txt('rLIrr'))===irrPre,(await txt('rLIrr'))+' vs '+irrPre);

  // --- multi-tier waterfall UI on a high-return deal ---
  await p.select('#presetSel','spec-selfstore');await sleep(550);
  const lpPre=await txt('wLpIrr');
  await p.evaluate(()=>{const c=document.getElementById('tiersOn');c.checked=true;c.dispatchEvent(new Event('change',{bubbles:true}));
    const addBtn=document.querySelector('[data-add="tier"]');addBtn.click();addBtn.click();addBtn.click();});
  await sleep(300);
  await p.evaluate(()=>{const rows=[...document.querySelectorAll('#tierRows tr')];const vals=[[8,20],[12,35],[18,50]];
    rows.forEach((r,i)=>{const inp=r.querySelectorAll('input');
      inp[0].value=vals[i][0];inp[0].dispatchEvent(new Event('input',{bubbles:true}));
      inp[1].value=vals[i][1];inp[1].dispatchEvent(new Event('input',{bubbles:true}));});});
  await sleep(550);
  const wf=await p.evaluate(()=>{const d=window.__lastDeal;return{rows:document.querySelectorAll('#tierRows tr').length,
    cons:Math.abs(d.lpProfit+d.gpProfit-d.profit)<1,lpIrr:d.lpIrr};});
  ok('tiers: 3 tier rows present',wf.rows===3,wf.rows);
  ok('tiers: waterfall conserves cash',wf.cons);
  ok('tiers: more promote lowers LP IRR vs single-tier',(wf.lpIrr*100).toFixed(1)+'%'!==lpPre&&wf.lpIrr<parseFloat(lpPre)/100+1e-9,
     (wf.lpIrr*100).toFixed(1)+'% vs '+lpPre);

  // --- inflation factor: real IRR display + CPI toggle ---
  await p.select('#presetSel','ind-oak-multi');await sleep(550);
  ok('inflation: input present',await p.evaluate(()=>!!document.getElementById('inflation')));
  await p.evaluate(()=>{const e=document.getElementById('inflation');e.value='3';e.dispatchEvent(new Event('input',{bubbles:true}));});
  await sleep(450);
  const infl=await p.evaluate(()=>{const d=window.__lastDeal;
    return{realL:d.realIrrL,nomL:d.irrL,shown:document.getElementById('rRealLIrr').textContent,
      fisher:Math.abs(d.realIrrL-((1+d.irrL)/1.03-1))<1e-9,below:d.realIrrL<d.irrL,inflEcho:d.inflation};});
  ok('inflation: engine uses 3% input',Math.abs(infl.inflEcho-0.03)<1e-9,infl.inflEcho);
  ok('inflation: real IRR = Fisher(nominal)',infl.fisher);
  ok('inflation: real IRR renders and is below nominal',/%$/.test(infl.shown)&&infl.below,infl.shown);
  // CPI checkbox exists in rent-roll rows
  ok('inflation: CPI toggle present on leases',await p.evaluate(()=>!!document.querySelector('#rrRows tr [data-k="cpi"]')));
  {await p.evaluate(()=>{const e=document.getElementById('inflation');e.value='8';e.dispatchEvent(new Event('input',{bubbles:true}));});
   await sleep(450);
   const before=await txt('rLIrr');
   await p.evaluate(()=>{const cb=document.querySelector('#rrRows tr [data-k="cpi"]');cb.checked=true;cb.dispatchEvent(new Event('change',{bubbles:true}));});
   await sleep(450);
   // lease escalation was 3%; CPI now pegs it to 8% inflation -> rent stream and IRR must move
   ok('inflation: toggling CPI (8% vs 3% esc) recomputes returns',(await txt('rLIrr'))!==before,(await txt('rLIrr'))+' vs '+before);}

  // --- after-tax module: enable on a preset, verify card + ordering ---
  await p.select('#presetSel','ind-oak-multi');await sleep(550);
  ok('tax: after-tax card hidden by default',await p.evaluate(()=>getComputedStyle(document.getElementById('taxCard')).display==='none'));
  const btIrr=await txt('rLIrr');
  await p.evaluate(()=>{const c=document.getElementById('taxOn');c.checked=true;c.dispatchEvent(new Event('change',{bubbles:true}));});
  await sleep(550);
  ok('tax: after-tax card shows when enabled',await p.evaluate(()=>getComputedStyle(document.getElementById('taxCard')).display!=='none'));
  const tx=await p.evaluate(()=>{const d=window.__lastDeal;return{on:d.taxOn,atIrr:d.afterTaxIrrL,bt:d.irrL,
    basisOk:Math.abs(d.depBasis-d.allIn*0.8)<1,saleOk:Math.abs(d.taxOnSale-(d.recaptureTax+d.capGainsTax))<1,
    shown:document.getElementById('atIrr').textContent}});
  ok('tax: engine reports tax on',tx.on===true);
  ok('tax: depreciable basis = allIn x (1-20%)',tx.basisOk,tx.basisOk);
  ok('tax: sale tax = recapture + cap gains',tx.saleOk);
  ok('tax: after-tax IRR renders and is below before-tax',/%$/.test(tx.shown)&&tx.atIrr<tx.bt,tx.shown+' vs '+(tx.bt*100).toFixed(1)+'%');
  ok('tax: before-tax IRR unchanged by enabling tax',(await txt('rLIrr'))===btIrr,(await txt('rLIrr'))+' vs '+btIrr);
  await p.evaluate(()=>{const c=document.getElementById('taxOn');c.checked=false;c.dispatchEvent(new Event('change',{bubbles:true}));});
  await sleep(400);
  ok('tax: disabling hides the after-tax card again',await p.evaluate(()=>getComputedStyle(document.getElementById('taxCard')).display==='none'));

  // --- theme + persistence ---
  await p.select('#themeMode','dark');await sleep(150);
  ok('theme: dark mode applies',await p.evaluate(()=>document.documentElement.dataset.theme==='dark'));
  await p.reload({waitUntil:'domcontentloaded'});
  await p.type('#gatekey','wbi7');await p.click('#gatego');await sleep(800);
  ok('persistence: theme survives reload',await p.evaluate(()=>document.documentElement.dataset.theme==='dark'));
  ok('persistence: model survives reload',await p.evaluate(()=>{const m=window.__wbi7.collectModel();return m.project==='ind-oak-multi';}));

  ok('no uncaught console/page errors during session',consoleErrs.length===0,consoleErrs.join(' | '));
  await b.close();
}
browserTests().then(()=>{
  console.log('\n'+pass+' passed, '+fail+' failed.');
  process.exit(fail?1:0);
}).catch(e=>{console.error('Harness error:',e.message);process.exit(2);});
