"""
Author: @CosasDePuma <kikefontanlorenzo@gmail.com>(https://github.com/cosasdepuma)
"""

class Parser:
    """ Parser component to create the instructions """
    def __init__(self):
        self.jumps = {}
        self.ipointer = 0
        self.instructions = []

    def build(self, tokens):
        """ Build instructions from tokens """
        node = []
        for token in tokens:
            # Add labels and the line of code to the jump map
            if token['id'] == 'label':
                self.jumps[token['value']] = self.ipointer
            # Add instructions to the list
            else:
                if token['id'] == 'keyword':
                    self.ipointer += 1
                    node = [token['value']]
                # Add instruction args to instruction array
                else:
                    node.append(token['value'])
        # Add last nodes to the list
        if node != []:
            self.instructions.append(node)

    def string(self):
        """ Show the Parser Tree """
        print("\n\t -- JUMP TABLE --")
        print("===================================")
        print(" Pointer\tAlias")
        print("-----------------------------------")
        for label in self.jumps:
            print("   {0}\t\t{1}".format(self.jumps[label], label))
        print("\n      -- INSTRUCTION TABLE --")
        print("===================================")
        print(" Command\tArgs")
        print("-----------------------------------")
        for instruction in self.instructions:
            print(" {0}\t\t".format(instruction[0]), end='')
            for args in instruction[1:]:
                print("{0} ".format(args), end='')
            print()
        print()
