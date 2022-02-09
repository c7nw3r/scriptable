from typing import List

from scriptable.api import AST
from scriptable.api.AST import ASTBinding


class LogicExpression(AST[bool]):
    def __init__(self, branch: List[AST]):
        self.operand_stack = [branch[x] for x in range(0, len(branch), 2)]
        self.operator_stack = [branch[x] for x in range(1, len(branch), 2)]

    def execute(self, binding: ASTBinding) -> bool:
        operand_stack = list(map(lambda ast: ast.execute(binding), self.operand_stack))
        operator_stack = list(map(lambda ast: ast.execute(binding), self.operator_stack))

        for i in range(len(operator_stack) - 1, -1, -1):
            value2 = operand_stack.pop(i + 1)
            value1 = operand_stack.pop(i)
            operator = operator_stack.pop(i)

            if operator == "and":
                operand_stack.insert(i, value1 and value2)
            if operator == "or":
                operand_stack.insert(i, value1 or value2)

        return operand_stack.pop()

    @staticmethod
    def parse(branch: List[AST]):
        return LogicExpression(branch)
