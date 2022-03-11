from typing import Dict, Any, Optional

# noinspection PyUnresolvedReferences
from antlr4 import InputStream, CommonTokenStream

from scriptable.abstract_engine import ScriptableEngine
from scriptable.antlr.MustacheLexer import MustacheLexer
from scriptable.antlr.MustacheParser import MustacheParser
from scriptable.api.ast_binding import ASTBinding
from scriptable.api.ast_restrictions import ASTRestrictions
from scriptable.listener.error_listener import ScriptableErrorListener
from scriptable.mustache_visitor import MustacheVisitorImpl


class MustacheEngine(ScriptableEngine):

    @staticmethod
    def parse(schema, restrictions: ASTRestrictions = ASTRestrictions()) -> 'MustacheEngine':
        lexer = MustacheLexer(MustacheEngine.stream(schema))
        stream = CommonTokenStream(lexer)
        parser = MustacheParser(stream)

        error_listener = ScriptableErrorListener()
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)
        lexer.removeErrorListeners()
        lexer.addErrorListener(error_listener)

        visitor = MustacheVisitorImpl(restrictions)
        tree = visitor.visit(parser.sAll())

        if len(error_listener.errors) > 0:
            raise ValueError(str(error_listener.errors[0]))

        return MustacheEngine(tree, restrictions)

    def execute(self, properties: Optional[dict] = None):
        properties = properties if properties is not None else {}
        return "".join([e.execute(ASTBinding(properties=properties)) for e in self.tree])

    def _create_binding(self, properties: Dict[str, Any], restrictions: ASTRestrictions):
        return ASTBinding(restrictions=restrictions, properties=properties)
