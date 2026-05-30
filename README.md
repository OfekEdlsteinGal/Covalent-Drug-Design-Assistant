## Overview

Warhead Screener for Covalent Inhibitors is a Python-based cheminformatics tool designed to automate the identification and prioritization of covalent inhibitor candidates from large chemical libraries.

Covalent inhibitors have become an important class of therapeutic agents in modern drug discovery. These compounds contain reactive functional groups, commonly known as **warheads**, that form covalent bonds with specific amino acid residues in target proteins. Selecting suitable covalent inhibitor candidates from large compound collections is often a time-consuming process that requires manual filtering, structural analysis, and evaluation of drug-like properties.

This project aims to automate part of this workflow by screening molecular libraries, detecting covalent warheads, filtering undesirable compounds, calculating physicochemical properties, and ranking potential candidates for further experimental evaluation.

---

## Motivation

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
```

---

## Output

The program generates a ranked table containing:

| Molecule ID | SMILES | Warhead Type | MW | LogP | HBD | HBA | Lipinski Violations | Score |
| ----------- | ------ | ------------ | -- | ---- | --- | --- | ------------------- | ----- |

Example output:

```text
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

---

## Installation

Clone the repository:

```bash
git clone https://github.com/OfekEdlsteinGal/Covalent-Drug-Design-Assistant.git
cd Covalent-Drug-Design-Assistant
```

Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

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

```bash
pytest
```

## Acknowledgments
This project was developed as part of the Scientific Programming Course. [Link to the course repository](https://github.com/OfekEdlsteinGal/Covalent-Drug-Design-Assistant).
