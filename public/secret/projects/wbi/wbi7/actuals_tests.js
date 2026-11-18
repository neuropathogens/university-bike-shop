/* WBI7 — analytic tests for actuals vs underwriting. parseActuals reads free-text
   "year NOI [EGI] [CF]" lines (whitespace/semicolon separated, $ and thousands commas
   tolerated). E_actuals compares each entered year against the model's projected
   annual figures, reporting per-year variance, a cumulative NOI index, and ahead/on/
   behind status. Variances are computed RELATIVE TO the engine's own projection so the
   tests don't hard-code numbers: read projected NOI, then feed actuals at known ratios. */
const fs=require('fs'),vm=require('vm');
const html=fs.readFileSync(__dirname+'/index.html','utf8');
const a=html.indexOf('/* ===================== WBI7 ENGINE START');
const b=html.indexOf('WBI7 ENGINE END ===================== */');
const ctx={console};vm.createContext(ctx);
vm.runInContext(html.slice(a,b+'WBI7 ENGINE END ===================== */'.length),ctx);
const {computeDeal,parseActuals,E_actuals}=ctx;
let pass=0,fail=0;
const ok=(n,c,x)=>{c?pass++:fail++;console.log((c?'  PASS  ':'  FAIL  ')+n+(c?'':'  -> '+x));};
const near=(p,q,t)=>Math.abs(p-q)<=t;

function mk(){return {version:'wbi7-1',project:'Base Deal',
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
  exit:{exitCap:0.055,sellCostPct:0.02},equity:{lpShare:1,pref:0,promote:0}};}

const projNoi=y=>{const d=computeDeal(mk());const r=(d.annual||[]).find(a=>a.y===y);return r?r.noi:null;};

console.log('--- Actuals vs underwriting ---');

// 1) parser: whitespace / semicolons / $ / thousands commas
{const p=parseActuals("1 1200000\n2; $1,250,000; 1,100,000\n# comment\n\n3 1300000 1150000 900000");
 ok('P1 parses three data rows (ignores blanks/comments)',p.length===3,p.length);
 ok('P1 year + NOI parsed',p[0].year===1&&p[0].noi===1200000,JSON.stringify(p[0]));
 ok('P1 $ and thousands commas stripped; EGI captured',p[1].year===2&&p[1].noi===1250000&&p[1].egi===1100000,JSON.stringify(p[1]));
 ok('P1 optional CF captured when present',p[2].cf===900000,JSON.stringify(p[2]));}

// 2) empty / junk input -> empty list
{ok('P2 empty input yields no rows',parseActuals("").length===0&&parseActuals("   \n#x").length===0,'');}

// 3) one year ABOVE projection -> "ahead", variance math correct
{const p1=projNoi(1);const R=E_actuals(mk(),[{year:1,noi:p1*1.10}],{threshold:0.05});
 ok('A3 one year tracked',R.nTracked===1,R.nTracked);
 const m=R.rows[0].metrics.noi;
 ok('A3 status ahead when actual 10% over projection',m.status==='ahead',m.status);
 ok('A3 variance $ = actual - projected',near(m.varAbs,p1*0.10,1),m.varAbs);
 ok('A3 variance % ~ +10%',near(m.varPct,0.10,1e-9),m.varPct);}

// 4) below projection -> "behind"
{const p1=projNoi(1);const R=E_actuals(mk(),[{year:1,noi:p1*0.90}],{threshold:0.05});
 ok('A4 status behind when actual 10% under projection',R.rows[0].metrics.noi.status==='behind',R.rows[0].metrics.noi.status);}

// 5) within threshold -> "on"
{const p1=projNoi(1);const R=E_actuals(mk(),[{year:1,noi:p1*1.01}],{threshold:0.05});
 ok('A5 status on-track within +/-5%',R.rows[0].metrics.noi.status==='on',R.rows[0].metrics.noi.status);}

// 6) cumulative index across multiple years
{const p1=projNoi(1),p2=projNoi(2),p3=projNoi(3);
 const R=E_actuals(mk(),[{year:1,noi:p1*0.95},{year:2,noi:p2*0.95},{year:3,noi:p3*0.95}],{threshold:0.02});
 ok('A6 three years tracked',R.nTracked===3,R.nTracked);
 ok('A6 cumulative projected NOI = sum of projections',near(R.cum.projNoi,p1+p2+p3,1),R.cum.projNoi);
 ok('A6 cumulative index ~ 0.95 of underwriting',near(R.cum.index,0.95,1e-6),R.cum.index);
 ok('A6 cumulative status behind (5% under, >2% bar)',R.cum.status==='behind',R.cum.status);
 ok('A6 latest reflects the most recent tracked year',R.latest&&R.latest.year===3,JSON.stringify(R.latest));}

// 7) a year beyond the projection horizon is flagged, not counted
{const R=E_actuals(mk(),[{year:99,noi:1000000}],{threshold:0.05});
 ok('A7 out-of-horizon year flagged beyond + not tracked',R.rows[0].beyond===true&&R.nTracked===0,JSON.stringify(R.rows[0]));}

// 8) optional EGI/CF metrics tracked only when provided
{const p1=projNoi(1);const R=E_actuals(mk(),[{year:1,noi:p1}],{threshold:0.05});
 ok('A8 NOI metric present, EGI/CF absent when not supplied',!!R.rows[0].metrics.noi&&!R.rows[0].metrics.egi&&!R.rows[0].metrics.cf,'');}

// 9) immutability
{const m=mk(),acts=[{year:1,noi:projNoi(1)*0.9}];const mB=JSON.stringify(m),aB=JSON.stringify(acts);
 E_actuals(m,acts,{threshold:0.05});
 ok('A9 model + actuals unchanged',JSON.stringify(m)===mB&&JSON.stringify(acts)===aB,'');}

// 10) empty actuals -> ok with nothing tracked
{const R=E_actuals(mk(),[],{threshold:0.05});
 ok('A10 empty actuals: ok, zero tracked',R.ok===true&&R.nTracked===0,JSON.stringify(R.cum));}

console.log('\n'+pass+' passed, '+fail+' failed.');
process.exit(fail?1:0);
