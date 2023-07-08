from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, List
import jsonpointer

"""
<<- for $i in /g >>
<<$i/j/k>>
<<- endfor >>
"""

@dataclass
class Ctx:
    data: Dict[str, any]
    vars: Dict[str, any]


@dataclass
class Expr(ABC):
    @abstractmethod
    def interpret(self, ctx: Ctx) -> any:
        pass

@dataclass
class ExprTemplate(Expr):
    exprs: List[Expr]

    def interpret(self, ctx: Ctx) -> str:
        return ''.join([str(expr.interpret(ctx)) for expr in self.exprs])

@dataclass
class ExprTemplateStr(Expr):
    string: str

    def interpret(self, ctx: Ctx) -> str:
        return self.string
    
@dataclass
class ExprJsonPtr(Expr):
    ptr: str

    def interpret(self, ctx: Ctx) -> any:
        return jsonpointer.resolve_pointer(ctx.data, self.ptr, None)
    
@dataclass
class ExprVar(Expr):
    var: str

    def interpret(self, ctx: Ctx) -> any:
        return ctx.vars[self.var]
    
@dataclass
class ExprVarJsonPtr(Expr):
    var: str
    ptr: str

    def interpret(self, ctx: Ctx) -> any:
        return jsonpointer.resolve_pointer(ctx.vars[self.var], self.ptr, None)

@dataclass
class ExprForList(Expr):
    var: str
    ptr: str
    template: ExprTemplate

    def interpret(self, ctx: Ctx) -> str:
        ls = jsonpointer.resolve_pointer(ctx, self.ptr, None)
        sb = ''
        for i in ls:
            ctx.vars[self.var] = i
            sb += self.template.interpret(ctx)
        return sb
    
@dataclass
class ExprForObj(Expr):
    k_var: str
    v_var: str
    ptr: str
    template: ExprTemplate

    def interpret(self, ctx: Ctx) -> str:
        if self.ptr == '/':
            obj = ctx.data
        else:
            obj = jsonpointer.resolve_pointer(ctx.data, self.ptr, None)
        sb = ''
        for k, v in obj.items():
            ctx.vars[self.k_var] = k
            ctx.vars[self.v_var] = v
            sb += self.template.interpret(ctx)
        return sb
    
tree = ExprForObj(
    'k', 'v', '/', 
    ExprTemplate([
        ExprTemplateStr('test '), 
        ExprVar('k'), 
        ExprTemplateStr(' :: '),
        ExprVarJsonPtr('v', '/name'),
        ExprTemplateStr('\n')
    ]))

print(tree.interpret(Ctx({'a':{'name': 'n1'}, 'b':{'name': 'n2'}, 'c':{'name': 'n3'}}, {})))
