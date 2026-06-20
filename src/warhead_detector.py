from pathlib import Path
import json
from rdkit import Chem


def load_warhead_patterns(pattern_file, selected_warheads="all"):
    """Load SMARTS patterns from a JSON file.

    selected_warheads can be "all" or a list of warhead names.
    """
    pattern_path = Path(pattern_file)
    with pattern_path.open("r", encoding="utf-8") as handle:
        raw_patterns = json.load(handle)

    if selected_warheads != "all" and selected_warheads is not None:
        selected_warheads = set(selected_warheads)
        raw_patterns = {
            name: data
            for name, data in raw_patterns.items()
            if name in selected_warheads
        }

    compiled_patterns = {}
    for name, data in raw_patterns.items():
        smarts = data["smarts"]
        pattern = Chem.MolFromSmarts(smarts)
        if pattern is None:
            raise ValueError(f"Invalid SMARTS pattern for {name}: {smarts}")
        compiled_patterns[name] = pattern

    return compiled_patterns


def detect_warheads(mol, compiled_patterns):
    """Return a list of warhead names detected in an RDKit molecule."""
    if mol is None:
        return []

    detected = []
    for name, pattern in compiled_patterns.items():
        if mol.HasSubstructMatch(pattern):
            detected.append(name)

    return detected
