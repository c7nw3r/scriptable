from typing import Any, List

from scriptable.api import AST
from scriptable.api.AST import ASTBinding
from scriptable.api.accessor import Accessor
from scriptable.runtime.accessor.typescript.array_accessor import ArrayAccessor


class Array(AST[Accessor[List[Any]]]):
    def __init__(self, accessor: Accessor[str]):
        self.accessor = accessor

    def execute(self, binding: ASTBinding) -> Accessor[str]:
        return self.accessor

    @staticmethod
    def parse(branch: List[AST]) -> 'Array':
        return Array(ArrayAccessor(branch))
