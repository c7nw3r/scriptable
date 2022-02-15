from typing import List, Any

from scriptable.api import AST
from scriptable.api.AST import ASTBinding, T
from scriptable.api.exit_value import ExitValue


class FunctionTail(AST[Any]):
    def __init__(self, branch: List[AST]):
        self.branch = branch

    def execute(self, context: ASTBinding) -> T:
        def unwrap(obj):
            # if isinstance(obj, List):
            #     return list(map(unwrap, obj))
            # if isinstance(obj, Accessor):
            #     return unwrap(obj.value)
            # if isinstance(obj, String):
            #     return obj.accessor.value
            # if isinstance(obj, Number):
            #     return obj.value
            # if isinstance(obj, Array):
            #     return unwrap(obj.accessor.value)
            # if isinstance(obj, Map):
            #     return unwrap(obj.accessor.value)
            return obj

        result = None
        for branch in self.branch:
            result = branch.execute(context)
            if isinstance(result, ExitValue):
                return unwrap(result.value)

        return result

    @staticmethod
    def parse(branch: List[AST]) -> 'FunctionTail':
        return FunctionTail(branch)

    def __repr__(self):
        return " ".join(map(str, self.branch))
