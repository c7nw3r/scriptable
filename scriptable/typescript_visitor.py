from scriptable.antlr.TypescriptParser import TypescriptParser
from scriptable.antlr.TypescriptVisitor import TypescriptVisitor
from scriptable.api.sandbox_settings import SandboxSettings
from scriptable.ast.boolean import Boolean
from scriptable.ast.expression.arithmetic_expression import ArithmeticExpression
from scriptable.ast.expression.logic_expression import LogicExpression
from scriptable.ast.expression.operator import And, Or, Not, Plus, Minus, Mul, Div, Power
from scriptable.ast.expression.term import Term
from scriptable.ast.number import Number


class TypescriptVisitorImpl(TypescriptVisitor):
    settings: SandboxSettings = SandboxSettings()

    def visitSNumber(self, ctx: TypescriptParser.SNumberContext):
        return Number.parse(ctx, self.settings)

    def visitSBoolean(self, ctx: TypescriptParser.SBooleanContext):
        return Boolean.parse(ctx)

    def visitSArithmeticExpression(self, ctx: TypescriptParser.SArithmeticExpressionContext):
        return ArithmeticExpression.parse(super().visitSArithmeticExpression(ctx))

    def visitSTerm(self, ctx: TypescriptParser.STermContext):
        return Term.parse(super().visitSTerm(ctx))

    def visitSAnd(self, ctx: TypescriptParser.SAndContext):
        return And()

    def visitSOr(self, ctx: TypescriptParser.SOrContext):
        return Or()

    def visitSNot(self, ctx: TypescriptParser.SNotContext):
        return Not()

    def visitSPlus(self, ctx: TypescriptParser.SPlusContext):
        return Plus()

    def visitSMinus(self, ctx: TypescriptParser.SMinusContext):
        return Minus()

    def visitSMul(self, ctx: TypescriptParser.SMulContext):
        return Mul()

    def visitSDiv(self, ctx: TypescriptParser.SDivContext):
        return Div()

    def visitSPower(self, ctx: TypescriptParser.SPowerContext):
        return Power()

    def visitSLogicExpression(self, ctx: TypescriptParser.SLogicExpressionContext):
        return LogicExpression.parse(super().visitSLogicExpression(ctx))

    def aggregateResult(self, aggregate, nextResult):
        array = []
        if aggregate is not None:
            array += aggregate
        if nextResult is not None:
            if isinstance(nextResult, list):
                array.extend(nextResult)
            else:
                array += [nextResult]
        return array
