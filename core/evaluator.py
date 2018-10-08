# -*- encoding: utf-8 -*-
"""
Author: @CosasDePuma <kikefontanlorenzo@gmail.com>(https://github.com/cosasdepuma)
"""

class Evaluator:
    """ Evaluator component to run the commands """
    def __init__(self, _program, _LANG):
        self.lang = _LANG
        self.jumps = _program[0]
        self.keywords = _program[2]
        self.instructions = _program[1]
        self.variables = { '___tmp___': '', 'ENDL': '\n' }

    def run(self):
        """ Run the instructions """
        ipointer = 0
        while ipointer < len(self.instructions):
            instruction = self.instructions[ipointer]
            if 'JUMPS' in self.keywords['std'][instruction['key']]['args']:
                instruction['args'][self.keywords['std'][instruction['key']]['args']['JUMPS']] = self.jumps
            if 'VARS' in self.keywords['std'][instruction['key']]['args']:
                instruction['args']['VAR_KEYS'] = self.keywords['variables']
                instruction['args'][self.keywords['std'][instruction['key']]['args']['VARS']] = self.variables
            if instruction['lib'] == 'std':
                output = self.keywords['std'][instruction['key']]['function'](instruction['args'])
            ipointer = output if type(output) is int else ipointer + 1
