# Generated from .\ExprParser.g4 by ANTLR 4.13.0
import json
from typing import Dict, Callable, List

import jsonpointer

import Functions
from src.generated.ExprParserListener import ExprParserListener

if "." in __name__:
    from src.generated.ExprParser import ExprParser
else:
    from src.generated.ExprParser import ExprParser


# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprDataApplier(ExprParserListener):

    def __init__(self):
        self.template: str = ''
        self.replacers: Dict[int, Callable[[Dict[str, any]], str]] = {}
        self.fn_args: Dict[int, Dict[int, List[Callable[[Dict[str, any]], str]]]] = {}
        self.curr_stmt = 0
        self.curr_fn = 0
        self.fn_depth = 0

    def data(self, data: Dict[str, any]):
        out = self.template
        for k, v in self.replacers.items():
            print(out + "hhhhhhhhhhhhh")
            out = out.replace(f'<<REPLACE_{k}>>', v(data))
            print(out)
        return out

    # Enter a parse tree produced by ExprParser#template.
    def enterTemplate(self, ctx: ExprParser.TemplateContext):
        self.template = ctx.getText().replace("<EOF>", "")

    # Exit a parse tree produced by ExprParser#template.
    def exitTemplate(self, ctx: ExprParser.TemplateContext):
        pass

    # Enter a parse tree produced by ExprParser#template_stmt.
    def enterTemplate_stmt(self, ctx: ExprParser.Template_stmtContext):
        self.curr_stmt += 1
        self.template = self.template.replace(ctx.getText(), f'<<REPLACE_{self.curr_stmt}>>')

    # Exit a parse tree produced by ExprParser#template_stmt.
    def exitTemplate_stmt(self, ctx: ExprParser.Template_stmtContext):
        pass

    # Enter a parse tree produced by ExprParser#stmt.
    def enterStmt(self, ctx: ExprParser.StmtContext):
        self.fn_depth = 0
        self.curr_fn = 0
        self.fn_args[self.curr_stmt] = {}
        if ctx.json_ptr():
            self.replacers[self.curr_stmt] = lambda data: jsonpointer.resolve_pointer(data, ctx.json_ptr().JSON_PTR().symbol.text)

    # Exit a parse tree produced by ExprParser#stmt.
    def exitStmt(self, ctx:ExprParser.StmtContext):
        print(json.dumps(self.fn_args, indent=2, default=str))
        print(json.dumps(self.replacers, indent=2, default=str))

    # Enter a parse tree produced by ExprParser#fn_name.
    def enterFn_name(self, ctx: ExprParser.Fn_nameContext):
        self.fn_depth += 1
        self.curr_fn += 1
        self.fn_args[self.curr_stmt][self.curr_fn] = []
        proc_step = lambda data, i=self.curr_stmt, j=self.curr_fn: getattr(Functions, ctx.getText())([arg(data) for arg in self.fn_args[i][j]])
        if self.curr_fn == 1:
            self.replacers[self.curr_stmt] = proc_step
        else:
            self.fn_args[self.curr_stmt][self.fn_depth - 1].append(proc_step)

    # Exit a parse tree produced by ExprParser#fn_call.
    def exitFn_call(self, ctx: ExprParser.Fn_callContext):
        self.fn_depth -= 1

    # Enter a parse tree produced by ExprParser#json_ptr.
    def enterJson_ptr(self, ctx: ExprParser.Json_ptrContext):
        self._add_arg(lambda data: str(jsonpointer.resolve_pointer(data, ctx.getText())))

    # Enter a parse tree produced by ExprParser#rdf_class.
    def enterRdf_class(self, ctx: ExprParser.Rdf_classContext):
        self._add_arg(lambda data: ctx.getText())

    # Enter a parse tree produced by ExprParser#num.
    def enterNum(self, ctx: ExprParser.NumContext):
        self._add_arg(lambda data: ctx.getText())

    # Enter a parse tree produced by ExprParser#str_content.
    def enterStr_content(self, ctx: ExprParser.Str_contentContext):
        self._add_arg(lambda data: ctx.getText())

    def _add_arg(self, proc_step: Callable[[Dict[str, any]], str]):
        self.fn_args[self.curr_stmt][self.curr_fn].append(proc_step)


del ExprParser
