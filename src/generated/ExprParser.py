# Generated from .\ExprParser.g4 by ANTLR 4.13.0
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
        4,1,25,77,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,4,0,26,8,0,11,0,
        12,0,27,1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,3,2,38,8,2,1,3,1,3,1,3,1,
        3,1,3,3,3,45,8,3,1,4,1,4,1,5,1,5,1,5,1,5,1,5,5,5,54,8,5,10,5,12,
        5,57,9,5,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,5,9,68,8,9,10,9,12,
        9,71,9,9,1,10,1,10,1,10,1,10,1,10,0,0,11,0,2,4,6,8,10,12,14,16,18,
        20,0,1,1,0,24,25,75,0,25,1,0,0,0,2,31,1,0,0,0,4,37,1,0,0,0,6,44,
        1,0,0,0,8,46,1,0,0,0,10,48,1,0,0,0,12,60,1,0,0,0,14,62,1,0,0,0,16,
        64,1,0,0,0,18,69,1,0,0,0,20,72,1,0,0,0,22,26,5,1,0,0,23,26,3,2,1,
        0,24,26,5,3,0,0,25,22,1,0,0,0,25,23,1,0,0,0,25,24,1,0,0,0,26,27,
        1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,29,1,0,0,0,29,30,5,0,0,1,
        30,1,1,0,0,0,31,32,5,2,0,0,32,33,3,4,2,0,33,34,5,4,0,0,34,3,1,0,
        0,0,35,38,3,10,5,0,36,38,3,12,6,0,37,35,1,0,0,0,37,36,1,0,0,0,38,
        5,1,0,0,0,39,45,3,10,5,0,40,45,3,12,6,0,41,45,3,14,7,0,42,45,3,16,
        8,0,43,45,3,20,10,0,44,39,1,0,0,0,44,40,1,0,0,0,44,41,1,0,0,0,44,
        42,1,0,0,0,44,43,1,0,0,0,45,7,1,0,0,0,46,47,5,16,0,0,47,9,1,0,0,
        0,48,49,3,8,4,0,49,50,5,8,0,0,50,55,3,6,3,0,51,52,5,5,0,0,52,54,
        3,6,3,0,53,51,1,0,0,0,54,57,1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,0,
        56,58,1,0,0,0,57,55,1,0,0,0,58,59,5,9,0,0,59,11,1,0,0,0,60,61,5,
        18,0,0,61,13,1,0,0,0,62,63,5,19,0,0,63,15,1,0,0,0,64,65,5,15,0,0,
        65,17,1,0,0,0,66,68,7,0,0,0,67,66,1,0,0,0,68,71,1,0,0,0,69,67,1,
        0,0,0,69,70,1,0,0,0,70,19,1,0,0,0,71,69,1,0,0,0,72,73,5,21,0,0,73,
        74,3,18,9,0,74,75,5,22,0,0,75,21,1,0,0,0,6,25,27,37,44,55,69
    ]

class ExprParser ( Parser ):

    grammarFileName = "ExprParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'<<'", "'<'", "'>>'", "','", 
                     "';'", "':'", "'('", "')'", "'{'", "'}'", "'/'", "'.'", 
                     "'-'" ]

    symbolicNames = [ "<INVALID>", "TEMPLATE_TEXT", "STMT_START", "NOT_STMT", 
                      "STMT_END", "COMMA", "SEMI", "COLON", "LPAREN", "RPAREN", 
                      "LCURLY", "RCURLY", "SLASH", "PERIOD", "DASH", "NUM", 
                      "FN_NAME", "ID", "JSON_PTR", "RDF_CLASS", "WS", "STR_START", 
                      "STR_END", "ESC", "STR_CONTENT", "ESC_CHAR" ]

    RULE_template = 0
    RULE_template_stmt = 1
    RULE_stmt = 2
    RULE_expr = 3
    RULE_fn_name = 4
    RULE_fn_call = 5
    RULE_json_ptr = 6
    RULE_rdf_class = 7
    RULE_num = 8
    RULE_str_content = 9
    RULE_str = 10

    ruleNames =  [ "template", "template_stmt", "stmt", "expr", "fn_name", 
                   "fn_call", "json_ptr", "rdf_class", "num", "str_content", 
                   "str" ]

    EOF = Token.EOF
    TEMPLATE_TEXT=1
    STMT_START=2
    NOT_STMT=3
    STMT_END=4
    COMMA=5
    SEMI=6
    COLON=7
    LPAREN=8
    RPAREN=9
    LCURLY=10
    RCURLY=11
    SLASH=12
    PERIOD=13
    DASH=14
    NUM=15
    FN_NAME=16
    ID=17
    JSON_PTR=18
    RDF_CLASS=19
    WS=20
    STR_START=21
    STR_END=22
    ESC=23
    STR_CONTENT=24
    ESC_CHAR=25

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class TemplateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def TEMPLATE_TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.TEMPLATE_TEXT)
            else:
                return self.getToken(ExprParser.TEMPLATE_TEXT, i)

        def template_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.Template_stmtContext)
            else:
                return self.getTypedRuleContext(ExprParser.Template_stmtContext,i)


        def NOT_STMT(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.NOT_STMT)
            else:
                return self.getToken(ExprParser.NOT_STMT, i)

        def getRuleIndex(self):
            return ExprParser.RULE_template

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTemplate" ):
                listener.enterTemplate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTemplate" ):
                listener.exitTemplate(self)




    def template(self):

        localctx = ExprParser.TemplateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_template)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 25
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 22
                    self.match(ExprParser.TEMPLATE_TEXT)
                    pass
                elif token in [2]:
                    self.state = 23
                    self.template_stmt()
                    pass
                elif token in [3]:
                    self.state = 24
                    self.match(ExprParser.NOT_STMT)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0)):
                    break

            self.state = 29
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Template_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STMT_START(self):
            return self.getToken(ExprParser.STMT_START, 0)

        def stmt(self):
            return self.getTypedRuleContext(ExprParser.StmtContext,0)


        def STMT_END(self):
            return self.getToken(ExprParser.STMT_END, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_template_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTemplate_stmt" ):
                listener.enterTemplate_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTemplate_stmt" ):
                listener.exitTemplate_stmt(self)




    def template_stmt(self):

        localctx = ExprParser.Template_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_template_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(ExprParser.STMT_START)
            self.state = 32
            self.stmt()
            self.state = 33
            self.match(ExprParser.STMT_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fn_call(self):
            return self.getTypedRuleContext(ExprParser.Fn_callContext,0)


        def json_ptr(self):
            return self.getTypedRuleContext(ExprParser.Json_ptrContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)




    def stmt(self):

        localctx = ExprParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stmt)
        try:
            self.state = 37
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.fn_call()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.json_ptr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fn_call(self):
            return self.getTypedRuleContext(ExprParser.Fn_callContext,0)


        def json_ptr(self):
            return self.getTypedRuleContext(ExprParser.Json_ptrContext,0)


        def rdf_class(self):
            return self.getTypedRuleContext(ExprParser.Rdf_classContext,0)


        def num(self):
            return self.getTypedRuleContext(ExprParser.NumContext,0)


        def str_(self):
            return self.getTypedRuleContext(ExprParser.StrContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = ExprParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expr)
        try:
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.fn_call()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.json_ptr()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 3)
                self.state = 41
                self.rdf_class()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 4)
                self.state = 42
                self.num()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 5)
                self.state = 43
                self.str_()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fn_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FN_NAME(self):
            return self.getToken(ExprParser.FN_NAME, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_fn_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFn_name" ):
                listener.enterFn_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFn_name" ):
                listener.exitFn_name(self)




    def fn_name(self):

        localctx = ExprParser.Fn_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_fn_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(ExprParser.FN_NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fn_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fn_name(self):
            return self.getTypedRuleContext(ExprParser.Fn_nameContext,0)


        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.COMMA)
            else:
                return self.getToken(ExprParser.COMMA, i)

        def getRuleIndex(self):
            return ExprParser.RULE_fn_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFn_call" ):
                listener.enterFn_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFn_call" ):
                listener.exitFn_call(self)




    def fn_call(self):

        localctx = ExprParser.Fn_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_fn_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.fn_name()
            self.state = 49
            self.match(ExprParser.LPAREN)
            self.state = 50
            self.expr()
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 51
                self.match(ExprParser.COMMA)
                self.state = 52
                self.expr()
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 58
            self.match(ExprParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Json_ptrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def JSON_PTR(self):
            return self.getToken(ExprParser.JSON_PTR, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_json_ptr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJson_ptr" ):
                listener.enterJson_ptr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJson_ptr" ):
                listener.exitJson_ptr(self)




    def json_ptr(self):

        localctx = ExprParser.Json_ptrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_json_ptr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(ExprParser.JSON_PTR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rdf_classContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RDF_CLASS(self):
            return self.getToken(ExprParser.RDF_CLASS, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_rdf_class

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRdf_class" ):
                listener.enterRdf_class(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRdf_class" ):
                listener.exitRdf_class(self)




    def rdf_class(self):

        localctx = ExprParser.Rdf_classContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_rdf_class)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(ExprParser.RDF_CLASS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(ExprParser.NUM, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_num

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNum" ):
                listener.enterNum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNum" ):
                listener.exitNum(self)




    def num(self):

        localctx = ExprParser.NumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_num)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(ExprParser.NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Str_contentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ESC_CHAR(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ESC_CHAR)
            else:
                return self.getToken(ExprParser.ESC_CHAR, i)

        def STR_CONTENT(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.STR_CONTENT)
            else:
                return self.getToken(ExprParser.STR_CONTENT, i)

        def getRuleIndex(self):
            return ExprParser.RULE_str_content

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStr_content" ):
                listener.enterStr_content(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStr_content" ):
                listener.exitStr_content(self)




    def str_content(self):

        localctx = ExprParser.Str_contentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_str_content)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24 or _la==25:
                self.state = 66
                _la = self._input.LA(1)
                if not(_la==24 or _la==25):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STR_START(self):
            return self.getToken(ExprParser.STR_START, 0)

        def str_content(self):
            return self.getTypedRuleContext(ExprParser.Str_contentContext,0)


        def STR_END(self):
            return self.getToken(ExprParser.STR_END, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_str

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStr" ):
                listener.enterStr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStr" ):
                listener.exitStr(self)




    def str_(self):

        localctx = ExprParser.StrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_str)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(ExprParser.STR_START)
            self.state = 73
            self.str_content()
            self.state = 74
            self.match(ExprParser.STR_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





