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
        4,1,28,118,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,1,0,1,1,1,1,1,1,
        1,1,4,1,44,8,1,11,1,12,1,45,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,
        1,3,1,4,1,4,1,4,1,4,1,5,1,5,3,5,64,8,5,1,6,1,6,1,6,1,6,1,6,3,6,71,
        8,6,1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,9,5,9,81,8,9,10,9,12,9,84,9,9,
        1,10,1,10,1,11,1,11,1,12,1,12,1,12,1,12,1,12,5,12,95,8,12,10,12,
        12,12,98,9,12,1,12,1,12,1,13,1,13,1,14,1,14,1,15,1,15,1,16,5,16,
        109,8,16,10,16,12,16,112,9,16,1,17,1,17,1,17,1,17,1,17,0,0,18,0,
        2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,0,1,1,0,27,28,111,
        0,36,1,0,0,0,2,43,1,0,0,0,4,47,1,0,0,0,6,55,1,0,0,0,8,57,1,0,0,0,
        10,63,1,0,0,0,12,70,1,0,0,0,14,72,1,0,0,0,16,75,1,0,0,0,18,77,1,
        0,0,0,20,85,1,0,0,0,22,87,1,0,0,0,24,89,1,0,0,0,26,101,1,0,0,0,28,
        103,1,0,0,0,30,105,1,0,0,0,32,110,1,0,0,0,34,113,1,0,0,0,36,37,3,
        2,1,0,37,38,5,0,0,1,38,1,1,0,0,0,39,44,5,1,0,0,40,44,3,8,4,0,41,
        44,3,4,2,0,42,44,5,3,0,0,43,39,1,0,0,0,43,40,1,0,0,0,43,41,1,0,0,
        0,43,42,1,0,0,0,44,45,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,3,1,
        0,0,0,47,48,5,2,0,0,48,49,3,14,7,0,49,50,5,4,0,0,50,51,3,6,3,0,51,
        52,5,2,0,0,52,53,3,16,8,0,53,54,5,4,0,0,54,5,1,0,0,0,55,56,3,2,1,
        0,56,7,1,0,0,0,57,58,5,2,0,0,58,59,3,10,5,0,59,60,5,4,0,0,60,9,1,
        0,0,0,61,64,3,24,12,0,62,64,3,26,13,0,63,61,1,0,0,0,63,62,1,0,0,
        0,64,11,1,0,0,0,65,71,3,24,12,0,66,71,3,26,13,0,67,71,3,28,14,0,
        68,71,3,30,15,0,69,71,3,34,17,0,70,65,1,0,0,0,70,66,1,0,0,0,70,67,
        1,0,0,0,70,68,1,0,0,0,70,69,1,0,0,0,71,13,1,0,0,0,72,73,5,16,0,0,
        73,74,3,18,9,0,74,15,1,0,0,0,75,76,5,17,0,0,76,17,1,0,0,0,77,82,
        3,20,10,0,78,79,5,15,0,0,79,81,3,20,10,0,80,78,1,0,0,0,81,84,1,0,
        0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,19,1,0,0,0,84,82,1,0,0,0,85,86,
        5,21,0,0,86,21,1,0,0,0,87,88,5,19,0,0,88,23,1,0,0,0,89,90,3,22,11,
        0,90,91,5,8,0,0,91,96,3,12,6,0,92,93,5,5,0,0,93,95,3,12,6,0,94,92,
        1,0,0,0,95,98,1,0,0,0,96,94,1,0,0,0,96,97,1,0,0,0,97,99,1,0,0,0,
        98,96,1,0,0,0,99,100,5,9,0,0,100,25,1,0,0,0,101,102,5,21,0,0,102,
        27,1,0,0,0,103,104,5,22,0,0,104,29,1,0,0,0,105,106,5,18,0,0,106,
        31,1,0,0,0,107,109,7,0,0,0,108,107,1,0,0,0,109,112,1,0,0,0,110,108,
        1,0,0,0,110,111,1,0,0,0,111,33,1,0,0,0,112,110,1,0,0,0,113,114,5,
        24,0,0,114,115,3,32,16,0,115,116,5,25,0,0,116,35,1,0,0,0,7,43,45,
        63,70,82,96,110
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
    RULE_cond_template_body = 3
    RULE_template_stmt = 4
    RULE_stmt = 5
    RULE_expr = 6
    RULE_cond_start = 7
    RULE_cond_end = 8
    RULE_cond_list = 9
    RULE_json_ptr_cond = 10
    RULE_fn_name = 11
    RULE_fn_call = 12
    RULE_json_ptr = 13
    RULE_rdf_class = 14
    RULE_num = 15
    RULE_str_content = 16
    RULE_str = 17

    ruleNames =  [ "root", "template", "cond_template", "cond_template_body", 
                   "template_stmt", "stmt", "expr", "cond_start", "cond_end", 
                   "cond_list", "json_ptr_cond", "fn_name", "fn_call", "json_ptr", 
                   "rdf_class", "num", "str_content", "str" ]

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
            self.state = 36
            self.template()
            self.state = 37
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
            self.state = 43 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 43
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        self.state = 39
                        self.match(TemplateParser.TEMPLATE_TEXT)
                        pass

                    elif la_ == 2:
                        self.state = 40
                        self.template_stmt()
                        pass

                    elif la_ == 3:
                        self.state = 41
                        self.cond_template()
                        pass

                    elif la_ == 4:
                        self.state = 42
                        self.match(TemplateParser.NOT_STMT)
                        pass



                else:
                    raise NoViableAltException(self)
                self.state = 45 
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

        def cond_template_body(self):
            return self.getTypedRuleContext(TemplateParser.Cond_template_bodyContext,0)


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
            self.state = 47
            self.match(TemplateParser.STMT_START)
            self.state = 48
            self.cond_start()
            self.state = 49
            self.match(TemplateParser.STMT_END)
            self.state = 50
            self.cond_template_body()
            self.state = 51
            self.match(TemplateParser.STMT_START)
            self.state = 52
            self.cond_end()
            self.state = 53
            self.match(TemplateParser.STMT_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cond_template_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def template(self):
            return self.getTypedRuleContext(TemplateParser.TemplateContext,0)


        def getRuleIndex(self):
            return TemplateParser.RULE_cond_template_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCond_template_body" ):
                listener.enterCond_template_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCond_template_body" ):
                listener.exitCond_template_body(self)




    def cond_template_body(self):

        localctx = TemplateParser.Cond_template_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_cond_template_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.template()
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
        self.enterRule(localctx, 8, self.RULE_template_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(TemplateParser.STMT_START)
            self.state = 58
            self.stmt()
            self.state = 59
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
        self.enterRule(localctx, 10, self.RULE_stmt)
        try:
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.fn_call()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 62
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
        self.enterRule(localctx, 12, self.RULE_expr)
        try:
            self.state = 70
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 65
                self.fn_call()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.json_ptr()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 67
                self.rdf_class()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 4)
                self.state = 68
                self.num()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 5)
                self.state = 69
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
        self.enterRule(localctx, 14, self.RULE_cond_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(TemplateParser.COND_START)
            self.state = 73
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
        self.enterRule(localctx, 16, self.RULE_cond_end)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
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

        def json_ptr_cond(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TemplateParser.Json_ptr_condContext)
            else:
                return self.getTypedRuleContext(TemplateParser.Json_ptr_condContext,i)


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
        self.enterRule(localctx, 18, self.RULE_cond_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.json_ptr_cond()
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 78
                self.match(TemplateParser.AND)
                self.state = 79
                self.json_ptr_cond()
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Json_ptr_condContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def JSON_PTR(self):
            return self.getToken(TemplateParser.JSON_PTR, 0)

        def getRuleIndex(self):
            return TemplateParser.RULE_json_ptr_cond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJson_ptr_cond" ):
                listener.enterJson_ptr_cond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJson_ptr_cond" ):
                listener.exitJson_ptr_cond(self)




    def json_ptr_cond(self):

        localctx = TemplateParser.Json_ptr_condContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_json_ptr_cond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(TemplateParser.JSON_PTR)
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
        self.enterRule(localctx, 22, self.RULE_fn_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
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
        self.enterRule(localctx, 24, self.RULE_fn_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.fn_name()
            self.state = 90
            self.match(TemplateParser.LPAREN)
            self.state = 91
            self.expr()
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 92
                self.match(TemplateParser.COMMA)
                self.state = 93
                self.expr()
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 99
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
        self.enterRule(localctx, 26, self.RULE_json_ptr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
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
        self.enterRule(localctx, 28, self.RULE_rdf_class)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
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
        self.enterRule(localctx, 30, self.RULE_num)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
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
        self.enterRule(localctx, 32, self.RULE_str_content)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==27 or _la==28:
                self.state = 107
                _la = self._input.LA(1)
                if not(_la==27 or _la==28):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 112
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
        self.enterRule(localctx, 34, self.RULE_str)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(TemplateParser.STR_START)
            self.state = 114
            self.str_content()
            self.state = 115
            self.match(TemplateParser.STR_END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





