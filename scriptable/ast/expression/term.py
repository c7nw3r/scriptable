from typing import Union, List

from scriptable.api import AST
from scriptable.api.AST import ASTBinding
from scriptable.ast.expression.arithmetic_expression import ArithmeticExpression

DataType = Union[int, float]


class Term(AST[DataType]):
    def __init__(self, branch: List[AST]):
        self.expression = ArithmeticExpression(branch)

    def execute(self, binding: ASTBinding) -> DataType:
        return self.expression.execute(binding)

    @staticmethod
    def parse(branch: List[AST]):
        return Term(branch)
