from pathlib import Path
import sys
import numpy as np

# Project root = parent folder of examples/
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Allow importing from src/
sys.path.append(str(PROJECT_ROOT))

from src.solver import solve_potential_range
from src.plot_coverage import plot_coverages


def main():
    # Simplified example parameters.
    # These values are demonstration-only and do not contain unpublished research data.
    species = [
        {
            "name": "Adsorbate A",
            "dG0": 0.20,
            "n": 0.0,
            "activity": 0.10,
        },
        {
            "name": "Adsorbate B",
            "dG0": 0.45,
            "n": -1.0,
            "activity": 0.10,
        },
        {
            "name": "Intermediate C",
            "dG0": 0.70,
            "n": -1.0,
            "activity": 1.00,
        },
    ]

    U_range = np.linspace(0.0, 1.2, 200)
    g = 10

    results = solve_potential_range(U_range, species, g=g)

    output_dir = PROJECT_ROOT / "outputs"
    output_dir.mkdir(exist_ok=True)

    output_path = output_dir / "demo_coverage_plot.png"

    plot_coverages(
        results=results,
        species=species,
        output_path=str(output_path),
    )

    print("Coverage values at selected potentials:")
    for U in [1.2, 1.0, 0.8, 0.6, 0.4, 0.2, 0.0]:
        idx = np.argmin(np.abs(U_range - U))
        print(
            f"U = {U_range[idx]:.2f} V | "
            f"Free sites = {results['Free sites'][idx]:.4f}"
        )

    print(f"\nDemo plot saved to: {output_path}")


if __name__ == "__main__":
    main()