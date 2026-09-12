# Stage 4R — Model Repair after Stage-11 Certification Regression

Date: 2026-09-12 (JST)  
Project: **Dynamic Tariff Choice for Generative AI**  
Canonical workflow: `ryotamatsuki/research-paper-workflow` v2.1

## Verdict

**GO TO REPEATED STAGE 4A.**

The Stage-11B hostile audit did not find a counterexample to the strict regular-branch T1--T3 algebra. It did identify two Stage-4A certification regressions: (i) future participation at exactly zero continuation surplus was not defined, even though the continuation solution sets the low-use participation constraint exactly binding; and (ii) the provider's global continuation strategy was not explicitly characterized at all installed-state histories. This repair changes only the game-definition and continuation-completeness layer. It does **not** add a player, state, tariff instrument, demand primitive, or new economic mechanism.

The previous Stage-8 freeze is therefore stale until the required downstream gates are rerun and a new Stage-8 freeze is issued.

## 1. Repaired participation convention

At the future participation stage, an integrated task accepts the tariff iff its maximized continuation utility is **weakly nonnegative**. A task with exactly zero continuation surplus participates. Usage is then the unique maximizer of its strictly concave usage problem.

At the earlier integration stage, a task with sunk cost exactly equal to current benefit plus expected continuation rent integrates. Under the baseline continuous Uniform distribution this cutoff type has measure zero, so this convention does not change installed masses, but it completes the individual strategy.

This is now an explicit primitive of the repaired game rather than an implicit refinement. It is economically material for future participation because the provider sets a participation constraint exactly binding for a positive mass of low-use tasks.

## 2. Frozen economic primitives retained

There is one monopoly provider and two potential task classes `j in {L,H}`. Baseline future value is

`v_j(q)=a_j q-q^2/2`, with `0<c<a_L<a_H` and `d=a_H-a_L>0`.

Provider real inference cost is `c q`. Metering has real activation cost `mu>=0`. Integration costs are `k~Uniform[0,K_j]`. An integrated task receives non-expropriable current benefit `b_j>0` before future repricing.

Timing remains:

1. tasks choose integration;
2. current benefit is realized;
3. provider observes installed masses `(l,h)`;
4. provider chooses tariff architecture and tariff parameters;
5. integrated tasks choose future participation and usage.

The anonymous tariff family remains `T(q)=F+p q`, with flat architecture `p=0` and metered/hybrid architecture `p>0`.

## 3. Primitive continuation reduction

For a fixed usage price `p`, define

`q_j(p)=max{a_j-p,0}`

and

`S_j(p)=max{a_j-p,0}^2/2`.

Under the repaired weak-participation convention, a fixed fee equal to a participation threshold implements that participation set exactly.

For any installed masses `(l,h)`, provider profit is increasing in `F` while the participation set is unchanged. Since `S_H(p)>=S_L(p)`, every global continuation optimum can therefore be represented by one of three participation regimes:

- **both served:** `F=S_L(p)`;
- **H-only:** `F=S_H(p)` with L excluded whenever H is present;
- **no service:** zero continuation profit.

With positive installed H mass, an L-only tariff cannot be implemented by an anonymous tariff because any tariff accepted by L is also accepted by H. When `h=0`, the both-served formula simply reduces to the single installed L class.

Negative fixed fees are never optimal: replacing `F<0` by `F=0` weakly raises provider revenue without excluding a task whose gross surplus is nonnegative. Prices at or above `a_H` produce zero usage and are weakly dominated by flat no-service. Hence the global continuation problem has a finite candidate reduction and a maximizer at every installed-state history.

### Flat architecture

At `p=0`, the candidate continuation profits are

`Pi_F^B(l,h)=(l+h)a_L^2/2-c(l a_L+h a_H)`,

`Pi_F^H(h)=h a_H^2/2-c h a_H`,

and `0`.

Thus the flat continuation value is

`V_F(l,h)=max{Pi_F^B(l,h), Pi_F^H(h), 0}`.

### Metered architecture

On the both-served branch,

`Pi_M^B(p|l,h)=(l+h)(a_L-p)^2/2+(p-c){l(a_L-p)+h(a_H-p)}`.

Its derivative and curvature are

`d Pi_M^B/dp = d h-(l+h)(p-c)`,

`d^2 Pi_M^B/dp^2=-(l+h)<0`.

Hence, whenever the both-served optimum is interior,

`p_B(l,h)=c+d h/(l+h)`.

For the H-only branch,

`Pi_M^H(p|h)=h[(a_H-p)^2/2+(p-c)(a_H-p)]`,

so

`d Pi_M^H/dp=h(c-p)` and `d^2 Pi_M^H/dp^2=-h`; therefore the H-only optimum is `p_H=c`, with gross value

`Pi_M^H(h)=h(a_H-c)^2/2`.

For arbitrary off-path states where the unconstrained both-served price reaches the L choke price, the both-served candidate is interpreted as the constrained maximum over `0<p<=a_L`; the H-only candidate and no-service candidate remain in the global comparison. Thus

`V_M(l,h)=max{max_{0<p<=a_L} Pi_M^B(p|l,h), Pi_M^H(h), 0}`.

Metering activation cost is paid only when the metered architecture is selected. The provider's global architecture best-response correspondence at every installed state is therefore determined by comparing `V_F(l,h)` with `V_M(l,h)-mu`. Equality permits any mixture; strict inequality gives the unique architecture best response. This correspondence, not the regular-branch formula, defines off-path continuation play.

## 4. Rational-expectations candidate-state bound

Let

`R_F=(a_H^2-a_L^2)/2`,

`l=b_L/K_L`,

`h_0=b_H/K_H`,

`h_F=(b_H+R_F)/K_H`.

Under every provider continuation candidate above, L future continuation rent is zero: L either has a binding participation constraint or is excluded. Hence the L installed mass is always `l` in any rational-expectations candidate.

H continuation rent is:

- `R_F` under both-served flat pricing;
- `R_F-d p` under both-served metering;
- `0` under H-only or no-service.

Therefore every rational-expectations candidate H installed mass lies in the closed interval

`h in [h_0,h_F]`.

This observation is the key repair for the prior alternative-equilibrium / active-set gap: it identifies the entire installed-state interval on which strict both-served dominance must be checked, rather than only the preferred `[h_M,h_F]` interval.

## 5. Repaired strict regular region R+

The repaired headline theorem is restricted to the strict region `R+` defined by:

1. `0<c<a_L<a_H`, `K_L,K_H>0`, `b_L,b_H>0`;
2. `l=b_L/K_L in (0,1)`;
3. `d c < b_H+R_F < K_H`, so the metered fixed point has a positive endpoint sign and `h_F<1`;
4. `p_B(l,h_F)<a_L`, so the both-served metered optimum is interior for every `h in [h_0,h_F]`;
5. `Pi_F^B(l,h_0)>0` and `Pi_F^B(l,h_F)>0`, so flat both-served pricing beats no-service on the entire candidate interval (the flat payoff is affine in `h`);
6. `Pi_F^B(l,h_F)>Pi_F^H(h_F)`;
7. `Pi_M^B(p_B(l,h_F)|l,h_F)>Pi_M^H(h_F)`.

Conditions 6--7 imply strict both-served dominance over H-only throughout `[h_0,h_F]`. For flat pricing,

`d[Pi_F^H-Pi_F^B]/dh=R_F>0`.

For metered pricing, writing `x=a_L-c>0`,

`d[Pi_M^H-Pi_M^B]/dh`

`= d{d l^2+2x(h+l)^2}/[2(h+l)^2] > 0`.

Thus checking strict dominance at `h_F` is sufficient for the whole candidate interval. The metered both-served payoff is strictly positive when `p_B<a_L`, because its fixed fee is positive and `p_B-c>=0`.

`R+` is deliberately stronger and more transparent than the superseded Stage-8 wording. No theorem is claimed for all positive parameters.

## 6. Repaired regular-branch objects

On `R+`, both architectures strictly use the both-served continuation for every rational-expectations candidate state.

Flat expectation therefore gives

`h_F=(b_H+R_F)/K_H`.

Metered expectation gives the unique root `h_M` of

`K_H h=b_H+R_F-d[c+d h/(l+h)]`.

Define

`g(h)=b_H+R_F-d[c+d h/(l+h)]-K_H h`.

Because `p_B(l,h_0)<a_L<(a_H+a_L)/2`,

`g(h_0)=R_F-d p_B(l,h_0)>0`.

Also `g(h_F)=-d p_B(l,h_F)<0`, and

`g'(h)=-K_H-d^2 l/(l+h)^2<0`.

Hence there is exactly one `h_M in (h_0,h_F)`.

The provider's gross metering gain on this strict both-served interval is unchanged:

`Phi(l,h)=(l+h)/2 [c+d h/(l+h)]^2`,

with `Phi_h>0`.

Thus

`mu_M=Phi(l,h_M)<Phi(l,h_F)=mu_F`.

For `mu_M<mu<mu_F`, pure flat and pure metered expectations each induce a profitable architecture deviation. Since `R+` rules out H-only/no-service as alternative rational-expectations continuation regimes throughout the complete candidate-state interval, the hidden-pure-equilibrium objection is also closed on the claimed domain.

## 7. Exact certified example under R+

For

`a_L=4, a_H=5, c=1, b_L=16/5, K_L=4, b_H=1/2, K_H=8, mu=13/10`,

`l=4/5`, `h_0=1/16`, `R_F=9/2`, and `h_F=5/8`.

At `h_0`:

- flat both-served profit is `271/80>0`;
- flat both-served exceeds flat H-only by `467/160>0`;
- metered both-served exceeds metered H-only by `18677/5520>0`.

At the worst active-set endpoint `h_F`:

- `p_B=82/57<a_L`;
- flat both-served exceeds flat H-only by `31/80>0`;
- metered both-served exceeds metered H-only by `3533/2280>0`.

The familiar equilibrium objects remain

`h_M=(sqrt(2849)-17)/80 ~= 0.454700307254`,

`mu_M ~= 1.164441597721 < 1.3 < 1.474561403509 ~= mu_F`.

Thus the Stage-11B repair does not change the exact regular example or the core threshold-separation mechanism.

## 8. Scope counterexample retained

At `a_L=4, a_H=5, c=1, l=0.1, h=0.6`, flat H-only profit exceeds flat both-served profit by exactly `23/10`. The repaired theorem therefore remains explicitly branch/domain restricted. The off-path continuation correspondence is globally defined, but a global equilibrium characterization outside `R+` is not asserted.

## 9. Change-control consequences

This repair changes the explicit game definition and narrows/clarifies the theorem domain. Accordingly:

- the old Stage-8 freeze and Stage-7.5A economic statement-fidelity certificate are stale;
- Stage 4A must be repeated immediately;
- if Stage 4A passes, the mandatory downstream sequence is Stage 6 novelty re-kill / ratification, Stage 7 regression, Stage 7.5, Stage 7.5A (including a renewed formal-verification fidelity gate), and Stage 8 refreeze before manuscript work resumes;
- the existing Lean source may remain mathematically valid as a conditional algebraic artifact, but it is not a certificate of the repaired participation/global-continuation game until Stage 7.5A is rerun.

## Final routing

**STAGE 4R REPAIR PASS — GO TO REPEATED STAGE 4A.**
