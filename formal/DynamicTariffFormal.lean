import Mathlib

namespace DynamicTariffFormal

/-- Provider meters when the real activation cost is below gross metering gain. -/
def MeteredPreferred (μ gain : ℝ) : Prop := μ < gain

/-- Provider prefers flat pricing when gross metering gain is below activation cost. -/
def FlatPreferred (μ gain : ℝ) : Prop := gain < μ

/--
Order-theoretic core of threshold separation.
This theorem does not derive the economic state ordering or the metering-gain map;
it certifies the implication once those two objects satisfy the stated order conditions.
-/
theorem threshold_separation
    {Ψ : ℝ → ℝ} {hM hF : ℝ}
    (hΨ : StrictMono Ψ) (hstate : hM < hF) :
    Ψ hM < Ψ hF := by
  exact hΨ hstate

/--
If the metered-induced and flat-induced thresholds are respectively Ψ hM and Ψ hF,
then any activation cost strictly between them makes the provider want to meter at
the flat-induced state and want to return to flat at the metered-induced state.
-/
theorem strict_gap_reverses_pure_responses
    {Ψ : ℝ → ℝ} {hM hF μ : ℝ}
    (hLow : Ψ hM < μ) (hHigh : μ < Ψ hF) :
    MeteredPreferred μ (Ψ hF) ∧ FlatPreferred μ (Ψ hM) := by
  exact ⟨hHigh, hLow⟩

/-- An antitone real-valued map has at most one fixed point. -/
theorem antitone_fixedPoint_unique
    {T : ℝ → ℝ} (hT : Antitone T)
    {x y : ℝ} (hx : T x = x) (hy : T y = y) :
    x = y := by
  apply le_antisymm
  · by_contra hxy
    have hyx : y < x := lt_of_not_ge hxy
    have hmap : T x ≤ T y := hT (le_of_lt hyx)
    rw [hx, hy] at hmap
    exact (not_lt_of_ge hmap) hyx
  · by_contra hyx
    have hxy : x < y := lt_of_not_ge hyx
    have hmap : T y ≤ T x := hT (le_of_lt hxy)
    rw [hy, hx] at hmap
    exact (not_lt_of_ge hmap) hxy

/--
If an antitone metering-induced integration map crosses below the 45-degree line
at the flat-induced state, every fixed point lies strictly below that state.
-/
theorem fixedPoint_below_flat_state
    {T : ℝ → ℝ} (hT : Antitone T)
    {hM hF : ℝ} (hfix : T hM = hM) (hbelow : T hF < hF) :
    hM < hF := by
  by_contra hnot
  have hle : hF ≤ hM := le_of_not_gt hnot
  have hmap : T hM ≤ T hF := hT hle
  rw [hfix] at hmap
  linarith

/--
Repair-specific lower-state skeleton. If an antitone integration map lies above
the 45-degree line at the zero-rent installed state h0, every fixed point lies
strictly above h0.
-/
theorem fixedPoint_above_zeroRentState
    {T : ℝ → ℝ} (hT : Antitone T)
    {h0 hM : ℝ} (hfix : T hM = hM) (habove : h0 < T h0) :
    h0 < hM := by
  by_contra hnot
  have hle : hM ≤ h0 := le_of_not_gt hnot
  have hmap : T h0 ≤ T hM := hT hle
  rw [hfix] at hmap
  linarith

/--
Repaired Stage-4R ordering skeleton: an antitone map with a fixed point, an
above-45-degree crossing at h0, and a below-45-degree crossing at hF places the
fixed point strictly inside (h0,hF).
-/
theorem fixedPoint_between_states
    {T : ℝ → ℝ} (hT : Antitone T)
    {h0 hM hF : ℝ} (hfix : T hM = hM)
    (habove : h0 < T h0) (hbelow : T hF < hF) :
    h0 < hM ∧ hM < hF := by
  exact ⟨fixedPoint_above_zeroRentState hT hfix habove,
    fixedPoint_below_flat_state hT hfix hbelow⟩

/--
Conditional uniqueness of the mixed installed state: a strictly decreasing state
response composed with a strictly increasing gross metering-gain map can hit a
given activation cost at most once.
-/
theorem mixed_state_unique
    {hOfRho Ψ : ℝ → ℝ} (hh : StrictAnti hOfRho) (hΨ : StrictMono Ψ)
    {ρ₁ ρ₂ μ : ℝ}
    (h1 : Ψ (hOfRho ρ₁) = μ) (h2 : Ψ (hOfRho ρ₂) = μ) :
    ρ₁ = ρ₂ := by
  by_contra hne
  rcases lt_or_gt_of_ne hne with hlt | hgt
  · have hs : Ψ (hOfRho ρ₂) < Ψ (hOfRho ρ₁) := hΨ (hh hlt)
    rw [h1, h2] at hs
    exact (lt_irrefl μ) hs
  · have hs : Ψ (hOfRho ρ₁) < Ψ (hOfRho ρ₂) := hΨ (hh hgt)
    rw [h1, h2] at hs
    exact (lt_irrefl μ) hs

/-- Positivity of the exact baseline derivative expression for Φ_h. -/
theorem baseline_phi_derivative_positive
    {c d l h : ℝ}
    (hc : 0 < c) (hd : 0 < d) (hl : 0 < l) (hh : 0 ≤ h) :
    0 <
      ((c * (l + h) + d * h) *
        (c * (l + h) + d * h + 2 * d * l)) /
        (2 * (l + h)^2) := by
  positivity

/--
An endpoint active-set dominance check propagates backward over an interval when
the rival-minus-preferred profit difference is monotone increasing.
-/
theorem endpoint_dominance_propagates
    {D : ℝ → ℝ} (hD : Monotone D)
    {h hF : ℝ} (hle : h ≤ hF) (hend : D hF < 0) :
    D h < 0 := by
  exact lt_of_le_of_lt (hD hle) hend

/--
Exact fixed-installed-base welfare identity used at repaired Stage 7. Here pStar
is the baseline provider-optimal metered usage price. The theorem certifies the
algebraic wedge, not the economic derivation of either threshold.
-/
theorem private_social_wedge_identity
    {c d l h : ℝ} (hn : l + h ≠ 0) :
    let pStar : ℝ := c + d * h / (l + h)
    let μP : ℝ := (l + h) * pStar^2 / 2
    let μW : ℝ := (l + h) * (c^2 - d^2 * (h / (l + h))^2) / 2
    μP - μW = d * h * pStar := by
  dsimp
  field_simp [hn]
  ring

/-- Positivity of the repaired Stage-7 fixed-base wedge on the strict branch. -/
theorem private_social_wedge_positive
    {c d l h : ℝ}
    (hc : 0 < c) (hd : 0 < d) (hl : 0 < l) (hh : 0 < h) :
    0 < d * h * (c + d * h / (l + h)) := by
  have hden : 0 < l + h := by positivity
  positivity

/--
Exact arithmetic scope guard: at the retained out-of-R installed composition,
H-only flat pricing beats the both-served flat continuation by 23/10.
-/
theorem hOnly_scope_counterexample :
    let aL : ℚ := 4
    let aH : ℚ := 5
    let c : ℚ := 1
    let l : ℚ := 1 / 10
    let h : ℚ := 3 / 5
    let both : ℚ := (l + h) * aL^2 / 2 - c * (l * aL + h * aH)
    let hOnly : ℚ := h * aH^2 / 2 - c * h * aH
    hOnly - both = 23 / 10 := by
  norm_num

#print axioms threshold_separation
#print axioms strict_gap_reverses_pure_responses
#print axioms antitone_fixedPoint_unique
#print axioms fixedPoint_below_flat_state
#print axioms fixedPoint_above_zeroRentState
#print axioms fixedPoint_between_states
#print axioms mixed_state_unique
#print axioms baseline_phi_derivative_positive
#print axioms endpoint_dominance_propagates
#print axioms private_social_wedge_identity
#print axioms private_social_wedge_positive
#print axioms hOnly_scope_counterexample

end DynamicTariffFormal
