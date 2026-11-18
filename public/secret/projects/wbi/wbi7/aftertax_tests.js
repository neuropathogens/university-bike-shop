const fs=require('fs'),vm=require('vm');
const html=fs.readFileSync('index.html','utf8');
const a=html.indexOf('/* ===================== WBI7 ENGINE START');
const b=html.indexOf('WBI7 ENGINE END ===================== */');
const ctx={console};vm.createContext(ctx);
vm.runInContext(html.slice(a,b+'WBI7 ENGINE END ===================== */'.length),ctx);
const {computeDeal}=ctx;
let pass=0,fail=0;
const ok=(n,c,x)=>{c?pass++:fail++;console.log((c?'  PASS  ':'  FAIL  ')+n+(c?'':'  -> '+x));};
const near=(a,b,t)=>Math.abs(a-b)<=t;
function base(over){return Object.assign({version:'wbi7-1',
  analysis:{holdMonths:120,discountRate:0.075,creditLoss:0,inflation:0},
  acquisition:{price:1000000,closingPct:0},capex:[],
  property:{suites:[{id:'S1',name:'A',sf:10000}]},
  mlas:[],rentRoll:[{id:'L1',suiteId:'S1',sf:10000,startMonth:0,termMonths:240,baseRent:0.70,
    escalation:{type:'fixedPct',value:0.03},freeMonths:0,recMethod:'none',recParam:0,mlaId:'MX',uponExpiry:'renew'}],
  absorption:[],expenses:[{name:'op',basis:'psf',amount:1.5,growth:0.03,recoverable:false,varOcc:false}],
  otherIncome:{amount:0,growth:0},
  debt:{type:'ltv',ltv:0.6,amount:0,rate:0.06,ioMonths:24,amortMonths:360},
  exit:{exitCap:0.07,sellCostPct:0.02},equity:{lpShare:1,pref:0,promote:0},
  tax:{enabled:true,landPct:0.20,depreciationYears:39,ordinaryRate:0.37,capGainsRate:0.20,recaptureRate:0.25}},over);}

console.log('--- After-tax: off by default ---');
{const d=computeDeal(base({tax:{enabled:false}}));
 ok('T28 tax off -> afterTaxIrrL null',d.afterTaxIrrL===null,d.afterTaxIrrL);
 ok('T28 tax off -> taxOnSale 0',d.taxOnSale===0,d.taxOnSale);}

console.log('--- After-tax: depreciation + basis mechanics ---');
{const d=computeDeal(base({}));
 const expDepBasis=d.allIn*(1-0.20);
 ok('T29 depreciable basis = allIn x (1 - land%)',near(d.depBasis,expDepBasis,1e-6),d.depBasis+' vs '+expDepBasis);
 const depMonthly=expDepBasis/(39*12),expAccum=depMonthly*d.M;
 ok('T29 accumulated depreciation = monthly x hold',near(d.accumDep,expAccum,1e-6),d.accumDep+' vs '+expAccum);
 ok('T29 adjusted basis = cost basis - accum dep',near(d.adjBasis,d.allIn-d.accumDep,1e-6),d.adjBasis);
 ok('T29 total gain = net sale - adjusted basis',near(d.totalGain,d.netSale-d.adjBasis,1e-6),d.totalGain);}

console.log('--- After-tax: recapture / cap-gains split ---');
{const d=computeDeal(base({}));
 const recPortion=Math.min(d.accumDep,Math.max(0,d.totalGain));
 const expRecap=recPortion*0.25,expCG=Math.max(0,d.totalGain-recPortion)*0.20;
 ok('T30 recapture tax = min(accumDep,gain) x 25%',near(d.recaptureTax,expRecap,1e-6),d.recaptureTax+' vs '+expRecap);
 ok('T30 cap-gains tax = remaining gain x 20%',near(d.capGainsTax,expCG,1e-6),d.capGainsTax+' vs '+expCG);
 ok('T30 total sale tax = recapture + cap gains',near(d.taxOnSale,d.recaptureTax+d.capGainsTax,1e-9),d.taxOnSale);
 ok('T30 after-tax proceeds = before-tax proceeds - sale tax',near(d.afterTaxProceeds,d.proceeds-d.taxOnSale,1e-6),d.afterTaxProceeds);}

console.log('--- After-tax: operating tax shield ---');
{const d=computeDeal(base({}));
 const depMonthly=d.depBasis/(39*12);
 // year 1 has 24mo IO so interest known; recompute year-1 tax from primitives
 // annual[0].tax should equal (noi - interest - dep) x ord for year 1
 // interest year1 = sum of interest months 1..12; reconstruct via ds (IO => ds==interest in yr1)
 const noi1=d.annual[0].noi, ds1=d.annual[0].ds; // IO year so ds==interest
 const expTax1=(noi1-ds1-depMonthly*12)*0.37;
 ok('T31 year-1 operating tax = (NOI - interest - dep) x ord (IO yr)',near(d.annual[0].tax,expTax1,1e-6),d.annual[0].tax+' vs '+expTax1);}

console.log('--- After-tax: shield raises after-tax return; ordering ---');
{const shielded=computeDeal(base({}));                         // land 20% -> real depreciation
 const noShield=computeDeal(base({tax:{enabled:true,landPct:1.0,depreciationYears:39,ordinaryRate:0.37,capGainsRate:0.20,recaptureRate:0.25}})); // land 100% -> no dep
 ok('T31b depreciation shield raises after-tax IRR',shielded.afterTaxIrrL>noShield.afterTaxIrrL,
    (shielded.afterTaxIrrL*100).toFixed(2)+'% vs '+(noShield.afterTaxIrrL*100).toFixed(2)+'%');
 ok('T31c after-tax IRR below before-tax IRR (positive tax)',shielded.afterTaxIrrL<shielded.irrL,
    (shielded.afterTaxIrrL*100).toFixed(2)+'% vs '+(shielded.irrL*100).toFixed(2)+'%');}

console.log('--- After-tax: zero-rate equivalence ---');
{const d=computeDeal(base({tax:{enabled:true,landPct:0.20,depreciationYears:39,ordinaryRate:0,capGainsRate:0,recaptureRate:0}}));
 ok('T32 zero tax rates -> after-tax IRR == before-tax IRR',near(d.afterTaxIrrL,d.irrL,1e-9),d.afterTaxIrrL+' vs '+d.irrL);
 ok('T32 zero tax rates -> sale tax 0',near(d.taxOnSale,0,1e-9),d.taxOnSale);
 ok('T32 zero tax rates -> after-tax EM == before-tax EM',near(d.afterTaxEmL,d.emL,1e-9),d.afterTaxEmL+' vs '+d.emL);}

console.log('\n'+pass+' passed, '+fail+' failed.');process.exit(fail?1:0);
