from ..Language.Binds import Functions

class Evaluator:
    def __init__(self):
        self.__variables = {}

    def evaluate(self,ast):
        ipointer = 0
        while ipointer < len(ast):
            instruction = ast[ipointer]
            if instruction:
                tree = instruction['command'].split('.')
                command = Functions
                for depth in tree:
                    command = command[depth]
                result = command.run(instruction['vars'],self.__variables)

                if result:
                    if result['variable']:
                        var = result['variable']
                        self.__variables[var['name']] = var['value']
            else:
                print("[ERROR NO CONTROLADO] No existe la instrucción de la línea " + str(ipointer))
            ipointer = ipointer + 1