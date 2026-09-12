"""Clean-room Stage 11B audit. No imports from production verification.

Run: python verification/stage11b_astra_independent.py
Requires numpy/scipy. Numeric searches are evidence, not universal proofs.
Tariffs evaluated from utility, demand, participation, revenue and resource cost.
"""
import json
import math
from fractions import Fraction as Q
from pathlib import Path
import numpy as np
from scipy.optimize import minimize_scalar, brentq


class Utility:
    def __init__(self, a=(4., 5.), kind='power', r=2., beta=(1., 1.), eps=1.):
        self.a, self.kind, self.r, self.beta, self.eps = a, kind, r, beta, eps

    def choke(self, j):
        return self.a[j] if self.kind == 'power' else self.a[j]-self.eps

    def q(self, j, p):
        if self.kind == 'power':
            return (max(self.a[j]-p, 0.)/self.beta[j])**(1/(self.r-1))
        return max(math.log(self.a[j]/(p+self.eps)), 0.)

    def v(self, j, q):
        if self.kind == 'power':
            return self.a[j]*q-self.beta[j]*q**self.r/self.r
        return self.a[j]*(1-math.exp(-q))-self.eps*q

    def s(self, j, p):
        q = self.q(j, p)
        return self.v(j, q)-p*q


def fee_candidate(u, c, masses, p, binding):
    F = u.s(binding, p) if binding is not None else 0.
    served = tuple(j for j in range(2) if u.s(j, p) >= F-1e-10)
    profit = sum(masses[j]*(F+(p-c)*u.q(j, p)) for j in served)
    rent = [max(u.s(j, p)-F, 0.) for j in range(2)]
    return dict(profit=profit, F=F, p=p, served=list(served), rent=rent)


def global_tariff(u, c, masses, metered):
    # At a given p profit is affine in F on each participation cell.
    # Its upper envelope occurs at a reservation fee or no service.
    candidates = [dict(profit=0., F=max(u.s(j, 0) for j in range(2))+1,
                       p=0. if not metered else max(u.choke(j) for j in range(2))+1,
                       served=[], rent=[0., 0.])]
    if not metered:
        candidates += [fee_candidate(u, c, masses, 0., j) for j in [0, 1, None]]
    else:
        # Partition at choke prices and at S_L=S_H. For the common-shape
        # baseline and exponential robustness no surplus-order crossing exists.
        knots = sorted(set([1e-12, *[u.choke(j) for j in range(2)]]))
        scan = np.linspace(0, max(knots), 101)
        for x, y in zip(scan[:-1], scan[1:]):
            if (u.s(0,x)-u.s(1,x))*(u.s(0,y)-u.s(1,y)) < 0:
                knots.append(brentq(lambda p:u.s(0,p)-u.s(1,p),x,y))
        knots = sorted(set(knots))
        for j in [0, 1, None]:
            for lo, hi in zip(knots[:-1], knots[1:]):
                if hi-lo < 1e-10:
                    continue
                # Subdivide to avoid equating one local optimizer with globality.
                grid = np.linspace(lo, hi, 13)
                for x in grid:
                    candidates.append(fee_candidate(u,c,masses,float(x),j))
                for x,y in zip(grid[:-1],grid[1:]):
                    fit=minimize_scalar(lambda p:-fee_candidate(u,c,masses,p,j)['profit'],
                                        bounds=(x+1e-12,y-1e-12),method='bounded',
                                        options={'xatol':1e-11})
                    if not fit.success or not math.isfinite(fit.fun):
                        raise RuntimeError('UNRESOLVED optimization')
                    candidates.append(fee_candidate(u,c,masses,float(fit.x),j))
    return max(candidates,key=lambda z:z['profit'])


def baseline_global(a,d,c,l,h):
    # Separate finite-candidate exact characterization, justified in audit text.
    # Used for large sweeps; independently compared with tariff optimizer above.
    n=l+h
    p=min(a,c+d*h/n) if n else c
    u=Utility((a,a+d))
    BF=fee_candidate(u,c,(l,h),0.,0)
    HF=fee_candidate(u,c,(l,h),0.,1)
    BM=fee_candidate(u,c,(l,h),p,0)
    HM=fee_candidate(u,c,(l,h),c,1)
    Z=dict(profit=0.,p=0.,F=(a+d)**2,served=[],rent=[0.,0.])
    return max([BF,HF,Z],key=lambda z:z['profit']), max([BM,HM,Z],key=lambda z:z['profit'])


def main():
    out={}
    a,d,c,l,bH,KH=4.,1.,1.,.8,.5,8.
    RF=((a+d)**2-a*a)/2
    h0=bH/KH
    hF=(bH+RF)/KH
    u=Utility()
    # Integration root uses utility-derived rents and direct tariff optimization.
    hM=brentq(lambda h:KH*h-bH-global_tariff(u,c,(l,h),True)['rent'][1],h0,hF,xtol=1e-10)
    def gain(h):
        return global_tariff(u,c,(l,h),True)['profit']-global_tariff(u,c,(l,h),False)['profit']
    muM,muF=gain(hM),gain(hF)
    mu=1.3
    hs=brentq(lambda h:gain(h)-mu,hM,hF,xtol=1e-10)
    Fstar=global_tariff(u,c,(l,hs),False)
    Mstar=global_tariff(u,c,(l,hs),True)
    rho=(bH+Fstar['rent'][1]-KH*hs)/(Fstar['rent'][1]-Mstar['rent'][1])
    out['baseline'] = dict(h0=h0,hM=hM,hF=hF,muM=muM,muF=muF,hstar=hs,rho=rho,
                           flat=Fstar,metered=Mstar,
                           flat_expectation_metering_deviation=muF-mu,
                           metered_expectation_flat_deviation=mu-muM)
    # Exact own-payoff evaluator for the outside-R guard.
    ll,hh=Q(1,10),Q(3,5)
    BF=(ll+hh)*8-(ll*4+hh*5)
    HF=hh*(Q(25,2)-5)
    assert HF-BF==Q(23,10)
    out['exact_outside_R']={'BF':str(BF),'HF':str(HF),'difference':str(HF-BF)}
    # Exhaustively compare numerical optimizer to finite-set algebra at selected states.
    maxerr=0.
    for aa,dd,cc,ll,hh in [(4,1,1,.8,x) for x in [0,.0625,.2,.625,.72,1]]+[(4,1,1,.1,.6),(1,3,.8,.1,.9),(1,1,.9,1,.1),(4,1,3,0,1),(4,1,1,1,0),(4,1,1,0,0)]:
        uf=Utility((aa,aa+dd))
        fast=baseline_global(aa,dd,cc,ll,hh)
        for arch in [False,True]:
            direct=global_tariff(uf,cc,(ll,hh),arch)
            err=abs(direct['profit']-fast[int(arch)]['profit'])
            maxerr=max(maxerr,err)
            assert err<1e-7,(aa,dd,cc,ll,hh,arch,err)
    out['direct_vs_finite_candidate_maxerror']=maxerr
    # State sweep independently of the preferred equilibrium: global active sets.
    sweep=[]
    for hh in np.linspace(0,1,501):
        ff,mm=baseline_global(a,d,c,l,float(hh))
        sweep.append([float(hh),ff['served'],mm['served'],mm['profit']-ff['profit']])
    out['boundary_sample']=[sweep[i] for i in [0,31,228,312,355,356,400,500]]
    out['state_sweep_count']=len(sweep)
    out['state_sweep']=sweep
    # Certification regression: sqrt-CDF check's flat state leaves both-served region.
    sqrt_hF=math.sqrt(5/8)
    sqrt_hM=brentq(lambda h:h-math.sqrt((5-(1+h/(l+h)))/8),0,sqrt_hF)
    sqrt_ff,sqrt_mm=baseline_global(a,d,c,l,sqrt_hF)
    sqrt_fm,sqrt_mmm=baseline_global(a,d,c,l,sqrt_hM)
    hB=Q(32,45); pB=Q(25,17); gainB=Q(250,153)
    lam_sqrt=(8*hB*hB-Q(1,2))/Q(9,2)
    lam_uniform=(7*hB-Q(1,2))/Q(9,2)
    # Exact flat-architecture (random fee) equilibrium at mu=17/10.
    # F=8 with probability lambda; F=25/2 otherwise, all indifferent users accept.
    exact_BF=(Q(4,5)+hB)*8-(Q(4,5)*4+hB*5)
    exact_HF=hB*(Q(25,2)-5)
    exact_BM=(Q(4,5)+hB)*(4-pB)**2/2+(pB-1)*(Q(4,5)*(4-pB)+hB*(5-pB))
    exact_HM=hB*8
    assert exact_BF==exact_HF and exact_BM>exact_HM
    assert exact_BM-exact_BF==gainB<Q(17,10)
    assert Q(0)<lam_sqrt<Q(1) and Q(1,2)+lam_sqrt*Q(9,2)==8*hB*hB
    assert Q(0)<lam_uniform<Q(1) and Q(1,2)+lam_uniform*Q(9,2)==7*hB
    # Uniform KH=7, mu=1637/1000 is just outside R and inside the false branch gap.
    uhf=Q(5,7); fake_muF=(Q(4,5)+uhf)*(1+uhf/(Q(4,5)+uhf))**2/2
    assert gainB<Q(1637,1000)<fake_muF
    out['cdf_certification_regression']=dict(sqrt_hM=sqrt_hM,sqrt_hF=sqrt_hF,
        flat_hF=sqrt_ff,metered_hF=sqrt_mm,
        fake_muF=(l+sqrt_hF)/2*(1+sqrt_hF/(l+sqrt_hF))**2,
        actual_gain_hF=sqrt_mm['profit']-sqrt_ff['profit'],
        actual_gain_hM=sqrt_mmm['profit']-sqrt_fm['profit'],
        H_only_flat_advantage=-l*4+sqrt_hF*4.5,
        boundary_h=str(hB),boundary_gain=str(gainB),flat_profit=str(exact_BF),
        sqrt_flat_fee_mix_probability=str(lam_sqrt),sqrt_mu='17/10',
        uniform_KH7_flat_fee_mix_probability=str(lam_uniform),uniform_mu='1637/1000',
        uniform_fake_muF=str(fake_muF))
    # All pure candidate classes: both, only H, no-service, and integration caps.
    eq_candidates=[]
    for arch in [False,True]:
        for hh in [h0,hM,hF,0.,1.]:
            ff,mm=baseline_global(a,d,c,l,hh)
            z=mm if arch else ff
            residual=min(1.,(bH+z['rent'][1])/KH)-hh
            architecture_gain=mm['profit']-ff['profit']-mu
            eq_candidates.append(dict(metered=arch,h=hh,served=z['served'],
                       integration_residual=residual,architecture_gain=architecture_gain,
                       equilibrium=abs(residual)<1e-8 and (architecture_gain>=0 if arch else architecture_gain<=0)))
    out['alternative_pure_candidates']=eq_candidates
    assert not any(x['equilibrium'] for x in eq_candidates)
    # Welfare computed as utility minus resource costs, without tariff transfers.
    def welfare(h,metered,kk,activation):
        ff,mm=baseline_global(a,d,c,l,h)
        z=mm if metered else ff
        bL,KL=3.2,4.
        w=bL*l+bH*h-KL*l*l/2-kk*h*h/2
        for j,m in enumerate([l,h]):
            if j in z['served']:
                q=u.q(j,z['p'])
                w+=m*(u.v(j,q)-c*q)
        return w-(activation if metered else 0.)
    welfare_examples=[]
    for kk in [8.,12.,20.,40.,80.,160.]:
        hf=(bH+RF)/kk
        hm=brentq(lambda h:kk*h-bH-(RF-d*(c+d*h/(l+h))),0.,hf)
        for activation in [0.,.05,.2,.5,1.3]:
            diff=welfare(hm,True,kk,activation)-welfare(hf,False,kk,activation)
            welfare_examples.append(dict(KH=kk,mu=activation,hM=hm,hF=hf,WM_minus_WF=diff))
    out['welfare_examples']=welfare_examples
    assert min(x['WM_minus_WF'] for x in welfare_examples)<0<max(x['WM_minus_WF'] for x in welfare_examples)
    # Nonquadratic utility, selected independently of repo power robustness:
    # v_j=a_j(1-exp(-q))-eps*q; strict concavity and finite satiation.
    expu=Utility((8.,10.),kind='exponential',eps=1.)
    ec=.2; el=.8; eb=.2; ek=8.
    er=expu.s(1,0)-expu.s(0,0)
    ehf=(eb+er)/ek
    ehm=brentq(lambda h:ek*h-eb-global_tariff(expu,ec,(el,h),True)['rent'][1],0.,ehf)
    expstates=[]
    for hh in np.linspace(ehm,ehf,15):
        ff=global_tariff(expu,ec,(el,float(hh)),False)
        mm=global_tariff(expu,ec,(el,float(hh)),True)
        expstates.append(dict(h=float(hh),flat=ff,metered=mm,gain=mm['profit']-ff['profit']))
    out['nonquadratic_exponential']=dict(a=[8,10],eps=1,c=ec,l=el,bH=eb,KH=ek,hM=ehm,hF=ehf,states=expstates)
    assert 0<ehm<ehf and all(x['flat']['served']==[0,1] and x['metered']['served']==[0,1] for x in expstates)
    assert all(x['gain']<y['gain'] for x,y in zip(expstates[:-1],expstates[1:]))
    # Adversarial curvature search: surplus ordering alone does not imply high usage.
    # These change the baseline primitive, so are scope tests, not counterexamples to T1.
    curvature=[]
    for aa in [(4.,5.),(4.,8.),(4.,12.)]:
        for betaH in [.25,.5,2.,4.,8.]:
            uu=Utility(aa,beta=(1.,betaH))
            ff=global_tariff(uu,1.,(.8,.3),False)
            mm=global_tariff(uu,1.,(.8,.3),True)
            if ff['served']==[0,1] and mm['served']==[0,1] and mm['rent'][1]>ff['rent'][1]+1e-7:
                curvature.append(dict(a=aa,betaH=betaH,flat=ff,metered=mm,
                                      q_at_zero=[uu.q(j,0) for j in range(2)]))
    out['curvature_rent_reversal_scope_tests']=curvature
    # Exact heterogeneous-curvature scope guard, both served and global.
    # v_L=4q-q^2/2, v_H=12q-4q^2; H means high total WTP, NOT high usage.
    cp=Q(7,46); cl,ch=Q(4,5),Q(3,10)
    cf=(4-cp)**2/2
    cr=(12-cp)**2/16-cf
    cprofit=(cl+ch)*cf+(cp-1)*(cl*(4-cp)+ch*(12-cp)/8)
    assert cr>1 and cprofit>Q(103,20) and cprofit>ch*Q(121,16)
    out['exact_curvature_scope_guard']=dict(p=str(cp),rentH=str(cr),flat_rentH='1',profit=str(cprofit),
                                          classification='outside common-curvature/high-use ordering; not a baseline counterexample')
    path=Path(__file__).with_name('stage11b_astra_results.json')
    path.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['nonquadratic_exponential','welfare_examples','alternative_pure_candidates','state_sweep']},indent=2))
    print('Welfare range:',min(welfare_examples,key=lambda x:x['WM_minus_WF']),max(welfare_examples,key=lambda x:x['WM_minus_WF']))
    print('Exponential states:',ehm,ehf,expstates[0]['gain'],expstates[-1]['gain'])
    print('Saved',path)


if __name__=='__main__':
    main()
