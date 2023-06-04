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
        self.cond_replacers: Dict[int, Callable[[Dict[str, any]], str]] = {}
        self.fn_args: Dict[int, Dict[int, List[Callable[[Dict[str, any]], str]]]] = {}
        self.cond_template: Dict[int, str] = {}
        self.curr_stmt = 0
        self.curr_fn = 0
        self.fn_id = 0
        self.fn_stack = []
        self.cond_stack = []
        lexer = TemplateLexer(InputStream(template))
        parser = src.generated.TemplateParser.TemplateParser(CommonTokenStream(lexer))
        ParseTreeWalker().walk(self, parser.root())

    def apply(self, data: Dict[str, any]):
        out = self.template
        for k, v in self.cond_replacers.items():
            out = out.replace(f'<<REPLACE_{k}>>', v(data))
        for k, v in self.replacers.items():
            out = out.replace(f'<<REPLACE_{k}>>', v(data))
        return out

    # Enter a parse tree produced by TemplateParser#template.
    def enterRoot(self, ctx: TemplateParser.TemplateContext):
        self.template = ctx.getText().replace("<EOF>", "")

    # Enter a parse tree produced by TemplateParser#template_stmt.
    def enterTemplate_stmt(self, ctx: TemplateParser.Template_stmtContext):
        print(ctx.getText())
        self.curr_stmt += 1
        self.template = self.template.replace(ctx.getText(), f'<<REPLACE_{self.curr_stmt}>>', 1)
        if self.cond_stack:
            print(self.curr_stmt)
            print(ctx.getText())
            self.cond_template[self.cond_stack[-1]] = self.cond_template[self.cond_stack[-1]].replace(ctx.getText(), f'<<REPLACE_{self.curr_stmt}>>', 1)
            print("PPPP")
            print(self.cond_template[self.cond_stack[-1]])
            print("PPPP")

    # Enter a parse tree produced by TemplateParser#fn_name.
    def enterFn_name(self, ctx: TemplateParser.Fn_nameContext):
        print(ctx.getText())
        self.fn_id += 1
        self.curr_fn = self.fn_id
        self.fn_args[self.curr_stmt] = {}
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
        if self.fn_stack:
            self.curr_fn = self.fn_stack[-1]

        # Enter a parse tree produced by TemplateParser#json_ptr.
    def enterJson_ptr(self, ctx: TemplateParser.Json_ptrContext):
        if self.fn_stack:
            self._add_arg(lambda data: str(jsonpointer.resolve_pointer(data, ctx.getText(), None)))
        else:
            self.replacers[self.curr_stmt] = lambda data: jsonpointer.resolve_pointer(data, ctx.getText())

    # Enter a parse tree produced by TemplateParser#rdf_class.
    def enterRdf_class(self, ctx: TemplateParser.Rdf_classContext):
        self._add_arg(lambda data: ctx.getText())

    # Enter a parse tree produced by TemplateParser#num.
    def enterNum(self, ctx: TemplateParser.NumContext):
        self._add_arg(lambda data: ctx.getText())

    # Enter a parse tree produced by TemplateParser#str_content.
    def enterStr_content(self, ctx: TemplateParser.Str_contentContext):
        self._add_arg(lambda data: ctx.getText())

    def enterCond_template(self, ctx:TemplateParser.Cond_templateContext):
        self.curr_stmt += 1
        self.cond_stack.append(self.curr_stmt)

    def enterCond_template_body(self, ctx:TemplateParser.Cond_startContext):
        self.cond_template[self.curr_stmt] = ctx.getText()


    def exitCond_template(self, ctx:TemplateParser.Cond_templateContext):
        cond = self.cond_stack.pop()
        self.template = self.template.replace(self.cond_template[cond], f'<<REPLACE_{cond}>>')
        print("@@@@@@@@@@@")
        print(self.template)
        print("@@@@@@@@@@@")
        print(ctx.getText())
        print("@@@@@@@@@@@")

    def enterJson_ptr_cond(self, ctx:TemplateParser.Cond_listContext):
        self.cond_replacers[self.curr_stmt] = lambda data, cond=self.cond_stack[-1]: self.sd(data, ctx.getText(), cond)

    def exitCond_start(self, ctx:TemplateParser.Cond_startContext):
        self.template = self.template.replace(f'<<{ctx.getText()}>>', "", 1)

    def exitCond_end(self, ctx:TemplateParser.Cond_endContext):
        self.template = self.template.replace(f'<<{ctx.getText()}>>', "", 1)

    def sd(self, data, ptr, cond):
        print("@@@@@@@@@@@")
        print(data)
        print(ptr)
        print("@@@@@@@@@@@")
        if jsonpointer.resolve_pointer(data, ptr, None) is None:
            return ""
        else:
            return self.cond_template[cond]

    def _add_arg(self, proc_step: Callable[[Dict[str, any]], str]):
        print([[self.curr_stmt],[self.curr_fn]])
        self.fn_args[self.curr_stmt][self.curr_fn].append(proc_step)

    def exitRoot(self, ctx:TemplateParser.RootContext):
        print(self.template)

del TemplateParser
