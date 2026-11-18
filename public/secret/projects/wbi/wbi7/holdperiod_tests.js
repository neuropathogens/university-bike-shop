/* WBI7 — analytic tests for hold-period analysis (E_holdAnalysis): IRR/EM by exit
   year. Checks consistency with computeDeal at the model's own hold, year coverage,
   the optimal-hold pick, input immutability, and degenerate handling. */
const fs=require('fs'),vm=require('vm');
const html=fs.readFileSync(__dirname+'/index.html','utf8');
const a=html.indexOf('/* ===================== WBI7 ENGINE START');
const b=html.indexOf('WBI7 ENGINE END ===================== */');
const ctx={console};vm.createContext(ctx);
vm.runInContext(html.slice(a,b+'WBI7 ENGINE END ===================== */'.length),ctx);
const {computeDeal,E_holdAnalysis}=ctx;
let pass=0,fail=0;
const ok=(n,c,x)=>{c?pass++:fail++;console.log((c?'  PASS  ':'  FAIL  ')+n+(c?'':'  -> '+x));};
const near=(a,b,t)=>Math.abs(a-b)<=t;

// a healthy multi-tenant deal with debt + rollover so IRR varies by exit year
function mk(over){return Object.assign({version:'wbi7-1',
  analysis:{holdMonths:84,discountRate:0.071,creditLoss:0.01,inflation:0},
  acquisition:{price:19600000,closingPct:0.015},capex:[],
  property:{suites:[{id:'S1',name:'U1',sf:30000},{id:'S2',name:'U2',sf:24000},{id:'S3',name:'U3',sf:20000},{id:'S4',name:'U4',sf:14000}]},
  mlas:[{id:'M1',name:'flex',marketRent:1.32,rentGrowth:0.03,termMonths:60,renewalProb:0.68,downtimeMonths:6,
    freeNew:2,freeRenew:1,tiNew:4,tiRenew:1.5,lcNew:0.05,lcRenew:0.025,escalation:{type:'fixedPct',value:0.03},recMethod:'net',recParam:100}],
  rentRoll:[{id:'L1',tenant:'A',suiteId:'S1',sf:30000,startMonth:-20,termMonths:60,baseRent:1.2,escalation:{type:'fixedPct',value:0.03},freeMonths:0,recMethod:'net',recParam:100,mlaId:'M1',uponExpiry:'market'},
    {id:'L2',tenant:'B',suiteId:'S2',sf:24000,startMonth:-8,termMonths:60,baseRent:1.28,escalation:{type:'fixedPct',value:0.03},freeMonths:0,recMethod:'net',recParam:100,mlaId:'M1',uponExpiry:'market'},
    {id:'L3',tenant:'C',suiteId:'S3',sf:20000,startMonth:-30,termMonths:48,baseRent:1.15,escalation:{type:'fixedPct',value:0.03},freeMonths:0,recMethod:'net',recParam:100,mlaId:'M1',uponExpiry:'market'},
    {id:'L4',tenant:'D',suiteId:'S4',sf:14000,startMonth:-3,termMonths:36,baseRent:1.34,escalation:{type:'fixedPct',value:0.03},freeMonths:0,recMethod:'net',recParam:100,mlaId:'M1',uponExpiry:'market'}],
  absorption:[],expenses:[{name:'CAM',basis:'psf',amount:1.35,growth:0.03,recoverable:true,varOcc:true},
    {name:'Tax',basis:'fixed',amount:225400,growth:0.02,recoverable:true,varOcc:false}],
  recoverySettings:{grossUpOn:false,grossUpPct:0.95,adminFee:0},otherIncome:{amount:0,growth:0},
  debt:{type:'ltv',ltv:0.6,amount:0,rate:0.064,ioMonths:12,amortMonths:360},
  exit:{exitCap:0.06,sellCostPct:0.02},equity:{lpShare:0.9,pref:0.08,promote:0.2}},over);}

console.log('--- Hold-period analysis ---');

const P=mk({});                              // 84-month hold
const baseY=Math.ceil(P.analysis.holdMonths/12);

// 1) coverage: one row per year, 1..planned hold
{const h=E_holdAnalysis(P);
 ok('H1 one row per year up to the planned hold',h.rows.length===baseY,h.rows.length+' vs '+baseY);
 ok('H1 years are 1..N in order',h.rows.every((r,i)=>r.year===i+1),JSON.stringify(h.rows.map(r=>r.year)));}

// 2) consistency: the row at the planned hold reproduces computeDeal exactly
{const h=E_holdAnalysis(P);const d=computeDeal(P);
 const row=h.rows.find(r=>r.year===baseY);
 ok('H2 IRR at planned-hold year == computeDeal IRR',near(row.irrL,d.irrL,1e-9),row.irrL+' vs '+d.irrL);
 ok('H2 EM at planned-hold year == computeDeal EM',near(row.emL,d.emL,1e-9),row.emL+' vs '+d.emL);
 ok('H2 exit value at planned-hold year == computeDeal value',near(row.value,d.value,1e-3),row.value+' vs '+d.value);}

// 3) a different hold reproduces computeDeal at that hold (spot check year 3)
{const h=E_holdAnalysis(P);const m=JSON.parse(JSON.stringify(P));m.analysis.holdMonths=36;
 const d3=computeDeal(m);const row3=h.rows.find(r=>r.year===3);
 ok('H3 year-3 IRR matches a 36-month computeDeal run',near(row3.irrL,d3.irrL,1e-9),row3.irrL+' vs '+d3.irrL);}

// 4) optimal hold is a real year and truly maximizes IRR over the set
{const h=E_holdAnalysis(P);
 const valid=h.rows.filter(r=>r.irrL!=null);
 const mx=Math.max.apply(null,valid.map(r=>r.irrL));
 ok('H4 bestYear is one of the analyzed years',h.rows.some(r=>r.year===h.bestYear),String(h.bestYear));
 ok('H4 bestIrr equals the max IRR across years',near(h.bestIrr,mx,1e-12),h.bestIrr+' vs '+mx);
 ok('H4 no analyzed year beats bestIrr',valid.every(r=>r.irrL<=h.bestIrr+1e-12),'');}

// 5) immutability: the input model is not mutated
{const before=JSON.parse(JSON.stringify(P));E_holdAnalysis(P);
 ok('H5 input model holdMonths unchanged',P.analysis.holdMonths===before.analysis.holdMonths,P.analysis.holdMonths);
 ok('H5 input model deep-equals its pre-call snapshot',JSON.stringify(P)===JSON.stringify(before),'mutated');}

// 6) values are finite/derivable for a healthy deal
{const h=E_holdAnalysis(mk({acquisition:{price:17900000,closingPct:0.02}}));
 ok('H6 every year has a finite exit value',h.rows.every(r=>isFinite(r.value)),'');
 ok('H6 most years produce a real IRR for a stabilized deal',
    h.rows.filter(r=>r.irrL!=null).length>=h.rows.length-1,'');}

// 7) degenerate model -> graceful (rows present, IRRs may be null, bestYear may be null)
{const blank={version:"wbi7-1",analysis:{holdMonths:60,discountRate:0.075,creditLoss:0},
   acquisition:{price:0,closingPct:0},capex:[],property:{suites:[]},mlas:[],rentRoll:[],
   absorption:[],expenses:[],recoverySettings:{grossUpOn:false,grossUpPct:0.95,adminFee:0},
   otherIncome:{amount:0,growth:0},debt:{type:'ltv',ltv:0,amount:0,rate:0,ioMonths:0,amortMonths:360},
   exit:{exitCap:0.06,sellCostPct:0},equity:{lpShare:1,pref:0,promote:0}};
 let h;try{h=E_holdAnalysis(blank);}catch(e){h=null;}
 ok('H7 degenerate model does not throw',!!h,'threw');
 ok('H7 degenerate model: 5 yearly rows (60-mo hold)',h&&h.rows.length===5,h?h.rows.length:0);
 ok('H7 degenerate model: IRRs null, bestYear null',h&&h.rows.every(r=>r.irrL===null)&&h.bestYear===null,'');}

console.log('\n'+pass+' passed, '+fail+' failed.');
process.exit(fail?1:0);
