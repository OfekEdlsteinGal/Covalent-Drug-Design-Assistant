# Warhead Screener for Covalent Inhibitors

> **Important:** This README describes a work-in-progress Python course project and may change during implementation.

## Summary

Warhead Screener for Covalent Inhibitors is a Python-based cheminformatics tool for screening small-molecule libraries and identifying compounds that contain covalent inhibitor warheads.

The tool will read molecular libraries from SMILES files, detect selected covalent warheads using SMARTS substructure matching, calculate basic drug-likeness descriptors, rank candidate molecules, and export the results as structured tables and summary plots.

The goal is to automate an early-stage medicinal chemistry workflow that is usually done manually: checking whether molecules contain electrophilic functional groups that may react covalently with amino acid residues such as cysteine, lysine, serine, or tyrosine.

---

## Motivation

Covalent inhibitors are an important class of molecules in modern drug discovery. They contain reactive functional groups, known as **warheads**, that can form covalent bonds with residues in target proteins. Examples include acrylamides, chloroacetamides, vinyl sulfones, sulfonyl fluorides, aldehydes, epoxides, and boronic acids.

In medicinal chemistry, researchers may need to screen many compounds and ask:

- Which molecules contain a covalent warhead?
- What type of warhead is present?
- Are the molecules reasonably drug-like?
- Which compounds should be prioritized for further analysis?

Doing this manually is time-consuming and error-prone. This project aims to make the process faster, reproducible, and easier to document.

---

## What Does This Project Do?

The project will:

1. Read a molecular library from a `.smi` file.
2. Convert SMILES strings into RDKit molecule objects.
3. Search each molecule for predefined covalent warhead motifs using SMARTS patterns.
4. Calculate basic molecular descriptors:
   - Molecular Weight
   - LogP
   - Hydrogen Bond Donors
   - Hydrogen Bond Acceptors
   - Topological Polar Surface Area
   - Number of Rotatable Bonds
5. Check basic Lipinski Rule of Five violations.
6. Assign a simple priority score.
7. Export the ranked results to a CSV file.
8. Generate summary plots, such as molecular weight distribution and warhead frequency.

---

## Initially Supported Warheads

The first implementation will support a small curated set of warhead patterns:

- Acrylamide
- Chloroacetamide
- Vinyl sulfone
- Sulfonyl fluoride
- Aldehyde
- Epoxide
- Boronic acid

Additional warheads can be added later by editing the SMARTS pattern file.

---

## Example Input

The expected input is a `.smi` file with one molecule per line:

```text
C=CC(=O)NC1=CC=CC=C1 acrylamide_example
ClCC(=O)NC1=CC=CC=C1 chloroacetamide_example
O=S(=O)(F)C1=CC=CC=C1 sulfonyl_fluoride_example
```

Each line contains:

```text
SMILES molecule_id
```

---

## Expected Output

The program will generate a CSV table containing one row per molecule.

Example columns:

| Molecule ID | SMILES | Warheads | MW | LogP | HBD | HBA | TPSA | Rotatable Bonds | Lipinski Violations | Score |
|------------|--------|----------|----|------|-----|-----|------|-----------------|---------------------|-------|

Example output:

```text
Molecule: acrylamide_example
Warhead: Acrylamide
MW: 147.18
LogP: 1.72
Lipinski Violations: 0
Priority Score: 90
```

The program will also save summary plots as PNG files.

---

## Technical Approach

The project will be implemented in Python using RDKit for cheminformatics.

Main steps:

1. Load input molecules from a SMILES file.
2. Validate SMILES strings.
3. Detect warheads using RDKit SMARTS matching.
4. Calculate molecular descriptors.
5. Apply simple Lipinski filtering.
6. Score molecules based on detected warheads and descriptor quality.
7. Export results to CSV.
8. Generate plots for quick visual inspection.

---

## Tech Stack

Planned dependencies:

- Python 3.10+
- RDKit
- pandas
- matplotlib
- pytest

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Warhead-Screener-for-Covalent-Inhibitors.git
cd Warhead-Screener-for-Covalent-Inhibitors
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

If RDKit installation through pip does not work on a specific system, it may be installed using conda:

```bash
conda install -c conda-forge rdkit
```

---

## Usage

Run the screener on the example input file:

```bash
python src/main.py --input data/example_library.smi --output output/results.csv
```

Optional: save plots to the output folder:

```bash
python src/main.py --input data/example_library.smi --output output/results.csv --plots output
```

---


### Example Files Included

The repository includes small example files so the project can be tested immediately:

```text
data/example_library.smi
data/example_library.sdf
data/example_config.json
```

Example SDF run:

```bash
python src/main.py --input data/example_library.sdf --output output/sdf_results.csv --plots output
```

Example config run:

```bash
python src/main.py --input data/example_library.smi --config data/example_config.json --output output/config_results.csv
```

## Running Tests

Run all tests using:

```bash
pytest
```

---

## Validation & Success Criteria

The project will be considered successful if it can:

- Correctly read a SMILES input file.
- Correctly identify known warheads in test molecules.
- Calculate basic descriptors using RDKit.
- Report Lipinski rule violations.
- Generate a ranked output CSV file.
- Generate at least one summary plot.
- Pass automated tests for warhead detection and scoring.

---

## Risks & Mitigations

### Warhead detection accuracy

SMARTS patterns may be too broad or too narrow.

**Mitigation:** The project will include test molecules with known warheads and unit tests for the detector.

### RDKit installation issues

RDKit can sometimes be difficult to install depending on the operating system.

**Mitigation:** The README includes both pip and conda installation options.

### Large library performance

Very large libraries may take longer to process.

**Mitigation:** The initial version will focus on small to medium libraries, and future versions may add progress bars or chunked processing.

---

## Future Development

Possible future improvements include:

- Support for `.sdf` files.
- More warhead classes.
- PAINS filtering.
- Excel export.
- Interactive HTML reports.
- GUI version.
- Custom user-defined SMARTS patterns.
- More advanced scoring for covalent inhibitor suitability.

---

## Repository Structure

```text
Warhead-Screener-for-Covalent-Inhibitors/
├── data/
│   ├── example_library.smi
│   └── warhead_patterns.json
├── output/
├── src/
│   ├── main.py
│   ├── warhead_detector.py
│   ├── descriptors.py
│   ├── scoring.py
│   └── visualization.py
├── tests/
│   ├── test_warhead_detector.py
│   └── test_scoring.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Deliverables

The final project will include:

- A working command-line Python tool.
- Example input data.
- Output CSV file generated from the example data.
- Summary plots.
- Automated tests.
- Installation and usage instructions.

---
## Use of AI Assistance

AI tools (ChatGPT) were used during the development of this project as a programming assistant.

The assistance included:

- Brainstorming project ideas and evaluating their feasibility.
- Designing the overall project structure and repository organization.
- Explaining RDKit functionality and SMARTS-based substructure searching.
- Assisting with implementation of molecular descriptor calculations and Lipinski rule evaluation.
- Helping design the scoring system and visualization components.
- Assisting with writing and improving unit tests.
- Providing guidance for debugging Python, RDKit, and Git issues encountered during development.


## Course Information

This project was prepared for the WIS Python course project.

Course repository: https://github.com/Code-Maven/wis-python-course-2026-03
