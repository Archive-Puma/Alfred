# --------------------------------------------------------------------------------
#    STATEMENTS  STATEMENTS  STATEMENTS  STATEMENTS  STATEMENTS  STATEMENTS
# --------------------------------------------------------------------------------


class InstructionList():
    def __init__(self, child=list()):
        self.child = child

    def __repr__(self):
        return "<InstructionList {0}>".format(self.child)

# --------------------------------------------------------------------------------
#  INHERITANCE  INHERITANCE  INHERITANCE  INHERITANCE  INHERITANCE  INHERITANCE
# --------------------------------------------------------------------------------

class Base():
    def eval(self):
        raise NotImplementedError()

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


# --------------------------------------------------------------------------------
#   FUNCTIONS  FUNCTIONS  FUNCTIONS  FUNCTIONS  FUNCTIONS  FUNCTIONS  FUNCTIONS
# --------------------------------------------------------------------------------

class Print(Base):
    def __init__(self,items: InstructionList):
        self.items = items
    
    def __repr__(self):
        return "<Print {0}>".format(self.items)

# --------------------------------------------------------------------------------
#  DEFINITIONS  DEFINITIONS  DEFINITIONS  DEFINITIONS  DEFINITIONS  DEFINITIONS
# --------------------------------------------------------------------------------

class Name(Base):
    def __init__(self,name):
        self.name = name
        self.isfunc = False

    def __repr__(self):
        return "<Name {0}>".format(self.name)


class Variable(Base):
    def __init__(self,name: Name,value):
        self.name = name
        self.value = value

    def __repr__(self):
        return "<Variable name={0}, value={1}>".format(
            self.name, self.value
        )






class Primitive(Base):
    def __init__(self,value):
        self.value = value

    def __repr__(self):
        return "<Primitive {0} ({1})>".format(self.value, self.value.__class__)