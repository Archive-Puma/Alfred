class Addition:
    def __init__(self):
        pass

    def run(self,variables,env):
        result = dict()

        name = variables['name']
        value = env['variable'][name]
        value = value + variables['number']

        result['variable'] = {
            'name':     name,
            'value':    value
        }

        return result


class Subtraction:
    def __init__(self):
        pass

    def run(self,variables,env):
        result = dict()

        name = variables['name']
        value = env['variable'][name]
        value = value - variables['number']

        result['variable'] = {
            'name':     name,
            'value':    value
        }

        return result


class Multiplication:
    def __init__(self):
        pass

    def run(self,variables,env):
        result = dict()

        name = variables['name']
        value = env['variable'][name]
        value = value * variables['number']

        result['variable'] = {
            'name':     name,
            'value':    value
        }

        return result


class Division:
    def __init__(self):
        pass

    def run(self,variables,env):
        result = dict()

        name    = variables['name']
        value   = env['variable'][name]
        vartype = type(value)

        if not variables['number'] is 0:
            value = value / variables['number']
            if vartype is int:
                value = int(value)

        result['variable'] = {
            'name':     name,
            'value':    value
        }

        return result