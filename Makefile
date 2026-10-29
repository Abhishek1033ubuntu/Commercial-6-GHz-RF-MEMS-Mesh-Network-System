.PHONY: all clean test firmware docs help

Default target runs when typing just make

all: firmware test

help:
@echo ""
@echo " Commercial 6 GHz RF-MEMS Mesh Network System — Build & Automation Menu "
@echo ""
@echo ""
@echo " Available Commands:"
@echo "   make help       - Display this assistance menu and usage instructions."
@echo "   make test       - Execute Python/scikit-rf simulation & COGS unit economics."
@echo "   make firmware   - Compile local C kernel module (mems_mesh_driver.ko)."
@echo "   make clean      - Remove firmware build artifacts and temp files."
@echo "   make docs       - Open and view the board fabrication & OpenWrt guide."
@echo ""
@echo " Documentation & Fabrication Pointer:"
@echo "   For step-by-step KiCad Gerber export guidelines and OpenWrt SDK integration,"
@echo "   please refer directly to: docs/FABRICATION_GUIDE.md"
@echo "========================================================================"

firmware:
@echo "Building Kernel Module via local toolchain..."
$(MAKE) -C firmware/src

test:
@echo "Running Financial & Technical Feasibility Simulation..."
python3 scripts/financial_and_tech_sim.py

docs:
@echo "Refer to docs/FABRICATION_GUIDE.md for fabrication and build instructions:"
@cat docs/FABRICATION_GUIDE.md 2>/dev/null || echo "File docs/FABRICATION_GUIDE.md not found."

clean:
@echo "Cleaning build artifacts..."
$(MAKE) -C firmware/src clean
