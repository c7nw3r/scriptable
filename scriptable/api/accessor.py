from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Any, List

T = TypeVar("T")


class Accessor(ABC, Generic[T]):
    value: T

    @abstractmethod
    def __getitem__(self, item):
        pass

    @abstractmethod
    def __call__(self, name: str, args: List[Any]):
        pass

    def __eq__(self, other):
        if isinstance(other, Accessor):
            return self.value == other.value
        return self.value == other
