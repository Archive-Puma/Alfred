"""
Author: @CosasDePuma <kikefontanlorenzo@gmail.com>(https://github.com/cosasdepuma)
"""

# pylint: disable=W0613

import re
from importlib import import_module

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

def learn(args, evaluator):
    """ Stop the program with a clean exit """
    lib = ' '.join(args[1:]).upper()
    lang = evaluator.lang.lower() + '-' if evaluator.lang else ''
    evaluator.keywords[lib] = import_module('lib.' + lang + lib.lower()).Lib()

def show(commands, evaluator):
    """ Show the output returned after running a module """
    options = {}
    instruction = None
    # Find the instruction
    for cmd in commands:
        if not instruction:
            cmd = cmd.upper()
            if cmd in evaluator.keywords.keys():
                instruction = evaluator.keywords[cmd]
    # Get the arguments
    if instruction:
        txt = ' '.join(commands).upper()
        for arg in instruction.args:
            # Find the next word after the argument
            matches = re.search('({0})\\ \\w+'.format(arg), txt).group()
            matches = re.sub('({0})\\ '.format(arg), '', matches)
            # Create the args dictionary
            if matches:
                options = {
                    arg.upper(): matches
                }
    # Run and show the module
    instruction.run(options)
    instruction.command('show')
