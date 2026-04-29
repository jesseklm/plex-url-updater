import sys
import tomllib
from pathlib import Path


def get_config_local(filename: Path) -> dict:
    with open(filename, 'rb') as f:
        return tomllib.load(f)


def get_config() -> dict:
    try:
        script_dir = Path(__file__).resolve().parent
        config_dict = get_config_local(script_dir / 'config.toml')
        return config_dict
    except FileNotFoundError as e:
        print(f'config.toml: {repr(e)}', file=sys.stderr)
        sys.exit(1)


config = get_config()
