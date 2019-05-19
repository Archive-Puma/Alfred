# -- Symbols Declaration -------------------------------------------------------

class Symbols():
    def __init__(self):
        self.identifiers = dict()
    def set(self, id, value):
        self.identifiers[id] = value
    def get(self, id):
        return self.identifiers.get(id,None)

# -- Symbols Definition --------------------------------------------------------

symbols = Symbols()
