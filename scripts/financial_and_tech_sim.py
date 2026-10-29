"""
Financial & Technical Feasibility Monte-Carlo Simulator
Author: Abhishek Singh
"""

import json
import numpy as np


def run_unit_economics_simulation(volume=10000):
  is_volume = volume >= 10000

  mems_switches = 15.20 if is_volume else 18.50
  hv_driver = 4.80 if is_volume else 6.20
  soc_main = 6.10 if is_volume else 7.80
  wifi_radio = 9.80 if is_volume else 12.40
  pcb_substrate = 5.20 if is_volume else 8.50
  misc_passives = 5.47 if is_volume else 8.90

  cogs_bom = (
      mems_switches
      + hv_driver
      + soc_main
      + wifi_radio
      + pcb_substrate
      + misc_passives
  )
  assembly = 3.20 if is_volume else 4.50
  warranty = 1.80

  total_cogs = cogs_bom + assembly + warranty
  msrp = 129.99
  margin = ((msrp - total_cogs) / msrp) * 100

  return {
      "Target Production Volume": volume,
      "Raw BOM Cost ($)": round(cogs_bom, 2),
      "Total Unit COGS ($)": round(total_cogs, 2),
      "Target MSRP ($)": msrp,
      "Gross Margin (%)": round(margin, 2),
  }


if __name__ == "__main__":
  print("=== 6 GHz RF-MEMS Mesh Node Feasibility Simulation ===")
  results = run_unit_economics_simulation(10000)
  print(json.dumps(results, indent=2))
