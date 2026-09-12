# Stage 7 — Welfare, Generality & Institutional Validation (Repaired Model)

Date: 2026-09-12 (JST)  
Project: **Dynamic Tariff Choice for Generative AI**  
Canonical workflow: `ryotamatsuki/research-paper-workflow` v2.1

## 1. Executive welfare/generality verdict

**GO TO STAGE 7.5.**

The repaired strict `R+` model retains non-transfer welfare content, a coherent private/social architecture wedge at a fixed installed base, and a defensible institutional interpretation beyond one vendor. The Stage-11B repair does not alter the welfare algebra on the certified both-served branch; it strengthens game completeness and narrows the certified domain.

The important limitations are now explicit:

- the fixed-installed-base private/social threshold wedge is not a global endogenous-welfare theorem;
- the restricted architecture-commitment welfare ranking is sign-indeterminate even within repaired strict `R+`;
- the headline threshold-splitting result is baseline-functional-form / strict-domain economics, not a theorem for arbitrary concave utility;
- a Stage-11B strictly concave counterexample reverses `h_M<h_F`, so concavity alone is insufficient;
- institutional evidence establishes coexistence of fixed-access, credit/token-based and committed-spend pricing structures and real workflow integration, but does **not** establish the causal feedback `installed integration -> later architecture choice` as an observed fact.

The surviving Stage-6 contribution remains the reciprocal architecture–state feedback and its two self-consistency thresholds. Stage 7 does not revive any killed novelty claim.

## 2. Canonical repaired input

Stage 7 is run on the repaired object certified in:

- `docs/STAGE_04R_REPAIR.md`;
- `docs/STAGE_04A_RECERTIFICATION.md`;
- `theorem_certificates/stage4a_repair_certificates.md`;
- `verification/stage4a_repair_independent.py`;
- `docs/STAGE_06_REKILL_REPAIR_RATIFICATION.md`.

The repaired theorem domain is strict `R+`. In particular, every rational-expectations candidate high-use installed mass lies in `[h_0,h_F]`, where `h_0=b_H/K_H`, and both-served flat and metered continuations are strict global active-set optima over that complete candidate interval.

Surviving theorem objects:

- **T1:** `h_0<h_M<h_F` on strict `R+`;
- **T2:** `mu_M<mu_F` on strict `R+`;
- **T3:** for `mu_M<mu<mu_F`, neither pure architecture is self-consistent and the certified branch has a unique aggregate mixed resolution;
- **B1:** architecture-insensitive integration implies `h_M=h_F` and threshold collapse.

## 3. Exact consumer / integration surplus

For an integrated type-`j` task, future gross indirect surplus before the fixed fee is

`S_j(p)=(a_j-p)^2/2`

whenever `p<a_j` on the certified both-served branch.

Let `r_j` be future continuation rent and let `b_j` be the non-expropriable current integration benefit. A task with sunk integration cost `k` obtains total private surplus

`b_j+r_j-k`.

With `k~Uniform[0,K_j]` and interior integration cutoff

`B_j=b_j+r_j=K_j n_j`,

aggregate ex-ante user/integrator surplus is exactly

`CS_j = integral_0^{B_j} (B_j-k) dk / K_j`

`= B_j^2/(2K_j) = K_j n_j^2/2`.

Hence, for interior installed masses,

`CS = K_L l^2/2 + K_H h^2/2`.

This is an exact integration-surplus identity. It is not the triangular-CS shortcut prohibited by the workflow.

The repaired future-participation convention — participate at zero continuation surplus — does not add welfare at the binding low-type participation constraint; it completes implementation of the allocation. At the integration cutoff, the equality type has measure zero under the baseline continuous distribution.

## 4. Future operating surplus and total welfare

For a served type `j` under usage price `p`,

`q_j=a_j-p`.

Real future operating surplus is

`omega_j(p)=a_j q_j-q_j^2/2-cq_j`

`=[(a_j-c)^2-(p-c)^2]/2`.

The identity is verified symbolically in `verification/stage7_repaired_verify.py`.

For installed masses `(l,h)`, future architecture `A`, and corresponding usage price `p_A`, total welfare is

`W_A(l,h)=b_L l+b_H h-K_L l^2/2-K_H h^2/2`

`+ l omega_L(p_A)+h omega_H(p_A)-1{A=M} mu`.

Tariff payments `F` and `p q` are transfers between integrated tasks and the provider and therefore do not enter total welfare. Real resource costs are:

- sunk integration costs;
- inference/servicing cost `c q` already embedded in `omega_j`;
- the real metering activation cost `mu`.

No current-period provider revenue is separately modeled. The primitive `b_j` is treated as a real, current, non-expropriable integration benefit, not as a provider transfer.

For the strict-gap mixed equilibrium `(h*,rho*)`, expected welfare is

`W_mix=(1-rho*) W_F(l,h*) + rho* W_M(l,h*)`.

Because repeated Stage 4A certifies a unique aggregate mixed equilibrium on strict `R+`, this on-branch expression needs no external equilibrium-selection rule.

For the exact baseline `a_L=4,a_H=5,c=1,b_L=16/5,K_L=4,b_H=1/2,K_H=8,mu=13/10`, the inherited exact/numerical objects remain

- `h_0=0.0625`;
- `h_M≈0.454700307254`;
- `h_F=0.625`;
- `h*≈0.529669331122`;
- `rho*≈0.545390764129`;
- `W_F(l,h_F)≈7.9175`;
- `W_M(l,h_M;mu=0)≈7.835552`;
- `W_mix≈7.191206`.

These last welfare numbers are illustrations, not theorem statements.

## 5. Planner-objective / choice-set register

### P0 — unrestricted relevant planner: FIRST BEST

The planner observes integration cost `k` and directly chooses integration `x in {0,1}` and future usage `q>=0` for each potential task.

Per-task problem:

`max_{x in {0,1},q>=0} x[b_j+a_j q-q^2/2-cq-k]`.

Therefore

`q_j^FB=(a_j-c)_+`,

and total real gross surplus from integrating type `j` before `k` is

`Omega_j^FB=b_j+(a_j-c)_+^2/2`.

The planner integrates iff

`k<=Omega_j^FB`.

With the normalized Uniform support,

`n_j^FB=min{Omega_j^FB/K_j,1}`.

Only this object is called **first best**.

### P1 — fixed-installed-base architecture welfare comparison

Hold `(l,h)` fixed. Let the provider choose its profit-maximizing tariff parameters within each architecture and compare the resulting real allocations/welfare.

This is a **fixed-allocation benchmark**, not first best and not a planner optimum over integration.

### P2 — architecture-commitment welfare benchmark

Commit only the future architecture before integration; within the chosen architecture the provider later reoptimizes tariff parameters. Integration then responds to the committed architecture, producing `h_F` or `h_M` on strict `R+`.

Compare

`W_F(l,h_F)` and `W_M(l,h_M)`.

This is a **restricted-instrument commitment benchmark**, not first best.

## 6. Benchmark-definition table

| Benchmark | Planner/evaluator choice set | What is held fixed | Correct label | Not allowed label |
|---|---|---|---|---|
| P0 | integration and usage for every task | nothing relevant | first best | — |
| P1 | only evaluates provider-optimal flat vs metered allocation | installed masses `(l,h)` | fixed-allocation benchmark | first best / second-best planner optimum |
| P2 | chooses architecture ex ante; provider later reoptimizes tariff within architecture | tariff family and later provider optimization | restricted-instrument commitment benchmark | first best |

## 7. Private versus social decision map at fixed installed base

On the certified both-served branch,

`p*(h)=c+d h/(l+h)`.

Provider gross gain from metering before activation cost is

`mu_P(l,h)=Phi(l,h)`

`=(l+h)/2 [c+d h/(l+h)]^2`.

This is the provider's private threshold for paying activation cost `mu`.

Holding `(l,h)` fixed, the real-welfare difference between provider-optimal metering and flat pricing is

`W_M-W_F = mu_W(l,h)-mu`,

where

`mu_W(l,h)=(l+h)/2 [c^2-d^2(h/(l+h))^2]`.

Exact subtraction gives

`mu_P(l,h)-mu_W(l,h)=d h p*(h)>0`.

This identity is verified symbolically in `verification/stage7_repaired_verify.py`.

Economic interpretation: the provider's incentive to meter contains rent extraction that is a transfer socially, while the social evaluator values only real usage/integration effects and the activation cost.

Maximum defensible wording:

> Holding the installed base fixed on the certified both-served branch, the monopolist is willing to incur a strictly larger metering activation cost than a social evaluator comparing the same decentralized allocations.

Prohibited wording:

> Metering is always socially excessive in the endogenous game.

## 8. Welfare propositions and thresholds

### W1 — fixed-installed-base private/social wedge

On the certified both-served branch with `d>0` and `h>0`,

`mu_P-mu_W=d h p*(h)>0`.

Classification: **BASELINE FUNCTIONAL FORM — analytic**.

Equilibrium status: **EQUILIBRIUM-INVARIANT CONDITIONAL ON FIXED BASE**. It is a benchmark identity, not an equilibrium-selection theorem.

### W2 — no unconditional endogenous architecture welfare ranking

Under P2 define

`mu_C^W=W_M(l,h_M;mu=0)-W_F(l,h_F)`.

Committed metering is preferred under this restricted benchmark iff `mu<mu_C^W`.

No unconditional sign survives even after imposing repaired strict `R+`.

Two deterministic examples that satisfy every `R+` condition and differ only in `K_H` are:

`a_L=2.5, a_H=3, c=0.5, b_L=1, K_L=4, b_H=0.5`.

- `K_H=16`: `h_0=0.03125`, `h_M≈0.09718859`, `h_F=0.1171875`, and `mu_C^W≈+0.00429994`;
- `K_H=8`: `h_0=0.0625`, `h_M≈0.18964502`, `h_F=0.234375`, and `mu_C^W≈-0.03595932`.

Both examples satisfy the repaired strict `R+` active-set/interiority inequalities. The sign reversal is regression-tested in `verification/stage7_repaired_verify.py`.

Classification: **NUMERICAL COUNTEREXAMPLE / sign-indeterminacy evidence**. It proves that an unconditional architecture-welfare ranking is false; it does not by itself provide a general sign theorem.

### W3 — no universal first-best/decentralized integration ordering is claimed

P0 integrates based on total real operating surplus. Decentralized integration is based on `b_j` plus tariff-dependent private continuation rent. The exact ordering can vary with parameters and support caps. No universal underintegration theorem is authorized.

## 9. Equilibrium-selection robustness table

| Welfare/policy claim | Equilibrium-set status | Selection/refinement used | All-equilibria proof/counterexample | Cross-component issue | Maximum wording |
|---|---|---|---|---|---|
| Welfare in strict pure regions of `R+` | unique certified aggregate regular-branch equilibrium | zero-surplus participation is model primitive, not refinement | Stage-4A global continuation/alternative-equilibrium audit | none | state welfare on strict `R+` only |
| Welfare in strict gap | unique aggregate mixed equilibrium on certified branch | endogenous `rho*`; no external selector | Stage-4A mixed uniqueness audit | none | expected welfare of the unique aggregate mixed resolution |
| W1 fixed-base wedge | fixed allocation, not equilibrium selection | none | exact identity | none | fixed-installed-base benchmark only |
| Equality boundaries `mu=mu_M,mu_F` | provider indifference | none imposed | no selection-free boundary theorem needed | none | exclude boundaries from headline claims |
| Outside `R+` welfare | continuation globally defined but equilibrium characterization may switch active set | none | exact `23/10` H-only counterexample shows global extension false | none | no outside-`R+` welfare ranking |

There are no multiple independent markets, regions, or parallel subgames in the baseline. Cross-market selection-combination analysis is **NOT APPLICABLE**.

## 10. Institutional evidence table — primary sources rechecked 2026-09-12

| Institutional link | Status | Evidence | What it does / does not validate |
|---|---|---|---|
| Business seat pricing plus Enterprise custom pricing | **ESTABLISHED** | OpenAI Business pricing: https://openai.com/business/pricing/ | validates fixed-access / seat-based pricing and Enterprise custom contracts |
| Credit- and token-based Enterprise pricing | **ESTABLISHED** | OpenAI Business pricing and rate card: https://openai.com/business/pricing/ ; https://help.openai.com/en/articles/11481834 | validates usage-sensitive pricing measured by credits/tokens/tasks/messages/minutes; does not establish endogenous architecture switching |
| Business allowances with shared-credit overage | **ESTABLISHED** | OpenAI flexible pricing: https://help.openai.com/en/articles/11487671-flexible-pricing-for-the-enterprise-edu-and-business-plans | validates a hybrid access-plus-flexible-usage structure |
| Pricing/rate-card revisions can apply to existing enterprise plans | **ESTABLISHED as occurrence** | OpenAI Enterprise help: https://help.openai.com/en/articles/8265053-what-is-chatgpt-enterprise | validates post-adoption pricing-rule changes can occur; the installed-base causal mechanism remains **SUGGESTIVE / MODEL INTERPRETATION** |
| Organization-specific workflow/data integration | **ESTABLISHED as capability** | OpenAI plugins: https://openai.com/business/apps/ | validates technical embedding into CRM/data/collaboration/code systems; sunk-cost magnitude is **UNVERIFIED** |
| Deepening enterprise workflow use and productivity effects | **SUGGESTIVE for `b_j>0` / integration depth** | OpenAI State of Enterprise AI 2025: https://openai.com/business/guides-and-resources/the-state-of-enterprise-ai-2025-report/ | supports positive current workflow benefits and deeper integration; does not identify the structural primitive or non-expropriability |
| Pay-as-you-go cloud compute | **ESTABLISHED** | AWS EC2 On-Demand: https://aws.amazon.com/ec2/pricing/on-demand/ | validates a genuinely metered cloud setting without long-term commitment |
| Committed-spend cloud pricing | **ESTABLISHED** | Google Cloud Compute CUDs: https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview | validates 1-/3-year minimum resource/spend commitments as a distinct pricing architecture |
| Reciprocal integration-to-architecture feedback observed in OpenAI/AWS/GCP | **UNVERIFIED** | no primary causal evidence identified | remains a theoretical mechanism, not an empirical fact |

Institutional conclusion: the primitives "relationship-specific workflow integration" and "coexisting fixed/committed and usage-sensitive pricing forms" are defensible. The paper must not state that current vendors choose architecture because an installed high-use base became large; that arrow is model interpretation unless future empirical evidence is supplied.

## 11. Generality / robustness evidence-classification table

| Claim | Baseline form/class | Evidence type | Assumptions used | Current maximum defensible scope | Stage-7.5A attack target |
|---|---|---|---|---|---|
| `h_0<h_M<h_F` | quadratic utility, Uniform integration cost, two types, strict `R+` | analytic + independent active-set audit | lower H rent under metering, unique fixed point, strict both-served dominance | **BASELINE FUNCTIONAL FORM** | attack nonuniform costs jointly with active-set/global-continuation conditions |
| `mu_M<mu_F` | same | analytic | T1 plus increasing `Phi(h)` | **BASELINE FUNCTIONAL FORM** | verify no quantifier drift from `R+` |
| pure-regime gap | same | analytic + Stage 4A alternative-equilibrium audit | distinct states, monotone gain, strict active-set dominance | **BASELINE FUNCTIONAL FORM** with structural interpretation | attack multiple fixed points, nonmonotone gain, active-set switching |
| `h_M<h_F` + strictly increasing `Psi` => threshold ordering | abstract ordered states | direct order argument / prior Lean core | ordered unique states and StrictMono gain supplied as assumptions | **SUFFICIENT-CONDITION THEOREM / organizing lemma** | verify it is not presented as primitive economic generality |
| common-curvature cubic utility | nonquadratic strictly concave numerical example | independent numerical reoptimization in `verification/stage11b_astra_independent_audit.py` | common curvature, chosen primitives, both-served global active set | **NUMERICAL ROBUSTNESS ONLY** | reproduce after final scope freeze if cited |
| arbitrary strict concavity | broad concave utility class | **counterexample exists** | Stage-11B log-inverse-demand H vs quadratic L example | **NO GENERAL CLAIM ALLOWED** | retain counterexample as permanent scope guard |
| general integration-cost CDF | strictly increasing CDF candidate class | historical pre-repair analytic/numerical evidence, currently stale | monotone continuation rent map, interiority, no active-set switch | **CONJECTURED / RESTRICTED FUNCTION CLASS pending 7.5A** | redo proof under repaired global-continuation scope |
| W1 `mu_P>mu_W` | quadratic both-served branch | exact analytic identity | fixed installed base, anonymous tariff | **BASELINE FUNCTIONAL FORM** | attack nonquadratic utilities; do not generalize automatically |
| endogenous welfare ranking | quadratic strict `R+` | two opposite-sign examples | restricted commitment benchmark | **NUMERICAL COUNTEREXAMPLE / sign-indeterminacy** | preserve counterexamples; no sign theorem required |

The Stage-11B strictly concave counterexample is decisive: "strict concavity" or "H is the high-use type at the flat price" does not suffice for `h_M<h_F`. In the counterexample, relevant demand/surplus curves cross under metering and the ordering reverses. Any broader theorem would need explicit relevant-price ordering/single-crossing conditions or equivalent primitive restrictions.

## 12. Generality across genuinely different settings

### Setting A — enterprise generative AI

Relationship-specific integration can consist of workflow agents, private plugins, data connectors, organizational processes, permissions, and training/reconfiguration around AI use. The economic mapping is credible when integration precedes later tariff revision and expected tariff form affects the value of integrating high-use workflows.

Evidence status: pricing diversity and workflow integration are **ESTABLISHED**; the reciprocal causal feedback is **UNVERIFIED / MODEL INTERPRETATION**.

### Setting B — cloud compute and committed-spend contracting

Cloud customers may migrate workloads and build provider-specific operational integration before renewal or future contract choice. Current cloud markets visibly combine pay-as-you-go compute with one-/three-year committed-use/spend contracts.

The same mechanism can apply if:

1. migration/integration is sunk before a later architecture choice;
2. expected architecture changes relationship-specific investment;
3. the profitability difference between architectures changes with installed high-use workload composition.

Evidence status: tariff diversity is **ESTABLISHED**; the full feedback is **SUGGESTIVE / theoretical**.

The mechanism is therefore not logically specific to tokens or LLMs, but its empirical presence must be established market by market.

## 13. Empirical predictions / discipline

These are model implications, not established facts.

1. Within a regime satisfying the `R+` logic, a larger installed share/mass of high-use tasks raises the provider's relative incentive to meter.
2. Anticipated metering lowers high-use integration relative to anticipated flat pricing in the baseline strict `R+` environment.
3. If integration becomes architecture-insensitive, the expectation-contingent threshold split should disappear.
4. The model should fit poorly in markets where the provider optimally excludes the low-use class; active-set switching is not a minor perturbation but a scope boundary.
5. The same observed coexistence of fixed and usage-sensitive tariffs is not sufficient evidence for the mechanism; empirical work would need variation in expectations/integration followed by later architecture incentives.

No unconditional quality-improvement comparative static is promoted. Any quality-to-threshold statement remains conditional until a separately certified primitive mapping is supplied.

## 14. Result-to-exposition triage

| Headline result | Economic object | Candidate vehicle | Why this vehicle | Verified source | Later manuscript action |
|---|---|---|---|---|---|
| T1 `h_0<h_M<h_F` | architecture-conditioned integration states | lemma/proposition | needed for mechanism but not novelty by itself | Stage 4R/4A | state immediately before threshold theorem |
| T2 `mu_M<mu_F` | self-consistency thresholds | main proposition + one phase diagram | central comparative object and easiest visual intuition | Stage 4R/4A | preserve as central figure/theorem |
| T3 pure-regime gap | equilibrium architecture | main proposition | direct economic consequence of threshold split | Stage 4R/4A | pair with same phase diagram; mixed resolution subordinate |
| mixed `h*,rho*` | equilibrium resolution | concise corollary / numerical line | not novelty; algebra useful but should not dominate | Stage 4A | avoid presenting as separate contribution |
| B1 threshold collapse | mechanism identification benchmark | corollary/prose | isolates endogenous-integration feedback | Stage 6 | place immediately after T2/T3 |
| W1 fixed-base private/social wedge | welfare threshold decomposition | proposition or concise displayed identity | clean analytic welfare result | this Stage 7 | explicitly label fixed-installed-base |
| W2 endogenous sign ambiguity | restricted commitment welfare | small numerical table or prose | prevents overclaim rather than supplies headline theorem | `verification/stage7_repaired_verify.py` | one compact robustness table at most |
| strict `R+` active-set conditions | theorem domain | assumptions paragraph + appendix table | prevents globality confusion | Stage 4R/4A | make domain visible before propositions |
| institutional mapping | evidence status | concise prose/table | separates facts from model interpretation | primary sources above | retain FACT/SUGGESTIVE distinction |

No figure is required for welfare sign ambiguity. The threshold phase diagram remains the single most informative visual.

## 15. Policy scope and limits

Stage 7 supports no unconditional policy prescription favoring flat or metered pricing.

What can be said:

- private and social incentives to meter differ at a fixed installed base because rent extraction is privately valuable but socially a transfer;
- once integration adjusts endogenously, welfare can rank the architectures either way within the same repaired regular family;
- commitment can matter, but the model does not establish that a regulator should mandate a pricing architecture;
- no tax/subsidy, antitrust intervention, interoperability rule, or price regulation is modeled, so such prescriptions are outside scope.

## 16. Candidate counterexample / red-team targets for Stage 7.5A

1. Re-attack every theorem quantifier using strict `R+`, especially whether the complete candidate interval `[h_0,h_F]` is carried into all statements.
2. Verify the zero-surplus participation convention is reflected consistently in theorem statements and formal-fidelity notes.
3. Re-run the nonuniform integration-cost CDF argument under repaired active-set/global-continuation requirements; do not inherit the stale pre-repair certificate automatically.
4. Preserve the Stage-11B strictly concave counterexample `h_M>h_F` as a permanent bar against arbitrary-concavity wording.
5. Search for multiple architecture-conditioned integration fixed points under nonuniform CDFs or nonmonotone continuation rents.
6. Search for nonmonotone provider architecture gain `Psi(h)` outside quadratic/common-curvature examples.
7. Reconfirm the two opposite-sign P2 welfare examples satisfy every `R+` inequality; this is now automated.
8. Audit Lean statement fidelity: the existing proof-critical algebra remains useful, but it does not prove participation implementation, global active-set reduction, or the entire economic SPNE.
9. Check that no title/abstract wording implies an endogenous "model improvement" or quality theorem absent from the repaired contribution set.

## 17. Welfare evidence ledger

| Claim | Equilibrium/selection attack | Artifact | Result | Surviving limitation |
|---|---|---|---|---|
| exact `omega_j(p)` | symbolic identity | `verification/stage7_repaired_verify.py` | PASS | quadratic baseline |
| exact integration surplus `K_j n_j^2/2` | exact integration over cost distribution | same | PASS | Uniform baseline |
| W1 `mu_P-mu_W=d h p*>0` | symbolic subtraction, fixed-base benchmark audit | same | PASS | not a global endogenous theorem |
| P0 first best | complete planner choice-set reconstruction | this report | PASS | no policy instrument interpretation |
| P2 welfare sign ambiguity | opposite-sign examples + explicit `R+` checks | `verification/stage7_repaired_verify.py` | PASS | counterexample evidence, not sign theorem |
| strict-gap welfare selection | Stage-4A alternative-equilibrium / mixed-uniqueness audit | `docs/STAGE_04A_RECERTIFICATION.md` | PASS | strict `R+`, equality boundaries excluded |
| institutional tariff diversity | primary-source recheck | source table above | PASS | does not establish causal feedback |
| arbitrary-concavity generality | adversarial nonquadratic search | `verification/stage11b_astra_independent_audit.py` | FAILS as broad claim | explicit counterexample retained |

## 18. Remaining fatal / major concerns

No Stage-7 fatal blocker is identified.

Major issues carried forward, but not blockers for Stage 7.5:

1. **Contribution thickness:** novelty remains narrow. The paper must sell the reciprocal feedback / threshold splitting, not generic hold-up, pricing architecture or AI relevance.
2. **Domain visibility:** strict `R+` is substantive. It must be prominent rather than buried in an appendix.
3. **Generality:** arbitrary strict concavity is false; nonuniform-CDF generality is not yet re-certified after repair.
4. **Institutional causality:** vendor pricing diversity and workflow integration are facts; installed-base causality is not.
5. **Title:** “Model Improvement” remains unsupported by the headline theorem and should not survive final manuscript closeout unless independently justified by a certified theorem.

## 19. Canonical verdict and Stage 7.5 contract

**GO TO STAGE 7.5.**

Stage 7.5 must decide whether the complete paper is worth carrying forward given the narrow but surviving threshold-splitting contribution and the substantive `R+` domain restriction. It may not add extensions.

Carry forward exactly:

- planner register P0/P1/P2;
- W1 as a fixed-installed-base benchmark only;
- W2 as sign-indeterminacy / counterexample evidence only;
- strict-`R+` equilibrium-selection scope;
- institutional FACT vs SUGGESTIVE distinction;
- arbitrary-concavity counterexample;
- general-CDF result as pending renewed 7.5A certification, not inherited fact;
- result-to-exposition triage above.

If Stage 7.5 remains GO, Stage 7.5A must independently re-certify quantifiers, selection scope, benchmark terminology and formal statement fidelity before any new Stage-8 freeze.