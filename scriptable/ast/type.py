from scriptable.antlr.TypescriptParser import TypescriptParser
from scriptable.api import AST
from scriptable.api.ast_binding import ASTBinding


class Type(AST[str]):

    def __init__(self, value: str):
        self.value = value

    def execute(self, context: ASTBinding) -> str:
        return self.value

    @staticmethod
    def parse(ctx: TypescriptParser.STypeContext):
        return Type(ctx.getText())