import sys
from pathlib import Path

import yaml


def get_config_local(filename: Path) -> dict:
    with open(filename) as file:
        return yaml.safe_load(file)


def get_config() -> dict:
    try:
        script_dir = Path(__file__).resolve().parent
        config_dict = get_config_local(script_dir / 'config.yaml')
        return config_dict
    except FileNotFoundError as e:
        print(f'config.yaml: {repr(e)}', file=sys.stderr)
        sys.exit(1)


config = get_config()
