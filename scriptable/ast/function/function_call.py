from typing import Any, List, Tuple

from scriptable.api import AST
from scriptable.api.AST import ASTBinding


class FunctionCall(AST[Tuple[str, List[Any]]]):
    def __init__(self, name: str, args: List[AST]):
        self.name = name
        self.args = args

    def execute(self, binding: ASTBinding) -> Tuple[str, List[Any]]:
        branch = list(map(lambda ast: ast.execute(binding), self.args))
        return self.name, branch

    @staticmethod
    def parse(text: str, branch: List[AST]) -> 'FunctionCall':
        return FunctionCall(text, branch)
