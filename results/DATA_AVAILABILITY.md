# Data Availability Statement

**Transparency statement.** The raw observational logs underlying the
manuscript (classroom recordings, transcription-derived dispersion
measurements, and teacher-burden surveys) are **not included** in this
package. They contain potentially identifying information about participants
and are subject to the confidentiality terms of the study's ethics approval.

Instead, this package provides a **reconstructed, model-consistent time
series** (`data/reproduction_data.csv`, `data/time_series_renamed.csv`)
generated analytically from the parameters reported in the manuscript
appendices (sigma_min = 0.45, beta = 0.0025, TRI_max = 4.5, k = 0.0022,
sigma_0 = 1.25; seed 42 for the noise term in DFRI).

**Intended use.** The reconstructed dataset is provided *solely for the
verification of computations and figures*: reviewers can confirm the
descriptive statistics, the Spearman rho = 0.969 between DFRI and TRI, the
OLS regression (TRI ~ DFRI), and the saturation of the dispersion curve at
approximately 1450 h (SD <= 0.4713).

**Limitation.** Because the series are model-generated, they carry no
measurement noise (except the controlled DFRI noise term) and must not be
used for meta-analysis, re-estimation of the model parameters as if they
were empirical data, or any secondary empirical research.
