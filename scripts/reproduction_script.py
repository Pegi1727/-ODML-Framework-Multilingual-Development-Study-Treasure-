"""
Reproduction script — Computational models specified in the document appendices.

Models (Appendix C & Table E1):
  1. Phonetic Dispersion Model (exponential decay):
        SD(t)  = sigma_min + (sigma_0 - sigma_min) * exp(-beta * t)
        sigma_min = 0.45, beta = 0.0025, sigma_0 = 1.25 (derived baseline)
  2. Teacher Relief Model (asymptotic growth):
        TRI(t) = TRI_max * (1 - exp(-k * t))
        TRI_max = 4.5, k = 0.0022
  3. Synthetic DFRI with Spearman rho = 0.969 (p < 0.0001) vs TRI — Table E2.
Sampling: N = 500 steps over 2000 exposure hours (Appendix C).
Saturation (Appendix C / Table E3): |Delta SD| < 0.001 between consecutive
steps (criterion point), plus the document-reported ~1450 h (Table E3).

Outputs (300 dpi PNG): sd_decay.png, sd_tri_dynamics.png, dfri_scatter.png
Plus reproduction_data.csv with all N = 500 simulated points.
"""

import os
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ------------------------------------------------------------------ models
N, HOURS = 500, 2000.0
t = np.linspace(0, HOURS, N)
SIGMA_0, SIGMA_MIN, BETA = 1.25, 0.45, 0.0025
TRI_MAX, K = 4.5, 0.0022
SAT_THRESHOLD = 0.001
TARGET_RHO = 0.969

sd = SIGMA_MIN + (SIGMA_0 - SIGMA_MIN) * np.exp(-BETA * t)   # Eq. 1
tri = TRI_MAX * (1.0 - np.exp(-K * t))                        # Eq. 2

# ------------------------------------------- saturation (|Delta SD| < 0.001)
deltas = np.abs(np.diff(sd))
sat_idx = int(np.argmax(deltas < SAT_THRESHOLD))
sat_hour = t[sat_idx]
print(f"Saturation criterion (|ΔSD| < {SAT_THRESHOLD}): t = {sat_hour:.1f} h, "
      f"SD = {sd[sat_idx]:.4f}")
print("Document-reported saturation (Table E3): ~1450 h "
      f"(SD at 1450 h = {np.interp(1450, t, sd):.4f})")

# ------------------ synthetic DFRI: bisection on noise to hit rho = 0.969
rng = np.random.default_rng(42)
base = tri / tri.max()
noise = rng.normal(0, 1, N)
lo, hi = 0.0, 1.0
rho = 1.0
for _ in range(60):
    a = (lo + hi) / 2
    rho, p = stats.spearmanr(base + a * noise, tri)
    if rho > TARGET_RHO:
        lo = a
    else:
        hi = a
dfri = base + a * noise
dfri = (dfri - dfri.min()) / (dfri.max() - dfri.min()) * (TRI_MAX * 0.6) + 0.5
rho, pval = stats.spearmanr(dfri, tri)
print(f"Spearman rho(DFRI, TRI) = {rho:.3f}, p = {pval:.2e}")

pd.DataFrame({"t_hours": t, "SD": sd, "TRI": tri, "DFRI": dfri}).to_csv(
    "/mnt/data/reproduction_data.csv", index=False)

# ------------------------------------------------------------------ plots
plt.rcParams.update({
    "font.family": "DejaVu Sans", "axes.spines.top": False,
    "axes.spines.right": False, "axes.grid": True, "grid.alpha": 0.3,
    "savefig.dpi": 300, "savefig.bbox": "tight"})

# --- Figure 1: sd_decay.png -------------------------------------------
fig, ax = plt.subplots(figsize=(7.5, 4.8))
ax.plot(t, sd, color="#1f77b4", lw=2.5,
        label=r"$SD(t)=\sigma_{min}+(\sigma_0-\sigma_{min})e^{-\beta t}$")
ax.axvline(1450, color="crimson", ls="--", lw=1.4, alpha=0.7,
           label="Saturation ≈ 1450 h (Table E3)")
ax.scatter([1450], [np.interp(1450, t, sd)], color="crimson", s=60, zorder=5)
ax.axvline(sat_hour, color="darkorange", ls=":", lw=1.4, alpha=0.8,
           label=f"|ΔSD| < {SAT_THRESHOLD} criterion → {sat_hour:.0f} h")
ax.set_xlabel("Cumulative exposure (hours)")
ax.set_ylabel("Phonetic Dispersion, SD (σ)")
ax.set_title("Exponential Decay of Phonetic Dispersion")
ax.set_xlim(0, HOURS); ax.set_ylim(0.4, 1.3)
ax.legend(frameon=False, loc="upper right", fontsize=9)
fig.savefig("/mnt/data/sd_decay.png"); plt.close(fig)

# --- Figure 2: sd_tri_dynamics.png ------------------------------------
fig, ax1 = plt.subplots(figsize=(7.5, 4.8))
ax1.plot(t, sd, color="#1f77b4", lw=2.5, label="SD (dispersion)")
ax1.set_xlabel("Cumulative exposure (hours)")
ax1.set_ylabel("Phonetic Dispersion, SD (σ)", color="#1f77b4")
ax1.tick_params(axis="y", labelcolor="#1f77b4"); ax1.set_xlim(0, HOURS)
ax2 = ax1.twinx()
ax2.plot(t, tri, color="#d62728", lw=2.5, ls="--", label="TRI (relief)")
ax2.set_ylabel("Teacher Relief Index, TRI", color="#d62728")
ax2.tick_params(axis="y", labelcolor="#d62728")
ax2.spines["right"].set_visible(True); ax2.set_ylim(0, TRI_MAX * 1.05)
lines = ax1.get_lines() + ax2.get_lines()
ax1.legend(lines, [l.get_label() for l in lines], frameon=False,
           loc="center right")
ax1.set_title("Dynamic Interaction Between SD and TRI")
fig.savefig("/mnt/data/sd_tri_dynamics.png"); plt.close(fig)

# --- Figure 3: dfri_scatter.png ---------------------------------------
slope, intercept = np.polyfit(dfri, tri, 1)
xs = np.linspace(dfri.min(), dfri.max(), 100)
fig, ax = plt.subplots(figsize=(6.8, 5.2))
ax.scatter(dfri, tri, s=18, alpha=0.55, color="#2ca02c", edgecolors="none",
           label=f"N = {N}")
ax.plot(xs, slope * xs + intercept, color="black", lw=2, label="Trendline (OLS)")
ax.set_xlabel("Digital Phonetic Reinforcement Index (DFRI)")
ax.set_ylabel("Teacher Relief Index (TRI)")
ax.set_title(f"Spearman ρ = {rho:.3f}  (p < 0.0001)")
ax.legend(frameon=False, loc="lower right")
fig.savefig("/mnt/data/dfri_scatter.png"); plt.close(fig)

# ------------------------------------------------------------ verification
for f in ["sd_decay.png", "sd_tri_dynamics.png", "dfri_scatter.png"]:
    p = f"/mnt/data/{f}"
    ok = os.path.exists(p) and os.path.getsize(p) > 10000
    print(f"{f}: {'OK' if ok else 'MISSING'} ({os.path.getsize(p):,} bytes)")

print(f"\nSD(0)={sd[0]:.4f}  SD(2000)={sd[-1]:.4f}  "
      f"TRI(0)={tri[0]:.4f}  TRI(2000)={tri[-1]:.4f}")
