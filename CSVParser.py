# Generated from CSV.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\t")
        buf.write("\37\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\7\2\13\n\2\f\2\16")
        buf.write("\2\16\13\2\3\3\3\3\3\4\3\4\3\4\7\4\25\n\4\f\4\16\4\30")
        buf.write("\13\4\3\4\5\4\33\n\4\3\4\3\4\3\4\2\2\5\2\4\6\2\2\2\36")
        buf.write("\2\b\3\2\2\2\4\17\3\2\2\2\6\21\3\2\2\2\b\f\5\4\3\2\t\13")
        buf.write("\5\6\4\2\n\t\3\2\2\2\13\16\3\2\2\2\f\n\3\2\2\2\f\r\3\2")
        buf.write("\2\2\r\3\3\2\2\2\16\f\3\2\2\2\17\20\5\6\4\2\20\5\3\2\2")
        buf.write("\2\21\26\7\5\2\2\22\23\7\3\2\2\23\25\7\5\2\2\24\22\3\2")
        buf.write("\2\2\25\30\3\2\2\2\26\24\3\2\2\2\26\27\3\2\2\2\27\32\3")
        buf.write("\2\2\2\30\26\3\2\2\2\31\33\7\4\2\2\32\31\3\2\2\2\32\33")
        buf.write("\3\2\2\2\33\34\3\2\2\2\34\35\7\b\2\2\35\7\3\2\2\2\5\f")
        buf.write("\26\32")
        return buf.getvalue()


class CSVParser ( Parser ):

    grammarFileName = "CSV.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'\r'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'\n'", "' '" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "FIELD", "TEXT", 
                      "STRING", "NL", "WS" ]

    RULE_csv = 0
    RULE_hdr = 1
    RULE_row = 2

    ruleNames =  [ "csv", "hdr", "row" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    FIELD=3
    TEXT=4
    STRING=5
    NL=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CsvContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def hdr(self):
            return self.getTypedRuleContext(CSVParser.HdrContext,0)


        def row(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSVParser.RowContext)
            else:
                return self.getTypedRuleContext(CSVParser.RowContext,i)


        def getRuleIndex(self):
            return CSVParser.RULE_csv

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCsv" ):
                listener.enterCsv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCsv" ):
                listener.exitCsv(self)




    def csv(self):

        localctx = CSVParser.CsvContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_csv)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.hdr()
            self.state = 10
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSVParser.FIELD:
                self.state = 7
                self.row()
                self.state = 12
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HdrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def row(self):
            return self.getTypedRuleContext(CSVParser.RowContext,0)


        def getRuleIndex(self):
            return CSVParser.RULE_hdr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHdr" ):
                listener.enterHdr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHdr" ):
                listener.exitHdr(self)




    def hdr(self):

        localctx = CSVParser.HdrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_hdr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self.row()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RowContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FIELD(self, i:int=None):
            if i is None:
                return self.getTokens(CSVParser.FIELD)
            else:
                return self.getToken(CSVParser.FIELD, i)

        def NL(self):
            return self.getToken(CSVParser.NL, 0)

        def getRuleIndex(self):
            return CSVParser.RULE_row

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRow" ):
                listener.enterRow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRow" ):
                listener.exitRow(self)




    def row(self):

        localctx = CSVParser.RowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_row)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.match(CSVParser.FIELD)
            self.state = 20
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CSVParser.T__0:
                self.state = 16
                self.match(CSVParser.T__0)
                self.state = 17
                self.match(CSVParser.FIELD)
                self.state = 22
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CSVParser.T__1:
                self.state = 23
                self.match(CSVParser.T__1)


            self.state = 26
            self.match(CSVParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





