import Lake
open Lake DSL

package «dynamic-tariff-choice-generative-ai» where

require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git" @ "v4.33.1"

lean_lib DynamicTariffFormal where
  srcDir := "formal"
