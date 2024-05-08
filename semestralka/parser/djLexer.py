# Generated from c:/Users/David/Documents/.ja/skola/ing/PRK/dejvuv-jazyk-prk/semestralka/dj.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,8,68,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,1,1,1,1,2,1,2,
        1,3,1,3,5,3,32,8,3,10,3,12,3,35,9,3,1,3,3,3,38,8,3,1,4,1,4,1,4,5,
        4,43,8,4,10,4,12,4,46,9,4,1,4,1,4,1,5,1,5,3,5,52,8,5,1,6,1,6,1,7,
        1,7,1,8,1,8,1,9,1,9,1,10,4,10,63,8,10,11,10,12,10,64,1,10,1,10,0,
        0,11,1,0,3,0,5,0,7,1,9,2,11,3,13,4,15,5,17,6,19,7,21,8,1,0,4,1,0,
        49,57,1,0,48,57,3,0,42,43,47,47,126,126,3,0,9,10,13,13,32,32,69,
        0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,
        17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,1,23,1,0,0,0,3,25,1,0,0,0,5,
        27,1,0,0,0,7,37,1,0,0,0,9,39,1,0,0,0,11,51,1,0,0,0,13,53,1,0,0,0,
        15,55,1,0,0,0,17,57,1,0,0,0,19,59,1,0,0,0,21,62,1,0,0,0,23,24,7,
        0,0,0,24,2,1,0,0,0,25,26,7,1,0,0,26,4,1,0,0,0,27,28,5,48,0,0,28,
        6,1,0,0,0,29,33,3,1,0,0,30,32,3,3,1,0,31,30,1,0,0,0,32,35,1,0,0,
        0,33,31,1,0,0,0,33,34,1,0,0,0,34,38,1,0,0,0,35,33,1,0,0,0,36,38,
        3,5,2,0,37,29,1,0,0,0,37,36,1,0,0,0,38,8,1,0,0,0,39,40,3,7,3,0,40,
        44,5,46,0,0,41,43,3,3,1,0,42,41,1,0,0,0,43,46,1,0,0,0,44,42,1,0,
        0,0,44,45,1,0,0,0,45,47,1,0,0,0,46,44,1,0,0,0,47,48,3,1,0,0,48,10,
        1,0,0,0,49,52,3,7,3,0,50,52,3,9,4,0,51,49,1,0,0,0,51,50,1,0,0,0,
        52,12,1,0,0,0,53,54,7,2,0,0,54,14,1,0,0,0,55,56,5,40,0,0,56,16,1,
        0,0,0,57,58,5,41,0,0,58,18,1,0,0,0,59,60,5,44,0,0,60,20,1,0,0,0,
        61,63,7,3,0,0,62,61,1,0,0,0,63,64,1,0,0,0,64,62,1,0,0,0,64,65,1,
        0,0,0,65,66,1,0,0,0,66,67,6,10,0,0,67,22,1,0,0,0,6,0,33,37,44,51,
        64,1,6,0,0
    ]

class djLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTEGER = 1
    FLOAT = 2
    VALUE = 3
    OPERATION = 4
    LBR = 5
    RBR = 6
    COMMA = 7
    WS = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>",
            "INTEGER", "FLOAT", "VALUE", "OPERATION", "LBR", "RBR", "COMMA", 
            "WS" ]

    ruleNames = [ "START_DIGIT", "DIGIT", "ZERO", "INTEGER", "FLOAT", "VALUE", 
                  "OPERATION", "LBR", "RBR", "COMMA", "WS" ]

    grammarFileName = "dj.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


