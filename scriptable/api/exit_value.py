from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass
class ExitValue(Generic[T]):
    status: int
    value: T


@dataclass
class GoTo:
    value: str
