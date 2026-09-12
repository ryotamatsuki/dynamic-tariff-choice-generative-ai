# Repaired Stage 8 — Welfare / Benchmark Register

Date: 2026-09-12 (JST)

Tariff payments are transfers. Total welfare counts current integration benefit, future gross task value, inference cost, sunk integration cost, and real metering activation cost.

For served type `j` under usage price `p`,

`omega_j(p)=[(a_j-c)^2-(p-c)^2]/2`.

For installed masses `(l,h)`,

`W_A=b_L l+b_H h-K_L l^2/2-K_H h^2/2+l omega_L(p_A)+h omega_H(p_A)-1{A=M}mu`.

## P0 — First best

The only benchmark called **first best** is the planner choosing integration and usage directly:

`max_{x in {0,1},q>=0} x[b_j+a_j q-q^2/2-cq-k]`.

Thus `q_j^FB=max{a_j-c,0}` and integration occurs iff

`k<=b_j+(a_j-c)_+^2/2`.

## P1 — Fixed-installed-base comparison

Hold `(l,h)` fixed and compare provider-optimal flat and metered decentralized allocations. This is not first best.

Provider private metering threshold:

`mu_P=(l+h)/2[c+d h/(l+h)]^2`.

Social threshold for the same fixed installed allocation:

`mu_W=(l+h)/2[c^2-d^2(h/(l+h))^2]`.

Exact identity:

`mu_P-mu_W=d h p*(h)>0`.

Maximum wording: holding installed masses fixed, the monopolist meters over a larger activation-cost region than a social evaluator comparing the same decentralized allocations.

## P2 — Restricted architecture-commitment benchmark

Commit only the future architecture before integration; tariff parameters are reoptimized later within that architecture. Compare flat and metered welfare at their architecture-induced installed states.

This is a restricted-instrument commitment benchmark, not first best. Strict-`R+` examples deliver both welfare rankings. No universal sign is frozen.

## Selection scope

On the strict certified branch, aggregate equilibrium is unique in the interior regions covered by T1–T3. Boundary cases `mu=mu_M,mu_F` admit architecture indifference and are excluded from selection-free welfare statements. Outside `R+`, global welfare is not characterized.

## Formal coverage

The identity and positivity of W1 are formally checked only as a proof-critical algebraic core. Planner interpretation, endogenous integration welfare, and benchmark construction remain analytically certified rather than fully formalized.
