from typing import Union, List

from scriptable.api import AST
from scriptable.api.accessor import Accessor
from scriptable.api.ast_binding import ASTBinding

DataType = Union[int, float]


class ArithmeticExpression(AST[DataType]):
    def __init__(self, branch: List[AST]):
        self.operand_stack = [branch[x] for x in range(0, len(branch), 2)]
        self.operator_stack = [branch[x] for x in range(1, len(branch), 2)]

    def execute(self, binding: ASTBinding) -> DataType:
        from copy import deepcopy

        def execute_branch(ast: AST):
            result = ast
            while isinstance(result, AST):
                result = result.execute(deepcopy(binding))
            return result

        def unwrap(obj):
            if isinstance(obj, Accessor):
                return obj.value
            return obj

        operand_stack = list(map(lambda ast: execute_branch(ast), self.operand_stack))
        operator_stack = list(map(lambda ast: execute_branch(ast), self.operator_stack))

        # search for exponent operator
        for i in range(len(operator_stack) - 1, -1, -1):
            if operator_stack[i] == "**":
                value2 = operand_stack.pop(i + 1)
                value1 = operand_stack.pop(i)
                operand_stack.insert(i, value1 ** value2)
                operator_stack.pop(i)

        # search for mul and div operator
        for i in range(len(operator_stack) - 1, -1, -1):
            if operator_stack[i] == "*":
                value2 = operand_stack.pop(i + 1)
                value1 = operand_stack.pop(i)
                operand_stack.insert(i, value1 * value2)
                operator_stack.pop(i)
            elif operator_stack[i] == "/":
                value2 = operand_stack.pop(i + 1)
                value1 = operand_stack.pop(i)
                operand_stack.insert(i, value1 / value2)
                operator_stack.pop(i)

        # search for plus and minus operator
        for i in range(len(operator_stack) - 1, -1, -1):
            if operator_stack[i] == "+":
                value2 = unwrap(operand_stack.pop(i + 1))
                value1 = unwrap(operand_stack.pop(i))
                operand_stack.insert(i, value1 + value2)
                operator_stack.pop(i)
            elif operator_stack[i] == "-":
                value2 = operand_stack.pop(i + 1)
                value1 = operand_stack.pop(i)
                operand_stack.insert(i, value1 - value2)
                operator_stack.pop(i)

        return operand_stack.pop()

    @staticmethod
    def parse(branch: List[AST]):
        return ArithmeticExpression(branch)

    def __repr__(self):
        stack = []
        for a, b in zip(self.operand_stack, self.operator_stack):
            stack.append(a)
            stack.append(b)
        stack.append(self.operand_stack[-1])

        return " ".join(map(str, stack))
