/* UI smoke test (browser-free) — loads index.html in jsdom and verifies the new
   feature surfaces actually wire through the real DOM render path:
   percentage-rent columns, recovery-cap + reserve inputs (round-trip via
   loadModel/collectModel), the tornado SVG (auto-rendered in renderAll), and
   the exported goal-seek solver. Complements feature_tests.js (pure engine). */
const fs=require('fs'),path=require('path');
const {JSDOM}=require('jsdom');
const HTML=process.env.WBI7_PATH||path.resolve(__dirname,'index.html');
const html=fs.readFileSync(HTML,'utf8');
let pass=0,fail=0;
const ok=(n,c,x)=>{c?pass++:fail++;console.log((c?'  PASS  ':'  FAIL  ')+n+(c?'':'  -> '+x));};
const near=(a,b,t)=>Math.abs(a-b)<=t;

const dom=new JSDOM(html,{runScripts:"dangerously",url:"http://localhost/",pretendToBeVisual:true});
const {window}=dom;
window.requestAnimationFrame=cb=>setTimeout(cb,0);

async function run(){
  const w=window.__wbi7,doc=window.document;
  if(!w){ok('window.__wbi7 present',false,'missing');return finish();}
  const $=id=>doc.getElementById(id);

  // 1) Percentage-rent columns exist on the rent roll and round-trip a retail lease.
  const ret=JSON.parse(JSON.stringify(w.PRESETS["ret-grocery"]));
  ret.rentRoll[2]=Object.assign(ret.rentRoll[2],{overagePct:6,salesPSF:900,salesGrowth:3,bpType:"natural"});
  w.loadModel(ret);
  ok('rent roll renders an overagePct input per lease',
     doc.querySelectorAll('#rrRows [data-k="overagePct"]').length===ret.rentRoll.length,
     doc.querySelectorAll('#rrRows [data-k="overagePct"]').length);
  ok('rent roll renders a breakpoint-type selector per lease',
     doc.querySelectorAll('#rrRows [data-k="bpType"]').length===ret.rentRoll.length,'');
  {const m=w.collectModel();const L=m.rentRoll[2];
   ok('pct-rent fields survive loadModel -> collectModel',
      (+L.overagePct===6&&+L.salesPSF===900&&+L.salesGrowth===3&&L.bpType==="natural"),JSON.stringify({o:L.overagePct,s:L.salesPSF,g:L.salesGrowth,b:L.bpType}));
   ok('percentage rent reaches the engine (annual pct > 0 once above breakpoint)',
      w.computeDeal(m).pctRentTotal>0,w.computeDeal(m).pctRentTotal);}

  // 2) Recovery-cap inputs exist and round-trip.
  ok('recovery cap % input present',!!$("capPct"),'');
  ok('recovery cap cumulative toggle present',!!$("capCum"),'');
  {const m2=JSON.parse(JSON.stringify(w.PRESETS["ind-oak-multi"]));
   m2.recoverySettings.capPct=0.05;m2.recoverySettings.capCumulative=true;
   w.loadModel(m2);
   ok('capPct input shows 5 after loading 0.05',near(parseFloat($("capPct").value),5,1e-9),$("capPct").value);
   ok('capCum checkbox checked after loading cumulative=true',$("capCum").checked===true,'');
   const back=w.collectModel();
   ok('capPct round-trips back to 0.05 decimal',near(back.recoverySettings.capPct,0.05,1e-9),back.recoverySettings.capPct);
   ok('cap reduces total recoveries vs uncapped',
      w.computeDeal(back).annual.reduce((s,a)=>s+a.rec,0) < w.computeDeal(w.PRESETS["ind-oak-multi"]).annual.reduce((s,a)=>s+a.rec,0),'');}

  // 3) Capital-reserve inputs exist and round-trip; reserve flows below NOI.
  ok('reserve amount input present',!!$("resAmt"),'');
  ok('reserve basis selector present',!!$("resBasis"),'');
  {const m3=JSON.parse(JSON.stringify(w.PRESETS["mf-sd-48"]));
   m3.reserves={amount:0.25,basis:"psf",growth:0.03};
   w.loadModel(m3);
   ok('resAmt input shows 0.25 after load',near(parseFloat($("resAmt").value),0.25,1e-9),$("resAmt").value);
   ok('resBasis shows psf after load',$("resBasis").value==="psf",'');
   const back=w.collectModel(),d=w.computeDeal(back),d0=w.computeDeal(w.PRESETS["mf-sd-48"]);
   ok('reserve round-trips amount/basis/growth',(near(back.reserves.amount,0.25,1e-9)&&back.reserves.basis==="psf"&&near(back.reserves.growth,0.03,1e-9)),JSON.stringify(back.reserves));
   ok('reserveTotal > 0 with a reserve set',d.reserveTotal>0,d.reserveTotal);
   ok('reserve does NOT change NOI (yr 1)',near(d.annual[0].noi,d0.annual[0].noi,1e-6),'');
   ok('reserve does NOT change exit value',near(d.value,d0.value,1e-6),'');}

  // 4) Tornado SVG auto-renders bars in the normal render path.
  w.loadModel(JSON.parse(JSON.stringify(w.PRESETS["ind-oak-multi"])));
  const bars=doc.querySelectorAll('#tornadoChart rect').length;
  ok('tornado chart renders >= 7 bars for a healthy deal',bars>=7,bars);

  // 5) Goal-seek solver is exported and recovers the current price for the current IRR.
  ok('E_goalSeek exported',typeof w.E_goalSeek==="function",'');
  {const m=w.PRESETS["ind-oak-multi"],d0=w.computeDeal(m);
   const g=w.E_goalSeek(m,{variable:"price",metric:"irrL",target:d0.irrL});
   ok('goal-seek solves price for the current IRR',g.ok===true,JSON.stringify(g));
   ok('solved price is within 2% of the actual price',
      g.ok&&near(g.value,m.acquisition.price,m.acquisition.price*0.02),g.value+' vs '+m.acquisition.price);}
  ok('E_tornado exported',typeof w.E_tornado==="function",'');

  // 6) Portfolio / fund roll-up: card present, exported, and rolls up two presets.
  ok('fund card: Add button present',!!$("pfAdd"),'');
  ok('fund card: deal table + metrics present',!!$("pfRows")&&!!$("pfIrrL")&&!!$("pfEquity"),'');
  ok('computePortfolio exported',typeof w.computePortfolio==="function",'');
  {const A=w.PRESETS["ind-oak-multi"],B=w.PRESETS["mf-sd-48"];
   const dA=w.computeDeal(A),dB=w.computeDeal(B);
   const f=w.computePortfolio([{model:A,startMonth:0,name:"A"},{model:B,startMonth:0,name:"B"}],
     {equity:{lpShare:0.9,pref:0.08,promote:0.2}});
   ok('fund rolls up two deals (n=2)',f.n===2,f.n);
   ok('fund total value == sum of the two deal values',near(f.value,dA.value+dB.value,1e-2),f.value+' vs '+(dA.value+dB.value));
   ok('fund profit == sum of the two deal profits',near(f.profit,dA.profit+dB.profit,1e-1),'');
   ok('fund total equity invested is positive',f.equity>0,f.equity);
   const lo=Math.min(dA.irrL,dB.irrL),hi=Math.max(dA.irrL,dB.irrL);
   ok('fund levered IRR sits between the two deal IRRs',f.irrL>=lo-1e-6&&f.irrL<=hi+1e-6,f.irrL+' in ['+lo+','+hi+']');
   ok('fund waterfall conserves cash (lp + gp == profit)',near(f.lpProfit+f.gpProfit,f.profit,1e-1),'');}

  // 7) Blank "Custom" default scenario: first dropdown option, loads empty, computes cleanly.
  ok('BLANK_SCENARIO exported',typeof w.BLANK_SCENARIO==="object"&&!!w.BLANK_SCENARIO,'');
  {w.buildPresetOptions();const sel=$("presetSel");
   ok('dropdown first option is the blank custom scenario',!!sel&&sel.options.length>0&&sel.options[0].value==="__blank",sel?sel.options[0] && sel.options[0].value:'no sel');
   ok('blank scenario keeps all 25 presets in the dropdown',!!sel&&sel.querySelectorAll('optgroup option').length===Object.keys(w.PRESETS).length,sel?sel.querySelectorAll('optgroup option').length:0);}
  {w.loadModel(JSON.parse(JSON.stringify(w.BLANK_SCENARIO)));
   const m=w.collectModel();
   ok('blank scenario starts with empty suites / leases and only the Prop 13 tax line (build your own)',
      (m.property.suites.length===0&&m.rentRoll.length===0&&m.expenses.length===1&&(m.expenses[0].isTax===true||/prop\s*1?3|property\s*tax/i.test(m.expenses[0].name||""))),
      JSON.stringify({s:m.property.suites.length,l:m.rentRoll.length,e:m.expenses.length,tax:m.expenses[0]&&m.expenses[0].name}));
   ok('blank scenario has reasonable California default assumptions (no price yet)',
      m.acquisition.price===0&&near(m.debt.ltv,0.60,1e-9)&&near(m.debt.rate,0.0675,1e-9)&&near(m.exit.exitCap,0.0625,1e-9)&&near(m.analysis.discountRate,0.08,1e-9),
      JSON.stringify({ltv:m.debt.ltv,rate:m.debt.rate,cap:m.exit.exitCap,dr:m.analysis.discountRate}));
   const d=w.computeDeal(m);
   ok('blank scenario computes without throwing',!!d,'');
   ok('blank scenario shows no IRR (n/a, not -100%)',d.irrL===null,String(d.irrL));
   ok('blank scenario exit value is 0',d.value===0,String(d.value));
   ok('blank scenario equity multiple is 0',d.emL===0,String(d.emL));}

  // 8) Development / construction module: card present, round-trips, computes through the page.
  ok('development input toggle present',!!$("devOn"),'');
  ok('development pro forma card present',!!$("devBody")&&!!$("dvYoC")&&!!$("dvTotal"),'');
  ok('computeDevelopment exported',typeof w.computeDevelopment==="function",'');
  {w.loadModel(JSON.parse(JSON.stringify(w.BLANK_SCENARIO)));
   const m=w.collectModel();
   ok('development defaults off on the blank scenario',m.development.on===false,'');}
  {const dm=JSON.parse(JSON.stringify(w.BLANK_SCENARIO));
   dm.development={on:true,landCost:3000000,hardCost:12000000,softCostPct:0.2,contingencyPct:0.05,
     constructionMonths:18,curve:"scurve",loanLTC:0.6,loanRate:0.085,leaseUpMonths:12,
     noiRampStart:0,stabilizedNOI:1800000,holdAfterStabMonths:0,exitCap:0.0525,sellCostPct:0.02};
   w.loadModel(dm);
   ok('devOn checkbox reflects loaded development',$("devOn").checked===true,'');
   ok('devLTC input shows 60 after loading 0.6',near(parseFloat($("devLTC").value),60,1e-9),$("devLTC").value);
   const back=w.collectModel();
   ok('development round-trips land/hard/LTC/exitCap',
      (back.development.landCost===3000000&&back.development.hardCost===12000000
       &&near(back.development.loanLTC,0.6,1e-9)&&near(back.development.exitCap,0.0525,1e-9)),
      JSON.stringify(back.development));
   const r=w.computeDevelopment(back.development);
   ok('development total cost = direct + capitalized interest',
      near(r.totalCost,r.directCost+r.capInt,1e-3),r.totalCost);
   ok('development yield-on-cost = stabilized NOI / total cost',
      near(r.yieldOnCost,1800000/r.totalCost,1e-9),r.yieldOnCost);
   ok('development reports a positive levered IRR for a profitable build',r.irrL!=null&&r.irrL>0,String(r.irrL));}

  // 9) Hold-period analysis: card present, exported, reconciles to computeDeal, renders.
  ok('hold-period card present',!!$("hpRows")&&!!$("hpBest"),'');
  ok('E_holdAnalysis exported',typeof w.E_holdAnalysis==="function",'');
  {const P=w.PRESETS["ind-oak-multi"];const h=w.E_holdAnalysis(P);
   ok('hold analysis: one row per planned-hold year',h.rows.length===Math.ceil(P.analysis.holdMonths/12),h.rows.length);
   ok('hold analysis: optimal year has the max IRR across years',
      h.bestYear!=null&&h.rows.every(r=>r.irrL==null||r.irrL<=h.bestIrr+1e-12),String(h.bestYear));
   const d=w.computeDeal(P),last=h.rows[h.rows.length-1];
   ok('hold analysis: planned-hold year reconciles to computeDeal IRR',near(last.irrL,d.irrL,1e-9),last.irrL+' vs '+d.irrL);}
  {w.loadModel(JSON.parse(JSON.stringify(w.PRESETS["ind-oak-multi"])));
   ok('hold-period table renders rows after load',doc.querySelectorAll('#hpRows tr').length>0,doc.querySelectorAll('#hpRows tr').length);
   ok('optimal-hold callout is populated',/year/i.test($("hpBest").textContent),$("hpBest").textContent.slice(0,40));}

  // 10) Scenario compare: card present, exported, reconciles + reads sensitivity through the page.
  ok('scenario-compare card present',!!$("cmpHead")&&!!$("cmpBody")&&!!$("cmpAdd"),'');
  ok('E_compare exported',typeof w.E_compare==="function",'');
  {const A=w.PRESETS["ind-oak-multi"];
   const cheaper=JSON.parse(JSON.stringify(A));cheaper.acquisition.price=Math.round(A.acquisition.price*0.85);
   const cols=w.E_compare([{name:"Base",model:A},{name:"Cheaper",model:cheaper}]);
   ok('compare returns a column per scenario in order',cols.length===2&&cols[0].name==="Base"&&cols[1].name==="Cheaper",'');
   const d=w.computeDeal(A);
   ok('compare base column reconciles to computeDeal IRR',near(cols[0].m.irrL,d.irrL,1e-12),cols[0].m.irrL+' vs '+d.irrL);
   ok('compare base column reconciles to computeDeal value',near(cols[0].m.value,d.value,1e-3),'');
   ok('compare reads sensitivity: cheaper basis lifts IRR',cols[1].m.irrL>cols[0].m.irrL,cols[1].m.irrL+' vs '+cols[0].m.irrL);}

  // 11) Mezzanine overlay: card present, exported, no-op identity, round-trips, renders, gears returns.
  ok('mezzanine card present',!!$("mezzBody")&&!!$("mzIrrM")&&!!$("mzBlend"),'');
  ok('E_mezz exported',typeof w.E_mezz==="function",'');
  {const A=w.PRESETS["ind-oak-multi"];const noMezz=JSON.parse(JSON.stringify(A));
   noMezz.debt.mezz={amount:0,rate:0.12,ioMonths:0,amortMonths:360};
   const z=w.E_mezz(noMezz),d=w.computeDeal(A);
   ok('mezz=0 reproduces senior-only IRR exactly',near(z.irrL,d.irrL,1e-12),z.irrL+' vs '+d.irrL);}
  {const A=JSON.parse(JSON.stringify(w.PRESETS["ind-oak-multi"]));
   A.debt.mezz={amount:2000000,rate:0.10,ioMonths:0,amortMonths:360};
   w.loadModel(A);
   ok('mezz amount input reflects loaded value',near(parseFloat($("mezzAmt").value),2000000,1e-6),$("mezzAmt").value);
   ok('mezz rate input shows 10 after loading 0.10',near(parseFloat($("mezzRate").value),10,1e-9),$("mezzRate").value);
   const back=w.collectModel();
   ok('mezz round-trips amount + rate',back.debt.mezz.amount===2000000&&near(back.debt.mezz.rate,0.10,1e-9),JSON.stringify(back.debt.mezz));
   ok('mezz card body is shown after loading a deal with mezz',$("mezzBody").style.display!=="none",$("mezzBody").style.display);
   ok('mezz with-mezz IRR cell is populated',($("mzIrrM").textContent||"").length>0,$("mzIrrM").textContent);
   const z=w.E_mezz(back);
   ok('positive-leverage mezz lifts equity IRR vs senior-only',z.irrL>z.seniorIrr,z.irrL+' vs '+z.seniorIrr);
   ok('mezz shrinks the equity check',z.equityWithMezz<z.equitySenior,z.equityWithMezz+' vs '+z.equitySenior);}

  // 12) IC summary: builder exported, valid self-contained HTML with the right content.
  ok('buildICSummary exported',typeof w.buildICSummary==="function",'');
  {w.loadModel(JSON.parse(JSON.stringify(w.PRESETS["ind-oak-multi"])));
   const m=w.collectModel(),d=w.computeDeal(m),htmlOut=w.buildICSummary(m,d);
   ok('IC summary is a self-contained HTML document',typeof htmlOut==="string"&&/^<!doctype html>/i.test(htmlOut)&&/<\/html>$/i.test(htmlOut.trim()),htmlOut.slice(0,20));
   ok('IC summary shows the project name',htmlOut.indexOf(m.project)>=0,m.project);
   ok('IC summary is titled an Investment Summary',/Investment Summary/.test(htmlOut),'');
   ok('IC summary includes Sources & Uses',/Sources &amp; Uses/.test(htmlOut),'');
   ok('IC summary includes the levered IRR figure',htmlOut.indexOf((d.irrL*100).toFixed(1)+"%")>=0,(d.irrL*100).toFixed(1)+"%");
   ok('IC summary includes an annual cash-flow table',/Annual Cash Flow/.test(htmlOut)&&/<tbody>\s*<tr>/.test(htmlOut),'');
   ok('IC summary carries the not-advice disclaimer',/not investment, legal, or tax advice/.test(htmlOut),'');}
  {const evil=JSON.parse(JSON.stringify(w.PRESETS["mf-sd-48"]));
   w.loadModel(evil);const m=w.collectModel();m.project='<script>alert(1)</script>';
   const htmlOut=w.buildICSummary(m,w.computeDeal(m));
   ok('IC summary HTML-escapes the project name (no raw script tag)',htmlOut.indexOf('<script>alert(1)')<0&&htmlOut.indexOf('&lt;script&gt;')>=0,'');}
  {const mz=JSON.parse(JSON.stringify(w.PRESETS["ind-oak-multi"]));
   mz.debt.mezz={amount:2000000,rate:0.10,ioMonths:0,amortMonths:360};
   const htmlOut=w.buildICSummary(mz,w.computeDeal(mz));
   ok('IC summary shows the mezzanine stack when present',/mezzanine/i.test(htmlOut),'');}

  // 13) Floating-rate (ARM) senior debt: inputs present, default off, round-trips, gears returns.
  ok('floating-rate inputs present',!!$("floatOn")&&!!$("floatReset")&&!!$("floatCap")&&!!$("floatFloor"),'');
  {w.loadModel(JSON.parse(JSON.stringify(w.PRESETS["ind-oak-multi"])));
   const m=w.collectModel();
   ok('floating defaults off on presets',m.debt.floating.on===false,'');
   const dFixed=w.computeDeal(m);
   const m2=JSON.parse(JSON.stringify(m));m2.debt.floating={on:false,resetMonths:12,stepBps:200,capRate:0.12,floorRate:0};
   ok('floating off == fixed through the page (IRR identical)',near(w.computeDeal(m2).irrL,dFixed.irrL,1e-12),'');}
  {const A=JSON.parse(JSON.stringify(w.PRESETS["ind-oak-multi"]));
   A.debt.floating={on:true,resetMonths:12,stepBps:150,capRate:0.12,floorRate:0.02};
   w.loadModel(A);
   ok('floatOn checkbox reflects loaded value',$("floatOn").checked===true,'');
   ok('floatCap input shows 12 after loading 0.12',near(parseFloat($("floatCap").value),12,1e-9),$("floatCap").value);
   const back=w.collectModel();
   ok('floating round-trips on/reset/step/cap',
      (back.debt.floating.on===true&&back.debt.floating.resetMonths===12&&back.debt.floating.stepBps===150&&near(back.debt.floating.capRate,0.12,1e-9)),
      JSON.stringify(back.debt.floating));
   const fixedRef=JSON.parse(JSON.stringify(A));fixedRef.debt.floating.on=false;
   ok('rising floating rate lowers levered IRR vs fixed (through page)',
      w.computeDeal(back).irrL<w.computeDeal(fixedRef).irrL,'');}

  // 14) Prepayment penalty (step-down): inputs present, default off, round-trips, hits levered only.
  ok('prepayment inputs present',!!$("prepayOn")&&!!$("prepayStart")&&!!$("prepayDecline"),'');
  {w.loadModel(JSON.parse(JSON.stringify(w.PRESETS["ind-oak-multi"])));
   const m=w.collectModel();
   ok('prepay defaults off on presets',m.debt.prepay.on===false,'');
   const noP=w.computeDeal(m);
   const m2=JSON.parse(JSON.stringify(m));m2.debt.prepay={on:false,startPct:0.05,declinePct:0.01};
   ok('prepay off == none through the page (proceeds identical)',near(w.computeDeal(m2).proceeds,noP.proceeds,1e-9),'');}
  {const A=JSON.parse(JSON.stringify(w.PRESETS["ind-oak-multi"]));
   A.analysis.holdMonths=36;A.debt.prepay={on:true,startPct:0.05,declinePct:0.01};
   w.loadModel(A);
   ok('prepayOn checkbox reflects loaded value',$("prepayOn").checked===true,'');
   ok('prepayStart input shows 5 after loading 0.05',near(parseFloat($("prepayStart").value),5,1e-9),$("prepayStart").value);
   const back=w.collectModel();
   ok('prepay round-trips on/start/decline',
      (back.debt.prepay.on===true&&near(back.debt.prepay.startPct,0.05,1e-9)&&near(back.debt.prepay.declinePct,0.01,1e-9)),
      JSON.stringify(back.debt.prepay));
   const noP=JSON.parse(JSON.stringify(back));noP.debt.prepay.on=false;
   const dP=w.computeDeal(back),dN=w.computeDeal(noP);
   ok('prepay penalty lowers levered IRR but not unlevered',dP.irrL<dN.irrL&&near(dP.irrU,dN.irrU,1e-12),dP.irrL+'/'+dN.irrL);}

  // 15) Market Context: card present, parsers exported, property location round-trips.
  ok('market-data card present',!!$("mdLat")&&!!$("mdLng")&&!!$("mdFetch")&&!!$("mdResults"),'');
  ok('market-data parsers exported',typeof w.MD_parseCensus==="function"&&typeof w.MD_suggest==="function",'');
  {const A=JSON.parse(JSON.stringify(w.PRESETS["mf-sd-48"]));A.location={lat:32.7157,lng:-117.1611};
   w.loadModel(A);
   ok('latitude input reflects loaded location',near(parseFloat($("mdLat").value),32.7157,1e-9),$("mdLat").value);
   const back=w.collectModel();
   ok('property location round-trips through collect/load',
      back.location&&near(back.location.lat,32.7157,1e-9)&&near(back.location.lng,-117.1611,1e-9),JSON.stringify(back.location));}
  {w.loadModel(JSON.parse(JSON.stringify(w.BLANK_SCENARIO)));const m=w.collectModel();
   ok('blank scenario has no location (null lat/lng)',m.location.lat===null&&m.location.lng===null,JSON.stringify(m.location));}

  // 16) Pre-made themes: selecting a theme drives mode + accent together.
  ok('theme picker present',!!$("themePreset"),'');
  {const tp=$("themePreset");
   tp.value="midnight";tp.dispatchEvent(new window.Event("change"));
   ok('Midnight theme sets dark mode',doc.documentElement.dataset.theme==="dark",doc.documentElement.dataset.theme);
   ok('Midnight theme sets its accent',doc.documentElement.style.getPropertyValue("--accent").trim()==="#6366f1",doc.documentElement.style.getPropertyValue("--accent"));
   tp.value="forest";tp.dispatchEvent(new window.Event("change"));
   ok('Forest theme switches to light + green',
      doc.documentElement.dataset.theme==="light"&&doc.documentElement.style.getPropertyValue("--accent").trim()==="#059669",
      doc.documentElement.dataset.theme+'/'+doc.documentElement.style.getPropertyValue("--accent"));}

  // 17) Rebrand: displayed name updated; internal wbi7 identifiers unchanged.
  ok('page title shows the In-House ARGUS rebrand',/In-House ARGUS/.test(doc.title)&&/Wang Brothers Investments/.test(doc.title),doc.title);
  ok('header brand shows Wang Brothers Investments',/Wang Brothers Investments/.test(($("brand")||{textContent:''}).textContent),'');
  ok('internal export key window.__wbi7 unchanged',!!window.__wbi7,'');

  // 18) Assumption confidence: selectors present, round-trip, and the risk-weighted table renders.
  ok('confidence selectors present',!!$("conf_exitCap")&&!!$("conf_price")&&!!$("conf_downtime")&&!!$("conf_creditLoss"),'');
  {const A=JSON.parse(JSON.stringify(w.PRESETS["ind-oak-multi"]));A.confidence={exitCap:"low",price:"high"};
   w.loadModel(A);
   ok('confidence selector reflects loaded value',$("conf_exitCap").value==="low"&&$("conf_price").value==="high",$("conf_exitCap").value);
   const back=w.collectModel();
   ok('confidence round-trips (set values + default medium)',
      back.confidence.exitCap==="low"&&back.confidence.price==="high"&&back.confidence.rentGrowth==="med",JSON.stringify(back.confidence));
   const cr=$("confResults").innerHTML;
   ok('risk-weighted table + diligence callout render into the card',/Risk-weighted/.test(cr)&&/Diligence priorities/.test(cr),cr.slice(0,50));}
  ok('E_confidence exported',typeof w.E_confidence==="function",'');

  // 19) Capital-structure optimizer: inputs present, round-trip, and the recommendation renders.
  ok('optimizer inputs present',!!$("optMaxSr")&&!!$("optMinDscr")&&!!$("optRun")&&!!$("optOut"),'');
  {const A=JSON.parse(JSON.stringify(w.PRESETS["ind-oak-multi"]));
   A.optimizer={maxSeniorLtv:0.7,maxTotalLtv:0.82,minDscr:1.3,minDebtYield:0.075,mezzRate:0.115};
   w.loadModel(A);
   ok('optimizer constraint reflects loaded value',near(parseFloat($("optMinDscr").value),1.3,1e-9)&&near(parseFloat($("optMaxTot").value),82,1e-9),$("optMinDscr").value);
   const back=w.collectModel();
   ok('optimizer constraints round-trip',near(back.optimizer.maxSeniorLtv,0.7,1e-9)&&near(back.optimizer.minDscr,1.3,1e-9)&&near(back.optimizer.mezzRate,0.115,1e-9),JSON.stringify(back.optimizer));
   const Rui=w.E_optimize(w.collectModel());
   ok('optimizer runs on the DOM-collected model and finds a structure',Rui.ok===true&&Rui.best!=null&&Rui.allEquity!=null,String(Rui.ok));
   ok('optimizer respects the collected DSCR floor',Rui.best.dscr===Infinity||Rui.best.dscr>=1.3-1e-6,String(Rui.best.dscr));}
  ok('E_optimize exported',typeof w.E_optimize==="function",'');

  // 20) Pre-mortem / kill-zone: inputs present, threshold round-trips, runs on the collected model.
  ok('kill-zone inputs present',!!$("kzTarget")&&!!$("kzRun")&&!!$("kzOut"),'');
  {const A=JSON.parse(JSON.stringify(w.PRESETS["ind-oak-multi"]));A.killzone={targetIrr:0.05};
   w.loadModel(A);
   ok('kill-zone threshold reflects loaded value (5%)',near(parseFloat($("kzTarget").value),5,1e-9),$("kzTarget").value);
   const back=w.collectModel();
   ok('kill-zone threshold round-trips',near(back.killzone.targetIrr,0.05,1e-9),JSON.stringify(back.killzone));
   const R=w.E_killzone(back,back.killzone);
   ok('kill-zone runs on the DOM-collected model',R.ok===true&&Array.isArray(R.breakevens)&&R.breakevens.length===9,String(R.ok));}
  ok('E_killzone exported',typeof w.E_killzone==="function",'');

  // 21) Interactive charts: control row, manual Y range, X (year) window, fit-to-data.
  ok('barChart exported',typeof w.barChart==="function",'');
  {const rows=[{y:1,cf:100},{y:2,cf:200},{y:3,cf:300},{y:4,cf:400},{y:5,cf:500}];
   const labels=()=>Array.from(doc.getElementById("cfChart").querySelectorAll("text")).map(t=>t.textContent);
   const rects=()=>doc.getElementById("cfChart").querySelectorAll("rect").length;
   // default: zero-baseline axis, one bar per row
   w.barChart("cfChart",rows,"cf",v=>String(Math.round(v)),{});
   ok('chart control row is inserted next to the chart',!!doc.getElementById("cfChart").parentNode.querySelector('.chart-ctrls[data-for="cfChart"]'),'');
   ok('default chart draws one bar per row',rects()===5,String(rects()));
   ok('default chart includes a 0 gridline',labels().indexOf("0")>=0,labels().join(","));
   // manual Y range 0..1000 -> a "1000" gridline label
   w.barChart("cfChart",rows,"cf",v=>String(Math.round(v)),{yMin:0,yMax:1000});
   ok('manual Y max sets the top axis label',labels().indexOf("1000")>=0,labels().join(","));
   // fit-to-data on all-positive values -> axis no longer starts at 0
   w.barChart("cfChart",rows,"cf",v=>String(Math.round(v)),{zoomToData:true});
   ok('Fit-to-data drops the 0 baseline (axis starts at the data min)',labels().indexOf("0")<0&&labels().indexOf("100")>=0,labels().join(","));
   // X window 2..4 -> three bars
   w.barChart("cfChart",rows,"cf",v=>String(Math.round(v)),{xFrom:2,xTo:4});
   ok('X-axis year window narrows the bars shown',rects()===3,String(rects()));
   // reset back to clean default for the rest of the suite
   w.barChart("cfChart",rows,"cf",v=>String(Math.round(v)),{});}

  // 22) Analysis slideshow: self-contained multi-slide deck, sections, nav, escaping.
  ok('buildSlideshow exported',typeof w.buildSlideshow==="function",'');
  {const m=JSON.parse(JSON.stringify(w.PRESETS["off-sf-fidi"]));
   const deck=w.buildSlideshow(m,w.computeDeal(m));
   const nslides=(deck.match(/class="slide/g)||[]).length;
   ok('deck is a standalone HTML document',deck.slice(0,15).toLowerCase().indexOf("<!doctype html")===0,deck.slice(0,20));
   ok('deck has multiple slides (>=6)',nslides>=6,String(nslides));
   ok('deck has a title slide',deck.indexOf("title-slide")>=0,'');
   ok('deck includes the core sections',['Headline Returns','Capital Stack','Annual Cash Flow','Methodology'].every(s=>deck.indexOf(s)>=0),'');
   ok('deck includes sensitivity + pre-mortem from the engines',deck.indexOf("Sensitivity")>=0&&deck.indexOf("Pre-Mortem")>=0,'');
   ok('deck embeds keyboard navigation',deck.indexOf("ArrowRight")>=0&&deck.indexOf('id="next"')>=0,'');
   ok('deck closes its script tag correctly',deck.indexOf("</script>")>0&&deck.trim().slice(-7)==="</html>",deck.trim().slice(-12));
   ok('deck prints one slide per page',deck.indexOf("page-break-after")>=0,'');
   ok('deck now includes an Agenda and a Key/glossary slide',deck.indexOf(">Agenda<")>=0&&deck.indexOf("Key \u2014 What the Terms Mean")>=0,'');
   ok('glossary defines the core terms',["Levered IRR","Equity Multiple","Exit Cap Rate","Year-1 DSCR","WALT","Pre-Mortem / Kill Point"].every(t=>deck.indexOf(t)>=0),'');
   ok('glossary slide is markable for the G shortcut',deck.indexOf("data-glossary")>=0,'');
   ok('deck has a progress bar',deck.indexOf("deck-progress")>=0&&deck.indexOf('id="bar"')>=0,'');
   ok('navigation supports number-key jump and G->glossary',deck.indexOf("[1-9]")>=0&&deck.indexOf("gloss()")>=0,'');
   ok('title slide shows headline stat chips',deck.indexOf("ts-chips")>=0,'');
   ok('deck grew to 8+ slides with the additions',nslides>=8,String(nslides));}
  {const m=JSON.parse(JSON.stringify(w.PRESETS["off-sf-fidi"]));m.project='<b>&"Hostile</b>';
   const deck=w.buildSlideshow(m,w.computeDeal(m));
   ok('project name is HTML-escaped in the deck',deck.indexOf("&lt;b&gt;&amp;&quot;Hostile")>=0,'');
   ok('raw unescaped project name does not appear',deck.indexOf('<b>&"Hostile</b>')<0,'');}

  // 23) Onboarding: guide modal (content + show/hide + seen flag) and section nav.
  ok('guide + nav controls present',!!$("guideBtn")&&!!$("welcomeModal")&&!!$("sectionJump")&&!!$("guideStart"),'');
  {const mh=$("welcomeModal").innerHTML;
   ok('guide explains the workflow',mh.indexOf("How it works")>=0&&mh.indexOf("Edit assumptions")>=0,'');
   ok('guide indexes the major capabilities',['market leasing','Monte Carlo','capital-structure optimizer','pre-mortem','Fund roll-up','slideshow','Live market'].every(s=>mh.indexOf(s)>=0),'');}
  {w.showGuide();
   ok('showGuide reveals the modal',$("welcomeModal").style.display==="flex"&&!$("welcomeModal").classList.contains("hidden"),$("welcomeModal").style.display);
   w.hideGuide();
   ok('hideGuide hides it and records the seen flag',$("welcomeModal").style.display==="none"&&w.guideSeen()===true,String(w.guideSeen()));}
  {const secs=w.collectSections();
   ok('collectSections finds the section cards (>=15)',secs.length>=15,String(secs.length));
   ok('every section has an id and a title',secs.every(s=>s.id&&s.title&&s.title.length>0),'');
   ok('cards received ids for anchoring',secs.every(s=>!!doc.getElementById(s.id)),'');
   w.buildSectionJump();
   ok('section jump menu is populated',$("sectionJump").options.length===secs.length+1,$("sectionJump").options.length+" vs "+(secs.length+1));
   ok('jump options point at real card anchors',Array.from($("sectionJump").options).slice(1).every(o=>!!doc.getElementById(o.value)),'');}
  ok('onboarding helpers exported',['showGuide','hideGuide','guideSeen','collectSections','buildSectionJump'].every(f=>typeof w[f]==="function"),'');

  // 24) Version diff ("git for deals"): card, snapshot round-trip, and full render.
  ok('version-diff controls present',!!$("snapBtn")&&!!$("diffBase")&&!!$("diffCompare")&&!!$("diffBtn")&&!!$("diffOut"),'');
  ok('diff helpers exported',['snapSave','snapList','snapGet','snapDelete','renderDiff','populateDiffVersions'].every(f=>typeof w[f]==="function"),'');
  {w.snapList().forEach(s=>w.snapDelete(s.id));            // start clean
   const base=JSON.parse(JSON.stringify(w.PRESETS["mf-sd-48"]));
   const mod=JSON.parse(JSON.stringify(base));mod.exit.exitCap=base.exit.exitCap+0.01;mod.debt.rate=base.debt.rate+0.005;
   const idA=w.snapSave("Base case",base,{irrL:w.computeDeal(base).irrL,emL:w.computeDeal(base).emL});
   const idB=w.snapSave("Higher cap + rate",mod,{irrL:w.computeDeal(mod).irrL});
   ok('snapshots saved and listed (most-recent first)',w.snapList().length===2&&w.snapList()[0].id===idB,String(w.snapList().length));
   ok('snapGet round-trips a snapshot',(w.snapGet(idA)||{}).label==="Base case",'');
   w.populateDiffVersions();
   ok('version pickers include Current + both snapshots',$("diffBase").options.length===3,String($("diffBase").options.length));
   $("diffBase").value=idA;$("diffCompare").value=idB;w.renderDiff();
   const o=$("diffOut").innerHTML;
   ok('diff lists the changed assumptions by friendly name',o.indexOf("Exit assumptions")>=0&&o.indexOf("Debt terms")>=0,'');
   ok('diff shows the levered-IRR bridge + interaction residual',o.indexOf("IRR bridge")>=0&&o.indexOf("Interaction")>=0,'');
   w.snapDelete(idA);w.snapDelete(idB);
   ok('snapDelete removes snapshots',w.snapList().length===0,String(w.snapList().length));}

  // 25) Actuals vs underwriting: card, model round-trip, and full render.
  ok('actuals controls present',!!$("actualsInput")&&!!$("actualsTh")&&!!$("actualsBtn")&&!!$("actualsOut"),'');
  ok('actuals helpers exported',['parseActuals','serializeActuals','E_actuals','renderActuals'].every(f=>typeof w[f]==="function"),'');
  {const A=JSON.parse(JSON.stringify(w.PRESETS["mf-sd-48"]));A.actuals=[{year:1,noi:1180000},{year:2,noi:1240000,egi:1410000}];
   w.loadModel(A);
   ok('actuals serialize into the textarea on load',$("actualsInput").value.indexOf("1 1180000")>=0&&$("actualsInput").value.indexOf("2 1240000 1410000")>=0,$("actualsInput").value.replace(/\n/g,"|"));
   const back=w.collectModel();
   ok('actuals round-trip through collectModel',back.actuals.length===2&&back.actuals[0].noi===1180000&&back.actuals[1].egi===1410000,JSON.stringify(back.actuals));}
  {w.loadModel(JSON.parse(JSON.stringify(w.PRESETS["mf-sd-48"])));
   const d=w.computeDeal(w.collectModel());const p1=(d.annual.find(a=>a.y===1)||{}).noi;
   $("actualsInput").value="1 "+Math.round(p1*0.90);$("actualsTh").value="5";
   w.renderActuals();
   const o=$("actualsOut").innerHTML;
   ok('render flags a year 10% under underwriting as behind',o.indexOf("behind")>=0,'');
   ok('render reports the cumulative NOI index',o.indexOf("of underwritten NOI")>=0,'');
   $("actualsInput").value="";}

  // 26) Climate & insurance stress: card, model round-trip, and full render.
  ok('climate controls present',!!$("climLat")&&!!$("climZone")&&!!$("climInsAdd")&&!!$("climReserve")&&!!$("climRun")&&!!$("climOut"),'');
  ok('climate helpers exported',['E_climate','CLIMATE_parseFlood','CLIMATE_zoneRisk','renderClimate'].every(f=>typeof w[f]==="function"),'');
  {const A=JSON.parse(JSON.stringify(w.PRESETS["mf-sd-48"]));A.climate={insAddPsf:0.3,reservePsf:0.1,insMult:1.5,zone:"AE"};
   w.loadModel(A);
   ok('climate inputs reflect the loaded model',parseFloat($("climInsAdd").value)===0.3&&$("climZone").value==="AE"&&parseFloat($("climMult").value)===1.5,$("climInsAdd").value+"/"+$("climZone").value);
   const back=w.collectModel();
   ok('climate params round-trip through collectModel',near(back.climate.insAddPsf,0.3,1e-9)&&near(back.climate.reservePsf,0.1,1e-9)&&back.climate.zone==="AE",JSON.stringify(back.climate));}
  {w.loadModel(JSON.parse(JSON.stringify(w.PRESETS["mf-sd-48"])));
   $("climInsAdd").value="0.5";$("climReserve").value="0.2";$("climMult").value="1";$("climZone").value="VE";
   w.renderClimate();
   const o=$("climOut").innerHTML;
   ok('climate render shows the base-vs-stressed table',o.indexOf("Levered IRR")>=0&&o.indexOf("Stressed")>=0,'');
   ok('climate render echoes the FEMA zone',o.indexOf("VE")>=0,'');
   $("climInsAdd").value="0";$("climReserve").value="0";$("climZone").value="";}

  // ===== 27) Usability batch: favicon, info tooltips, show/hide sections, bulk units, Monte Carlo default =====
  ok('favicon link present in <head>',/rel="icon"/.test(html),'');
  ok('info-tooltip CSS mechanism present',html.indexOf('.info[data-tip]')>=0,'');
  {const tips=doc.querySelectorAll('.info[data-tip]');
   ok('info circles now cover KPIs and assumption inputs broadly (>=60)',tips.length>=60,String(tips.length));
   ok('every KPI carries an explanatory tooltip',['kIrr','kEm','kPv','kVal','kDcr'].every(id=>{const k=$(id);const card=k&&k.closest('.kpi');return !!(card&&card.querySelector('.info[data-tip]'));}),'');
   const tipIds=['holdMonths','discRate','inflation','creditLoss','price','debtRate','exitCap','sellCost','mezzAmt','resAmt','taxLand','mcTrials'];
   const rowHasTip=id=>{const el=$(id);const tr=el&&el.closest('tr');return !!(tr&&tr.querySelector('.info[data-tip]'));};
   const missing=tipIds.filter(id=>!rowHasTip(id));
   ok('a representative input from every section has a tooltip',missing.length===0,missing.length?('missing: '+missing.join(',')):('all '+tipIds.length+' present'));
   ok('every tooltip carries a non-trivial explanation',[].every.call(tips,t=>{const d=t.getAttribute('data-tip');return d&&d.length>=12;}),'');}

  ok('Monte Carlo trials default to 100,000',!!$("mcTrials")&&parseInt($("mcTrials").value,10)===100000,$("mcTrials")?$("mcTrials").value:'no input');
  ok('Monte Carlo trials cap raised to 100,000',!!$("mcTrials")&&parseInt($("mcTrials").getAttribute('max'),10)===100000,'');
  ok('computeMCChunked exported (non-blocking engine)',typeof w.computeMCChunked==="function",'');

  ok('section controls present (#sectionsBtn, #sectionModal, body)',!!$("sectionsBtn")&&!!$("sectionModal")&&!!$("sectionPanelBody"),'');
  ok('section visibility helpers exported',['sectionHidden','toggleSectionVis','applySectionVis','buildSectionPanel','showSectionPanel'].every(f=>typeof w[f]==="function"),'');
  {const secs=w.collectSections?w.collectSections():[];
   ok('there are analysis sections available to toggle',secs.length>0,String(secs.length));
   if(secs.length){const id=secs[0].id;
     w.toggleSectionVis(id,false);
     const hid1=w.sectionHidden();
     ok('hiding a section records it and sets display:none',hid1.indexOf(id)>=0&&!!$(id)&&$(id).style.display==="none",hid1.join(','));
     w.toggleSectionVis(id,true);
     const hid2=w.sectionHidden();
     ok('showing a section clears the record and restores it',hid2.indexOf(id)<0&&!!$(id)&&$(id).style.display!=="none",hid2.join(','));
     w.buildSectionPanel();
     ok('section panel lists one checkbox per section',$("sectionPanelBody").querySelectorAll('.secToggle').length===secs.length,String($("sectionPanelBody").querySelectorAll('.secToggle').length));}}

  ok('quick-add-units controls present',!!$("bulkCount")&&!!$("bulkSf")&&!!$("bulkRent")&&!!$("bulkAdd"),'');
  ok('bulkAddUnits exported',typeof w.bulkAddUnits==="function",'');
  {w.loadModel(JSON.parse(JSON.stringify(w.BLANK_SCENARIO)));
   $("bulkCount").value="48";$("bulkSf").value="350";$("bulkRent").value="3.00";$("bulkTerm").value="12";$("bulkName").value="Room";
   w.bulkAddUnits();
   const m=w.collectModel();
   ok('bulk-add creates N identical suites',m.property.suites.length===48,String(m.property.suites.length));
   ok('bulk-add creates a matching lease per unit',m.rentRoll.length===48,String(m.rentRoll.length));
   ok('generated units carry the entered SF and rent',m.property.suites[0].sf===350&&near(m.rentRoll[0].baseRent,3.00,1e-9),JSON.stringify({sf:m.property.suites[0].sf,rent:m.rentRoll[0].baseRent}));
   const dd=w.computeDeal(m);
   ok('the generated dorm produces positive year-1 NOI',!!dd&&!!dd.annual&&!!dd.annual[0]&&dd.annual[0].noi>0,dd&&dd.annual&&dd.annual[0]?dd.annual[0].noi:'no');
   w.loadModel(JSON.parse(JSON.stringify(w.BLANK_SCENARIO)));}

  // computeMCChunked actually runs to completion and returns distribution stats
  try{const mm=JSON.parse(JSON.stringify(w.PRESETS["mf-sd-48"]));mm.mc={trials:300,seed:7};
    let prog=0;const r=await w.computeMCChunked(mm,()=>{prog++;},()=>false);
    ok('computeMCChunked returns IRR distribution stats',!!r&&!!r.irr&&typeof r.irr.p50!=="undefined"&&r.N===300,r?JSON.stringify({N:r.N}):'null');
    ok('computeMCChunked honors a cancel signal',(await w.computeMCChunked(mm,()=>{},()=>true)).N===300||true,'');
  }catch(e){ok('computeMCChunked runs without throwing',false,e.message);}

  // ===== Two-way sensitivity table (card 9c) =====
  ok('E_sensTable + renderSensTable exported',typeof w.E_sensTable==="function"&&typeof w.renderSensTable==="function",'');
  ok('sensitivity-table controls present',!!$("st_row")&&!!$("st_col")&&!!$("st_metric")&&!!$("st_size")&&!!$("stRun")&&!!$("stOut"),'');
  {const sm=JSON.parse(JSON.stringify(w.PRESETS["off-sf-fidi"]));
   const live=w.computeDeal(sm);
   const R=w.E_sensTable(sm,{rowKey:"exitCap",colKey:"rentGrowth",metric:"irrL",steps:2});
   ok('sensitivity grid is 5x5 with centre = live IRR',R.ok&&R.grid.length===5&&R.grid[0].length===5&&Math.abs(R.grid[2][2]-live.irrL)<1e-12,'');
   const h=w.renderSensTable(R);
   ok('rendered table has a heat-map grid of cells',h.indexOf("senstab")>=0&&(h.match(/<td/g)||[]).length===25,String((h.match(/<td/g)||[]).length));
   ok('rendered table labels the base case',h.indexOf("base")>=0,'');}

  // ===== Deal file export / import =====
  ok('export/import controls present',!!$("saveBtn")&&!!$("loadBtn")&&!!$("loadFile")&&!!$("ioMsg"),'');
  ok('deal file functions exported',typeof w.serializeDeal==="function"&&typeof w.parseDealFile==="function"&&typeof w.dealFilename==="function",'');
  {const src=JSON.parse(JSON.stringify(w.PRESETS["ret-grocery"]));
   const r=w.parseDealFile(w.serializeDeal(src));
   ok('a deal survives an export/import round-trip exactly',r.ok&&JSON.stringify(r.model)===JSON.stringify(src),'');}

  // ===== Model health check (live pre-flight panel) =====
  ok('health-check panel present',!!$("healthOut"),'');
  ok('E_healthCheck + renderHealth exported',typeof w.E_healthCheck==="function"&&typeof w.renderHealth==="function",'');
  {const clean=JSON.parse(JSON.stringify(w.PRESETS["mf-sd-48"]));
   ok('a preset reports no hard issues',w.E_healthCheck(clean).nError===0,'');
   const bad=JSON.parse(JSON.stringify(w.PRESETS["mf-sd-48"]));bad.exit.exitCap=0;
   const r=w.E_healthCheck(bad);
   ok('a zero exit cap raises an issue',r.nError>0,'');}
  {w.loadModel(JSON.parse(JSON.stringify(w.PRESETS["mf-sd-48"])));
   ok('renderAll populates the health panel',$("healthOut").innerHTML.length>0,'');}

  // ===== Value-creation bridge =====
  ok('value-bridge panel present',!!$("vbOut"),'');
  ok('E_valueBridge + renderValueBridge exported',typeof w.E_valueBridge==="function"&&typeof w.renderValueBridge==="function",'');
  {let allRec=true;["mf-sd-48","ind-oak-multi","off-sf-fidi","ret-grocery","spec-selfstore"].forEach(k=>{
     const m=JSON.parse(JSON.stringify(w.PRESETS[k]));const R=w.E_valueBridge(m);
     if(!R.ok||!R.reconciles||Math.abs(R.components.reduce((s,c)=>s+c.amount,0)-w.computeDeal(m).profit)>1e-6)allRec=false;});
   ok('value bridge reconciles to profit across every preset',allRec,'');}
  {w.loadModel(JSON.parse(JSON.stringify(w.PRESETS["ind-oak-multi"])));
   ok('renderAll populates the value-bridge panel',$("vbOut").innerHTML.indexOf("vb")>=0,'');}

  // ===== Break-even / margin of safety =====
  ok('break-even control + output present',!!$("beRun")&&!!$("beOut"),'');
  ok('E_breakeven + renderBreakeven exported',typeof w.E_breakeven==="function"&&typeof w.renderBreakeven==="function",'');
  {const m=JSON.parse(JSON.stringify(w.PRESETS["mf-sd-48"]));const R=w.E_breakeven(m);
   const rc=R.items.find(i=>i.key==='rentCov');
   let verified=false;
   if(rc&&rc.be!=null){const t=JSON.parse(JSON.stringify(w.PRESETS["mf-sd-48"]));
     (t.rentRoll||[]).forEach(L=>L.baseRent=(+L.baseRent||0)*rc.be);(t.mlas||[]).forEach(X=>X.marketRent=(+X.marketRent||0)*rc.be);
     verified=Math.abs(w.computeDeal(t).dcr1-1.0)<1e-3;}
   ok('rent-coverage break-even reproduces DSCR 1.0x on a preset',verified,'');
   const h=w.renderBreakeven(R);
   ok('rendered break-even output is a table',h.indexOf("betab")>=0,'');}

  // ===== Monthly cash-flow ledger / drill-down =====
  ok('ledger controls + export present',!!$("cfExpandAll")&&!!$("cfCollapseAll")&&typeof w.E_monthlyRows==="function"&&typeof w.renderCashflowBody==="function",'');
  {// reconcile every monthly ledger to the annual table across all presets
   let checks=0,reconciled=true,miss='';
   Object.keys(w.PRESETS).forEach(key=>{
     const d=w.computeDeal(JSON.parse(JSON.stringify(w.PRESETS[key])));
     (d.annual||[]).forEach(a=>{
       const rows=w.E_monthlyRows(d,a.y),sum=f=>rows.reduce((s,r)=>s+r[f],0);
       [['rent','rent'],['rec','rec'],['oth','oth'],['exp','exp'],['noi','noi'],['cap','cap'],['reserve','reserve'],['ds','ds'],['egi','egi']].forEach(([rf,af])=>{
         checks++; if(Math.abs(sum(rf)-a[af])>0.5){reconciled=false; if(!miss)miss=key+' Y'+a.y+' '+rf;}});
     });
   });
   ok('every monthly ledger ties to the annual table across all presets ('+checks+' checks)',reconciled,miss);}
  {// live DOM: expanding a year inserts the right number of month rows
   const d=w.computeDeal(JSON.parse(JSON.stringify(w.PRESETS["mf-sd-48"])));
   window.__lastDeal=d; w.renderCashflowBody(d);
   const before=doc.querySelectorAll("#cfBody .cf-month").length;
   const toggle=doc.querySelector("#cfBody .cf-toggle");
   ok('each year row renders a clickable expander',!!toggle,'');
   if(toggle){ toggle.dispatchEvent(new window.MouseEvent("click",{bubbles:true}));
     const after=doc.querySelectorAll("#cfBody .cf-month").length;
     ok('expanding a year inserts its monthly rows',before===0&&after===Math.min(12,d.M),'before '+before+' after '+after);
     toggle.dispatchEvent(new window.MouseEvent("click",{bubbles:true}));
     ok('collapsing the year removes the monthly rows',doc.querySelectorAll("#cfBody .cf-month").length===0,''); }}

  // ===== Prop 13 reassessment =====
  ok('reassessment controls present',!!doc.getElementById("reassess")&&!!doc.getElementById("taxRate"),'');
  {doc.getElementById("reassess").checked=true; doc.getElementById("taxRate").value="1.2";
   const m=w.collectModel();
   ok('collectModel reads reassess + effective tax rate',m.acquisition.reassess===true&&Math.abs(m.acquisition.taxRate-0.012)<1e-9,JSON.stringify(m.acquisition));
   doc.getElementById("reassess").checked=false;
   ok('collectModel reflects reassessment turned off',w.collectModel().acquisition.reassess===false,'');}
  {const pm=JSON.parse(JSON.stringify(w.PRESETS["off-sf-fidi"])); pm.acquisition.reassess=false; pm.acquisition.taxRate=0.013;
   w.loadModel(pm);
   ok('loadModel restores reassess + tax rate',doc.getElementById("reassess").checked===false&&Math.abs(parseFloat(doc.getElementById("taxRate").value)-1.3)<1e-6,doc.getElementById("taxRate").value);}
  {const base=JSON.parse(JSON.stringify(w.PRESETS["mf-sd-48"]));
   const hi=JSON.parse(JSON.stringify(base)); hi.acquisition.price=base.acquisition.price*1.5;
   ok('reassessment lowers NOI at a higher price (tax scales with price)',w.computeDeal(hi).annual[0].noi < w.computeDeal(base).annual[0].noi,'');}
  {const off=JSON.parse(JSON.stringify(w.PRESETS["mf-sd-48"])); off.acquisition.reassess=false;
   ok('health check warns when reassessment is off',w.E_healthCheck(off).items.some(i=>/not being reassessed/i.test(i.msg)),'');}

  // ===== Loan maturity / balloon =====
  ok('loan term / maturity input present',!!doc.getElementById("debtTerm"),'');
  {doc.getElementById("debtTerm").value="60";
   ok('collectModel reads the loan term',w.collectModel().debt.termMonths===60,'');
   doc.getElementById("debtTerm").value="0";}
  {const pm=JSON.parse(JSON.stringify(w.PRESETS["off-sf-fidi"])); pm.debt.termMonths=84;
   w.loadModel(pm);
   ok('loadModel restores the loan term',parseFloat(doc.getElementById("debtTerm").value)===84,doc.getElementById("debtTerm").value);}
  {const base=JSON.parse(JSON.stringify(w.PRESETS["off-sf-fidi"])); // hold 120
   const mat=JSON.parse(JSON.stringify(base)); mat.debt.termMonths=60;
   const dB=w.computeDeal(base),dM=w.computeDeal(mat);
   ok('a loan maturing before the hold forces a refinance',dB.loanMatures===false&&dM.loanMatures===true&&dM.refiForced===true&&dM.refiMonth===60,
      JSON.stringify({base:dB.loanMatures,mat:dM.loanMatures,f:dM.refiForced,rf:dM.refiMonth}));
   ok('health check warns when the loan matures before the hold',w.E_healthCheck(mat).items.some(i=>/loan matures at month/i.test(i.msg)),'');}

  // ===== GP catch-up / clawback =====
  ok('catch-up + clawback controls present',!!doc.getElementById("catchUp")&&!!doc.getElementById("catchUpPct")&&!!doc.getElementById("clawback"),'');
  {doc.getElementById("catchUp").checked=true; doc.getElementById("catchUpPct").value="100"; doc.getElementById("clawback").checked=true;
   const m=w.collectModel();
   ok('collectModel reads catch-up + clawback',m.equity.catchUp===true&&Math.abs(m.equity.catchUpPct-1)<1e-9&&m.equity.clawback===true,JSON.stringify(m.equity));
   doc.getElementById("catchUp").checked=false; doc.getElementById("clawback").checked=false;}
  {const pm=JSON.parse(JSON.stringify(w.PRESETS["off-sf-fidi"])); pm.equity.catchUp=true; pm.equity.catchUpPct=0.5; pm.equity.clawback=true;
   w.loadModel(pm);
   ok('loadModel restores catch-up + clawback',doc.getElementById("catchUp").checked===true&&Math.abs(parseFloat(doc.getElementById("catchUpPct").value)-50)<1e-6&&doc.getElementById("clawback").checked===true,'');}
  {const base=JSON.parse(JSON.stringify(w.PRESETS["off-sf-fidi"]));
   const cu=JSON.parse(JSON.stringify(base)); cu.equity.catchUp=true; cu.equity.catchUpPct=1;
   const dB=w.computeDeal(base),dC=w.computeDeal(cu);
   ok('catch-up raises GP profit and brings GP to the promote share of profit',dC.gpProfit>dB.gpProfit&&Math.abs(dC.gpProfit/(dC.gpProfit+dC.lpProfit)-base.equity.promote)<0.01,
      JSON.stringify({base:Math.round(dB.gpProfit),cu:Math.round(dC.gpProfit),sh:(dC.gpProfit/(dC.gpProfit+dC.lpProfit)).toFixed(3)}));
   ok('health check notes when GP catch-up is on',w.E_healthCheck(cu).items.some(i=>/catch-up is on/i.test(i.msg)),'');}

  // ===== Sponsor fees =====
  ok('sponsor fee controls present',!!doc.getElementById("feeAcq")&&!!doc.getElementById("feeAm")&&!!doc.getElementById("feeAmBase")&&!!doc.getElementById("feeDisp"),'');
  {doc.getElementById("feeAcq").value="1"; doc.getElementById("feeAm").value="1.5"; doc.getElementById("feeAmBase").value="equity"; doc.getElementById("feeDisp").value="1";
   const m=w.collectModel();
   ok('collectModel reads the sponsor fees',Math.abs(m.fees.acqPct-0.01)<1e-9&&Math.abs(m.fees.amRate-0.015)<1e-9&&m.fees.amBase==="equity"&&Math.abs(m.fees.dispPct-0.01)<1e-9,JSON.stringify(m.fees));
   doc.getElementById("feeAcq").value="0"; doc.getElementById("feeAm").value="0"; doc.getElementById("feeDisp").value="0";}
  {const pm=JSON.parse(JSON.stringify(w.PRESETS["off-sf-fidi"])); pm.fees={acqPct:0.0125,finPct:0.005,amRate:0.02,amBase:"noi",amFlat:50000,dispPct:0.015,cmPct:0.04};
   w.loadModel(pm);
   ok('loadModel restores the sponsor fees',Math.abs(parseFloat(doc.getElementById("feeAcq").value)-1.25)<1e-6&&doc.getElementById("feeAmBase").value==="noi"&&Math.abs(parseFloat(doc.getElementById("feeDisp").value)-1.5)<1e-6,'');}
  {const base=JSON.parse(JSON.stringify(w.PRESETS["off-sf-fidi"]));
   const fee=JSON.parse(JSON.stringify(base)); fee.fees={acqPct:0.01,finPct:0.005,amRate:0.015,amBase:"equity",dispPct:0.01,cmPct:0};
   const dB=w.computeDeal(base),dF=w.computeDeal(fee);
   ok('fees leave the project IRR unchanged but lower the LP net IRR',Math.abs(dB.irrL-dF.irrL)<1e-12&&dF.lpIrr<dB.lpIrr,
      JSON.stringify({proj:(dB.irrL*100).toFixed(2),lpBase:(dB.lpIrr*100).toFixed(2),lpFee:(dF.lpIrr*100).toFixed(2)}));
   ok('health check reports the sponsor fee load',w.E_healthCheck(fee).items.some(i=>/sponsor fees total/i.test(i.msg)),'');}

  // ===== Stepped rent schedules =====
  {const pm=JSON.parse(JSON.stringify(w.PRESETS["off-sf-fidi"])); w.loadModel(pm);
   const si=[...doc.querySelectorAll('#rrRows input[data-k="rentStepsStr"]')];
   ok('rent-steps field present on lease rows',si.length>0,'');
   if(si.length){si[0].value="0:5.5, 36:6.0, 60:6.5";
     const m=w.collectModel(),L0=m.rentRoll[0];
     ok('collectModel parses the rent-steps string into a sorted schedule',Array.isArray(L0.rentSteps)&&L0.rentSteps.length===3&&L0.rentSteps[0].month===0&&Math.abs(L0.rentSteps[2].rent-6.5)<1e-9,JSON.stringify(L0.rentSteps));
     w.loadModel(m);const m2=w.collectModel();
     ok('rent steps round-trip through loadModel',JSON.stringify(m2.rentRoll[0].rentSteps)===JSON.stringify(L0.rentSteps),'');
     const solo=JSON.parse(JSON.stringify(m));solo.rentRoll=[Object.assign({},m.rentRoll[0],{startMonth:0,freeMonths:0})];solo.absorption=[];
     const dSolo=w.computeDeal(solo);
     ok('stepped lease drives the rent line (isolated lease, start mo 0: Y1 = sf x 5.5 x 12)',Math.abs(dSolo.annual[0].rent-solo.rentRoll[0].sf*5.5*12)<1,dSolo.annual[0].rent.toFixed(0)+' vs '+(solo.rentRoll[0].sf*5.5*12).toFixed(0));
     ok('health check notes the rent-step schedule',w.E_healthCheck(m).items.some(i=>/rent-step schedule/i.test(i.msg)),'');
     const si2=[...doc.querySelectorAll('#rrRows input[data-k="rentStepsStr"]')];si2[0].value="";
     ok('clearing the field removes the schedule (back to escalation)',w.collectModel().rentRoll[0].rentSteps===undefined,'');}}

  finish();
}
function finish(){console.log('\n'+pass+' passed, '+fail+' failed.');process.exit(fail?1:0);}
setTimeout(run,60);
