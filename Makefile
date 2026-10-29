.PHONY: all clean test firmware help

all: firmware test

firmware:
	@echo "Checking C Kernel Driver Syntax..."
	@gcc -fsyntax-only firmware/mems_mesh_driver.c 2>/dev/null || gcc -fsyntax-only firmware/src/mems_mesh_driver.c
	@echo "Driver syntax OK."

test:
	@echo "Running Technical & Financial Simulations..."
	@python3 scripts/financial_and_tech_sim.py

clean:
	@echo "Cleaning temporary build files..."
	@rm -rf dist/ *.egg-info build/

help:
	@echo "Commercial 6 GHz RF-MEMS Mesh System - Build Targets:"
	@echo "  make firmware  - Syntax-check C kernel driver"
	@echo "  make test      - Run Python RF & financial simulations"
	@echo "  make clean     - Remove temporary build artifacts"
	@echo ""
	@echo "See docs/FABRICATION_GUIDE.md for hardware Gerber export instructions."
