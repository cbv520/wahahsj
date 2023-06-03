import sys

from antlr4 import *

from ExprDataApplier import ExprDataApplier
from src.generated.ExprLexer import ExprLexer
from src.generated.ExprParser import ExprParser


def main(argv):
    input = "sakjd <<LN(rdf:PP, LN('2 ','3\\\\n',LN('4',/id)), 6E10, URL_ENCODE('@@', /jj))>>543 5 ew <<LN('w', /gary)>>"
    lexer = ExprLexer(InputStream(input))
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    dataApplier = ExprDataApplier()
    ParseTreeWalker().walk(dataApplier, parser.template())
    dataApplier.data({'id':111, 'jj': "k", "gary":'grrr'})
   # Functions.__dict__.get("LN")(*[1,2,7][::-1])





if __name__ == '__main__':
    main(sys.argv)


