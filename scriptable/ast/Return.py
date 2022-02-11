from typing import List

from scriptable.api import AST
from scriptable.api.AST import ASTBinding
from scriptable.api.exit_value import ExitValue


class Return(AST[ExitValue]):
    def __init__(self, item: AST):
        self.item = item

    def execute(self, binding: ASTBinding) -> ExitValue:
        value = self.item.execute(binding)
        return ExitValue(0, value)

    @staticmethod
    def parse(branch: List[AST]) -> 'Return':
        return Return(branch[0])
