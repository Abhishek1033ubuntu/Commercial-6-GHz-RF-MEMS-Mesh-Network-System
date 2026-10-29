# Commercial 6 GHz RF-MEMS Mesh Network System

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Abhishek1033ubuntu/Commercial-6-GHz-RF-MEMS-Mesh-Network-System/blob/main/scripts/RF_6GHz_MEMS_Simulation.ipynb)
![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)
![AI Collaborator](https://img.shields.io/badge/Co--Engineered%20With-Google%20Gemini-8E75B5?logo=googlegemini&logoColor=white)
![Build](https://img.shields.io/badge/OpenWrt%20Build-Passing-brightgreen.svg)
![RF Spectrum](https://img.shields.io/badge/RF%20Band-UNII--5..8%20(5.925--7.125%20GHz)-orange.svg)
![Hardware](https://img.shields.io/badge/PCB-Rogers%20RO4350B%204--Layer-red.svg)
![Latest Release](https://img.shields.io/github/v/release/Abhishek1033ubuntu/Commercial-6-GHz-RF-MEMS-Mesh-Network-System?color=blue)
![SemVer](https://img.shields.io/badge/SemVer-2.0.0-brightgreen.svg)
[![PyPI Version](https://img.shields.io/pypi/v/rf-mems-mesh-sim?color=blue)](https://pypi.org/project/rf-mems-mesh-sim/) 
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/rf-mems-mesh-sim)
![PyPI - License](https://img.shields.io/pypi/l/rf-mems-mesh-sim)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.23773556-blue?style=for-the-badge&logo=zenodo&logoColor=white)](https://doi.org/10.5281/zenodo.23773556)  

High-performance 6 GHz Wi-Fi mesh node utilizing **Menlo Micro RF-MEMS switches** for ultralow loss, full-duplex backhaul capacity across multi-hop node topologies.

## Licensing & Author Attribution

**Author:** Abhishek Singh ( UIDAI: 9414 9122 9013) 

AI Technical Collaborator: Google Gemini

This project is released under the **Apache License 2.0**. You are free to use, modify, and distribute this software and hardware design for both non-commercial and commercial purposes under the terms of the Apache 2.0 License.

For custom enterprise development, hardware fabrication consulting, or proprietary licensing inquiries, please contact the author directly.


Commercial-grade, high-performance Wi-Fi/6 GHz mesh node leveraging Menlo Micro RF-MEMS switches for full-duplex backhaul capacity and zero-bandwidth degradation across multi-hop topologies.

## System Highlights
- **RF Switching:** Menlo Micro MM5130 SP4T RF-MEMS switch (<0.4 dB insertion loss @ 6 GHz).
- **High-Voltage Driver:** Menlo Micro MM101 / MD05 Gate Driver (88V–90V DC bias).
- **PCB Architecture:** 4-Layer Hybrid Stackup (Top: Rogers RO4350B 0.254mm, $50\Omega$ CPWG; Inner/Bottom: FR-4).
- **Baseband & Wireless:** MediaTek MT7621AT SoC + MT7915D Wi-Fi 6E (5.925 GHz – 7.125 GHz UNII-5..8).
- **Firmware Integration:** OpenWrt kernel module (`kmod-mems-mesh-ctrl`) enforcing sub-10µs cold-switching under strict 0.5V power limits to prevent contact degradation.

## Directory Structure
```
.
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── workflows/
│       └── build-test.yml            # Automated kernel compile & Python sim check
├── docs/
│   ├── BOM_MASTER.csv                # Complete manufacturing BOM with 1k/10k pricing
│   ├── FABRICATION_GUIDE.md          # Gerber export & OpenWrt compilation guide 
│   ├── FINANCIAL_AND_COMPETITIVE_ANALYSIS.md
│   └── RF_6GHZ_STACKUP_SPEC.md       # Rogers RO4350B 50Ω CPWG specification
├── firmware/
│   ├── Makefile                      # OpenWrt Buildroot package recipe
│   └── src/
│       ├── Kbuild                    # Linux Kernel build rules
│       ├── Makefile                  # Local C compiler Makefile
│       └── mems_mesh_driver.c        # <10µs cold-switching kernel module
├── hardware/
│   ├── gerbers/                      # Ready-to-order manufacturing zip/gerbers
│   │   ├── MASTER_NODE-F_Cu.gbr
│   │   └── MASTER_NODE-Drill.drl
│   ├── MASTER_NODE_N00_6GHZ.kicad_pcb# KiCad PCB trace routing file
│   └── MASTER_NODE_N00_6GHZ.net      # Hardware schematic netlist
├── scripts/
│   └── financial_and_tech_sim.py     # Colab / Python Monte-Carlo unit economics sim
├── .gitignore                        # Build artifact exclusions
├── CLA.md                            # Contributor License Agreement for dual-licensing
├── LICENSE                           # Apache License, Version 2.0
├── Makefile                          # Top-level repository orchestration script
└── README.md                         # Public repository landing page & badge index
├── pyproject.toml                     # Modern Build System Config (Flit/Setuptools)
├── setup.cfg                          # Package Metadata
├── python_pkg/
     └── rf_mems_mesh_sim/
         ├── __init__.py                # Package Exports
         ├── cpwg_model.py              # Rogers RO4350B S-parameter calculations
         ├── cold_switch.py             # Sub-10µs cold-switching timing dynamics
         └── economics.py               # Unit COGS & Monte-Carlo financial model

```
## Quick Start & Local Verification

```bash
# Clone the repository
git clone [https://github.com/your-org/rf-mems-mesh-node.git](https://github.com/your-org/rf-mems-mesh-node.git)
cd rf-mems-mesh-node

# Run feasibility & financial simulations
make test

# Build Linux kernel driver module
make firmware
```

## Python Package Installation

Install the simulation suite directly via `pip`:

```bash
pip install rf-mems-mesh-sim
```
## Quick Usage
Python

```
import rf_mems_mesh_sim as sim

# 1. CPWG & Switch S-parameter simulation
sim.simulate_cpwg_sparameters()

# 2. Sub-10us cold-switching timing
sim.simulate_cold_switching()

# 3. Unit economics calculation
print(sim.calculate_unit_economics(10000))
```

## Licensing & Author Attribution  

**Lead Author & Principal Investigator:** Abhishek Singh | UIDAI: 9414 9122 9013 (<abhishek1033@gmail.com> | <abhishek.singh.941491229013@proton.me>)

AI Technical Collaborator: Google Gemini

Licensed under the Apache License, Version 2.0 (the "License"). You may obtain a copy of the License in the LICENSE file or at http://www.apache.org/licenses/LICENSE-2.0.

## ⚡ Support

| Platform | Link |
| :--- | :--- |
| **PayPal** | [![PayPal](https://img.shields.io/badge/Donate-PayPal-blue.svg?logo=paypal)](https://www.paypal.me/Abhishek1033ubuntu) |
| **GitHub Sponsors** | [![GitHub Sponsors](https://img.shields.io/badge/Sponsor-GitHub-ea4aaa.svg?logo=github)](https://github.com/sponsors/Abhishek1033ubuntu) |


## Citation & Attribution

If you use this reference hardware design, OpenWrt kernel module, or 6 GHz RF-MEMS simulation code in your academic research, commercial product, or technical report, please cite this project as follows:

**APA Style:**
> Singh, A. (2026). *Commercial 6 GHz RF-MEMS Mesh Network System* (Version 1.0.0) [Hardware Reference Design & OpenWrt Firmware]. GitHub. https://github.com/Abhishek1033ubuntu/Commercial-6-GHz-RF-MEMS-Mesh-Network-System

**BibTeX Entry (for LaTeX & Academic Papers):**
```bibtex
@misc{singh2026rfmemsmesh,
  author       = {Singh, Abhishek},
  title        = {{Commercial 6 GHz RF-MEMS Mesh Network System}},
  year         = {2026},
  publisher    = {GitHub},
  journal      = {GitHub Repository},
  howpublished = {\url{[https://github.com/Abhishek1033ubuntu/Commercial-6-GHz-RF-MEMS-Mesh-Network-System](https://github.com/Abhishek1033ubuntu/Commercial-6-GHz-RF-MEMS-Mesh-Network-System)}},
  note         = {Co-Engineered with Google Gemini. Distributed under the Apache License 2.0}
}
