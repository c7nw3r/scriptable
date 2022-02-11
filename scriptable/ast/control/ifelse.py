from typing import Any, List, Optional

from scriptable.api import AST
from scriptable.api.AST import ASTBinding


class If(AST[Optional[Any]]):

    def __init__(self, branch: List[AST]):
        self.branch = branch

    def execute(self, context: ASTBinding) -> Optional[Any]:
        expression = self.branch[0].execute(context)
        if expression:
            return self.branch[1].execute(context)
        return None

    @staticmethod
    def parse(branch: List[AST]) -> 'If':
        return If(branch)