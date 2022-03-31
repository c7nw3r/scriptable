from scriptable.antlr.TypescriptParser import TypescriptParser
from scriptable.api import AST
from scriptable.api.ast_binding import ASTBinding


class Optional(AST[str]):

    def execute(self, context: ASTBinding) -> 'Optional':
        return self

    @staticmethod
    def parse(_ctx: TypescriptParser.SOptionalContext):
        return Optional()

    def __repr__(self):
        return "?"
