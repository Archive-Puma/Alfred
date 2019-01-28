# -*- coding: utf-8 -*-

class Define:
    def __init__(self):
        pass
    def run(self,variables,env=None):
        result = {}

        value = variables['value']

        if type(value) is str:
            if value[0] is '"' and value[-1] is '"':
                value = value[1:-1]

        result['variable'] = {
            'name': variables['name'],
            'value': value
        }
        return result
