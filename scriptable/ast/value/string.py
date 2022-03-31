from scriptable.antlr.TypescriptParser import TypescriptParser
from scriptable.api import AST
from scriptable.api.accessor import Accessor
from scriptable.api.ast_binding import ASTBinding
from scriptable.runtime.accessor.typescript.string_accessor import TypescriptStringAccessor


class String(AST[Accessor[str]]):
    def __init__(self, accessor: Accessor[str]):
        self.accessor = accessor

    def execute(self, binding: ASTBinding) -> Accessor[str]:
        return self.accessor

    @staticmethod
    def parse(ctx: TypescriptParser.SStringContext) -> 'String':
        return String(TypescriptStringAccessor(ctx.getText()[1:-1]))

    def __repr__(self):
        return f"'{self.accessor.value}'"