from scriptable.antlr.TypescriptParser import TypescriptParser
from scriptable.api import AST
from scriptable.api.ast_binding import ASTBinding


class Boolean(AST[bool]):
    def __init__(self, value: bool):
        self.value = value

    def execute(self, binding: ASTBinding) -> bool:
        return self.value

    @staticmethod
    def parse(ctx: TypescriptParser.SBooleanContext) -> 'Boolean':
        text = ctx.getText()
        return Boolean(text == "true")
