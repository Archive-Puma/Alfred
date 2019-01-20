# -*- enconding: utf-8 -*-

class Preprocessor:
    def __init__(self, code):
        self.__jumps  = []
        self.__code   = code
        # Preprocess
        self.__lines()
        self.__unnewlines()
        self.__jumps_comments()

    def __lines(self):
        if type(self.__code) == str:
            self.__code = self.__code.splitlines()
        else:
            raise Exception("[NECESITO ERROR HANDLING] El código no es un String")
    
    def __unnewlines(self):
        if type(self.__code) == list:
            self.__code = list(filter(None,self.__code))
        else:
            raise Exception("[NECESITO ERROR HANDLING] El código no es una Lista")

    def __jumps_comments(self):
        result = []
        for line in self.__code:
            # check if is not a comment
            if line[0] is not '(' and line[len(line)-1] is not ')':
                result.append(line)
        self.__code = result



    def get(self):
        return self.__code,self.__jumps