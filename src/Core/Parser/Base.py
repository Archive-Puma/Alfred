# -*- enconding: utf-8 -*-

import re

from ..Language import ES as Language

class Parser:
    def __init__(self):
        self.__IP = -1
        self.__AST = []
        self.__JUMPS = {}

        self.__defJump = Language['Syntax']['?']

    def __regex(self,loc):
        print(loc)
        ast     = dict()
        index   = 0
        result  = None
        Instructions    = Language['Syntax'][loc[0].lower()]
        Pattern         = list(Instructions.keys())

        while not result and index < len(self.__defJump):
            result = re.search(self.__defJump[index], loc, flags=re.IGNORECASE)
            index = index + 1

        if result:
            name = result.group('name').lower()
            self.__JUMPS[name] = self.__IP
        else:
            index = 0
            self.__IP = self.__IP + 1
            while not result and index < len(Pattern):
                result = re.search(Pattern[index], loc, flags=re.IGNORECASE)
                if result:
                    ast = { 'command': Instructions[Pattern[index]], 'vars': {} }
                    for variable in list(result.groupdict().keys()):
                        value = result.group(variable)
                        if variable == 'name':
                           value = value.lower()
                        elif variable == 'value':
                            if value.isnumeric():
                                value = int(value)
                        elif variable == 'number':
                            value = int(value)
                        ast['vars'][variable] = value
                    self.__AST.append(ast)
                index = index + 1


    def parse(self,code):
        if type(code) is list:
            if code[0].lower() == Language['Invoke']:
                for loc in code[1:]:
                    self.__regex(loc)
            else:
                raise Exception("[EXCEPCION CUTRE] Los programas deben empezar con la instrucción \"Alfred\"")
        else:
            raise Exception("[ERROR UN POCO CUTRE] El código no ha sido preprocesado")

    def get(self):
        return self.__AST, self.__JUMPS