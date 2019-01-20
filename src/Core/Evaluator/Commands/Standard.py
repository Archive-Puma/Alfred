class Define:
    def __init__(self):
        pass
    def run(self,variables,env=None):
        result = {}
        result['variable'] = {
            'name': variables['name'],
            'value': variables['value']
        }
        return result
