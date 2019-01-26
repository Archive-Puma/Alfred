from _thread import start_new_thread

from ..Language.Binds import Functions

class Evaluator:
    def __init__(self):
        self.__jumps        = dict()
        self.__handlers     = list()
        self.__variables    = dict()

        self.__environment = {
            'jumps':        dict(),
            'handlers':     self.__handlers,
            'variables':    self.__variables
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
                    if 'handler' in keys:
                        handler = result['handler']
                        self.__environment['handlers'].append({
                            'type':     handler['type'],
                            'handler':  handler['handler']
                        })
                    if 'thread' in keys:
                        thread = result['thread']
                        start_new_thread(thread['function'],thread['kwargs'])

            else:
                print("[ERROR NO CONTROLADO] No existe la instrucción de la línea " + str(ipointer))
            ipointer = ipointer + 1

    def interrupt(self):
        command = Functions['Base']['Exit']
        command.run(None,self.__environment)