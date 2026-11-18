/* WBI7 — analytic tests for the new modules: percentage rent (retail overage),
   recovery caps, capital reserves, tornado sensitivity, and goal seek. Extracts the
   pure engine from index.html and checks it against hand-computed values, mirroring
   the style of engine_tests2.js / aftertax_tests.js. */
const fs=require('fs'),vm=require('vm');
const html=fs.readFileSync(__dirname+'/index.html','utf8');
const a=html.indexOf('/* ===================== WBI7 ENGINE START');
const b=html.indexOf('WBI7 ENGINE END ===================== */');
const ctx={console};vm.createContext(ctx);
vm.runInContext(html.slice(a,b+'WBI7 ENGINE END ===================== */'.length),ctx);
const {computeDeal,E_tornado,E_goalSeek}=ctx;
let pass=0,fail=0;
const ok=(n,c,x)=>{c?pass++:fail++;console.log((c?'  PASS  ':'  FAIL  ')+n+(c?'':'  -> '+x));};
const near=(a,b,t)=>Math.abs(a-b)<=t;

/* one suite = the whole building, no debt/expenses unless overridden, long hold */
function base(over){return Object.assign({version:'wbi7-1',
  analysis:{holdMonths:120,discountRate:0.075,creditLoss:0,inflation:0},
  acquisition:{price:10000000,closingPct:0},capex:[],
  property:{suites:[{id:'S1',name:'A',sf:10000}]},
  mlas:[{id:'M1',name:'mkt',marketRent:2.0,rentGrowth:0,termMonths:240,renewalProb:1,downtimeMonths:0,
    freeNew:0,freeRenew:0,tiNew:0,tiRenew:0,lcNew:0,lcRenew:0,escalation:{type:'fixedPct',value:0},recMethod:'none',recParam:0}],
  rentRoll:[{id:'L1',suiteId:'S1',sf:10000,startMonth:0,termMonths:240,baseRent:2.0,
    escalation:{type:'fixedPct',value:0},freeMonths:0,recMethod:'none',recParam:0,mlaId:'M1',uponExpiry:'renew'}],
  absorption:[],expenses:[],otherIncome:{amount:0,growth:0},
  debt:{type:'amount',ltv:0,amount:0,rate:0.06,ioMonths:0,amortMonths:360},
  exit:{exitCap:0.07,sellCostPct:0},equity:{lpShare:1,pref:0,promote:0}},over);}

console.log('--- Percentage rent (retail overage) ---');
// annual base rent = 10000 sf x $2.00/sf/mo x 12 = $240,000 (esc 0, flat)
{const d=computeDeal(base({}));
 ok('P0 no pct params -> pctRentTotal 0',d.pctRentTotal===0,d.pctRentTotal);}
{ // natural breakpoint = 240,000 / 6% = $4,000,000; sales $3.0M < bp -> no overage
 const d=computeDeal(base({rentRoll:[{id:'L1',suiteId:'S1',sf:10000,startMonth:0,termMonths:240,baseRent:2.0,
   escalation:{type:'fixedPct',value:0},freeMonths:0,recMethod:'none',recParam:0,mlaId:'M1',uponExpiry:'renew',
   overagePct:6,salesPSF:300,salesGrowth:0,bpType:'natural'}]}));
 ok('P1 natural bp, sales below breakpoint -> 0 overage',near(d.annual[0].pct,0,1e-6),d.annual[0].pct);}
{ // sales $5.0M > $4.0M bp; overage = 6% x (5,000,000 - 4,000,000) = $60,000/yr
 const d=computeDeal(base({rentRoll:[{id:'L1',suiteId:'S1',sf:10000,startMonth:0,termMonths:240,baseRent:2.0,
   escalation:{type:'fixedPct',value:0},freeMonths:0,recMethod:'none',recParam:0,mlaId:'M1',uponExpiry:'renew',
   overagePct:6,salesPSF:500,salesGrowth:0,bpType:'natural'}]}));
 ok('P2 natural bp yr-1 overage = $60,000',near(d.annual[0].pct,60000,1e-6),d.annual[0].pct);
 ok('P2 overage lifts NOI by the overage',near(d.annual[0].noi,d.annual[0].rent+60000,1e-6),d.annual[0].noi);
 // monthly true-up: constant $5M/12 sales cross $4M bp only in the 10th month (index 9)
 ok('P2 no overage before breakpoint crossed (month 8 = 0)',near(d.monthly.pctRent[8],0,1e-9),d.monthly.pctRent[8]);
 ok('P2 overage begins once cumulative crosses bp (month 9 > 0)',d.monthly.pctRent[9]>0,d.monthly.pctRent[9]);}
{ // fixed breakpoint $350/sf/yr -> $3,500,000; overage = 6% x (5,000,000 - 3,500,000) = $90,000
 const d=computeDeal(base({rentRoll:[{id:'L1',suiteId:'S1',sf:10000,startMonth:0,termMonths:240,baseRent:2.0,
   escalation:{type:'fixedPct',value:0},freeMonths:0,recMethod:'none',recParam:0,mlaId:'M1',uponExpiry:'renew',
   overagePct:6,salesPSF:500,salesGrowth:0,bpType:'fixed',bpAmount:350}]}));
 ok('P3 fixed bp yr-1 overage = $90,000',near(d.annual[0].pct,90000,1e-6),d.annual[0].pct);}
{ // overage raises returns vs no overage
 const noP=computeDeal(base({}));
 const withP=computeDeal(base({rentRoll:[{id:'L1',suiteId:'S1',sf:10000,startMonth:0,termMonths:240,baseRent:2.0,
   escalation:{type:'fixedPct',value:0},freeMonths:0,recMethod:'none',recParam:0,mlaId:'M1',uponExpiry:'renew',
   overagePct:6,salesPSF:500,salesGrowth:0,bpType:'natural'}]}));
 ok('P4 overage raises unlevered IRR',withP.irrU>noP.irrU,(withP.irrU*100).toFixed(2)+' vs '+(noP.irrU*100).toFixed(2));
 ok('P4 overage capitalized at exit (higher value)',withP.value>noP.value,withP.value+' vs '+noP.value);}

console.log('--- Recovery caps ---');
// NNN: whole-building net lease (share 100%), one recoverable expense $10/sf/yr growing 10%/yr.
// base monthly pool = 100,000/12 = 8,333.33; ceiling year y (cumulative) = base x 1.05^y.
function capBase(rs){return base({analysis:{holdMonths:48,discountRate:0.075,creditLoss:0,inflation:0},
  rentRoll:[{id:'L1',suiteId:'S1',sf:10000,startMonth:0,termMonths:240,baseRent:2.0,
    escalation:{type:'fixedPct',value:0},freeMonths:0,recMethod:'net',recParam:100,mlaId:'M1',uponExpiry:'renew'}],
  expenses:[{name:'CAM',basis:'psf',amount:10,growth:0.10,recoverable:true,varOcc:false}],
  recoverySettings:rs});}
{const unc=computeDeal(capBase({grossUpOn:false,capPct:0}));
 const cap=computeDeal(capBase({grossUpOn:false,capPct:0.05,capCumulative:true}));
 // year 1 held flat at base-year level: 12 x 8,333.33 = 100,000
 ok('C1 cap holds yr-1 recovery at base-year level (100,000)',near(cap.annual[0].rec,100000,1e-3),cap.annual[0].rec);
 // uncapped yr-1 exceeds base (grows within the year)
 ok('C1 uncapped yr-1 recovery exceeds base (intra-year growth)',unc.annual[0].rec>100000+1,unc.annual[0].rec);
 // ceiling at annual[y] = base x 1.05^y (cumulative cap, base-year=annual[0]):
 //   annual[1] (months 12-23) = base x 1.05^1 = 8,750/mo x 12 = 105,000
 ok('C2 cap yr-2 recovery = base x 1.05^1 x 12 (105,000)',near(cap.annual[1].rec,105000,1e-3),cap.annual[1].rec);
 //   annual[2] (months 24-35) = base x 1.05^2 = 9,187.50/mo x 12 = 110,250
 ok('C2b cap yr-3 recovery = base x 1.05^2 x 12 (110,250)',near(cap.annual[2].rec,110250,1e-3),cap.annual[2].rec);
 ok('C3 cap reduces total recoveries vs uncapped',
    cap.annual.reduce((s,x)=>s+x.rec,0)<unc.annual.reduce((s,x)=>s+x.rec,0),'');}
{const noncum=computeDeal(capBase({grossUpOn:false,capPct:0.05,capCumulative:false}));
 ok('C4 non-cumulative cap also reduces recoveries (yr-1 <= base growth)',noncum.annual[0].rec<=100000+1e-6,noncum.annual[0].rec);}

console.log('--- Capital reserves (below NOI) ---');
function resBase(res){return base({analysis:{holdMonths:120,discountRate:0.075,creditLoss:0,inflation:0},
  acquisition:{price:3000000,closingPct:0},
  rentRoll:[{id:'L1',suiteId:'S1',sf:10000,startMonth:0,termMonths:240,baseRent:2.0,
    escalation:{type:'fixedPct',value:0},freeMonths:0,recMethod:'none',recParam:0,mlaId:'M1',uponExpiry:'renew'}],
  debt:{type:'ltv',ltv:0.6,amount:0,rate:0.06,ioMonths:24,amortMonths:360},reserves:res});}
{const noR=computeDeal(resBase({amount:0,basis:'psf',growth:0}));
 ok('R0 no reserve -> reserveTotal 0',noR.reserveTotal===0,noR.reserveTotal);
 // $1/sf/yr x 10,000 sf = $10,000/yr, growth 0, over 120 months = $100,000
 const wR=computeDeal(resBase({amount:1,basis:'psf',growth:0}));
 ok('R1 reserveTotal = $1/sf x 10,000 sf x 120/12 yrs = 100,000',near(wR.reserveTotal,100000,1e-3),wR.reserveTotal);
 ok('R2 yr-1 reserve = $10,000',near(wR.annual[0].reserve,10000,1e-6),wR.annual[0].reserve);
 ok('R3 reserve does NOT change NOI',near(wR.annual[0].noi,noR.annual[0].noi,1e-6),wR.annual[0].noi);
 ok('R3 reserve does NOT change exit value',near(wR.value,noR.value,1e-6),wR.value);
 ok('R3 reserve does NOT change yr-1 DSCR',near(wR.dcr1,noR.dcr1,1e-9),wR.dcr1);
 ok('R4 reserve lowers levered IRR (below-NOI capital cost)',wR.irrL<noR.irrL,(wR.irrL*100).toFixed(3)+' vs '+(noR.irrL*100).toFixed(3));
 ok('R4 reserve lowers unlevered IRR',wR.irrU<noR.irrU,'');}

console.log('--- Tornado sensitivity ---');
{const model=base({acquisition:{price:3000000,closingPct:0},
   debt:{type:'ltv',ltv:0.6,amount:0,rate:0.06,ioMonths:24,amortMonths:360},
   mlas:[{id:'M1',name:'mkt',marketRent:2.0,rentGrowth:0.03,termMonths:60,renewalProb:0.7,downtimeMonths:6,
     freeNew:2,freeRenew:0,tiNew:5,tiRenew:2,lcNew:0.05,lcRenew:0.025,escalation:{type:'fixedPct',value:0.03},recMethod:'none',recParam:0}],
   rentRoll:[{id:'L1',suiteId:'S1',sf:10000,startMonth:0,termMonths:48,baseRent:2.0,
     escalation:{type:'fixedPct',value:0.03},freeMonths:0,recMethod:'none',recParam:0,mlaId:'M1',uponExpiry:'market'}]});
 const priceBefore=model.acquisition.price;
 const t=E_tornado(model);
 ok('TOR1 base = computeDeal levered IRR',near(t.base,computeDeal(model).irrL,1e-12),t.base);
 ok('TOR2 seven drivers returned',t.drivers.length===7,t.drivers.length);
 ok('TOR2 each driver has low/high/name',t.drivers.every(d=>d.name&&('low'in d)&&('high'in d)),'');
 const sw=d=>(d.low==null||d.high==null)?-1:Math.abs(d.high-d.low);
 let sorted=true;for(let i=1;i<t.drivers.length;i++)if(sw(t.drivers[i])>sw(t.drivers[i-1])+1e-12)sorted=false;
 ok('TOR3 drivers sorted by descending IRR swing',sorted,'');
 const price=t.drivers.find(d=>d.name==='Purchase price');
 ok('TOR4 cheaper price (low shock) gives higher IRR than dearer (high shock)',price.low>price.high,price.low+' vs '+price.high);
 ok('TOR5 input model not mutated',model.acquisition.price===priceBefore,model.acquisition.price);}

console.log('--- Goal seek ---');
{const model=base({acquisition:{price:3000000,closingPct:0},debt:{type:'ltv',ltv:0.6,amount:0,rate:0.06,ioMonths:24,amortMonths:360}});
 const d0=computeDeal(model);
 // solve price to hit the current levered IRR -> should recover ~the current price
 const g=E_goalSeek(model,{variable:'price',metric:'irrL',target:d0.irrL});
 ok('G1 goal-seek price succeeds',g.ok===true,JSON.stringify(g));
 ok('G1 achieved IRR == target',near(g.achieved,d0.irrL,1e-4),g.achieved+' vs '+d0.irrL);
 ok('G1 solved price ~ current price',near(g.value,model.acquisition.price,model.acquisition.price*0.02),g.value);
 // solve exit cap to hit a target equity multiple
 const tgtEM=d0.emL*1.05;
 const g2=E_goalSeek(model,{variable:'exitCap',metric:'emL',target:tgtEM});
 ok('G2 goal-seek exit cap for EM succeeds',g2.ok===true,JSON.stringify(g2));
 ok('G2 achieved EM == target',near(g2.achieved,tgtEM,1e-3),g2.achieved+' vs '+tgtEM);
 ok('G2 higher target EM needs tighter (lower) exit cap',g2.value<model.exit.exitCap,g2.value+' vs '+model.exit.exitCap);
 // unreachable target -> ok:false
 const g3=E_goalSeek(model,{variable:'exitCap',metric:'irrL',target:5.0});
 ok('G3 unreachable target returns ok:false',g3.ok===false,JSON.stringify(g3));
 // solve a uniform rent factor for a higher IRR
 const g4=E_goalSeek(model,{variable:'rent',metric:'irrL',target:d0.irrL+0.03});
 ok('G4 rent goal-seek for higher IRR needs factor > 1',g4.ok&&g4.value>1,JSON.stringify(g4));}

console.log('\n'+pass+' passed, '+fail+' failed.');process.exit(fail?1:0);
