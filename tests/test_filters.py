from rdkit import Chem
from src.filters import get_pains_matches


def test_pains_function_returns_list():
    mol = Chem.MolFromSmiles("CCO")
    matches = get_pains_matches(mol)
    assert isinstance(matches, list)
