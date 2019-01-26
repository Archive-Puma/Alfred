class Type:
    def __init__(self):
        self.__nl = '\n'
        self.__types = {
            str: 'Texto',
            int: 'Entero',
            float: 'Decimal'
        }

    def run(self,variables,env=None):
        name = variables['name']
        variable = env['variables'][name]
        vartype = type(variable)
        
        print(self.__types[vartype], end=self.__nl)
        return None


class Variable:
    def __init__(self):
        self.__nl = '\n'

    def run(self,variables,env=None):
        name = variables['name']
        variable = env['variables'][name]
        print(variable, end=self.__nl)
        return None