from symbols import symbols,_tmpvar

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
            raise TypeError("[x] Sólo se puede preguntar texto.")
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
