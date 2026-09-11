# 4-Layer Hybrid PCB Stackup & RF Geometry

## Substrate Stackup
- **Layer 1 (Top RF Signal):** Rogers RO4350B (0.254 mm / 10 mil thickness, $\epsilon_r = 3.66$, $\tan\delta = 0.0037$). 1.0 oz (35 µm) electro-deposited copper foil.
- **Layer 2 (RF Ground Plane):** Solid ground plane, 1.0 oz copper. No splits underneath RF traces or MM5130 package.
- **Layer 3 (Power & HV Bias):** FR-4 core (1.0 mm thickness). Carries 88V–90V DC gate bias lines and regulated 5V/3.3V/1.8V supply rails.
- **Layer 4 (Digital Bottom):** FR-4, 1.0 oz copper. High-speed digital lines, PCIe, GPIO, UART.

## 6 GHz CPWG Impedance Matching
- **Target Impedance:** $50\,\Omega \pm 2\%$ @ 6.5 GHz center frequency.
- **Trace Width ($W$):** 0.48 mm (19 mils).
- **Ground Gap ($S$):** 0.22 mm (8.7 mils).
- **Via Stitching:** Ground via fence spaced at 1.2 mm pitch along both sides of CPWG traces.
- **Creepage & Clearance:** Minimum 0.8 mm distance between Layer 3 90V HV traces and logic/RF ground fills.
