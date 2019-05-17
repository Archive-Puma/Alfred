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

class Stdin(Node):
    def __init__(self,text):
        self.text = text
    def __repr__(self):
        return "<Input {}>".format(self.text)
    def eval(self):
        value = self.text.eval()
        if not isinstance(value, str):
            raise TypeError("[x] Sólo se puede preguntar texto.")
        input(value)

class Stdout(Node):
    def __init__(self,item,end='\n'):
        self.end = end
        self.item = item
    def __repr__(self):
        return "<Print {} ({})>".format(self.item, self.end)
    def eval(self):
        print(self.item.eval(),end=self.end)
