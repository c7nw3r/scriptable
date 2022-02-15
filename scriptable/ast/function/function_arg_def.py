from typing import Any, List, Tuple, Optional

from scriptable.api import AST
from scriptable.api.AST import ASTBinding


class FunctionArgDef(AST[Any]):
    def __init__(self, arg_name: AST[Any], arg_type: Optional[AST[str]]):
        self.arg_name = arg_name
        self.arg_type = arg_type

    def execute(self, binding: ASTBinding) -> Tuple[str, List[Any]]:
        arg_name = self.arg_name.execute(binding)
        arg_type = self.arg_type.execute(binding)
        return arg_name

    @staticmethod
    def parse(branch: List[AST]) -> 'FunctionArgDef':
        return FunctionArgDef(branch[0], None if len(branch) == 1 else branch[1])

    def __repr__(self):
        return self.arg_name + "(" + str(self.arg_type) + ")"
