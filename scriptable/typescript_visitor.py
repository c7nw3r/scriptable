from scriptable.antlr.TypescriptParser import TypescriptParser
from scriptable.antlr.TypescriptVisitor import TypescriptVisitor
from scriptable.api.sandbox_settings import SandboxSettings
from scriptable.ast.Return import Return
from scriptable.ast.boolean import Boolean
from scriptable.ast.control.For import For
from scriptable.ast.control.ForIn import ForIn
from scriptable.ast.control.ForOf import ForOf
from scriptable.ast.control.While import While
from scriptable.ast.control.ifelse import If
from scriptable.ast.expression.arithmetic_expression import ArithmeticExpression
from scriptable.ast.expression.arithmetic_term import ArithmeticTerm
from scriptable.ast.expression.logic_expression import LogicExpression
from scriptable.ast.expression.logic_term import LogicTerm
from scriptable.ast.expression.operator import And, Or, Not, Plus, Minus, Mul, Div, Power, Equals, NotEquals, LowerThan, \
    LowerEquals, GreaterThan, GreaterEquals
from scriptable.ast.function.function import Function
from scriptable.ast.function.function_access import FunctionAccess
from scriptable.ast.function.function_arg import FunctionArg
from scriptable.ast.function.function_arg_def import FunctionArgDef
from scriptable.ast.function.function_call import FunctionCall
from scriptable.ast.function.function_head import FunctionHead
from scriptable.ast.function.function_lambda import FunctionLambda
from scriptable.ast.function.function_tail import FunctionTail
from scriptable.ast.number import Number
from scriptable.ast.overloading import Overloading
from scriptable.ast.property.property import Property
from scriptable.ast.property.property_access import PropertyAccess
from scriptable.ast.type import Type
from scriptable.ast.value.array import Array
from scriptable.ast.value.map import Map
from scriptable.ast.value.string import String
from scriptable.ast.variable.assignment import Assignment
from scriptable.ast.variable.decrement import Decrement
from scriptable.ast.variable.immutable_var import ImmutableVar
from scriptable.ast.variable.increment import Increment
from scriptable.ast.variable.mutable_var import MutableVar


class TypescriptVisitorImpl(TypescriptVisitor):
    settings: SandboxSettings = SandboxSettings()

    def visitSNumber(self, ctx: TypescriptParser.SNumberContext):
        return Number.parse(ctx, self.settings)

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

    def visitSFunctionCall(self, ctx: TypescriptParser.SFunctionCallContext):
        return FunctionCall.parse(ctx.getChild(0).getText(), super().visitSFunctionCall(ctx))

    def visitSFunctionAccess(self, ctx: TypescriptParser.SFunctionAccessContext):
        return FunctionAccess(super().visitSFunctionAccess(ctx))

    def visitSReturn(self, ctx: TypescriptParser.SReturnContext):
        return Return.parse(super().visitSReturn(ctx))

    def visitSIf(self, ctx: TypescriptParser.SIfContext):
        return If.parse(super().visitSIf(ctx))

    def visitSType(self, ctx: TypescriptParser.STypeContext):
        return Type.parse(ctx)

    def visitSFunctionArg(self, ctx: TypescriptParser.SFunctionArgContext):
        return FunctionArg.parse(super().visitSFunctionArg(ctx))

    def visitSFunctionArgDef(self, ctx: TypescriptParser.SFunctionArgDefContext):
        return FunctionArgDef.parse(super().visitSFunctionArgDef(ctx))

    def visitSFunctionHead(self, ctx: TypescriptParser.SFunctionHeadContext):
        return FunctionHead.parse(ctx.getChild(1).getText(), super().visitSFunctionHead(ctx))

    def visitSFunctionTail(self, ctx: TypescriptParser.SFunctionTailContext):
        return FunctionTail.parse(super().visitSFunctionTail(ctx))

    def visitSFunction(self, ctx: TypescriptParser.SFunctionContext):
        return Function.parse(super().visitSFunction(ctx))

    def visitSFunctionLambda(self, ctx: TypescriptParser.SFunctionLambdaContext):
        return FunctionLambda.parse(super().visitSFunctionLambda(ctx))

    def visitSOverloading(self, ctx: TypescriptParser.SOverloadingContext):
        return Overloading.parse(super().visitSOverloading(ctx))

    def visitSWhile(self, ctx: TypescriptParser.SWhileContext):
        return While.parse(super().visitSWhile(ctx))

    def visitSMutableVar(self, ctx: TypescriptParser.SMutableVarContext):
        return MutableVar.parse(ctx.getChild(1).getText(), super().visitSMutableVar(ctx)[0])

    def visitSImmutableVar(self, ctx: TypescriptParser.SImmutableVarContext):
        return ImmutableVar.parse(ctx.getChild(1).getText(), super().visitSImmutableVar(ctx)[0])

    def visitSAssignment(self, ctx: TypescriptParser.SAssignmentContext):
        return Assignment.parse(ctx.getChild(0).getText(), super().visitSAssignment(ctx)[0])

    def visitSEndlessLoop(self, ctx: TypescriptParser.SEndlessLoopContext):
        raise ValueError("endless loops are not supported")

    def visitSFor(self, ctx: TypescriptParser.SForContext):
        return For.parse(super().visitSFor(ctx))

    def visitSForOf(self, ctx: TypescriptParser.SForOfContext):
        return ForOf.parse(ctx.getChild(3).getText(), super().visitSForOf(ctx))

    def visitSForIn(self, ctx: TypescriptParser.SForInContext):
        return ForIn.parse(ctx.getChild(3).getText(), super().visitSForIn(ctx))

    def visitSIncrement(self, ctx: TypescriptParser.SIncrementContext):
        return Increment.parse(ctx.getChild(0).getText())

    def visitSDecrement(self, ctx: TypescriptParser.SDecrementContext):
        return Decrement.parse(ctx.getChild(0).getText())

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
