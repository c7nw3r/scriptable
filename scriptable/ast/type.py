from scriptable.antlr.TypescriptParser import TypescriptParser
from scriptable.api import AST
from scriptable.api.AST import ASTBinding, T


class Type(AST[str]):

    def __init__(self, value: str):
        self.value = value

    def execute(self, context: ASTBinding) -> T:
        return self.value

    @staticmethod
    def parse(ctx: TypescriptParser.STypeContext):
        return Type(ctx.getText())