# Stage 4A — Independent Mathematical Adversarial Re-Certification

Date: 2026-09-12 (JST)  
Project: **Dynamic Tariff Choice for Generative AI**  
Canonical workflow: `ryotamatsuki/research-paper-workflow` v2.1

## 1. Executive adversarial verdict

**GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS.**

The Stage-11B certification regressions are closed at the Stage-4/4A layer.

The repaired game now explicitly defines participation at zero continuation surplus and globally defines the provider continuation best-response correspondence at every installed-state history. The headline theorem domain is strengthened from the superseded regular-region wording to strict `R+`, which requires both-served flat and metered continuations to be the strict global active-set optima over the **complete rational-expectations candidate interval** `[h_0,h_F]`, not merely the preferred `[h_M,h_F]` interval.

An independently written direct-payoff evaluator (`verification/stage4a_repair_independent.py`) does not import the production symbolic solver. It reconstructs continuation payoffs from primitives, enumerates both-served / H-only / no-service regimes, searches architecture-specific integration fixed points, attacks hidden pure equilibria, tests arbitrary off-path installed masses, and retains the exact outside-region `23/10` counterexample.

No fatal counterexample to T1--T3 was found on repaired `R+`.

## 2. Independent reconstruction summary

The repaired future participation rule is weak IR: a task accepts iff maximized continuation utility is weakly nonnegative, and accepts at equality. Thus `F=S_L(p)` implements the both-served continuation exactly.

For fixed `p`, provider profit is increasing in `F` while the participation set is unchanged. Because `S_H(p)>=S_L(p)`, the only economically relevant fixed-fee thresholds are:

- `F=S_L(p)` — both served;
- `F=S_H(p)` — H-only;
- no service.

With positive installed H mass, L-only cannot be implemented by an anonymous tariff. Negative fixed fees are never optimal, and prices at/above the H choke price are no-service outcomes. This reduces the global continuation problem to a finite active-set comparison plus one-dimensional price maximization.

On the both-served metered branch,

`p_B(l,h)=c+d h/(l+h)`

whenever this price is below `a_L`, with strict SOC `-(l+h)<0`.

On the H-only metered branch, the unique optimum is `p_H=c`, with strict SOC `-h<0` for positive installed H mass.

The architecture-level continuation values are globally defined as

`V_F(l,h)=max{Pi_F^B(l,h),Pi_F^H(h),0}`

and

`V_M(l,h)=max{max_{0<p<=a_L}Pi_M^B(p|l,h),Pi_M^H(h),0}`.

The provider compares `V_F(l,h)` against `V_M(l,h)-mu`; equality permits mixing. This best-response correspondence exists at every installed-state history, including histories outside the headline region.

## 3. Headline theorem-certificate table

| Claim | Exact scope | Equilibrium-set status | Candidate-deviation audit | Alternative-equilibrium audit | Boundary/regime audit | Result |
|---|---|---|---|---|---|---|
| T1: `h_0<h_M<h_F` | repaired strict `R+` | unique architecture-specific integration fixed points on candidate interval | PASS | PASS | PASS | PASS |
| T2: `mu_M<mu_F` | repaired strict `R+` | threshold objects unique | PASS | PASS | PASS | PASS |
| T3: no pure architecture for `mu_M<mu<mu_F`; unique regular-branch mixed aggregate resolution | repaired strict `R+`, strict gap | UNIQUE aggregate equilibrium on claimed branch, up to measure-zero integration cutoff and irrelevant off-path selections | PASS | PASS | PASS | PASS |
| B1: architecture-insensitive integration collapses thresholds | same branch logic | unique threshold object | PASS | N/A | PASS | PASS |

No theorem is certified globally outside `R+`.

## 4. T1 certificate — integration ordering

### Exact claim

For every parameter vector in repaired `R+`, flat expectation induces

`h_F=(b_H+R_F)/K_H`,

and metered expectation has a unique fixed point `h_M` satisfying

`K_H h_M=b_H+R_F-d[c+d h_M/(l+h_M)]`,

with

`h_0<h_M<h_F`, where `h_0=b_H/K_H`.

### Proof-critical facts

Define

`g(h)=b_H+R_F-d[c+d h/(l+h)]-K_H h`.

On `R+`, `p_B(l,h_0)<a_L<(a_H+a_L)/2`, hence

`g(h_0)=R_F-d p_B(l,h_0)>0`.

Also

`g(h_F)=-d p_B(l,h_F)<0`,

and

`g'(h)=-K_H-d^2 l/(l+h)^2<0`.

Therefore exactly one root lies in `(h_0,h_F)`.

### Independent attack

The clean-room evaluator obtains integration rents from the globally selected direct-payoff continuation, scans the full `[h_0,h_F]` interval, and finds exactly one flat root and one metered root. For the exact example:

`h_0=0.0625`,

`h_M=0.454700307254`,

`h_F=0.625`.

### Surviving limitation

This is a strict `R+` result, not a global statement over all installed compositions or arbitrary demand systems.

## 5. T2 certificate — threshold separation

### Exact claim

On repaired `R+`,

`mu_M=Phi(l,h_M)<Phi(l,h_F)=mu_F`,

where

`Phi(l,h)=(l+h)/2[c+d h/(l+h)]^2`.

### Independent attack

The direct-payoff evaluator does not call the production `Phi` implementation. It computes global flat and metered continuation profits separately and forms their difference. On the strict both-served candidate interval that direct difference reproduces the certified threshold ordering.

For the exact example:

`mu_M=1.164441597721`,

`mu_F=1.474561403509`.

The analytic derivative remains strictly positive:

`Phi_h=[c(l+h)+dh][c(l+h)+dh+2dl]/[2(l+h)^2]>0`.

### Surviving limitation

The abstract implication `h_M<h_F` plus strictly increasing metering gain is an organizing sufficient-condition lemma, not a primitive theorem for arbitrary concave demand.

## 6. T3 certificate — pure-regime gap and mixed resolution

### Exact claim

For every parameter vector in repaired `R+` and every activation cost satisfying

`mu_M<mu<mu_F`,

neither a pure flat expectation nor a pure metered expectation is self-consistent. On the certified strict regular branch there is a unique mixed aggregate resolution `(h*,rho*)` satisfying

`Phi(l,h*)=mu`,

`h_M<h*<h_F`,

and

`rho*=K_H(h_F-h*)/[d p_B(l,h*)] in (0,1)`.

### Candidate-deviation audit

At `h_F`, direct global continuation payoffs satisfy

`V_M(l,h_F)-V_F(l,h_F)-mu=mu_F-mu>0`,

so flat expectation induces a profitable metering deviation.

At `h_M`,

`V_M(l,h_M)-V_F(l,h_M)-mu=mu_M-mu<0`,

so metered expectation induces a profitable flat deviation.

### Alternative-equilibrium audit

This audit is separate from the candidate-deviation check.

Any H-only or no-service expectation gives H zero future continuation rent and therefore H installed state `h_0=b_H/K_H`. By repaired `R+`, both-served flat and both-served metered continuations **strictly** dominate H-only/no-service throughout `[h_0,h_F]`, including `h_0`. Therefore H-only or no-service cannot support an alternative pure rational-expectations equilibrium on the claimed domain.

L-only is not implementable by an anonymous tariff when positive H mass is installed. Since `b_H>0`, candidate H mass is never zero.

The global integration maps generated by the direct continuation evaluator have exactly one flat root and one metered root on the full candidate interval. No second active-set root appears.

### Mixed-equilibrium audit

`Phi` is continuous and strictly increasing on the strict both-served interval. Hence `Phi(h)=mu` has exactly one solution `h* in (h_M,h_F)`.

At `h*`, the provider is indifferent between architectures. The only mixing probability consistent with H integration mass `h*` is

`rho*=K_H(h_F-h*)/[d p_B(l,h*)]`.

The metered fixed-point residual is strictly decreasing, which implies `0<rho*<1`. Thus no continuum of provider mixing probabilities supports the same installed state.

For the exact example:

`h*=0.529669331122`,

`p*=1.398346655612`,

`rho*=0.545390764129`.

### Equilibrium-set status

**UNIQUE aggregate mixed equilibrium on the claimed strict `R+` gap**, up to:

- the measure-zero integration cutoff task, whose action has no aggregate effect;
- arbitrary best-response selections at genuinely off-path provider indifference histories, which do not alter the on-path certified allocation or payoffs.

No uniqueness is claimed outside `R+` or at `mu=mu_M,mu_F`.

## 7. Participation / indifference audit

### Future participation tie

Previously: unresolved and certification-invalidating.

Repaired primitive: a task participates at zero continuation surplus. Therefore the positive L mass participates when `F=S_L(p)` and the provider's exact maximum is attained rather than merely approached as a supremum.

This convention is not used asymmetrically across task classes: H likewise participates when exactly indifferent.

### Integration cutoff tie

The baseline integration-cost distribution is continuous. A task exactly at the cutoff is indifferent; the repaired convention assigns integration at equality. The set has measure zero, so aggregate installed masses and provider payoffs are invariant to this individual selection.

### Provider architecture indifference

At `h*`, provider architecture indifference is substantive and intentionally supports the mixed equilibrium. No deterministic architecture tie-breaking rule is imposed there. At off-path architecture-indifference states, any best-response selection is admissible; no headline claim depends on those selections.

### Active-set indifference

Repaired `R+` imposes strict both-served dominance over H-only/no-service on the entire candidate-state interval. Hence there is no on-path active-set tie in the headline theorem.

## 8. Equilibrium-selection / refinement audit

The zero-surplus participation rule is now part of the model primitives and is disclosed as economically material. It is not a dominance refinement introduced only to delete an inconvenient equilibrium.

No weak-dominance elimination is used.

Provider mixing at `h*` is an ordinary best response under payoff equality. The supporting probability is pinned down by the H integration consistency equation.

The theorem does not state selection-free conclusions at equality boundaries or outside `R+`.

## 9. Global boundary / active-set audit

The provider continuation correspondence is defined at arbitrary installed masses, not only on the regular branch.

For quadratic demand:

`Pi_F^H-Pi_F^B` is strictly increasing in `h` with derivative `R_F>0`.

Likewise the H-only-minus-both metered-profit difference has derivative

`d{d l^2+2(a_L-c)(h+l)^2}/[2(h+l)^2]>0`.

The repaired region therefore checks the worst candidate endpoint `h_F` for both/H-only ordering and both endpoints for the affine flat/no-service comparison.

The permanent outside-region point

`a_L=4, a_H=5, c=1, l=0.1, h=0.6`

still yields

`Pi_F^H-Pi_F^B=23/10>0`.

This is retained as proof that the headline theorem cannot be global in installed composition.

## 10. Continuation-completeness audit

### Off-path histories

For every installed-state history `(l,h)`:

- flat continuation compares both-served, H-only, and no-service directly;
- metered continuation maximizes the both-served expression over its feasible price interval, compares it with the globally optimized H-only candidate and no-service, and then subtracts activation cost at architecture choice;
- architecture best response is any maximizer of the resulting flat and metered values.

Thus no off-path state is assigned `None`, NaN, solver failure, or an automatically unprofitable continuation.

The independent code deliberately evaluates masses including `l=0`, `h=0`, small states near active-set switches, the permanent outside-region counterexample, unit masses, and `h=2`. A finite continuation candidate is returned throughout.

### Scope distinction

Continuation **play** is globally defined. The T1--T3 **equilibrium characterization** remains restricted to `R+`. These are now explicitly different claims.

## 11. Counterexample-search design and results

The repeated Stage-4A attack used:

- direct primitive payoff construction rather than production formulas;
- active-set enumeration;
- a dense scan of all rational-expectations candidate states in `[h_0,h_F]`;
- independent root search for flat and metered integration mappings;
- explicit H-only/no-service expectation tests at `h_0`;
- off-path installed-mass stress states;
- the exact `23/10` outside-region counterexample.

Result: no counterexample to T1--T3 on repaired `R+`; global all-parameter generality remains false and is not claimed.

## 12. Welfare-selection and benchmark audit

No welfare primitive or benchmark changes at this repair. Stage-7 results are not re-certified here.

The repaired continuation game does not alter the on-branch allocation/payoff formulas used by the existing fixed-installed-base welfare calculation. Nevertheless, because the Stage-8 freeze was reopened, Stage 7 must later receive a regression check before refreeze.

## 13. Evidence ledger

| Claim | Attack actually performed | Artifact | Result | Surviving limitation |
|---|---|---|---|---|
| exact binding-PC implementation | explicit zero-surplus participation audit | `docs/STAGE_04R_REPAIR.md` | PASS | depends on disclosed weak-participation primitive |
| global continuation existence | active-set candidate reduction and arbitrary-state stress | `verification/stage4a_repair_independent.py` | PASS | global equilibrium outside `R+` not characterized |
| T1 | independent global-continuation root scan | same | PASS | strict `R+` only |
| T2 | direct architecture-profit difference | same | PASS | quadratic baseline theorem |
| T3 candidate deviations | direct global provider payoffs at `h_F,h_M` | same | PASS | strict gap only |
| T3 alternative equilibria | H-only/no-service state `h_0`, full candidate-interval active-set scan | same | PASS | outside `R+` unresolved by design |
| mixed uniqueness | independent `h*` root and `rho*` support calculation | same | PASS | aggregate uniqueness on regular branch |
| scope guard | exact H-only counterexample | same | PASS | proves global extension false |

## 14. Formal-verification applicability

**FORMALIZATION APPLICABLE.**

The existing Lean file remains useful for its conditional algebraic core, but the former Stage-7.5A economic statement-fidelity certificate is stale because the game definition and certified domain have been repaired after freeze.

Renewed Stage-7.5A formal-fidelity targets should include, at minimum:

1. repaired T1 endpoint/root ordering on the strengthened domain assumptions;
2. T2 threshold ordering;
3. strict-gap response reversal and mixed-state uniqueness skeleton;
4. exact outside-region counterexample;
5. a machine-checkable statement of the active-set endpoint inequalities used to define `R+`, where practical.

The participation convention and global economic candidate reduction may remain human-certified if they are not naturally encoded, but the eventual formal certificate must explicitly say they are outside Lean coverage rather than implying full-game formalization.

## 15. Permanent regression tests created

New permanent independent artifact:

`verification/stage4a_repair_independent.py`.

It preserves:

- full `[h_0,h_F]` strict active-set dominance for the exact example;
- one flat and one metered integration fixed point;
- strict threshold ordering;
- strict-gap architecture deviations;
- unique mixed support;
- failure of H-only/no-service alternative candidates at `h_0`;
- arbitrary off-path continuation finiteness;
- exact `23/10` outside-region counterexample.

The Stage-11B independent audit remains separately preserved and is not overwritten.

## 16. Certification-regression closure

### CR-1 — undefined participation tie

**Closed.** Future participation at zero continuation surplus is now an explicit symmetric model primitive.

### CR-2 — incomplete off-path continuation

**Closed.** The provider global continuation best-response correspondence is now defined for every installed-state history by primitive active-set maximization. The regular theorem no longer substitutes its on-branch formula for global continuation play.

### Workflow lesson

The original Stage-4A PASS should have failed the mandatory indifference and continuation-completeness fields. Future Stage-4A audits should require an explicit line item for every positive-mass participation tie and an explicit continuation correspondence for every sequential subgame state before awarding `GO`.

## 17. Exact blocker / earliest affected stage

No unresolved Stage-4A correctness blocker remains on the repaired claim domain.

Because the repair changed a strategy-domain convention and tightened the certified theorem domain, the old downstream certifications cannot simply be inherited. The required next routing is the canonical downstream sequence beginning with Stage 6 Novelty Re-Kill / ratification, followed by Stage 7, Stage 7.5, Stage 7.5A and Stage 8 refreeze before returning to manuscript/referee work.

## Final verdict

**GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS.**

**Next authorized stage: Stage 6 Novelty Re-Kill / repair ratification.**
