from typing import Any, List

from scriptable.api import AST
from scriptable.api.AST import ASTBinding


class PropertyAccess(AST[Any]):
    def __init__(self, branch: List[AST]):
        self.branch = branch

    def execute(self, binding: ASTBinding) -> bool:
        branch = list(map(lambda ast: ast.execute(binding), self.branch))
        current = branch.pop(0)
        while len(branch) > 0:
            current = current[branch.pop(0)]
        return current

    @staticmethod
    def parse(branch: List[AST]) -> 'PropertyAccess':
        return PropertyAccess(branch)
