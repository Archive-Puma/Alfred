# -*- enconding: utf-8 -*-

from Core.Parser.Base           import Parser
from Core.Evaluator.Base        import Evaluator
from Core.Source.Preprocessor   import Preprocessor
from Core.Environment.Arguments import Arguments

if __name__ == '__main__':
    args = Arguments().parse()
    if args.source:
        parser          = Parser()
        evaluator       = Evaluator()
        preprocessor    = Preprocessor(args.source)

        code,jumps = preprocessor.get()
        
        parser.parse(code)
        ast = parser.get()

        evaluator.evaluate(ast)
