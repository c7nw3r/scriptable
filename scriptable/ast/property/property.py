from typing import Any

from scriptable.antlr.TypescriptParser import TypescriptParser
from scriptable.api import AST
from scriptable.api.ast_binding import ASTBinding


class Property(AST[Any]):
    def __init__(self, value: str, strict: bool = False):
        self.value = value
        self.strict = strict

    def execute(self, binding: ASTBinding) -> Any:
        if self.value in binding.properties:
            return binding.properties[self.value]
        if self.strict:
            raise ValueError(f"no property with name {self.value} found")
        return self.value

    @staticmethod
    def parse(ctx: TypescriptParser.SPropertyContext, strict: bool = False) -> 'Property':
        return Property(ctx.getText(), strict)

    def __repr__(self):
        return self.value
