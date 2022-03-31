from typing import Any, List

from scriptable.api import AST
from scriptable.api.accessor import Accessor
from scriptable.api.ast_binding import ASTBinding
from scriptable.ast.optional import Optional


class PropertyDelete(AST[Any]):
    def __init__(self, branch: List[AST]):
        self.branch = branch[0].branch

    def execute(self, binding: ASTBinding) -> bool:
        def unwrap(obj):
            if isinstance(obj, Accessor):
                return obj.value
            return obj

        branch = list(map(lambda ast: ast.execute(binding), self.branch))
        current = branch.pop(0)

        optional = False
        while len(branch) > 1:
            key = unwrap(branch.pop(0))
            if isinstance(key, Optional):
                optional = True
                continue

            current = current[key]
            optional = False

        key = unwrap(branch.pop(0))
        if key not in current and optional:
            return False

        del current[key]
        return True

    @staticmethod
    def parse(branch: List[AST]) -> 'PropertyDelete':
        return PropertyDelete(branch)
