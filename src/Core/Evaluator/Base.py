from ..Language.Binds import Functions

class Evaluator:
    def __init__(self):
        self.__variables = {}
        self.__environment = {
            'jumps':    dict(),
            'variable': self.__variables
        }

    def evaluate(self,ast,jumps):
        ipointer = 0
        self.__environment['jumps'] = jumps
        while ipointer < len(ast):
            instruction = ast[ipointer]
            if instruction:
                tree = instruction['command'].split('.')
                command = Functions
                for depth in tree:
                    command = command[depth]
                result = command.run(instruction['vars'],self.__environment)

                if result:
                    keys = list(result.keys())
                    if 'jump' in keys:
                        ipointer = result['jump']
                    if 'variable' in keys:
                        var = result['variable']
                        self.__variables[var['name']] = var['value']
            else:
                print("[ERROR NO CONTROLADO] No existe la instrucción de la línea " + str(ipointer))
            ipointer = ipointer + 1