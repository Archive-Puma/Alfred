"""
Author: @CosasDePuma <kikefontanlorenzo@gmail.com>(https://github.com/cosasdepuma)
"""

class Lib:
    """ Calculate the Fibonacci sequence up to a certain number """
    def __init__(self):
        # Argument labels
        self.args = ['HASTA']
        # Variables
        self.sequence = []

    def command(self, operation):
        """ Switch of the command to execute """
        ret = None
        if operation == 'show':
            self.show()
        elif operation == 'get':
            ret = self.get()
        return ret

    def run(self, parameters):
        """ Run the algorithm """
        prev = 0
        actual = 1
        while actual < int(parameters['HASTA']):
            nexts = prev + actual
            self.sequence.append(nexts)
            prev = actual
            actual = nexts

    def show(self):
        """ Show the result """
        string = ''
        for num in self.sequence:
            string += str(num) + ', '
        print(string[:-2])

    def get(self):
        """ Return the result """
        return self.sequence
