# -*- enconding: utf-8 -*-

from Core.Parser                import Parser
from Core.Evaluator             import Evaluator
from Core.Source                import Preprocessor
from Core.Environment           import Arguments

def main():
    args = Arguments().parse()
    if args.source:
        parser          = Parser()
        evaluator       = Evaluator()
        preprocessor    = Preprocessor(args.source)

        code,jumps = preprocessor.get()
        
        parser.parse(code)
        ast,jumps = parser.get()

        evaluator.evaluate(ast,jumps)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupción ejecutada")