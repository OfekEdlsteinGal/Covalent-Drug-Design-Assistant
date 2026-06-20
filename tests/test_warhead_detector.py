from rdkit import Chem
from src.warhead_detector import detect_warheads, load_warhead_patterns


def test_detect_acrylamide():
    mol = Chem.MolFromSmiles("C=CC(=O)NC1=CC=CC=C1")
    patterns = {"acrylamide": Chem.MolFromSmarts("C=CC(=O)N")}
    assert detect_warheads(mol, patterns) == ["acrylamide"]


def test_no_warhead_detected():
    mol = Chem.MolFromSmiles("CCO")
    patterns = {"acrylamide": Chem.MolFromSmarts("C=CC(=O)N")}
    assert detect_warheads(mol, patterns) == []


def test_load_selected_warheads(tmp_path):
    pattern_file = tmp_path / "patterns.json"
    pattern_file.write_text(
        '{"acrylamide": {"smarts": "C=CC(=O)N"}, "aldehyde": {"smarts": "[CX3H1](=O)"}}',
        encoding="utf-8",
    )
    patterns = load_warhead_patterns(pattern_file, ["aldehyde"])
    assert list(patterns.keys()) == ["aldehyde"]
