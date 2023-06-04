# Generated from .\TemplateParser.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .TemplateParser import TemplateParser
else:
    from TemplateParser import TemplateParser

# This class defines a complete listener for a parse tree produced by TemplateParser.
class TemplateParserListener(ParseTreeListener):

    # Enter a parse tree produced by TemplateParser#root.
    def enterRoot(self, ctx:TemplateParser.RootContext):
        pass

    # Exit a parse tree produced by TemplateParser#root.
    def exitRoot(self, ctx:TemplateParser.RootContext):
        pass


    # Enter a parse tree produced by TemplateParser#template.
    def enterTemplate(self, ctx:TemplateParser.TemplateContext):
        pass

    # Exit a parse tree produced by TemplateParser#template.
    def exitTemplate(self, ctx:TemplateParser.TemplateContext):
        pass


    # Enter a parse tree produced by TemplateParser#cond_template.
    def enterCond_template(self, ctx:TemplateParser.Cond_templateContext):
        pass

    # Exit a parse tree produced by TemplateParser#cond_template.
    def exitCond_template(self, ctx:TemplateParser.Cond_templateContext):
        pass


    # Enter a parse tree produced by TemplateParser#cond_template_body.
    def enterCond_template_body(self, ctx:TemplateParser.Cond_template_bodyContext):
        pass

    # Exit a parse tree produced by TemplateParser#cond_template_body.
    def exitCond_template_body(self, ctx:TemplateParser.Cond_template_bodyContext):
        pass


    # Enter a parse tree produced by TemplateParser#template_stmt.
    def enterTemplate_stmt(self, ctx:TemplateParser.Template_stmtContext):
        pass

    # Exit a parse tree produced by TemplateParser#template_stmt.
    def exitTemplate_stmt(self, ctx:TemplateParser.Template_stmtContext):
        pass


    # Enter a parse tree produced by TemplateParser#stmt.
    def enterStmt(self, ctx:TemplateParser.StmtContext):
        pass

    # Exit a parse tree produced by TemplateParser#stmt.
    def exitStmt(self, ctx:TemplateParser.StmtContext):
        pass


    # Enter a parse tree produced by TemplateParser#expr.
    def enterExpr(self, ctx:TemplateParser.ExprContext):
        pass

    # Exit a parse tree produced by TemplateParser#expr.
    def exitExpr(self, ctx:TemplateParser.ExprContext):
        pass


    # Enter a parse tree produced by TemplateParser#cond_start.
    def enterCond_start(self, ctx:TemplateParser.Cond_startContext):
        pass

    # Exit a parse tree produced by TemplateParser#cond_start.
    def exitCond_start(self, ctx:TemplateParser.Cond_startContext):
        pass


    # Enter a parse tree produced by TemplateParser#cond_end.
    def enterCond_end(self, ctx:TemplateParser.Cond_endContext):
        pass

    # Exit a parse tree produced by TemplateParser#cond_end.
    def exitCond_end(self, ctx:TemplateParser.Cond_endContext):
        pass


    # Enter a parse tree produced by TemplateParser#cond_list.
    def enterCond_list(self, ctx:TemplateParser.Cond_listContext):
        pass

    # Exit a parse tree produced by TemplateParser#cond_list.
    def exitCond_list(self, ctx:TemplateParser.Cond_listContext):
        pass


    # Enter a parse tree produced by TemplateParser#json_ptr_cond.
    def enterJson_ptr_cond(self, ctx:TemplateParser.Json_ptr_condContext):
        pass

    # Exit a parse tree produced by TemplateParser#json_ptr_cond.
    def exitJson_ptr_cond(self, ctx:TemplateParser.Json_ptr_condContext):
        pass


    # Enter a parse tree produced by TemplateParser#fn_name.
    def enterFn_name(self, ctx:TemplateParser.Fn_nameContext):
        pass

    # Exit a parse tree produced by TemplateParser#fn_name.
    def exitFn_name(self, ctx:TemplateParser.Fn_nameContext):
        pass


    # Enter a parse tree produced by TemplateParser#fn_call.
    def enterFn_call(self, ctx:TemplateParser.Fn_callContext):
        pass

    # Exit a parse tree produced by TemplateParser#fn_call.
    def exitFn_call(self, ctx:TemplateParser.Fn_callContext):
        pass


    # Enter a parse tree produced by TemplateParser#json_ptr.
    def enterJson_ptr(self, ctx:TemplateParser.Json_ptrContext):
        pass

    # Exit a parse tree produced by TemplateParser#json_ptr.
    def exitJson_ptr(self, ctx:TemplateParser.Json_ptrContext):
        pass


    # Enter a parse tree produced by TemplateParser#rdf_class.
    def enterRdf_class(self, ctx:TemplateParser.Rdf_classContext):
        pass

    # Exit a parse tree produced by TemplateParser#rdf_class.
    def exitRdf_class(self, ctx:TemplateParser.Rdf_classContext):
        pass


    # Enter a parse tree produced by TemplateParser#num.
    def enterNum(self, ctx:TemplateParser.NumContext):
        pass

    # Exit a parse tree produced by TemplateParser#num.
    def exitNum(self, ctx:TemplateParser.NumContext):
        pass


    # Enter a parse tree produced by TemplateParser#str_content.
    def enterStr_content(self, ctx:TemplateParser.Str_contentContext):
        pass

    # Exit a parse tree produced by TemplateParser#str_content.
    def exitStr_content(self, ctx:TemplateParser.Str_contentContext):
        pass


    # Enter a parse tree produced by TemplateParser#str.
    def enterStr(self, ctx:TemplateParser.StrContext):
        pass

    # Exit a parse tree produced by TemplateParser#str.
    def exitStr(self, ctx:TemplateParser.StrContext):
        pass



del TemplateParser