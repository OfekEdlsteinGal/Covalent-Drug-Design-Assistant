from pathlib import Path
from src.main import screen_library


def test_screen_library_smiles_example():
    df = screen_library(
        "data/example_library.smi",
        "data/warhead_patterns.json",
        None,
    )
    assert "Warheads" in df.columns
    assert "Score" in df.columns
    assert len(df) >= 1


def test_screen_library_sdf_example():
    sdf_path = Path("data/example_library.sdf")
    if not sdf_path.exists():
        return
    df = screen_library(
        sdf_path,
        "data/warhead_patterns.json",
        None,
    )
    assert len(df) == 3
