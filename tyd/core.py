from __future__ import annotations

from typing import Callable, Optional, TypeVar

T = TypeVar("T")
K = TypeVar("K")

def unwrap(item: Optional[T]) -> T:
    if item is None:
        raise RuntimeError("Called unwrap on None")
    else:
        return item

def unwrap_or(item: Optional[T], default: T) -> T:
    return item or default

def unwrap_or_else(item: Optional[T], fn: Callable[[], T]):
    return item or fn()

def map(item: Optional[T], fn: Callable[[T], K]) -> Optional[K]:
    if item:
        return fn(item)

def is_some(item: Optional[T]) -> bool:
    return item is not None

def is_none(item: Optional[T]) -> bool:
    return item is None
