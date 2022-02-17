from scriptable.antlr.HypothesisVisitor import HypothesisVisitor
from scriptable.antlr.TypescriptParser import TypescriptParser
from scriptable.api.ast_restrictions import ASTRestrictions
from scriptable.ast.boolean import Boolean
from scriptable.ast.expression.arithmetic_expression import ArithmeticExpression
from scriptable.ast.expression.arithmetic_term import ArithmeticTerm
from scriptable.ast.expression.concat_expression import ConcatExpression
from scriptable.ast.expression.logic_expression import LogicExpression
from scriptable.ast.expression.logic_term import LogicTerm
from scriptable.ast.expression.operator import And, Or, Not, Plus, Minus, Mul, Div, Power, Equals, NotEquals, LowerThan
from scriptable.ast.expression.operator import LowerEquals, GreaterThan, GreaterEquals
from scriptable.ast.number import Number
from scriptable.ast.property.property import Property
from scriptable.ast.property.property_access import PropertyAccess
from scriptable.ast.type import Type
from scriptable.ast.value.array import Array
from scriptable.ast.value.map import Map
from scriptable.ast.value.string import String


class HypothesisVisitorImpl(HypothesisVisitor):

    def __init__(self, restrictions: ASTRestrictions):
        self.restrictions = restrictions

    def visitSNumber(self, ctx: TypescriptParser.SNumberContext):
        return Number.parse(ctx, self.restrictions)

    def visitSBoolean(self, ctx: TypescriptParser.SBooleanContext):
        return Boolean.parse(ctx)

    def visitSString(self, ctx: TypescriptParser.SStringContext):
        return String.parse(ctx)

    def visitSArray(self, ctx: TypescriptParser.SArrayContext):
        return Array.parse(super().visitSArray(ctx))

    def visitSMap(self, ctx: TypescriptParser.SMapContext):
        return Map.parse(super().visitSMap(ctx))

    def visitSArithmeticExpression(self, ctx: TypescriptParser.SArithmeticExpressionContext):
        return ArithmeticExpression.parse(super().visitSArithmeticExpression(ctx))

    def visitSArithmeticTerm(self, ctx: TypescriptParser.SArithmeticTermContext):
        return ArithmeticTerm.parse(super().visitSArithmeticTerm(ctx))

    def visitSBooleanTerm(self, ctx: TypescriptParser.SBooleanTermContext):
        return LogicTerm.parse(super().visitSBooleanTerm(ctx))

    def visitSBooleanExpression(self, ctx: TypescriptParser.SBooleanExpressionContext):
        return LogicExpression.parse(super().visitSBooleanExpression(ctx))

    def visitSNumberExpression(self, ctx: TypescriptParser.SNumberExpressionContext):
        return LogicExpression.parse(super().visitSNumberExpression(ctx))

    def visitSNumberTerm(self, ctx: TypescriptParser.SNumberTermContext):
        return LogicTerm.parse(super().visitSNumberTerm(ctx))

    def visitSStringExpression(self, ctx: TypescriptParser.SStringExpressionContext):
        return LogicExpression.parse(super().visitSStringExpression(ctx))

    def visitSConcatExpression(self, ctx: TypescriptParser.SConcatExpressionContext):
        return ConcatExpression.parse(super().visitSConcatExpression(ctx))

    def visitSStringTerm(self, ctx: TypescriptParser.SStringTermContext):
        return LogicTerm.parse(super().visitSStringTerm(ctx))

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

    def visitSEquals(self, ctx: TypescriptParser.SEqualsContext):
        return Equals()

    def visitSNotEquals(self, ctx: TypescriptParser.SNotEqualsContext):
        return NotEquals()

    def visitSLowerThan(self, ctx: TypescriptParser.SLowerThanContext):
        return LowerThan()

    def visitSLowerEquals(self, ctx: TypescriptParser.SLowerEqualsContext):
        return LowerEquals()

    def visitSGreaterThan(self, ctx: TypescriptParser.SGreaterThanContext):
        return GreaterThan()

    def visitSGreaterEquals(self, ctx: TypescriptParser.SGreaterEqualsContext):
        return GreaterEquals()

    def visitSProperty(self, ctx: TypescriptParser.SPropertyContext):
        return Property.parse(ctx)

    def visitSPropertyAccess(self, ctx: TypescriptParser.SPropertyAccessContext):
        return PropertyAccess.parse(super().visitSPropertyAccess(ctx))

    def visitSType(self, ctx: TypescriptParser.STypeContext):
        return Type.parse(ctx)

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
