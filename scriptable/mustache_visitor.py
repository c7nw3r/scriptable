from typing import Any, List

from scriptable import AST
from scriptable.antlr.MustacheParser import MustacheParser
from scriptable.antlr.MustacheParserVisitor import MustacheParserVisitor
from scriptable.api import ASTBinding
from scriptable.api.ast_restrictions import ASTRestrictions
from scriptable.ast.property.property import Property


class MustacheVisitorImpl(MustacheParserVisitor):

    def __init__(self, restrictions: ASTRestrictions):
        self.restrictions = restrictions

    def visitSText(self, ctx: MustacheParser.STextContext):
        return Text(ctx.getText())

    def visitSProperty(self, ctx: MustacheParser.SPropertyContext):
        return Property(ctx.getText()[2:-2], True)

    def visitSTagStart(self, ctx: MustacheParser.STagStartContext):
        return Property(ctx.getText()[3:-2], True)

    def visitSTag(self, ctx: MustacheParser.STagContext):
        elements = super().visitSTag(ctx)
        return MustacheTag(elements)

    def aggregateResult(self, aggregate, next_result):
        array = []
        if aggregate is not None:
            array += aggregate
        if next_result is not None:
            if isinstance(next_result, list):
                array.extend(next_result)
            else:
                array += [next_result]
        return array


class Text(AST[str]):
    def __init__(self, value: str):
        self.value = value

    def execute(self, binding: ASTBinding) -> Any:
        return self.value


class MustacheTag(AST[str]):
    def __init__(self, branch: List[AST]):
        self.expr = branch[0]
        self.branch = branch[1:]

    def execute(self, binding: ASTBinding) -> Any:
        expr = self.expr.execute(binding)

        if isinstance(expr, bool):
            return "".join(e.execute(binding) for e in self.branch) if expr else ""
        elif isinstance(expr, list):
            def run_iteration(entry) -> str:
                new_binding = ASTBinding(properties={".":entry})
                return "".join([e.execute(new_binding) for e in self.branch])

            return "".join([run_iteration(e) for e in expr])
        else:
            raise ValueError("cannot execute mustache tag")
