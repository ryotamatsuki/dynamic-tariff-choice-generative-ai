# Dynamic Tariff Choice for Generative AI

Theory project on dynamic tariff architecture, sunk AI-specific integration, and welfare.

## Status

**Stage 7.5A passed — Stage 8 Canonical Theory Freeze authorized.**

The post-Stage-11B repair route is complete through the final pre-freeze gate:

- Stage 4R repair: PASS
- repeated Stage 4A: PASS
- Stage 6: GO
- Stage 7: GO
- Stage 7.5: GO
- Stage 7.5A: **GO — GENERALITY / QUANTIFIER CERTIFICATION PASS**
- Formal Verification Gate: **FORMAL VERIFICATION PASS**
- Next stage: **Stage 8 — Canonical Theory Freeze**

Portfolio status SSOT: `ryotamatsuki/economic-theory-research-portfolio#30`.

## Repaired mechanism

On strict `R+`, every rational-expectations H installed state lies in `[h_0,h_F]`, and both-served flat and metered continuations are strict global active-set optima over that candidate interval. Anticipated metering induces `h_M<h_F`; provider metering gain rises with the installed high-use state; therefore `mu_M<mu_F`. For `mu_M<mu<mu_F`, neither pure architecture is self-consistent and the certified branch has a unique aggregate mixed resolution.

The surviving contribution is the reciprocal feedback

`expected architecture -> continuation rent -> sunk integration -> installed high-use state -> relative architecture profitability -> architecture choice`.

Architecture-insensitive integration collapses the threshold split.

## Final pre-freeze scope

- T1–T3 are quadratic-baseline results on strict `R+`.
- The abstract order result is an organizing sufficient-condition lemma.
- Common-curvature nonquadratic evidence is numerical robustness only.
- Arbitrary strict concavity is not a valid general theorem.
- No non-Uniform integration-cost CDF theorem is carried into the repaired freeze.
- The fixed-installed-base welfare wedge is not a global endogenous-welfare theorem.
- Institutional evidence motivates tariff diversity and workflow integration but does not establish the model's causal feedback empirically.

Canonical Stage-7.5A records:

- `docs/STAGE_075A_REPAIRED_CERTIFICATION.md`
- `verification/stage075a_scope_verify.py`
- `formal/FORMAL_VERIFICATION_CERTIFICATE_REPAIRED.md`
- `formal/DynamicTariffFormal.lean`

The repaired formal build passed on commit `d6ac2a4bca0bf10dbfea23b274951d15b39d8551`, workflow run `34678945920`. Lean certifies a targeted proof-critical core only, not the complete economic game or equilibrium correspondence.

Recommended manuscript title after refreeze: **Dynamic Tariff Choice for Generative AI: Integration, Commitment, and Welfare**.

The pre-repair Stage-8 freeze and Stage-10 manuscript remain historical/stale until the new Stage-8 freeze is completed.
