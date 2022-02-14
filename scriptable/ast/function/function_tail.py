from typing import List, Any

from scriptable.api import AST
from scriptable.api.AST import ASTBinding, T


class FunctionTail(AST[Any]):
    def __init__(self, branch: List[AST]):
        self.branch = branch

    def execute(self, context: ASTBinding) -> T:
        return self.branch[-1].execute(context)

    @staticmethod
    def parse(branch: List[AST]) -> 'FunctionTail':
        return FunctionTail(branch)
