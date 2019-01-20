from ..Language.Binds import Functions

class Evaluator:
    def __init__(self):
        pass

    def evaluate(self,ast):
        ipointer = 0
        while ipointer < len(ast):
            instruction = ast[ipointer]
            if instruction:
                tree = instruction['command'].split('.')
                command = Functions
                for depth in tree:
                    command = command[depth]
                command.run(instruction['vars'])
            else:
                print("[ERROR NO CONTROLADO] No existe la instrucción de la línea " + line)
            ipointer = ipointer + 1