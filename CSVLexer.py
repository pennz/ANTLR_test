# Generated from CSV.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\t")
        buf.write("\60\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write("\7\4\b\t\b\3\2\3\2\3\3\3\3\3\4\3\4\3\4\5\4\31\n\4\3\5")
        buf.write("\6\5\34\n\5\r\5\16\5\35\3\6\3\6\3\6\3\6\7\6$\n\6\f\6\16")
        buf.write("\6\'\13\6\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\b\2\2\t\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\3\2\4\6\2\f\f\17\17$$..\3\2$")
        buf.write("$\2\64\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\3\21\3\2\2\2\5")
        buf.write("\23\3\2\2\2\7\30\3\2\2\2\t\33\3\2\2\2\13\37\3\2\2\2\r")
        buf.write("*\3\2\2\2\17,\3\2\2\2\21\22\7.\2\2\22\4\3\2\2\2\23\24")
        buf.write("\7\17\2\2\24\6\3\2\2\2\25\31\5\t\5\2\26\31\5\13\6\2\27")
        buf.write("\31\3\2\2\2\30\25\3\2\2\2\30\26\3\2\2\2\30\27\3\2\2\2")
        buf.write("\31\b\3\2\2\2\32\34\n\2\2\2\33\32\3\2\2\2\34\35\3\2\2")
        buf.write("\2\35\33\3\2\2\2\35\36\3\2\2\2\36\n\3\2\2\2\37%\7$\2\2")
        buf.write(" !\7$\2\2!$\7$\2\2\"$\n\3\2\2# \3\2\2\2#\"\3\2\2\2$\'")
        buf.write("\3\2\2\2%#\3\2\2\2%&\3\2\2\2&(\3\2\2\2\'%\3\2\2\2()\7")
        buf.write("$\2\2)\f\3\2\2\2*+\7\f\2\2+\16\3\2\2\2,-\7\"\2\2-.\3\2")
        buf.write("\2\2./\b\b\2\2/\20\3\2\2\2\7\2\30\35#%\3\b\2\2")
        return buf.getvalue()


class CSVLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    FIELD = 3
    TEXT = 4
    STRING = 5
    NL = 6
    WS = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "'\r'", "'\n'", "' '" ]

    symbolicNames = [ "<INVALID>",
            "FIELD", "TEXT", "STRING", "NL", "WS" ]

    ruleNames = [ "T__0", "T__1", "FIELD", "TEXT", "STRING", "NL", "WS" ]

    grammarFileName = "CSV.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


