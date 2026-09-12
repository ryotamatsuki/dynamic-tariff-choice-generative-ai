# Stage 7.5 — Full-Theory Freeze Decision (Repaired Model)

Date: 2026-09-12 (JST)  
Project: **Dynamic Tariff Choice for Generative AI**  
Canonical workflow: `ryotamatsuki/research-paper-workflow` v2.1

## 1. Executive freeze-decision verdict

**GO TO STAGE 7.5A GENERALITY / QUANTIFIER RED-TEAM.**

The repaired project remains worth full-paper investment. The case is narrower than the superseded pre-repair version, but the central economic object is not merely a parameter exercise: anticipated tariff architecture changes relationship-specific sunk integration, the resulting installed high-use composition changes the provider's later relative incentive to choose that same architecture, and this reciprocal feedback converts one fixed-state architecture-switching threshold into two expectation-contingent self-consistency thresholds.

The full-paper case does **not** rest on generic hold-up, AI as an application label, mixed equilibrium, two-part tariffs, or model-quality improvement. Those claims remain killed. It rests on the interaction theorem and its benchmark collapse.

Stage 7.5 is an editorial/value gate only. It does not authorize theory freeze. The repaired model must now pass Stage 7.5A quantifier, benchmark, generality and formal-fidelity certification before any new Stage-8 freeze.

## 2. Recommended working title

The prior title, **“Dynamic Tariff Choice for Generative AI: Model Improvement, Commitment, and Welfare,”** overstates the role of model/quality improvement. Quality improvement is not part of the headline theorem.

Recommended working title for the next manuscript revision:

**Dynamic Tariff Choice for Generative AI: Integration, Commitment, and Welfare**

This is a clarification/reclassification only. No manuscript edit is authorized until a repaired Stage-8 freeze.

## 3. Core question and notation-free mechanism

### Core question

When users make sunk, relationship-specific AI integration decisions before a provider can revise future tariff architecture, can expectations about future flat versus metered pricing alter the installed customer/task composition in a way that feeds back into the provider's own later pricing-architecture incentive?

### Notation-free explanation

Yes. A future usage charge is especially costly to heavy-use workflows, so expecting metering discourages some heavy-use integration. But the provider's gain from metering is itself larger when more heavy-use workflows are installed. Therefore the provider evaluates metering against a different installed base depending on which architecture users expected in the first place. The static architecture switch is no longer evaluated at one state: it is evaluated at two endogenous self-consistent states. This can create an interval in which a flat-price expectation makes metering profitable while a metered-price expectation makes flat pricing profitable.

### Minimal causal / strategic chain

`expected future architecture`

`-> architecture-dependent continuation rent`

`-> sunk relationship-specific integration`

`-> installed high-use composition`

`-> provider's ex-post relative gain from metering`

`-> future architecture choice`.

This reciprocal final arrow back to the architecture decision is the full-paper mechanism.

## 4. Mechanism card

| Element | Repaired project object |
|---|---|
| Phenomenon | Pricing architecture anticipated before relationship-specific integration can fail to be self-confirming ex post. |
| Friction | Users sink integration before the provider chooses/revises future architecture; metering has a real activation cost. |
| Strategic response | Heavy-use integration responds to expected continuation rent under the anticipated architecture. |
| Equilibrium effect | Installed composition changes the provider's relative gain from metering, splitting one fixed-state threshold into `mu_M<mu_F`; the strict interval between them has no pure architecture equilibrium on the certified branch. |
| Welfare effect | At a fixed installed base, the provider tolerates a larger metering cost than a social evaluator because private rent extraction is a transfer socially; with endogenous integration there is no unconditional flat-versus-metered welfare ranking. |
| Empirical implication | Pricing-architecture incentives should be stronger in markets/accounts with more deeply integrated high-use workloads, while anticipated usage pricing should discourage heavy-use integration more strongly than light-use integration. This is a model implication, not an established causal fact. |

## 5. Essential vs tractability assumptions

### Economically essential to the certified mechanism

1. **Sunk integration precedes the future architecture decision.** If integration is fixed/exogenous, the threshold split collapses.
2. **Expected architecture changes continuation rents and therefore installed composition.** Without architecture-sensitive integration, `h_M=h_F`.
3. **The provider's relative gain from metering increases over the relevant installed-state range.** Together with `h_M<h_F`, this generates threshold separation.
4. **There is an architecture margin with a real activation/implementation cost.** This produces the switching-threshold object whose self-consistency is studied.
5. **Positive non-expropriable current integration benefit.** This permits positive sunk integration before future repricing and avoids the earlier complete-expropriation collapse.
6. **The claimed theorem domain keeps the same active set globally optimal over the complete rational-expectations candidate interval.** In the quadratic baseline this is encoded by strict `R+`.

### Game-completion / implementation assumptions

- A future participant accepts at zero continuation surplus. This weak-IR tie convention is explicit, symmetric, and required for exact implementation of the binding participation constraint.
- Provider continuation play is globally defined off path by comparing both-served, H-only and no-service candidates. This is required for a complete game but is not itself the source of novelty.

### Tractability / baseline structure

- two usage classes `L,H`;
- quadratic future utility in the certified baseline;
- Uniform integration-cost distribution in the certified baseline;
- anonymous two-part tariff family;
- monopoly provider;
- one market and one provider architecture choice.

The project does **not** currently prove that arbitrary concavity, arbitrary cost distributions, competition, or richer tariff menus preserve the headline theorem.

## 6. Core propositions and certification status

| Object | Current exact status | Stage-4A status | Full-paper role |
|---|---|---|---|
| T1: `h_0<h_M<h_F` | Universal over strict `R+` in quadratic baseline | PASS | mechanism input, not standalone novelty |
| T2: `mu_M<mu_F` | Universal over strict `R+` | PASS | main threshold-separation theorem |
| T3: `mu_M<mu<mu_F` gives no pure architecture and a unique aggregate mixed resolution on the certified branch | Universal over strict `R+` and strict gap | PASS | main equilibrium consequence; mixed equilibrium itself is not novelty |
| B1: architecture-insensitive integration collapses thresholds | exact benchmark | PASS | mechanism-identification benchmark |
| W1: `mu_P-mu_W=d h p*(h)>0` | fixed-installed-base quadratic both-served benchmark | analytically verified at Stage 7 | welfare implication, explicitly not a global policy theorem |
| W2: endogenous architecture-commitment welfare ranking has no universal sign | two strict-`R+` counterexamples of opposite sign | verified at Stage 7 | blocks overclaiming; not a headline novelty theorem |

The repaired Stage-4A certificates exist for every headline mathematical claim T1–T3/B1.

## 7. Baseline vs robustness vs intended-general-theorem classification

| Claim | Maximum defensible classification before Stage 7.5A |
|---|---|
| T1 `h_M<h_F` | **BASELINE FUNCTIONAL FORM on strict `R+`** |
| T2 threshold separation | **BASELINE FUNCTIONAL FORM on strict `R+`** |
| T3 pure-regime gap | **BASELINE FUNCTIONAL FORM on strict `R+`** |
| `h_M<h_F` + strictly increasing architecture gain implies threshold separation | **SUFFICIENT-CONDITION THEOREM / organizing lemma**; not primitive functional-form generality |
| common-curvature cubic example | **NUMERICAL ROBUSTNESS ONLY** |
| arbitrary strictly concave utility | **FALSE AS A GENERAL CLAIM**; Stage-11B counterexample reverses the state ordering |
| non-Uniform integration-cost CDF | pre-repair evidence only; **STALE PENDING STAGE 7.5A RECERTIFICATION** |
| W1 fixed-base welfare wedge | **BASELINE ANALYTIC IDENTITY** |
| endogenous welfare ambiguity | **COUNTEREXAMPLE / SIGN-INDETERMINACY EVIDENCE** |

No broad function-class theorem is being smuggled into Stage 7.5.

## 8. Closest-paper distinction

The closest predecessors establish most ingredients separately. Gans (2012) shows that sunk access before future pricing creates anticipation and hold-up/unravelling. Muthers and Wismer (2022) combine tariff form, commitment and sunk seller participation. Min and Ryu (2025) study sunk investment before later two-part-tariff extraction. Sundararajan (2004), Ladas–Kavadias–Loch (2022), Wang and Hu (2014), and related work establish fixed/usage or committed/contingent architecture choice and mixed pricing-regime equilibria. Recent LLM/cloud work establishes costly usage, two-part tariffs, committed spend and AI-specific pricing problems.

The repaired paper therefore claims none of those ingredients as new. Its distinction is the **reciprocal state feedback within the architecture choice itself**: the architecture expected before integration changes the installed state, and that installed state changes the ex-post profitability of the same architecture. The resulting `mu_M<mu_F` self-consistency split and pure-regime gap are not reproduced by simply relabeling the main theorem of any single identified predecessor. This is a narrow but precise whole-game distinction.

## 9. Does the result survive a credible alternative formulation already tested?

**Yes, with an important qualification.**

An independently solved common-curvature nonquadratic (cubic) utility example preserves `h_M<h_F` and increasing architecture gain. This shows that the baseline mechanism is not numerically unique to the exact quadratic formula.

However, a different strictly concave admissible utility specification reverses `h_M<h_F`. Therefore the alternative-formulation evidence is **numerical robustness only**, not a general concavity theorem. This limitation is a reason to proceed to Stage 7.5A, not a reason to kill the full paper.

## 10. Welfare / organizational relevance

The mechanism has non-transfer welfare content. Under a fixed installed base, the provider's private metering threshold exceeds the social threshold by

`d h p*(h)>0`,

because private metering incentives include rent extraction that is a transfer socially. This gives a clean interpretation of why the provider can prefer metering at activation costs for which the same decentralized allocation comparison lowers welfare.

Once integration is endogenous, however, the welfare ranking can reverse. This is substantive rather than a failure: the architecture changes both real usage distortion and sunk integration. The project therefore has a welfare story, but not a one-directional policy recommendation.

The organizational interpretation also survives outside the literal GenAI label: any setting with relationship-specific sunk integration before a later architecture decision can potentially display the same logic if architecture affects continuation rents and architecture profitability depends on installed composition. Cloud commitments are suggestive, not proof that the feedback is empirically present.

## 11. Would a skeptical field referee see more than a parameter exercise?

**Yes, but only if the manuscript is disciplined.**

Reasons for `GO`:

- the threshold split is an exact theorem on a transparently defined strict domain, not a numerical pattern;
- the architecture-insensitive benchmark collapses the two thresholds and identifies the source of the effect;
- the mechanism can be stated without quadratic notation;
- the result survives at least one nonquadratic formulation numerically;
- there is a genuine welfare implication separate from transfers;
- Stage-4A has independently attacked alternative active sets, hidden pure equilibria and off-path continuation.

Reasons a referee may still reject:

- strict `R+` is economically substantive and can look restrictive if buried;
- arbitrary concavity is false, so the paper cannot claim broad demand-system generality;
- the novelty is narrower than generic hold-up or tariff-form commitment;
- empirical evidence does not establish the causal feedback in AI/cloud markets.

The correct response is **not** to add extensions at Stage 7.5. The response is to make the narrow theorem and its mechanism identification unusually transparent.

## 12. Fatal / major referee risks

### Fatal risks

**None currently identified inside the certified claim set.** Stage-11B found certification defects, but Stage 4R/4A repaired them and re-certified T1–T3.

### Major but bounded risks

1. **Novelty compression:** Muthers–Wismer, Gans and Min–Ryu leave only the reciprocal threshold-splitting interaction as novelty.
2. **Domain restriction:** strict `R+` must be prominent because outside it active-set changes can destroy the simple state ordering.
3. **Generality:** strict concavity alone is insufficient; a known counterexample reverses `h_M<h_F`.
4. **Institutional causality:** observed tariff diversity and workflow integration do not prove `installed integration -> later architecture choice`.
5. **Title/exposition:** “Model Improvement” is unsupported by the headline theorem and should be removed in the next authorized manuscript revision.
6. **Formal fidelity:** the old Stage-7.5A economic certificate is stale after the repaired game definition; it must be renewed before freeze.

None requires a new model extension at this gate.

## 13. Full-paper value assessment

**Full paper remains justified.**

The result is too structured to reduce to a short correction/note: the paper has a complete dynamic game, an endogenous state-feedback mechanism, a threshold-separation theorem, a pure-regime gap, an identification benchmark, welfare decomposition, institutional interpretation, and explicit boundary counterexamples. At the same time, the project should not be sold as a broad general theory of AI pricing.

The paper's value proposition is:

> a precise dynamic self-consistency problem in tariff architecture created by relationship-specific integration, with a theorem showing how a single static switch splits into two endogenous thresholds.

That is a full-paper contribution if presented tightly.

## 14. Recommended journal level

### Primary positioning

**International Journal of Industrial Organization (IJIO): plausible but demanding.**

The project fits industrial organization, nonlinear pricing, commitment and endogenous adoption/integration. The principal risk at IJIO is not mathematical correctness but perceived narrowness relative to the closest hold-up/commitment literature.

### Alternative positioning

**Journal of Industrial Economics (JIE): possible but less preferred at the current scope.** The strict-domain and limited functional-form generality make this a higher-risk positioning unless the mechanism is exceptionally clean in exposition.

A solid field-journal fallback exists if the top field positioning rejects the contribution as too narrow. Stage 7.5 therefore should not downgrade the project to a research note merely because IJIO acceptance is uncertain.

## 15. Exact Stage-7.5A input package

Stage 7.5A must receive, without model modification:

1. `docs/STAGE_04R_REPAIR.md` — repaired game, weak-participation primitive, global continuation and strict `R+`;
2. `docs/STAGE_04A_RECERTIFICATION.md` — repeated hostile mathematical certification;
3. `theorem_certificates/stage4a_repair_certificates.md` — exact T1–T3/B1 quantifiers and scope;
4. `verification/stage4a_repair_independent.py` — clean-room active-set / alternative-equilibrium audit;
5. `docs/STAGE_06_REKILL_REPAIR_RATIFICATION.md` — surviving novelty and killed claims;
6. `docs/STAGE_07_REPAIRED_WELFARE_GENERALITY.md` — planner register, welfare, selection and robustness classifications;
7. `verification/stage7_repaired_verify.py` — welfare identities and strict-`R+` sign-reversal checks;
8. `verification/stage11b_astra_independent_audit.py` — nonquadratic robustness and strict-concavity counterexample evidence;
9. current Lean source `formal/DynamicTariffFormal.lean` plus build configuration, treated only as a conditional algebraic artifact until renewed fidelity certification.

### Mandatory Stage-7.5A attacks

Stage 7.5A must independently test:

- whether every T1–T3 quantifier matches repaired strict `R+` exactly;
- whether the `R+` endpoint active-set conditions used in the theorem statement are sufficient and stated without hidden stronger assumptions;
- whether weak participation at equality changes any formal theorem signature or economic statement;
- whether the abstract order lemma is clearly separated from primitive demand generality;
- whether any non-Uniform CDF claim can be re-certified under repaired global continuation, otherwise it remains dropped;
- whether the common-curvature nonquadratic example is correctly labeled numerical only;
- whether first best, fixed-installed-base, and restricted architecture-commitment benchmarks are terminologically exact;
- whether welfare claims are valid for the certified equilibrium set rather than a selected candidate;
- whether the Lean theorem signatures, assumptions and `#print axioms` evidence still match the repaired economic statements;
- whether any formalization target requires expansion because the repaired `R+` domain and participation convention postdate the old certificate.

### Stage-7.5A prohibited upgrades

Do not claim arbitrary concavity, global all-parameter results, empirical causality, generic excessive metering, generic mixed-equilibrium novelty, or quality/model-improvement novelty.

## 16. Final Stage-7.5 verdict

**GO TO STAGE 7.5A GENERALITY / QUANTIFIER RED-TEAM.**

No extension is authorized. The repaired model, exact claim scope, welfare benchmark register and evidence classifications are now the fixed inputs to Stage 7.5A. A new Stage-8 freeze remains blocked until Stage 7.5A passes.