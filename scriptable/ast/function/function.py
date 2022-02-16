from typing import List

from scriptable.api import AST
from scriptable.api.ast_binding import ASTBinding
from scriptable.ast.function.function_head import FunctionHead
from scriptable.ast.function.function_tail import FunctionTail


class Function(AST[None]):
    def __init__(self, head: FunctionHead, tail: FunctionTail):
        self.head = head
        self.tail = tail

    def execute(self, context: ASTBinding) -> None:
        def execute_function(args, binding):
            from copy import deepcopy
            _binding = deepcopy(binding)

            for i, e in enumerate(self.head.args):
                arg_name = e.arg_name.value
                _binding.add_property(arg_name, args[i])

            return self.tail.execute(_binding)

        context.add_function(self.head.name, execute_function)
        return None

    @staticmethod
    def parse(branch: List[AST]) -> 'Function':
        # noinspection PyTypeChecker
        return Function(branch[0], branch[1])

    def __repr__(self):
        return str(self.head) + str(self.tail)
