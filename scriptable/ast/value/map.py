from typing import Any, List, Dict

from scriptable.api import AST
from scriptable.api.accessor import Accessor
from scriptable.api.ast_binding import ASTBinding
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
            value = branch[i + 1]
            _dict[branch[i].value] = value.value if isinstance(value, Accessor) else value
        return Map(MapAccessor(_dict))
