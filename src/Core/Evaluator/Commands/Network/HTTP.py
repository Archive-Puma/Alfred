from http.server    import SimpleHTTPRequestHandler
from socketserver   import TCPServer

def create(host,port,handler,variables,env):
        if 'port' in variables.keys():
            port = variables['port']
        httpd = TCPServer((host,port), handler)
        print("Servidor HTTP en http://{0}:{1}/".format(host,port))
        httpd.serve_forever()
        httpd.shutdown()

class Server:
    def __init__(self):
        self.__hostname = 'localhost'
        self.__port     = 8080
        self.__handler  = SimpleHTTPRequestHandler

        self.__result   = dict()

    def run (self,variables,env):
        self.__result['thread'] = {
            'function': create,
            'kwargs':
            (
                self.__hostname,
                self.__port,
                self.__handler,
                variables,env
            )
        }
        return self.__result