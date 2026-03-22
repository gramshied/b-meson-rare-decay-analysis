"""
Load LHCb charm dataset and inspect available branches.

Physics meaning of key variables:

Lc_M:
    Invariant mass of Λc+ reconstructed from pKπ.
    Should peak at 2286.5 MeV for true Λc+.

Lc_PT:
    Transverse momentum of Λc+.
    Higher PT often indicates production from heavy hadron decay.

Lc_IPCHI2:
    Impact parameter χ² with respect to primary vertex.
    Small → prompt production (cc̄)
    Large → from B decay (displaced)

Lc_FDCHI2:
    Flight distance χ².
    Measures how far Λc+ traveled before decaying.

p_PROBNNp:
    Neural network probability that a track is a proton.
    Critical for Λc+ → pKπ reconstruction.

p_PROBNNk:
    Probability proton track is actually a kaon (mis-ID).

K_PROBNNk:
    Kaon identification probability.

pi_PROBNNpi:
    Pion identification probability.

Lc_ENDVERTEX_CHI2:
    Quality of reconstructed decay vertex.
    Lower = better vertex fit.
"""

import uproot
import pandas as pd


def load_root_file(file_path):
    print(f"Opening file: {file_path}")

    file = uproot.open(file_path)

    print("\nAvailable keys:")
    for key in file.keys():
        print(key)

    # Try common tree names
    tree_name = None
    for key in file.keys():
        if "DecayTree" in key or "tree" in key.lower():
            tree_name = key
            break

    if tree_name is None:
        print("\nNo suitable tree found.")
        return None

    print(f"\nUsing tree: {tree_name}")

    tree = file[tree_name]

    branches = tree.keys()

    print("\nBranches:")
    for b in branches:
        print(b)

    # Convert a small sample to pandas for inspection
    df = tree.arrays(branches[:50], library="pd")

    print("\nSample data:")
    print(df.head())

    # Check for Λc variables
    lc_vars = [b for b in branches if "Lc" in b or "Lc_" in b]

    if len(lc_vars) == 0:
        print("\n⚠️ No Λc+ variables found in dataset.")
        print("Switch to MC generation mode (Step 1e).")
    else:
        print("\nFound Λc-related variables:")
        for v in lc_vars:
            print(v)

    return df


if __name__ == "__main__":
    load_root_file("D:/b_meson_analysis/charm_baryon_analysis/data/B2HHH_MagnetDown.root")