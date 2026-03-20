# Search for a Rare B-Meson Decay

### MVA-based Signal-Background Discrimination and CLs Upper Limit Estimation using LHCb Open Data

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![CERN Open Data](https://img.shields.io/badge/Data-CERN%20Open%20Data-orange)
![HEP Analysis](https://img.shields.io/badge/Field-High%20Energy%20Physics-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## Physics Motivation

Rare decays of B mesons provide a powerful probe of physics beyond the Standard Model (BSM). Processes such as lepton flavor-violating decays (e.g., ( B \to \tau \ell X )) are highly suppressed in the Standard Model but can be enhanced in new physics scenarios.

This project implements a realistic High Energy Physics (HEP) analysis pipeline using LHCb open data, culminating in a statistical upper limit on a signal yield and branching fraction using the CLs method. The workflow closely mirrors analyses performed at experiments such as Belle II and LHCb.

---

## Analysis Pipeline

```text
CERN Open Data (ROOT)
        ↓
Data Loading (uproot, pandas)
        ↓
Exploratory Data Analysis + Blinding
        ↓
Feature Engineering (HEP-inspired variables)
        ↓
BDT Training (XGBoost)
        ↓
Selection Optimization (Punzi Figure of Merit)
        ↓
Invariant Mass Fit (iminuit, extended likelihood)
        ↓
CLs Hypothesis Testing (toy Monte Carlo)
        ↓
Upper Limit on Signal Yield and Branching Fraction
```

---

## Key Results

* BDT Performance (AUC): ~0.62 (data-driven signal proxy)
* Selection optimized using Punzi figure of merit
* Mass fit model: Gaussian (signal) + exponential (background)
* Fit outcome: no statistically significant signal observed
* Statistical method: CLs (toy Monte Carlo implementation)

The CLs curve remains near unity across the scanned range, indicating no sensitivity to exclude signal hypotheses with the current dataset and selection.

---

## Technical Skills Demonstrated

* HEP data analysis using uproot and pandas
* Boosted Decision Trees (XGBoost) for signal/background discrimination
* Feature engineering based on detector-level observables
* Punzi figure of merit for rare decay optimization
* Unbinned extended maximum likelihood fitting with iminuit
* CLs hypothesis testing implemented from first principles
* Toy Monte Carlo simulation for statistical inference
* Scientific visualization using mplhep
* Reproducible and modular analysis workflow

---

## How to Run

### Clone repository

```bash
git clone <your-repo-url>
cd b_meson_analysis
```

### Create environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

### Run analysis (in order)

```bash
notebooks/01_exploratory_analysis.ipynb
notebooks/02_bdt_training.ipynb
notebooks/03_punzi_optimization.ipynb
notebooks/04_mass_fit.ipynb
notebooks/05_upper_limit.ipynb
```

---

## Project Structure

```text
b_meson_analysis/
├── data/              
├── notebooks/         
├── src/               
├── plots/             
├── results/           
├── requirements.txt
└── README.md
```

---

## References

* CERN Open Data Portal (Record 4900)
* G. Punzi, *Sensitivity of searches for new signals*, physics/0308063 (2003)
* A.L. Read, *Presentation of search results: the CLs technique*, J. Phys. G 28 (2002) 2693
* Belle II Physics Book, arXiv:1808.10567
* LHCb Collaboration public datasets and documentation

---

## Summary

This project implements a complete end-to-end HEP analysis pipeline, from raw detector data to statistical inference. It demonstrates practical experience with machine learning in particle physics, likelihood-based signal extraction, and modern statistical techniques used in collider experiments.

While no signal was observed, the methodology and workflow are directly transferable to real analyses at Belle II and LHCb.

---

## Author

Gramshi E D
MSc Physics - University of Kerala
Research interests: High Energy Physics, Machine Learning, Physics Beyond the Standard Model
