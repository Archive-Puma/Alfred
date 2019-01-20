class Write:
    def __init__(self):
        self.__nl = '\n'

    def run(self,vars):
        print(vars['quoted'], end=self.__nl)
        return None