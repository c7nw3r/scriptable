# Generated from Hypothesis.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .HypothesisParser import HypothesisParser
else:
    from HypothesisParser import HypothesisParser

# This class defines a complete listener for a parse tree produced by HypothesisParser.
class HypothesisListener(ParseTreeListener):

    # Enter a parse tree produced by HypothesisParser#sAll.
    def enterSAll(self, ctx:HypothesisParser.SAllContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sAll.
    def exitSAll(self, ctx:HypothesisParser.SAllContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sOperand.
    def enterSOperand(self, ctx:HypothesisParser.SOperandContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sOperand.
    def exitSOperand(self, ctx:HypothesisParser.SOperandContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sOperator.
    def enterSOperator(self, ctx:HypothesisParser.SOperatorContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sOperator.
    def exitSOperator(self, ctx:HypothesisParser.SOperatorContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sExpression.
    def enterSExpression(self, ctx:HypothesisParser.SExpressionContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sExpression.
    def exitSExpression(self, ctx:HypothesisParser.SExpressionContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sTerm.
    def enterSTerm(self, ctx:HypothesisParser.STermContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sTerm.
    def exitSTerm(self, ctx:HypothesisParser.STermContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sValue.
    def enterSValue(self, ctx:HypothesisParser.SValueContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sValue.
    def exitSValue(self, ctx:HypothesisParser.SValueContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sPlus.
    def enterSPlus(self, ctx:HypothesisParser.SPlusContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sPlus.
    def exitSPlus(self, ctx:HypothesisParser.SPlusContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sMinus.
    def enterSMinus(self, ctx:HypothesisParser.SMinusContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sMinus.
    def exitSMinus(self, ctx:HypothesisParser.SMinusContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sMul.
    def enterSMul(self, ctx:HypothesisParser.SMulContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sMul.
    def exitSMul(self, ctx:HypothesisParser.SMulContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sDiv.
    def enterSDiv(self, ctx:HypothesisParser.SDivContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sDiv.
    def exitSDiv(self, ctx:HypothesisParser.SDivContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sPower.
    def enterSPower(self, ctx:HypothesisParser.SPowerContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sPower.
    def exitSPower(self, ctx:HypothesisParser.SPowerContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sAnd.
    def enterSAnd(self, ctx:HypothesisParser.SAndContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sAnd.
    def exitSAnd(self, ctx:HypothesisParser.SAndContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sOr.
    def enterSOr(self, ctx:HypothesisParser.SOrContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sOr.
    def exitSOr(self, ctx:HypothesisParser.SOrContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sNot.
    def enterSNot(self, ctx:HypothesisParser.SNotContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sNot.
    def exitSNot(self, ctx:HypothesisParser.SNotContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sEquals.
    def enterSEquals(self, ctx:HypothesisParser.SEqualsContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sEquals.
    def exitSEquals(self, ctx:HypothesisParser.SEqualsContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sNotEquals.
    def enterSNotEquals(self, ctx:HypothesisParser.SNotEqualsContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sNotEquals.
    def exitSNotEquals(self, ctx:HypothesisParser.SNotEqualsContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sLowerThan.
    def enterSLowerThan(self, ctx:HypothesisParser.SLowerThanContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sLowerThan.
    def exitSLowerThan(self, ctx:HypothesisParser.SLowerThanContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sLowerEquals.
    def enterSLowerEquals(self, ctx:HypothesisParser.SLowerEqualsContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sLowerEquals.
    def exitSLowerEquals(self, ctx:HypothesisParser.SLowerEqualsContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sGreaterThan.
    def enterSGreaterThan(self, ctx:HypothesisParser.SGreaterThanContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sGreaterThan.
    def exitSGreaterThan(self, ctx:HypothesisParser.SGreaterThanContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sGreaterEquals.
    def enterSGreaterEquals(self, ctx:HypothesisParser.SGreaterEqualsContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sGreaterEquals.
    def exitSGreaterEquals(self, ctx:HypothesisParser.SGreaterEqualsContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sArithmeticExpression.
    def enterSArithmeticExpression(self, ctx:HypothesisParser.SArithmeticExpressionContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sArithmeticExpression.
    def exitSArithmeticExpression(self, ctx:HypothesisParser.SArithmeticExpressionContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sArithmeticTerm.
    def enterSArithmeticTerm(self, ctx:HypothesisParser.SArithmeticTermContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sArithmeticTerm.
    def exitSArithmeticTerm(self, ctx:HypothesisParser.SArithmeticTermContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sBooleanOperand.
    def enterSBooleanOperand(self, ctx:HypothesisParser.SBooleanOperandContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sBooleanOperand.
    def exitSBooleanOperand(self, ctx:HypothesisParser.SBooleanOperandContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sBooleanOperator.
    def enterSBooleanOperator(self, ctx:HypothesisParser.SBooleanOperatorContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sBooleanOperator.
    def exitSBooleanOperator(self, ctx:HypothesisParser.SBooleanOperatorContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sBooleanExpression.
    def enterSBooleanExpression(self, ctx:HypothesisParser.SBooleanExpressionContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sBooleanExpression.
    def exitSBooleanExpression(self, ctx:HypothesisParser.SBooleanExpressionContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sBooleanTerm.
    def enterSBooleanTerm(self, ctx:HypothesisParser.SBooleanTermContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sBooleanTerm.
    def exitSBooleanTerm(self, ctx:HypothesisParser.SBooleanTermContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sNumberOperand.
    def enterSNumberOperand(self, ctx:HypothesisParser.SNumberOperandContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sNumberOperand.
    def exitSNumberOperand(self, ctx:HypothesisParser.SNumberOperandContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sNumberOperator.
    def enterSNumberOperator(self, ctx:HypothesisParser.SNumberOperatorContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sNumberOperator.
    def exitSNumberOperator(self, ctx:HypothesisParser.SNumberOperatorContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sNumberExpression.
    def enterSNumberExpression(self, ctx:HypothesisParser.SNumberExpressionContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sNumberExpression.
    def exitSNumberExpression(self, ctx:HypothesisParser.SNumberExpressionContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sNumberTerm.
    def enterSNumberTerm(self, ctx:HypothesisParser.SNumberTermContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sNumberTerm.
    def exitSNumberTerm(self, ctx:HypothesisParser.SNumberTermContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sStringOperand.
    def enterSStringOperand(self, ctx:HypothesisParser.SStringOperandContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sStringOperand.
    def exitSStringOperand(self, ctx:HypothesisParser.SStringOperandContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sStringOperator.
    def enterSStringOperator(self, ctx:HypothesisParser.SStringOperatorContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sStringOperator.
    def exitSStringOperator(self, ctx:HypothesisParser.SStringOperatorContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sStringExpression.
    def enterSStringExpression(self, ctx:HypothesisParser.SStringExpressionContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sStringExpression.
    def exitSStringExpression(self, ctx:HypothesisParser.SStringExpressionContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sStringTerm.
    def enterSStringTerm(self, ctx:HypothesisParser.SStringTermContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sStringTerm.
    def exitSStringTerm(self, ctx:HypothesisParser.SStringTermContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sConcatOperand.
    def enterSConcatOperand(self, ctx:HypothesisParser.SConcatOperandContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sConcatOperand.
    def exitSConcatOperand(self, ctx:HypothesisParser.SConcatOperandContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sConcatExpression.
    def enterSConcatExpression(self, ctx:HypothesisParser.SConcatExpressionContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sConcatExpression.
    def exitSConcatExpression(self, ctx:HypothesisParser.SConcatExpressionContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sConcatLeft.
    def enterSConcatLeft(self, ctx:HypothesisParser.SConcatLeftContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sConcatLeft.
    def exitSConcatLeft(self, ctx:HypothesisParser.SConcatLeftContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sConcatRight.
    def enterSConcatRight(self, ctx:HypothesisParser.SConcatRightContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sConcatRight.
    def exitSConcatRight(self, ctx:HypothesisParser.SConcatRightContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sConcatBoth.
    def enterSConcatBoth(self, ctx:HypothesisParser.SConcatBothContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sConcatBoth.
    def exitSConcatBoth(self, ctx:HypothesisParser.SConcatBothContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sType.
    def enterSType(self, ctx:HypothesisParser.STypeContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sType.
    def exitSType(self, ctx:HypothesisParser.STypeContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sProperty.
    def enterSProperty(self, ctx:HypothesisParser.SPropertyContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sProperty.
    def exitSProperty(self, ctx:HypothesisParser.SPropertyContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sPropertyAware.
    def enterSPropertyAware(self, ctx:HypothesisParser.SPropertyAwareContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sPropertyAware.
    def exitSPropertyAware(self, ctx:HypothesisParser.SPropertyAwareContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sPropertyAccess.
    def enterSPropertyAccess(self, ctx:HypothesisParser.SPropertyAccessContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sPropertyAccess.
    def exitSPropertyAccess(self, ctx:HypothesisParser.SPropertyAccessContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sString.
    def enterSString(self, ctx:HypothesisParser.SStringContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sString.
    def exitSString(self, ctx:HypothesisParser.SStringContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sNumber.
    def enterSNumber(self, ctx:HypothesisParser.SNumberContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sNumber.
    def exitSNumber(self, ctx:HypothesisParser.SNumberContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sBoolean.
    def enterSBoolean(self, ctx:HypothesisParser.SBooleanContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sBoolean.
    def exitSBoolean(self, ctx:HypothesisParser.SBooleanContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sArray.
    def enterSArray(self, ctx:HypothesisParser.SArrayContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sArray.
    def exitSArray(self, ctx:HypothesisParser.SArrayContext):
        pass


    # Enter a parse tree produced by HypothesisParser#sMap.
    def enterSMap(self, ctx:HypothesisParser.SMapContext):
        pass

    # Exit a parse tree produced by HypothesisParser#sMap.
    def exitSMap(self, ctx:HypothesisParser.SMapContext):
        pass



del HypothesisParser