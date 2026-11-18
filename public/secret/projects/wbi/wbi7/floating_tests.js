/* WBI7 — analytic tests for floating-rate (ARM) senior debt. The fixed path is
   already proven byte-identical by the golden suite; these check the floating
   behavior itself: off == fixed, the rate steps at the reset interval, the cap and
   floor bind, and a rising vs falling path moves returns the right way. Uses a
   full-term interest-only loan so debt service reads the rate path directly. */
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

// price 15,000,000 @ 60% LTV = 9,000,000 senior; full-term IO @ 6% so annual debt
// service reads the rate directly (year-0 ds = 9.0M*0.06 = 540,000)
function mk(over){const m=Object.assign({version:'wbi7-1',
  analysis:{holdMonths:84,discountRate:0.071,creditLoss:0,inflation:0},
  acquisition:{price:15000000,closingPct:0},capex:[],
  property:{suites:[{id:'S1',name:'U1',sf:100000}]},
  mlas:[{id:'M1',name:'flex',marketRent:1.2,rentGrowth:0.03,termMonths:120,renewalProb:1,downtimeMonths:0,
    freeNew:0,freeRenew:0,tiNew:0,tiRenew:0,lcNew:0,lcRenew:0,escalation:{type:'fixedPct',value:0.03},recMethod:'none',recParam:0}],
  rentRoll:[{id:'L1',tenant:'A',suiteId:'S1',sf:100000,startMonth:0,termMonths:120,baseRent:1.2,escalation:{type:'fixedPct',value:0.03},freeMonths:0,recMethod:'none',recParam:0,mlaId:'M1',uponExpiry:'renew'}],
  absorption:[],expenses:[{name:'CAM',basis:'psf',amount:1.0,growth:0.03,recoverable:false,varOcc:false}],
  recoverySettings:{grossUpOn:false,grossUpPct:0.95,adminFee:0},otherIncome:{amount:0,growth:0},
  debt:{type:'ltv',ltv:0.6,amount:0,rate:0.06,ioMonths:240,amortMonths:360},
  exit:{exitCap:0.06,sellCostPct:0.02},equity:{lpShare:1,pref:0,promote:0}},over);return m;}

console.log('--- Floating-rate (ARM) debt ---');

// 1) off == fixed: floating.on=false reproduces the no-floating deal exactly
{const base=mk({});const off=mk({});off.debt.floating={on:false,resetMonths:12,stepBps:200,capRate:0.12,floorRate:0};
 const d0=computeDeal(base),d1=computeDeal(off);
 ok('F1 floating off == fixed: IRR identical',near(d0.irrL,d1.irrL,1e-12),d0.irrL+' vs '+d1.irrL);
 ok('F1 floating off == fixed: year-1 DSCR identical',(d0.dcr1===d1.dcr1)||near(d0.dcr1,d1.dcr1,1e-12),d0.dcr1+' vs '+d1.dcr1);
 ok('F1 floating off == fixed: year-1 debt service identical',near(d0.annual[0].ds,d1.annual[0].ds,1e-9),'');}

// 2) IO sanity: year-0 debt service == loan * rate
{const d=computeDeal(mk({}));
 ok('F2 IO year-0 debt service == 9.0M * 6%',near(d.annual[0].ds,9000000*0.06,1),d.annual[0].ds);}

// 3) the rate steps at the reset interval: +100bps/yr -> year-1 ds / year-0 ds == 7%/6%
{const m=mk({});m.debt.floating={on:true,resetMonths:12,stepBps:100,capRate:0.20,floorRate:0};
 const d=computeDeal(m);
 ok('F3 year-1 ds reflects a +100bps step',near(d.annual[1].ds/d.annual[0].ds,0.07/0.06,1e-6),d.annual[1].ds/d.annual[0].ds+' vs '+(0.07/0.06));
 ok('F3 year-2 ds reflects +200bps cumulative',near(d.annual[2].ds/d.annual[0].ds,0.08/0.06,1e-6),d.annual[2].ds/d.annual[0].ds);}

// 4) the cap binds: cap == start rate -> rate can never rise -> identical to fixed
{const base=mk({});const capped=mk({});capped.debt.floating={on:true,resetMonths:12,stepBps:300,capRate:0.06,floorRate:0};
 const d0=computeDeal(base),dc=computeDeal(capped);
 ok('F4 cap at the start rate fully binds: IRR == fixed',near(d0.irrL,dc.irrL,1e-12),d0.irrL+' vs '+dc.irrL);
 ok('F4 cap at the start rate: later-year ds flat (no rise)',near(dc.annual[3].ds,dc.annual[0].ds,1e-6),dc.annual[3].ds+' vs '+dc.annual[0].ds);}

// 5) the floor binds: falling path with floor == start rate -> rate can never fall -> fixed
{const base=mk({});const floored=mk({});floored.debt.floating={on:true,resetMonths:12,stepBps:-300,capRate:0.20,floorRate:0.06};
 const d0=computeDeal(base),df=computeDeal(floored);
 ok('F5 floor at the start rate fully binds: IRR == fixed',near(d0.irrL,df.irrL,1e-12),d0.irrL+' vs '+df.irrL);}

// 6) direction: a rising rate path lowers levered IRR; a falling path lifts it
{const base=computeDeal(mk({}));
 const rise=mk({});rise.debt.floating={on:true,resetMonths:12,stepBps:150,capRate:0.20,floorRate:0};
 const fall=mk({});fall.debt.floating={on:true,resetMonths:12,stepBps:-100,capRate:0.20,floorRate:0.01};
 const dr=computeDeal(rise),dfl=computeDeal(fall);
 ok('F6 rising rates lower the levered IRR vs fixed',dr.irrL<base.irrL,dr.irrL+' vs '+base.irrL);
 ok('F6 falling rates lift the levered IRR vs fixed',dfl.irrL>base.irrL,dfl.irrL+' vs '+base.irrL);
 ok('F6 rising rates raise total debt service over the hold',
    dr.annual.reduce((s,a)=>s+a.ds,0) > base.annual.reduce((s,a)=>s+a.ds,0),'');}

// 7) reset interval matters: a 24-month reset rises slower than a 12-month reset
{const r12=mk({});r12.debt.floating={on:true,resetMonths:12,stepBps:100,capRate:0.20,floorRate:0};
 const r24=mk({});r24.debt.floating={on:true,resetMonths:24,stepBps:100,capRate:0.20,floorRate:0};
 const d12=computeDeal(r12),d24=computeDeal(r24);
 ok('F7 slower resets => less total debt service',
    d24.annual.reduce((s,a)=>s+a.ds,0) < d12.annual.reduce((s,a)=>s+a.ds,0),'');
 ok('F7 24-mo reset: year-1 ds still at the start rate',near(d24.annual[1].ds,d24.annual[0].ds,1e-6),d24.annual[1].ds+' vs '+d24.annual[0].ds);}

// 8) amortizing floating loan still fully services and amortizes (no blow-up)
{const m=mk({});m.debt.ioMonths=0;m.debt.amortMonths=360;
 m.debt.floating={on:true,resetMonths:12,stepBps:100,capRate:0.20,floorRate:0};
 const d=computeDeal(m);
 ok('F8 amortizing floating loan: finite IRR',d.irrL!=null&&isFinite(d.irrL),String(d.irrL));
 ok('F8 amortizing floating loan: balance at sale below original loan',d.balSale<9000000,d.balSale);
 ok('F8 amortizing floating loan: debt service rises after first reset',d.annual[2].ds>d.annual[0].ds,d.annual[2].ds+' vs '+d.annual[0].ds);}

console.log('\n'+pass+' passed, '+fail+' failed.');
process.exit(fail?1:0);
