from typing import Union, List

from scriptable.api import AST
from scriptable.api.ast_binding import ASTBinding
from scriptable.ast.expression.arithmetic_expression import ArithmeticExpression

DataType = Union[int, float]


class ArithmeticTerm(AST[DataType]):
    def __init__(self, branch: List[AST]):
        self.expression = ArithmeticExpression(branch)

    def execute(self, binding: ASTBinding) -> DataType:
        return self.expression.execute(binding)

    @staticmethod
    def parse(branch: List[AST]):
        return ArithmeticTerm(branch)
