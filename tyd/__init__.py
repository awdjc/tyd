from typing import Optional

from .core import (
    is_none,
    is_some,
    map,
    unwrap,
    unwrap_or,
    unwrap_or_else,
)

__all__ = [
    "is_none",
    "is_some",
    "map",
    "unwrap",
    "unwrap_or",
    "unwrap_or_else",
    "Optional"  # re-export
]
__version__ = "0.0.1"
