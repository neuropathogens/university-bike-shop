/* WBI7 — analytic tests for the version diff ("git for deals"). E_diff walks two
   model snapshots and returns leaf-level changes (path, old, new, kind) with number
   tolerance; E_diffBridge attributes the levered-IRR change to each top-level group
   of assumptions by replacing only that group and re-running the engine. These check:
   identical-model no-change, single/nested/array leaf changes, number tolerance,
   added/removed elements and keys, attribution correctness (each group's standalone
   effect), single-change zero residual, full-coverage of changes, and immutability. */
const fs=require('fs'),vm=require('vm');
const html=fs.readFileSync(__dirname+'/index.html','utf8');
const a=html.indexOf('/* ===================== WBI7 ENGINE START');
const b=html.indexOf('WBI7 ENGINE END ===================== */');
const ctx={console};vm.createContext(ctx);
vm.runInContext(html.slice(a,b+'WBI7 ENGINE END ===================== */'.length),ctx);
const {computeDeal,E_diff,E_diffBridge}=ctx;
let pass=0,fail=0;
const ok=(n,c,x)=>{c?pass++:fail++;console.log((c?'  PASS  ':'  FAIL  ')+n+(c?'':'  -> '+x));};
const near=(p,q,t)=>Math.abs(p-q)<=t;
const clone=x=>JSON.parse(JSON.stringify(x));

function mk(over){const m={version:'wbi7-1',project:'Base Deal',
  analysis:{holdMonths:84,discountRate:0.072,creditLoss:0.01,inflation:0},
  acquisition:{price:15000000,closingPct:0},capex:[],
  property:{suites:[{id:'S1',name:'U1',sf:100000}]},
  mlas:[{id:'M1',name:'flex',marketRent:1.25,rentGrowth:0.03,termMonths:60,renewalProb:0.7,downtimeMonths:6,
    freeNew:1,freeRenew:0,tiNew:3,tiRenew:1,lcNew:0.05,lcRenew:0.025,escalation:{type:'fixedPct',value:0.03},recMethod:'net',recParam:100}],
  rentRoll:[{id:'L1',tenant:'A',suiteId:'S1',sf:100000,startMonth:-12,termMonths:60,baseRent:1.2,escalation:{type:'fixedPct',value:0.03},freeMonths:0,recMethod:'net',recParam:100,mlaId:'M1',uponExpiry:'market'}],
  absorption:[],expenses:[{name:'CAM',basis:'psf',amount:1.2,growth:0.03,recoverable:true,varOcc:true},
    {name:'Tax',basis:'fixed',amount:170000,growth:0.02,recoverable:true,varOcc:false}],
  recoverySettings:{grossUpOn:false,grossUpPct:0.95,adminFee:0},otherIncome:{amount:0,growth:0},
  debt:{type:'ltv',ltv:0.6,amount:0,rate:0.062,ioMonths:0,amortMonths:360},
  exit:{exitCap:0.055,sellCostPct:0.02},equity:{lpShare:1,pref:0,promote:0}};
  return Object.assign(m,over||{});}

console.log('--- Version diff (git for deals) ---');

// 1) identical models -> no changes
{const m=mk();const R=E_diff(m,clone(m));
 ok('D1 identical models report no changes',R.summary.n===0,R.summary.n);}

// 2) single leaf change with correct path/old/new/kind
{const o=mk(),n=clone(o);n.debt.rate=0.07;
 const R=E_diff(o,n);
 ok('D2 one change detected',R.summary.n===1&&R.summary.changed===1,JSON.stringify(R.summary));
 const c=R.changes[0];
 ok('D2 path/old/new/kind correct',c.path==='debt.rate'&&c.old===0.062&&c.new===0.07&&c.kind==='changed',JSON.stringify(c));}

// 3) number tolerance: the load round-trip's float drift is not a change
{const o=mk(),n=clone(o);n.mlas[0].rentGrowth=0.03+1e-12;
 const R=E_diff(o,n);
 ok('D3 sub-epsilon float drift is ignored',R.summary.n===0,R.summary.n);}

// 4) nested + array-indexed paths
{const o=mk(),n=clone(o);n.rentRoll[0].baseRent=1.30;n.exit.exitCap=0.06;
 const R=E_diff(o,n);
 const paths=R.changes.map(c=>c.path).sort();
 ok('D4 nested + array paths reported',R.summary.n===2&&paths[0]==='exit.exitCap'&&paths[1]==='rentRoll[0].baseRent',paths.join(','));}

// 5) added / removed array element
{const o=mk(),n=clone(o);n.rentRoll.push({id:'L2',tenant:'B',sf:0,baseRent:2.0});
 const R=E_diff(o,n);
 ok('D5 added array element flagged as added',R.summary.added===1&&R.changes[0].path==='rentRoll[1]',JSON.stringify(R.summary));
 const R2=E_diff(n,o);
 ok('D5 reverse direction flags it as removed',R2.summary.removed===1,JSON.stringify(R2.summary));}

// 6) added / removed top-level key (reported at the subtree level, like an added element)
{const o=mk(),n=clone(o);n.killzone={targetIrr:0.05};
 const R=E_diff(o,n);
 const c=R.changes[0];
 ok('D6 added top-level key detected as a subtree add',R.summary.added===1&&c.path==='killzone'&&c.kind==='added'&&c.new&&c.new.targetIrr===0.05,JSON.stringify(c));}

// 7) attribution: single-group change -> contribution equals total, residual ~ 0
{const o=mk(),n=clone(o);n.exit.exitCap=0.065;
 const B=E_diffBridge(o,n);
 const indep=computeDeal((()=>{const m=clone(o);m.exit=clone(n.exit);return m;})()).irrL-computeDeal(o).irrL;
 ok('D7 exit group is the only contributor',B.groups.length===1&&B.groups[0].key==='exit',JSON.stringify(B.groups.map(g=>g.key)));
 ok('D7 contribution matches an independent re-run',near(B.groups[0].contribution,indep,1e-12),B.groups[0].contribution+' vs '+indep);
 ok('D7 single-group residual is ~0',near(B.residual,0,1e-9),B.residual);
 ok('D7 total equals new IRR minus base',near(B.total,B.newIrr-B.baseIrr,1e-12),B.total);}

// 8) attribution across multiple groups: each contribution is its standalone effect,
//    groups cover all changed top-level keys, and total = sumContrib + residual
{const o=mk(),n=clone(o);n.exit.exitCap=0.065;n.debt.rate=0.075;n.mlas[0].rentGrowth=0.02;
 const B=E_diffBridge(o,n);
 ok('D8 three changed groups attributed',B.groups.length===3,B.groups.map(g=>g.key).join(','));
 // verify each group's standalone contribution
 let okAll=true;B.groups.forEach(g=>{const m=clone(o);m[g.key]=clone(n[g.key]);
   const c=computeDeal(m).irrL-computeDeal(o).irrL;if(!near(c,g.contribution,1e-12))okAll=false;});
 ok('D8 every group contribution matches its independent re-run',okAll,'');
 const sum=B.groups.reduce((s,g)=>s+g.contribution,0);
 ok('D8 total = sum of contributions + interaction residual',near(B.total,sum+B.residual,1e-12),B.total+' vs '+(sum+B.residual));
 // interactions are real -> residual is generally non-zero here
 ok('D8 a non-trivial interaction residual is surfaced',Math.abs(B.residual)>1e-9,B.residual);}

// 9) immutability: inputs untouched by diff and bridge
{const o=mk(),n=clone(o);n.debt.rate=0.08;n.exit.exitCap=0.07;
 const oBefore=JSON.stringify(o),nBefore=JSON.stringify(n);
 E_diff(o,n);E_diffBridge(o,n);
 ok('D9 base + new models unchanged after diff/bridge',JSON.stringify(o)===oBefore&&JSON.stringify(n)===nBefore,'');}

console.log('\n'+pass+' passed, '+fail+' failed.');
process.exit(fail?1:0);
