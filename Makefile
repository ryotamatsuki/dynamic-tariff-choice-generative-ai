PYTHON ?= python3

.PHONY: all verify verify-python verify-lean artifacts paper clean

all: verify artifacts paper

verify: verify-python verify-lean

verify-python:
	$(PYTHON) verification/baseline_checks.py
	$(PYTHON) verification/robustness_checks.py
	$(PYTHON) verification/stage4a_repair_independent.py
	$(PYTHON) verification/stage7_repaired_verify.py
	$(PYTHON) -m unittest discover -s tests -v
	$(PYTHON) scripts/check_integrity.py

verify-lean:
	lake build DynamicTariffFormal
	@if grep -R -n -E 'sorry|admit' formal/*.lean; then echo 'Forbidden proof placeholder found.'; exit 1; fi

artifacts:
	$(PYTHON) scripts/generate_outputs.py

paper: artifacts
	latexmk -pdf -interaction=nonstopmode -halt-on-error -cd paper/main.tex

clean:
	latexmk -C -cd paper/main.tex || true
	rm -f figures/threshold_phase.tex tables/baseline_example.tex
