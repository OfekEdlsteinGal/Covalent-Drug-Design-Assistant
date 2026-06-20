from src.config import load_config
from src.io_utils import read_molecule_file


def test_load_config(tmp_path):
    config_file = tmp_path / "config.json"
    config_file.write_text('{"warheads": ["acrylamide"], "max_lipinski_violations": 1}', encoding="utf-8")
    config = load_config(config_file)
    assert config["warheads"] == ["acrylamide"]
    assert config["max_lipinski_violations"] == 1


def test_read_smiles_file(tmp_path):
    smi_file = tmp_path / "test.smi"
    smi_file.write_text("CCO ethanol\n", encoding="utf-8")
    molecules = read_molecule_file(smi_file)
    assert len(molecules) == 1
    assert molecules[0]["MoleculeID"] == "ethanol"
    assert molecules[0]["ValidStructure"] is True
