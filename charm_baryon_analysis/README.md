# Charm Baryon Tagging: Λc⁺ Reconstruction, Dalitz Analysis, and FEI Extension Prototype

## Overview

This project develops a complete analysis pipeline for charm baryon reconstruction and tagging, motivated by the extension of the Full Event Interpretation (FEI) algorithm at Belle II to include baryonic decay modes.

The study focuses on Λc⁺ → pK⁻π⁺ reconstruction, Dalitz plot analysis, partial reconstruction of B → Λc⁺ + X decays using the missing mass technique, and the development of a machine learning-based charm baryon tagger.

This work builds directly on a previous B-meson rare decay analysis using LHCb open data and extends it to baryonic final states relevant for Belle II physics.

---

## Physics Motivation

Charm baryon decays provide a unique probe of heavy flavor dynamics and contribute significantly (~6%) to B-meson decay channels. However, baryonic B decays are experimentally challenging due to multi-body final states and partial reconstruction.

The Belle II Full Event Interpretation (FEI) currently focuses on mesonic decay channels. Extending FEI to include B → Λc⁺ X modes can improve tagging efficiency and enhance the sensitivity of many precision measurements.

This project demonstrates a prototype workflow for such an extension, including reconstruction, background suppression, and tagging.

---

## Analysis Pipeline

```
MC / Open Data
        ↓
PID Preselection (proton identification)
        ↓
Λc⁺ Mass Fit (Crystal Ball + Chebyshev)
        ↓
Dalitz Analysis (m²(pK), m²(Kπ))
        ↓
sPlot Background Subtraction
        ↓
B → Λc⁺ X Reconstruction (Missing Mass)
        ↓
Charm Baryon Tagger (XGBoost BDT)
        ↓
Tagging Efficiency & Impact Estimate
```

---

## Key Results

* Λc⁺ mass reconstruction:

  * Crystal Ball fit with peak near 2286 MeV
  * Signal yield extracted from unbinned maximum likelihood fit

* Dalitz analysis:

  * Phase-space distribution reproduced
  * sWeighted Dalitz plot isolates signal structure

* Missing mass reconstruction:

  * Demonstrates partial reconstruction of B → Λc⁺ X
  * Clear separation between signal-like and combinatorial background

* Charm baryon tagger:

  * AUC ~ 0.7–0.9 (depending on training sample)
  * Key discriminating features:

    * log(IPχ²)
    * log(FDχ²)
    * pT ratio

* Tagging performance:

  * Tagging efficiency: O(50–70%)
  * Significant rejection of prompt Λc⁺ background

* Estimated impact:

  * Additional tagging contribution from baryonic modes
  * Potential improvement over baseline FEI efficiency

---

## Technical Skills Demonstrated

* 3-body invariant mass reconstruction (Λc⁺ → pK⁻π⁺)
* Crystal Ball fitting with unbinned maximum likelihood (iminuit)
* Dalitz plot analysis and kinematic boundary construction
* sPlot / sWeights for background subtraction
* Proton particle identification (PROBNNp-based selection)
* Missing mass reconstruction for partial decay chains
* Machine learning (XGBoost) for charm baryon tagging
* Feature engineering based on detector and decay physics
* Tagging efficiency measurement and optimization
* Modular HEP analysis workflow (multi-notebook pipeline)

---

## Connection to Belle II FEI

The Full Event Interpretation (FEI) reconstructs tag-side B mesons using multivariate classifiers trained on exclusive decay channels.

This project extends that concept by:

* Introducing Λc⁺ → pK⁻π⁺ as a tagging candidate
* Developing a classifier to distinguish B-origin Λc⁺ from prompt production
* Estimating the gain in tagging efficiency from baryonic modes

This directly aligns with ongoing efforts to improve FEI performance at Belle II.

---

## How to Run

From the repository root:

```
cd charm_baryon_analysis

# Activate environment
venv\Scripts\activate

# Install requirements
pip install -r requirements_charm.txt
```

Run notebooks in order:

1. `01_pid_preselection.ipynb`
2. `02_Lc_mass_fit.ipynb`
3. `03_dalitz_analysis.ipynb`
4. `04_B_to_Lc_chain.ipynb`
5. `05_charm_baryon_tagger.ipynb`

---

## Data

This project uses:

* CERN Open Data (LHCb datasets)
* Synthetic Monte Carlo for Λc⁺ reconstruction and decay modeling

Data files are not included due to size.
Download from: https://opendata.cern.ch

---

## References

* Belle Λc⁺ branching fraction measurement: arXiv:1312.7826
* Belle Ξc measurements: arXiv:1811.09738, arXiv:1904.12093
* Full Event Interpretation (FEI): arXiv:1807.08680
* sPlot method: Pivk & Le Diberder, NIM A555 (2005) 356
* CERN Open Data Portal

---

## Author

Gramshi E D
MSc Physics - Nuclear / Particle Physics
Experience: CERN ROOT, detector analysis (BARC), machine learning in HEP
