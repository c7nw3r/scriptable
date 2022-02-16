from typing import List, Any

from scriptable.api import AST
from scriptable.api.ast_binding import ASTBinding
from scriptable.ast.function.function_arg_def import FunctionArgDef


class FunctionLambda(AST[Any]):
    def __init__(self, head: List[AST], tail: List[AST]):
        self.head = head
        self.tail = tail

    def execute(self, context: ASTBinding) -> Any:
        def callback(args):
            from copy import deepcopy
            _binding = deepcopy(context)

            for i, e in enumerate(self.head):
                arg_name = e.arg_name.value
                _binding.add_property(arg_name, args[i])

            return self.tail[0].execute(_binding)

        return callback

    @staticmethod
    def parse(branch: List[AST]) -> 'FunctionLambda':
        head = list(filter(lambda x: isinstance(x, FunctionArgDef), branch))
        tail = list(filter(lambda x: not isinstance(x, FunctionArgDef), branch))
        return FunctionLambda(head, tail)

    def __repr__(self):
        return str(self.head) + str(self.tail)
