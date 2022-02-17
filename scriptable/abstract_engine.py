from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional

# noinspection PyUnresolvedReferences
from antlr4 import InputStream, CommonTokenStream

from scriptable.api import AST
from scriptable.api.accessor import Accessor
from scriptable.api.ast_restrictions import ASTRestrictions
from scriptable.api.exit_value import ExitValue
from scriptable.ast.number import Number
from scriptable.ast.value.array import Array
from scriptable.ast.value.map import Map
from scriptable.ast.value.string import String


class ScriptableEngine(ABC):

    def __init__(self, tree: List[AST], restrictions: ASTRestrictions):
        self.tree = tree
        self.restrictions = restrictions

    def execute(self, properties: Optional[dict] = None):
        properties = properties if properties is not None else {}

        def unwrap(obj):
            if isinstance(obj, List):
                return list(map(unwrap, obj))
            if isinstance(obj, Accessor):
                return unwrap(obj.value)
            if isinstance(obj, String):
                return obj.accessor.value
            if isinstance(obj, Number):
                return obj.value
            if isinstance(obj, Array):
                return unwrap(obj.accessor.value)
            if isinstance(obj, Map):
                return unwrap(obj.accessor.value)
            return obj

        binding = self._create_binding(properties, self.restrictions)
        result = None
        for branch in self.tree:
            result = branch.execute(binding)
            if isinstance(result, ExitValue):
                return unwrap(result.value)

        return unwrap(result)

    @abstractmethod
    def _create_binding(self, properties: Dict[str, Any], restrictions: ASTRestrictions):
        pass

    @staticmethod
    def stream(obj):
        if isinstance(obj, InputStream):
            return obj
        if isinstance(obj, str):
            return InputStream(str(obj))
        if isinstance(obj, bytes):
            return InputStream(obj.decode("utf-8"))
        if isinstance(obj, bytearray):
            return InputStream(obj.decode("utf-8"))
        raise ValueError(str(obj) + " cannot be converted to input stream")
