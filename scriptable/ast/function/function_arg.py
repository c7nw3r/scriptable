from typing import Any, List, Tuple

from scriptable.api import AST
from scriptable.api.ast_binding import ASTBinding


class FunctionArg(AST[Any]):
    def __init__(self, arg_value: AST[Any]):
        self.arg_value = arg_value

    def execute(self, binding: ASTBinding) -> Tuple[str, List[Any]]:
        return self.arg_value.execute(binding)

    @staticmethod
    def parse(branch: List[AST]) -> 'FunctionArg':
        return FunctionArg(branch[0])

    def __repr__(self):
        return str(self.arg_value)