from typing import List

# noinspection PyUnresolvedReferences
from antlr4 import InputStream, CommonTokenStream

from scriptable.antlr.TypescriptLexer import TypescriptLexer
from scriptable.antlr.TypescriptParser import TypescriptParser
from scriptable.api import AST
from scriptable.api.AST import ASTBinding
from scriptable.typescript_visitor import TypescriptVisitorImpl


class TypescriptEngine:

    @staticmethod
    def parse(schema) -> 'TypescriptEngine':
        lexer = TypescriptLexer(TypescriptEngine.stream(schema))
        stream = CommonTokenStream(lexer)
        parser = TypescriptParser(stream)

        visitor = TypescriptVisitorImpl()
        tree = visitor.visit(parser.sAll())

        return TypescriptEngine(tree)

    def __init__(self, tree: List[AST]):
        self.tree = tree

    def execute(self):
        return self.tree[0].execute(ASTBinding())

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
