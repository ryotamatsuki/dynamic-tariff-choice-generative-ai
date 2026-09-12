# Stage 11 — Astra reservation repair and recheck

Date: 2026-09-13 (JST)  
Project: **Dynamic Tariff Choice for Generative AI: Integration, Commitment, and Welfare**  
Canonical workflow: `ryotamatsuki/research-paper-workflow`  
Audit target / repair base: `b85f386f458ed394d0df9b0f2af5b1de02c27d59`  
Repair branch: `repair/stage11-astra-reservations`

## 1. Incoming independent verdict

The independent Astra cross-check returned:

**PASS WITH MATERIAL RESERVATIONS / REPAIR WITHIN STAGE 11.**

The prior Stage-11 PASS and Stage-12 authorization were not used as evidence that the new reservations were resolved. This record is additive; `docs/STAGE_11_REFEREE_ATTACK_REPAIRED.md` and the historical audit branches remain unchanged provenance.

## 2. Current recheck verdict

**REPAIR WITHIN STAGE 11 — MATHEMATICAL REPAIRS IMPLEMENTED; LITERATURE-SOURCE BLOCKER REMAINS.**

No primitive, timing, strategy space, strict `R+` domain, T1--T3 theorem statement, B1, or W1 has been changed. The repair corrects manuscript characterization at equality boundaries and closes previously compressed arguments for global continuation, candidate-state completeness, and the strategic construction of the mixed equilibrium.

Stage 12 is fail-closed and remains paused because the complete published version of Hagiu (2006) could not be inspected in the current environment. The publisher abstract and a complete public working-paper predecessor were inspected and materially narrowed the novelty claim, but the user's repair rule explicitly prohibits a Stage-12 GO while a material literature comparison remains unresolved.

If the complete published Hagiu text later shows whole-game absorption of the paper's specific reciprocal architecture-state-profitability loop and its two-threshold/interior-mixing result, the earliest affected stage is **Stage 6**. Otherwise Stage 11 can be re-ratified without changing the certified theorem package.

## 3. Reservation A — pure-equilibrium equality boundaries

### Incoming issue

The manuscript said that pure metering was self-consistent only for `mu<mu_M` and pure flat pricing only for `mu>mu_F`, despite an equilibrium concept that permits provider indifference.

### Repair

The manuscript now states:

- pure metering is self-consistent iff `mu<=mu_M`;
- pure flat pricing is self-consistent iff `mu>=mu_F`;
- at `mu=mu_M`, aggregate consistency forces `h=h_M` and `rho=1`;
- at `mu=mu_F`, aggregate consistency forces `h=h_F` and `rho=0`;
- the interior mixed equilibrium remains restricted to `mu_M<mu<mu_F`.

At `mu=mu_M`, any `rho<1` raises expected H continuation rent at `h_M` by `(1-rho)d p*(h_M)>0`. The integration crossing therefore moves above `h_M`; strict monotonicity of `Phi` makes metering strictly optimal and contradicts `rho<1`. At `mu=mu_F`, any `rho>0` implies `K_H(h_F-h)=rho d p*(h)>0`, hence `h<h_F`; strict monotonicity gives `Phi(l,h)<mu_F`, so flat pricing is strictly optimal and positive metering probability is impossible.

The permanent exact example is retained:

- `l=4/5`;
- `h_0=1/16`;
- `h_M=(-17+sqrt(2849))/80`;
- `h_F=5/8`;
- `mu_M=-461/200+13 sqrt(2849)/200`;
- `mu_F=1681/1140`;
- at the flat boundary the tariff is `(F,p)=(8,0)`.

### Status

**RESOLVED mathematically and in manuscript.** This is a boundary characterization repair, not a change in T3's strict-middle theorem statement.

## 4. Reservation B — close global continuation inside the manuscript

Let `A=a_L`, `d=a_H-a_L`, and `n=l+h`. The repair derives the provider problem from user utility and active sets rather than relying on the both-served FOC/SOC.

For `0<=p<a_L`, optimal both-served fixed fee is `F=S_L(p)` because profit is strictly increasing in `F` within a positive active set. The exact both-served loss identity is

`B(p*)-B(p)=n(p-p*)^2/2`,

where

`p*=c+d h/n`.

Thus `p*` is the unique global both-served maximizer on the relevant price interval. Strict `R+` gives `0<p*<a_L`, so the open metered strategy set `p>0` attains the optimum.

The optimized metered both-served minus H-only gap is

`D_M(h)=l(A-c)^2/2-d(A-c)h-d^2 l h/[2(l+h)]`,

with

`D'_M(h)=-d(A-c)-d^2 l^2/[2(l+h)^2]<0`.

For flat pricing,

`D_F(h)=l(A^2/2-cA)-h d(2A+d)/2`,

and

`D'_F(h)=-d(2A+d)/2<0`.

Hence strict both-served dominance at `h_F` propagates to every candidate state below `h_F`.

The Appendix now explicitly covers:

- optimal fixed fees conditional on an active set;
- negative fixed-fee deviations;
- both-served, H-only, L-only, and no-service classifications;
- why anonymous tariffs make L-only infeasible with positive H mass;
- the zero-H-mass labeling exception;
- `p<a_L`, `p=a_L`, `a_L<p<a_H`, and `p>=a_H`;
- global H-only metered optimum at `p=c>0`;
- why no-service covers the zero-usage/subsidy boundary;
- endpoint propagation across the complete candidate interval.

### Status

**RESOLVED mathematically and in manuscript.** No new theory assumption was introduced.

## 5. Reservation C — candidate-state interval completeness

The repaired proof no longer starts by imposing `h in [h_0,h_F]`.

1. At any globally optimal continuation, L continuation rent is zero. When served, the optimal fixed fee binds the lowest active participation constraint; when not served, continuation value is zero.
2. Hence L integrates iff `k<=b_L`, so non-saturation yields `l=b_L/K_L`.
3. H continuation rent is in `[0,R_F]`: H-only/no-service give zero rent; a both-served tariff gives `R_F-dp`, and flat gives the upper endpoint `R_F`.
4. A provider mixture gives a convex combination of continuation rents in the same interval.
5. Since strict `R+` imposes `b_H+R_F<K_H`, H integration never saturates and every candidate satisfies `h in [h_0,h_F]`.
6. Only after that result is established are the strict endpoint-dominance conditions applied to the full candidate interval.

Weak participation is explicitly identified as necessary for exact fixed-fee attainment, and positive candidate masses/non-saturation are stated.

### Status

**RESOLVED.** No silent domain shrinkage occurred.

## 6. Reservation D — strategic construction of the mixed equilibrium

The repaired equilibrium section and Appendix now specify a complete on-path strategic construction.

At the unique `h*` satisfying `Phi(l,h*)=mu`, the provider is indifferent between the actual globally optimal tariffs

- flat: `(F_F,p_F)=(a_L^2/2,0)`;
- metered: `(F_M,p_M)=(S_L(p*(h*)),p*(h*))`.

The provider realizes the metered tariff with probability `rho`. Users integrate before the realization and evaluate realization-contingent future utility; they do not choose usage at an average marginal price.

Aggregation requires

`rho*=K_H(h_F-h*)/[d p*(h*)]`,

and the strict middle region yields `0<rho*<1`.

User integration strategies are

`x_L(k)=1{k<=b_L}`,

`x_H(k)=1{k<=b_H+R_F-rho* d p*(h*)}`.

Uniform costs aggregate these cutoffs to `l=b_L/K_L` and `h=h*`. Each atomless user's unilateral integration deviation leaves the aggregate state unchanged. Off path the provider uses the globally optimized continuation values `V_F` and `V_M`, mixing only at a genuine tie. The manuscript distinguishes uniqueness of the aggregate pair `(h*,rho*)` from uniqueness of every measure-zero cutoff action or off-path tie-breaking rule; no unnecessary independent user mixing is introduced.

### Status

**RESOLVED.**

## 7. Reservation E — prior-art re-kill

A new evidence table is stored in `docs/STAGE_11_ASTRA_REPAIR_PRIOR_ART.md`. The fresh comparison covers Hagiu (2006), Gans (2012), Muthers & Wismer (2022), Wang & Hu (2014), Min & Ryu (2025), Sundararajan (2004), and current LLM/cloud work.

The manuscript now explicitly abandons novelty for the generic timing loop

`expectations -> early participation/investment -> later pricing`.

The remaining candidate contribution is narrower:

`anticipated tariff architecture -> sunk installed composition -> relative profitability of tariff architectures -> ex-post architecture choice`,

with two expectation-contingent thresholds and an interior provider-mixing region.

### Hagiu source status

Hagiu is the strongest threat. The publisher abstract confirms seller-before-buyer arrival, fixed and variable fees, and endogenous commitment to buyer price. A complete 60-page public predecessor was inspected and confirms a timing in which the platform can either announce all prices early or announce seller terms and wait to set the user price later after the seller-side environment is determined.

However, the complete published RAND version of record could not be retrieved in the current environment. The available publisher PDF is restricted and the ResearchGate record exposes only a request-full-text route. The current evidence is enough to kill generic timing/commitment novelty and to narrow the manuscript, but not enough under the user's explicit rule to close the whole-game absorption test conclusively.

### Status

**UNRESOLVED SOURCE LIMITATION.** Stage 12 remains paused. If the published full text reveals absorption, roll back to Stage 6.

## 8. AI positioning and assumption dependence

The abstract, introduction, discussion, and conclusion now state that AI is a motivating application, not a theorem-specific primitive. The same formal mechanism can represent other digital services with sunk integration, heterogeneous future usage value, and noncommitted future tariff architecture. No new AI-specific model was introduced.

Assumption dependence is recorded rather than generalized away:

- two types and uniform integration costs: tractability / one-dimensional cutoffs; no broader distribution theorem;
- quadratic common-curvature utility: qualitatively important for the certified ordering; arbitrary strict concavity is prohibited by the permanent counterexample;
- anonymous tariffs: substantive for the active-set ordering and impossibility of L-only screening with positive H mass;
- monopoly and noncommitment: substantive game-form assumptions;
- weak participation: essential for exact binding fixed-fee implementation; no strict-participation equivalence theorem;
- real activation cost `mu`: needed for a nondegenerate switching margin but insufficient by itself to create threshold separation, as the architecture-insensitive benchmark shows.

The GenAI-forward title versus a more general digital-service title is deliberately left to Stage 12 after the Stage-11 literature blocker is closed.

## 9. Verification architecture

The historical verifier `verification/stage11_repaired_independent.py` is preserved. The additive `verification/stage11_astra_repair_verify.py` independently checks:

- the exact square-loss identity;
- exact `D_M`, `D'_M`, `D_F`, and `D'_F` formulas;
- a direct user-utility-derived provider-profit evaluator;
- all active-set price boundaries through and beyond `p=a_L` and `p=a_H`;
- explicit negative fixed-fee probes;
- exact `mu_M` and `mu_F` boundary conditions;
- candidate-interval rent identities;
- the interior mixed-equilibrium cutoffs and aggregation;
- manuscript guards for the repaired boundary and strategic-language statements.

The script does not treat NaN, nonconvergence, or a missing solver branch as evidence that no deviation exists. It does not call the production continuation solver.

No new Lean theorem has been added. The existing Lean target is rerun by the unchanged formal-build job as a regression check; successful rerun must not be described as formal verification of the new prose-level active-set or boundary arguments.

## 10. Welfare/formal regression status

The repair does not change W1 or its benchmark. Transfers still cancel in social welfare; `mu` and integration costs remain real resource costs; fixed-installed-base and endogenous-integration welfare comparisons remain separate. The formal-verification coverage ceiling is unchanged.

## 11. Files changed in this repair

- `sections/00_abstract.tex`
- `sections/01_introduction_repaired.tex`
- `sections/02_model.tex`
- `sections/03_equilibrium.tex`
- `sections/07_related_literature_repaired.tex`
- `sections/08_discussion.tex`
- `sections/09_conclusion.tex`
- `sections/10_appendix.tex`
- `references/frontier.bib`
- `references/extra.bib`
- `verification/stage11_astra_repair_verify.py` (new)
- `Makefile`
- `.github/workflows/verify.yml`
- `docs/STAGE_11_ASTRA_REPAIR_PRIOR_ART.md` (new)
- `docs/STAGE_11_ASTRA_REPAIR_RECHECK.md` (new)
- `theorem_certificates/current_scope.md`
- `STATUS.md`

## 12. Gate routing

Current verdict before final branch CI closeout:

**REPAIR WITHIN STAGE 11.**

Even if the mathematical, Lean-regression, reproducibility, figure/table, and manuscript-build checks are green, the unresolved published-Hagiu source comparison keeps Stage 12 unauthorized under the user-specified fail-closed rule. The CI closeout evidence and PR identity are to be appended/recorded after the final repair HEAD is tested.
