from typing import List

from scriptable.api import AST
from scriptable.api.AST import ASTBinding, EmptyAST
from scriptable.ast.variable.assignment import Assignment


class For(AST[None]):

    def __init__(self, assignment: Assignment, expression: AST, statement: AST, tail: AST):
        self.assignment = assignment
        self.expression = expression
        self.statement = statement
        self.tail = tail

    def execute(self, context: ASTBinding) -> None:
        if self.assignment.name in context.properties:
            raise ValueError(f"property {self.assignment.name} is already defined")

        self.assignment.execute(context)
        value = context.properties[self.assignment.name]
        assert value <= context.sandbox.max_loops, "max loops exceeded"

        counter = 0
        while self.expression.execute(context):
            self.tail.execute(context)
            self.statement.execute(context)

            assert counter <= context.sandbox.max_loops, "max loops exceeded"
            counter = counter + 1

        return None

    @staticmethod
    def parse(branch: List[AST]) -> 'For':
        if len(branch) > 3:
            # noinspection PyTypeChecker
            return For(branch[0], branch[1], branch[2], branch[3])
        # noinspection PyTypeChecker
        return For(branch[0], branch[1], branch[2], EmptyAST())
