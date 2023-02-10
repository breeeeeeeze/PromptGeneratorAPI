""" File path utilities. """
from pathlib import Path
from typing import Union


def get_parent(path: Union[str, Path]):
    """ Get parent directory of the given path. """
    if isinstance(path, str):
        path = Path(path)

    if not isinstance(path, Path):
        raise TypeError(f'Unknown path type: {type(path)}')

    return path.parent
