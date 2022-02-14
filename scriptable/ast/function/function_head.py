from typing import List, Optional

from scriptable.api import AST
from scriptable.ast.function.function_arg_def import FunctionArgDef
from scriptable.ast.type import Type


class FunctionHead:
    def __init__(self, name: str, args: List[FunctionArgDef], r_type: Optional[AST]):
        self.name = name
        self.args = args
        self.r_type = r_type

    # noinspection PyTypeChecker
    @staticmethod
    def parse(name: str, branch: List[AST]) -> 'FunctionHead':
        if len(branch) > 0 and isinstance(branch[-1], Type):
            return FunctionHead(name, branch, branch[-1])
        return FunctionHead(name, branch, None)
