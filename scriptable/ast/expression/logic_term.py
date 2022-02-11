from typing import Union, List

from scriptable.api import AST
from scriptable.api.AST import ASTBinding
from scriptable.ast.expression.logic_expression import LogicExpression

DataType = Union[int, float]


class LogicTerm(AST[DataType]):
    def __init__(self, branch: List[AST]):
        self.expression = LogicExpression(branch)

    def execute(self, binding: ASTBinding) -> DataType:
        return self.expression.execute(binding)

    @staticmethod
    def parse(branch: List[AST]):
        return LogicTerm(branch)
