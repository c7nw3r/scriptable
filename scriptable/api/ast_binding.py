from dataclasses import dataclass, field
from typing import Dict, Callable, List, Any

from scriptable.api.ast_restrictions import ASTRestrictions


@dataclass
class ASTBinding:
    functions: Dict[str, Callable[[List[Any], 'ASTBinding'], Any]] = field(default_factory=lambda: {})
    properties: Dict[str, Any] = field(default_factory=lambda: {})
    signatures: Dict[str, int] = field(default_factory=lambda: {})
    restrictions: ASTRestrictions = ASTRestrictions()

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
