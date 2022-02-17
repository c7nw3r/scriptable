from typing import Dict, Any

# noinspection PyUnresolvedReferences
from antlr4 import InputStream, CommonTokenStream

from scriptable.abstract_engine import ScriptableEngine
from scriptable.antlr.HypothesisLexer import HypothesisLexer
from scriptable.antlr.HypothesisParser import HypothesisParser
from scriptable.api.ast_binding import ASTBinding
from scriptable.api.ast_restrictions import ASTRestrictions
from scriptable.hypothesis_visitor import HypothesisVisitorImpl
from scriptable.listener.error_listener import ScriptableErrorListener


class HypothesisEngine(ScriptableEngine):

    @staticmethod
    def parse(schema, restrictions: ASTRestrictions = ASTRestrictions()) -> 'HypothesisEngine':
        lexer = HypothesisLexer(HypothesisEngine.stream(schema))
        stream = CommonTokenStream(lexer)
        parser = HypothesisParser(stream)

        error_listener = ScriptableErrorListener()
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)
        lexer.removeErrorListeners()
        lexer.addErrorListener(error_listener)

        visitor = HypothesisVisitorImpl(restrictions)
        tree = visitor.visit(parser.sAll())

        if len(error_listener.errors) > 0:
            raise ValueError(str(error_listener.errors[0]))

        return HypothesisEngine(tree, restrictions)

    def _create_binding(self, properties: Dict[str, Any], restrictions: ASTRestrictions):
        return ASTBinding(restrictions=restrictions, properties=properties)
