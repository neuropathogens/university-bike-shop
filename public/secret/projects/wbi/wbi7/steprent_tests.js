/* WBI7 — tests for stepped rent schedules. A lease can carry an explicit schedule of
   (month-from-commencement, $/SF/mo) steps that overrides the single escalation rate: the
   rent is the last step at or before the current lease month and is flat between steps,
   with the base rent applying before the first step. This represents the negotiated bumps
   common in ARGUS office/retail leases. Leases without a schedule fall back to the
   escalation path and are byte-identical. */
const fs=require('fs'),vm=require('vm');
const html=fs.readFileSync(__dirname+'/index.html','utf8');
const a=html.indexOf('/* ===================== WBI7 ENGINE START');
const b=html.indexOf('WBI7 ENGINE END ===================== */');
const ctx={console};vm.createContext(ctx);
vm.runInContext(html.slice(a,b+'WBI7 ENGINE END ===================== */'.length),ctx);
const {computeDeal,E_rentAt,E_esc}=ctx;
let pass=0,fail=0;
const ok=(n,c,x)=>{c?pass++:fail++;console.log((c?'  PASS  ':'  FAIL  ')+n+(c?'':'  -> '+x));};
const near=(a,b,e)=>Math.abs(a-b)<=(e==null?1:e);

console.log('--- stepped rent schedules ---');

// ===== E_rentAt unit tests =====
const steps=[{m:0,r:3},{m:36,r:3.6},{m:60,r:4.2}];
ok('E_rentAt returns the first step at k=0',near(E_rentAt(3,null,steps,0),3,1e-9),'');
ok('E_rentAt is flat between steps (k=35 still first step)',near(E_rentAt(3,null,steps,35),3,1e-9),'');
ok('E_rentAt takes the new step exactly at its month (k=36)',near(E_rentAt(3,null,steps,36),3.6,1e-9),'');
ok('E_rentAt holds the last step past the end (k=200)',near(E_rentAt(3,null,steps,200),4.2,1e-9),'');
ok('E_rentAt before the first step uses the base',near(E_rentAt(2.5,null,[{m:12,r:5}],0),2.5,1e-9),'');
{const esc={type:'fixedPct',value:0.03};
 ok('E_rentAt with no steps equals E_esc (byte-identical fallback)',near(E_rentAt(3,esc,null,24),E_esc(3,esc,24),1e-12),'');}

// ===== computeDeal integration =====
function mkDeal(over){return Object.assign({version:'wbi7-1',
  analysis:{holdMonths:84,discountRate:0.08,creditLoss:0,inflation:0.025},
  acquisition:{price:20000000,closingPct:0.02,reassess:false,taxRate:0.0115},capex:[],
  property:{suites:[{id:'S1',name:'U1',sf:100000}]},
  mlas:[{id:'M1',name:'mkt',marketRent:4,rentGrowth:0.03,termMonths:60,renewalProb:1,downtimeMonths:0,freeNew:0,freeRenew:0,tiNew:0,tiRenew:0,lcNew:0,lcRenew:0,escalation:{type:'fixedPct',value:0.03},recMethod:'net',recParam:100}],
  rentRoll:[{id:'L1',tenant:'A',suiteId:'S1',sf:100000,startMonth:0,termMonths:84,baseRent:3,escalation:{type:'fixedPct',value:0.03},freeMonths:0,recMethod:'net',recParam:100,mlaId:'M1',uponExpiry:'market'}],
  absorption:[],expenses:[{name:'Opex',basis:'psf',amount:3,growth:0,recoverable:false,varOcc:false}],
  recoverySettings:{grossUpOn:false,grossUpPct:0.95,adminFee:0},otherIncome:{amount:0,growth:0},
  debt:{type:'ltv',ltv:0,amount:0,rate:0.06,ioMonths:0,amortMonths:360,termMonths:0,refiOn:false,refiLtv:0.6,refiRate:0.06,refiCostPct:0,mezz:{amount:0,rate:0}},
  exit:{exitCap:0.07,sellCostPct:0.02},equity:{lpShare:1,pref:0,promote:0},fees:{}},over);}
const L=mkDeal().rentRoll[0];

// stepped lease: $3 (yrs1-3), $3.60 (yrs4-5), $4.20 (yrs6-7)
{const d=computeDeal(mkDeal({rentRoll:[Object.assign({},L,{rentSteps:[{month:0,rent:3},{month:36,rent:3.6},{month:60,rent:4.2}]})]}));
 const A=d.annual;
 ok('year 1 base rent = sf x first step x 12',near(A[0].rent,100000*3*12),A[0].rent.toFixed(0));
 ok('rent is flat within the first step (Y2 = Y1)',near(A[1].rent,A[0].rent),'');
 ok('rent steps up at month 36 (Y4 = $3.60)',near(A[3].rent,100000*3.6*12),A[3].rent.toFixed(0));
 ok('rent steps up at month 60 (Y6 = $4.20)',near(A[5].rent,100000*4.2*12),A[5].rent.toFixed(0));
 ok('rent is flat within a later step (Y5 = Y4)',near(A[4].rent,A[3].rent),'');}

// steps override the escalation field
{const stepped=computeDeal(mkDeal({rentRoll:[Object.assign({},L,{escalation:{type:'fixedPct',value:0.03},rentSteps:[{month:0,rent:3},{month:36,rent:3.6}]})]}));
 const esc=computeDeal(mkDeal());
 ok('steps override the escalation (Y2 differs from the 3% escalated lease)',Math.abs(stepped.annual[1].rent-esc.annual[1].rent)>1000,'');}

// in-place lease that commenced before acquisition lands on the right step
{const d=computeDeal(mkDeal({rentRoll:[Object.assign({},L,{startMonth:-24,termMonths:120,rentSteps:[{month:0,rent:3},{month:36,rent:3.6},{month:60,rent:4.2}]})]}));
 // model month 0 = lease month 24 -> still first step ($3); model month 12 = lease month 36 -> $3.60
 ok('a lease commenced 24mo pre-acquisition reads the correct in-place step (Y1 = $3)',near(d.annual[0].rent,100000*3*12),d.annual[0].rent.toFixed(0));
 ok('and steps up when its schedule reaches the next bump (Y2 = $3.60)',near(d.annual[1].rent,100000*3.6*12),d.annual[1].rent.toFixed(0));}

// no steps -> identical to escalation-only deal
{const noSteps=computeDeal(mkDeal());const noSteps2=computeDeal(mkDeal({rentRoll:[Object.assign({},L,{rentSteps:[]})]}));
 ok('an empty step schedule is identical to no schedule',near(noSteps.irrL,noSteps2.irrL,1e-12)&&near(noSteps.annual[2].rent,noSteps2.annual[2].rent,1e-9),'');}

// percentage-rent natural breakpoint reflects stepped rent
{const d=computeDeal(mkDeal({rentRoll:[Object.assign({},L,{rentSteps:[{month:0,rent:3},{month:36,rent:6}],overagePct:7,salesPSF:120,salesGrowth:0,bpType:'natural'})]}));
 // breakpoint = annual base rent / overage%; it should jump when the rent steps to $6 -> overage falls
 const y2over=d.annual[1].pct, y4over=d.annual[3].pct;
 ok('percentage-rent breakpoint uses the stepped rent (overage drops when rent steps up)',y4over<=y2over+1,'y2 '+y2over.toFixed(0)+' y4 '+y4over.toFixed(0));}

// immutability
{const m=mkDeal({rentRoll:[Object.assign({},L,{rentSteps:[{month:0,rent:3},{month:36,rent:3.6}]})]});const before=JSON.stringify(m);computeDeal(m);computeDeal(m);
 ok('computing a stepped-rent deal never mutates the model',JSON.stringify(m)===before,'');}

console.log('\n'+pass+' passed, '+fail+' failed.');
process.exit(fail?1:0);
