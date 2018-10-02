"""
Author: @CosasDePuma <kikefontanlorenzo@gmail.com>(https://github.com/cosasdepuma)
"""

# pylint: disable=W0613

import re
from importlib import import_module

def define(args, evaluator):
    """ Define variables """
    args = ' '.join(args).upper()
    # Variable
    name = re.match('.* {0}'.format(evaluator.keywords['=']), args).group()
    # Variable value
    value = re.sub('{0} '.format(name), '', args)
    # Variable name
    name = re.sub(' {0}'.format(evaluator.keywords['=']), '', name)
    # Temporal value
    if value == evaluator.keywords['<<']:
        value = evaluator.variables['___tmp___']
        evaluator.variables.pop('___tmp___', None)
    evaluator.variables[name] = value

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
    lib = re.sub(' ', '_', lib)
    lang = evaluator.lang.lower() + '.' if evaluator.lang else ''
    lib = import_module('lib.' + lang + lib.lower())
    evaluator.keywords[lib.COMMAND] = lib.Lib()

def run(commands, evaluator):
    """ Save the output returned after running a module """
    evaluator.variables['___tmp___'] = _modrun(commands, evaluator).command('get')


def show(commands, evaluator):
    """ Show the output returned after running a module
    or the value of a variable """
    if evaluator.keywords['$$'] in ' '.join(commands).upper():
        _showvar(commands, evaluator)
    else:
        _modrun(commands, evaluator).command('show')


def _modrun(commands, evaluator):
    """ Run a module """
    options = {}
    instruction = None
    instruction_str = None
    # Find the instruction
    cmds = ' '.join(commands).upper().split(' ')
    for keywords in evaluator.keywords:
        if not instruction:
            matches = 0
            keyword = keywords.split(' ')
            for key in keyword:
                if key in cmds:
                    matches += 1
            if matches == len(keyword):
                instruction_str = keywords
                instruction = evaluator.keywords[keywords]
                break
    # Get the arguments
    if instruction:
        txt = ' '.join(commands).upper()
        txt = re.sub(instruction_str, '', txt)
        for arg in instruction.args:
            # Find the next word after the argument
            matches = re.search('({0})\\ .*?\\ '.format(arg), txt)
            if not matches:
                matches = re.search('({0})\\ .*'.format(arg), txt)
            matches = re.sub('({0})'.format(arg), '', matches.group())
            matches = re.sub('\\ ', '', matches)
            # Create the args dictionary
            if matches:
                options = {
                    arg.upper(): matches
                }
    # Run and save the result of the module
    instruction.run(options)
    return instruction

def _showvar(args, evaluator):
    """ Show the value of a variable """
    args = ' '.join(args).upper()
    args = re.sub(evaluator.keywords['$$'], '', args).strip()
    print(evaluator.variables[args])
