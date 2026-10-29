.PHONY: all clean test firmware pypi help

all: firmware test

firmware:
	@echo "Checking C Kernel Driver Syntax..."
	gcc -fsyntax-only firmware/mems_mesh_driver.c
	@echo "Driver syntax OK."

test:
	@echo "Running Technical & Financial Simulations..."
	python3 scripts/financial_and_tech_sim.py

pypi:
	@echo "Building PyPI distribution..."
	python3 -m pip install --upgrade build twine
	python3 -m build
	@echo "Distribution ready in dist/"

clean:
	@echo "Cleaning temporary build files..."
	rm -rf dist/ *.egg-info build/ firmware/*.o firmware/*.ko

help:
	@echo "Commercial 6 GHz RF-MEMS Mesh System - Build Targets:"
	@echo "  make firmware  - Syntax-check C kernel driver"
	@echo "  make test      - Run Python RF & financial simulations"
	@echo "  make pypi      - Build PyPI release package"
	@echo "  make clean     - Remove temporary build artifacts"
	@echo ""
	@echo "See docs/FABRICATION_GUIDE.md for hardware Gerber export instructions."
