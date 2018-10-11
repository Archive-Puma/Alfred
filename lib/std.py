"""
Author: @CosasDePuma <kikefontanlorenzo@gmail.com>(https://github.com/cosasdepuma)
"""

from importlib import import_module

def _solve_expressions(expr, variables):
    print(expr)
    return False

def define(args):
    if args['VALUE'].upper() in args['VAR_KEYS']['output']:
        args['VALUE'] = args['VARIABLES']['___tmp___']
    if args['NAME'].upper() in args['VAR_KEYS']['endl']:
        args['NAME'] = 'ENDL'
        if (args['VALUE'][0] == '\'' and args['VALUE'][-1] == '\'') or \
           (args['VALUE'][0] == '\"' and args['VALUE'][-1] == '\"'):
           args['VALUE'] = args['VALUE'][1:-1]
    args['VARIABLES'][args['NAME']] = args['VALUE']

def echo(args):
    endl = args['VARIABLES']['ENDL']
    if endl == '\\n':
        endl = '\n'
    if args['STRING']:
        print(args['STRING'], end=endl)

def goto(args):
    ipointer = None
    if args['CONDITIONAL']:
        if _solve_expressions(args['CONDITIONAL'], args['VAR_KEYS']):
            ipointer = args['JUMPS'][args['CONDITIONAL JUMP']]
    else:
        ipointer = args['JUMPS'][args['LABEL']]
    return ipointer

def halt(args):
    CODES = {
        'ALFRED': 0
    }
    EXIT_CODE = CODES[args['EXIT_CODE'].upper()] if args['EXIT_CODE'].upper() in CODES else -1
    exit(EXIT_CODE)

def learn(args):
    lib = "lib.{0}.{1}".format(args['lang'], args['lib'])
    config = import_module(lib).LIB_CONFIGURATION
    return config['COMMANDS']

def show(args):
    output = None
    if 'NAME' in args:
        if args['NAME'].upper() in args['VAR_KEYS']['output']:
            output = args['VARIABLES']['___tmp___']
        else:
            output = args['VARIABLES'][args['NAME']]
    echo({'STRING': output, 'VARIABLES': args['VARIABLES']})
