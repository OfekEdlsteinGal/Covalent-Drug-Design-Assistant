from pathlib import Path
import matplotlib.pyplot as plt


def make_summary_plots(df, output_dir):
    """Generate summary plots from screening results."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    if "MW" in df.columns:
        plt.figure()
        df["MW"].dropna().hist(bins=20)
        plt.xlabel("Molecular Weight")
        plt.ylabel("Count")
        plt.title("Molecular Weight Distribution")
        plt.tight_layout()
        plt.savefig(output_path / "molecular_weight_distribution.png")
        plt.close()

    if "LogP" in df.columns:
        plt.figure()
        df["LogP"].dropna().hist(bins=20)
        plt.xlabel("LogP")
        plt.ylabel("Count")
        plt.title("LogP Distribution")
        plt.tight_layout()
        plt.savefig(output_path / "logp_distribution.png")
        plt.close()

    if "LipinskiViolations" in df.columns:
        plt.figure()
        df["LipinskiViolations"].value_counts().sort_index().plot(kind="bar")
        plt.xlabel("Number of Lipinski Violations")
        plt.ylabel("Count")
        plt.title("Lipinski Violation Counts")
        plt.tight_layout()
        plt.savefig(output_path / "lipinski_violation_counts.png")
        plt.close()

    if "Warheads" in df.columns:
        warhead_counts = {}
        for item in df["Warheads"].dropna():
            if item == "None":
                continue
            for warhead in str(item).split(";"):
                warhead_counts[warhead] = warhead_counts.get(warhead, 0) + 1

        if warhead_counts:
            plt.figure()
            plt.bar(warhead_counts.keys(), warhead_counts.values())
            plt.xlabel("Warhead Type")
            plt.ylabel("Count")
            plt.title("Detected Warhead Frequency")
            plt.xticks(rotation=45, ha="right")
            plt.tight_layout()
            plt.savefig(output_path / "warhead_frequency.png")
            plt.close()
