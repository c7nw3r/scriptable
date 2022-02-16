from typing import List, Any

from scriptable.api import AST
from scriptable.api.ast_binding import ASTBinding
from scriptable.api.exit_value import ExitValue


class FunctionTail(AST[Any]):
    def __init__(self, branch: List[AST]):
        self.branch = branch

    def execute(self, context: ASTBinding) -> Any:
        result = None
        for branch in self.branch:
            result = branch.execute(context)
            if isinstance(result, ExitValue):
                return result.value

        return result

    @staticmethod
    def parse(branch: List[AST]) -> 'FunctionTail':
        return FunctionTail(branch)

    def __repr__(self):
        return " ".join(map(str, self.branch))
