# 4-Layer Hybrid PCB Stackup & 6 GHz CPWG Geometry

## PCB Stackup Specifications
- **Layer 1 (Top RF Signal):** Rogers RO4350B (0.254 mm / 10 mil height, $\epsilon_r = 3.66$, $\tan\delta = 0.0037$). 1.0 oz (35 µm) electro-deposited copper.
- **Layer 2 (RF Ground Plane):** Solid continuous ground plane, 1.0 oz copper. No splits underneath RF traces or MM5130 switch IC.
- **Layer 3 (Power & HV Bias):** FR-4 core (1.0 mm height). Carries 88V–90V DC gate bias routing and 5V/3.3V/1.8V power rails.
- **Layer 4 (Digital Bottom):** FR-4, 1.0 oz copper. Digital logic, PCIe lanes, GPIO, and console UART.

## 6.5 GHz CPWG Trace Dimensions
- **System Impedance ($Z_0$):** 50 Ω ± 2%
- **Trace Width ($W$):** 0.48 mm (19 mils)
- **Ground Gap ($S$):** 0.22 mm (8.7 mils)
- **Via Stitching:** Ground via fence spaced at 1.2 mm pitch along both CPWG ground pours.
- **HV Isolation:** Minimum 0.8 mm clearance between Layer 3 90V HV traces and low-voltage digital/RF ground fills.
