import os
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

        self.config = {
            'Alfred_DIR': os.path.dirname(os.path.realpath(__file__)),
            'Alfred_CORE': os.path.join(os.path.dirname(os.path.realpath(__file__)), 'core')
        }

        print(self.config)
    
    def config(self):
        pass

    def start(self):
        # Execute file by file
        for file_ in sys.argv[1:]:
            # Read the code
            source = self.read(file_)
            # Execute the code
            self.run()

    def read(self, _file):
        source = None
        # Open file in read mode
        with open(_file, 'r') as sourcefile:
            # Process the code
            self.process(sourcefile)

    def process(self, _sourcefile):
        # Read line by line
        for lineofcode in _sourcefile:
            # Tokenize the line of code with the lexer
            self.lexer.tokenizer(lineofcode)
            # Some debug logs
            if debug: print('LEXER', self.lexer.tokens)
            # Build the program with the parser
            self.parser.build(self.lexer.tokens)

    def run(self):
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
    alf.start()
