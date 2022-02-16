from typing import List

from scriptable.api import AST
from scriptable.api.ast_binding import ASTBinding
from scriptable.api.exit_value import GoTo


class LoopTail(AST[GoTo]):

    def __init__(self, branch: List[AST]):
        self.branch = branch

    def execute(self, context: ASTBinding) -> GoTo:
        for item in self.branch:
            result = item.execute(context)
            if isinstance(result, GoTo):
                return result
        return GoTo("end-of-loop")

    @staticmethod
    def parse(branch: List[AST]) -> 'LoopTail':
        return LoopTail(branch)
