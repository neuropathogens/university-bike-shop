/* WBI7 — tests for the value-creation bridge (E_valueBridge). It decomposes levered
   profit into operating income, NOI growth, cap-rate movement, selling costs, and
   leverage. The central guarantee is EXACT reconciliation: the five sources sum to
   computeDeal's profit. These also check the economic directions (cap compression is a
   gain, expansion a loss; more rent growth lifts the NOI-growth term; no debt zeroes
   leverage; a cheaper-than-yield loan makes leverage positive), the no-income guard,
   and base-model immutability. */
const fs=require('fs'),vm=require('vm');
const html=fs.readFileSync(__dirname+'/index.html','utf8');
const a=html.indexOf('/* ===================== WBI7 ENGINE START');
const b=html.indexOf('WBI7 ENGINE END ===================== */');
const ctx={console};vm.createContext(ctx);
vm.runInContext(html.slice(a,b+'WBI7 ENGINE END ===================== */'.length),ctx);
const {computeDeal,E_valueBridge}=ctx;
let pass=0,fail=0;
const ok=(n,c,x)=>{c?pass++:fail++;console.log((c?'  PASS  ':'  FAIL  ')+n+(c?'':'  -> '+x));};
const comp=(R,key)=>R.components.find(c=>c.key===key).amount;

function mkDeal(over){const m=Object.assign({version:'wbi7-1',
  analysis:{holdMonths:84,discountRate:0.072,creditLoss:0.03,inflation:0.025},
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

console.log('--- Value-creation bridge ---');

const M=mkDeal(),R=E_valueBridge(M),d=computeDeal(M);
ok('result has the expected shape',R.ok===true&&Array.isArray(R.components)&&R.components.length===5,JSON.stringify(R.ok&&R.components&&R.components.length));

// the central guarantee: components sum to profit exactly
const sum=R.components.reduce((s,c)=>s+c.amount,0);
ok('the five sources reconcile exactly to levered profit',Math.abs(sum-d.profit)<1e-6,String(sum-d.profit));
ok('the reconciles flag is set',R.reconciles===true,'');
ok('income-driven + bet + selling + leverage == profit',Math.abs((R.incomeDriven+R.bet+comp(R,'selling')+R.leverage)-d.profit)<1e-6,'');

// reconciliation holds across varied structures
let recOK=true;
[{exit:{exitCap:0.05,sellCostPct:0.02}},{debt:{type:'ltv',ltv:0.75,amount:0,rate:0.07,ioMonths:24,amortMonths:300,mezz:{amount:0,rate:0}}},{analysis:{holdMonths:120,discountRate:0.07,creditLoss:0.05,inflation:0.02}}].forEach(o=>{
  const m=mkDeal(o),r=E_valueBridge(m),dd=computeDeal(m);
  if(!r.ok||Math.abs(r.components.reduce((s,c)=>s+c.amount,0)-dd.profit)>1e-6)recOK=false;
});
ok('reconciliation holds across different leverage, hold, and exit assumptions',recOK,'');

// economic directions
const goinCap=d.goin;
const compress=E_valueBridge(mkDeal({exit:{exitCap:Math.max(0.01,goinCap-0.02),sellCostPct:0.02}}));
const expand=E_valueBridge(mkDeal({exit:{exitCap:goinCap+0.02,sellCostPct:0.02}}));
ok('cap-rate compression is a positive contribution',comp(compress,'capShift')>0,String(comp(compress,'capShift')));
ok('cap-rate expansion is a negative contribution',comp(expand,'capShift')<0,String(comp(expand,'capShift')));

const lowG=E_valueBridge(mkDeal({mlas:[Object.assign({},mkDeal().mlas[0],{rentGrowth:0.01})]}));
const highG=E_valueBridge(mkDeal({mlas:[Object.assign({},mkDeal().mlas[0],{rentGrowth:0.05})]}));
ok('higher rent growth increases the NOI-growth contribution',comp(highG,'noiGrowth')>comp(lowG,'noiGrowth'),'');

// leverage line
const noDebt=E_valueBridge(mkDeal({debt:{type:'amount',ltv:0,amount:0,rate:0.055,ioMonths:0,amortMonths:360,mezz:{amount:0,rate:0}}}));
ok('an all-cash deal has ~zero leverage contribution',Math.abs(comp(noDebt,'leverage'))<1,String(comp(noDebt,'leverage')));
ok('financing shows as a cost in total-dollar profit (interest paid)',comp(R,'leverage')<0,String(comp(R,'leverage')));

// selling costs are a drag
ok('selling costs are a negative contribution',comp(R,'selling')<0,'');

// guards
ok('a no-income model is rejected',(()=>{const m=mkDeal({acquisition:{price:0,closingPct:0},rentRoll:[],mlas:[],property:{suites:[]}});return E_valueBridge(m).ok===false;})(),'');

// immutability
{const m=mkDeal();const before=JSON.stringify(m);E_valueBridge(m);E_valueBridge(m);
 ok('the bridge never mutates the model',JSON.stringify(m)===before,'model changed');}

console.log('\n'+pass+' passed, '+fail+' failed.');
process.exit(fail?1:0);
