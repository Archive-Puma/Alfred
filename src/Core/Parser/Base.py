# -*- enconding: utf-8 -*-

import re

from ..Language.Translations.ES  import Language

class Parser:
    def __init__(self):
        self.__AST = []

    def __regex(self,loc):
        ast     = dict()
        index   = 0
        result  = None
        Instructions    = Language['Syntax'][loc[0].lower()]
        Pattern         = list(Instructions.keys())
        while not result and index < len(Pattern):
            result = re.search(Pattern[index], loc, flags=re.IGNORECASE)
            if result:
                ast = { 'command': Instructions[Pattern[index]], 'vars': {} }
                for variable in list(result.groupdict().keys()):
                    ast['vars'][variable] = result.group(variable)
            index = index + 1
        return ast


    def parse(self,code):
        if type(code) is list:
            if code[0].lower() == Language['Invoke']:
                for loc in code[1:]:
                    self.__AST.append(self.__regex(loc))
            else:
                raise Exception("[EXCEPCION CUTRE] Los programas deben empezar con la instrucción \"Alfred\"")
        else:
            raise Exception("[ERROR UN POCO CUTRE] El código no ha sido preprocesado")

    def get(self):
        return self.__AST