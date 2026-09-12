# Stage 11 — Repaired Full-Manuscript Referee Attack Gate

Date: 2026-09-12 (JST)  
Project: **Dynamic Tariff Choice for Generative AI: Integration, Commitment, and Welfare**  
Canonical workflow: `ryotamatsuki/research-paper-workflow` v2.1  
Audit base: repaired full draft / administrative `main` head `026051f09cbfff564e4a094a437a53c653d26484`  
Independent audit branch: `audit/stage11-repaired-independent`

## 1. Canonical verdict

**GO — REFEREE ATTACK GATE PASS.**

No fatal attack survives against the repaired theorem package or the manuscript's current scoped claims. No Stage-4A or Stage-7.5A certification regression was found. The repaired full draft may proceed to **Stage 12 — Journal Positioning** after the Stage-11 closeout CI is green.

The verdict is deliberately narrow. The surviving contribution remains an interaction result: anticipated tariff architecture changes the sunk installed high-use state, and that state changes the provider's later relative gain from the same architecture, splitting one fixed-state threshold into two self-consistency thresholds. Generic hold-up, fixed-versus-usage pricing, two-part tariffs, mixed pricing equilibria, AI/cloud application, and a generic private/social wedge remain non-contributions.

## 2. Independence and attack protocol

The pre-repair branch `audit/stage11b-astra-independent` was retained but **not inherited**. This Stage 11 starts from the repaired Stage-10 manuscript and reconstructs high-risk objects from primitives.

A new permanent audit script, `verification/stage11_repaired_independent.py`, checks:

1. the exact frozen baseline independently;
2. the endpoint-propagation identities behind global both-served continuation on `[h_0,h_F]`;
3. finite price deviations using a clean-room direct payoff evaluator that enumerates both-served, H-only, and no-service regimes;
4. T1/T2 threshold objects in the exact example;
5. the permanent `23/10` outside-domain guard;
6. an admissible strictly-concave nonbaseline counterexample showing why arbitrary strict-concavity scope is prohibited.

The script is wired into `make verify-python` and the independent `verify` workflow.

## 3. Mathematical / continuation attack

### 3.1 Global continuation over the certified candidate interval

The highest-risk repaired claim is that strict `R+` endpoint conditions imply both-served continuation dominance over the complete candidate interval `[h_0,h_F]`.

For flat pricing, the independent reconstruction gives

`d/dh [Pi_F^B(l,h)-Pi_F^H(h)] = -d(2a_L+d)/2 < 0`.

For the provider-optimal both-served metered branch, with

`p*(h)=c+d h/(l+h)`,

the independent reconstruction gives

`d/dh [Pi_M^B(p*(h)|l,h)-Pi_M^H(h)]`

`= - d [2(a_L-c)(l+h)^2+d l^2] / [2(l+h)^2] < 0`.

Thus both relevant both-served-minus-H-only gaps are strictly decreasing in `h`. Strict dominance at `h_F` therefore propagates to every candidate state below `h_F`. No-service is separately dominated by the positive-profit conditions. This independently confirms the economic monotonicity hypothesis that the Lean endpoint-propagation lemma itself does not derive.

### 3.2 Finite deviations leaving the preferred branch

The clean-room evaluator does not call the production continuation solver. For representative states `h_0`, `h_M`, an interior state, and `h_F`, it searches a dense grid of positive marginal prices and, at every price, compares the fixed-fee thresholds that induce:

- both classes served;
- H only served;
- no service.

The global finite-deviation search reproduces the analytic `p*(h)` and finds no profitable H-only/no-service deviation in the certified interval. No `None`, NaN, invalid branch, or nonconvergence outcome is used as evidence against a deviation.

### 3.3 Exact baseline reconstruction

For the permanent exact example

`a_L=4, a_H=5, c=1, b_L=16/5, K_L=4, b_H=1/2, K_H=8`,

the independent reconstruction gives

- `l=4/5`;
- `R_F=9/2`;
- `h_0=1/16`;
- `h_F=5/8`;
- `h_M=(-17+sqrt(2849))/80 ≈ 0.4547003073`;
- `mu_M=-461/200+13 sqrt(2849)/200 ≈ 1.164441598`;
- `mu_F=1681/1140 ≈ 1.474561404`.

The frozen illustrative `mu=13/10` lies strictly between the thresholds. The T1/T2/T3 example is therefore reproduced independently.

### 3.4 Generality hostile counterexample

A new Stage-11 scope attack allows different strictly-concave quadratic curvatures:

- `v_L(q)=3q-q^2/2`;
- `v_H(q)=(9/2)q-q^2`;
- `c=1`, `l=4/5`, `h=1/5`.

Both utility functions are strictly concave. The optimized both-served metered marginal price is `15/16`, but H's continuation rent rises from `9/16` under flat pricing to `1071/1024` under metering. Thus the state-order mechanism can reverse once common curvature is relaxed.

This is **not** a failure of the manuscript because the repaired manuscript explicitly refuses an arbitrary-strict-concavity theorem and treats nonquadratic/common-curvature exercises as numerical robustness only. The counterexample is retained as a permanent Stage-11 guard against future scope inflation.

### 3.5 Certification-regression verdict

**No mathematical certification regression found.**

The Stage-4A global-continuation certificate survives the new finite-deviation attack. The Stage-7.5A scope ceiling is confirmed, not contradicted, by the new strict-concavity counterexample.

## 4. Theorem / formal-verification attack

The manuscript's theorem language remains within `theorem_certificates/current_scope.md`:

- T1–T3 are quadratic-baseline results on strict `R+`;
- T1 states `h_0<h_M<h_F`;
- T3 excludes equality boundaries;
- outside-`R+` global characterization is not claimed;
- W1 is fixed-installed-base only;
- endogenous architecture welfare is sign-indeterminate;
- nonquadratic results are numerical only;
- no non-Uniform-CDF theorem is claimed.

The manuscript's Lean language also remains within the repaired formal certificate. It does not claim that Lean certifies weak participation, global provider optimization, the complete atomless integration game, mixed-equilibrium existence, or institutional interpretation.

**Attack classification: MINOR / RESOLVED.** No scope drift was found.

## 5. Welfare / benchmark attack

The manuscript uses `first best` only for the planner problem that directly chooses integration and usage. The fixed-installed-base private/social threshold comparison is explicitly labeled as a comparison of the same decentralized allocations. The architecture-commitment comparison is separately labeled restricted and is reported as sign-indeterminate.

The independent algebra reproduces

`mu_P-mu_W = d h p*(h) > 0`

for the fixed installed base.

No transfer-accounting error or benchmark-label drift was found.

**Attack classification: MINOR / RESOLVED.** No theory change required.

## 6. Novelty / whole-game absorption attack

The Stage-11 search reopened the strongest threats rather than inheriting Stage 6.

- **Gans (2012), _Mobile Application Pricing_** contains access/adoption before later application pricing and therefore kills generic future-pricing / sunk-adoption novelty.
- **Muthers & Wismer (2022), _Why Do Platforms Charge Proportional Fees? Commitment and Seller Participation_** combines tariff form, seller participation, and hold-up and remains the strongest conceptual threat.
- **Min & Ryu (2025), _Price Discrimination, Two-Part Tariff, and Hold-Up_** has sunk downstream investment before a monopolistic supplier offers two-part tariffs and kills generic sunk-investment / later-two-part-tariff novelty.
- **Wang & Hu (2014), _Committed Versus Contingent Pricing Under Competition_** contains a unique mixed pricing-regime equilibrium, so mixing itself is not novel.
- Static fixed-versus-usage and pay-per-use literatures continue to kill architecture-choice and metering-cost novelty as standalone contributions.

The targeted Stage-11 re-kill did **not identify a single prior model that absorbs the complete reciprocal loop**

`expected architecture -> installed composition -> relative profitability of that architecture -> architecture choice`

and the resulting expectation-contingent threshold split. This is an evidence-based non-absorption verdict, not a claim that no unpublished or undiscovered prior art can exist.

**Attack classification: MAJOR BUT FIXABLE / RESOLVED BY NARROW CLAIM.**

Required discipline: the Introduction, Related Literature, Abstract, and any Stage-12 journal pitch must sell only the reciprocal state-feedback / threshold-splitting result. They may not sell generic hold-up, mixed pricing, metering costs, or GenAI labeling as novelty. The repaired manuscript currently obeys that restriction.

## 7. Assumption / mechanism attack

### Metering activation cost `mu`

A positive real activation cost is essential for a nondegenerate architecture threshold, but it is not sufficient for threshold splitting. With architecture-insensitive integration, `h_M=h_F` and the two thresholds collapse even when `mu` remains. Thus the headline split is not mechanically generated by adding a fixed cost.

The economic interpretation of `mu` remains deliberately narrow: it is a real resource cost of operating the metered architecture, not customer budget risk, procurement aversion, or a transfer. This is a benchmark primitive rather than an empirical estimate.

**Attack classification: MINOR / RESOLVED.**

### Weak participation at zero surplus

Weak participation is outcome-relevant because the provider binds the low-use participation constraint exactly. It is therefore not innocuous wording. The model already states it as a primitive. Stage 11 adds an explicit limitation sentence: the paper does not claim that the same pure-strategy characterization has been established under strict participation, which would require a separate limit or epsilon-implementation analysis.

**Attack classification: MINOR / FIX APPLIED.** No theorem is broadened.

### Functional form / two types / uniform integration costs

These restrictions materially support tractability and the certified ordering. Stage 11 deliberately found a strictly-concave heterogeneous-curvature counterexample outside the theorem class. The manuscript already treats these restrictions as scope, not genericity.

**Attack classification: MINOR / RESOLVED BY SCOPE.**

## 8. Institutional / external-validity attack

Current primary-source checks confirm that closely related markets exhibit the payment structures used only as motivation:

- OpenAI Business uses fixed per-user seat charges and allows optional workspace credits beyond included usage limits; Enterprise/Edu can use contract-level shared credits;
- AWS Savings Plans exchange discounted prices for a one- or three-year monetary/usage commitment;
- Google Cloud committed-use discounts exchange discounted prices for minimum resource use or minimum spend commitments over one- or three-year terms.

Stage 11 found one source-mapping weakness: the manuscript previously used the flexible-pricing Help Center citation to support both fixed Business seat charges and additional credits. The fixed seat charge is more directly documented on OpenAI's Business pricing page. A separate bibliography entry and citation were added.

These facts motivate feasible tariff forms only. They do not establish the paper's causal reciprocal feedback empirically, and the manuscript says so.

**Attack classification: MINOR / FIX APPLIED.**

## 9. Numerical / figure / exposition attack

The headline figure and table are generated deterministically from the frozen exact example by `scripts/generate_outputs.py`. Their captions explicitly state that the numbers are illustrative and do not expand theorem quantifiers. The figure shows the two exact-example thresholds and the strict gap; the table reports generated exact and decimal objects.

No numerical exercise is used as proof of T1–T3. The exact theorem claims remain analytic.

**Attack classification: MINOR / RESOLVED.**

## 10. Journal-fit attack

The repaired paper is now mathematically narrower than its pre-repair version. That is appropriate for correctness, but it raises the relative importance of journal positioning. The paper is not a broad theorem on nonlinear pricing or a general AI-pricing theory. Its publishable object is a compact dynamic self-consistency mechanism with a clean threshold split, plus a narrow welfare wedge.

**Attack classification: MAJOR BUT FIXABLE / ROUTED TO STAGE 12.**

This is not a theory blocker. Stage 12 must choose a journal family whose contribution standard fits a narrow but nontrivial IO/dynamic-pricing mechanism and must reassess whether the GenAI-forward title helps or creates an application-relabeling desk-reject risk.

## 11. Attack ledger

| Attack | Severity | Status | Earliest affected stage if failed | Theory reopened? |
|---|---|---|---|---|
| Global continuation / finite regime deviation | FATAL candidate | PASS | Stage 4 / 4A | No |
| T1–T3 exact reconstruction | FATAL candidate | PASS | Stage 4 / 4A | No |
| Arbitrary strict-concavity generalization | FATAL if claimed | Counterexample retained; claim not made | Stage 7.5A | No |
| Formal-verification scope inflation | MAJOR | PASS | Stage 7.5A Formal Gate | No |
| Welfare benchmark drift | MAJOR | PASS | Stage 7 | No |
| Whole-game novelty absorption | MAJOR BUT FIXABLE | Narrow contribution survives targeted re-kill | Stage 6 | No |
| `mu` mechanicality / ad hoc interpretation | MINOR | Resolved by collapse benchmark + narrow interpretation | Stage 3/4 if redefined | No |
| Weak participation dependence | MINOR | Limitation made explicit | Stage 4 if convention changed | No |
| Current institutional source mapping | MINOR | Fixed | Stage 10/11 prose | No |
| Numerical-as-proof / visual overstatement | MINOR | PASS | Stage 10 | No |
| Journal fit / contribution level | MAJOR BUT FIXABLE | Stage 12 task | Stage 12 | No |

## 12. Gate rule evaluation

- unresolved FATAL attacks: **0**;
- certification regressions: **0**;
- material unresolved continuation failures: **0 found**;
- solver failures silently filtered: **none in the Stage-11 direct evaluator**;
- theorem quantifier inflation: **none**;
- benchmark terminology drift: **none**;
- formal scope inflation: **none**;
- bounded manuscript fixes applied: **institutional source mapping; weak-participation limitation**;
- theory change made: **none**.

## 13. Routing

**GO — REFEREE ATTACK GATE PASS.**

After green Stage-11 closeout CI:

**GO TO STAGE 12 — JOURNAL POSITIONING.**

Stage 12 must use the repaired theorem scope and the narrow reciprocal-state-feedback contribution. It must not reopen killed novelty claims merely to target a higher-ranked journal.
