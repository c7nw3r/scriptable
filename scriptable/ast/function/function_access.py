from typing import Any, List

from scriptable.api import AST
from scriptable.api.AST import ASTBinding
from scriptable.api.accessor import Accessor


class FunctionAccess(AST[Any]):
    def __init__(self, branch: List[AST]):
        self.branch = branch

    def execute(self, binding: ASTBinding) -> Any:
        branch = list(map(lambda ast: ast.execute(binding), self.branch))
        source = branch[0]
        if isinstance(source, Accessor):
            return branch[0](branch[1][0], branch[1][1])
        if hasattr(branch[0], branch[1][0]):
            return getattr(branch[0], branch[1][0])(*branch[1][1])
        return branch[0].__call__(*branch[1])

    @staticmethod
    def parse(branch: List[AST]) -> 'FunctionAccess':
        return FunctionAccess(branch)
