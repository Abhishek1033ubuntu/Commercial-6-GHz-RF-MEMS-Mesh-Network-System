#!/usr/bin/env python3
"""
Financial COGS and Unit Economics Simulation Script
"""

import json

def calculate_unit_economics(production_volume):
    mems_rf_switches = 15.20 if production_volume >= 10000 else 18.50
    hv_driver = 4.80 if production_volume >= 10000 else 6.20
    soc_main = 6.10 if production_volume >= 10000 else 7.80
    wifi_radio = 9.80 if production_volume >= 10000 else 12.40
    pcb_hybrid = 5.20 if production_volume >= 10000 else 8.50
    passives_and_misc = 5.47 if production_volume >= 10000 else 8.90

    cogs_raw = (mems_rf_switches + hv_driver + soc_main + 
                wifi_radio + pcb_hybrid + passives_and_misc)

    assembly_testing = 3.20 if production_volume >= 10000 else 4.50
    warranty_reserve = 1.80
    
    total_unit_cogs = cogs_raw + assembly_testing + warranty_reserve
    msrp = 129.99
    gross_margin_pct = ((msrp - total_unit_cogs) / msrp) * 100

    return {
        "Production Volume": production_volume,
        "Raw BOM ($)": round(cogs_raw, 2),
        "Total Unit COGS ($)": round(total_unit_cogs, 2),
        "Target MSRP ($)": msrp,
        "Gross Margin (%)": round(gross_margin_pct, 2)
    }

if __name__ == "__main__":
    print("--- Commercial Unit Economics Analysis ---")
    for vol in [1000, 10000, 50000]:
        print(json.dumps(calculate_unit_economics(vol), indent=2))
