from typing import Union, List

from scriptable.api import AST
from scriptable.api.AST import ASTBinding

DataType = Union[int, float]


class ConcatExpression(AST[str]):
    def __init__(self, branch: List[AST]):
        self.operand_stack = [branch[x] for x in range(0, len(branch), 2)]
        self.operator_stack = [branch[x] for x in range(1, len(branch), 2)]

    def execute(self, binding: ASTBinding) -> str:
        from copy import deepcopy

        def execute_branch(ast: AST):
            result = ast
            while isinstance(result, AST):
                result = result.execute(deepcopy(binding))
            return result

        operand_stack = list(map(lambda ast: execute_branch(ast), self.operand_stack))
        operator_stack = list(map(lambda ast: execute_branch(ast), self.operator_stack))

        return "".join(map(str, operand_stack))

    @staticmethod
    def parse(branch: List[AST]):
        return ConcatExpression(branch)

    def __repr__(self):
        stack = []
        for a, b in zip(self.operand_stack, self.operator_stack):
            stack.append(a)
            stack.append(b)
        stack.append(self.operand_stack[-1])

        return " ".join(map(str, stack))
