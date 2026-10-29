"""
Unit COGS and Financial Feasibility Simulation Module
Author: Abhishek Singh
"""

import json


def calculate_unit_economics(production_volume: int = 10000) -> dict:
    """Calculates unit economics and margins based on target production volume.

    Args:
        production_volume (int): Target manufacturing run size (e.g., 1000,
          10000, 50000).

    Returns:
        dict: Itemized COGS breakdown, target MSRP, and gross margin percentage.
    """
    # Tiered pricing scaling
    is_volume = production_volume >= 10000

    mems_rf_switches = 15.20 if is_volume else 18.50
    hv_driver = 4.80 if is_volume else 6.20
    soc_main = 6.10 if is_volume else 7.80
    wifi_radio = 9.80 if is_volume else 12.40
    pcb_hybrid = 5.20 if is_volume else 8.50
    passives_and_misc = 5.47 if is_volume else 8.90

    cogs_raw = (
        mems_rf_switches
        + hv_driver
        + soc_main
        + wifi_radio
        + pcb_hybrid
        + passives_and_misc
    )

    assembly_testing = 3.20 if is_volume else 4.50
    warranty_reserve = 1.80

    total_unit_cogs = cogs_raw + assembly_testing + warranty_reserve
    msrp = 129.99
    gross_margin_pct = ((msrp - total_unit_cogs) / msrp) * 100

    return {
        "Production Volume": production_volume,
        "Raw BOM ($)": round(cogs_raw, 2),
        "Total Unit COGS ($)": round(total_unit_cogs, 2),
        "Target MSRP ($)": msrp,
        "Gross Margin (%)": round(gross_margin_pct, 2),
    }


def print_financial_report():
    """Prints a formatted financial breakdown across standard production volumes."""
    print("--- Commercial Unit Economics Analysis ---")
    for vol in [1000, 10000, 50000]:
        print(json.dumps(calculate_unit_economics(vol), indent=2))


if __name__ == "__main__":
    print_financial_report()
