# -*- coding: utf-8 -*-

import socket

def create(host,port,variables):
        if 'port' in variables.keys():
            port = variables['port']

        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
        server.bind((host,port))
        server.listen(10)

        print("Servidor Discard en tcp://{0}:{1}/".format(host,port))

        while True:
            client, address = server.accept()
            while True:
                data = client.recv(1024)
                if data:
                    print("Discard :: {0} :: {1}".format(address,data))
                else:
                    client.close()
                    break

class Server:
    def __init__(self):
        self.__hostname = 'localhost'
        self.__port     = 9000

        self.__result   = dict()

    def run (self,variables,env=None):
        self.__result['thread'] = {
            'function': create,
            'kwargs':
            (
                self.__hostname,
                self.__port,
                variables
            )
        }
        return self.__result
