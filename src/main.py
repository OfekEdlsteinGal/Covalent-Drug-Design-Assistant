import argparse
from pathlib import Path
import pandas as pd

try:
    from .config import load_config
    from .io_utils import read_molecule_file
    from .warhead_detector import load_warhead_patterns, detect_warheads
    from .descriptors import calculate_descriptors, count_lipinski_violations
    from .filters import build_pains_catalog, get_pains_matches
    from .scoring import calculate_score
    from .visualization import make_summary_plots
except ImportError:
    from config import load_config
    from io_utils import read_molecule_file
    from warhead_detector import load_warhead_patterns, detect_warheads
    from descriptors import calculate_descriptors, count_lipinski_violations
    from filters import build_pains_catalog, get_pains_matches
    from scoring import calculate_score
    from visualization import make_summary_plots


def screen_library(input_file, pattern_file, config_file=None):
    config = load_config(config_file)
    patterns = load_warhead_patterns(pattern_file, config.get("warheads", "all"))
    molecules = read_molecule_file(input_file)

    enable_pains = bool(config.get("enable_pains_filter", True))
    pains_catalog = build_pains_catalog() if enable_pains else None
    max_lipinski = config.get("max_lipinski_violations")

    results = []

    for entry in molecules:
        mol = entry["Mol"]
        detected_warheads = detect_warheads(mol, patterns)
        desc = calculate_descriptors(mol)
        lipinski_violations = count_lipinski_violations(desc)
        pains_matches = get_pains_matches(mol, pains_catalog) if enable_pains else []
        pains_alert = len(pains_matches) > 0
        score = calculate_score(detected_warheads, lipinski_violations, pains_alert)

        keep_by_lipinski = (
            max_lipinski is None or lipinski_violations <= int(max_lipinski)
        )

        results.append({
            "MoleculeID": entry["MoleculeID"],
            "SMILES": entry["SMILES"],
            "ValidStructure": entry["ValidStructure"],
            "Warheads": ";".join(detected_warheads) if detected_warheads else "None",
            **desc,
            "LipinskiViolations": lipinski_violations,
            "PAINSAlert": pains_alert,
            "PAINSMatches": ";".join(pains_matches) if pains_matches else "None",
            "PassesConfigFilters": keep_by_lipinski,
            "Score": score,
        })

    df = pd.DataFrame(results)
    df = df.sort_values(by="Score", ascending=False)
    return df


def main():
    parser = argparse.ArgumentParser(
        description="Screen SMILES/SDF libraries for covalent inhibitor warheads."
    )
    parser.add_argument("--input", required=True, help="Input .smi or .sdf file")
    parser.add_argument("--output", default="output/results.csv", help="Output CSV file")
    parser.add_argument("--excel", default=None, help="Optional output Excel file")
    parser.add_argument(
        "--patterns",
        default="data/warhead_patterns.json",
        help="JSON file containing warhead SMARTS patterns",
    )
    parser.add_argument("--config", default=None, help="Optional JSON config file")
    parser.add_argument("--plots", default=None, help="Optional directory for plots")

    args = parser.parse_args()

    df = screen_library(args.input, args.patterns, args.config)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)

    if args.excel:
        excel_path = Path(args.excel)
        excel_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_excel(excel_path, index=False)

    if args.plots:
        make_summary_plots(df, args.plots)

    print(f"Screening complete. Results saved to: {output_path}")
    if args.excel:
        print(f"Excel file saved to: {args.excel}")
    print(df[["MoleculeID", "Warheads", "MW", "LogP", "LipinskiViolations", "PAINSAlert", "Score"]])


if __name__ == "__main__":
    main()
