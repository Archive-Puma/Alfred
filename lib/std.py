"""
Author: @CosasDePuma <kikefontanlorenzo@gmail.com>(https://github.com/cosasdepuma)
"""

# pylint: disable=W0613

def echo(args, evaluator):
    """ Show a message through the stdin """
    print(' '.join(args))

def goto(args, evaluator):
    """ Jump to a new instruction """
    args = args[1:]
    args = ' '.join(args)
    return evaluator.jumps[args]

def halt(args, evaluator):
    """ Stop the program with a clean exit """
    exit(0)
