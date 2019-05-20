# -- Imports -------------------------------------------------------------------

from symbols import symbols
from defines import TMPVAR
from operator import (
    add,sub,mul,truediv
)

# -- Node Declaration ----------------------------------------------------------

class Node():
    def eval(self):
        raise NotImplementedError()

# -- Structure -----------------------------------------------------------------

class InstructionList(Node):
    def __init__(self, child=list()):
        self.child = child
    def __repr__(self):
        return "<InstructionList {}>".format(self.child)
    def __iter__(self):
        return iter(self.child)
    def __len__(self):
        return len(self.child)
    def eval():
        ret = list()
        for instruction in self.child:
            result = instruction.eval()
            if res is not None:
                ret.append(result)
        return ret

# -- Conditionals --------------------------------------------------------------

class Conditional(Node):
    def __init__(self, condition, truestmt, falsestmt=None):
        self.condition = condition
        self.truestmt = truestmt
        self.falsestmt = falsestmt
    def __repr__(self):
        return "<Condition {} True={} False={}>".format(
            self.condition, self.truestmt, self.falsestmt)
    def eval(self):
        if self.condition.eval():
            self.truestmt.eval()
        else:
            self.falsestmt.eval()

# -- Variables -----------------------------------------------------------------

class Primitive(Node):
    def __init__(self,value):
        self.value = value
    def __repr__(self):
        return "<Primitive {} ({})>".format(self.value, self.value.__class__)
    def eval(self):
        return self.value

class Identifier(Node):
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return "<Identifier {} ({})>".format(self.name, self.eval())
    def eval(self):
        value = symbols.get(self.name)
        if value:
            value = value.eval()
        return value
    def assign(self, value):
        symbols.set(self.name,value)

class Assignment(Node):
    def __init__(self,name,value=Identifier(TMPVAR)):
        self.name = name
        self.value = value
    def __repr__(self):
        return "<Assignment {} ({})>".format(self.name, self.value)
    def eval(self):
        self.name.assign(self.value)

# -- Binary Operations ---------------------------------------------------------

class BinaryOp(Node):
    __operator = {
        'mas': add,
        'menos': sub,
        'por': mul,
        'entre': truediv,

        '+': add,
        '-': sub,
        '*': mul,
        '/': truediv
    }
    def __init__(self,operation,lhs,rhs):
        self.operation = operation
        self.lhs = lhs
        self.rhs = rhs
    def __repr__(self):
        return "<BinaryOp {} ({},{})>".format(
            self.operation, self.lhs, self.rhs)
    def eval(self):
        result = None
        lhs = self.lhs.eval() if isinstance(self.lhs, Node) else self.lhs
        rhs = self.rhs.eval() if isinstance(self.rhs, Node) else self.rhs
        operation = self.__operator[self.operation]

        if operation is add and (isinstance(lhs,str) or isinstance(rhs,str)):
                result = "{}{}".format(lhs,rhs)
        elif operation is truediv and rhs == 0:
                raise ZeroDivisionError("[🐛] No se puede dividir entre cero.")
        else:
            result = operation(lhs,rhs)
        return result

# -- Methods -------------------------------------------------------------------

class Stdin(Node):
    def __init__(self,text):
        self.text = text
    def __repr__(self):
        return "<Input {}>".format(self.text)
    def eval(self):
        value = self.text.eval()
        if not isinstance(value, str):
            raise TypeError("[🐛] Sólo se puede preguntar texto.")
        response = input(value)
        symbols.set(TMPVAR,Primitive(response))

class Stdout(Node):
    def __init__(self,text,end='\n'):
        self.end = end
        self.text = text
    def __repr__(self):
        if self.end == '':
            return "<Print {}>".format(self.text)
        else:
            return "<Println {}>".format(self.text)
    def eval(self):
        print(self.text.eval(),end=self.end)

# -- Others --------------------------------------------------------------------

class Empty(Node):
    def __repr__(self):
        return "<Empty>"
    def eval(self):
        pass
