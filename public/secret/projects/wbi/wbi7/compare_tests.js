/* WBI7 — analytic tests for scenario compare (E_compare): a side-by-side metric
   stack. Checks reconciliation to computeDeal, column order, that a cheaper-basis
   variant reads through correctly, input immutability, and edge/degenerate cases. */
const fs=require('fs'),vm=require('vm');
const html=fs.readFileSync(__dirname+'/index.html','utf8');
const a=html.indexOf('/* ===================== WBI7 ENGINE START');
const b=html.indexOf('WBI7 ENGINE END ===================== */');
const ctx={console};vm.createContext(ctx);
vm.runInContext(html.slice(a,b+'WBI7 ENGINE END ===================== */'.length),ctx);
const {computeDeal,E_compare}=ctx;
let pass=0,fail=0;
const ok=(n,c,x)=>{c?pass++:fail++;console.log((c?'  PASS  ':'  FAIL  ')+n+(c?'':'  -> '+x));};
const near=(a,b,t)=>Math.abs(a-b)<=t;

function mk(over){return Object.assign({version:'wbi7-1',
  analysis:{holdMonths:84,discountRate:0.071,creditLoss:0.01,inflation:0},
  acquisition:{price:19600000,closingPct:0.015},capex:[],
  property:{suites:[{id:'S1',name:'U1',sf:50000}]},
  mlas:[{id:'M1',name:'flex',marketRent:1.32,rentGrowth:0.03,termMonths:60,renewalProb:0.7,downtimeMonths:6,
    freeNew:1,freeRenew:0,tiNew:3,tiRenew:1,lcNew:0.05,lcRenew:0.025,escalation:{type:'fixedPct',value:0.03},recMethod:'net',recParam:100}],
  rentRoll:[{id:'L1',tenant:'A',suiteId:'S1',sf:50000,startMonth:-12,termMonths:84,baseRent:1.25,escalation:{type:'fixedPct',value:0.03},freeMonths:0,recMethod:'net',recParam:100,mlaId:'M1',uponExpiry:'market'}],
  absorption:[],expenses:[{name:'CAM',basis:'psf',amount:1.35,growth:0.03,recoverable:true,varOcc:true},
    {name:'Tax',basis:'fixed',amount:225400,growth:0.02,recoverable:true,varOcc:false}],
  recoverySettings:{grossUpOn:false,grossUpPct:0.95,adminFee:0},otherIncome:{amount:0,growth:0},
  debt:{type:'ltv',ltv:0.6,amount:0,rate:0.064,ioMonths:12,amortMonths:360},
  exit:{exitCap:0.06,sellCostPct:0.02},equity:{lpShare:0.9,pref:0.08,promote:0.2}},over);}

console.log('--- Scenario compare ---');

// 1) reconciliation: each compared metric equals computeDeal's for that scenario
{const base=mk({});const c=E_compare([{name:'Base',model:base}]);const d=computeDeal(base);
 ok('C1 one column returned',c.length===1&&c[0].name==='Base'&&c[0].ok,'');
 const m=c[0].m;
 ok('C1 value matches computeDeal',near(m.value,d.value,1e-3),m.value+' vs '+d.value);
 ok('C1 levered IRR matches computeDeal',near(m.irrL,d.irrL,1e-12),m.irrL+' vs '+d.irrL);
 ok('C1 equity multiple matches computeDeal',near(m.emL,d.emL,1e-12),m.emL+' vs '+d.emL);
 ok('C1 DSCR matches computeDeal',(m.dcr1===d.dcr1)||near(m.dcr1,d.dcr1,1e-9),m.dcr1+' vs '+d.dcr1);
 ok('C1 going-in yield matches computeDeal',near(m.goin,d.goin,1e-12),m.goin+' vs '+d.goin);
 ok('C1 equity matches computeDeal equity0',near(m.equity,d.equity0,1e-3),m.equity+' vs '+d.equity0);
 ok('C1 price reads from the model',m.price===base.acquisition.price,m.price);}

// 2) order preserved across multiple scenarios
{const c=E_compare([{name:'A',model:mk({})},{name:'B',model:mk({})},{name:'C',model:mk({})}]);
 ok('C2 three columns in order A,B,C',c.length===3&&c[0].name==='A'&&c[2].name==='C',c.map(x=>x.name).join(','));}

// 3) sensitivity reads through: a cheaper basis lifts IRR and yield-in vs base
{const base=mk({});const cheap=mk({acquisition:{price:16000000,closingPct:0.015}});
 const c=E_compare([{name:'Base',model:base},{name:'Cheaper',model:cheap}]);
 ok('C3 cheaper basis has higher going-in yield',c[1].m.goin>c[0].m.goin,c[1].m.goin+' vs '+c[0].m.goin);
 ok('C3 cheaper basis has higher levered IRR',c[1].m.irrL>c[0].m.irrL,c[1].m.irrL+' vs '+c[0].m.irrL);
 ok('C3 cheaper basis needs less equity',c[1].m.equity<c[0].m.equity,c[1].m.equity+' vs '+c[0].m.equity);}

// 4) immutability
{const base=mk({});const snap=JSON.stringify(base);E_compare([{name:'x',model:base}]);
 ok('C4 input model not mutated',JSON.stringify(base)===snap,'mutated');}

// 5) empty input -> empty array
{ok('C5 empty list -> []',E_compare([]).length===0,'');
 ok('C5 null-ish entries filtered out',E_compare([null,{},{name:'ok',model:mk({})}]).length===1,'');}

// 6) degenerate model -> ok:false, m null, no throw
{const blank={version:"wbi7-1",analysis:{holdMonths:60,discountRate:0.075,creditLoss:0},
   acquisition:{price:0,closingPct:0},capex:[],property:{suites:[]},mlas:[],rentRoll:[],
   absorption:[],expenses:[],recoverySettings:{grossUpOn:false,grossUpPct:0.95,adminFee:0},
   otherIncome:{amount:0,growth:0},debt:{type:'ltv',ltv:0,amount:0,rate:0,ioMonths:0,amortMonths:360},
   exit:{exitCap:0.06,sellCostPct:0},equity:{lpShare:1,pref:0,promote:0}};
 let c;try{c=E_compare([{name:'blank',model:blank}]);}catch(e){c=null;}
 ok('C6 degenerate model does not throw',!!c,'threw');
 // computeDeal succeeds on a blank model (returns zeros), so ok:true with a null IRR
 ok('C6 degenerate column present with null IRR',c&&c[0]&&c[0].m&&c[0].m.irrL===null,JSON.stringify(c&&c[0]&&c[0].m&&c[0].m.irrL));}

console.log('\n'+pass+' passed, '+fail+' failed.');
process.exit(fail?1:0);
