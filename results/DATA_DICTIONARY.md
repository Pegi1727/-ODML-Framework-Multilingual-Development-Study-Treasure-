# Data Dictionary

## 1. `data/reproduction_data.csv` and `data/time_series_renamed.csv`

Both files contain the same N = 500 rows (one per simulated time step,
t = 0 to 2000 h, evenly spaced at ~4.008 h). `time_series_renamed.csv` uses
human-readable column names.

### `t_hours` / `Time_Hours`
- **Description:** cumulative exposure time since intervention start.
- **Units:** hours. **Type:** float.
- **Range:** 0.0 – 2000.0 (step ≈ 4.008).
- **Generation:** `numpy.linspace(0, 2000, 500)` in `code/reproduction_script.py`.

### `SD` / `Phonetic_Dispersion_SD`
- **Description:** Phonetic Dispersion Index — within-group phonetic
  dispersion (standard-deviation scale).
- **Units:** sigma (σ) units, dimensionless index. **Type:** float.
- **Range:** 0.4554 – 1.2500 (theoretical floor sigma_min = 0.45, baseline
  sigma_0 = 1.25).
- **Generation:** exponential decay model
  `SD(t) = 0.45 + (1.25 - 0.45) * exp(-0.0025 * t)` (Appendix C, Eq. 1).
  Deterministic — no noise.

### `TRI` / `Teacher_Relief_TRI`
- **Description:** Teacher Relief Index — aggregate reduction of teacher
  burden attributable to digital phonetic reinforcement.
- **Units:** index points (0 = no relief). **Type:** float.
- **Range:** 0.0 – 4.4448 (asymptote TRI_max = 4.5).
- **Generation:** asymptotic growth model
  `TRI(t) = 4.5 * (1 - exp(-0.0022 * t))` (Appendix C, Eq. 2).
  Deterministic — no noise.

### `DFRI`
- **Description:** Digital Phonetic Reinforcement Index — synthetic index of
  digital-tool reinforcement intensity, generated to exhibit the reported
  rank correlation with TRI.
- **Units:** index points. **Type:** float.
- **Range:** 0.5 – 3.2.
- **Generation:** `base = TRI / TRI.max()` plus Gaussian noise
  (seed 42, `numpy.random.default_rng`), with the noise amplitude chosen by
  bisection so that Spearman rho(DFRI, TRI) = 0.969; then min–max rescaled to
  [0.5, 3.2] (Table E2 of the manuscript).

## 2. `data/statistical_summary.csv`

Long-format table of summary statistics with columns:
`category` (Descriptive / Spearman / Pearson / Saturation / OLS),
`term` (variable or model), `statistic` (e.g., mean, rho, hour, slope),
`value` (numeric result). Derived in `statistical_report.md` /
`reproduction_analysis.xlsx` from `reproduction_data.csv`.

## 3. `data/reproduction_analysis.xlsx`

Workbook version of the analysis: data series, descriptive statistics,
correlation and regression results, and saturation-hour estimates.
