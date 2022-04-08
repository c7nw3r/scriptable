from typing import List

from scriptable.api import AST
from scriptable.api.ast_binding import ASTBinding
from scriptable.api.exit_value import GoTo


class DoWhile(AST[None]):

    def __init__(self, tail: AST, expression: AST):
        self.tail = tail
        self.expression = expression

    def execute(self, context: ASTBinding) -> None:
        counter = 1
        self.tail.execute(context)

        while self.expression.execute(context):
            result = self.tail.execute(context)

            if isinstance(result, GoTo) and result.value == "break":
                break
            if isinstance(result, GoTo) and result.value == "continue":
                continue

            assert counter <= context.restrictions.max_loops, "max loops exceeded"
            counter += 1
        return None

    @staticmethod
    def parse(branch: List[AST]) -> 'DoWhile':
        return DoWhile(branch[0], branch[1])
