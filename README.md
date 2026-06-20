<<<<<<< HEAD
# Warhead Screener for Covalent Inhibitors

> **Important:** This README describes a work-in-progress Python course project and may change during implementation.

## Summary

Warhead Screener for Covalent Inhibitors is a Python-based cheminformatics tool for screening small-molecule libraries and identifying compounds that contain covalent inhibitor warheads.

The tool will read molecular libraries from SMILES files, detect selected covalent warheads using SMARTS substructure matching, calculate basic drug-likeness descriptors, rank candidate molecules, and export the results as structured tables and summary plots.

The goal is to automate an early-stage medicinal chemistry workflow that is usually done manually: checking whether molecules contain electrophilic functional groups that may react covalently with amino acid residues such as cysteine, lysine, serine, or tyrosine.
=======
## Overview

Warhead Screener for Covalent Inhibitors is a Python-based cheminformatics tool designed to automate the identification and prioritization of covalent inhibitor candidates from large chemical libraries.

Covalent inhibitors have become an important class of therapeutic agents in modern drug discovery. These compounds contain reactive functional groups, commonly known as **warheads**, that form covalent bonds with specific amino acid residues in target proteins. Selecting suitable covalent inhibitor candidates from large compound collections is often a time-consuming process that requires manual filtering, structural analysis, and evaluation of drug-like properties.

This project aims to automate part of this workflow by screening molecular libraries, detecting covalent warheads, filtering undesirable compounds, calculating physicochemical properties, and ranking potential candidates for further experimental evaluation.
>>>>>>> ecaefad72d165baace107c314473d38a57da2b89

---

## Motivation

<<<<<<< HEAD
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
=======
During medicinal chemistry and drug discovery projects, researchers frequently need to identify molecules containing electrophilic warheads capable of reacting with amino acid residues such as cysteine, lysine, serine, or tyrosine.

This process often involves:

* Manual inspection of molecular structures.
* Searching for known warhead motifs.
* Calculating molecular properties.
* Removing compounds with undesirable structural features.
* Prioritizing candidates for synthesis or biological testing.

The goal of this project is to provide a reproducible and automated workflow that simplifies these tasks and helps researchers focus on the most promising molecules.

---

## Features

### 1. Covalent Warhead Detection

The software automatically scans molecular libraries and identifies compounds containing known covalent warheads using SMARTS-based substructure searches.

Initially supported warheads include:

* Acrylamides
* Cyanoacrylamides
* Vinyl sulfones
* Vinyl sulfonamides
* Chloroacetamides
* Sulfonyl fluorides
* Epoxides
* Aldehydes
* Boronic acids

Additional warheads can be added by extending the SMARTS pattern database.

---

### 2. Chemical Library Screening

The tool accepts large collections of molecules and screens them automatically.

Supported input formats:

* SMILES (.smi)
* Structure Data Files (.sdf)

Each molecule is evaluated individually and annotated with detected warhead information.

---

### 3. Drug-Likeness Evaluation

For each compound, the software calculates common medicinal chemistry descriptors, including:

* Molecular Weight (MW)
* LogP
* Hydrogen Bond Donors (HBD)
* Hydrogen Bond Acceptors (HBA)
* Topological Polar Surface Area (TPSA)
* Number of Rotatable Bonds

The program evaluates compliance with Lipinski's Rule of Five and reports potential violations.

---

### 4. Structural Alert Filtering

The tool can identify and flag potentially problematic compounds, including:

* PAINS (Pan-Assay Interference Compounds)
* Reactive structural alerts
* Undesirable functional groups

This allows users to quickly remove compounds that are likely to generate false-positive biological results.

---

### 5. Candidate Ranking

After screening, compounds are assigned a prioritization score based on:

* Presence of desired warheads
* Drug-likeness properties
* Number of Lipinski violations
* Structural alerts
* Physicochemical properties

The goal is not to predict biological activity, but rather to prioritize compounds that may be suitable for further investigation.

---

### 6. Data Export and Visualization

Results can be exported to:

* CSV files
* Excel spreadsheets

The software can also generate summary plots such as:

* Molecular weight distribution
* LogP distribution
* Lipinski violation counts
* Warhead frequency analysis

Generated figures will be saved as PNG files.

---

## Input

### Required Input

A chemical library containing molecular structures:

```text
library.smi
```

or

```text
library.sdf
```

### Optional Configuration File

Users may provide a configuration file specifying:

* Warheads to search for
* Filtering options
* Scoring parameters
* Output preferences

Example:

```json
{
  "warheads": ["acrylamide", "vinyl_sulfone"],
  "max_lipinski_violations": 1
}
>>>>>>> ecaefad72d165baace107c314473d38a57da2b89
```

---

<<<<<<< HEAD
## Expected Output

The program will generate a CSV table containing one row per molecule.

Example columns:

| Molecule ID | SMILES | Warheads | MW | LogP | HBD | HBA | TPSA | Rotatable Bonds | Lipinski Violations | Score |
|------------|--------|----------|----|------|-----|-----|------|-----------------|---------------------|-------|
=======
## Output

The program generates a ranked table containing:

| Molecule ID | SMILES | Warhead Type | MW | LogP | HBD | HBA | Lipinski Violations | Score |
| ----------- | ------ | ------------ | -- | ---- | --- | --- | ------------------- | ----- |
>>>>>>> ecaefad72d165baace107c314473d38a57da2b89

Example output:

```text
<<<<<<< HEAD
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
=======
compound_001
Warhead: Acrylamide
MW: 412.3
LogP: 2.8
Lipinski Violations: 0
Priority Score: 91
```

---

## Technologies

This project is implemented in Python and primarily relies on:

* RDKit
* Pandas
* NumPy
* Matplotlib
* OpenPyXL
* Pytest
>>>>>>> ecaefad72d165baace107c314473d38a57da2b89

---

## Installation

Clone the repository:

```bash
<<<<<<< HEAD
git clone https://github.com/YOUR_USERNAME/Warhead-Screener-for-Covalent-Inhibitors.git
cd Warhead-Screener-for-Covalent-Inhibitors
```

Create and activate a virtual environment:
=======
git clone https://github.com/OfekEdlsteinGal/Covalent-Drug-Design-Assistant.git
cd Covalent-Drug-Design-Assistant
```

Create a virtual environment:
>>>>>>> ecaefad72d165baace107c314473d38a57da2b89

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

<<<<<<< HEAD
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
=======
---

## Running the Project

Screen a SMILES library:

```bash
python src/main.py --input library.smi
```

Screen an SDF library:

```bash
python src/main.py --input library.sdf
```

Specify a configuration file:

```bash
python src/main.py --input library.sdf --config config.json
```

## Running Tests
To run the automated tests and verify the substructure matching logic:
>>>>>>> ecaefad72d165baace107c314473d38a57da2b89

```bash
pytest
```

<<<<<<< HEAD
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

## Course Information

This project was prepared for the WIS Python course project.

Course repository: https://github.com/Code-Maven/wis-python-course-2026-03
=======
## Acknowledgments
This project was developed as part of the Scientific Programming Course. [Link to the course repository](https://github.com/OfekEdlsteinGal/Covalent-Drug-Design-Assistant).
>>>>>>> ecaefad72d165baace107c314473d38a57da2b89
