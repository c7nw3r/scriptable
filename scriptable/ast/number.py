from typing import Union

from scriptable.antlr.TypescriptParser import TypescriptParser
from scriptable.api import AST
from scriptable.api.AST import ASTBinding
from scriptable.api.sandbox_settings import SandboxSettings

DataType = Union[int, float]


class Number(AST[DataType]):
    def __init__(self, value: DataType):
        self.value = value

    def execute(self, binding: ASTBinding) -> DataType:
        return self.value

    @staticmethod
    def parse(ctx: TypescriptParser.SNumberContext, settings: SandboxSettings) -> 'Number':
        text = ctx.getText()
        assert len(text) <= settings.max_precision, f"max value precision exceeded"

        if "." in text:
            assert len(text[text.find("."):]) <= settings.max_scale, "max value scale exceeded"
            return Number(float(text))

        return Number(int(text))
