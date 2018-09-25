class Parser:
    def __init__(self):
        self.jumps = {}
        self.ipointer = 0
        self.instructions = []

    def build(self, tokens):
        args = False
        node = []
        for token in tokens:
            # Add labels and the line of code to the jump map
            if token['id'] == 'label':
                self.jumps[token['value']] = self.ipointer
            # Add instructions to the list
            else:
                if token['id'] == 'keyword':
                    args = True
                    self.ipointer += 1
                    node = [token['value']]
                # Add instruction args to instruction array
                else:
                    node.append(token['value'])
        # Add last nodes to the list
        if node != []:
            self.instructions.append(node)
