import numpy as np
from scipy.optimize import brentq


def solve_coverages(U, species, g=10, temperature=298.15):
    """
    Solve competitive surface coverages using a multicomponent Frumkin adsorption isotherm.

    Parameters
    ----------
    U : float
        Applied potential.
    species : list of dict
        Each species should have: name, dG0, n, activity.
    g : float
        Frumkin lateral interaction parameter.
    temperature : float
        Temperature in K.

    Returns
    -------
    dict
        Coverage of each species and free sites.
    """
    k_B = 8.617e-5  # eV/K
    beta = 1.0 / (k_B * temperature)

    def equation(theta_total):
        sum_terms = 0.0
        for sp in species:
            dG_U = sp["dG0"] + sp["n"] * U
            sum_terms += (
                np.exp(-dG_U * beta)
                * sp["activity"]
                * np.exp(-g * theta_total)
            )
        return theta_total - (1.0 - theta_total) * sum_terms

    try:
        theta_total = brentq(equation, 0.0, 1.0, xtol=1e-12)
    except ValueError:
        theta_total = 1.0 if equation(1.0) < 0 else 0.0

    theta_free = 1.0 - theta_total

    k_eff_values = []
    for sp in species:
        dG_U = sp["dG0"] + sp["n"] * U
        k_eff = (
            np.exp(-dG_U * beta)
            * sp["activity"]
            * np.exp(-g * theta_total)
        )
        k_eff_values.append(k_eff)

    sum_k = sum(k_eff_values)

    coverages = {"Free sites": theta_free}

    if sum_k > 0:
        for sp, k_eff in zip(species, k_eff_values):
            coverages[sp["name"]] = theta_total * (k_eff / sum_k)
    else:
        for sp in species:
            coverages[sp["name"]] = 0.0

    return coverages


def solve_potential_range(U_range, species, g=10, temperature=298.15):
    """
    Calculate coverages over a potential range.
    """
    results = {"Potential": list(U_range), "Free sites": []}

    for sp in species:
        results[sp["name"]] = []

    for U in U_range:
        coverage = solve_coverages(U, species, g=g, temperature=temperature)
        results["Free sites"].append(coverage["Free sites"])

        for sp in species:
            results[sp["name"]].append(coverage[sp["name"]])

    return results
