from pathlib import Path
from rdkit import Chem


def read_smiles_file(input_file):
    """Read a SMILES file with format: SMILES molecule_id."""
    molecules = []

    with open(input_file, "r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            parts = line.split()
            smiles = parts[0]
            molecule_id = parts[1] if len(parts) > 1 else f"molecule_{line_number}"
            mol = Chem.MolFromSmiles(smiles)

            molecules.append({
                "MoleculeID": molecule_id,
                "SMILES": smiles,
                "Mol": mol,
                "ValidStructure": mol is not None,
            })

    return molecules


def read_sdf_file(input_file):
    """Read molecules from an SDF file."""
    molecules = []
    supplier = Chem.SDMolSupplier(str(input_file), removeHs=False)

    for index, mol in enumerate(supplier, start=1):
        if mol is None:
            molecules.append({
                "MoleculeID": f"invalid_sdf_record_{index}",
                "SMILES": None,
                "Mol": None,
                "ValidStructure": False,
            })
            continue

        molecule_id = mol.GetProp("_Name") if mol.HasProp("_Name") else f"molecule_{index}"
        smiles = Chem.MolToSmiles(mol)

        molecules.append({
            "MoleculeID": molecule_id,
            "SMILES": smiles,
            "Mol": mol,
            "ValidStructure": True,
        })

    return molecules


def read_molecule_file(input_file):
    """Read SMILES or SDF input based on file extension."""
    path = Path(input_file)
    suffix = path.suffix.lower()

    if suffix in {".smi", ".smiles", ".txt"}:
        return read_smiles_file(path)

    if suffix == ".sdf":
        return read_sdf_file(path)

    raise ValueError(
        f"Unsupported input format '{suffix}'. Use .smi, .smiles, .txt, or .sdf."
    )
