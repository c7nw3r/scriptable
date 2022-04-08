# Generated from MustacheParser.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\f")
        buf.write("\61\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3")
        buf.write("\2\3\2\3\2\7\2\22\n\2\f\2\16\2\25\13\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\7\5$\n\5\f\5\16\5")
        buf.write("\'\13\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\2\2\b\2\4")
        buf.write("\6\b\n\f\2\2\2/\2\23\3\2\2\2\4\30\3\2\2\2\6\34\3\2\2\2")
        buf.write("\b \3\2\2\2\n*\3\2\2\2\f.\3\2\2\2\16\22\5\b\5\2\17\22")
        buf.write("\5\n\6\2\20\22\5\f\7\2\21\16\3\2\2\2\21\17\3\2\2\2\21")
        buf.write("\20\3\2\2\2\22\25\3\2\2\2\23\21\3\2\2\2\23\24\3\2\2\2")
        buf.write("\24\26\3\2\2\2\25\23\3\2\2\2\26\27\7\2\2\3\27\3\3\2\2")
        buf.write("\2\30\31\7\4\2\2\31\32\7\t\2\2\32\33\7\n\2\2\33\5\3\2")
        buf.write("\2\2\34\35\7\5\2\2\35\36\7\13\2\2\36\37\7\f\2\2\37\7\3")
        buf.write("\2\2\2 %\5\4\3\2!$\5\f\7\2\"$\5\n\6\2#!\3\2\2\2#\"\3\2")
        buf.write("\2\2$\'\3\2\2\2%#\3\2\2\2%&\3\2\2\2&(\3\2\2\2\'%\3\2\2")
        buf.write("\2()\5\6\4\2)\t\3\2\2\2*+\7\6\2\2+,\7\7\2\2,-\7\b\2\2")
        buf.write("-\13\3\2\2\2./\7\3\2\2/\r\3\2\2\2\6\21\23#%")
        return buf.getvalue()


class MustacheParser ( Parser ):

    grammarFileName = "MustacheParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'{{#'", "'{{/'", "'{{'" ]

    symbolicNames = [ "<INVALID>", "TEXT", "OPEN_TAG_START", "OPEN_TAG_END", 
                      "OPEN", "PROPERTY", "CLOSE", "PROPERTY_TAG_START", 
                      "CLOSE_TAG_START", "PROPERTY_TAG_END", "CLOSE_TAG_END" ]

    RULE_sAll = 0
    RULE_sTagStart = 1
    RULE_sTagEnd = 2
    RULE_sTag = 3
    RULE_sProperty = 4
    RULE_sText = 5

    ruleNames =  [ "sAll", "sTagStart", "sTagEnd", "sTag", "sProperty", 
                   "sText" ]

    EOF = Token.EOF
    TEXT=1
    OPEN_TAG_START=2
    OPEN_TAG_END=3
    OPEN=4
    PROPERTY=5
    CLOSE=6
    PROPERTY_TAG_START=7
    CLOSE_TAG_START=8
    PROPERTY_TAG_END=9
    CLOSE_TAG_END=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SAllContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MustacheParser.EOF, 0)

        def sTag(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MustacheParser.STagContext)
            else:
                return self.getTypedRuleContext(MustacheParser.STagContext,i)


        def sProperty(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MustacheParser.SPropertyContext)
            else:
                return self.getTypedRuleContext(MustacheParser.SPropertyContext,i)


        def sText(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MustacheParser.STextContext)
            else:
                return self.getTypedRuleContext(MustacheParser.STextContext,i)


        def getRuleIndex(self):
            return MustacheParser.RULE_sAll

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSAll" ):
                listener.enterSAll(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSAll" ):
                listener.exitSAll(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSAll" ):
                return visitor.visitSAll(self)
            else:
                return visitor.visitChildren(self)




    def sAll(self):

        localctx = MustacheParser.SAllContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sAll)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MustacheParser.TEXT) | (1 << MustacheParser.OPEN_TAG_START) | (1 << MustacheParser.OPEN))) != 0):
                self.state = 15
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MustacheParser.OPEN_TAG_START]:
                    self.state = 12
                    self.sTag()
                    pass
                elif token in [MustacheParser.OPEN]:
                    self.state = 13
                    self.sProperty()
                    pass
                elif token in [MustacheParser.TEXT]:
                    self.state = 14
                    self.sText()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 20
            self.match(MustacheParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class STagStartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_TAG_START(self):
            return self.getToken(MustacheParser.OPEN_TAG_START, 0)

        def PROPERTY_TAG_START(self):
            return self.getToken(MustacheParser.PROPERTY_TAG_START, 0)

        def CLOSE_TAG_START(self):
            return self.getToken(MustacheParser.CLOSE_TAG_START, 0)

        def getRuleIndex(self):
            return MustacheParser.RULE_sTagStart

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSTagStart" ):
                listener.enterSTagStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSTagStart" ):
                listener.exitSTagStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSTagStart" ):
                return visitor.visitSTagStart(self)
            else:
                return visitor.visitChildren(self)




    def sTagStart(self):

        localctx = MustacheParser.STagStartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sTagStart)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(MustacheParser.OPEN_TAG_START)
            self.state = 23
            self.match(MustacheParser.PROPERTY_TAG_START)
            self.state = 24
            self.match(MustacheParser.CLOSE_TAG_START)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class STagEndContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_TAG_END(self):
            return self.getToken(MustacheParser.OPEN_TAG_END, 0)

        def PROPERTY_TAG_END(self):
            return self.getToken(MustacheParser.PROPERTY_TAG_END, 0)

        def CLOSE_TAG_END(self):
            return self.getToken(MustacheParser.CLOSE_TAG_END, 0)

        def getRuleIndex(self):
            return MustacheParser.RULE_sTagEnd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSTagEnd" ):
                listener.enterSTagEnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSTagEnd" ):
                listener.exitSTagEnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSTagEnd" ):
                return visitor.visitSTagEnd(self)
            else:
                return visitor.visitChildren(self)




    def sTagEnd(self):

        localctx = MustacheParser.STagEndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_sTagEnd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(MustacheParser.OPEN_TAG_END)
            self.state = 27
            self.match(MustacheParser.PROPERTY_TAG_END)
            self.state = 28
            self.match(MustacheParser.CLOSE_TAG_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class STagContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sTagStart(self):
            return self.getTypedRuleContext(MustacheParser.STagStartContext,0)


        def sTagEnd(self):
            return self.getTypedRuleContext(MustacheParser.STagEndContext,0)


        def sText(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MustacheParser.STextContext)
            else:
                return self.getTypedRuleContext(MustacheParser.STextContext,i)


        def sProperty(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MustacheParser.SPropertyContext)
            else:
                return self.getTypedRuleContext(MustacheParser.SPropertyContext,i)


        def getRuleIndex(self):
            return MustacheParser.RULE_sTag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSTag" ):
                listener.enterSTag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSTag" ):
                listener.exitSTag(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSTag" ):
                return visitor.visitSTag(self)
            else:
                return visitor.visitChildren(self)




    def sTag(self):

        localctx = MustacheParser.STagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_sTag)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.sTagStart()
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MustacheParser.TEXT or _la==MustacheParser.OPEN:
                self.state = 33
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MustacheParser.TEXT]:
                    self.state = 31
                    self.sText()
                    pass
                elif token in [MustacheParser.OPEN]:
                    self.state = 32
                    self.sProperty()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 38
            self.sTagEnd()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SPropertyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN(self):
            return self.getToken(MustacheParser.OPEN, 0)

        def PROPERTY(self):
            return self.getToken(MustacheParser.PROPERTY, 0)

        def CLOSE(self):
            return self.getToken(MustacheParser.CLOSE, 0)

        def getRuleIndex(self):
            return MustacheParser.RULE_sProperty

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSProperty" ):
                listener.enterSProperty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSProperty" ):
                listener.exitSProperty(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSProperty" ):
                return visitor.visitSProperty(self)
            else:
                return visitor.visitChildren(self)




    def sProperty(self):

        localctx = MustacheParser.SPropertyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_sProperty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(MustacheParser.OPEN)
            self.state = 41
            self.match(MustacheParser.PROPERTY)
            self.state = 42
            self.match(MustacheParser.CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class STextContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(MustacheParser.TEXT, 0)

        def getRuleIndex(self):
            return MustacheParser.RULE_sText

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSText" ):
                listener.enterSText(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSText" ):
                listener.exitSText(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSText" ):
                return visitor.visitSText(self)
            else:
                return visitor.visitChildren(self)




    def sText(self):

        localctx = MustacheParser.STextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_sText)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(MustacheParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





