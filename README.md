# Competitive Frumkin Adsorption Isotherm Modeling Demo

This repository demonstrates a simplified Python workflow for calculating competitive surface coverages using a multicomponent Frumkin adsorption isotherm model.

The code structure was developed during my M.S. research on electrocatalyst surface poisoning in high-temperature polymer electrolyte membrane fuel cells. To avoid disclosure of unpublished research data, this public version uses simplified example parameters and demonstration outputs.

This model accounts for lateral adsorbate–adsorbate interactions (Frumkin parameter g) and potential-dependent adsorption free energies, enabling quantitative comparison of surface site availability across different catalyst interfaces.

## Repository Structure

```text
📁frumkin-adsorption-isotherm-demo/
├── README.md
├── requirements.txt
├── 📁src
│     ├── solver.py
│     └── plot_coverage.py
├── 📁examples
│      └── run_demo.py
└── 📁outputs
       └── demo_coverage_plot.png
