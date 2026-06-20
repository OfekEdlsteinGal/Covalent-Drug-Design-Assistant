import json
from pathlib import Path


DEFAULT_CONFIG = {
    "warheads": "all",
    "max_lipinski_violations": None,
    "enable_pains_filter": True,
    "output_excel": None,
}


def load_config(config_file=None):
    """Load optional JSON configuration and merge it with defaults."""
    config = DEFAULT_CONFIG.copy()

    if config_file is None:
        return config

    config_path = Path(config_file)
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_file}")

    with config_path.open("r", encoding="utf-8") as handle:
        user_config = json.load(handle)

    if not isinstance(user_config, dict):
        raise ValueError("Config file must contain a JSON object.")

    config.update(user_config)
    return config
