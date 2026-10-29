import numpy as np
import matplotlib.pyplot as plt
import skrf as rf
from skrf.media import CPW

def simulate_cpwg_sparameters(freq_min=5.0, freq_max=7.5, points=501):
    freq = rf.Frequency(freq_min, freq_max, points, unit='ghz')
    cpw_line = CPW(
        frequency=freq,
        w=0.48e-3,
        s=0.22e-3,
        h=0.254e-3,
        ep_r=3.66,
        t=35e-6
    )
    line_20mm = cpw_line.line(20e-3, unit='m', name='RO4350B_CPWG')
    f_ghz = freq.f / 1e9
    s21_db_combined = line_20mm.s21.s_db.flatten() - (0.30 + 0.015 * (f_ghz - 5.0))
    s11_db_combined = -22.0 + 1.2 * (f_ghz - 5.0)

    fig, ax = plt.subplots(1, 2, figsize=(14, 5))
    ax[0].plot(f_ghz, s11_db_combined, color='red', linewidth=2, label='S11 Return Loss')
    ax[0].set_title("CPWG + MM5130 Return Loss (S11)")
    ax[0].set_xlabel("Frequency (GHz)")
    ax[0].set_ylabel("dB")
    ax[0].set_ylim(-30, 0)
    ax[0].grid(True, linestyle='--', alpha=0.7)
    ax[0].legend(loc='upper right')

    ax[1].plot(f_ghz, s21_db_combined, color='blue', linewidth=2, label='S21 Insertion Loss')
    ax[1].set_title("CPWG + MM5130 Total Insertion Loss (S21)")
    ax[1].set_xlabel("Frequency (GHz)")
    ax[1].set_ylabel("dB")
    ax[1].set_ylim(-1.0, 0.0)
    ax[1].grid(True, linestyle='--', alpha=0.7)
    ax[1].legend(loc='lower left')

    plt.suptitle("6.5 GHz Rogers RO4350B Substrate & MM5130 Switch Performance", fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()
