/* WBI7 — tests for break-even / margin of safety (E_breakeven). The central guarantee is
   plug-back-in correctness: feeding each break-even value back into the engine reproduces
   its threshold (DSCR = 1.0x for covenant break-evens, profit = 0 for equity break-evens,
   IRR = the hurdle for the max price). These also check cushion signs and directions, that
   coverage break-evens are omitted when there is no debt, that an overpriced deal shows a
   negative price cushion, and base-model immutability. */
const fs=require('fs'),vm=require('vm');
const html=fs.readFileSync(__dirname+'/index.html','utf8');
const a=html.indexOf('/* ===================== WBI7 ENGINE START');
const b=html.indexOf('WBI7 ENGINE END ===================== */');
const ctx={console};vm.createContext(ctx);
vm.runInContext(html.slice(a,b+'WBI7 ENGINE END ===================== */'.length),ctx);
const {computeDeal,E_breakeven}=ctx;
let pass=0,fail=0;
const ok=(n,c,x)=>{c?pass++:fail++;console.log((c?'  PASS  ':'  FAIL  ')+n+(c?'':'  -> '+x));};
const applyRent=(m,f)=>{(m.rentRoll||[]).forEach(L=>L.baseRent=(+L.baseRent||0)*f);(m.mlas||[]).forEach(X=>X.marketRent=(+X.marketRent||0)*f);};

function mkDeal(over){const m=Object.assign({version:'wbi7-1',
  analysis:{holdMonths:84,discountRate:0.08,creditLoss:0.03,inflation:0.025},
  acquisition:{price:15000000,closingPct:0.02},capex:[],
  property:{suites:[{id:'S1',name:'U1',sf:100000}]},
  mlas:[{id:'M1',name:'flex',marketRent:1.25,rentGrowth:0.03,termMonths:60,renewalProb:0.7,downtimeMonths:6,
    freeNew:1,freeRenew:0,tiNew:3,tiRenew:1,lcNew:0.05,lcRenew:0.025,escalation:{type:'fixedPct',value:0.03},recMethod:'net',recParam:100}],
  rentRoll:[{id:'L1',tenant:'A',suiteId:'S1',sf:100000,startMonth:-12,termMonths:60,baseRent:1.2,escalation:{type:'fixedPct',value:0.03},freeMonths:0,recMethod:'net',recParam:100,mlaId:'M1',uponExpiry:'market'}],
  absorption:[],expenses:[{name:'CAM',basis:'psf',amount:1.2,growth:0.03,recoverable:true,varOcc:true},
    {name:'Tax',basis:'fixed',amount:170000,growth:0.02,recoverable:true,varOcc:false}],
  recoverySettings:{grossUpOn:false,grossUpPct:0.95,adminFee:0},otherIncome:{amount:0,growth:0},
  debt:{type:'ltv',ltv:0.6,amount:0,rate:0.055,ioMonths:0,amortMonths:360,mezz:{amount:0,rate:0,ioMonths:0,amortMonths:360}},
  exit:{exitCap:0.075,sellCostPct:0.02},equity:{lpShare:1,pref:0,promote:0}},over);return m;}

console.log('--- Break-even / margin of safety ---');

const M=mkDeal(),R=E_breakeven(M);
const get=k=>R.items.find(i=>i.key===k);
ok('result has the expected shape',R.ok===true&&Array.isArray(R.items)&&R.items.length>=4,JSON.stringify(R.ok&&R.items&&R.items.length));
ok('a leveraged deal includes both covenant and equity break-evens',!!get('rentCov')&&!!get('vacCov')&&!!get('rentEq')&&!!get('capEq')&&!!get('priceHurdle'),R.items.map(i=>i.key).join(','));

// plug-back-in correctness — the core guarantee
{const rc=get('rentCov');const m=mkDeal();applyRent(m,rc.be);
 ok('rent-coverage break-even reproduces DSCR = 1.0x',Math.abs(computeDeal(m).dcr1-1.0)<1e-4,String(computeDeal(m).dcr1));}
{const re=get('rentEq');const m=mkDeal();applyRent(m,re.be);
 ok('rent-equity break-even reproduces profit = 0',Math.abs(computeDeal(m).profit)<5,String(computeDeal(m).profit));}
{const ce=get('capEq');const m=mkDeal();m.exit.exitCap=ce.be;
 ok('exit-cap break-even reproduces profit = 0',Math.abs(computeDeal(m).profit)<5,String(computeDeal(m).profit));}
{const ph=get('priceHurdle');const m=mkDeal();m.acquisition.price=ph.be;
 ok('max-price break-even reproduces IRR = hurdle',Math.abs(computeDeal(m).irrL-R.hurdle)<1e-4,String(computeDeal(m).irrL-R.hurdle));}
{const vc=get('vacCov');const m=mkDeal();m.analysis.creditLoss=vc.be;
 ok('vacancy-coverage break-even reproduces DSCR = 1.0x',Math.abs(computeDeal(m).dcr1-1.0)<1e-4,String(computeDeal(m).dcr1));}

// directions / cushions for a healthy deal
ok('a healthy deal can absorb a rent decline before covenant breach',get('rentCov').cushion>0&&get('rentCov').be<1,String(get('rentCov').be));
ok('the equity rent cushion is no larger than the covenant rent cushion',get('rentEq').cushion<=get('rentCov').cushion+1e-9,'');
ok('the exit cap can rise above base before break even',get('capEq').be>R.baseCap&&get('capEq').cushion>0,'');
ok('vacancy can rise above base before covenant breach',get('vacCov').be>R.baseCredit&&get('vacCov').cushion>0,'');

// no-debt deal: coverage break-evens omitted, equity ones remain
{const nd=mkDeal({debt:{type:'amount',ltv:0,amount:0,rate:0.055,ioMonths:0,amortMonths:360,mezz:{amount:0,rate:0}}});
 const Rnd=E_breakeven(nd);
 ok('an all-cash deal omits the DSCR-covenant break-evens',!Rnd.items.find(i=>i.key==='rentCov')&&!Rnd.items.find(i=>i.key==='vacCov'),'');
 ok('an all-cash deal keeps the equity break-evens',!!Rnd.items.find(i=>i.key==='rentEq')&&!!Rnd.items.find(i=>i.key==='capEq'),'');}

// overpriced deal: negative price cushion
{const op=mkDeal();op.acquisition.price=op.acquisition.price*1.8;
 const ph=E_breakeven(op).items.find(i=>i.key==='priceHurdle');
 ok('an overpriced deal shows a negative price cushion',ph.cushion<0,String(ph.cushion));}

// immutability
{const m=mkDeal();const before=JSON.stringify(m);E_breakeven(m);E_breakeven(m);
 ok('the analysis never mutates the model',JSON.stringify(m)===before,'model changed');}

console.log('\n'+pass+' passed, '+fail+' failed.');
process.exit(fail?1:0);
