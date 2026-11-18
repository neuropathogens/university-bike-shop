/* WBI7 — analytic tests for the two-way sensitivity table (E_sensTable). Pure overlay:
   two drivers are each stepped across a symmetric range of fixed increments and the
   full engine is re-run at every (row,col) pair. These check: grid dimensions for each
   size, the centre cell equaling the live model exactly (for several metrics), symmetric
   delta-labeled axes, economically-correct monotonicity (exit cap up => IRR down, rent
   growth up => IRR up, price up => IRR down, loan rate up => IRR down), the same-driver
   and unknown-driver guards, min/max bracketing, step clamping, and — most important —
   base-model immutability (the overlay must mutate nothing). */
const fs=require('fs'),vm=require('vm');
const html=fs.readFileSync(__dirname+'/index.html','utf8');
const a=html.indexOf('/* ===================== WBI7 ENGINE START');
const b=html.indexOf('WBI7 ENGINE END ===================== */');
const ctx={console};vm.createContext(ctx);
vm.runInContext(html.slice(a,b+'WBI7 ENGINE END ===================== */'.length),ctx);
const {computeDeal,E_sensTable}=ctx;
let pass=0,fail=0;
const ok=(n,c,x)=>{c?pass++:fail++;console.log((c?'  PASS  ':'  FAIL  ')+n+(c?'':'  -> '+x));};

// healthy deal with a comfortably positive, defined levered IRR
function mkHealthy(over){const m=Object.assign({version:'wbi7-1',
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
  exit:{exitCap:0.055,sellCostPct:0.02},equity:{lpShare:1,pref:0,promote:0}},over);return m;}

console.log('--- Two-way sensitivity table ---');

const M=mkHealthy();
const live=computeDeal(M);

// dimensions
const R1=E_sensTable(M,{rowKey:'exitCap',colKey:'rentGrowth',metric:'irrL',steps:1});
const R2=E_sensTable(M,{rowKey:'exitCap',colKey:'rentGrowth',metric:'irrL',steps:2});
const R3=E_sensTable(M,{rowKey:'exitCap',colKey:'rentGrowth',metric:'irrL',steps:3});
ok('steps=1 builds a 3x3 grid',R1.ok&&R1.grid.length===3&&R1.grid[0].length===3,JSON.stringify(R1.grid&&R1.grid.length));
ok('steps=2 builds a 5x5 grid',R2.ok&&R2.grid.length===5&&R2.grid[0].length===5,'');
ok('steps=3 builds a 7x7 grid',R3.ok&&R3.grid.length===7&&R3.grid[0].length===7,'');

// centre cell == live model, for several metrics
ok('centre cell equals live levered IRR exactly',Math.abs(R2.grid[R2.baseRow][R2.baseCol]-live.irrL)<1e-12,String(R2.grid[R2.baseRow][R2.baseCol]-live.irrL));
const Rem=E_sensTable(M,{rowKey:'exitCap',colKey:'price',metric:'emL',steps:2});
ok('centre cell equals live equity multiple exactly',Math.abs(Rem.grid[Rem.baseRow][Rem.baseCol]-live.emL)<1e-12,'');
const Rpr=E_sensTable(M,{rowKey:'price',colKey:'debtRate',metric:'profit',steps:2});
ok('centre cell equals live total profit exactly',Math.abs(Rpr.grid[Rpr.baseRow][Rpr.baseCol]-live.profit)<1e-6,'');

// axes: centre labeled "base", symmetric, deltas centered on zero
ok('row/col centre header is "base"',R2.rowHeaders[2]==='base'&&R2.colHeaders[2]==='base',R2.rowHeaders.join(','));
ok('axis deltas are symmetric and centered on 0',R2.rowDeltas[0]===-R2.rowDeltas[4]&&R2.rowDeltas[2]===0,R2.rowDeltas.join(','));
ok('header count matches grid size',R2.rowHeaders.length===5&&R2.colHeaders.length===5,'');

// economically-correct monotonicity (relative to the engine's own output, not hardcoded)
// rows = exit cap ascending top->bottom; higher exit cap => lower IRR
ok('exit cap up => levered IRR down (base column)',R2.grid[0][R2.baseCol] > R2.grid[4][R2.baseCol],R2.grid[0][R2.baseCol]+' vs '+R2.grid[4][R2.baseCol]);
// cols = rent growth ascending left->right; higher growth => higher IRR
ok('rent growth up => levered IRR up (base row)',R2.grid[R2.baseRow][0] < R2.grid[R2.baseRow][4],R2.grid[R2.baseRow][0]+' vs '+R2.grid[R2.baseRow][4]);
const Rp=E_sensTable(M,{rowKey:'price',colKey:'debtRate',metric:'irrL',steps:2});
ok('purchase price up => levered IRR down (base column)',Rp.grid[0][Rp.baseCol] > Rp.grid[4][Rp.baseCol],'');
ok('loan rate up => levered IRR down (base row)',Rp.grid[Rp.baseRow][0] > Rp.grid[Rp.baseRow][4],'');

// full monotonic ordering down the exit-cap axis at the base column
let mono=true;for(let r=1;r<5;r++){if(!(R2.grid[r][R2.baseCol] <= R2.grid[r-1][R2.baseCol]+1e-12))mono=false;}
ok('levered IRR is monotone non-increasing down the exit-cap axis',mono,'');

// min/max bracket every finite cell
let within=true;R2.grid.forEach(row=>row.forEach(v=>{if(v!=null&&(v<R2.min-1e-12||v>R2.max+1e-12))within=false;}));
ok('reported min/max bracket all grid values',within&&R2.min<=R2.max,'');

// guards
ok('same driver on both axes is rejected',E_sensTable(M,{rowKey:'exitCap',colKey:'exitCap'}).ok===false,'');
ok('unknown driver is rejected',E_sensTable(M,{rowKey:'exitCap',colKey:'nope'}).ok===false,'');

// step clamping: 0 -> 1 (3x3), 10 -> 4 (9x9)
ok('steps below 1 clamp to a 3x3 grid',E_sensTable(M,{rowKey:'exitCap',colKey:'price',steps:0}).grid.length===3,'');
ok('steps above 4 clamp to a 9x9 grid',E_sensTable(M,{rowKey:'exitCap',colKey:'price',steps:10}).grid.length===9,'');

// base-model immutability — the overlay must mutate nothing
const before=JSON.stringify(M);
E_sensTable(M,{rowKey:'price',colKey:'rentLevel',metric:'profit',steps:3});
E_sensTable(M,{rowKey:'creditLoss',colKey:'opexGrowth',metric:'irrL',steps:2});
ok('base model is never mutated by the overlay',JSON.stringify(M)===before,'model changed');
ok('re-running yields an identical centre cell (determinism)',E_sensTable(M,{rowKey:'exitCap',colKey:'rentGrowth',metric:'irrL',steps:2}).grid[2][2]===R2.grid[2][2],'');

console.log('\n'+pass+' passed, '+fail+' failed.');
process.exit(fail?1:0);
