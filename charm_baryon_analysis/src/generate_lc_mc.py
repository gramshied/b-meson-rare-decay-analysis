import numpy as np
import pandas as pd

np.random.seed(42)

N = 200000
N_sig = 100000
N_bkg = 100000

# Constants (MeV)
M_Lc = 2286.5
mp = 938.3
mK = 493.7
mpi = 139.6


# -----------------------
# SIGNAL
# -----------------------
sig = pd.DataFrame()

sig["Lc_M"] = np.random.normal(2286.5, 5.0, N_sig)
sig["Lc_PT"] = np.random.exponential(3000, N_sig)
sig["log_IPCHI2"] = np.random.normal(-1.0, 0.8, N_sig)
sig["log_FDCHI2"] = np.random.normal(2.5, 0.5, N_sig)

sig["p_PROBNNp"] = np.random.beta(8, 2, N_sig)
sig["K_PROBNNk"] = np.random.beta(7, 2, N_sig)
sig["pi_PROBNNpi"] = np.random.beta(7, 2, N_sig)

sig["Lc_ENDVERTEX_CHI2"] = np.random.chisquare(1, N_sig)

# Dalitz variables
sig["m2_pK"] = np.random.uniform(1.5e6, 6.5e6, N_sig)
sig["m2_Kpi"] = np.random.uniform(0.3e6, 3.0e6, N_sig)

sig["label"] = 1


# -----------------------
# BACKGROUND
# -----------------------
bkg = pd.DataFrame()

bkg["Lc_M"] = np.random.uniform(2150, 2450, N_bkg)
bkg["Lc_PT"] = np.random.exponential(2000, N_bkg)
bkg["log_IPCHI2"] = np.random.uniform(-2, 3, N_bkg)
bkg["log_FDCHI2"] = np.random.uniform(0, 4, N_bkg)

bkg["p_PROBNNp"] = np.random.beta(2, 5, N_bkg)
bkg["K_PROBNNk"] = np.random.beta(2, 5, N_bkg)
bkg["pi_PROBNNpi"] = np.random.beta(2, 5, N_bkg)

bkg["Lc_ENDVERTEX_CHI2"] = np.random.uniform(0, 10, N_bkg)

bkg["m2_pK"] = np.random.uniform(1.5e6, 6.5e6, N_bkg)
bkg["m2_Kpi"] = np.random.uniform(0.3e6, 3.0e6, N_bkg)

bkg["label"] = 0


# -----------------------
# COMBINE
# -----------------------
df = pd.concat([sig, bkg], ignore_index=True)

df.to_csv("D:/b_meson_analysis/charm_baryon_analysis/data/lc_candidates.csv", index=False)

print("Generated MC dataset saved to data/lc_candidates.csv")
print(df.head())