from typing import Any, List

from scriptable.api import AST
from scriptable.api.accessor import Accessor
from scriptable.api.ast_binding import ASTBinding


class PropertyAccess(AST[Any]):
    def __init__(self, branch: List[AST]):
        self.branch = branch

    def execute(self, binding: ASTBinding) -> bool:
        def unwrap(obj):
            if isinstance(obj, Accessor):
                return obj.value
            return obj

        branch = list(map(lambda ast: ast.execute(binding), self.branch))
        current = branch.pop(0)
        while len(branch) > 0:
            key = unwrap(branch.pop(0))
            if key not in current:
                raise ValueError(f"no property '{key}' found")
            current = current[key]
        return current

    @staticmethod
    def parse(branch: List[AST]) -> 'PropertyAccess':
        return PropertyAccess(branch)
