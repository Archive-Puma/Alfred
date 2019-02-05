class Symbols():
    def __init__(self):
        self.variables = dict()
        self.functions = dict()
    
    def setvar(self,name,value):
        self.variables[name] = value
    
    def getvar(self,name):
        return self.variables[name]

symbols = Symbols()


# --------------------------------------------------------------------------------
#  INHERITANCE  INHERITANCE  INHERITANCE  INHERITANCE  INHERITANCE  INHERITANCE
# --------------------------------------------------------------------------------

class Base():
    def eval(self):
        raise NotImplementedError()

# --------------------------------------------------------------------------------
#    STATEMENTS  STATEMENTS  STATEMENTS  STATEMENTS  STATEMENTS  STATEMENTS
# --------------------------------------------------------------------------------

class InstructionList():
    def __init__(self, child=list()):
        self.child = child

    def __repr__(self):
        return "<InstructionList {0}>".format(self.child)

    def __iter__(self):
        return iter(self.child)

    def eval(self):
        ret = list()

        for instruction in self:
            res = instruction.eval()
            
            if res is not None:
                ret.append(res)
        return ret

class Pass(Base):
    def __repr__(self):
        return "<Pass>"

    def eval(self):
        pass

# --------------------------------------------------------------------------------
#     CONDITIONALS  CONDITIONALS  CONDITIONALS  CONDITIONALS  CONDITIONALS
# --------------------------------------------------------------------------------

class If(Base):
    def __init__(
        self,
        condition: Base,
        truestmt: InstructionList,
        falsestmt: InstructionList = None):
        self.condition = condition
        self.truestmt = truestmt
        self.falsestmt = falsestmt

    def __repr__(self):
        return "<If condition={0} true={1} false={2}>".format(
            self.condition, self.truestmt, self.falsestmt
        )

    def eval(self):
        if self.condition.eval():
            self.truestmt.eval()
        elif self.falsestmt is not None:
            self.falsestmt.eval()

# --------------------------------------------------------------------------------
#   LOOPS  LOOPS  LOOPS  LOOPS  LOOPS  LOOPS  LOOPS  LOOPS  LOOPS  LOOPS  LOOPS
# --------------------------------------------------------------------------------

class While(Base):
    def __init__(
        self,
        condition: Base,
        body: InstructionList):
        self.condition = condition
        self.body = body

    def __repr__(self):
        return "<While condition={0} body={1}".format(
            self.condition, self.body
        )

    def eval(self):
        while self.condition.eval():
            self.body.eval()


# --------------------------------------------------------------------------------
#   FUNCTIONS  FUNCTIONS  FUNCTIONS  FUNCTIONS  FUNCTIONS  FUNCTIONS  FUNCTIONS
# --------------------------------------------------------------------------------

class Print(Base):
    def __init__(self,items: InstructionList):
        self.items = items
    
    def __repr__(self):
        return "<Print {0}>".format(self.items)

    def eval(self):
        print(*self.items.eval())


# --------------------------------------------------------------------------------
#  DEFINITIONS  DEFINITIONS  DEFINITIONS  DEFINITIONS  DEFINITIONS  DEFINITIONS
# --------------------------------------------------------------------------------

class Name(Base):
    def __init__(self,name):
        self.name = name
        self.isfunc = False

    def __repr__(self):
        return "<Name {0}>".format(self.name)

    def eval(self):
        if self.isfunc:
            pass            # TODO
        else:
            return symbols.getvar(self.name)
        
    def assign(self,value):
        if self.isfunc:
            pass            # TODO
        else:
            symbols.setvar(self.name,value)

class Define(Base):
    def __init__(self,name: Name,value):
        self.name = name
        self.value = value

    def __repr__(self):
        return "<Define name={0}, value={1}>".format(
            self.name, self.value
        )

    def eval(self):
        if self.name.isfunc:
            pass            # TODO
        else:
            self.name.assign(self.value.eval())

class Primitive(Base):
    def __init__(self,value):
        self.value = value

    def __repr__(self):
        return "<Primitive {0} ({1})>".format(self.value, self.value.__class__)

    def eval(self):
        return self.value