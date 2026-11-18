/* WBI7 — tests for the monthly cash-flow ledger (E_monthlyRows). The central guarantee
   is reconciliation: the per-month rows for any hold year must sum exactly to that year's
   row in the annual table, component by component (base rent, credit loss, recoveries,
   percentage rent, other income, EGI, opex, NOI, reserves, capital, debt service). This
   is what makes a surprising annual number defensible — you can trace it to the month.
   Also checks the operating-cash-flow and EGI definitions per row, row counts for full and
   partial years, occupancy bounds, and that out-of-range years return nothing. */
const fs=require('fs'),vm=require('vm');
const html=fs.readFileSync(__dirname+'/index.html','utf8');
const a=html.indexOf('/* ===================== WBI7 ENGINE START');
const b=html.indexOf('WBI7 ENGINE END ===================== */');
const ctx={console};vm.createContext(ctx);
vm.runInContext(html.slice(a,b+'WBI7 ENGINE END ===================== */'.length),ctx);
const {computeDeal,E_monthlyRows}=ctx;
let pass=0,fail=0;
const ok=(n,c,x)=>{c?pass++:fail++;console.log((c?'  PASS  ':'  FAIL  ')+n+(c?'':'  -> '+x));};
const near=(a,b,e)=>Math.abs(a-b)<=(e==null?0.5:e);

function mkDeal(over){const m=Object.assign({version:'wbi7-1',
  analysis:{holdMonths:66,discountRate:0.08,creditLoss:0.04,inflation:0.025},
  acquisition:{price:14000000,closingPct:0.02},
  capex:[{month:4,amount:250000,label:'roof'}],
  property:{suites:[{id:'S1',name:'U1',sf:90000}]},
  mlas:[{id:'M1',name:'flex',marketRent:1.30,rentGrowth:0.03,termMonths:60,renewalProb:0.7,downtimeMonths:6,
    freeNew:2,freeRenew:0,tiNew:3,tiRenew:1,lcNew:0.05,lcRenew:0.025,escalation:{type:'fixedPct',value:0.03},recMethod:'net',recParam:100}],
  rentRoll:[{id:'L1',tenant:'A',suiteId:'S1',sf:60000,startMonth:-6,termMonths:48,baseRent:1.25,escalation:{type:'fixedPct',value:0.03},freeMonths:0,recMethod:'net',recParam:100,mlaId:'M1',uponExpiry:'market'},
            {id:'L2',tenant:'B',suiteId:'S1',sf:30000,startMonth:0,termMonths:36,baseRent:1.20,escalation:{type:'fixedPct',value:0.03},freeMonths:2,recMethod:'net',recParam:100,mlaId:'M1',uponExpiry:'market'}],
  absorption:[],
  expenses:[{name:'CAM',basis:'psf',amount:1.4,growth:0.03,recoverable:true,varOcc:true},
    {name:'Tax',basis:'fixed',amount:160000,growth:0.02,recoverable:true,varOcc:false}],
  recoverySettings:{grossUpOn:false,grossUpPct:0.95,adminFee:0},
  otherIncome:{amount:2000,growth:0.03},
  reserves:{psf:0.25,growth:0.03},
  debt:{type:'ltv',ltv:0.6,amount:0,rate:0.055,ioMonths:12,amortMonths:360,mezz:{amount:0,rate:0}},
  exit:{exitCap:0.072,sellCostPct:0.02},equity:{lpShare:1,pref:0,promote:0}},over);return m;}

console.log('--- Monthly cash-flow ledger ---');

const M=mkDeal(),d=computeDeal(M);
ok('result carries the monthly arrays needed for the ledger',!!d.monthly&&Array.isArray(d.monthly.clAmt)&&Array.isArray(d.monthly.oth),'');

// --- reconciliation: monthly sums == annual, every component, every year ---
const comps=[['rent','rent'],['cl','cl'],['rec','rec'],['pct','pct'],['oth','oth'],['exp','exp'],['noi','noi'],['cap','cap'],['reserve','reserve'],['ds','ds'],['egi','egi']];
let reconAll=true,firstMiss='';
(d.annual||[]).forEach(an=>{
  const rows=E_monthlyRows(d,an.y);
  const sum=f=>rows.reduce((s,r)=>s+r[f],0);
  comps.forEach(([rf,af])=>{ if(!near(sum(rf),an[af])){ reconAll=false; if(!firstMiss)firstMiss='Y'+an.y+' '+rf+': '+sum(rf).toFixed(2)+' vs '+an[af].toFixed(2); } });
});
ok('every component of every year ties out to the annual table',reconAll,firstMiss);

// spot-check a couple of components in isolation so a single broad pass can't hide a sign error
{const r1=E_monthlyRows(d,1);
 ok('year-1 base rent reconciles',near(r1.reduce((s,r)=>s+r.rent,0),d.annual[0].rent),'');
 ok('year-1 NOI reconciles',near(r1.reduce((s,r)=>s+r.noi,0),d.annual[0].noi),'');
 ok('year-1 debt service reconciles',near(r1.reduce((s,r)=>s+r.ds,0),d.annual[0].ds),'');
 ok('year-1 reserves reconcile',near(r1.reduce((s,r)=>s+r.reserve,0),d.annual[0].reserve),'');}

// --- per-row definitions ---
{const r=E_monthlyRows(d,2);
 ok('EGI per row = rent - credit loss + recoveries + % rent + other',r.every(x=>near(x.egi,x.rent-x.cl+x.rec+x.pct+x.oth,1e-6)),'');
 ok('operating cash flow per row = NOI - capital - reserves - debt service',r.every(x=>near(x.ocf,x.noi-x.cap-x.reserve-x.ds,1e-6)),'');
 ok('the capital month carries a non-zero capital figure somewhere in the hold',
    [1,2,3,4,5,6].some(y=>E_monthlyRows(d,y).some(x=>x.cap>0)),'no capital row found');}

// --- row counts ---
ok('a full hold year returns 12 monthly rows',E_monthlyRows(d,1).length===12,String(E_monthlyRows(d,1).length));
{const Y=d.Y,lastCount=E_monthlyRows(d,Y).length,expect=d.M-(Y-1)*12;
 ok('the final (partial) year returns the right number of rows',lastCount===expect,lastCount+' vs '+expect);}

// --- occupancy bounds ---
ok('occupancy on every row is within [0, 1]',E_monthlyRows(d,1).every(r=>r.occ>=0&&r.occ<=1.0001),'');

// --- out of range ---
ok('year 0 returns no rows',E_monthlyRows(d,0).length===0,'');
ok('a year beyond the hold returns no rows',E_monthlyRows(d,d.Y+3).length===0,'');
ok('a missing result returns no rows',E_monthlyRows(null,1).length===0,'');

console.log('\n'+pass+' passed, '+fail+' failed.');
process.exit(fail?1:0);
