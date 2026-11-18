/* WBI7 — analytic tests for the portfolio / fund roll-up (computePortfolio).
   Extracts the pure engine from index.html and checks the aggregation against
   first principles: a lone deal reproduces itself (and is offset-invariant),
   dollars are additive across deals, the fund IRR blends deal IRRs, and the
   fund-level waterfall conserves total cash (lp + gp = fund profit). */
const fs=require('fs'),vm=require('vm');
const html=fs.readFileSync(__dirname+'/index.html','utf8');
const a=html.indexOf('/* ===================== WBI7 ENGINE START');
const b=html.indexOf('WBI7 ENGINE END ===================== */');
const ctx={console};vm.createContext(ctx);
vm.runInContext(html.slice(a,b+'WBI7 ENGINE END ===================== */'.length),ctx);
const {computeDeal,computePortfolio}=ctx;
let pass=0,fail=0;
const ok=(n,c,x)=>{c?pass++:fail++;console.log((c?'  PASS  ':'  FAIL  ')+n+(c?'':'  -> '+x));};
const near=(a,b,t)=>Math.abs(a-b)<=t;

/* a compact, healthy single-suite deal with debt (real levered returns) */
function base(over){return Object.assign({version:'wbi7-1',
  analysis:{holdMonths:120,discountRate:0.075,creditLoss:0,inflation:0},
  acquisition:{price:3000000,closingPct:0},capex:[],
  property:{suites:[{id:'S1',name:'A',sf:10000}]},
  mlas:[{id:'M1',name:'mkt',marketRent:2.0,rentGrowth:0.03,termMonths:240,renewalProb:1,downtimeMonths:0,
    freeNew:0,freeRenew:0,tiNew:0,tiRenew:0,lcNew:0,lcRenew:0,escalation:{type:'fixedPct',value:0.03},recMethod:'none',recParam:0}],
  rentRoll:[{id:'L1',suiteId:'S1',sf:10000,startMonth:0,termMonths:240,baseRent:2.0,
    escalation:{type:'fixedPct',value:0.03},freeMonths:0,recMethod:'none',recParam:0,mlaId:'M1',uponExpiry:'renew'}],
  absorption:[],expenses:[],otherIncome:{amount:0,growth:0},
  debt:{type:'ltv',ltv:0.6,amount:0,rate:0.06,ioMonths:24,amortMonths:360},
  exit:{exitCap:0.07,sellCostPct:0},equity:{lpShare:1,pref:0,promote:0}},over);}

console.log('--- Portfolio roll-up ---');

// 0) empty fund -> graceful zeros/nulls
{const f=computePortfolio([]);
 ok('PF0 empty fund -> n=0, irr null, equity 0',f.n===0&&f.irrL===null&&f.equity===0,JSON.stringify({n:f.n,irr:f.irrL,eq:f.equity}));}

// 1) single deal, offset 0 -> reproduces the deal exactly
{const m=base({});const d=computeDeal(m);
 const f=computePortfolio([{model:m,startMonth:0,name:'one'}]);
 ok('PF1 single-deal fund levered IRR == deal IRR',near(f.irrL,d.irrL,1e-9),f.irrL+' vs '+d.irrL);
 ok('PF1 single-deal fund unlevered IRR == deal IRR',near(f.irrU,d.irrU,1e-9),f.irrU+' vs '+d.irrU);
 ok('PF1 single-deal fund EM == deal EM',near(f.emL,d.emL,1e-9),f.emL+' vs '+d.emL);
 ok('PF1 single-deal fund profit == deal profit',near(f.profit,d.profit,1e-3),f.profit+' vs '+d.profit);
 ok('PF1 single-deal fund equity == deal equity0',near(f.equity,d.equity0,1e-3),f.equity+' vs '+d.equity0);
 ok('PF1 fund timeline length == deal M',f.M===d.M,f.M+' vs '+d.M);
 ok('PF1 one deal listed in fund',f.deals.length===1&&f.deals[0].name==='one','');}

// 2) two identical deals, offset 0 -> dollars double, IRR/EM unchanged (scale-invariant)
{const m=base({});const d=computeDeal(m);
 const f=computePortfolio([{model:m,startMonth:0},{model:m,startMonth:0}]);
 ok('PF2 two identical: fund profit == 2x deal profit',near(f.profit,2*d.profit,1e-2),f.profit+' vs '+2*d.profit);
 ok('PF2 two identical: fund equity == 2x deal equity',near(f.equity,2*d.equity0,1e-2),f.equity+' vs '+2*d.equity0);
 ok('PF2 two identical: fund IRR == deal IRR (scale-invariant)',near(f.irrL,d.irrL,1e-9),f.irrL+' vs '+d.irrL);
 ok('PF2 two identical: fund EM == deal EM',near(f.emL,d.emL,1e-9),f.emL+' vs '+d.emL);}

// 3) single deal, offset by K months -> IRR offset-invariant; outlay lands at month K
{const K=24,m=base({});const d=computeDeal(m);
 const f=computePortfolio([{model:m,startMonth:K}]);
 ok('PF3 offset deal: fund IRR == deal IRR (time-shift factors out)',near(f.irrL,d.irrL,1e-9),f.irrL+' vs '+d.irrL);
 ok('PF3 offset deal: equity outlay lands at fund month K',near(f.fundEq[K],d.eq[0],1e-6),f.fundEq[K]+' vs '+d.eq[0]);
 ok('PF3 offset deal: timeline length == K + deal M',f.M===K+d.M,f.M+' vs '+(K+d.M));
 ok('PF3 offset deal: months before K are empty',f.fundEq.slice(0,K).every(x=>x===0),'');}

// 4) two different deals -> dollars are additive; fund IRR blends the two deal IRRs
{const m1=base({});                                   // 8% going-in vs 7% exit
 const m2=base({acquisition:{price:2600000,closingPct:0}}); // cheaper -> stronger
 const d1=computeDeal(m1),d2=computeDeal(m2);
 const f=computePortfolio([{model:m1,startMonth:0},{model:m2,startMonth:0}]);
 ok('PF4 fund profit == sum of deal profits',near(f.profit,d1.profit+d2.profit,1e-2),f.profit+' vs '+(d1.profit+d2.profit));
 ok('PF4 fund equity == sum of deal equity',near(f.equity,d1.equity0+d2.equity0,1e-2),f.equity+' vs '+(d1.equity0+d2.equity0));
 ok('PF4 fund value == sum of deal values',near(f.value,d1.value+d2.value,1e-2),'');
 const lo=Math.min(d1.irrL,d2.irrL),hi=Math.max(d1.irrL,d2.irrL);
 ok('PF4 fund IRR lies between the two deal IRRs',f.irrL>=lo-1e-6&&f.irrL<=hi+1e-6,f.irrL+' in ['+lo+','+hi+']');}

// 5) deferring the STRONGER of two different deals pulls the fund IRR toward the
//    weaker one (a time-shift factors out for identical streams, so the deals must
//    differ for timing to bite — that is the real economic content here)
{const m1=base({});                                        // weaker (price 3.0M)
 const m2=base({acquisition:{price:2600000,closingPct:0}}); // stronger (price 2.6M)
 const fNow=computePortfolio([{model:m1,startMonth:0},{model:m2,startMonth:0}]);
 const fLater=computePortfolio([{model:m1,startMonth:0},{model:m2,startMonth:36}]);
 ok('PF5 deferring the stronger deal 3 yrs lowers fund IRR',fLater.irrL<fNow.irrL,fLater.irrL+' vs '+fNow.irrL);}

// 6) fund-level waterfall conserves cash: lp + gp == fund profit
{const m1=base({}),m2=base({acquisition:{price:2600000,closingPct:0}});
 const f=computePortfolio([{model:m1,startMonth:0},{model:m2,startMonth:6}],
   {equity:{lpShare:0.9,pref:0.08,promote:0.2}});
 ok('PF6 fund waterfall conserves cash (lp + gp == profit)',near(f.lpProfit+f.gpProfit,f.profit,1e-2),
    (f.lpProfit+f.gpProfit)+' vs '+f.profit);
 ok('PF6 GP earns a promote (gp share of profit > 1 - lpShare)',
    f.profit>0?(f.gpProfit/f.profit)>0.10+1e-9:true,(f.profit>0?f.gpProfit/f.profit:0));
 ok('PF6 LP IRR is below the combined fund IRR (promote drag)',
    (f.lpIrr!=null&&f.irrL!=null)?f.lpIrr<=f.irrL+1e-9:true,f.lpIrr+' vs '+f.irrL);}

console.log('\n'+pass+' passed, '+fail+' failed.');
process.exit(fail?1:0);
