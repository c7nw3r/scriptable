from typing import Any, List

from scriptable.api import AST
from scriptable.api.ast_binding import ASTBinding, SourceAwareContext


class FunctionAccess(AST[Any]):
    def __init__(self, branch: List[AST]):
        self.branch = branch

    def execute(self, binding: ASTBinding) -> Any:
        current = None

        for item in self.branch:
            _binding = binding if current is None else SourceAwareContext(current, binding)
            current = item.execute(_binding)

        return current

    @staticmethod
    def parse(branch: List[AST]) -> 'FunctionAccess':
        return FunctionAccess(branch)
