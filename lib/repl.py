class Repl(object):
    def __init__(self, parser):
        self.prompt = "🎩 »"
        self.ipointer = 0
        self.parse = parser.parse
    def interactive(self):
        while True:
            repl = input("{} :: {} ".format(
                str(self.ipointer).zfill(4), self.prompt))
            if repl:
                result = self.parse("Alfred, {}".format(repl))
                for node in result:
                    node.eval()
                self.ipointer += 1
