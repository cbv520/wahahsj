# Generated from .\TemplateParser.g4 by ANTLR 4.13.0
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
        4,1,28,110,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,1,0,1,0,1,1,1,1,1,1,1,1,4,1,40,8,1,11,1,
        12,1,41,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,
        3,4,58,8,4,1,5,1,5,1,5,1,5,1,5,3,5,65,8,5,1,6,1,6,1,6,1,7,1,7,1,
        8,1,8,1,8,5,8,75,8,8,10,8,12,8,78,9,8,1,9,1,9,1,10,1,10,1,10,1,10,
        1,10,5,10,87,8,10,10,10,12,10,90,9,10,1,10,1,10,1,11,1,11,1,12,1,
        12,1,13,1,13,1,14,5,14,101,8,14,10,14,12,14,104,9,14,1,15,1,15,1,
        15,1,15,1,15,0,0,16,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,0,
        1,1,0,27,28,105,0,32,1,0,0,0,2,39,1,0,0,0,4,43,1,0,0,0,6,51,1,0,
        0,0,8,57,1,0,0,0,10,64,1,0,0,0,12,66,1,0,0,0,14,69,1,0,0,0,16,71,
        1,0,0,0,18,79,1,0,0,0,20,81,1,0,0,0,22,93,1,0,0,0,24,95,1,0,0,0,
        26,97,1,0,0,0,28,102,1,0,0,0,30,105,1,0,0,0,32,33,3,2,1,0,33,34,
        5,0,0,1,34,1,1,0,0,0,35,40,5,1,0,0,36,40,3,6,3,0,37,40,3,4,2,0,38,
        40,5,3,0,0,39,35,1,0,0,0,39,36,1,0,0,0,39,37,1,0,0,0,39,38,1,0,0,
        0,40,41,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,3,1,0,0,0,43,44,5,
        2,0,0,44,45,3,12,6,0,45,46,5,4,0,0,46,47,3,2,1,0,47,48,5,2,0,0,48,
        49,3,14,7,0,49,50,5,4,0,0,50,5,1,0,0,0,51,52,5,2,0,0,52,53,3,8,4,
        0,53,54,5,4,0,0,54,7,1,0,0,0,55,58,3,20,10,0,56,58,3,22,11,0,57,
        55,1,0,0,0,57,56,1,0,0,0,58,9,1,0,0,0,59,65,3,20,10,0,60,65,3,22,
        11,0,61,65,3,24,12,0,62,65,3,26,13,0,63,65,3,30,15,0,64,59,1,0,0,
        0,64,60,1,0,0,0,64,61,1,0,0,0,64,62,1,0,0,0,64,63,1,0,0,0,65,11,
        1,0,0,0,66,67,5,16,0,0,67,68,3,16,8,0,68,13,1,0,0,0,69,70,5,17,0,
        0,70,15,1,0,0,0,71,76,5,21,0,0,72,73,5,15,0,0,73,75,5,21,0,0,74,
        72,1,0,0,0,75,78,1,0,0,0,76,74,1,0,0,0,76,77,1,0,0,0,77,17,1,0,0,
        0,78,76,1,0,0,0,79,80,5,19,0,0,80,19,1,0,0,0,81,82,3,18,9,0,82,83,
        5,8,0,0,83,88,3,10,5,0,84,85,5,5,0,0,85,87,3,10,5,0,86,84,1,0,0,
        0,87,90,1,0,0,0,88,86,1,0,0,0,88,89,1,0,0,0,89,91,1,0,0,0,90,88,
        1,0,0,0,91,92,5,9,0,0,92,21,1,0,0,0,93,94,5,21,0,0,94,23,1,0,0,0,
        95,96,5,22,0,0,96,25,1,0,0,0,97,98,5,18,0,0,98,27,1,0,0,0,99,101,
        7,0,0,0,100,99,1,0,0,0,101,104,1,0,0,0,102,100,1,0,0,0,102,103,1,
        0,0,0,103,29,1,0,0,0,104,102,1,0,0,0,105,106,5,24,0,0,106,107,3,
        28,14,0,107,108,5,25,0,0,108,31,1,0,0,0,7,39,41,57,64,76,88,102
    ]

class TemplateParser ( Parser ):

    grammarFileName = "TemplateParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'<<'", "'<'", "'>>'", "','", 
                     "';'", "':'", "'('", "')'", "'{'", "'}'", "'/'", "'.'", 
                     "'-'", "'&'", "'if'", "'endif'" ]

    symbolicNames = [ "<INVALID>", "TEMPLATE_TEXT", "STMT_START", "NOT_STMT", 
                      "STMT_END", "COMMA", "SEMI", "COLON", "LPAREN", "RPAREN", 
                      "LCURLY", "RCURLY", "SLASH", "PERIOD", "DASH", "AND", 
                      "COND_START", "COND_END", "NUM", "FN_NAME", "ID", 
                      "JSON_PTR", "RDF_CLASS", "WS", "STR_START", "STR_END", 
                      "ESC", "STR_CONTENT", "ESC_CHAR" ]

    RULE_root = 0
    RULE_template = 1
    RULE_cond_template = 2
    RULE_template_stmt = 3
    RULE_stmt = 4
    RULE_expr = 5
    RULE_cond_start = 6
    RULE_cond_end = 7
    RULE_cond_list = 8
    RULE_fn_name = 9
    RULE_fn_call = 10
    RULE_json_ptr = 11
    RULE_rdf_class = 12
    RULE_num = 13
    RULE_str_content = 14
    RULE_str = 15

    ruleNames =  [ "root", "template", "cond_template", "template_stmt", 
                   "stmt", "expr", "cond_start", "cond_end", "cond_list", 
                   "fn_name", "fn_call", "json_ptr", "rdf_class", "num", 
                   "str_content", "str" ]

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
    AND=15
    COND_START=16
    COND_END=17
    NUM=18
    FN_NAME=19
    ID=20
    JSON_PTR=21
    RDF_CLASS=22
    WS=23
    STR_START=24
    STR_END=25
    ESC=26
    STR_CONTENT=27
    ESC_CHAR=28

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def template(self):
            return self.getTypedRuleContext(TemplateParser.TemplateContext,0)


        def EOF(self):
            return self.getToken(TemplateParser.EOF, 0)

        def getRuleIndex(self):
            return TemplateParser.RULE_root

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoot" ):
                listener.enterRoot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoot" ):
                listener.exitRoot(self)




    def root(self):

        localctx = TemplateParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.template()
            self.state = 33
            self.match(TemplateParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TemplateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEMPLATE_TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(TemplateParser.TEMPLATE_TEXT)
            else:
                return self.getToken(TemplateParser.TEMPLATE_TEXT, i)

        def template_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TemplateParser.Template_stmtContext)
            else:
                return self.getTypedRuleContext(TemplateParser.Template_stmtContext,i)


        def cond_template(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TemplateParser.Cond_templateContext)
            else:
                return self.getTypedRuleContext(TemplateParser.Cond_templateContext,i)


        def NOT_STMT(self, i:int=None):
            if i is None:
                return self.getTokens(TemplateParser.NOT_STMT)
            else:
                return self.getToken(TemplateParser.NOT_STMT, i)

        def getRuleIndex(self):
            return TemplateParser.RULE_template

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTemplate" ):
                listener.enterTemplate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTemplate" ):
                listener.exitTemplate(self)




    def template(self):

        localctx = TemplateParser.TemplateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_template)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 39
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        self.state = 35
                        self.match(TemplateParser.TEMPLATE_TEXT)
                        pass

                    elif la_ == 2:
                        self.state = 36
                        self.template_stmt()
                        pass

                    elif la_ == 3:
                        self.state = 37
                        self.cond_template()
                        pass

                    elif la_ == 4:
                        self.state = 38
                        self.match(TemplateParser.NOT_STMT)
                        pass



                else:
                    raise NoViableAltException(self)
                self.state = 41 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cond_templateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STMT_START(self, i:int=None):
            if i is None:
                return self.getTokens(TemplateParser.STMT_START)
            else:
                return self.getToken(TemplateParser.STMT_START, i)

        def cond_start(self):
            return self.getTypedRuleContext(TemplateParser.Cond_startContext,0)


        def STMT_END(self, i:int=None):
            if i is None:
                return self.getTokens(TemplateParser.STMT_END)
            else:
                return self.getToken(TemplateParser.STMT_END, i)

        def template(self):
            return self.getTypedRuleContext(TemplateParser.TemplateContext,0)


        def cond_end(self):
            return self.getTypedRuleContext(TemplateParser.Cond_endContext,0)


        def getRuleIndex(self):
            return TemplateParser.RULE_cond_template

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCond_template" ):
                listener.enterCond_template(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCond_template" ):
                listener.exitCond_template(self)




    def cond_template(self):

        localctx = TemplateParser.Cond_templateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_cond_template)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(TemplateParser.STMT_START)
            self.state = 44
            self.cond_start()
            self.state = 45
            self.match(TemplateParser.STMT_END)
            self.state = 46
            self.template()
            self.state = 47
            self.match(TemplateParser.STMT_START)
            self.state = 48
            self.cond_end()
            self.state = 49
            self.match(TemplateParser.STMT_END)
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
            return self.getToken(TemplateParser.STMT_START, 0)

        def stmt(self):
            return self.getTypedRuleContext(TemplateParser.StmtContext,0)


        def STMT_END(self):
            return self.getToken(TemplateParser.STMT_END, 0)

        def getRuleIndex(self):
            return TemplateParser.RULE_template_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTemplate_stmt" ):
                listener.enterTemplate_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTemplate_stmt" ):
                listener.exitTemplate_stmt(self)




    def template_stmt(self):

        localctx = TemplateParser.Template_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_template_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(TemplateParser.STMT_START)
            self.state = 52
            self.stmt()
            self.state = 53
            self.match(TemplateParser.STMT_END)
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
            return self.getTypedRuleContext(TemplateParser.Fn_callContext,0)


        def json_ptr(self):
            return self.getTypedRuleContext(TemplateParser.Json_ptrContext,0)


        def getRuleIndex(self):
            return TemplateParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)




    def stmt(self):

        localctx = TemplateParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_stmt)
        try:
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.fn_call()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
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
            return self.getTypedRuleContext(TemplateParser.Fn_callContext,0)


        def json_ptr(self):
            return self.getTypedRuleContext(TemplateParser.Json_ptrContext,0)


        def rdf_class(self):
            return self.getTypedRuleContext(TemplateParser.Rdf_classContext,0)


        def num(self):
            return self.getTypedRuleContext(TemplateParser.NumContext,0)


        def str_(self):
            return self.getTypedRuleContext(TemplateParser.StrContext,0)


        def getRuleIndex(self):
            return TemplateParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = TemplateParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expr)
        try:
            self.state = 64
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.fn_call()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.json_ptr()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 61
                self.rdf_class()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 4)
                self.state = 62
                self.num()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 5)
                self.state = 63
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


    class Cond_startContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COND_START(self):
            return self.getToken(TemplateParser.COND_START, 0)

        def cond_list(self):
            return self.getTypedRuleContext(TemplateParser.Cond_listContext,0)


        def getRuleIndex(self):
            return TemplateParser.RULE_cond_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCond_start" ):
                listener.enterCond_start(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCond_start" ):
                listener.exitCond_start(self)




    def cond_start(self):

        localctx = TemplateParser.Cond_startContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_cond_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(TemplateParser.COND_START)
            self.state = 67
            self.cond_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cond_endContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COND_END(self):
            return self.getToken(TemplateParser.COND_END, 0)

        def getRuleIndex(self):
            return TemplateParser.RULE_cond_end

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCond_end" ):
                listener.enterCond_end(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCond_end" ):
                listener.exitCond_end(self)




    def cond_end(self):

        localctx = TemplateParser.Cond_endContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_cond_end)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(TemplateParser.COND_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cond_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def JSON_PTR(self, i:int=None):
            if i is None:
                return self.getTokens(TemplateParser.JSON_PTR)
            else:
                return self.getToken(TemplateParser.JSON_PTR, i)

        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(TemplateParser.AND)
            else:
                return self.getToken(TemplateParser.AND, i)

        def getRuleIndex(self):
            return TemplateParser.RULE_cond_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCond_list" ):
                listener.enterCond_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCond_list" ):
                listener.exitCond_list(self)




    def cond_list(self):

        localctx = TemplateParser.Cond_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_cond_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(TemplateParser.JSON_PTR)
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 72
                self.match(TemplateParser.AND)
                self.state = 73
                self.match(TemplateParser.JSON_PTR)
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            return self.getToken(TemplateParser.FN_NAME, 0)

        def getRuleIndex(self):
            return TemplateParser.RULE_fn_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFn_name" ):
                listener.enterFn_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFn_name" ):
                listener.exitFn_name(self)




    def fn_name(self):

        localctx = TemplateParser.Fn_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_fn_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(TemplateParser.FN_NAME)
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
            return self.getTypedRuleContext(TemplateParser.Fn_nameContext,0)


        def LPAREN(self):
            return self.getToken(TemplateParser.LPAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TemplateParser.ExprContext)
            else:
                return self.getTypedRuleContext(TemplateParser.ExprContext,i)


        def RPAREN(self):
            return self.getToken(TemplateParser.RPAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(TemplateParser.COMMA)
            else:
                return self.getToken(TemplateParser.COMMA, i)

        def getRuleIndex(self):
            return TemplateParser.RULE_fn_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFn_call" ):
                listener.enterFn_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFn_call" ):
                listener.exitFn_call(self)




    def fn_call(self):

        localctx = TemplateParser.Fn_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_fn_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.fn_name()
            self.state = 82
            self.match(TemplateParser.LPAREN)
            self.state = 83
            self.expr()
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 84
                self.match(TemplateParser.COMMA)
                self.state = 85
                self.expr()
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 91
            self.match(TemplateParser.RPAREN)
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
            return self.getToken(TemplateParser.JSON_PTR, 0)

        def getRuleIndex(self):
            return TemplateParser.RULE_json_ptr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJson_ptr" ):
                listener.enterJson_ptr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJson_ptr" ):
                listener.exitJson_ptr(self)




    def json_ptr(self):

        localctx = TemplateParser.Json_ptrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_json_ptr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(TemplateParser.JSON_PTR)
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
            return self.getToken(TemplateParser.RDF_CLASS, 0)

        def getRuleIndex(self):
            return TemplateParser.RULE_rdf_class

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRdf_class" ):
                listener.enterRdf_class(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRdf_class" ):
                listener.exitRdf_class(self)




    def rdf_class(self):

        localctx = TemplateParser.Rdf_classContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_rdf_class)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(TemplateParser.RDF_CLASS)
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
            return self.getToken(TemplateParser.NUM, 0)

        def getRuleIndex(self):
            return TemplateParser.RULE_num

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNum" ):
                listener.enterNum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNum" ):
                listener.exitNum(self)




    def num(self):

        localctx = TemplateParser.NumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_num)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(TemplateParser.NUM)
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
                return self.getTokens(TemplateParser.ESC_CHAR)
            else:
                return self.getToken(TemplateParser.ESC_CHAR, i)

        def STR_CONTENT(self, i:int=None):
            if i is None:
                return self.getTokens(TemplateParser.STR_CONTENT)
            else:
                return self.getToken(TemplateParser.STR_CONTENT, i)

        def getRuleIndex(self):
            return TemplateParser.RULE_str_content

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStr_content" ):
                listener.enterStr_content(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStr_content" ):
                listener.exitStr_content(self)




    def str_content(self):

        localctx = TemplateParser.Str_contentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_str_content)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27 or _la==28:
                self.state = 99
                _la = self._input.LA(1)
                if not(_la==27 or _la==28):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 104
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
            return self.getToken(TemplateParser.STR_START, 0)

        def str_content(self):
            return self.getTypedRuleContext(TemplateParser.Str_contentContext,0)


        def STR_END(self):
            return self.getToken(TemplateParser.STR_END, 0)

        def getRuleIndex(self):
            return TemplateParser.RULE_str

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStr" ):
                listener.enterStr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStr" ):
                listener.exitStr(self)




    def str_(self):

        localctx = TemplateParser.StrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_str)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(TemplateParser.STR_START)
            self.state = 106
            self.str_content()
            self.state = 107
            self.match(TemplateParser.STR_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





