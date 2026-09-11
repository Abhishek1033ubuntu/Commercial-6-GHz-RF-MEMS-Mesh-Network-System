# Commercial 6 GHz RF-MEMS Mesh Network System

Commercial-grade, high-performance Wi-Fi/6 GHz mesh node leveraging Menlo Micro RF-MEMS switches for full-duplex backhaul capacity and zero-bandwidth degradation across multi-hop topologies.

## System Highlights
- **RF Switching:** Menlo Micro MM5130 SP4T RF-MEMS switch (<0.4 dB insertion loss @ 6 GHz).
- **High-Voltage Driver:** Menlo Micro MM101 / MD05 Gate Driver (88V–90V DC bias).
- **PCB Architecture:** 4-Layer Hybrid Stackup (Top: Rogers RO4350B 0.254mm, $50\Omega$ CPWG; Inner/Bottom: FR-4).
- **Baseband & Wireless:** MediaTek MT7621AT SoC + MT7915D Wi-Fi 6E (5.925 GHz – 7.125 GHz UNII-5..8).
- **Firmware Integration:** OpenWrt kernel module (`kmod-mems-mesh-ctrl`) enforcing sub-10µs cold-switching under strict 0.5V power limits to prevent contact degradation.

## Directory Structure
```
├── hardware/
│   ├── MASTER_NODE_N00_6GHZ.net
│   └── pcb_stackup_spec.md
├── firmware/
│   ├── mems_mesh_driver.c
│   └── Makefile
├── docs/
│   ├── FINANCIAL_AND_COMPETITIVE_ANALYSIS.md
│   └── BOM_MASTER.csv
└── scripts/
└── financial_and_tech_sim.py
```
