from typing import Any, List, Tuple

from scriptable.api import AST
from scriptable.api.AST import ASTBinding, SourceAwareContext
from scriptable.api.accessor import Accessor


class FunctionCall(AST[Tuple[str, List[Any]]]):
    def __init__(self, name: str, args: List[AST]):
        self.name = name
        self.args = args

    def execute(self, binding: ASTBinding) -> Tuple[str, List[Any]]:
        args = list(map(lambda x: x.execute(binding), self.args))

        if isinstance(binding, SourceAwareContext):
            source = binding.source
            if isinstance(source, Accessor):
                return source(self.name, args)
            if hasattr(source, self.name):
                return getattr(source, self.name)(*args)
            return source.__call__(*args)

        if self.name in binding.functions:
            from copy import deepcopy
            _binding = deepcopy(binding)

            # recursion guard
            # ***************
            signature = self.name + "(" + ", ".join(map(str, args)) + ")"
            assert _binding.add_signature(signature) > 1, "recursion loop determined"

            function = _binding.functions[self.name]
            return function(args, _binding)

        raise ValueError(f"cannot find function {self.name}")

    @staticmethod
    def parse(text: str, branch: List[AST]) -> 'FunctionCall':
        return FunctionCall(text, branch)

    def __repr__(self):
        return self.name + "(" + ", ".join(map(str, self.args)) + ")"
