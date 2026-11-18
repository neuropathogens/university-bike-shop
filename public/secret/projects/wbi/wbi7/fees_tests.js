/* WBI7 — tests for sponsor (GP) fees: acquisition, financing, asset-management,
   disposition, and construction-management. Fees are transfers from the equity pool to
   the GP, so deal-level returns (project IRR, equity multiple, value, total profit) are
   unchanged; they only shift the LP/GP split — the LP bears the fees on its capital and
   the GP receives them. All default 0, so the presets are byte-identical. */
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

function mkDeal(fees,over){const m=Object.assign({version:'wbi7-1',
  analysis:{holdMonths:60,discountRate:0.08,creditLoss:0,inflation:0.025},
  acquisition:{price:20000000,closingPct:0.02,reassess:false,taxRate:0.0115},
  capex:[{month:6,amount:500000,desc:'reno'}],property:{suites:[{id:'S1',name:'U1',sf:100000}]},
  mlas:[{id:'M1',name:'flex',marketRent:1.6,rentGrowth:0.03,termMonths:120,renewalProb:0.7,downtimeMonths:6,
    freeNew:0,freeRenew:0,tiNew:0,tiRenew:0,lcNew:0,lcRenew:0,escalation:{type:'fixedPct',value:0.03},recMethod:'net',recParam:100}],
  rentRoll:[{id:'L1',tenant:'A',suiteId:'S1',sf:100000,startMonth:-6,termMonths:120,baseRent:1.6,escalation:{type:'fixedPct',value:0.03},freeMonths:0,recMethod:'net',recParam:100,mlaId:'M1',uponExpiry:'market'}],
  absorption:[],expenses:[{name:'Opex',basis:'psf',amount:3,growth:0.03,recoverable:false,varOcc:false}],
  recoverySettings:{grossUpOn:false,grossUpPct:0.95,adminFee:0},otherIncome:{amount:0,growth:0},
  debt:{type:'ltv',ltv:0.6,amount:0,rate:0.06,ioMonths:0,amortMonths:360,termMonths:0,refiOn:false,refiLtv:0.6,refiRate:0.06,refiCostPct:0,mezz:{amount:0,rate:0}},
  exit:{exitCap:0.07,sellCostPct:0.02},equity:{lpShare:0.9,pref:0.08,promote:0.2},
  fees:fees||{}},over);return m;}

console.log('--- sponsor (GP) fees ---');
const noFee=computeDeal(mkDeal({}));
const price=20000000, loan=0.6*price, capex=500000;

// 1. deal-level metrics unchanged by fees
{const d=computeDeal(mkDeal({acqPct:0.01,finPct:0.005,amRate:0.015,amBase:'equity',dispPct:0.01,cmPct:0.04}));
 ok('project IRR, equity multiple, value and total profit are unchanged by fees',
    near(d.irrL,noFee.irrL,1e-12)&&near(d.emL,noFee.emL,1e-12)&&near(d.value,noFee.value,1e-6)&&near(d.lpProfit+d.gpProfit,noFee.lpProfit+noFee.gpProfit,1),'');}

// 2. fees shift the split: LP down, GP up
{const d=computeDeal(mkDeal({amRate:0.02,amBase:'equity'}));
 ok('fees lower the LP IRR and raise the GP IRR',d.lpIrr<noFee.lpIrr&&d.gpIrr>noFee.gpIrr,
    'LP '+(noFee.lpIrr*100).toFixed(2)+'->'+(d.lpIrr*100).toFixed(2));}

// 3. acquisition fee = pct x price
{const d=computeDeal(mkDeal({acqPct:0.0125}));
 ok('acquisition fee equals the rate times the purchase price',near(d.fees.acq,0.0125*price),d.fees.acq.toFixed(0));}

// 4. financing fee = pct x loan (close), plus pct x new loan at a refi
{const d=computeDeal(mkDeal({finPct:0.01}));
 ok('financing fee equals the rate times the loan at close',near(d.fees.financing,0.01*loan),d.fees.financing.toFixed(0));
 const dR=computeDeal(mkDeal({finPct:0.01},{debt:Object.assign(mkDeal({}).debt,{termMonths:36,refiLtv:0.6,refiRate:0.06})}));
 ok('financing fee picks up the refinance loan when the loan matures',dR.fees.financing>0.01*loan+1,dR.fees.financing.toFixed(0));}

// 5. disposition fee = pct x gross sale value
{const d=computeDeal(mkDeal({dispPct:0.015}));
 ok('disposition fee equals the rate times the gross sale value',near(d.fees.disposition,0.015*noFee.value),d.fees.disposition.toFixed(0));}

// 6. construction-management fee = pct x capex
{const d=computeDeal(mkDeal({cmPct:0.05}));
 ok('construction-management fee equals the rate times capex',near(d.fees.construction,0.05*capex),d.fees.construction.toFixed(0));}

// 7. AM fee on equity base = rate x equity x years
{const d=computeDeal(mkDeal({amRate:0.015,amBase:'equity'}));
 const baseEquity=noFee.allIn-noFee.loan, expect=0.015*baseEquity*(60/12);
 ok('asset-management fee on the equity base = rate x invested equity x years',near(d.fees.am,expect,1),d.fees.am.toFixed(0)+' vs '+expect.toFixed(0));}

// 8. AM fee on EGI base = rate x total EGI
{const d=computeDeal(mkDeal({amRate:0.03,amBase:'egi'}));
 const totEGI=noFee.annual.reduce((s,a)=>s+a.egi,0);
 ok('asset-management fee on the EGI base = rate x total EGI',near(d.fees.am,0.03*totEGI,2),d.fees.am.toFixed(0)+' vs '+(0.03*totEGI).toFixed(0));}

// 9. AM fee on NOI base = rate x total NOI
{const d=computeDeal(mkDeal({amRate:0.04,amBase:'noi'}));
 const totNOI=noFee.annual.reduce((s,a)=>s+a.noi,0);
 ok('asset-management fee on the NOI base = rate x total NOI',near(d.fees.am,0.04*totNOI,2),d.fees.am.toFixed(0)+' vs '+(0.04*totNOI).toFixed(0));}

// 10. AM flat fee = flat x years
{const d=computeDeal(mkDeal({amRate:0,amBase:'flat',amFlat:120000}));
 ok('flat asset-management fee = annual amount x years',near(d.fees.am,120000*(60/12),1),d.fees.am.toFixed(0));}

// 11. fees are an internal transfer (LP + GP profit conserved vs no-fee)
{const d=computeDeal(mkDeal({acqPct:0.02,amRate:0.02,amBase:'egi',dispPct:0.01}));
 ok('total LP + GP profit is conserved (fees move profit between them, not out)',near(d.lpProfit+d.gpProfit,noFee.lpProfit+noFee.gpProfit,1),'');}

// 12. zero fees == no fees
{const d=computeDeal(mkDeal({acqPct:0,finPct:0,amRate:0,dispPct:0,cmPct:0}));
 ok('explicit zero fees give the identical split to no fees',near(d.lpProfit,noFee.lpProfit,1e-6)&&near(d.gpProfit,noFee.gpProfit,1e-6),'');}

// 13. immutability
{const m=mkDeal({acqPct:0.02,amRate:0.015,amBase:'equity',dispPct:0.01});const before=JSON.stringify(m);computeDeal(m);computeDeal(m);
 ok('computing the deal never mutates the model',JSON.stringify(m)===before,'model changed');}

console.log('\n'+pass+' passed, '+fail+' failed.');
process.exit(fail?1:0);
