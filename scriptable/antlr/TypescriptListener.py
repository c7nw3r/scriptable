# Generated from Typescript.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TypescriptParser import TypescriptParser
else:
    from TypescriptParser import TypescriptParser

# This class defines a complete listener for a parse tree produced by TypescriptParser.
class TypescriptListener(ParseTreeListener):

    # Enter a parse tree produced by TypescriptParser#sAll.
    def enterSAll(self, ctx:TypescriptParser.SAllContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sAll.
    def exitSAll(self, ctx:TypescriptParser.SAllContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sOperand.
    def enterSOperand(self, ctx:TypescriptParser.SOperandContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sOperand.
    def exitSOperand(self, ctx:TypescriptParser.SOperandContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sOperator.
    def enterSOperator(self, ctx:TypescriptParser.SOperatorContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sOperator.
    def exitSOperator(self, ctx:TypescriptParser.SOperatorContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sExpression.
    def enterSExpression(self, ctx:TypescriptParser.SExpressionContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sExpression.
    def exitSExpression(self, ctx:TypescriptParser.SExpressionContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sTerm.
    def enterSTerm(self, ctx:TypescriptParser.STermContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sTerm.
    def exitSTerm(self, ctx:TypescriptParser.STermContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sValue.
    def enterSValue(self, ctx:TypescriptParser.SValueContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sValue.
    def exitSValue(self, ctx:TypescriptParser.SValueContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sInvocation.
    def enterSInvocation(self, ctx:TypescriptParser.SInvocationContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sInvocation.
    def exitSInvocation(self, ctx:TypescriptParser.SInvocationContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sControl.
    def enterSControl(self, ctx:TypescriptParser.SControlContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sControl.
    def exitSControl(self, ctx:TypescriptParser.SControlContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sStatement.
    def enterSStatement(self, ctx:TypescriptParser.SStatementContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sStatement.
    def exitSStatement(self, ctx:TypescriptParser.SStatementContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sPlus.
    def enterSPlus(self, ctx:TypescriptParser.SPlusContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sPlus.
    def exitSPlus(self, ctx:TypescriptParser.SPlusContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sMinus.
    def enterSMinus(self, ctx:TypescriptParser.SMinusContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sMinus.
    def exitSMinus(self, ctx:TypescriptParser.SMinusContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sMul.
    def enterSMul(self, ctx:TypescriptParser.SMulContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sMul.
    def exitSMul(self, ctx:TypescriptParser.SMulContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sDiv.
    def enterSDiv(self, ctx:TypescriptParser.SDivContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sDiv.
    def exitSDiv(self, ctx:TypescriptParser.SDivContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sPower.
    def enterSPower(self, ctx:TypescriptParser.SPowerContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sPower.
    def exitSPower(self, ctx:TypescriptParser.SPowerContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sAnd.
    def enterSAnd(self, ctx:TypescriptParser.SAndContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sAnd.
    def exitSAnd(self, ctx:TypescriptParser.SAndContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sOr.
    def enterSOr(self, ctx:TypescriptParser.SOrContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sOr.
    def exitSOr(self, ctx:TypescriptParser.SOrContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sNot.
    def enterSNot(self, ctx:TypescriptParser.SNotContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sNot.
    def exitSNot(self, ctx:TypescriptParser.SNotContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sEquals.
    def enterSEquals(self, ctx:TypescriptParser.SEqualsContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sEquals.
    def exitSEquals(self, ctx:TypescriptParser.SEqualsContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sNotEquals.
    def enterSNotEquals(self, ctx:TypescriptParser.SNotEqualsContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sNotEquals.
    def exitSNotEquals(self, ctx:TypescriptParser.SNotEqualsContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sLowerThan.
    def enterSLowerThan(self, ctx:TypescriptParser.SLowerThanContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sLowerThan.
    def exitSLowerThan(self, ctx:TypescriptParser.SLowerThanContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sLowerEquals.
    def enterSLowerEquals(self, ctx:TypescriptParser.SLowerEqualsContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sLowerEquals.
    def exitSLowerEquals(self, ctx:TypescriptParser.SLowerEqualsContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sGreaterThan.
    def enterSGreaterThan(self, ctx:TypescriptParser.SGreaterThanContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sGreaterThan.
    def exitSGreaterThan(self, ctx:TypescriptParser.SGreaterThanContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sGreaterEquals.
    def enterSGreaterEquals(self, ctx:TypescriptParser.SGreaterEqualsContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sGreaterEquals.
    def exitSGreaterEquals(self, ctx:TypescriptParser.SGreaterEqualsContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sArithmeticExpression.
    def enterSArithmeticExpression(self, ctx:TypescriptParser.SArithmeticExpressionContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sArithmeticExpression.
    def exitSArithmeticExpression(self, ctx:TypescriptParser.SArithmeticExpressionContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sArithmeticTerm.
    def enterSArithmeticTerm(self, ctx:TypescriptParser.SArithmeticTermContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sArithmeticTerm.
    def exitSArithmeticTerm(self, ctx:TypescriptParser.SArithmeticTermContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sBooleanOperand.
    def enterSBooleanOperand(self, ctx:TypescriptParser.SBooleanOperandContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sBooleanOperand.
    def exitSBooleanOperand(self, ctx:TypescriptParser.SBooleanOperandContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sBooleanOperator.
    def enterSBooleanOperator(self, ctx:TypescriptParser.SBooleanOperatorContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sBooleanOperator.
    def exitSBooleanOperator(self, ctx:TypescriptParser.SBooleanOperatorContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sBooleanExpression.
    def enterSBooleanExpression(self, ctx:TypescriptParser.SBooleanExpressionContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sBooleanExpression.
    def exitSBooleanExpression(self, ctx:TypescriptParser.SBooleanExpressionContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sBooleanTerm.
    def enterSBooleanTerm(self, ctx:TypescriptParser.SBooleanTermContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sBooleanTerm.
    def exitSBooleanTerm(self, ctx:TypescriptParser.SBooleanTermContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sNumberOperand.
    def enterSNumberOperand(self, ctx:TypescriptParser.SNumberOperandContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sNumberOperand.
    def exitSNumberOperand(self, ctx:TypescriptParser.SNumberOperandContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sNumberOperator.
    def enterSNumberOperator(self, ctx:TypescriptParser.SNumberOperatorContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sNumberOperator.
    def exitSNumberOperator(self, ctx:TypescriptParser.SNumberOperatorContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sNumberExpression.
    def enterSNumberExpression(self, ctx:TypescriptParser.SNumberExpressionContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sNumberExpression.
    def exitSNumberExpression(self, ctx:TypescriptParser.SNumberExpressionContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sNumberTerm.
    def enterSNumberTerm(self, ctx:TypescriptParser.SNumberTermContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sNumberTerm.
    def exitSNumberTerm(self, ctx:TypescriptParser.SNumberTermContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sStringOperand.
    def enterSStringOperand(self, ctx:TypescriptParser.SStringOperandContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sStringOperand.
    def exitSStringOperand(self, ctx:TypescriptParser.SStringOperandContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sStringOperator.
    def enterSStringOperator(self, ctx:TypescriptParser.SStringOperatorContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sStringOperator.
    def exitSStringOperator(self, ctx:TypescriptParser.SStringOperatorContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sStringExpression.
    def enterSStringExpression(self, ctx:TypescriptParser.SStringExpressionContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sStringExpression.
    def exitSStringExpression(self, ctx:TypescriptParser.SStringExpressionContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sStringTerm.
    def enterSStringTerm(self, ctx:TypescriptParser.SStringTermContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sStringTerm.
    def exitSStringTerm(self, ctx:TypescriptParser.SStringTermContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sConcatOperand.
    def enterSConcatOperand(self, ctx:TypescriptParser.SConcatOperandContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sConcatOperand.
    def exitSConcatOperand(self, ctx:TypescriptParser.SConcatOperandContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sConcatExpression.
    def enterSConcatExpression(self, ctx:TypescriptParser.SConcatExpressionContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sConcatExpression.
    def exitSConcatExpression(self, ctx:TypescriptParser.SConcatExpressionContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sConcatLeft.
    def enterSConcatLeft(self, ctx:TypescriptParser.SConcatLeftContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sConcatLeft.
    def exitSConcatLeft(self, ctx:TypescriptParser.SConcatLeftContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sConcatRight.
    def enterSConcatRight(self, ctx:TypescriptParser.SConcatRightContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sConcatRight.
    def exitSConcatRight(self, ctx:TypescriptParser.SConcatRightContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sConcatBoth.
    def enterSConcatBoth(self, ctx:TypescriptParser.SConcatBothContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sConcatBoth.
    def exitSConcatBoth(self, ctx:TypescriptParser.SConcatBothContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sType.
    def enterSType(self, ctx:TypescriptParser.STypeContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sType.
    def exitSType(self, ctx:TypescriptParser.STypeContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sOptional.
    def enterSOptional(self, ctx:TypescriptParser.SOptionalContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sOptional.
    def exitSOptional(self, ctx:TypescriptParser.SOptionalContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sPropertyDelete.
    def enterSPropertyDelete(self, ctx:TypescriptParser.SPropertyDeleteContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sPropertyDelete.
    def exitSPropertyDelete(self, ctx:TypescriptParser.SPropertyDeleteContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sFunction.
    def enterSFunction(self, ctx:TypescriptParser.SFunctionContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sFunction.
    def exitSFunction(self, ctx:TypescriptParser.SFunctionContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sFunctionArg.
    def enterSFunctionArg(self, ctx:TypescriptParser.SFunctionArgContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sFunctionArg.
    def exitSFunctionArg(self, ctx:TypescriptParser.SFunctionArgContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sFunctionArgs.
    def enterSFunctionArgs(self, ctx:TypescriptParser.SFunctionArgsContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sFunctionArgs.
    def exitSFunctionArgs(self, ctx:TypescriptParser.SFunctionArgsContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sFunctionArgDef.
    def enterSFunctionArgDef(self, ctx:TypescriptParser.SFunctionArgDefContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sFunctionArgDef.
    def exitSFunctionArgDef(self, ctx:TypescriptParser.SFunctionArgDefContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sFunctionArgDefs.
    def enterSFunctionArgDefs(self, ctx:TypescriptParser.SFunctionArgDefsContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sFunctionArgDefs.
    def exitSFunctionArgDefs(self, ctx:TypescriptParser.SFunctionArgDefsContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sFunctionHead.
    def enterSFunctionHead(self, ctx:TypescriptParser.SFunctionHeadContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sFunctionHead.
    def exitSFunctionHead(self, ctx:TypescriptParser.SFunctionHeadContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sFunctionTail.
    def enterSFunctionTail(self, ctx:TypescriptParser.SFunctionTailContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sFunctionTail.
    def exitSFunctionTail(self, ctx:TypescriptParser.SFunctionTailContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sFunctionCall.
    def enterSFunctionCall(self, ctx:TypescriptParser.SFunctionCallContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sFunctionCall.
    def exitSFunctionCall(self, ctx:TypescriptParser.SFunctionCallContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sFunctionLambda.
    def enterSFunctionLambda(self, ctx:TypescriptParser.SFunctionLambdaContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sFunctionLambda.
    def exitSFunctionLambda(self, ctx:TypescriptParser.SFunctionLambdaContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sProperty.
    def enterSProperty(self, ctx:TypescriptParser.SPropertyContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sProperty.
    def exitSProperty(self, ctx:TypescriptParser.SPropertyContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sPropertyAware.
    def enterSPropertyAware(self, ctx:TypescriptParser.SPropertyAwareContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sPropertyAware.
    def exitSPropertyAware(self, ctx:TypescriptParser.SPropertyAwareContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sPropertyAccess.
    def enterSPropertyAccess(self, ctx:TypescriptParser.SPropertyAccessContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sPropertyAccess.
    def exitSPropertyAccess(self, ctx:TypescriptParser.SPropertyAccessContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sFunctionAware.
    def enterSFunctionAware(self, ctx:TypescriptParser.SFunctionAwareContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sFunctionAware.
    def exitSFunctionAware(self, ctx:TypescriptParser.SFunctionAwareContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sFunctionAccess.
    def enterSFunctionAccess(self, ctx:TypescriptParser.SFunctionAccessContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sFunctionAccess.
    def exitSFunctionAccess(self, ctx:TypescriptParser.SFunctionAccessContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sLine.
    def enterSLine(self, ctx:TypescriptParser.SLineContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sLine.
    def exitSLine(self, ctx:TypescriptParser.SLineContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sBody.
    def enterSBody(self, ctx:TypescriptParser.SBodyContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sBody.
    def exitSBody(self, ctx:TypescriptParser.SBodyContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sReturn.
    def enterSReturn(self, ctx:TypescriptParser.SReturnContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sReturn.
    def exitSReturn(self, ctx:TypescriptParser.SReturnContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sIf.
    def enterSIf(self, ctx:TypescriptParser.SIfContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sIf.
    def exitSIf(self, ctx:TypescriptParser.SIfContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sElse.
    def enterSElse(self, ctx:TypescriptParser.SElseContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sElse.
    def exitSElse(self, ctx:TypescriptParser.SElseContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sElseIf.
    def enterSElseIf(self, ctx:TypescriptParser.SElseIfContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sElseIf.
    def exitSElseIf(self, ctx:TypescriptParser.SElseIfContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sString.
    def enterSString(self, ctx:TypescriptParser.SStringContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sString.
    def exitSString(self, ctx:TypescriptParser.SStringContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sNumber.
    def enterSNumber(self, ctx:TypescriptParser.SNumberContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sNumber.
    def exitSNumber(self, ctx:TypescriptParser.SNumberContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sBoolean.
    def enterSBoolean(self, ctx:TypescriptParser.SBooleanContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sBoolean.
    def exitSBoolean(self, ctx:TypescriptParser.SBooleanContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sArray.
    def enterSArray(self, ctx:TypescriptParser.SArrayContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sArray.
    def exitSArray(self, ctx:TypescriptParser.SArrayContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sMap.
    def enterSMap(self, ctx:TypescriptParser.SMapContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sMap.
    def exitSMap(self, ctx:TypescriptParser.SMapContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sEndlessLoop.
    def enterSEndlessLoop(self, ctx:TypescriptParser.SEndlessLoopContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sEndlessLoop.
    def exitSEndlessLoop(self, ctx:TypescriptParser.SEndlessLoopContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sWhile.
    def enterSWhile(self, ctx:TypescriptParser.SWhileContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sWhile.
    def exitSWhile(self, ctx:TypescriptParser.SWhileContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sFor.
    def enterSFor(self, ctx:TypescriptParser.SForContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sFor.
    def exitSFor(self, ctx:TypescriptParser.SForContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sForOf.
    def enterSForOf(self, ctx:TypescriptParser.SForOfContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sForOf.
    def exitSForOf(self, ctx:TypescriptParser.SForOfContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sForIn.
    def enterSForIn(self, ctx:TypescriptParser.SForInContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sForIn.
    def exitSForIn(self, ctx:TypescriptParser.SForInContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sLoopTail.
    def enterSLoopTail(self, ctx:TypescriptParser.SLoopTailContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sLoopTail.
    def exitSLoopTail(self, ctx:TypescriptParser.SLoopTailContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sContinue.
    def enterSContinue(self, ctx:TypescriptParser.SContinueContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sContinue.
    def exitSContinue(self, ctx:TypescriptParser.SContinueContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sBreak.
    def enterSBreak(self, ctx:TypescriptParser.SBreakContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sBreak.
    def exitSBreak(self, ctx:TypescriptParser.SBreakContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sMutableVar.
    def enterSMutableVar(self, ctx:TypescriptParser.SMutableVarContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sMutableVar.
    def exitSMutableVar(self, ctx:TypescriptParser.SMutableVarContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sImmutableVar.
    def enterSImmutableVar(self, ctx:TypescriptParser.SImmutableVarContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sImmutableVar.
    def exitSImmutableVar(self, ctx:TypescriptParser.SImmutableVarContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sAssignment.
    def enterSAssignment(self, ctx:TypescriptParser.SAssignmentContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sAssignment.
    def exitSAssignment(self, ctx:TypescriptParser.SAssignmentContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sIncrement.
    def enterSIncrement(self, ctx:TypescriptParser.SIncrementContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sIncrement.
    def exitSIncrement(self, ctx:TypescriptParser.SIncrementContext):
        pass


    # Enter a parse tree produced by TypescriptParser#sDecrement.
    def enterSDecrement(self, ctx:TypescriptParser.SDecrementContext):
        pass

    # Exit a parse tree produced by TypescriptParser#sDecrement.
    def exitSDecrement(self, ctx:TypescriptParser.SDecrementContext):
        pass



del TypescriptParser