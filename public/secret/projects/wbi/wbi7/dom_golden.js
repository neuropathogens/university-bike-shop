/* DOM golden harness (browser-free) — loads index.html in jsdom, drives the real
   render path via window.__wbi7.loadModel, and checks the locked display goldens
   for the 5 representative presets plus matrix cell counts. Substitutes for the
   puppeteer Part B suite in environments without a Chrome binary. */
const fs=require('fs'),path=require('path');
const {JSDOM}=require('jsdom');
const HTML=process.env.WBI7_PATH||path.resolve(__dirname,'index.html');
let html=fs.readFileSync(HTML,'utf8');

let pass=0,fail=0;
const ok=(n,c,x)=>{c?pass++:fail++;console.log((c?'  PASS  ':'  FAIL  ')+n+(c?'':'  -> '+x));};

const DISPLAY_GOLDENS={
  "mf-sd-48":{rUIrr:'6.7%',rUEm:'1.71\u00d7',rLIrr:'7.4%',rLEm:'1.95\u00d7',rMirr:'7.4%',
    rPvTot:'$18,200,186',rValue:'$22,121,846',rDyF:'10.4%',rDcr:'1.10',
    suOcc:'100.0%',suWalt:'0.4 yrs',suGoin:'4.8%',wLpIrr:'7.4%',wGpIrr:'7.4%',totSF:'40,320 sf'},
  "ind-oak-multi":{rUIrr:'10.5%',rUEm:'1.80\u00d7',rLIrr:'14.7%',rLEm:'2.28\u00d7',rMirr:'13.5%',
    rPvTot:'$23,840,030',rValue:'$27,222,094',rDyF:'13.9%',rDcr:'1.78',
    suOcc:'100.0%',suWalt:'3.1 yrs',suGoin:'6.7%',wLpIrr:'14.1%',wGpIrr:'19.6%',totSF:'88,000 sf'},
  "off-sf-fidi":{rUIrr:'7.8%',rUEm:'1.75\u00d7',rLIrr:'8.3%',rLEm:'1.79\u00d7',rMirr:'8.2%',
    rPvTot:'$51,450,271',rValue:'$72,424,137',rDyF:'19.0%',rDcr:'1.61',
    suOcc:'80.0%',suWalt:'5.2 yrs',suGoin:'6.1%',wLpIrr:'8.2%',wGpIrr:'8.5%',totSF:'95,000 sf'},
  "ret-grocery":{rUIrr:'7.1%',rUEm:'1.71\u00d7',rLIrr:'7.6%',rLEm:'1.82\u00d7',rMirr:'7.6%',
    rPvTot:'$34,756,854',rValue:'$40,404,115',rDyF:'13.7%',rDcr:'1.60',
    suOcc:'100.0%',suWalt:'6.5 yrs',suGoin:'5.9%',wLpIrr:'7.6%',wGpIrr:'7.6%',totSF:'83,300 sf'},
  "spec-selfstore":{rUIrr:'15.7%',rUEm:'2.57\u00d7',rLIrr:'24.8%',rLEm:'4.26\u00d7',rMirr:'21.0%',
    rPvTot:'$20,404,730',rValue:'$23,446,766',rDyF:'19.5%',rDcr:'2.06',
    suOcc:'100.0%',suWalt:'0.7 yrs',suGoin:'8.2%',wLpIrr:'23.6%',wGpIrr:'32.6%',totSF:'88,000 sf'}
};

const dom=new JSDOM(html,{runScripts:"dangerously",url:"http://localhost/",pretendToBeVisual:true});
const {window}=dom;
window.requestAnimationFrame=cb=>setTimeout(cb,0);

function run(){
  const w=window.__wbi7;
  if(!w){ok('window.__wbi7 present',false,'missing — script error?');finish();return;}
  // open the app (boot wires events + does first render). Gate calls boot() on correct key,
  // but __wbi7 is exported regardless; loadModel triggers renderAll which we read.
  const $=id=>window.document.getElementById(id);
  for(const preset of Object.keys(DISPLAY_GOLDENS)){
    const m=JSON.parse(JSON.stringify(w.PRESETS[preset]));
    w.loadModel(m);
    for(const [id,want] of Object.entries(DISPLAY_GOLDENS[preset])){
      const e=$(id);const got=e?e.textContent:null;
      ok(preset+'.'+id+' == "'+want+'"',got===want,'got "'+got+'"');
    }
    const pvC=window.document.querySelectorAll('#mxPvWrap td.out').length;
    const irC=window.document.querySelectorAll('#mxIrrWrap td.out').length;
    ok(preset+': PV matrix 25 cells',pvC===25,pvC);
    ok(preset+': IRR matrix 25 cells',irC===25,irC);
  }
  finish();
}
function finish(){
  console.log('\n'+pass+' passed, '+fail+' failed.');
  process.exit(fail?1:0);
}
// jsdom runs the inline <script> synchronously on construction; __wbi7 should exist now.
setTimeout(run,50);
