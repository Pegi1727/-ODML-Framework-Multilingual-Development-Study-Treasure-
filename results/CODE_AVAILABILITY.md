# Code Availability

All code required to reproduce the computational results is included.

## Scripts

| File | Purpose |
|---|---|
| `code/run_all.py` | **Recommended entry point.** Regenerates every output (data, 3 figures at 300 dpi, statistics) into a fresh `outputs/` folder and runs automatic verification: Spearman rho ≈ 0.969 (±0.002), saturation near 1450 h (first hour with SD <= 0.4713 within 1400–1500 h), SD asymptote = sigma_min = 0.45, TRI asymptote ≈ 4.5. Also writes SHA-256 checksums of all generated files. Exit code 0 only if all checks pass. |
| `code/reproduction_script.py` | Original standalone reproduction script implementing the three models (SD decay, TRI growth, synthetic DFRI with bisection-tuned noise, seed 42) and producing the same figures and `reproduction_data.csv`. |

Both scripts are deterministic: the only stochastic element (Gaussian noise
for DFRI) uses a fixed seed (`numpy.random.default_rng(42)`), so repeated
runs produce byte-identical CSV outputs and visually identical figures.

## Environment

- Python >= 3.9
- numpy, pandas, scipy, matplotlib (pinned versions in `REQUIREMENTS.txt`)
- No network access or external data is required.

## Runtime

The full run completes in under 10 seconds on a standard laptop.

## License note

The scripts are provided for peer-review verification purposes; reuse beyond
the review should follow the journal's code-sharing policy and cite the
manuscript.
