from sys import exit

class Exit:
    def __init__(self):
        self.__ExitCode = 0

    def run(self,variables=None,env=None):
        for handler in env['handlers']:
            if handler['type'] == 'httpd':
                handler['handler'].shutdown()

        exit(self.__ExitCode)
        return None
