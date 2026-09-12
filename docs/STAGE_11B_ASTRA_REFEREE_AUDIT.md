# Stage 11B — Independent Referee Audit

## Dynamic Tariff Choice for Generative AI: Model Improvement, Commitment, and Welfare

- Canonical theory-freeze commit: `2597e82044ec94a58fad033227ea415e64af8c6d`
- Stage-10 manuscript closeout commit: `c6325c169efaeac14fe9c563281fee5252940255`
- Current stage audited: Stage 11 — Robustness / Referee Attack Gate
- Independent verification code: `verification/stage11b_astra_independent_audit.py`

This audit was conducted independently of any other Stage-11 referee report, repair proposal, or verdict. Existing Stage-8 freeze records, theorem certificates, welfare records, Lean artifacts, and production verification code were treated as audit objects rather than correctness evidence. Core calculations were reconstructed from primitive payoffs and, where numerical work was used, through a separate direct-payoff path.

---

## 1. Executive verdict

The central strict regular-branch mathematics survived the hostile audit. In particular, on the certified both-served branch, I independently recover

\[
0<h_M<h_F,\qquad \Phi_h>0,\qquad \mu_M<\mu_F,
\]

and the candidate-deviation logic for

\[
\mu_M<\mu<\mu_F
\]

is correct: a flat expectation induces a state at which the provider wants to meter, while a metered expectation induces a state at which the provider wants to return to flat. In the frozen numerical baseline the independent calculation yields approximately

\[
h_M=0.4547003,\qquad h_F=0.625,
\]

\[
\mu_M=1.1644416<1.3<1.4745614=\mu_F.
\]

I did not find a hidden H-only, L-only, zero-service, zero-profit, or boundary pure equilibrium that survives inside the strict certified regular region and invalidates Proposition T3.

However, the present Stage-11 gate should not pass. Two defects invalidate inheritance of the Stage-4A continuation certification.

First, the continuation tariff repeatedly sets the low type exactly at its participation constraint, `F=S_L(p)`. The frozen game states voluntary participation but does not specify the tie-breaking rule when a positive mass of type-L tasks obtains exactly zero continuation surplus. This is not a measure-zero issue: the entire installed L mass is indifferent. Under unfavorable tie-breaking, the advertised both-served allocation at the exact fee is not implemented; the provider instead faces a supremum problem with `F=S_L(p)-epsilon`. Thus the continuation equilibrium/payoff correspondence is not fully defined by the stated primitives.

Second, the manuscript invokes rational-expectations/subgame-perfect continuation logic, but the Stage-4A certification does not fully define and solve provider continuation strategies after all off-path installed states, active-set switches, and participation boundaries. The workflow itself requires ties, participation changes, active sets, and every off-path continuation relevant to an upstream deviation to be explicitly defined and solved.

These are **CERTIFICATION REGRESSION** findings. They do not amount to a counterexample to the strict regular-branch algebra, but they do invalidate the current equilibrium certification.

**Final Stage-11 verdict: REOPEN EARLIER STAGE / NO-GO.**

Earliest rollback stage: **Stage 4A**.

---

## 2. Top 5 rejection risks

### Risk 1 — Participation tie-breaking is missing

**Attack**  
The provider sets `F=S_L(p)`, so type L receives exactly zero future utility. Under the stated voluntary-participation rule, why must all L tasks participate rather than reject?

**Severity**  
**MAJOR BUT FIXABLE**

**Exact evidence**  
The model/freeze specifies voluntary participation but no tie-breaking rule. The equilibrium derivation nevertheless counts all L tasks as participants when the L participation constraint binds exactly.

**Mathematical/economic consequence**  
The exact continuation payoff is not defined without a selection convention. If zero-surplus users reject, the advertised tariff is not both-served. The provider can approach the same payoff through `F=S_L(p)-epsilon`, but may fail to attain the closed-form maximum. This affects the game-theoretic status of the continuation problem, the definition of `Phi`, and the subgame-perfect interpretation.

**Can the paper answer now?**  
No. The convention is not stated in the frozen model.

**Required fix**  
Explicitly define participation at zero utility and re-certify all binding-PC continuation problems. Alternatively reformulate the provider problem with strict participation and characterize the resulting limiting/supremum solution.

**Earliest affected stage**  
Stage 4A.

**Certification regression?**  
**YES — CERTIFICATION REGRESSION.**

---

### Risk 2 — Off-path SPNE continuation is incomplete

**Attack**  
Are provider strategies and active-set choices fully defined for every installed state that can arise after an off-path history?

**Severity**  
**MAJOR BUT FIXABLE**

**Exact evidence**  
The paper expressly restricts its theorem to a regular both-served branch and does not globally characterize the continuation game outside that branch. This is acceptable for a branch-specific theorem but is not sufficient by itself for a literal subgame-perfect strategy profile over the full game.

**Mathematical/economic consequence**  
The on-path T1–T3 result may remain valid, but the stronger equilibrium certification is incomplete until off-path provider best responses are defined over all relevant states.

**Can the paper answer now?**  
Only partially. The model acknowledges the scope restriction but does not complete the strategy correspondence.

**Required fix**  
Either (i) define and solve the provider continuation correspondence globally across both-served, H-only, L-only where feasible, and no-service regions; or (ii) narrow the equilibrium language to the branch-specific rational-expectations object actually certified.

**Earliest affected stage**  
Stage 4A.

**Certification regression?**  
**YES — CERTIFICATION REGRESSION.**

---

### Risk 3 — The abstract generality theorem is largely order-preserving tautology

**Attack**  
Does the Stage-7.5A sufficient-condition theorem add economic content, or merely state that a strictly increasing function preserves order?

**Severity**  
**MAJOR BUT FIXABLE**

**Exact evidence**  
The formal theorem `threshold_separation` assumes both `StrictMono Psi` and `hM<hF` and concludes `Psi(hM)<Psi(hF)` directly.

**Mathematical/economic consequence**  
The economic work lies entirely in primitive conditions implying the state ordering and gain monotonicity. The abstract result itself is a useful organizational lemma, not substantive generality.

**Can the paper answer now?**  
Yes, if it keeps the claim narrow. The manuscript already avoids claiming arbitrary concave utility.

**Required fix**  
Do not sell the abstract implication as a broad robustness theorem. Either derive economically interpretable primitive sufficient conditions or explicitly label it as an order-theoretic reduction.

**Earliest affected stage**  
Stage 7.5A only if current wording is retained as substantive generality; otherwise Stage 10 exposition.

**Certification regression?**  
NO.

---

### Risk 4 — The regular region does substantial economic work

**Attack**  
Does the headline mechanism survive when active sets change near the boundary of the certified region?

**Severity**  
**MAJOR BUT FIXABLE**

**Exact evidence**  
The exact outside-region example `a_L=4, a_H=5, c=1, l=0.1, h=0.6` independently reproduces the H-only flat advantage

\[
\frac{23}{10}=2.3.
\]

A direct active-set comparison at `a_L=4, a_H=5, c=1, l=0.1` gives approximate switching points

\[
h^{flat}_{switch}=0.0888889,
\]

\[
h^{meter}_{switch}=0.1402700.
\]

Hence there is a neighborhood in which flat pricing chooses H-only while metered pricing still serves both types.

**Mathematical/economic consequence**  
Crossing the boundary of `R` changes not only the provider price formula but also the future rent map that determines integration. The headline state-regime feedback can therefore change discontinuously across active-set boundaries.

**Can the paper answer now?**  
Yes on scope: the manuscript expressly restricts the theorem. No on broad economic generality.

**Required fix**  
Make the active-set restriction economically transparent and, ideally, state explicit primitive inequalities defining the region rather than leaving part of `R` as a certified global-optimality condition.

**Earliest affected stage**  
Stage 7.5A / Stage 10 exposition unless the theorem domain itself is altered.

**Certification regression?**  
NO.

---

### Risk 5 — Novelty survives, but narrowly

**Attack**  
Is the contribution more than sunk investment/hold-up plus a new AI application?

**Severity**  
**MAJOR BUT FIXABLE**

**Exact evidence**  
The neighboring literature already contains: unlimited vs usage pricing and metering costs; forward-looking adoption under future pricing; sunk platform participation followed by later pricing; tariff form as a commitment device; subscription/pay-per-use/business-model choice; dynamic cloud contracts; and two-part tariff implementation for AI/LLM services.

**Mathematical/economic consequence**  
The paper cannot credibly claim novelty for hold-up, lack of commitment, mixed pricing-regime equilibrium, subscription vs usage pricing, two-part tariffs, or AI pricing as such. The surviving novelty is narrower: expected architecture changes the installed state, and that state in turn changes the provider's incentive to choose the same architecture, splitting one static threshold into two self-consistency thresholds.

**Can the paper answer now?**  
Partly. The current introduction is cautious, but the contribution remains thin for IJIO unless the reciprocal feedback is made more economically substantive.

**Required fix**  
Position the contribution exclusively around the reciprocal state-architecture feedback and perform a direct closest-paper absorption comparison.

**Earliest affected stage**  
Stage 6/7 literature positioning or Stage 10 exposition; theory reopen only if a stronger result is pursued.

**Certification regression?**  
NO.

---

## 3. Referee A — novelty / mechanism

**Verdict: MAJOR BUT FIXABLE.**

The closest prior work materially narrows the novelty claim.

- Sundararajan (2004) already studies unlimited-usage versus usage-based pricing and costly administration of usage pricing.
- Gans (2012) already studies sunk platform/device access before later application pricing and shows that expectations of later pricing can undermine upstream adoption.
- Penmetsa, Gal-Or & May (2015) analyze dynamic subscription-service pricing with forward-looking adoption and commitment.
- Muthers & Wismer (2022) directly connect platform-specific sunk participation, hold-up, and tariff form.
- Ladas, Kavadias & Loch analyze selling versus pay-per-use business-model choice.
- Recent subscription/pay-per-use papers compare subscription, spot, and two-part tariffs in multi-unit service settings.
- Bergemann, Bonatti & Smolin (2025) analyze LLM pricing and two-part tariff implementation.
- Bergemann & Wang (2025) analyze dynamic cloud pricing and committed-spend contracts.
- Bhaskaran, Erat & Mukherjee (2026) analyze prepaid digital services, including AI/cloud settings, and two-part tariffs/endogenous quality.
- Bichuch & Yaish (2026) analyze dynamic GenAI service pricing with costly use and future quality effects.

The strongest whole-game absorption candidate is Gans (2012). Under the natural translation,

- sunk AI integration corresponds to prior platform/device access;
- later tariff choice corresponds to later application pricing;
- future-price expectations reduce current integration/adoption;
- lack of commitment creates hold-up/unravelling.

This translation absorbs a large fraction of the intuition, but not the full headline theorem. The specific reciprocal loop

\[
\text{expected architecture}
\to
\text{installed composition}
\to
\text{provider architecture incentive}
\]

and the induced separation

\[
\mu_M<\mu_F
\]

are not simply restatements of the standard hold-up result.

**Novelty verdict:** survives, but only narrowly. The paper should not sell any broader ingredient as new.

The bibliographic reference in the audit prompt to “Wang & Hu” is not uniquely identifiable from author names alone. The closest recent subscription/spot-pricing work located should be checked against the intended reference before submission.

---

## 4. Referee B — mathematical validity / equilibrium set

The baseline regular-branch algebra is largely correct.

For fixed installed masses `(l,h)` and both classes participating, with `a_H=a_L+d`, the provider profit is

\[
\Pi_B(p)
=(l+h)\frac{(a_L-p)^2}{2}
+(p-c)\{l(a_L-p)+h(a_H-p)\}.
\]

Differentiation gives

\[
\Pi_B'(p)=dh-(l+h)(p-c),
\]

so the unique interior optimum is

\[
p^*(h)=c+d\frac{h}{l+h}.
\]

The second derivative is

\[
\Pi_B''(p)=-(l+h)<0.
\]

Thus the FOC/SOC calculation is valid on the both-served branch.

The gross metering advantage over optimized flat pricing simplifies to

\[
\Phi(l,h)=\frac{l+h}{2}
\left(c+d\frac{h}{l+h}\right)^2.
\]

The derivative is positive for positive `c,d,l` and nonnegative `h`:

\[
\Phi_h
=
\frac{[c(l+h)+dh][c(l+h)+dh+2dl]}{2(l+h)^2}>0.
\]

The material mathematical defect is not the branch algebra but the unmodeled participation tie and incomplete whole-game continuation strategy.

---

## 5. Referee C — welfare / benchmark / institution

The paper correctly distinguishes three objects:

1. the true first best, in which the planner chooses integration and usage directly;
2. a fixed-installed-base comparison of decentralized tariffs;
3. endogenous-integration welfare under architecture commitment.

For an integrated class-j task, the unrestricted planner chooses

\[
q_j^{FB}=a_j-c
\]

and integrates when

\[
k\le b_j+\frac{(a_j-c)^2}{2}.
\]

The fixed-base private/social threshold identity independently reproduces

\[
\mu_P-\mu_W=dhp^*(h)>0.
\]

This does **not** imply a global statement that the monopolist meters “too much” in the endogenous game. The manuscript correctly avoids that inference.

I independently verified sign reversal in the endogenous architecture comparison: admissible parameterizations exist with `W_M-W_F>0` and others with `W_M-W_F<0`. Thus the paper's claim of no unconditional endogenous welfare ranking is correct.

Institutionally, the paper is appropriately cautious. Real-world enterprise AI/cloud markets do exhibit fixed-access, usage-linked, hybrid, and committed-spend contracts. But there is no established fact in the cited institutional material that installed AI integration causally induces providers to switch tariff architecture. That channel must remain labeled a model interpretation, not an observed market fact.

---

## 6. Referee D — exposition / journal fit / claim scope

The most conspicuous exposition problem is the working title phrase **“Model Improvement.”**

The baseline does not endogenize model quality, and the discussion only offers a conditional quality interpretation: if an exogenous quality index moves both thresholds monotonically relative to the fixed activation cost, then a flat-to-mixed-to-metered path may arise.

That is weaker than what the title suggests.

**Severity:** MAJOR BUT FIXABLE.

**Bounded fix:** remove “Model Improvement” from the title and keep the quality discussion conditional.

**Theory-changing alternative:** retain the title only after proving a genuine model-improvement/quality comparative-static theorem. That would require reopening theory.

For IJIO/JIE-level placement, the current risk is not obviously incorrect mathematics but limited theoretical depth once the contribution is properly netted against the existing hold-up, subscription-pricing, platform-fee, and cloud-pricing literatures.

---

## 7. Primitive re-derivation of continuation pricing

### Both-served branch

For `p<a_L`, type-j usage is

\[
q_j=a_j-p.
\]

Indirect gross surplus before the fixed fee is

\[
S_j(p)=\frac{(a_j-p)^2}{2}.
\]

Since `S_H(p)>S_L(p)`, the provider extracts the low type's continuation surplus through

\[
F=S_L(p),
\]

subject to the unresolved zero-surplus participation convention.

Substitution produces

\[
\Pi_B(p)
=(l+h)S_L(p)
+(p-c)[lq_L(p)+hq_H(p)].
\]

FOC and SOC give

\[
p^*(h)=c+d\frac{h}{l+h},
\qquad
\Pi_B''(p)=-(l+h)<0.
\]

Feasibility requires the relevant price to satisfy

\[
0<p^*(h)<a_L.
\]

The lower inequality follows from `c>0`. The upper inequality is a substantive domain restriction.

### H-only branch

With only H participating,

\[
F=S_H(p),
\]

and

\[
\Pi_H(p)
=h\left[
\frac{(a_H-p)^2}{2}
+(p-c)(a_H-p)
\right].
\]

For the quadratic baseline, the unique optimum is

\[
p_H^*=c.
\]

### L-only branch

Under a common anonymous tariff, a genuine L-only continuation is infeasible: any tariff acceptable to L gives H at least as much gross surplus because `a_H>a_L`.

### F=0

With a positive mass of participating users, `F=0` is generally dominated by increasing the fixed fee until a participation constraint binds.

### p at participation boundaries

`p=a_L` is the boundary at which L demand collapses to zero and the solution becomes effectively H-only. For `p>=a_H`, both demands are zero.

### Zero service / zero demand

A metered zero-demand continuation pays the activation cost without generating usage and is weakly dominated by a flat no-service continuation when the provider can choose architecture freely.

---

## 8. Candidate-deviation re-audit

Under a flat expectation, the high-use installed state is `h_F`. The provider's deviation gain from activating metering is

\[
\Phi(l,h_F)-\mu=\mu_F-\mu.
\]

For `mu<mu_F`, flat is not self-consistent.

Under a metered expectation, the installed state is `h_M`. The provider's net metering gain is

\[
\Phi(l,h_M)-\mu=\mu_M-\mu.
\]

For `mu>mu_M`, metering is not self-consistent.

Therefore, for

\[
\mu_M<\mu<\mu_F,
\]

both candidate pure expectations fail. This result is independently reproduced.

---

## 9. Alternative-equilibrium search

The audit deliberately searched for alternatives rather than stopping after candidate-deviation failure.

Examined possibilities included:

- H-only continuation;
- L-only continuation;
- one type indifferent;
- both types indifferent;
- `F=0`;
- `p=0`;
- participation-boundary pricing;
- zero demand;
- zero provider profit;
- no integration;
- full integration;
- one integration class exactly at its cutoff;
- provider architecture indifference;
- user integration indifference;
- economically admissible nongeneric boundary cases.

No additional pure equilibrium was found inside the strict certified regular region that invalidates T3.

A useful hostile check is the H-only expectation. If H expects zero continuation rent under H-only pricing, its installed mass is

\[
h_0=b_H/K_H.
\]

Because metered continuation still leaves positive H rent on the regular branch,

\[
h_0<h_M<h_F.
\]

For the quadratic baseline, the H-only relative-profit advantage is increasing in h. Therefore, if both-served globally dominates H-only throughout the certified interval `[h_M,h_F]`, it also dominates at the still lower `h_0`. Thus the H-only pure-equilibrium attack is a **FALSE POSITIVE / NO ISSUE** inside the stated domain.

---

## 10. Boundary / active-set / H-only audit

For flat pricing, the difference between H-only and both-served profits can be written as

\[
D_F(h)
=hR_F-l\left(\frac{a_L^2}{2}-ca_L\right),
\]

so

\[
D_F'(h)=R_F>0.
\]

For optimized metering, the independent derivative of the H-only relative-profit advantage is

\[
D_M'(h)
=
\frac{
 d\{2(a_L-c)(h+l)^2+d l^2\}
}{2(h+l)^2}>0.
\]

Thus active-set changes are economically systematic rather than isolated computational failures.

In the retained outside-region example,

\[
a_L=4,\quad a_H=5,\quad c=1,\quad l=0.1,\quad h=0.6,
\]

both-served flat profit is

\[
\frac{11}{5},
\]

while H-only flat profit is

\[
\frac{9}{2},
\]

so H-only wins by

\[
\frac{23}{10}.
\]

Near the boundary at `l=0.1`, flat and metered active-set switching occur at different h values, so the two architectures can imply different participation sets. In that region the simple formulas for `h_F`, `h_M`, and the rent difference no longer describe the whole game.

This does not refute the branch-specific theorem, but it confirms that `R` does substantial economic work.

---

## 11. Indifference and multiplicity audit

The paper explicitly excludes `mu=mu_M` and `mu=mu_F` from the strict headline theorem. That is appropriate because the provider is indifferent on those boundaries.

In the mixed equilibrium, provider indifference is intentional and pins down the installed state.

Integration-cost cutoff indifference occurs only for a zero-measure set of atomless users under a continuous cost distribution and does not create aggregate multiplicity.

The material exception is the type-L participation constraint under the provider tariff. Because **all installed L tasks** receive exactly zero continuation utility at `F=S_L(p)`, their participation indifference is a positive-mass phenomenon and must be explicitly resolved in the game definition.

---

## 12. Mixed-equilibrium existence and uniqueness audit

Inside the strict gap,

\[
\Phi(l,h_M)<\mu<\Phi(l,h_F).
\]

Because `Phi(l,h)` is continuous and strictly increasing in h, there is a unique

\[
h^*\in(h_M,h_F)
\]

such that

\[
\Phi(l,h^*)=\mu.
\]

At that state, if the provider meters with probability `rho`, H's expected continuation rent is

\[
R_F-\rho d p^*(h^*).
\]

The integration condition implies

\[
\rho^*
=\frac{K_H(h_F-h^*)}{d p^*(h^*)}.
\]

Positivity follows from `h^*<h_F`.

Define the metered fixed-point residual

\[
g(h)=b_H+R_F-dp^*(h)-K_Hh.
\]

Then

\[
g'(h)
=-K_H-\frac{d^2l}{(l+h)^2}<0.
\]

Since `g(h_M)=0` and `h^*>h_M`, we have `g(h^*)<0`, which is equivalent to

\[
K_H(h_F-h^*)<d p^*(h^*).
\]

Hence

\[
0<\rho^*<1.
\]

The mixed state and mixing probability are therefore unique on the regular branch, conditional on the stated continuation implementation.

**Severity of the mixed-equilibrium attack:** **FALSE POSITIVE / NO ISSUE** for the strict regular branch, aside from the participation-tie defect already identified.

---

## 13. Quantifier / functional-form red team

### Nonquadratic admissible utility where the mechanism survives

Using a common strictly concave cubic perturbation

\[
v_j(q)=a_jq-\frac{q^2}{2}-0.1\frac{q^3}{3},
\]

and independently reoptimizing the continuation problem from primitive demand and payoff expressions, the audit finds approximately

\[
h_M=0.3795827<h_F=0.4831025,
\]

with provider metering gain increasing over the relevant interval:

\[
\Psi(h_M)=0.6418619
<0.7562440=\Psi(h_F).
\]

Thus the headline mechanism is not merely an algebraic accident of the quadratic baseline.

### Counterexample to any arbitrary-concavity generalization

Strict concavity alone is insufficient. Consider a quadratic L type and an H type with

\[
v_H(q)=\frac{q}{0.6}\left[1+\ln(5/q)\right].
\]

At flat pricing,

\[
q_H(0)=5>4=q_L(0),
\]

and

\[
S_H(0)=8.333\ldots>8=S_L(0).
\]

Yet under an admissible metered continuation, the demand/surplus ordering can cross on the relevant price interval, producing approximately

\[
h_M=0.2119414>0.2=h_F.
\]

Thus neither concavity nor the label “high-use type” by itself implies the baseline state ordering.

The abstract sufficient-condition theorem is therefore valid but thin: all substantive economics lies in the primitive assumptions that generate `h_M<h_F` and `Psi'>0`.

**Certification regression?** NO, because the frozen manuscript does not claim arbitrary concave demand.

---

## 14. Welfare-selection audit

The benchmark taxonomy is correct.

### True first best

Planner chooses integration and usage directly:

\[
q_j^{FB}=a_j-c,
\]

and integration occurs if

\[
k\le b_j+\frac{(a_j-c)^2}{2}.
\]

### Fixed-installed-base comparison

Holding `(l,h)` fixed, provider and social thresholds differ by

\[
\mu_P-\mu_W=dhp^*(h)>0.
\]

This is a constrained decentralized-allocation comparison, not the first best.

### Endogenous integration comparison

Architecture expectations change installed h. Independent admissible parameter checks generate both

\[
W_M-W_F>0
\]

and

\[
W_M-W_F<0.
\]

Therefore no unconditional endogenous welfare ranking exists in the baseline family.

The paper's current welfare claim is appropriately narrow. Any statement such as “the monopolist meters too much” without the fixed-installed-base qualifier would be invalid.

---

## 15. Prior-art absorption test

### Closest-paper candidate: Gans (2012), *Mobile Application Pricing*

Translation into the present model:

- prior platform/device access -> sunk AI integration;
- later application price -> future provider tariff;
- expected future pricing reduces adoption -> expected metering reduces integration;
- lack of commitment -> pricing hold-up.

Under this translation, a large part of the economic intuition is already known.

However, the current main theorem is not fully absorbed. The extra object is the feedback

\[
\text{expected tariff architecture}
\to
\text{installed composition}
\to
\text{provider's later architecture payoff},
\]

which creates two self-consistency thresholds rather than only the standard investment/adoption hold-up effect.

### Absorption verdict

**Not fully absorbed, but novelty is narrow.**

The paper must not implicitly claim novelty for:

- sunk investment before repricing;
- lack of commitment;
- adoption responses to future prices;
- subscription versus usage pricing;
- two-part tariffs;
- tariff form as a commitment device;
- mixed strategy per se;
- AI/cloud as an application domain.

The defensible novelty claim is specifically the reciprocal state-regime feedback and threshold splitting.

---

## 16. Lean / formal-verification fidelity audit

The audited Lean file contains no visible `sorry`/`admit` in the proof-critical targets.

The formal artifact certifies conditional logical/algebraic facts including:

- threshold separation from `StrictMono Psi` and `hM<hF`;
- response reversal for a cost inside the strict gap;
- uniqueness of fixed points of antitone maps;
- conditional uniqueness of a mixed state;
- positivity of the supplied baseline `Phi_h` expression;
- exact arithmetic of the retained `23/10` scope counterexample.

The Lean file **does not prove**:

- demand derivation from primitive utility;
- global tariff optimization across active sets;
- participation implementation at binding fixed fees;
- the global continuation correspondence;
- existence of the baseline `h_M` from the complete economic game;
- that the supplied `Phi` expression equals the true global architecture payoff difference in every relevant subgame;
- existence of the mixed equilibrium as a full economic equilibrium;
- `0<rho<1` from the full primitives;
- absence of alternative pure equilibria;
- all off-path SPNE conditions;
- welfare accounting or first-best claims.

The formalization itself is reasonably transparent about these limits. The problem is not a false Lean proof; it is that formal success cannot substitute for the missing economic-game certification.

---

## 17. Evidence ledger for all material PASS findings

| Item | Audit result |
|---|---|
| Both-served `p*=c+dh/(l+h)` | PASS |
| SOC on both-served branch | PASS |
| `Phi=(l+h)(p*)^2/2` | PASS |
| Baseline `Phi_h>0` | PASS |
| `0<h_M<h_F` under strict baseline restrictions | PASS |
| `mu_M<mu_F` | PASS |
| Flat candidate fails in strict gap | PASS |
| Metered candidate fails in strict gap | PASS |
| Hidden H-only pure equilibrium inside strict R | PASS — not found; analytically excluded under maintained active-set dominance |
| L-only pure continuation | PASS — infeasible under anonymous tariff and ordered surplus |
| Zero-service hidden equilibrium inside strict R | PASS — not found |
| Unique mixed state `h*` | PASS |
| `0<rho*<1` | PASS |
| Mixed regular-branch uniqueness | PASS |
| Threshold collapse with architecture-insensitive integration | PASS |
| W1 fixed-installed-base welfare wedge | PASS |
| Endogenous welfare sign indeterminacy | PASS |
| Nonquadratic example preserving mechanism | PASS |
| Arbitrary-concavity generalization | FAIL if asserted; not currently asserted |
| Outside-R H-only counterexample | PASS |
| Lean conditional theorem fidelity | PASS with narrow scope |

---

## 18. Certification-regression ledger

### CR-1 — Participation tie not defined

**Status:** CERTIFICATION REGRESSION

**Earliest rollback:** Stage 4A.

**Missing workflow check:** ties, participation changes, and payoff-relevant boundary behavior must be defined over the complete game domain.

**Why material:** the exact optimized fixed fee places a positive mass of users at zero utility.

---

### CR-2 — Full off-path continuation not certified

**Status:** CERTIFICATION REGRESSION

**Earliest rollback:** Stage 4A.

**Missing workflow check:** every off-path state induced by upstream histories must have a valid downstream continuation before a subgame-perfect claim is certified.

**Why material:** active sets switch outside the regular interval, and the provider's continuation problem changes discretely.

---

No new certification regression was found for the Stage-7 welfare benchmark or the stated Stage-7.5A quantifiers. The nonquadratic counterexample only confirms that the existing prohibition on arbitrary-concavity language is necessary.

---

## 19. Consolidated severity table

| Finding | Severity | Certification regression? |
|---|---|---:|
| Participation tie rule absent | MAJOR BUT FIXABLE | YES — Stage 4A |
| Off-path SPNE continuation incomplete | MAJOR BUT FIXABLE | YES — Stage 4A |
| Core T1–T3 regular-branch algebra | FALSE POSITIVE / NO ISSUE | NO |
| Hidden H-only pure equilibrium inside R | FALSE POSITIVE / NO ISSUE | NO |
| Mixed equilibrium existence/uniqueness | FALSE POSITIVE / NO ISSUE | NO |
| R performs substantial economic work | MAJOR BUT FIXABLE | NO |
| Abstract sufficient-condition generality is thin | MAJOR BUT FIXABLE | NO |
| Arbitrary concavity would overturn state ordering | FALSE if asserted; currently not asserted | NO |
| Welfare benchmark accounting | FALSE POSITIVE / NO ISSUE | NO |
| Endogenous welfare sign indeterminacy | FALSE POSITIVE / NO ISSUE | NO |
| Novelty versus hold-up/pricing literature | MAJOR BUT FIXABLE | NO |
| “Model Improvement” in title | MAJOR BUT FIXABLE | NO |
| Lean proves full economic theorem | FALSE; formal file does not actually do so | NO |
| AI institutional causal interpretation | MINOR; current prose is sufficiently qualified | NO |

No **FATAL** mathematical counterexample to the frozen strict-`R` T1–T3 theorem was found.

---

## 20. Exact required repairs

1. Define participation at zero continuation surplus and re-certify every binding-participation continuation.
2. Re-run Stage 4A with a complete off-path continuation map and explicit active-set/corner outcome taxonomy.
3. Turn the regular-region global-active-set condition into transparent primitive or verifiable inequalities wherever possible.
4. Treat the abstract `StrictMono Psi + hM<hF` implication as an organizing lemma, not substantive functional-form robustness.
5. If robustness is intended to be a major contribution, derive primitive sufficient conditions such as relevant-price demand ordering/single crossing; otherwise retain narrow baseline claims.
6. Rewrite novelty positioning around reciprocal state-architecture feedback only.
7. Explicitly distinguish the contribution from Gans, Muthers–Wismer, Sundararajan, Penmetsa–Gal-Or–May, Min–Ryu, business-model-choice work, and 2024–2026 AI/cloud pricing papers.
8. Resolve the exact bibliographic identity of the “Wang & Hu” reference before submission.
9. Remove “Model Improvement” from the title unless a genuine quality/model-improvement comparative-static theorem is added.
10. Keep the current narrow welfare wording; do not convert W1 into a global policy claim.
11. Keep Lean/formal-verification claims conditional and explicitly state that participation tie-breaking and full off-path SPNE are outside the current formal scope unless later formalized.

---

## 21. Earliest rollback stage

**Stage 4A.**

The rollback is not triggered by failure of the strict regular-branch T1–T3 algebra. It is triggered by an incompletely specified continuation game and an incomplete subgame-perfect continuation certificate.

After repairing Stage 4A, Stage 7 and Stage 7.5A need only regression rechecks unless the model or theorem domain is changed materially.

---

## 22. Final Stage-11 verdict

# REOPEN EARLIER STAGE / NO-GO

The central branch-specific threshold-splitting mechanism survives independent primitive re-derivation, active-set attacks, mixed-equilibrium reconstruction, and a nonquadratic robustness check. I did not find a fatal counterexample to the strict baseline theorem.

Nevertheless, the current Stage-4A certification cannot be inherited because the game does not specify a payoff-relevant participation tie at the binding low-type constraint and does not fully certify off-path continuation strategies across active-set changes. Those are Stage-4A-level defects under the repository's own workflow.

The paper therefore should not proceed directly to journal positioning under the current certification state.

---

## IJIO referee classification

**Reject**

現状なら Reject に置く。中心的な regular-branch 数理は概ね正しく、pure-regime gap も単なる solver artefact ではない。しかし、participation tie-breaking と off-path continuation の未定義は SPNE certification 上の実質的欠陥である。さらに、Gans、Muthers–Wismer、Min–Ryu 等により「sunk investment × 将来価格 × hold-up」は既知で、残る新規性は二つの self-consistency threshold への分裂にかなり限定される。強い both-served restriction と、一般化定理が実質的に order-preserving lemma である点を考えると、現状の厚みでは IJIO 級の理論貢献として不足する。

---

## Literature / institutional audit notes

The novelty and institutional checks referenced the following literature families and current pricing institutions:

- Sundararajan (2004), *Nonlinear Pricing of Information Goods*.
- Gans (2012), *Mobile Application Pricing*.
- Penmetsa, Gal-Or & May (2015), *Dynamic Pricing of New Services in Subscription Markets*.
- Muthers & Wismer (2022), *Why Do Platforms Charge Proportional Fees? Commitment and Seller Participation*.
- Ladas, Kavadias & Loch, selling versus pay-per-use business-model choice.
- Min & Ryu, sunk investment followed by monopolistic two-part-tariff choice / hold-up.
- Bergemann, Bonatti & Smolin (2025), *The Economics of Large Language Models: Token Allocation, Fine-Tuning, and Optimal Pricing*.
- Bergemann & Wang (2025), *Optimal Pricing of Cloud Services: Committed Spend under Demand Uncertainty*.
- Bhaskaran, Erat & Mukherjee (2026), *Pay More, Use More: Consumer Bias and Demand Management for Digital Services*.
- Bichuch & Yaish (2026), *Freemium Is All You Need*.
- Current enterprise AI/cloud pricing examples including fixed access, usage credits, and committed-spend contracts.

The institutional distinction retained in this audit is:

- **FACT:** multiple pricing architectures and committed-spend contracts exist in AI/cloud markets.
- **SUGGESTIVE:** enterprise integration is costly and can precede future contract revisions.
- **MODEL INTERPRETATION:** installed integration causally changes a provider's incentive to switch tariff architecture.

The third statement is not established as a current empirical fact by the institutional material reviewed here.
