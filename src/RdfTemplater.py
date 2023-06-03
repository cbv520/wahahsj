# Generated from .\TemplateParser.g4 by ANTLR 4.13.0
from typing import Dict, Callable, List

import jsonpointer
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker

import Functions
import src
from src.generated.TemplateLexer import TemplateLexer
from src.generated.TemplateParser import TemplateParser
from src.generated.TemplateParserListener import TemplateParserListener


# This class defines a complete listener for a parse tree produced by TemplateParser.
class RdfTemplater(TemplateParserListener):

    def __init__(self, template: str):
        self.replacers: Dict[int, Callable[[Dict[str, any]], str]] = {}
        self.fn_args: Dict[int, Dict[int, List[Callable[[Dict[str, any]], str]]]] = {}
        self.curr_stmt = 0
        self.curr_fn = 0
        self.fn_id = 0
        self.fn_stack = []
        lexer = TemplateLexer(InputStream(template))
        parser = src.generated.TemplateParser.TemplateParser(CommonTokenStream(lexer))
        ParseTreeWalker().walk(self, parser.template())

    def apply(self, data: Dict[str, any]):
        out = self.template
        for k, v in self.replacers.items():
            out = out.replace(f'<<REPLACE_{k}>>', v(data))
        return out

    # Enter a parse tree produced by TemplateParser#template.
    def enterTemplate(self, ctx: TemplateParser.TemplateContext):
        self.template = ctx.getText().replace("<EOF>", "")

    # Enter a parse tree produced by TemplateParser#template_stmt.
    def enterTemplate_stmt(self, ctx: TemplateParser.Template_stmtContext):
        self.curr_stmt += 1
        self.template = self.template.replace(ctx.getText(), f'<<REPLACE_{self.curr_stmt}>>')

    # Enter a parse tree produced by TemplateParser#stmt.
    def enterStmt(self, ctx: TemplateParser.StmtContext):
        self.fn_args[self.curr_stmt] = {}
        if ctx.json_ptr():
            self.replacers[self.curr_stmt] = lambda data: jsonpointer.resolve_pointer(data, ctx.json_ptr().JSON_PTR().symbol.text)

    # Enter a parse tree produced by TemplateParser#fn_name.
    def enterFn_name(self, ctx: TemplateParser.Fn_nameContext):
        self.fn_id += 1
        self.curr_fn = self.fn_id
        self.fn_args[self.curr_stmt][self.curr_fn] = []
        proc_step = lambda data, i=self.curr_stmt, j=self.curr_fn: getattr(Functions, ctx.getText())([arg(data) for arg in self.fn_args[i][j]])
        if len(self.fn_stack) == 0:
            self.replacers[self.curr_stmt] = proc_step
        else:
            self.fn_args[self.curr_stmt][self.fn_stack[-1]].append(proc_step)
        self.fn_stack.append(self.curr_fn)

    # Exit a parse tree produced by TemplateParser#fn_call.
    def exitFn_call(self, ctx: TemplateParser.Fn_callContext):
        self.fn_stack.pop()
        if len(self.fn_stack) > 0:
            self.curr_fn = self.fn_stack[-1]

        # Enter a parse tree produced by TemplateParser#json_ptr.
    def enterJson_ptr(self, ctx: TemplateParser.Json_ptrContext):
        self._add_arg(lambda data: str(jsonpointer.resolve_pointer(data, ctx.getText())))

    # Enter a parse tree produced by TemplateParser#rdf_class.
    def enterRdf_class(self, ctx: TemplateParser.Rdf_classContext):
        self._add_arg(lambda data: ctx.getText())

    # Enter a parse tree produced by TemplateParser#num.
    def enterNum(self, ctx: TemplateParser.NumContext):
        self._add_arg(lambda data: ctx.getText())

    # Enter a parse tree produced by TemplateParser#str_content.
    def enterStr_content(self, ctx: TemplateParser.Str_contentContext):
        self._add_arg(lambda data: ctx.getText())

    def _add_arg(self, proc_step: Callable[[Dict[str, any]], str]):
        self.fn_args[self.curr_stmt][self.curr_fn].append(proc_step)


del TemplateParser
