from sys        import exit
from operator   import (
    add,sub,mul,truediv,pow,mod,
    eq,gt,lt,
    pos,neg,not_,inv,
)
from .symbols   import symbols

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

class Loop(Base):
    def __init__(
        self,
        condition: Base,
        body: InstructionList):
        self.condition = condition
        self.body = body


class While(Loop):
    def __repr__(self):
        return "<While condition={0} body={1}".format(
            self.condition, self.body
        )

    def eval(self):
        while self.condition.eval():
            self.body.eval()


class DoWhile(Loop):
    def __repr__(self):
        return "<DoWhile condition={0} body={1}".format(
            self.condition, self.body
        )
    
    def eval(self):
        self.body.eval()
        while self.condition.eval():
            self.body.eval()


# --------------------------------------------------------------------------------
#   FUNCTIONS  FUNCTIONS  FUNCTIONS  FUNCTIONS  FUNCTIONS  FUNCTIONS  FUNCTIONS
# --------------------------------------------------------------------------------

class Exit(Base):
    def __repr__(self):
        return "<Exit>"
    
    def eval(self):
        exit(0)

class Print(Base):
    def __init__(self,item: InstructionList):
        self.item = item
    
    def __repr__(self):
        return "<Print {0}>".format(self.item)

    def eval(self):
        print(self.item.eval())

# --------------------------------------------------------------------------------
#   BINOP  BINOP  BINOP  BINOP  BINOP  BINOP  BINOP  BINOP  BINOP  BINOP  BINOP
# --------------------------------------------------------------------------------

class UnaryOp(Base):
    __operations = {
        '+': pos,
        '-': neg,
        '~': inv,
        'no': not_,
    }

    def __repr__(self):
        return "<UnaryOp: operation='{0}' expr={1}>".format(
            self.operation, self.expr
        )

    def __init__(self, operation, expr: Base):
        self.operation = operation
        self.expr = expr

    def eval(self):
        return self.__operations[self.operation](self.expr.eval())

class BinaryOp(Base):
    __operators = {
        # Binary Operations (Maths)
        'mas':      add,
        'menos':    sub,
        'por':      mul,
        'entre':    truediv,
        'elevado':  pow,
        'modulo':   mod,

        '+':        add,
        '-':        sub,
        '*':        mul,
        '/':        truediv,
        '**':       pow,
        '^':        pow,
        '%':        mod,
        # Binary Operations (Bool)
        'igual':    eq,
        'mayor':    gt,
        'menor':    lt,
        
        '==':       eq,
        '>':        gt,
        '<':        lt,
    }

    def __init__(self,op,left,right):
        self.op = op
        self.left = left
        self.right = right

    def __repr__(self):
        return "<BinaryOp op='{0}' objects=({1},{2})>".format(
            self.op, self.left, self.right
        )

    def eval(self):
        op      = self.__operators[self.op]
        left    = self.left.eval()
        right   = self.right.eval()

        if op is add:
            if type(left) is str or type(right) is str:
                return(str(self.left.eval()) + str(self.right.eval()))

        return op(self.left.eval(), self.right.eval())

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
            pass            # TODO: Functions
        else:
            return symbols.getvar(self.name)
        
    def assign(self,value):
        if self.isfunc:
            pass            # TODO: Functions
        else:
            symbols.setvar(self.name,value)

class Assignment(Base):
    def __init__(self,name: Name,value):
        self.name = name
        self.value = value


class Define(Assignment):
    def __repr__(self):
        return "<Define name={0}, value={1}>".format(
            self.name, self.value
        )

    def eval(self):
        if self.name.isfunc:
            pass            # TODO: Functions
        else:
            self.name.assign(self.value.eval())


class Modify(Assignment):
    def __repr__(self):
        return "<Modify name={0}, value={1}>".format(
            self.name, self.value
        )

    def eval(self):
        if self.name.isfunc:
            raise AttributeError("NO SE PUEDEN MODIFICAR FUNCIONES") # FIXME: Functions
        else:
            if self.name.eval() is None:
                raise NameError("LA VARIABLE NO HA SIDO INICIALIZADA") # FIXME: Variables
            self.name.assign(self.value.eval())


class Primitive(Base):
    def __init__(self,value):
        self.value = value

    def __repr__(self):
        return "<Primitive {0} ({1})>".format(self.value, self.value.__class__)

    def eval(self):
        return self.value