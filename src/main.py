# -*- enconding: utf-8 -*-

from Core.Parser                import Parser
from Core.Evaluator             import Evaluator
from Core.Source                import Preprocessor
from Core.Environment           import Arguments

class Main:
    def __init__(self):
        args = Arguments().parse()
        if args.source:
            self.__parser          = Parser()
            self.__evaluator       = Evaluator()
            self.__preprocessor    = Preprocessor(args.source)

    def run(self):
        code,jumps = self.__preprocessor.get()
        
        self.__parser.parse(code)
        ast,jumps = self.__parser.get()

        self.__evaluator.evaluate(ast,jumps)

    def interrupt(self):
        self.__evaluator.interrupt()

if __name__ == '__main__':
    main = Main()
    try:
        main.run()
        while True:
            pass
    except KeyboardInterrupt:
        main.interrupt()