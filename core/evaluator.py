"""
Author: @CosasDePuma <kikefontanlorenzo@gmail.com>(https://github.com/cosasdepuma)
"""

# pylint: disable=R0903

BAD_EXIT_STATUS_CODE = 0x4a4f4b4552 # Joker

class Evaluator:
    """ Evaluator component to run the commands """
    def __init__(self, _program, _LANG):
        self.lang = _LANG
        self.jumps = _program[0]
        self.keywords = _program[2]
        self.instructions = _program[1]

    def run(self):
        """ Run the instructions """
        # Declare the instruction pointer
        pointer = 0
        # Run while there are instructions
        while pointer < len(self.instructions):
            # Get the next instruction
            instruction = self.instructions[pointer]
            # Run the instruction
            direction = self.keywords[instruction[0]](instruction[1:], self)
            # Modify the instruction pointer if last command return the new direction
            pointer = pointer + 1 if not direction else direction
        # Exit with a -1 code if the program not end with a halt instruction
        exit(BAD_EXIT_STATUS_CODE)
