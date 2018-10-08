"""
Author: @CosasDePuma <kikefontanlorenzo@gmail.com>(https://github.com/cosasdepuma)
"""

from importlib import import_module

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
    return args['JUMPS'][args['LABEL']]

def halt(args):
    CODES = {
        'ALFRED': 0
    }
    EXIT_CODE = CODES[args['EXIT_CODE'].upper()]
    exit(EXIT_CODE)

def learn(args):
    lib = "lib.{0}.{1}".format(args['lang'], args['lib'])
    NAME = import_module(lib).NAME
    print(NAME)

def show(args):
    output = None
    if 'NAME' in args:
        output = args['VARIABLES'][args['NAME']]
    echo({'STRING': output, 'VARIABLES': args['VARIABLES']})
