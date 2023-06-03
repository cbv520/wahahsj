# Generated from .\ExprParser.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprParserListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#template.
    def enterTemplate(self, ctx:ExprParser.TemplateContext):
        pass

    # Exit a parse tree produced by ExprParser#template.
    def exitTemplate(self, ctx:ExprParser.TemplateContext):
        pass


    # Enter a parse tree produced by ExprParser#template_stmt.
    def enterTemplate_stmt(self, ctx:ExprParser.Template_stmtContext):
        pass

    # Exit a parse tree produced by ExprParser#template_stmt.
    def exitTemplate_stmt(self, ctx:ExprParser.Template_stmtContext):
        pass


    # Enter a parse tree produced by ExprParser#stmt.
    def enterStmt(self, ctx:ExprParser.StmtContext):
        pass

    # Exit a parse tree produced by ExprParser#stmt.
    def exitStmt(self, ctx:ExprParser.StmtContext):
        pass


    # Enter a parse tree produced by ExprParser#expr.
    def enterExpr(self, ctx:ExprParser.ExprContext):
        pass

    # Exit a parse tree produced by ExprParser#expr.
    def exitExpr(self, ctx:ExprParser.ExprContext):
        pass


    # Enter a parse tree produced by ExprParser#fn_name.
    def enterFn_name(self, ctx:ExprParser.Fn_nameContext):
        pass

    # Exit a parse tree produced by ExprParser#fn_name.
    def exitFn_name(self, ctx:ExprParser.Fn_nameContext):
        pass


    # Enter a parse tree produced by ExprParser#fn_call.
    def enterFn_call(self, ctx:ExprParser.Fn_callContext):
        pass

    # Exit a parse tree produced by ExprParser#fn_call.
    def exitFn_call(self, ctx:ExprParser.Fn_callContext):
        pass


    # Enter a parse tree produced by ExprParser#json_ptr.
    def enterJson_ptr(self, ctx:ExprParser.Json_ptrContext):
        pass

    # Exit a parse tree produced by ExprParser#json_ptr.
    def exitJson_ptr(self, ctx:ExprParser.Json_ptrContext):
        pass


    # Enter a parse tree produced by ExprParser#rdf_class.
    def enterRdf_class(self, ctx:ExprParser.Rdf_classContext):
        pass

    # Exit a parse tree produced by ExprParser#rdf_class.
    def exitRdf_class(self, ctx:ExprParser.Rdf_classContext):
        pass


    # Enter a parse tree produced by ExprParser#num.
    def enterNum(self, ctx:ExprParser.NumContext):
        pass

    # Exit a parse tree produced by ExprParser#num.
    def exitNum(self, ctx:ExprParser.NumContext):
        pass


    # Enter a parse tree produced by ExprParser#str_content.
    def enterStr_content(self, ctx:ExprParser.Str_contentContext):
        pass

    # Exit a parse tree produced by ExprParser#str_content.
    def exitStr_content(self, ctx:ExprParser.Str_contentContext):
        pass


    # Enter a parse tree produced by ExprParser#str.
    def enterStr(self, ctx:ExprParser.StrContext):
        pass

    # Exit a parse tree produced by ExprParser#str.
    def exitStr(self, ctx:ExprParser.StrContext):
        pass



del ExprParser