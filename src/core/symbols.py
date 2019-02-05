class Symbols():
    def __init__(self):
        self.variables = dict()
        self.functions = dict() # TODO: Functions
    
    def setvar(self,name,value):
        self.variables[name] = value
    
    def getvar(self,name):
        return self.variables.get(name,None)

symbols = Symbols()