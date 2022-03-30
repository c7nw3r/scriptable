# noinspection PyUnresolvedReferences
from antlr4 import InputStream, CommonTokenStream

from scriptable.abstract_engine import ScriptableEngine
from scriptable.antlr.TypescriptLexer import TypescriptLexer
from scriptable.antlr.TypescriptParser import TypescriptParser
from scriptable.api.ast_binding import ASTBinding
from scriptable.api.ast_restrictions import ASTRestrictions
from scriptable.api.property_resolver import PropertySource
from scriptable.listener.error_listener import ScriptableErrorListener
from scriptable.runtime.buildin.typescript.console import Console
from scriptable.runtime.buildin.typescript.process import Process
from scriptable.typescript_visitor import TypescriptVisitorImpl


class TypescriptEngine(ScriptableEngine):

    @staticmethod
    def parse(schema, restrictions: ASTRestrictions = ASTRestrictions()) -> 'TypescriptEngine':
        lexer = TypescriptLexer(TypescriptEngine.stream(schema))
        stream = CommonTokenStream(lexer)
        parser = TypescriptParser(stream)

        error_listener = ScriptableErrorListener()
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)
        lexer.removeErrorListeners()
        lexer.addErrorListener(error_listener)

        visitor = TypescriptVisitorImpl(restrictions)
        tree = visitor.visit(parser.sAll())

        if len(error_listener.errors) > 0:
            raise ValueError(str(error_listener.errors[0]))

        return TypescriptEngine(tree, restrictions)

    def _create_binding(self, properties: PropertySource):
        binding = ASTBinding(restrictions=self.restrictions)
        binding.add_property("console", Console())
        binding.add_property("process", Process(properties))
        return binding
