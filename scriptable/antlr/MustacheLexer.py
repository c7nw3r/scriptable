# Generated from MustacheLexer.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\f")
        buf.write("a\b\1\b\1\b\1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6")
        buf.write("\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f")
        buf.write("\4\r\t\r\3\2\6\2 \n\2\r\2\16\2!\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\7\3\7\3\b\3\b\7\b;\n\b\f\b\16\b>\13\b\3\b\5\bA\n\b")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\7\nL\n\n\f\n\16\n")
        buf.write("O\13\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\7\fX\n\f\f\f\16")
        buf.write("\f[\13\f\3\r\3\r\3\r\3\r\3\r\2\2\16\6\3\b\4\n\5\f\6\16")
        buf.write("\2\20\2\22\7\24\b\26\t\30\n\32\13\34\f\6\2\3\4\5\5\3\2")
        buf.write("}}\4\2C\\c|\6\2\62;C\\aac|\2`\2\6\3\2\2\2\2\b\3\2\2\2")
        buf.write("\2\n\3\2\2\2\2\f\3\2\2\2\3\22\3\2\2\2\3\24\3\2\2\2\4\26")
        buf.write("\3\2\2\2\4\30\3\2\2\2\5\32\3\2\2\2\5\34\3\2\2\2\6\37\3")
        buf.write("\2\2\2\b#\3\2\2\2\n)\3\2\2\2\f/\3\2\2\2\16\64\3\2\2\2")
        buf.write("\20\66\3\2\2\2\22@\3\2\2\2\24B\3\2\2\2\26I\3\2\2\2\30")
        buf.write("P\3\2\2\2\32U\3\2\2\2\34\\\3\2\2\2\36 \n\2\2\2\37\36\3")
        buf.write("\2\2\2 !\3\2\2\2!\37\3\2\2\2!\"\3\2\2\2\"\7\3\2\2\2#$")
        buf.write("\7}\2\2$%\7}\2\2%&\7%\2\2&\'\3\2\2\2\'(\b\3\2\2(\t\3\2")
        buf.write("\2\2)*\7}\2\2*+\7}\2\2+,\7\61\2\2,-\3\2\2\2-.\b\4\3\2")
        buf.write(".\13\3\2\2\2/\60\7}\2\2\60\61\7}\2\2\61\62\3\2\2\2\62")
        buf.write("\63\b\5\4\2\63\r\3\2\2\2\64\65\t\3\2\2\65\17\3\2\2\2\66")
        buf.write("\67\t\4\2\2\67\21\3\2\2\28<\5\16\6\29;\5\20\7\2:9\3\2")
        buf.write("\2\2;>\3\2\2\2<:\3\2\2\2<=\3\2\2\2=A\3\2\2\2><\3\2\2\2")
        buf.write("?A\7\60\2\2@8\3\2\2\2@?\3\2\2\2A\23\3\2\2\2BC\7\177\2")
        buf.write("\2CD\7\177\2\2DE\3\2\2\2EF\b\t\5\2FG\3\2\2\2GH\b\t\6\2")
        buf.write("H\25\3\2\2\2IM\5\16\6\2JL\5\20\7\2KJ\3\2\2\2LO\3\2\2\2")
        buf.write("MK\3\2\2\2MN\3\2\2\2N\27\3\2\2\2OM\3\2\2\2PQ\7\177\2\2")
        buf.write("QR\7\177\2\2RS\3\2\2\2ST\b\13\6\2T\31\3\2\2\2UY\5\16\6")
        buf.write("\2VX\5\20\7\2WV\3\2\2\2X[\3\2\2\2YW\3\2\2\2YZ\3\2\2\2")
        buf.write("Z\33\3\2\2\2[Y\3\2\2\2\\]\7\177\2\2]^\7\177\2\2^_\3\2")
        buf.write("\2\2_`\b\r\6\2`\35\3\2\2\2\13\2\3\4\5!<@MY\7\7\4\2\7\5")
        buf.write("\2\7\3\2\3\t\2\6\2\2")
        return buf.getvalue()


class MustacheLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    MUSTACHE = 1
    MUSTACHE_TAG_START = 2
    MUSTACHE_TAG_END = 3

    TEXT = 1
    OPEN_TAG_START = 2
    OPEN_TAG_END = 3
    OPEN = 4
    PROPERTY = 5
    CLOSE = 6
    PROPERTY_TAG_START = 7
    CLOSE_TAG_START = 8
    PROPERTY_TAG_END = 9
    CLOSE_TAG_END = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE", "MUSTACHE", "MUSTACHE_TAG_START", "MUSTACHE_TAG_END" ]

    literalNames = [ "<INVALID>",
            "'{{#'", "'{{/'", "'{{'" ]

    symbolicNames = [ "<INVALID>",
            "TEXT", "OPEN_TAG_START", "OPEN_TAG_END", "OPEN", "PROPERTY", 
            "CLOSE", "PROPERTY_TAG_START", "CLOSE_TAG_START", "PROPERTY_TAG_END", 
            "CLOSE_TAG_END" ]

    ruleNames = [ "TEXT", "OPEN_TAG_START", "OPEN_TAG_END", "OPEN", "Letter", 
                  "LetterOrDigit", "PROPERTY", "CLOSE", "PROPERTY_TAG_START", 
                  "CLOSE_TAG_START", "PROPERTY_TAG_END", "CLOSE_TAG_END" ]

    grammarFileName = "MustacheLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[7] = self.CLOSE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def CLOSE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            print("CLOSE")
     


