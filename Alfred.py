import sys

# Import the core of the program
from Lexer import Lexer
from Parser import Parser
from Evaluator import *

# Debug flag to show logs
debug = False

class Alfred:
    def __init__(self):
        # Implement some commands
        self.keywords = {
            'ADIOS': halt,
            'DI': echo,
            'VETE': goto
        }
        # Create the lexer and the parser
        self.lexer = Lexer(self.keywords.keys())
        self.parser = Parser()
        # Read all the files
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
                # Build the program with the parser
                self.parser.build(self.lexer.tokens)
        # Some debug logs
        if debug:
            print('INSTRUCTION POINTER', self.parser.ipointer)
            print('JUMP TABLE', self.parser.jumps)
            print('INSTRUCTION STACK', self.parser.instructions)
        # Run the built program with the evaluator
        self.evaluator = Evaluator(self.parser.jumps, self.parser.instructions, self.keywords)
        self.evaluator.run()


if __name__ == '__main__':
    alf = Alfred()
