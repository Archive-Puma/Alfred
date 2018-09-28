"""
Author: @CosasDePuma <kikefontanlorenzo@gmail.com>(https://github.com/cosasdepuma)
"""

import sys

# Import the core of the program
from config.lang import manager
from core.parser import Parser
from core.lexer import Lexer
from core.evaluator import Evaluator

# Configuration variables
LANG = "ES"
VERBOSE = True

class Alfred:
    """ Class with the program behaviour """
    def __init__(self):
        # Implement some commands
        language = manager(LANG)
        self.keywords = language[0]
        self.controlflow_keywords = language[1]

        # Create the lexer, the parser and the evaluator
        self.evaluator = None
        self.parser = Parser()
        self.lexer = Lexer(self.keywords.keys(), self.controlflow_keywords)

    def start(self):
        """ Start the module by reading the files
        and executing the commands """
        # Execute file by file
        for file_ in sys.argv[1:]:
            # Read the code
            self.read(file_)
            # Execute the code
            self.run()

    def read(self, _file):
        """ Read the file given """
        # Open file in read mode
        with open(_file, 'r') as sourcefile:
            # Process the code
            self.process(sourcefile)

    def process(self, _sourcefile):
        """ Process the code line by line creating
        the tokens and building the commands """
        # Read line by line
        for lineofcode in _sourcefile:
            # Tokenize the line of code with the lexer
            self.lexer.tokenizer(lineofcode)
            # Build the program with the parser
            self.parser.build(self.lexer.tokens)

    def run(self):
        """ Run the program executing the commands """
        # Some verbose logs
        if VERBOSE:
            self.parser.string()
        # Run the built program with the evaluator
        self.evaluator = Evaluator(self.parser.jumps, self.parser.instructions, self.keywords)
        self.evaluator.run()



if __name__ == '__main__':
    ALF = Alfred()
    ALF.start()