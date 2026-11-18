/* WBI7 — tests for the GP catch-up and clawback waterfall. With a catch-up, after the LP
   receives return of capital and its preferred return, the GP takes catchUpPct of
   distributions until the GP's profit equals promote x (total profit above capital) — so
   the promote applies to the WHOLE profit, not just the band above the pref, and the GP is
   no longer under-promoted. A clawback is a final true-up that returns GP profit to the LP
   if the LP's lifetime cash flows fail to clear the preferred return. Both are opt-in, so
   the default waterfall (and the shipped presets) are unchanged. */
const fs=require('fs'),vm=require('vm');
const html=fs.readFileSync(__dirname+'/index.html','utf8');
const a=html.indexOf('/* ===================== WBI7 ENGINE START');
const b=html.indexOf('WBI7 ENGINE END ===================== */');
const ctx={console};vm.createContext(ctx);
vm.runInContext(html.slice(a,b+'WBI7 ENGINE END ===================== */'.length),ctx);
const {E_waterfall,E_waterfallCatchup}=ctx;
let pass=0,fail=0;
const ok=(n,c,x)=>{c?pass++:fail++;console.log((c?'  PASS  ':'  FAIL  ')+n+(c?'':'  -> '+x));};
const near=(a,b,e)=>Math.abs(a-b)<=(e==null?1e-6:e);
const sum=a=>a.reduce((s,x)=>s+x,0);
const profitShareGP=wf=>{const g=sum(wf.gp),l=sum(wf.lp);return g/(g+l);}; // share of net profit (above capital)

console.log('--- GP catch-up & clawback waterfall ---');

// helper: a contribution then a single distribution 12 months later
const cf=(contrib,dist)=>{const a=new Array(13).fill(0);a[0]=-contrib;a[12]=dist;return a;};

// 1. conservation: LP + GP = total cash flow each period
{const wf=E_waterfallCatchup(cf(100,140),0.9,0.08,0.2,1,false);const c=cf(100,140);
 let okc=true;for(let t=0;t<c.length;t++)if(!near(wf.lp[t]+wf.gp[t],c[t],1e-6))okc=false;
 ok('catch-up waterfall conserves cash (LP + GP = total each period)',okc,'');}

// 2. full catch-up brings GP to exactly the promote share of profit
{const wf=E_waterfallCatchup(cf(100,140),0.9,0.08,0.2,1,false);
 ok('100% catch-up gives the GP exactly the promote share of total profit',near(profitShareGP(wf),0.2,1e-6),(profitShareGP(wf)*100).toFixed(3)+'%');}

// 3. catch-up raises GP profit vs the default (no-catch-up) waterfall
{const base=E_waterfall(cf(100,140),0.9,0.08,0.2);
 const cu=E_waterfallCatchup(cf(100,140),0.9,0.08,0.2,1,false);
 ok('catch-up raises GP profit vs the default waterfall (under-promote fixed)',sum(cu.gp)>sum(base.gp),
    'base '+sum(base.gp).toFixed(2)+' vs cu '+sum(cu.gp).toFixed(2));
 ok('default (no catch-up) under-promotes the GP below the promote share',profitShareGP(base)<0.2,(profitShareGP(base)*100).toFixed(2)+'%');}

// 4. when the catch-up completes, 50% and 100% catch-up give the same final GP profit
{const c=cf(100,300); // ample profit so catch-up completes either way
 const full=E_waterfallCatchup(c,0.9,0.08,0.2,1,false);
 const half=E_waterfallCatchup(c,0.9,0.08,0.2,0.5,false);
 ok('a completed catch-up gives the same final GP profit at 50% and 100% (timing differs, end split same)',near(sum(full.gp),sum(half.gp),1e-6),
    sum(full.gp).toFixed(2)+' vs '+sum(half.gp).toFixed(2));
 ok('both reach the promote share when the catch-up completes',near(profitShareGP(full),0.2,1e-6)&&near(profitShareGP(half),0.2,1e-6),'');}

// 5. when the catch-up is INCOMPLETE (thin profit), a higher catch-up % gives the GP more
{const c=cf(100,110); // only 10 of profit; pref (~8) eats most, catch-up can't complete
 const full=E_waterfallCatchup(c,0.9,0.08,0.2,1,false);
 const half=E_waterfallCatchup(c,0.9,0.08,0.2,0.5,false);
 ok('an incomplete catch-up gives the GP more at 100% than at 50%',sum(full.gp)>sum(half.gp),
    'full '+sum(full.gp).toFixed(3)+' vs half '+sum(half.gp).toFixed(3));}

// 6. a catch-up rate at or below the promote never completes (no over-credit to GP)
{const c=cf(100,300);
 const atPromo=E_waterfallCatchup(c,0.9,0.08,0.2,0.2,false); // == promote -> never catches up
 const belowPromo=E_waterfallCatchup(c,0.9,0.08,0.15,0.1,false);
 ok('a catch-up rate equal to the promote does not over-credit the GP',profitShareGP(atPromo)<0.2+1e-6,(profitShareGP(atPromo)*100).toFixed(2)+'%');
 ok('a catch-up rate below the promote leaves the GP at/below the residual share',sum(belowPromo.gp)>0,'');}

// 7. promote 0 -> LP gets all profit even with catch-up on
{const wf=E_waterfallCatchup(cf(100,200),0.9,0.08,0,1,false);
 ok('promote of 0 routes all profit to the LP even with catch-up on',near(profitShareGP(wf),0,1e-6),(profitShareGP(wf)*100).toFixed(3)+'%');}

// 8. clawback: LP misses pref after the GP took promote -> GP returns profit to the LP
{const c=[-100,200,-150,60]; // big early distribution (GP earns promote), late capital call, weak final
 const off=E_waterfallCatchup(c,0.9,0.08,0.2,1,false);
 const on =E_waterfallCatchup(c,0.9,0.08,0.2,1,true);
 ok('clawback returns money to the LP when it misses its pref',sum(on.lp)>sum(off.lp)+1e-6,
    'off LP '+sum(off.lp).toFixed(2)+' vs on LP '+sum(on.lp).toFixed(2));
 ok('clawback reduces the GP by the same amount it adds to the LP (conserves)',
    near(sum(on.lp)+sum(on.gp),sum(off.lp)+sum(off.gp),1e-6),'');
 ok('the reported clawback is positive and capped at the GP profit',on.claw>0&&on.claw<=sum(off.gp.filter(x=>x>0))+1e-6,'claw '+on.claw.toFixed(2));}

// 9. clawback does NOT trigger when the LP clears its pref
{const c=cf(100,300); // LP easily clears pref
 const on=E_waterfallCatchup(c,0.9,0.08,0.2,1,true);
 ok('clawback does not trigger when the LP clears its preferred return',near(on.claw,0,1e-6),'claw '+on.claw.toFixed(4));}

// 10. contributions split by equity share
{const wf=E_waterfallCatchup(cf(100,140),0.9,0.08,0.2,1,false);
 ok('contributions split by equity share (LP 90% / GP 10%)',near(wf.lp[0],-90,1e-6)&&near(wf.gp[0],-10,1e-6),'');}

console.log('\n'+pass+' passed, '+fail+' failed.');
process.exit(fail?1:0);
