# Generated from c:/Users/David/Documents/.ja/skola/ing/PRK/dejvuv-jazyk-prk/semestralka/dj.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,8,33,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,1,1,1,1,1,
        1,1,1,1,1,2,1,2,3,2,19,8,2,1,2,1,2,1,2,3,2,24,8,2,5,2,26,8,2,10,
        2,12,2,29,9,2,1,3,1,3,1,3,0,0,4,0,2,4,6,0,1,1,0,1,2,31,0,8,1,0,0,
        0,2,11,1,0,0,0,4,18,1,0,0,0,6,30,1,0,0,0,8,9,3,2,1,0,9,10,5,0,0,
        1,10,1,1,0,0,0,11,12,5,4,0,0,12,13,5,5,0,0,13,14,3,4,2,0,14,15,5,
        6,0,0,15,3,1,0,0,0,16,19,3,6,3,0,17,19,3,2,1,0,18,16,1,0,0,0,18,
        17,1,0,0,0,19,27,1,0,0,0,20,23,5,7,0,0,21,24,3,6,3,0,22,24,3,2,1,
        0,23,21,1,0,0,0,23,22,1,0,0,0,24,26,1,0,0,0,25,20,1,0,0,0,26,29,
        1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,5,1,0,0,0,29,27,1,0,0,0,30,
        31,7,0,0,0,31,7,1,0,0,0,3,18,23,27
    ]

class djParser ( Parser ):

    grammarFileName = "dj.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>", "INTEGER", "FLOAT", "VALUE", "OPERATION", 
                      "LBR", "RBR", "COMMA", "WS" ]

    RULE_start = 0
    RULE_expression = 1
    RULE_operands = 2
    RULE_value = 3

    ruleNames =  [ "start", "expression", "operands", "value" ]

    EOF = Token.EOF
    INTEGER=1
    FLOAT=2
    VALUE=3
    OPERATION=4
    LBR=5
    RBR=6
    COMMA=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(djParser.ExpressionContext,0)


        def EOF(self):
            return self.getToken(djParser.EOF, 0)

        def getRuleIndex(self):
            return djParser.RULE_start

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = djParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.expression()
            self.state = 9
            self.match(djParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPERATION(self):
            return self.getToken(djParser.OPERATION, 0)

        def LBR(self):
            return self.getToken(djParser.LBR, 0)

        def operands(self):
            return self.getTypedRuleContext(djParser.OperandsContext,0)


        def RBR(self):
            return self.getToken(djParser.RBR, 0)

        def getRuleIndex(self):
            return djParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = djParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self.match(djParser.OPERATION)
            self.state = 12
            self.match(djParser.LBR)
            self.state = 13
            self.operands()
            self.state = 14
            self.match(djParser.RBR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(djParser.ValueContext)
            else:
                return self.getTypedRuleContext(djParser.ValueContext,i)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(djParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(djParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(djParser.COMMA)
            else:
                return self.getToken(djParser.COMMA, i)

        def getRuleIndex(self):
            return djParser.RULE_operands

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperands" ):
                return visitor.visitOperands(self)
            else:
                return visitor.visitChildren(self)




    def operands(self):

        localctx = djParser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_operands)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2]:
                self.state = 16
                self.value()
                pass
            elif token in [4]:
                self.state = 17
                self.expression()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 20
                self.match(djParser.COMMA)
                self.state = 23
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 2]:
                    self.state = 21
                    self.value()
                    pass
                elif token in [4]:
                    self.state = 22
                    self.expression()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(djParser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(djParser.FLOAT, 0)

        def getRuleIndex(self):
            return djParser.RULE_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = djParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            _la = self._input.LA(1)
            if not(_la==1 or _la==2):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





