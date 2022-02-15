from typing import List

from scriptable.api import AST
from scriptable.api.AST import ASTBinding


class While(AST[None]):

    def __init__(self, expression: AST, tail: AST):
        self.expression = expression
        self.tail = tail

    def execute(self, context: ASTBinding) -> None:
        counter = 0
        while self.expression.execute(context):
            self.tail.execute(context)

            assert counter <= context.sandbox.max_loops, "max loops exceeded"
            counter += 1
        return None

    @staticmethod
    def parse(branch: List[AST]) -> 'While':
        return While(branch[0], branch[1])
