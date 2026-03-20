"""
load_data.py

Purpose:
--------
Load LHCb open data ROOT files using uproot, inspect structure,
and convert to a pandas DataFrame for analysis.

Physics Context:
----------------
This dataset contains reconstructed B meson decay candidates.
We are interested in kinematic and topological variables that help
separate real B decays (signal) from combinatorial background.
"""

import uproot
import pandas as pd
import os


def load_root_file(file_path, tree_name="DecayTree"):
    """
    Load ROOT file and return pandas DataFrame.

    Parameters
    ----------
    file_path : str
        Path to ROOT file
    tree_name : str
        Name of the TTree inside ROOT file

    Returns
    -------
    df : pandas.DataFrame
    """
    with uproot.open(file_path) as file:
        tree = file[tree_name]

        # Print all branches
        print("\nAvailable branches:\n")
        for branch in tree.keys():
            print(branch)

        # Convert to pandas DataFrame
        df = tree.arrays(library="pd")

    return df


def save_branch_summary(df, output_path):
    """
    Save summary statistics of branches.

    Parameters
    ----------
    df : pandas.DataFrame
    output_path : str
    """
    summary = df.describe(include="all")
    summary.to_csv(output_path)
    print(f"\nBranch summary saved to: {output_path}")


def explain_physics_variables():
    """
    Key physics variables:

    B_M:
        Invariant mass of the reconstructed B meson candidate (MeV/c^2).
        Signal appears as a peak near the true B mass (~5279 MeV).

    B_PT:
        Transverse momentum of the B candidate (MeV/c).
        High PT typically indicates real heavy particle decays.

    B_IPCHI2_OWNPV:
        Impact parameter chi-square relative to the primary vertex.
        Large values → particle is displaced → likely from B decay.

    B_FDCHI2_OWNPV:
        Flight distance chi-square from the primary vertex.
        Measures how significantly the decay vertex is separated.

    B_DIRA_OWNPV:
        Cosine of angle between B momentum and line from PV to decay vertex.
        Close to 1 → B points back to the PV (good candidate).

    h1_PROBNN*, h2_PROBNN*:
        Particle ID probabilities from neural networks.
        Example:
            PROBNNK → probability particle is a kaon
            PROBNNpi → probability particle is a pion
        Useful for separating decay modes.
    """
    pass


if __name__ == "__main__":

    data_path = "D:/b_meson_analysis/data/B2HHH_MagnetDown.root"  # adjust if needed

    if not os.path.exists(data_path):
        print(f"File not found: {data_path}")
        exit()

    df = load_root_file(data_path)

    print("\nFirst 5 rows:\n")
    print(df.head())

    os.makedirs("../results", exist_ok=True)
    save_branch_summary(df, "D:/b_meson_analysis/results/branch_summary.csv")