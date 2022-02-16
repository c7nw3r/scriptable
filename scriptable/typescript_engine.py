from typing import List, Dict, Any, Optional

# noinspection PyUnresolvedReferences
from antlr4 import InputStream, CommonTokenStream

from scriptable.antlr.TypescriptLexer import TypescriptLexer
from scriptable.antlr.TypescriptParser import TypescriptParser
from scriptable.api import AST
from scriptable.api.accessor import Accessor
from scriptable.api.ast_binding import ASTBinding
from scriptable.api.ast_restrictions import ASTRestrictions
from scriptable.api.exit_value import ExitValue
from scriptable.ast.number import Number
from scriptable.ast.value.array import Array
from scriptable.ast.value.map import Map
from scriptable.ast.value.string import String
from scriptable.runtime.buildin.typescript.console import Console
from scriptable.runtime.buildin.typescript.process import Process
from scriptable.typescript_visitor import TypescriptVisitorImpl


class TypescriptEngine:

    @staticmethod
    def parse(schema, restrictions: ASTRestrictions = ASTRestrictions()) -> 'TypescriptEngine':
        lexer = TypescriptLexer(TypescriptEngine.stream(schema))
        stream = CommonTokenStream(lexer)
        parser = TypescriptParser(stream)

        visitor = TypescriptVisitorImpl(restrictions)
        tree = visitor.visit(parser.sAll())

        return TypescriptEngine(tree, restrictions)

    def __init__(self, tree: List[AST], restrictions: ASTRestrictions):
        self.tree = tree
        self.restrictions = restrictions

    def execute(self, properties: Optional[Dict[str, Any]] = None):
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

    def _create_binding(self, properties: Dict[str, Any], restrictions: ASTRestrictions):
        binding = ASTBinding(restrictions=restrictions)
        binding.add_property("console", Console())
        binding.add_property("process", Process(properties))
        return binding

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
