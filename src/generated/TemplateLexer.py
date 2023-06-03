# Generated from .\TemplateLexer.lex by ANTLR 4.13.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,28,219,6,-1,6,-1,6,-1,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,
        4,7,4,2,5,7,5,2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,
        2,12,7,12,2,13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,
        7,18,2,19,7,19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,
        2,25,7,25,2,26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,
        7,31,2,32,7,32,2,33,7,33,1,0,4,0,74,8,0,11,0,12,0,75,1,1,1,1,1,1,
        1,1,1,1,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,
        1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,13,1,14,
        1,14,1,15,1,15,1,16,1,16,1,17,1,17,1,18,1,18,1,19,1,19,1,20,1,20,
        3,20,124,8,20,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,22,1,23,
        3,23,136,8,23,1,23,4,23,139,8,23,11,23,12,23,140,1,23,1,23,4,23,
        145,8,23,11,23,12,23,146,3,23,149,8,23,1,23,1,23,3,23,153,8,23,1,
        23,4,23,156,8,23,11,23,12,23,157,3,23,160,8,23,1,24,1,24,1,24,5,
        24,165,8,24,10,24,12,24,168,9,24,1,25,1,25,4,25,172,8,25,11,25,12,
        25,173,1,26,1,26,1,26,1,26,5,26,180,8,26,10,26,12,26,183,9,26,1,
        27,1,27,1,27,1,27,1,28,4,28,190,8,28,11,28,12,28,191,1,28,1,28,1,
        29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,
        32,4,32,210,8,32,11,32,12,32,211,1,33,1,33,3,33,216,8,33,1,33,1,
        33,0,0,34,4,1,6,2,8,3,10,4,12,5,14,6,16,7,18,8,20,9,22,10,24,11,
        26,12,28,13,30,14,32,15,34,0,36,0,38,0,40,0,42,0,44,0,46,16,48,17,
        50,18,52,19,54,20,56,21,58,22,60,23,62,24,64,25,66,26,68,27,70,28,
        4,0,1,2,3,8,1,0,60,60,2,0,65,90,97,122,1,0,48,57,2,0,45,46,95,95,
        2,0,69,69,101,101,2,0,43,43,45,45,3,0,9,10,12,13,32,32,2,0,39,39,
        92,92,226,0,4,1,0,0,0,0,6,1,0,0,0,0,8,1,0,0,0,1,10,1,0,0,0,1,12,
        1,0,0,0,1,14,1,0,0,0,1,16,1,0,0,0,1,18,1,0,0,0,1,20,1,0,0,0,1,22,
        1,0,0,0,1,24,1,0,0,0,1,26,1,0,0,0,1,28,1,0,0,0,1,30,1,0,0,0,1,32,
        1,0,0,0,1,46,1,0,0,0,1,48,1,0,0,0,1,50,1,0,0,0,1,52,1,0,0,0,1,54,
        1,0,0,0,1,56,1,0,0,0,1,58,1,0,0,0,1,60,1,0,0,0,1,62,1,0,0,0,2,64,
        1,0,0,0,2,66,1,0,0,0,2,68,1,0,0,0,3,70,1,0,0,0,4,73,1,0,0,0,6,77,
        1,0,0,0,8,82,1,0,0,0,10,84,1,0,0,0,12,89,1,0,0,0,14,91,1,0,0,0,16,
        93,1,0,0,0,18,95,1,0,0,0,20,97,1,0,0,0,22,99,1,0,0,0,24,101,1,0,
        0,0,26,103,1,0,0,0,28,105,1,0,0,0,30,107,1,0,0,0,32,109,1,0,0,0,
        34,111,1,0,0,0,36,113,1,0,0,0,38,115,1,0,0,0,40,117,1,0,0,0,42,119,
        1,0,0,0,44,123,1,0,0,0,46,125,1,0,0,0,48,128,1,0,0,0,50,135,1,0,
        0,0,52,161,1,0,0,0,54,171,1,0,0,0,56,175,1,0,0,0,58,184,1,0,0,0,
        60,189,1,0,0,0,62,195,1,0,0,0,64,199,1,0,0,0,66,203,1,0,0,0,68,209,
        1,0,0,0,70,215,1,0,0,0,72,74,8,0,0,0,73,72,1,0,0,0,74,75,1,0,0,0,
        75,73,1,0,0,0,75,76,1,0,0,0,76,5,1,0,0,0,77,78,5,60,0,0,78,79,5,
        60,0,0,79,80,1,0,0,0,80,81,6,1,0,0,81,7,1,0,0,0,82,83,5,60,0,0,83,
        9,1,0,0,0,84,85,5,62,0,0,85,86,5,62,0,0,86,87,1,0,0,0,87,88,6,3,
        1,0,88,11,1,0,0,0,89,90,5,44,0,0,90,13,1,0,0,0,91,92,5,59,0,0,92,
        15,1,0,0,0,93,94,5,58,0,0,94,17,1,0,0,0,95,96,5,40,0,0,96,19,1,0,
        0,0,97,98,5,41,0,0,98,21,1,0,0,0,99,100,5,123,0,0,100,23,1,0,0,0,
        101,102,5,125,0,0,102,25,1,0,0,0,103,104,5,47,0,0,104,27,1,0,0,0,
        105,106,5,46,0,0,106,29,1,0,0,0,107,108,5,45,0,0,108,31,1,0,0,0,
        109,110,5,38,0,0,110,33,1,0,0,0,111,112,5,39,0,0,112,35,1,0,0,0,
        113,114,5,92,0,0,114,37,1,0,0,0,115,116,7,1,0,0,116,39,1,0,0,0,117,
        118,7,2,0,0,118,41,1,0,0,0,119,120,7,3,0,0,120,43,1,0,0,0,121,124,
        3,38,17,0,122,124,3,40,18,0,123,121,1,0,0,0,123,122,1,0,0,0,124,
        45,1,0,0,0,125,126,5,105,0,0,126,127,5,102,0,0,127,47,1,0,0,0,128,
        129,5,101,0,0,129,130,5,110,0,0,130,131,5,100,0,0,131,132,5,105,
        0,0,132,133,5,102,0,0,133,49,1,0,0,0,134,136,5,45,0,0,135,134,1,
        0,0,0,135,136,1,0,0,0,136,138,1,0,0,0,137,139,3,40,18,0,138,137,
        1,0,0,0,139,140,1,0,0,0,140,138,1,0,0,0,140,141,1,0,0,0,141,148,
        1,0,0,0,142,144,5,46,0,0,143,145,3,40,18,0,144,143,1,0,0,0,145,146,
        1,0,0,0,146,144,1,0,0,0,146,147,1,0,0,0,147,149,1,0,0,0,148,142,
        1,0,0,0,148,149,1,0,0,0,149,159,1,0,0,0,150,152,7,4,0,0,151,153,
        7,5,0,0,152,151,1,0,0,0,152,153,1,0,0,0,153,155,1,0,0,0,154,156,
        3,40,18,0,155,154,1,0,0,0,156,157,1,0,0,0,157,155,1,0,0,0,157,158,
        1,0,0,0,158,160,1,0,0,0,159,150,1,0,0,0,159,160,1,0,0,0,160,51,1,
        0,0,0,161,166,3,38,17,0,162,165,3,44,20,0,163,165,5,95,0,0,164,162,
        1,0,0,0,164,163,1,0,0,0,165,168,1,0,0,0,166,164,1,0,0,0,166,167,
        1,0,0,0,167,53,1,0,0,0,168,166,1,0,0,0,169,172,3,44,20,0,170,172,
        3,42,19,0,171,169,1,0,0,0,171,170,1,0,0,0,172,173,1,0,0,0,173,171,
        1,0,0,0,173,174,1,0,0,0,174,55,1,0,0,0,175,176,5,47,0,0,176,181,
        3,54,25,0,177,178,5,47,0,0,178,180,3,54,25,0,179,177,1,0,0,0,180,
        183,1,0,0,0,181,179,1,0,0,0,181,182,1,0,0,0,182,57,1,0,0,0,183,181,
        1,0,0,0,184,185,3,54,25,0,185,186,5,58,0,0,186,187,3,54,25,0,187,
        59,1,0,0,0,188,190,7,6,0,0,189,188,1,0,0,0,190,191,1,0,0,0,191,189,
        1,0,0,0,191,192,1,0,0,0,192,193,1,0,0,0,193,194,6,28,2,0,194,61,
        1,0,0,0,195,196,3,34,15,0,196,197,1,0,0,0,197,198,6,29,3,0,198,63,
        1,0,0,0,199,200,3,34,15,0,200,201,1,0,0,0,201,202,6,30,1,0,202,65,
        1,0,0,0,203,204,3,36,16,0,204,205,1,0,0,0,205,206,6,31,2,0,206,207,
        6,31,4,0,207,67,1,0,0,0,208,210,8,7,0,0,209,208,1,0,0,0,210,211,
        1,0,0,0,211,209,1,0,0,0,211,212,1,0,0,0,212,69,1,0,0,0,213,216,3,
        34,15,0,214,216,3,36,16,0,215,213,1,0,0,0,215,214,1,0,0,0,216,217,
        1,0,0,0,217,218,6,33,1,0,218,71,1,0,0,0,21,0,1,2,3,75,123,135,140,
        146,148,152,157,159,164,166,171,173,181,191,211,215,5,5,1,0,4,0,
        0,6,0,0,5,2,0,5,3,0
    ]

class TemplateLexer(Lexer):

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
    AND = 15
    COND_START = 16
    COND_END = 17
    NUM = 18
    FN_NAME = 19
    ID = 20
    JSON_PTR = 21
    RDF_CLASS = 22
    WS = 23
    STR_START = 24
    STR_END = 25
    ESC = 26
    STR_CONTENT = 27
    ESC_CHAR = 28

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE", "STMT_MODE", "STR_MODE", "STR_ESC_MODE" ]

    literalNames = [ "<INVALID>",
            "'<<'", "'<'", "'>>'", "','", "';'", "':'", "'('", "')'", "'{'", 
            "'}'", "'/'", "'.'", "'-'", "'&'", "'if'", "'endif'" ]

    symbolicNames = [ "<INVALID>",
            "TEMPLATE_TEXT", "STMT_START", "NOT_STMT", "STMT_END", "COMMA", 
            "SEMI", "COLON", "LPAREN", "RPAREN", "LCURLY", "RCURLY", "SLASH", 
            "PERIOD", "DASH", "AND", "COND_START", "COND_END", "NUM", "FN_NAME", 
            "ID", "JSON_PTR", "RDF_CLASS", "WS", "STR_START", "STR_END", 
            "ESC", "STR_CONTENT", "ESC_CHAR" ]

    ruleNames = [ "TEMPLATE_TEXT", "STMT_START", "NOT_STMT", "STMT_END", 
                  "COMMA", "SEMI", "COLON", "LPAREN", "RPAREN", "LCURLY", 
                  "RCURLY", "SLASH", "PERIOD", "DASH", "AND", "QUOTE", "BACKSLASH", 
                  "ALPHA", "DIGIT", "ID_SYMBOLS", "ALPHA_NUMERIC", "COND_START", 
                  "COND_END", "NUM", "FN_NAME", "ID", "JSON_PTR", "RDF_CLASS", 
                  "WS", "STR_START", "STR_END", "ESC", "STR_CONTENT", "ESC_CHAR" ]

    grammarFileName = "TemplateLexer.lex"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


