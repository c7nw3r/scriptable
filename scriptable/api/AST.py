from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import TypeVar, Generic, Any, Dict


@dataclass
class ASTBinding:
    properties: Dict[str, Any] = field(default_factory=lambda: {})

    def add_property(self, name: str, value: Any):
        self.properties[name] = value


T = TypeVar("T")


class AST(ABC, Generic[T]):

    @abstractmethod
    def execute(self, context: ASTBinding) -> T:
        pass


@dataclass
class FunctionSpec:
    params: [str]
    result: str


class BindingAware:

    def bind(self, binding: ASTBinding):
        pass
