# Stage 8 — Model Register

## Players and primitives

One monopoly provider and a continuum of potential enterprise task integrations in classes `j in {L,H}`. Each potential task has sunk integration cost `k` and receives current/pre-repricing benefit `b_j>0` if integrated.

Baseline future value:

`v_j(q)=a_j q-q^2/2`, with `0<c<a_L<a_H` and `d=a_H-a_L>0`.

Provider real inference cost is `c q`. Metering carries real activation cost `mu>=0`.

Baseline integration costs: `k~Uniform[0,K_j]`, normalized potential mass one per class.

## Timing and information

1. Tasks decide whether to integrate.
2. Current benefit `b_j` is realized and is not expropriable by later repricing.
3. Provider observes installed masses `(l,h)`.
4. Provider chooses future tariff architecture and tariff parameters.
5. Integrated tasks decide future participation and usage.

Users are forward-looking and atomless. They take aggregate masses and any provider mixing probability as given. Provider cannot commit ex ante to the complete future tariff schedule.

## Choice and strategy sets

Users choose integrate/not integrate and, if served, `q>=0` with voluntary participation.

Provider tariff family is anonymous `T(q)=F+p q`.

- flat architecture: `p=0`;
- metered/hybrid architecture: `p>0`.

Provider chooses feasible `(F,p)` globally within the architecture. No discriminatory menu, arbitrary nonlinear tariff, competition, congestion, capacity choice, intermediary layer, or additional state is part of the frozen baseline.

## Demand and continuation surplus

Conditional usage under `T(q)=F+p q`:

`q_j=max{a_j-p,0}`.

Indirect gross surplus before `F`:

`S_j(p)=(a_j-p)^2/2` when `p<a_j`.

A task integrates iff sunk cost does not exceed current benefit plus expected future continuation rent.

## Certified regular region R

Baseline theorem is restricted to parameter vectors satisfying:

- `K_L,K_H>0`;
- `l=b_L/K_L in (0,1)`;
- `R_F=(a_H^2-a_L^2)/2` and `d c < b_H+R_F < K_H`;
- relevant interior metered price below `a_L`;
- on the full relevant installed-state interval, globally optimal flat and metered continuations both serve L and H rather than H-only/no-service.

The final condition is a substantive active-set restriction.

## Equilibrium concept

Rational-expectations / subgame-perfect continuation logic in an atomless continuum integration game. Provider chooses a global continuation optimum after observing installed masses.

Equality boundaries `mu=mu_M` and `mu=mu_F` are excluded from the strict headline theorem because of provider indifference. Global equilibrium characterization outside `R` is not claimed.

## Baseline equilibrium objects

`p(h)=c+d h/(l+h)`.

`Phi(l,h)=(l+h)/2 * [c+d h/(l+h)]^2`.

`Phi_h=[c(l+h)+dh][c(l+h)+dh+2dl]/[2(l+h)^2] > 0`.

`h_F=(b_H+R_F)/K_H`.

`h_M` is the unique root in `(0,h_F)` of

`K_H h=b_H+R_F-d[c+d h/(l+h)]`.

`mu_M=Phi(l,h_M)` and `mu_F=Phi(l,h_F)`.
