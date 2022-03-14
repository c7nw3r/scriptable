from typing import Any, List

from scriptable.api import AST
from scriptable.api.accessor import Accessor
from scriptable.api.ast_binding import ASTBinding


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
        while len(branch) > 1:
            current = current[unwrap(branch.pop(0))]

        del current[unwrap(branch.pop(0))]
        return True

    @staticmethod
    def parse(branch: List[AST]) -> 'PropertyDelete':
        return PropertyDelete(branch)
