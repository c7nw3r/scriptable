from typing import Union

from scriptable.antlr.TypescriptParser import TypescriptParser
from scriptable.api import AST
from scriptable.api.ast_binding import ASTBinding
from scriptable.api.ast_restrictions import ASTRestrictions

DataType = Union[int, float]


class Number(AST[DataType]):
    def __init__(self, value: DataType):
        self.value = value

    def execute(self, binding: ASTBinding) -> DataType:
        return self.value

    @staticmethod
    def parse(ctx: TypescriptParser.SNumberContext, settings: ASTRestrictions) -> 'Number':
        text = ctx.getText()
        assert len(text) <= settings.max_precision, f"max value precision exceeded"

        if "." in text:
            assert len(text[text.find("."):]) <= settings.max_scale, "max value scale exceeded"
            return Number(float(text))

        return Number(int(text))

    def __repr__(self):
        return str(self.value)
