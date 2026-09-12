# Stage 8 — Welfare / Benchmark Register

## Welfare accounting

Tariff payments are transfers between provider and users and do not enter total welfare. Real objects are current integration benefit, future gross task value, inference cost, sunk integration cost, and real metering activation cost.

For served type `j` under usage price `p`, real future operating surplus is

`omega_j(p)=[(a_j-c)^2-(p-c)^2]/2`.

For installed masses `(l,h)` and architecture `A`,

`W_A=b_L l+b_H h-K_L l^2/2-K_H h^2/2+l omega_L(p_A)+h omega_H(p_A)-1{A=M}mu`.

## P0 — First best

The only benchmark labeled **first best** is the unrestricted relevant planner choosing integration and usage directly:

`max_{x in {0,1},q>=0} x[b_j+a_j q-q^2/2-cq-k]`.

Hence

`q_j^FB=max{a_j-c,0}`

and integration occurs iff

`k <= b_j+(a_j-c)_+^2/2`.

## P1 — Fixed-installed-base architecture benchmark

Hold `(l,h)` fixed and compare provider-optimal flat and metered continuations. This is not first best.

Provider private metering threshold:

`mu_P=(l+h)/2 [c+d h/(l+h)]^2`.

Fixed-allocation social threshold:

`mu_W=(l+h)/2 [c^2-d^2(h/(l+h))^2]`.

Exact identity:

`mu_P-mu_W=d h p*(h)>0`.

Maximum wording: holding installed allocation fixed, the monopolist meters over a larger activation-cost region than a social evaluator comparing the same decentralized allocations.

## P2 — Restricted architecture-commitment benchmark

Commit only the future architecture before integration and allow future tariff-parameter reoptimization inside that architecture. Compare `W_F(l,h_F)` with `W_M(l,h_M)`.

This is a restricted-instrument commitment benchmark, not first best.

No unconditional sign survives. Numerical counterexamples within the baseline family produce both rankings, so no generic welfare superiority claim is frozen.

## Selection scope

On strict certified regions, equilibrium is unique on the regular branch, so welfare can be stated for that branch without an added selection rule. At `mu=mu_M` or `mu_F`, tie sets exist and no selection-free boundary welfare claim is frozen. Outside `R`, global welfare is not characterized.
