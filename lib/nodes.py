from symbols import symbols,_tmpvar
from operator import (
    add,sub,mul,truediv
)


class Node():
    def eval(self):
        raise NotImplementedError()

class InstructionList(Node):
    def __init__(self, child=list()):
        self.child = child
    def __repr__(self):
        return "<InstructionList {}>".format(self.child)
    def __iter__(self):
        return iter(self.child)
    def eval():
        ret = list()
        for instruction in self.child:
            result = instruction.eval()
            if res is not None:
                ret.append(result)
        return ret


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
        return "<BinaryOp {} ({},{})>".format(self.operation, self.lhs, self.rhs)
    def eval(self):
        result = None
        lhs = self.lhs.eval()
        rhs = self.rhs.eval()
        operation = self.__operator[self.operation]

        if operation is add:
            if isinstance(lhs,str) or isinstance(rhs,str):
                result = "{}{}".format(lhs,rhs)
        else:
            result = operation(lhs,rhs)
        return result








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
        return symbols.get(self.name)
    def assign(self, value):
        symbols.set(self.name,value)

class Assignment(Node):
    def __init__(self,name,value=Identifier(_tmpvar)):
        self.name = name
        self.value = value
    def __repr__(self):
        return "<Assignment {} ({})>".format(self.name, self.value)
    def eval(self):
        value = self.value.eval()
        self.name.assign(value.eval())













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
        symbols.set(_tmpvar,Primitive(response))

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
