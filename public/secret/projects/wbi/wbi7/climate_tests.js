/* WBI7 — analytic tests for climate / insurance stress. E_climate is a pure overlay
   that raises insurance cost (multiplier on the matched line + owner-borne additive
   insurance and uninsured-loss reserve per SF) and re-runs the engine. CLIMATE_parseFlood
   reads a FEMA NFHL (ArcGIS) response; CLIMATE_zoneRisk maps a zone to a risk tier.
   Checks: additive owner cost reduces year-1 NOI by exactly that amount, the stress
   lowers DSCR and IRR, the multiplier scales an owner-paid insurance line, neutral
   options are a no-op, immutability, flood-zone parsing, and zone-risk mapping. */
const fs=require('fs'),vm=require('vm');
const html=fs.readFileSync(__dirname+'/index.html','utf8');
const a=html.indexOf('/* ===================== WBI7 ENGINE START');
const b=html.indexOf('WBI7 ENGINE END ===================== */');
const ctx={console};vm.createContext(ctx);
vm.runInContext(html.slice(a,b+'WBI7 ENGINE END ===================== */'.length),ctx);
const {computeDeal,E_climate,CLIMATE_parseFlood,CLIMATE_zoneRisk}=ctx;
let pass=0,fail=0;
const ok=(n,c,x)=>{c?pass++:fail++;console.log((c?'  PASS  ':'  FAIL  ')+n+(c?'':'  -> '+x));};
const near=(p,q,t)=>Math.abs(p-q)<=t;

function mk(insurance){const exp=[{name:'CAM',basis:'psf',amount:1.2,growth:0.03,recoverable:true,varOcc:true},
    {name:'Tax',basis:'fixed',amount:170000,growth:0.02,recoverable:true,varOcc:false}];
  if(insurance)exp.push({name:'Insurance',basis:'psf',amount:0.30,growth:0.03,recoverable:false,varOcc:false});
  return {version:'wbi7-1',project:'Base Deal',
  analysis:{holdMonths:84,discountRate:0.072,creditLoss:0.01,inflation:0},
  acquisition:{price:15000000,closingPct:0},capex:[],
  property:{suites:[{id:'S1',name:'U1',sf:100000}]},
  mlas:[{id:'M1',name:'flex',marketRent:1.25,rentGrowth:0.03,termMonths:60,renewalProb:0.7,downtimeMonths:6,
    freeNew:1,freeRenew:0,tiNew:3,tiRenew:1,lcNew:0.05,lcRenew:0.025,escalation:{type:'fixedPct',value:0.03},recMethod:'net',recParam:100}],
  rentRoll:[{id:'L1',tenant:'A',suiteId:'S1',sf:100000,startMonth:-12,termMonths:60,baseRent:1.2,escalation:{type:'fixedPct',value:0.03},freeMonths:0,recMethod:'net',recParam:100,mlaId:'M1',uponExpiry:'market'}],
  absorption:[],expenses:exp,
  recoverySettings:{grossUpOn:false,grossUpPct:0.95,adminFee:0},otherIncome:{amount:0,growth:0},
  debt:{type:'ltv',ltv:0.6,amount:0,rate:0.062,ioMonths:0,amortMonths:360},
  exit:{exitCap:0.055,sellCostPct:0.02},equity:{lpShare:1,pref:0,promote:0}};}

console.log('--- Climate / insurance stress ---');

// 1) additive owner-borne cost reduces year-1 NOI by exactly that amount
{const R=E_climate(mk(),{insAddPsf:0.25,reservePsf:0.15});
 ok('C1 SF picked up from the deal (100k)',R.sf===100000,R.sf);
 ok('C1 added annual owner cost = (0.25+0.15) x SF',near(R.addAnnual,0.40*100000,1),R.addAnnual);
 ok('C1 year-1 NOI drops by ~the added cost (modulo intra-year escalation)',near(R.delta.noi,-R.addAnnual,R.addAnnual*0.02),R.delta.noi+' vs '+(-R.addAnnual));}

// 2) the stress lowers DSCR, IRR, equity multiple, value and profit
{const R=E_climate(mk(),{insAddPsf:0.30,reservePsf:0.20});
 ok('C2 DSCR falls under the stress',R.delta.dscr<0,R.delta.dscr);
 ok('C2 levered IRR falls under the stress',R.delta.irrL<0,R.delta.irrL);
 ok('C2 value and profit fall under the stress',R.delta.value<0&&R.delta.profit<0,R.delta.value+'/'+R.delta.profit);}

// 3) multiplier scales an owner-paid insurance line (non-recoverable here)
{const R=E_climate(mk(true),{insMult:2});
 const insY1=0.30*100000; // owner-paid insurance, year 1
 ok('C3 insurance line detected',R.hadInsurance===true,'');
 ok('C3 doubling owner-paid insurance reduces NOI by ~one premium',near(R.delta.noi,-insY1,insY1*0.02),R.delta.noi+' vs '+(-insY1));}

// 4) no insurance line + multiplier only -> no NOI change (nothing to scale, no reserve)
{const R=E_climate(mk(false),{insMult:3});
 ok('C4 multiplier with no insurance line is a no-op',R.hadInsurance===false&&near(R.delta.noi,0,1e-6),R.delta.noi);}

// 5) neutral options -> zero stress
{const R=E_climate(mk(true),{insMult:1,insAddPsf:0,reservePsf:0});
 ok('C5 neutral options leave the deal unchanged',near(R.delta.noi,0,1e-6)&&near(R.delta.irrL||0,0,1e-9),R.delta.noi);}

// 6) immutability + zone passthrough
{const m=mk(true),before=JSON.stringify(m);
 const R=E_climate(m,{insAddPsf:0.2,reservePsf:0.1,insMult:1.5,zone:'AE'});
 ok('C6 base model unchanged after stress',JSON.stringify(m)===before,'');
 ok('C6 zone passed through to the result',R.zone==='AE',R.zone);}

// 7) FEMA NFHL flood-zone parsing
{const j={features:[{attributes:{FLD_ZONE:'AE',ZONE_SUBTY:'',SFHA_TF:'T'}}]};
 const z=CLIMATE_parseFlood(j);
 ok('C7 parses FLD_ZONE / SFHA from a FEMA response',z&&z.zone==='AE'&&z.sfha===true,JSON.stringify(z));
 ok('C7 empty feature set -> null',CLIMATE_parseFlood({features:[]})===null&&CLIMATE_parseFlood(null)===null,'');}

// 8) zone -> risk mapping
{const hi=CLIMATE_zoneRisk('VE'),aZone=CLIMATE_zoneRisk('A'),lo=CLIMATE_zoneRisk('X'),
   mod=CLIMATE_zoneRisk('X','0.2 PCT ANNUAL CHANCE FLOOD HAZARD'),un=CLIMATE_zoneRisk('D');
 ok('C8 V/A zones map to high risk with a suggested stress',hi.risk==='high'&&aZone.risk==='high'&&hi.suggestAddPsf>0,JSON.stringify(hi));
 ok('C8 plain X maps to low (no stress)',lo.risk==='low'&&lo.suggestAddPsf===0,JSON.stringify(lo));
 ok('C8 shaded X (0.2%) maps to moderate',mod.risk==='moderate'&&mod.suggestAddPsf>0,JSON.stringify(mod));
 ok('C8 zone D maps to undetermined',un.risk==='undetermined',JSON.stringify(un));}

console.log('\n'+pass+' passed, '+fail+' failed.');
process.exit(fail?1:0);
