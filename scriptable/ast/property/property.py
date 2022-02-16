from typing import Any

from scriptable.antlr.TypescriptParser import TypescriptParser
from scriptable.api import AST
from scriptable.api.ast_binding import ASTBinding


class Property(AST[Any]):
    def __init__(self, value: str):
        self.value = value

    def execute(self, binding: ASTBinding) -> Any:
        if self.value in binding.properties:
            return binding.properties[self.value]
        return self.value

    @staticmethod
    def parse(ctx: TypescriptParser.SPropertyContext) -> 'Property':
        return Property(ctx.getText())

    def __repr__(self):
        return self.value
