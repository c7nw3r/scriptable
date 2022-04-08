# Generated from MustacheParser.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MustacheParser import MustacheParser
else:
    from MustacheParser import MustacheParser

# This class defines a complete generic visitor for a parse tree produced by MustacheParser.

class MustacheParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MustacheParser#sAll.
    def visitSAll(self, ctx:MustacheParser.SAllContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MustacheParser#sTagStart.
    def visitSTagStart(self, ctx:MustacheParser.STagStartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MustacheParser#sTagEnd.
    def visitSTagEnd(self, ctx:MustacheParser.STagEndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MustacheParser#sTag.
    def visitSTag(self, ctx:MustacheParser.STagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MustacheParser#sProperty.
    def visitSProperty(self, ctx:MustacheParser.SPropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MustacheParser#sText.
    def visitSText(self, ctx:MustacheParser.STextContext):
        return self.visitChildren(ctx)



del MustacheParser