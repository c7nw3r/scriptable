# Generated from Hypothesis.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .HypothesisParser import HypothesisParser
else:
    from HypothesisParser import HypothesisParser

# This class defines a complete generic visitor for a parse tree produced by HypothesisParser.

class HypothesisVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by HypothesisParser#sAll.
    def visitSAll(self, ctx:HypothesisParser.SAllContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sOperand.
    def visitSOperand(self, ctx:HypothesisParser.SOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sOperator.
    def visitSOperator(self, ctx:HypothesisParser.SOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sExpression.
    def visitSExpression(self, ctx:HypothesisParser.SExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sTerm.
    def visitSTerm(self, ctx:HypothesisParser.STermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sValue.
    def visitSValue(self, ctx:HypothesisParser.SValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sPlus.
    def visitSPlus(self, ctx:HypothesisParser.SPlusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sMinus.
    def visitSMinus(self, ctx:HypothesisParser.SMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sMul.
    def visitSMul(self, ctx:HypothesisParser.SMulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sDiv.
    def visitSDiv(self, ctx:HypothesisParser.SDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sPower.
    def visitSPower(self, ctx:HypothesisParser.SPowerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sAnd.
    def visitSAnd(self, ctx:HypothesisParser.SAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sOr.
    def visitSOr(self, ctx:HypothesisParser.SOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sNot.
    def visitSNot(self, ctx:HypothesisParser.SNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sEquals.
    def visitSEquals(self, ctx:HypothesisParser.SEqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sNotEquals.
    def visitSNotEquals(self, ctx:HypothesisParser.SNotEqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sLowerThan.
    def visitSLowerThan(self, ctx:HypothesisParser.SLowerThanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sLowerEquals.
    def visitSLowerEquals(self, ctx:HypothesisParser.SLowerEqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sGreaterThan.
    def visitSGreaterThan(self, ctx:HypothesisParser.SGreaterThanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sGreaterEquals.
    def visitSGreaterEquals(self, ctx:HypothesisParser.SGreaterEqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sArithmeticExpression.
    def visitSArithmeticExpression(self, ctx:HypothesisParser.SArithmeticExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sArithmeticTerm.
    def visitSArithmeticTerm(self, ctx:HypothesisParser.SArithmeticTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sBooleanOperand.
    def visitSBooleanOperand(self, ctx:HypothesisParser.SBooleanOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sBooleanOperator.
    def visitSBooleanOperator(self, ctx:HypothesisParser.SBooleanOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sBooleanExpression.
    def visitSBooleanExpression(self, ctx:HypothesisParser.SBooleanExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sBooleanTerm.
    def visitSBooleanTerm(self, ctx:HypothesisParser.SBooleanTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sNumberOperand.
    def visitSNumberOperand(self, ctx:HypothesisParser.SNumberOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sNumberOperator.
    def visitSNumberOperator(self, ctx:HypothesisParser.SNumberOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sNumberExpression.
    def visitSNumberExpression(self, ctx:HypothesisParser.SNumberExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sNumberTerm.
    def visitSNumberTerm(self, ctx:HypothesisParser.SNumberTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sStringOperand.
    def visitSStringOperand(self, ctx:HypothesisParser.SStringOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sStringOperator.
    def visitSStringOperator(self, ctx:HypothesisParser.SStringOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sStringExpression.
    def visitSStringExpression(self, ctx:HypothesisParser.SStringExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sStringTerm.
    def visitSStringTerm(self, ctx:HypothesisParser.SStringTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sConcatOperand.
    def visitSConcatOperand(self, ctx:HypothesisParser.SConcatOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sConcatExpression.
    def visitSConcatExpression(self, ctx:HypothesisParser.SConcatExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sConcatLeft.
    def visitSConcatLeft(self, ctx:HypothesisParser.SConcatLeftContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sConcatRight.
    def visitSConcatRight(self, ctx:HypothesisParser.SConcatRightContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sConcatBoth.
    def visitSConcatBoth(self, ctx:HypothesisParser.SConcatBothContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sType.
    def visitSType(self, ctx:HypothesisParser.STypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sProperty.
    def visitSProperty(self, ctx:HypothesisParser.SPropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sPropertyAware.
    def visitSPropertyAware(self, ctx:HypothesisParser.SPropertyAwareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sPropertyAccess.
    def visitSPropertyAccess(self, ctx:HypothesisParser.SPropertyAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sString.
    def visitSString(self, ctx:HypothesisParser.SStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sNumber.
    def visitSNumber(self, ctx:HypothesisParser.SNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sBoolean.
    def visitSBoolean(self, ctx:HypothesisParser.SBooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sArray.
    def visitSArray(self, ctx:HypothesisParser.SArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HypothesisParser#sMap.
    def visitSMap(self, ctx:HypothesisParser.SMapContext):
        return self.visitChildren(ctx)



del HypothesisParser