.PHONY: all clean test firmware hardware-check

all: firmware test

firmware:
	@echo "Building Kernel Module via local toolchain..."
	$(MAKE) -C firmware/src

test:
	@echo "Running Financial & Technical Feasibility Simulation..."
	python3 scripts/financial_and_tech_sim.py

clean:
	@echo "Cleaning build artifacts..."
	$(MAKE) -C firmware/src clean
