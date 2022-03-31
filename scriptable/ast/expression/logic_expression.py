from typing import List

from scriptable.api import AST
from scriptable.api.ast_binding import ASTBinding
from scriptable.ast.expression.operator import Operator


class LogicExpression(AST[bool]):
    def __init__(self, branch: List[AST]):
        self.operand_stack = list(filter(lambda x: not isinstance(x, Operator), branch))
        self.operator_stack = list(filter(lambda x: isinstance(x, Operator), branch))

    def execute(self, binding: ASTBinding) -> bool:
        operand_stack = list(map(lambda ast: ast.execute(binding), self.operand_stack))
        operator_stack = list(map(lambda ast: ast.execute(binding), self.operator_stack))

        if len(operand_stack) == 1:
            value = operand_stack.pop()
            for _ in operator_stack:
                value = not value
            return value

        for i in range(len(operator_stack) - 1, -1, -1):
            value2 = operand_stack.pop(i + 1)
            value1 = operand_stack.pop(i)
            operator = operator_stack.pop(i)

            if operator == "and":
                operand_stack.insert(i, value1 and value2)
            if operator == "or":
                operand_stack.insert(i, value1 or value2)
            if operator == "==":
                operand_stack.insert(i, value1 == value2)
            if operator == "!=":
                operand_stack.insert(i, value1 != value2)
            if operator == ">":
                operand_stack.insert(i, value1 > value2)
            if operator == ">=":
                operand_stack.insert(i, value1 >= value2)
            if operator == "<":
                operand_stack.insert(i, value1 < value2)
            if operator == "<=":
                operand_stack.insert(i, value1 <= value2)

        return operand_stack.pop()

    @staticmethod
    def parse(branch: List[AST]):
        return LogicExpression(branch)

    def __repr__(self):
        stack = []
        for a, b in zip(self.operand_stack, self.operator_stack):
            stack.append(a)
            stack.append(b)
        stack.append(self.operand_stack[-1])

        return " ".join(map(str, stack))
