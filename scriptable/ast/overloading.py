from typing import List, Any

from scriptable.api import AST
from scriptable.api.AST import ASTBinding
from scriptable.api.accessor import Accessor


class Overloading(AST[Any]):
    def __init__(self, branch: List[AST]):
        self.branch = branch

    def execute(self, context: ASTBinding) -> Any:
        def mapper(obj):
            if isinstance(obj, Accessor):
                return obj.value
            return obj

        branch = list(map(lambda x: x.execute(context), self.branch))
        branch = list(map(mapper, branch))

        return "".join(branch)

    @staticmethod
    def parse(branch: List[AST]) -> 'Overloading':
        return Overloading(branch)
