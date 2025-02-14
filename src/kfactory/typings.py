"""KFactory types."""

from collections.abc import Callable
from pathlib import Path
from typing import TypeAlias

from kfactory.kcell import KCell

CellFactory = Callable[..., KCell]
"""
    A function that will return a [KCell][kfactory.kcell.KCell].
"""
CellSpec: TypeAlias = str | CellFactory | KCell | dict[str, CellFactory | KCell]
"""
    Can be a string or another means to retrieve a [KCell][kfactory.kcell.KCell].
"""
PathType: TypeAlias = str | Path
"""
    A string that can be parsed to a `Path` object or a `Path` object directly.
"""
