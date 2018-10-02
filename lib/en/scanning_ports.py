"""
Author: @CosasDePuma <kikefontanlorenzo@gmail.com>(https://github.com/cosasdepuma)
"""

import socket
import threading

COMMAND = "PORT SCAN"
LANG = ['Scanning open ports of', 'Open ports']

class Lib:
    """ Check if the most important TCP ports are open """
    def __init__(self):
        # Argument labels
        self.args = ['OF']
        # Variables
        self.timeout = 0.5
        self.open_ports = []
        self.ports = [7, 9, 11, 13, 17, 18, 19, 20, 21, 22, 23,
                      25, 37, 39, 42, 43, 49, 50, 53, 63, 67,
                      68, 69, 79, 80, 88, 95, 101, 102, 107,
                      109, 110, 111, 113, 115, 117, 119, 123,
                      137, 138, 139, 143, 161, 162, 163, 164,
                      174, 177, 178, 179, 191, 194, 201, 202,
                      204, 209, 245, 347, 363, 369, 389, 427,
                      434, 435, 443, 444, 445, 464, 468, 487,
                      488, 496, 500, 535, 538, 546, 989, 990,
                      3306]

    def command(self, operation):
        """ Switch of the command to execute """
        ret = None
        if operation == 'show':
            self.show()
        elif operation == 'get':
            ret = self.get()
        return ret

    def run(self, parameters):
        """ Run the scanner """
        self.open_ports = []
        print("{0} {1}...".format(LANG[0], parameters['OF'].lower()))
        self._multiscanner(parameters['OF'])
        self.open_ports.sort()

    def show(self):
        """ Show the result """
        print("{0}: ".format(LANG[1]), end='')
        for port in self.open_ports:
            print("{0} ".format(port), end='')
        print()

    def get(self):
        """ Return the result """
        return self.open_ports

    def _multiscanner(self, ipaddr):
        """ Creates a mutithreading scanner """
        threads = []
        # Init all the scanners
        for port in self.ports:
            thread = threading.Thread(target=self._tcp_scan, args=(ipaddr, port))
            threads.append(thread)
        # Start all the threads
        for thread in threads:
            thread.start()
        # Lock the script until all threads complete
        for thread in threads:
            thread.join()

    def _tcp_scan(self, ipaddr, port):
        """ Check if a port is open """
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.settimeout(self.timeout)
        status = sock.connect_ex((ipaddr, port))
        if status == 0:
            self.open_ports.append(int(port))
        sock.close()
