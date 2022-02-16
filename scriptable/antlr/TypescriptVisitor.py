# Generated from Typescript.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TypescriptParser import TypescriptParser
else:
    from TypescriptParser import TypescriptParser

# This class defines a complete generic visitor for a parse tree produced by TypescriptParser.

class TypescriptVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TypescriptParser#sAll.
    def visitSAll(self, ctx:TypescriptParser.SAllContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sOperand.
    def visitSOperand(self, ctx:TypescriptParser.SOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sOperator.
    def visitSOperator(self, ctx:TypescriptParser.SOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sExpression.
    def visitSExpression(self, ctx:TypescriptParser.SExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sTerm.
    def visitSTerm(self, ctx:TypescriptParser.STermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sValue.
    def visitSValue(self, ctx:TypescriptParser.SValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sInvocation.
    def visitSInvocation(self, ctx:TypescriptParser.SInvocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sControl.
    def visitSControl(self, ctx:TypescriptParser.SControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sStatement.
    def visitSStatement(self, ctx:TypescriptParser.SStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sPlus.
    def visitSPlus(self, ctx:TypescriptParser.SPlusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sMinus.
    def visitSMinus(self, ctx:TypescriptParser.SMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sMul.
    def visitSMul(self, ctx:TypescriptParser.SMulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sDiv.
    def visitSDiv(self, ctx:TypescriptParser.SDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sPower.
    def visitSPower(self, ctx:TypescriptParser.SPowerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sAnd.
    def visitSAnd(self, ctx:TypescriptParser.SAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sOr.
    def visitSOr(self, ctx:TypescriptParser.SOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sNot.
    def visitSNot(self, ctx:TypescriptParser.SNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sEquals.
    def visitSEquals(self, ctx:TypescriptParser.SEqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sNotEquals.
    def visitSNotEquals(self, ctx:TypescriptParser.SNotEqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sLowerThan.
    def visitSLowerThan(self, ctx:TypescriptParser.SLowerThanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sLowerEquals.
    def visitSLowerEquals(self, ctx:TypescriptParser.SLowerEqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sGreaterThan.
    def visitSGreaterThan(self, ctx:TypescriptParser.SGreaterThanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sGreaterEquals.
    def visitSGreaterEquals(self, ctx:TypescriptParser.SGreaterEqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sArithmeticExpression.
    def visitSArithmeticExpression(self, ctx:TypescriptParser.SArithmeticExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sArithmeticTerm.
    def visitSArithmeticTerm(self, ctx:TypescriptParser.SArithmeticTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sBooleanOperand.
    def visitSBooleanOperand(self, ctx:TypescriptParser.SBooleanOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sBooleanOperator.
    def visitSBooleanOperator(self, ctx:TypescriptParser.SBooleanOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sBooleanExpression.
    def visitSBooleanExpression(self, ctx:TypescriptParser.SBooleanExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sBooleanTerm.
    def visitSBooleanTerm(self, ctx:TypescriptParser.SBooleanTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sNumberOperand.
    def visitSNumberOperand(self, ctx:TypescriptParser.SNumberOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sNumberOperator.
    def visitSNumberOperator(self, ctx:TypescriptParser.SNumberOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sNumberExpression.
    def visitSNumberExpression(self, ctx:TypescriptParser.SNumberExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sNumberTerm.
    def visitSNumberTerm(self, ctx:TypescriptParser.SNumberTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sStringOperand.
    def visitSStringOperand(self, ctx:TypescriptParser.SStringOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sStringOperator.
    def visitSStringOperator(self, ctx:TypescriptParser.SStringOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sStringExpression.
    def visitSStringExpression(self, ctx:TypescriptParser.SStringExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sStringTerm.
    def visitSStringTerm(self, ctx:TypescriptParser.SStringTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sConcatOperand.
    def visitSConcatOperand(self, ctx:TypescriptParser.SConcatOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sConcatExpression.
    def visitSConcatExpression(self, ctx:TypescriptParser.SConcatExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sConcatLeft.
    def visitSConcatLeft(self, ctx:TypescriptParser.SConcatLeftContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sConcatRight.
    def visitSConcatRight(self, ctx:TypescriptParser.SConcatRightContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sConcatBoth.
    def visitSConcatBoth(self, ctx:TypescriptParser.SConcatBothContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sType.
    def visitSType(self, ctx:TypescriptParser.STypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sFunction.
    def visitSFunction(self, ctx:TypescriptParser.SFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sFunctionArg.
    def visitSFunctionArg(self, ctx:TypescriptParser.SFunctionArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sFunctionArgs.
    def visitSFunctionArgs(self, ctx:TypescriptParser.SFunctionArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sFunctionArgDef.
    def visitSFunctionArgDef(self, ctx:TypescriptParser.SFunctionArgDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sFunctionArgDefs.
    def visitSFunctionArgDefs(self, ctx:TypescriptParser.SFunctionArgDefsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sFunctionHead.
    def visitSFunctionHead(self, ctx:TypescriptParser.SFunctionHeadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sFunctionTail.
    def visitSFunctionTail(self, ctx:TypescriptParser.SFunctionTailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sFunctionCall.
    def visitSFunctionCall(self, ctx:TypescriptParser.SFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sFunctionLambda.
    def visitSFunctionLambda(self, ctx:TypescriptParser.SFunctionLambdaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sProperty.
    def visitSProperty(self, ctx:TypescriptParser.SPropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sPropertyAware.
    def visitSPropertyAware(self, ctx:TypescriptParser.SPropertyAwareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sPropertyAccess.
    def visitSPropertyAccess(self, ctx:TypescriptParser.SPropertyAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sFunctionAware.
    def visitSFunctionAware(self, ctx:TypescriptParser.SFunctionAwareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sFunctionAccess.
    def visitSFunctionAccess(self, ctx:TypescriptParser.SFunctionAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sLine.
    def visitSLine(self, ctx:TypescriptParser.SLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sBody.
    def visitSBody(self, ctx:TypescriptParser.SBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sReturn.
    def visitSReturn(self, ctx:TypescriptParser.SReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sIf.
    def visitSIf(self, ctx:TypescriptParser.SIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sElse.
    def visitSElse(self, ctx:TypescriptParser.SElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sElseIf.
    def visitSElseIf(self, ctx:TypescriptParser.SElseIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sString.
    def visitSString(self, ctx:TypescriptParser.SStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sNumber.
    def visitSNumber(self, ctx:TypescriptParser.SNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sBoolean.
    def visitSBoolean(self, ctx:TypescriptParser.SBooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sArray.
    def visitSArray(self, ctx:TypescriptParser.SArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sMap.
    def visitSMap(self, ctx:TypescriptParser.SMapContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sEndlessLoop.
    def visitSEndlessLoop(self, ctx:TypescriptParser.SEndlessLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sWhile.
    def visitSWhile(self, ctx:TypescriptParser.SWhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sFor.
    def visitSFor(self, ctx:TypescriptParser.SForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sForOf.
    def visitSForOf(self, ctx:TypescriptParser.SForOfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sForIn.
    def visitSForIn(self, ctx:TypescriptParser.SForInContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sLoopTail.
    def visitSLoopTail(self, ctx:TypescriptParser.SLoopTailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sContinue.
    def visitSContinue(self, ctx:TypescriptParser.SContinueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sBreak.
    def visitSBreak(self, ctx:TypescriptParser.SBreakContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sMutableVar.
    def visitSMutableVar(self, ctx:TypescriptParser.SMutableVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sImmutableVar.
    def visitSImmutableVar(self, ctx:TypescriptParser.SImmutableVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sAssignment.
    def visitSAssignment(self, ctx:TypescriptParser.SAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sIncrement.
    def visitSIncrement(self, ctx:TypescriptParser.SIncrementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypescriptParser#sDecrement.
    def visitSDecrement(self, ctx:TypescriptParser.SDecrementContext):
        return self.visitChildren(ctx)



del TypescriptParser