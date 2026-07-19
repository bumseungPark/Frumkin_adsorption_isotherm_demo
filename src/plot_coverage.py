import matplotlib.pyplot as plt


def plot_coverages(results, species, output_path=None):
    """
    Plot potential-dependent surface coverages.

    Parameters
    ----------
    results : dict
        Coverage results from solve_potential_range.
    species : list of dict
        Species information.
    output_path : str or None
        If provided, save the figure to this path.
    """
    U_range = results["Potential"]

    plt.figure(figsize=(8, 6), dpi=120)

    plt.plot(
        U_range,
        results["Free sites"],
        label="Free sites",
        linewidth=3,
    )

    for sp in species:
        plt.plot(
            U_range,
            results[sp["name"]],
            label=sp["name"],
            linewidth=3,
            alpha=0.85,
        )

    plt.xlabel("Potential (V)")
    plt.ylabel("Surface coverage")
    plt.xlim(min(U_range), max(U_range))
    plt.ylim(-0.05, 1.05)
    plt.legend(frameon=False)
    plt.tight_layout()

    if output_path is not None:
        plt.savefig(output_path, dpi=300)

    plt.show()
