# Generated from .\ExprLexer.lex by ANTLR 4.13.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,25,202,6,-1,6,-1,6,-1,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,
        4,7,4,2,5,7,5,2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,
        2,12,7,12,2,13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,
        7,18,2,19,7,19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,
        2,25,7,25,2,26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,1,0,
        4,0,68,8,0,11,0,12,0,69,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,3,1,3,1,3,
        1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,
        1,11,1,11,1,12,1,12,1,13,1,13,1,14,1,14,1,15,1,15,1,16,1,16,1,17,
        1,17,1,18,1,18,1,19,1,19,3,19,116,8,19,1,20,3,20,119,8,20,1,20,4,
        20,122,8,20,11,20,12,20,123,1,20,1,20,4,20,128,8,20,11,20,12,20,
        129,3,20,132,8,20,1,20,1,20,3,20,136,8,20,1,20,4,20,139,8,20,11,
        20,12,20,140,3,20,143,8,20,1,21,1,21,1,21,5,21,148,8,21,10,21,12,
        21,151,9,21,1,22,1,22,4,22,155,8,22,11,22,12,22,156,1,23,1,23,1,
        23,1,23,5,23,163,8,23,10,23,12,23,166,9,23,1,24,1,24,1,24,1,24,1,
        25,4,25,173,8,25,11,25,12,25,174,1,25,1,25,1,26,1,26,1,26,1,26,1,
        27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,29,4,29,193,8,29,11,
        29,12,29,194,1,30,1,30,3,30,199,8,30,1,30,1,30,0,0,31,4,1,6,2,8,
        3,10,4,12,5,14,6,16,7,18,8,20,9,22,10,24,11,26,12,28,13,30,14,32,
        0,34,0,36,0,38,0,40,0,42,0,44,15,46,16,48,17,50,18,52,19,54,20,56,
        21,58,22,60,23,62,24,64,25,4,0,1,2,3,8,1,0,60,60,2,0,65,90,97,122,
        1,0,48,57,2,0,45,46,95,95,2,0,69,69,101,101,2,0,43,43,45,45,3,0,
        9,10,12,13,32,32,2,0,39,39,92,92,209,0,4,1,0,0,0,0,6,1,0,0,0,0,8,
        1,0,0,0,1,10,1,0,0,0,1,12,1,0,0,0,1,14,1,0,0,0,1,16,1,0,0,0,1,18,
        1,0,0,0,1,20,1,0,0,0,1,22,1,0,0,0,1,24,1,0,0,0,1,26,1,0,0,0,1,28,
        1,0,0,0,1,30,1,0,0,0,1,44,1,0,0,0,1,46,1,0,0,0,1,48,1,0,0,0,1,50,
        1,0,0,0,1,52,1,0,0,0,1,54,1,0,0,0,1,56,1,0,0,0,2,58,1,0,0,0,2,60,
        1,0,0,0,2,62,1,0,0,0,3,64,1,0,0,0,4,67,1,0,0,0,6,71,1,0,0,0,8,76,
        1,0,0,0,10,78,1,0,0,0,12,83,1,0,0,0,14,85,1,0,0,0,16,87,1,0,0,0,
        18,89,1,0,0,0,20,91,1,0,0,0,22,93,1,0,0,0,24,95,1,0,0,0,26,97,1,
        0,0,0,28,99,1,0,0,0,30,101,1,0,0,0,32,103,1,0,0,0,34,105,1,0,0,0,
        36,107,1,0,0,0,38,109,1,0,0,0,40,111,1,0,0,0,42,115,1,0,0,0,44,118,
        1,0,0,0,46,144,1,0,0,0,48,154,1,0,0,0,50,158,1,0,0,0,52,167,1,0,
        0,0,54,172,1,0,0,0,56,178,1,0,0,0,58,182,1,0,0,0,60,186,1,0,0,0,
        62,192,1,0,0,0,64,198,1,0,0,0,66,68,8,0,0,0,67,66,1,0,0,0,68,69,
        1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,5,1,0,0,0,71,72,5,60,0,0,
        72,73,5,60,0,0,73,74,1,0,0,0,74,75,6,1,0,0,75,7,1,0,0,0,76,77,5,
        60,0,0,77,9,1,0,0,0,78,79,5,62,0,0,79,80,5,62,0,0,80,81,1,0,0,0,
        81,82,6,3,1,0,82,11,1,0,0,0,83,84,5,44,0,0,84,13,1,0,0,0,85,86,5,
        59,0,0,86,15,1,0,0,0,87,88,5,58,0,0,88,17,1,0,0,0,89,90,5,40,0,0,
        90,19,1,0,0,0,91,92,5,41,0,0,92,21,1,0,0,0,93,94,5,123,0,0,94,23,
        1,0,0,0,95,96,5,125,0,0,96,25,1,0,0,0,97,98,5,47,0,0,98,27,1,0,0,
        0,99,100,5,46,0,0,100,29,1,0,0,0,101,102,5,45,0,0,102,31,1,0,0,0,
        103,104,5,39,0,0,104,33,1,0,0,0,105,106,5,92,0,0,106,35,1,0,0,0,
        107,108,7,1,0,0,108,37,1,0,0,0,109,110,7,2,0,0,110,39,1,0,0,0,111,
        112,7,3,0,0,112,41,1,0,0,0,113,116,3,36,16,0,114,116,3,38,17,0,115,
        113,1,0,0,0,115,114,1,0,0,0,116,43,1,0,0,0,117,119,5,45,0,0,118,
        117,1,0,0,0,118,119,1,0,0,0,119,121,1,0,0,0,120,122,3,38,17,0,121,
        120,1,0,0,0,122,123,1,0,0,0,123,121,1,0,0,0,123,124,1,0,0,0,124,
        131,1,0,0,0,125,127,5,46,0,0,126,128,3,38,17,0,127,126,1,0,0,0,128,
        129,1,0,0,0,129,127,1,0,0,0,129,130,1,0,0,0,130,132,1,0,0,0,131,
        125,1,0,0,0,131,132,1,0,0,0,132,142,1,0,0,0,133,135,7,4,0,0,134,
        136,7,5,0,0,135,134,1,0,0,0,135,136,1,0,0,0,136,138,1,0,0,0,137,
        139,3,38,17,0,138,137,1,0,0,0,139,140,1,0,0,0,140,138,1,0,0,0,140,
        141,1,0,0,0,141,143,1,0,0,0,142,133,1,0,0,0,142,143,1,0,0,0,143,
        45,1,0,0,0,144,149,3,36,16,0,145,148,3,42,19,0,146,148,5,95,0,0,
        147,145,1,0,0,0,147,146,1,0,0,0,148,151,1,0,0,0,149,147,1,0,0,0,
        149,150,1,0,0,0,150,47,1,0,0,0,151,149,1,0,0,0,152,155,3,42,19,0,
        153,155,3,40,18,0,154,152,1,0,0,0,154,153,1,0,0,0,155,156,1,0,0,
        0,156,154,1,0,0,0,156,157,1,0,0,0,157,49,1,0,0,0,158,159,5,47,0,
        0,159,164,3,48,22,0,160,161,5,47,0,0,161,163,3,48,22,0,162,160,1,
        0,0,0,163,166,1,0,0,0,164,162,1,0,0,0,164,165,1,0,0,0,165,51,1,0,
        0,0,166,164,1,0,0,0,167,168,3,48,22,0,168,169,5,58,0,0,169,170,3,
        48,22,0,170,53,1,0,0,0,171,173,7,6,0,0,172,171,1,0,0,0,173,174,1,
        0,0,0,174,172,1,0,0,0,174,175,1,0,0,0,175,176,1,0,0,0,176,177,6,
        25,2,0,177,55,1,0,0,0,178,179,3,32,14,0,179,180,1,0,0,0,180,181,
        6,26,3,0,181,57,1,0,0,0,182,183,3,32,14,0,183,184,1,0,0,0,184,185,
        6,27,1,0,185,59,1,0,0,0,186,187,3,34,15,0,187,188,1,0,0,0,188,189,
        6,28,2,0,189,190,6,28,4,0,190,61,1,0,0,0,191,193,8,7,0,0,192,191,
        1,0,0,0,193,194,1,0,0,0,194,192,1,0,0,0,194,195,1,0,0,0,195,63,1,
        0,0,0,196,199,3,32,14,0,197,199,3,34,15,0,198,196,1,0,0,0,198,197,
        1,0,0,0,199,200,1,0,0,0,200,201,6,30,1,0,201,65,1,0,0,0,21,0,1,2,
        3,69,115,118,123,129,131,135,140,142,147,149,154,156,164,174,194,
        198,5,5,1,0,4,0,0,6,0,0,5,2,0,5,3,0
    ]

class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    STMT_MODE = 1
    STR_MODE = 2
    STR_ESC_MODE = 3

    TEMPLATE_TEXT = 1
    STMT_START = 2
    NOT_STMT = 3
    STMT_END = 4
    COMMA = 5
    SEMI = 6
    COLON = 7
    LPAREN = 8
    RPAREN = 9
    LCURLY = 10
    RCURLY = 11
    SLASH = 12
    PERIOD = 13
    DASH = 14
    NUM = 15
    FN_NAME = 16
    ID = 17
    JSON_PTR = 18
    RDF_CLASS = 19
    WS = 20
    STR_START = 21
    STR_END = 22
    ESC = 23
    STR_CONTENT = 24
    ESC_CHAR = 25

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE", "STMT_MODE", "STR_MODE", "STR_ESC_MODE" ]

    literalNames = [ "<INVALID>",
            "'<<'", "'<'", "'>>'", "','", "';'", "':'", "'('", "')'", "'{'", 
            "'}'", "'/'", "'.'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "TEMPLATE_TEXT", "STMT_START", "NOT_STMT", "STMT_END", "COMMA", 
            "SEMI", "COLON", "LPAREN", "RPAREN", "LCURLY", "RCURLY", "SLASH", 
            "PERIOD", "DASH", "NUM", "FN_NAME", "ID", "JSON_PTR", "RDF_CLASS", 
            "WS", "STR_START", "STR_END", "ESC", "STR_CONTENT", "ESC_CHAR" ]

    ruleNames = [ "TEMPLATE_TEXT", "STMT_START", "NOT_STMT", "STMT_END", 
                  "COMMA", "SEMI", "COLON", "LPAREN", "RPAREN", "LCURLY", 
                  "RCURLY", "SLASH", "PERIOD", "DASH", "QUOTE", "BACKSLASH", 
                  "ALPHA", "DIGIT", "ID_SYMBOLS", "ALPHA_NUMERIC", "NUM", 
                  "FN_NAME", "ID", "JSON_PTR", "RDF_CLASS", "WS", "STR_START", 
                  "STR_END", "ESC", "STR_CONTENT", "ESC_CHAR" ]

    grammarFileName = "ExprLexer.lex"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


