from rdkit.Chem import Descriptors, Crippen, rdMolDescriptors


def calculate_descriptors(mol):
    """Calculate basic medicinal chemistry descriptors for an RDKit molecule."""
    if mol is None:
        return {
            "MW": None,
            "LogP": None,
            "HBD": None,
            "HBA": None,
            "TPSA": None,
            "RotatableBonds": None,
        }

    return {
        "MW": round(Descriptors.MolWt(mol), 2),
        "LogP": round(Crippen.MolLogP(mol), 2),
        "HBD": int(rdMolDescriptors.CalcNumHBD(mol)),
        "HBA": int(rdMolDescriptors.CalcNumHBA(mol)),
        "TPSA": round(rdMolDescriptors.CalcTPSA(mol), 2),
        "RotatableBonds": int(rdMolDescriptors.CalcNumRotatableBonds(mol)),
    }


def count_lipinski_violations(desc):
    """Count simple Lipinski Rule of Five violations."""
    violations = 0

    if desc["MW"] is not None and desc["MW"] > 500:
        violations += 1
    if desc["LogP"] is not None and desc["LogP"] > 5:
        violations += 1
    if desc["HBD"] is not None and desc["HBD"] > 5:
        violations += 1
    if desc["HBA"] is not None and desc["HBA"] > 10:
        violations += 1

    return violations
