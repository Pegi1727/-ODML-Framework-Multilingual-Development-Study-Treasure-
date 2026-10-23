# Statistical Report — Reconstructed Study (reproduction_data.csv)

n = 500 time points (t = 0.0–2000 h)

## 1) Descriptive statistics
| Variable | n | Mean | SD | Min | Median | Max |
|---|---|---|---|---|---|---|
| SD | 500 | 0.6094 | 0.1977 | 0.4554 | 0.5157 | 1.2500 |
| TRI | 500 | 3.4873 | 1.1362 | 0.0000 | 4.0014 | 4.4448 |
| DFRI | 500 | 2.5244 | 0.6521 | 0.5000 | 2.8178 | 3.2000 |

## 2) Spearman correlation (DFRI vs TRI)
rho = 0.9690, p = 1.558e-304

## 3) Pearson correlation (DFRI vs TRI)
r = 0.9971, p = 0.000e+00

## 4) Saturation-hour estimates
- (a) First hour with SD ≤ 0.4713: **1450.9 h** (consistent with the 1450 h note)
- (b) First hour with |ΔSD| < 0.001 between consecutive steps: **837.7 h** (discrete criterion)
- (c) First hour with SD within 1% of sigma_min: **1755.5 h** (sigma_min = 0.4554 at t = 2000 h)

## 5) OLS regression: TRI ~ DFRI
TRI = 1.7374·DFRI + -0.8987  (R² = 0.9943, slope SE = 0.0059, p < 1e-300)

## Methods
Spearman/Pearson via scipy.stats; OLS via scipy.stats.linregress; saturation hours read from the sorted time series.
