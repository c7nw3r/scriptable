from typing import Any, List, Dict

from scriptable.api import AST
from scriptable.api.AST import ASTBinding
from scriptable.api.accessor import Accessor
from scriptable.runtime.accessor.typescript.map_accessor import MapAccessor


class Map(AST[Accessor[Dict[str, Any]]]):
    def __init__(self, accessor: Accessor[Dict[str, Any]]):
        self.accessor = accessor

    def execute(self, binding: ASTBinding) -> Accessor[Dict[str, Any]]:
        return self.accessor

    @staticmethod
    def parse(branch: List[AST]) -> 'Map':
        branch = list(map(lambda x: x.execute(ASTBinding()), branch))
        _dict = {}
        for i in range(0, len(branch), 2):
            _dict[branch[i].value] = branch[i + 1]
        return Map(MapAccessor(_dict))
