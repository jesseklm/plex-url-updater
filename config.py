import sys
import tomllib
from pathlib import Path

CONFIG_FILE = Path(__file__).resolve().parent / 'config.toml'


def load_config(filename: Path) -> dict:
    with filename.open('rb') as f:
        return tomllib.load(f)


def get_config() -> dict:
    try:
        return load_config(CONFIG_FILE)
    except FileNotFoundError:
        print(f'Config file not found: {CONFIG_FILE}', file=sys.stderr)
        sys.exit(1)
    except tomllib.TOMLDecodeError as e:
        print(f'Config file is not valid TOML: {e}', file=sys.stderr)
        sys.exit(1)


config = get_config()
