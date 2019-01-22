class Jump:
    def __init__(self):
        pass

    def run(self,variables,env):
        name = variables['name']
        return { 'jump': env['jumps'][name] }