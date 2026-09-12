# Repaired Stage 8 — Model Register

Date: 2026-09-12 (JST)

## Baseline primitives

One monopoly provider and two atomless task classes `j in {L,H}`. Future utility is `v_j(q)=a_j q-q^2/2`, with `0<c<a_L<a_H`, `d=a_H-a_L>0`. Real inference cost is `c q`; metering activation cost is `mu>=0`. Integration costs are `k~Uniform[0,K_j]`; integration yields non-expropriable current benefit `b_j>0`.

Timing: integration -> current benefit -> provider observes installed masses `(l,h)` -> provider chooses future architecture and tariff -> participation/usage.

Tariff family is anonymous `T(q)=F+p q`; flat has `p=0`, metered/hybrid has `p>0`. A future task participates iff continuation utility is weakly nonnegative; zero-surplus tasks participate. Usage is `q_j(p)=max{a_j-p,0}`. The exact integration-cutoff type integrates; it has measure zero under the continuous baseline distribution.

## Global continuation game

Gross surplus before `F` is `S_j(p)=max{a_j-p,0}^2/2`. Since `S_H>=S_L`, the relevant participation regimes are both served (`F=S_L(p)`), H-only (`F=S_H(p)`), and no service. Anonymous tariffs cannot serve L while excluding installed H.

Flat continuation:

`V_F(l,h)=max{Pi_F^B(l,h),Pi_F^H(h),0}`,

where `Pi_F^B=(l+h)a_L^2/2-c(l a_L+h a_H)` and `Pi_F^H=h a_H^2/2-c h a_H`.

Both-served metered profit is

`Pi_M^B(p|l,h)=(l+h)(a_L-p)^2/2+(p-c){l(a_L-p)+h(a_H-p)}`.

Its interior maximizer is `p_B(l,h)=c+d h/(l+h)`. H-only metering is maximized at `p=c`, with `Pi_M^H=h(a_H-c)^2/2`. Off path,

`V_M(l,h)=max{max_{0<p<=a_L}Pi_M^B(p|l,h),Pi_M^H(h),0}`.

Provider architecture choice compares `V_F(l,h)` with `V_M(l,h)-mu`; equality permits mixing. This defines provider continuation play at every installed state.

## Candidate interval and strict R+

Let `R_F=(a_H^2-a_L^2)/2`, `l=b_L/K_L`, `h_0=b_H/K_H`, `h_F=(b_H+R_F)/K_H`. Every rational-expectations candidate H mass lies in `[h_0,h_F]`.

Headline results require strict `R+`:

1. `0<c<a_L<a_H`, `K_L,K_H,b_L,b_H>0`;
2. `l in (0,1)`;
3. `d c < b_H+R_F < K_H`;
4. `p_B(l,h_F)<a_L`;
5. `Pi_F^B(l,h_0)>0` and `Pi_F^B(l,h_F)>0`;
6. `Pi_F^B(l,h_F)>Pi_F^H(h_F)`;
7. `Pi_M^B(p_B(l,h_F)|l,h_F)>Pi_M^H(h_F)`.

The repaired Stage 4A audit shows these endpoint conditions give strict both-served dominance over the complete candidate interval. No global theorem outside `R+` is frozen.

## Equilibrium objects on R+

`h_M` is the unique root of `K_H h=b_H+R_F-d[c+d h/(l+h)]`, with `h_0<h_M<h_F`.

`Phi(l,h)=(l+h)/2[c+d h/(l+h)]^2`, with `Phi_h>0`.

`mu_M=Phi(l,h_M)` and `mu_F=Phi(l,h_F)`.

For `mu_M<mu<mu_F`, neither pure architecture is self-consistent; the certified branch has a unique aggregate mixed resolution `(h*,rho*)`, where `Phi(l,h*)=mu` and `rho*=K_H(h_F-h*)/[d p_B(l,h*)] in (0,1)`.
