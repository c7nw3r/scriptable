from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import TypeVar, Generic, Any, Dict, Callable, List


@dataclass
class ASTBinding:
    functions: Dict[str, Callable[[List[Any], 'ASTBinding'], Any]] = field(default_factory=lambda: {})
    properties: Dict[str, Any] = field(default_factory=lambda: {})
    signatures: Dict[str, int] = field(default_factory=lambda: {})

    def add_property(self, name: str, value: Any):
        self.properties[name] = value

    def add_function(self, name: str, value: Callable[[List[Any]], Any]):
        self.functions[name] = value

    def add_signature(self, signature: str) -> int:
        if signature in self.signatures:
            self.signatures[signature] += 1
        else:
            self.signatures[signature] = 1
        return self.signatures[signature]


class SourceAwareContext(ASTBinding):
    def __init__(self, source: Any, context: ASTBinding):
        self.source = source
        self.functions = context.functions
        self.properties = context.properties

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
