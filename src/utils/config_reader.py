import json
from pathlib import Path
from typing import Any


def read_config(path: Path) -> dict[str, Any]:
    """
    Reads the config file and returns a dictionary.
    """
    with open(path, encoding='utf-8') as file_:
        return json.load(file_)
