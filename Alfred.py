import sys
from NewLexer import Lexer
from Parser import Parser
from Evaluator import *

debug = False

class Alfred:
    def __init__(self):

        self.keywords = {
            'ADIOS': halt,
            'DI': echo,
            'VETE': goto
        }

        self.lexer = Lexer(self.keywords.keys())
        self.parser = Parser()
        for file_ in sys.argv[1:]:
            self.readLine(file_)

    def readLine(self, _file):
        # Open file in read mode
        with open(_file, 'r') as sourcefile:
            # Read line by line
            for lineofcode in sourcefile:
                # Tokenize the line of code with the lexer
                self.lexer.tokenizer(lineofcode)
                if debug: print('LEXER', self.lexer.tokens)
                self.parser.build(self.lexer.tokens)
        
        if debug:
            print('INSTRUCTION POINTER', self.parser.ipointer)
            print('JUMP TABLE', self.parser.jumps)
            print('INSTRUCTION STACK', self.parser.instructions)
        
        self.evaluator = Evaluator(self.parser.jumps, self.parser.instructions, self.keywords)
        self.evaluator.run()            



if __name__ == '__main__':
    alf = Alfred()