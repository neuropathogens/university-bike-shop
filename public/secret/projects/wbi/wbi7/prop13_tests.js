/* WBI7 — tests for California Prop 13 property-tax reassessment. On a change of ownership
   the property is reassessed to the purchase price, so with reassessment on the property-tax
   line is computed as effective rate x price (not the seller's basis / manual amount), it
   scales with any price change, and its growth is capped at the 2% Prop 13 limit. With
   reassessment off it falls back to the manual amount (static in price). The tax line is
   designated by an isTax flag or a Prop 13 / property-tax name. Critically, when the manual
   amount already equals rate x price (as the shipped presets are built), reassess-on and
   reassess-off produce the identical result — which is why the presets stay byte-identical. */
const fs=require('fs'),vm=require('vm');
const html=fs.readFileSync(__dirname+'/index.html','utf8');
const a=html.indexOf('/* ===================== WBI7 ENGINE START');
const b=html.indexOf('WBI7 ENGINE END ===================== */');
const ctx={console};vm.createContext(ctx);
vm.runInContext(html.slice(a,b+'WBI7 ENGINE END ===================== */'.length),ctx);
const {computeDeal}=ctx;
let pass=0,fail=0;
const ok=(n,c,x)=>{c?pass++:fail++;console.log((c?'  PASS  ':'  FAIL  ')+n+(c?'':'  -> '+x));};
const near=(a,b,e)=>Math.abs(a-b)<=(e==null?1:e);
// analytical year-1 sum of a fixed expense escalating continuously at g
function yr1(annualBase,g){let s=0;for(let m=0;m<12;m++)s+=annualBase/12*Math.pow(1+g,m/12);return s;}

function mkDeal(over){const taxLine=Object.assign({name:"Property taxes (Prop 13)",basis:"fixed",amount:1,growth:0.02,recoverable:false,varOcc:false,isTax:true},(over&&over.__tax)||{});
  const m=Object.assign({version:'wbi7-1',
  analysis:{holdMonths:72,discountRate:0.08,creditLoss:0,inflation:0.025},
  acquisition:{price:10000000,closingPct:0.02,reassess:true,taxRate:0.012},
  capex:[],property:{suites:[{id:'S1',name:'U1',sf:100000}]},
  mlas:[{id:'M1',name:'flex',marketRent:1.2,rentGrowth:0.03,termMonths:120,renewalProb:0.7,downtimeMonths:6,
    freeNew:0,freeRenew:0,tiNew:0,tiRenew:0,lcNew:0,lcRenew:0,escalation:{type:'fixedPct',value:0.03},recMethod:'net',recParam:100}],
  rentRoll:[{id:'L1',tenant:'A',suiteId:'S1',sf:100000,startMonth:-6,termMonths:120,baseRent:1.2,escalation:{type:'fixedPct',value:0.03},freeMonths:0,recMethod:'net',recParam:100,mlaId:'M1',uponExpiry:'market'}],
  absorption:[],expenses:[taxLine],
  recoverySettings:{grossUpOn:false,grossUpPct:0.95,adminFee:0},otherIncome:{amount:0,growth:0},
  debt:{type:'amount',ltv:0,amount:0,rate:0.05,ioMonths:0,amortMonths:360,mezz:{amount:0,rate:0}},
  exit:{exitCap:0.07,sellCostPct:0.02},equity:{lpShare:1,pref:0,promote:0}},over);
  delete m.__tax;return m;}

console.log('--- Prop 13 reassessment ---');

// 1. reassess on: year-1 tax = rate x price (manual amount ignored)
{const m=mkDeal({__tax:{amount:999999}}); const d=computeDeal(m);
 const expect=yr1(0.012*10000000,0.02);
 ok('reassess on computes year-1 tax as rate x price (manual amount ignored)',near(d.annual[0].exp,expect),d.annual[0].exp.toFixed(2)+' vs '+expect.toFixed(2));}

// 2. tax scales linearly with price
{const base=computeDeal(mkDeal()).annual[0].exp;
 const dbl=computeDeal(mkDeal({acquisition:{price:20000000,closingPct:0.02,reassess:true,taxRate:0.012}})).annual[0].exp;
 ok('reassessed tax scales linearly with purchase price',near(dbl,base*2,1),dbl.toFixed(0)+' vs '+(base*2).toFixed(0));}

// 3. reassess off: tax = manual amount, independent of price
{const off=mkDeal({__tax:{amount:120000},acquisition:{price:10000000,closingPct:0.02,reassess:false,taxRate:0.012}});
 const offHi=mkDeal({__tax:{amount:120000},acquisition:{price:50000000,closingPct:0.02,reassess:false,taxRate:0.012}});
 const e1=computeDeal(off).annual[0].exp,e2=computeDeal(offHi).annual[0].exp;
 ok('reassess off uses the manual amount',near(e1,yr1(120000,0.02)),e1.toFixed(0));
 ok('reassess off tax does not change with price',near(e1,e2),'changed with price');}

// 4. 2% Prop 13 cap binds even if the line growth is higher
{const capped=mkDeal({__tax:{amount:1,growth:0.06}}); // reassess on -> growth capped at 2%
 const dC=computeDeal(capped);
 const expectY5=yr1(0.012*10000000,0.02)*Math.pow(1.02,4)/1; // year-5 base ~ rate*price grown 4y at 2%
 // compare year-5 tax to a 2%-grown expectation (within a tolerance for intra-year compounding)
 const y5=dC.annual[4].exp, ref2=yr1(0.012*10000000*Math.pow(1.02,4),0.02);
 ok('reassessment caps tax growth at 2% even when the line asks for more',near(y5,ref2,2),y5.toFixed(0)+' vs '+ref2.toFixed(0));}

// 5. byte-identical equivalence: manual amount = rate x price, growth 2% -> on == off
{const onM=mkDeal({__tax:{amount:115000,growth:0.02},acquisition:{price:10000000,closingPct:0.02,reassess:true,taxRate:0.0115}});
 const offM=mkDeal({__tax:{amount:115000,growth:0.02},acquisition:{price:10000000,closingPct:0.02,reassess:false,taxRate:0.0115}});
 // 1.15% x 10,000,000 = 115,000 == manual amount, so identical
 ok('when manual amount already equals rate x price, on and off are identical (presets stay byte-identical)',
    near(computeDeal(onM).annual[0].noi,computeDeal(offM).annual[0].noi,1e-6),'');}

// 6. designation by Prop 13 / property-tax name (no isTax flag)
{const byName=mkDeal({__tax:{name:"Property Taxes",isTax:false,amount:1}});
 ok('a property-tax-named line is reassessed without an explicit flag',
    near(computeDeal(byName).annual[0].exp,yr1(0.012*10000000,0.02)),'');}

// 7. designation by isTax flag (generic name)
{const byFlag=mkDeal({__tax:{name:"Taxes",isTax:true,amount:1}});
 ok('a generically-named line with the isTax flag is reassessed',
    near(computeDeal(byFlag).annual[0].exp,yr1(0.012*10000000,0.02)),'');}
{const neither=mkDeal({__tax:{name:"Misc",isTax:false,amount:77000}});
 ok('a non-tax line is left as a manual expense',near(computeDeal(neither).annual[0].exp,yr1(77000,0.02)),'');}

// 8. recoverable reassessed tax still flows into recoveries (NNN)
{const rec=mkDeal({__tax:{recoverable:true,amount:1}});
 const noRec=mkDeal({__tax:{recoverable:false,amount:1}});
 ok('a recoverable reassessed tax raises recoveries vs the same tax non-recoverable',
    computeDeal(rec).annual[0].rec>computeDeal(noRec).annual[0].rec,'');}

// 9. immutability
{const m=mkDeal();const before=JSON.stringify(m);computeDeal(m);computeDeal(m);
 ok('computing the deal never mutates the model',JSON.stringify(m)===before,'model changed');}

console.log('\n'+pass+' passed, '+fail+' failed.');
process.exit(fail?1:0);
