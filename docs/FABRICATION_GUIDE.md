# Board Fabrication & OpenWrt Integration Guide

This guide details the exact steps to generate manufacturing Gerbers for board houses (JLCPCB, PCBWay, Sierra Circuits) and compile the OpenWrt kernel module.

---

## 1. PCB Gerber & NC Drill Export (KiCad v7/v8)

To export fabrication files from the schematic netlist (`hardware/MASTER_NODE_N00_6GHZ.net`) and layout specifications:

### A. Stackup Setup
1. Open the project in KiCad PCB Editor.
2. Navigate to **File → Board Setup → Board Stackup → Physical Stackup**.
3. Configure the 4 layers according to `RF_6GHZ_STACKUP_SPEC.md`:
   * **Layer 1 (Top RF):** Rogers RO4350B (0.254 mm / 10 mil thickness, $\varepsilon_r = 3.66$).
   * **Layer 2 (RF GND):** Solid Ground Plane (35 µm Cu).
   * **Layer 3 (Power/HV):** 88V Gate Bias & Power Rails (35 µm Cu).
   * **Layer 4 (Digital Bottom):** FR-4 Core (1.0 mm thickness).

### B. Design Rule Check (DRC)
1. Go to **Inspect → Design Rules Checker**.
2. Set the minimum $50\,\Omega$ CPWG trace clearance to **0.22 mm** (8.7 mils).
3. Set the 88V High-Voltage isolation clearance to **0.8 mm**.
4. Click **Run DRC** and resolve all clearance errors.

### C. Gerber Output Export
1. Go to **File → Fabrication Outputs → Gerbers (.gbr)**.
2. Select layers: `F.Cu`, `B.Cu`, `In1.Cu`, `In2.Cu`, `F.Silkscreen`, `B.Silkscreen`, `F.Mask`, `B.Mask`, and `Edge.Cuts`.
3. Check **Use Protel filename extensions** and click **Plot**.
4. Click **Generate Drill Files...**, set Units to **Millimeters**, and click **Generate Drill File**.
5. Compress all exported `.gbr` and `.drl` files into a single archive: `hardware/gerbers/MASTER_NODE_N00_6GHZ_Gerbers.zip`.

---

## 2. OpenWrt Buildroot Integration & Driver Compilation

To build the `mems_mesh_driver.c` kernel module into an OpenWrt firmware image:

### A. Environment Setup
```bash
# Navigate to your OpenWrt SDK directory
cd /path/to/openwrt-sdk

# Create package target directory
mkdir -p package/kernel/mems-mesh-ctrl

# Copy firmware package from repository
cp -r /path/to/repo/firmware/* package/kernel/mems-mesh-ctrl/

```

### B. Selection & Build

```bash
# Launch OpenWrt configuration menu
make menuconfig

# Navigate to: Kernel modules -> Network Devices
# Select <M> or <*> for kmod-mems-mesh-ctrl

# Compile the driver package
make package/kernel/mems-mesh-ctrl/compile V=s

```

### C. Deployment Verification

On the active node, install and verify kernel actuation via SSH:

```bash
# Install package
opkg install kmod-mems-mesh-ctrl_1.0-1_mipsel_24kc.ipk

# Load module and verify dmesg outputs
insmod mems_mesh_driver.ko
dmesg | grep mems_mesh_ctrl

```
