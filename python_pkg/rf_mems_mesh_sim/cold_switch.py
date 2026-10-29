import numpy as np
import matplotlib.pyplot as plt

def simulate_cold_switching(rf_power_start_dbm=24.0, target_time_us=10.0):
    t = np.linspace(0, 20, 1000)
    rf_mute_start = 2.0
    tau_rf = 0.35

    rf_power_dBm = np.where(
        t < rf_mute_start,
        rf_power_start_dbm,
        -30.0 + (rf_power_start_dbm - (-30.0)) * np.exp(-(t - rf_mute_start) / tau_rf)
    )

    v_gate_start = 2.8
    tau_gate = 1.1

    v_gate = np.where(
        t < v_gate_start,
        0.0,
        88.0 * (1.0 - np.exp(-(t - v_gate_start) / tau_gate))
    )

    fig, ax1 = plt.subplots(figsize=(12, 5))
    color = 'tab:red'
    ax1.set_xlabel('Time (microseconds)')
    ax1.set_ylabel('RF Input Power (dBm)', color=color)
    ax1.plot(t, rf_power_dBm, color=color, linewidth=2.5, label='RF Power Envelope')
    ax1.axhline(y=7.0, color='darkred', linestyle='--', linewidth=1.5, label='Hot-Switch Safety Threshold (+7 dBm)')
    ax1.set_ylim(-35, 30)
    ax1.grid(True, linestyle='--', alpha=0.5)

    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('MM101 Gate Voltage (V)', color=color)
    ax2.plot(t, v_gate, color=color, linewidth=2.5, linestyle='-.', label='HV Gate Bias (88V)')
    ax2.set_ylim(-5, 100)

    plt.title(f"MM5130 Cold-Switching Sequence (<{target_time_us} µs Settling Window)", fontsize=13, fontweight='bold')
    fig.tight_layout()
    plt.show()
