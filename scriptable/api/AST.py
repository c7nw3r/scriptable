from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TypeVar, Generic


@dataclass
class ASTBinding:
    pass

T = TypeVar("T")


class AST(ABC, Generic[T]):

    @abstractmethod
    def execute(self, context: ASTBinding) -> T:
        pass


@dataclass
class FunctionSpec:
    params: [str]
    result: str
