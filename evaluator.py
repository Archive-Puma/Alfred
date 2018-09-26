"""
Author: @CosasDePuma <kikefontanlorenzo@gmail.com>(https://github.com/cosasdepuma)
"""

BAD_EXIT_STATUS_CODE = 0x4a4f4b4552 # Joker

class Evaluator:
    """ Evaluator component to run the commands """
    def __init__(self, _jumps, _instructions, _keywords):
        self.jumps = _jumps
        self._keywords = _keywords
        self.instructions = _instructions

    def run(self):
        """ Run the instructions """
        # Declare the instruction pointer
        pointer = 0
        # Run while there are instructions
        while pointer < len(self.instructions):
            # Get the next instruction
            instruction = self.instructions[pointer]
            # Run the instruction
            direction = self._keywords[instruction[0]](instruction[1:], self)
            # Modify the instruction pointer if last command return the new direction
            pointer = pointer + 1 if not direction else direction
        # Exit with a -1 code if the program not end with a halt instruction
        exit(BAD_EXIT_STATUS_CODE)


#   ____________________________
#  /                            \
# |         INSTRUCTIONS         |
#  \____________________________/

# Prints a message in stdin
def echo(args, eval):
    print(' '.join(args))

# Jump to a new instruction
def goto(args, eval):
    args = args[1:]
    args = ' '.join(args)
    return eval.jumps[args]

# Stop the program with a clean exit
def halt(args, eval):
    exit(0)
