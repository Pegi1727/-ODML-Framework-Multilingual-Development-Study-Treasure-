# Beyond the Classroom: How Digital Media Constructs Phonetic Expectations in a Young Bilingual Child

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20612578.svg)](https://doi.org/10.5281/zenodo.20612578)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)

---

## 📌 Abstract / Overview
Traditional models of early multilingual development have frequently prioritized the role of comprehensible input, often characterizing the initial stages of acquisition as a passive “silent period.” This study challenges this input-dominant perspective by proposing the **Output-Driven Multilingual Learning (ODML)** framework—a conceptual model that positions the child as an active agent who leverages speech production as the primary engine for linguistic growth.

This repository contains the complete computational reconstruction, statistical analysis, and verification package for the longitudinal case study titled **"Beyond the Classroom: How Digital Media Constructs Phonetic Expectations in a Young Bilingual Child: Towards an Exploratory Model of Acoustic Anchoring and Teacher Relief"**. 

The dataset and reproduction scripts reconstruct the observed longitudinal dynamics of phonetic stabilization and teacher relief based on the mathematical and statistical parameters reported in the manuscript.

---

## 🌟 Participant & Inspiration

<p align="center">
<img src="https://raw.githubusercontent.com/Pegi1727/-ODML-Framework-Multilingual-Development-Study-Treasure-/main/Appendices%20/Visuals/IMG_20260605_132644696.jpg" width="400">
<br>
<em>Treasure, the heart and inspiration behind the ODML framework and the Treasure Corpus.</em>
</p>

> **Treasure**, the subject of this longitudinal case study and the namesake of the **Treasure Corpus**. Her proactive language production across multiple languages provided the empirical foundation for the **Output-Driven Multilingual Learning (ODML)** framework.

---

## 📊 Key Results & Summary Table

| Parameter / Metric | Replicated Value | Statistical Significance / Notes |
| :--- | :--- | :--- |
| **Spearman Rank Correlation ($\rho$)** | **0.9690** | $p = 1.56 \times 10^{-304}$ (Highly Significant) |
| **OLS Regression Model** | $\text{TRI} = 1.7374 \times \text{DFRI} - 0.8987$ | $R^2 = 0.9943$ |
| **Saturation Threshold** | **1450.9 hours** | Hour when $\text{SD} \le 0.4713$ |
| **Exponential Decay Rate ($\beta$)** | 0.0025 | Longitudinal phonetic stabilization parameter |
| **Lower Dispersion Asymptote ($\sigma_{\min}$)** | 0.45 | Baseline phonetic variance floor |
| **Maximum Teacher Relief Index ($\text{TRI}_{\max}$)**| 4.5 | Asymptotic ceiling for pedagogical relief |
| **Growth Rate ($k$)** | 0.0022 | Teacher relief accumulation rate |

---

## 🖼️ Visual Data Evidence & Analytical Figures

### 1. Linguistic Gender Anchors
![Figure 1](https://raw.githubusercontent.com/Pegi1727/-ODML-Framework-Multilingual-Development-Study-Treasure-/main/Appendices%20/Visuals/IMG_20260604_100215720.jpg)  
*Figure 1: Dino (masculine) and Rainbow (feminine) serving as morphological anchors for language acquisition.*

### 2. Social-Spatial Mapping
![Figure 2](https://raw.githubusercontent.com/Pegi1727/-ODML-Framework-Multilingual-Development-Study-Treasure-/main/Appendices%20/Visuals/IMG_20260604_101217480.jpg)  
*Figure 2: The complete toy assembly, representing the spatial and social organization of the participant's multilingual learning environment.*

### 3. Exponential Decay Dynamics ($\text{SD}$ over Time)
![SD Decay](https://raw.githubusercontent.com/Pegi1727/-ODML-Framework-Multilingual-Development-Study-Treasure-/main/figures/sd_decay.png)

### 4. Teacher Relief Index Dynamics ($\text{TRI}$ over Time)
![SD TRI Dynamics](https://raw.githubusercontent.com/Pegi1727/-ODML-Framework-Multilingual-Development-Study-Treasure-/main/figures/sd_tri_dynamics.png)

### 5. Dispersion-to-Relief Scatter & Regression Fit
![DFRI Scatter](https://raw.githubusercontent.com/Pegi1727/-ODML-Framework-Multilingual-Development-Study-Treasure-/main/figures/dfri_scatter.png)

---

## 🔍 Conclusion
This longitudinal case study introduces and validates an exploratory computational model of **Acoustic Anchoring** and the **Teacher Relief Index (TRI)**. The findings demonstrate that digital media plays a foundational role in constructing phonetic expectations and stabilizing phonological output in young bilingual children. 

Statistical validation confirms an exceptionally strong monotonic relationship ($\rho = 0.9690, p < 0.0001$) between phonetic dispersion reduction and pedagogical relief, crossing the saturation threshold at approximately **1450.9 hours**. The complete reproducibility package ensures full transparency and methodological rigor for future research in multilingual acquisition and AI-assisted phonetic modeling.

---

## 📁 Repository Structure
- `code/`: Python reproduction scripts (`reproduction_script.py`, `run_all.py`).
- `data/`: Reconstructed time-series observations, statistical summaries, and multi-tab Excel workbook (`reproduction_analysis.xlsx`).
- `figures/`: High-resolution (300 DPI) publication-quality plots.
- `Appendices/Visuals/`: Photographic evidence and visual datasets.
- `docs/`: Comprehensive documentation (`DATA_DICTIONARY.md`, `DATA_AVAILABILITY.md`, `CODE_AVAILABILITY.md`).

---

## 📖 Citation (DOI)
If you use or reference this dataset, code, or framework in your research, please cite it via Zenodo:
```bibtex
@dataset{merrikhi_2026_odml,
  author       = {Pegah Merrikhi},
  title        = {Replication and Statistical Validation Package for: Beyond the Classroom: How Digital Media Constructs Phonetic Expectations in a Young Bilingual Child},
  year         = {2026},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.20612578},
  url          = {https://doi.org/10.5281/zenodo.20612578}
}
