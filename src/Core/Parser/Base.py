# -*- enconding: utf-8 -*-

from ..Language.Translations.ES  import Language

class Parser:
    def __init__(self):
        self.__AST = []

    def __parse(self,loc):
        flag    = None
        temp    = None
        words   = loc.split()
        data    = { 'command': None, 'vars': {} }
        current = Language['Syntax']
        
        # parse word by word
        for word in words:
            # if there is no flag, parse plane text
            if not flag:
                # format input word
                # - lower case
                # - remove accentuated 'o'
                word = word.lower().replace('ó','o')
                # check if the input corresponds to the syntax
                if word in current:
                    # update the syntax (next word)
                    current = current[word]
                    # check if a variable is required
                    if type(current) is dict:
                        # quoted string ("text")
                        if '%quoted%' in current:
                            flag = '%quoted%'
                            temp = None
                        # no variable required (plain text)
                        else:
                            flag = None
            # get quoted strings
            elif flag is '%quoted%':
                # check if it is the first word of the quoted string
                if not temp:
                    # check if it is quoted
                    if word[0] is '"':
                        temp = word[1:]
                    # check if it is only one quoted word
                    if word[len(word)-1] is '"' and word[len(word)-2] is not '\\':
                        flag = None
                        data['vars']['quoted'] = temp
                        temp = None
                # it is not the first word of the quoted string
                else:
                    # add the word to the builder
                    temp = "{0} {1}".format(temp,word)
                    # check if it is the last word and it is not an escaped quote
                    if word[len(word)-1] is '"' and word[len(word)-2] is not '\\':
                        flag = None
                        data['vars']['quoted'] = temp[:-1]
                        temp = None
                # update the syntax (next word)
                if not flag:
                    current = current['%quoted%']
        # if there are no more words and the syntax is ended, get the command
        if type(current) is str:
            data['command'] = current
        # return the command and the variables
        return data if data['command'] else None
        

    def parse(self,code):
        if type(code) is list:
            if code[0].lower() == Language['Invoke']:
                for loc in code[1:]:
                    self.__AST.append(self.__parse(loc))
            else:
                raise Exception("[EXCEPCION CUTRE] Los programas deben empezar con la instrucción \"Alfred\"")
        else:
            raise Exception("[ERROR UN POCO CUTRE] El código no ha sido preprocesado")

    def get(self):
        return self.__AST