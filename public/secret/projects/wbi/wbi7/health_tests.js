/* WBI7 — tests for the model health check (E_healthCheck). Read-only pre-flight scan;
   these check that a sane deal is clean, that each rule fires on the input that should
   trip it (missing exit cap, zero hold, negative equity from an oversized fixed loan,
   sub-1.0x DSCR, fat-fingered rate/cost ratios, aggressive cap compression and rent
   growth, mezz-below-senior, refi-after-sale), that severity counts match the item list,
   and that the scan never mutates the model. */
const fs=require('fs'),vm=require('vm');
const html=fs.readFileSync(__dirname+'/index.html','utf8');
const a=html.indexOf('/* ===================== WBI7 ENGINE START');
const b=html.indexOf('WBI7 ENGINE END ===================== */');
const ctx={console};vm.createContext(ctx);
vm.runInContext(html.slice(a,b+'WBI7 ENGINE END ===================== */'.length),ctx);
const {computeDeal,E_healthCheck}=ctx;
let pass=0,fail=0;
const ok=(n,c,x)=>{c?pass++:fail++;console.log((c?'  PASS  ':'  FAIL  ')+n+(c?'':'  -> '+x));};
const has=(R,sub)=>R.items.some(i=>i.msg.indexOf(sub)>=0);

// a clean, conservative deal: moderate leverage, sane caps and growth
function mkHealthy(over){const m=Object.assign({version:'wbi7-1',
  analysis:{holdMonths:84,discountRate:0.072,creditLoss:0.03,inflation:0.025},
  acquisition:{price:15000000,closingPct:0.02},capex:[],
  property:{suites:[{id:'S1',name:'U1',sf:100000}]},
  mlas:[{id:'M1',name:'flex',marketRent:1.25,rentGrowth:0.03,termMonths:60,renewalProb:0.7,downtimeMonths:6,
    freeNew:1,freeRenew:0,tiNew:3,tiRenew:1,lcNew:0.05,lcRenew:0.025,escalation:{type:'fixedPct',value:0.03},recMethod:'net',recParam:100}],
  rentRoll:[{id:'L1',tenant:'A',suiteId:'S1',sf:100000,startMonth:-12,termMonths:60,baseRent:1.2,escalation:{type:'fixedPct',value:0.03},freeMonths:0,recMethod:'net',recParam:100,mlaId:'M1',uponExpiry:'market'}],
  absorption:[],expenses:[{name:'CAM',basis:'psf',amount:1.2,growth:0.03,recoverable:true,varOcc:true},
    {name:'Tax',basis:'fixed',amount:170000,growth:0.02,recoverable:true,varOcc:false}],
  recoverySettings:{grossUpOn:false,grossUpPct:0.95,adminFee:0},otherIncome:{amount:0,growth:0},
  debt:{type:'ltv',ltv:0.6,amount:0,rate:0.062,ioMonths:0,amortMonths:360,mezz:{amount:0,rate:0,ioMonths:0,amortMonths:360}},
  exit:{exitCap:0.09,sellCostPct:0.02},equity:{lpShare:1,pref:0.08,promote:0.2}},over);return m;}

console.log('--- Model health check ---');

const base=E_healthCheck(mkHealthy());
ok('result has the expected shape',base.ok===true&&Array.isArray(base.items)&&typeof base.nError==='number',JSON.stringify(Object.keys(base)));
ok('a clean deal reports no hard issues',base.nError===0,JSON.stringify(base.items.map(i=>i.sev+':'+i.msg)));
ok('a clean deal reports no warnings',base.nWarn===0,JSON.stringify(base.items.map(i=>i.sev+':'+i.msg)));
const baseW=base.nWarn;

// structural errors
ok('zero exit cap is flagged as an issue',(()=>{const r=E_healthCheck(mkHealthy({exit:{exitCap:0,sellCostPct:0.02}}));return r.nError>base.nError&&has(r,'Exit cap');})(),'');
ok('zero hold period is flagged as an issue',(()=>{const m=mkHealthy();m.analysis.holdMonths=0;const r=E_healthCheck(m);return r.nError>0&&has(r,'Hold period');})(),'');
ok('a fixed loan exceeding cost is flagged (negative equity)',(()=>{const m=mkHealthy();m.debt.type='amount';m.debt.amount=30000000;const r=E_healthCheck(m);return r.nError>0&&has(r,'negative equity');})(),'');

// coverage
ok('sub-1.0x DSCR is flagged',(()=>{const m=mkHealthy();m.debt.type='amount';m.debt.amount=13000000;m.debt.rate=0.14;m.debt.amortMonths=180;const r=E_healthCheck(m);return has(r,'DSCR is below 1.0');})(),'');

// pricing / typo guards
ok('an implausible exit cap (50%) is flagged',(()=>{const r=E_healthCheck(mkHealthy({exit:{exitCap:0.5,sellCostPct:0.02}}));return has(r,'Exit cap rate of 50');})(),'');
ok('aggressive cap compression is flagged',(()=>{const r=E_healthCheck(mkHealthy({exit:{exitCap:0.03,sellCostPct:0.02}}));return has(r,'cap compression');})(),'');
ok('an implausible loan rate (67.5%) is flagged',(()=>{const m=mkHealthy();m.debt.rate=0.675;const r=E_healthCheck(m);return has(r,'Loan rate');})(),'');
ok('excessive closing costs are flagged',(()=>{const m=mkHealthy();m.acquisition.closingPct=0.20;const r=E_healthCheck(m);return has(r,'Closing costs');})(),'');
ok('excessive selling costs are flagged',(()=>{const r=E_healthCheck(mkHealthy({exit:{exitCap:0.06,sellCostPct:0.15}}));return has(r,'Selling costs');})(),'');
ok('very high credit/vacancy loss is flagged',(()=>{const m=mkHealthy();m.analysis.creditLoss=0.30;const r=E_healthCheck(m);return has(r,'vacancy loss');})(),'');

// growth
ok('aggressive rent growth is flagged',(()=>{const m=mkHealthy();m.mlas.forEach(x=>x.rentGrowth=0.10);const r=E_healthCheck(m);return has(r,'rent growth');})(),'');

// waterfall / mezz / refi
ok('an unusually high promote is flagged',(()=>{const m=mkHealthy();m.equity.promote=0.70;const r=E_healthCheck(m);return has(r,'promote');})(),'');
ok('an unusually high preferred return is flagged',(()=>{const m=mkHealthy();m.equity.pref=0.30;const r=E_healthCheck(m);return has(r,'Preferred return');})(),'');
ok('mezzanine priced below senior is flagged',(()=>{const m=mkHealthy();m.debt.mezz={amount:1000000,rate:0.03,ioMonths:0,amortMonths:360};const r=E_healthCheck(m);return has(r,'mezzanine rate');})(),'');
ok('a refinance after the hold ends is flagged',(()=>{const m=mkHealthy();m.debt.refiOn=true;m.debt.refiMonth=999;const r=E_healthCheck(m);return has(r,'refinance month');})(),'');

// counts consistency
{const r=E_healthCheck(mkHealthy({exit:{exitCap:0.5,sellCostPct:0.15}}));
 ok('severity counts match the item list',
   r.nError===r.items.filter(i=>i.sev==='error').length&&r.nWarn===r.items.filter(i=>i.sev==='warn').length&&r.nInfo===r.items.filter(i=>i.sev==='info').length,'');}

// immutability
{const m=mkHealthy();const before=JSON.stringify(m);E_healthCheck(m);E_healthCheck(m);
 ok('the scan never mutates the model',JSON.stringify(m)===before,'model changed');}

// robustness on an empty model
ok('an empty model does not throw',(()=>{try{const r=E_healthCheck({});return r.ok===true;}catch(e){return false;}})(),'');

console.log('\n'+pass+' passed, '+fail+' failed.');
process.exit(fail?1:0);
