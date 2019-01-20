class Write:
    def __init__(self):
        self.__nl = '\n'

    def run(self,variables,env=None):
        print(variables['text'], end=self.__nl)
        return None