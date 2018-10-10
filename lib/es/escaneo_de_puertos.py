"""
Author: @CosasDePuma <kikefontanlorenzo@gmail.com>(https://github.com/cosasdepuma)
"""

import socket
import threading

result = []
timeout = 0.5
modes = ['abiertos']

def _port_array(ports):
    ports = ports.upper().replace('Y', ',', 1)
    ports = ports.upper().replace(' ', '')
    ports = ports.split(',')
    int_ports = []
    for port in ports:
        if not port.isdigit():
            int_ports = None
            break
        else:
            int_ports.append(int(port))
    return int_ports

def _tcpscan(ipaddr, port):
    global result
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.settimeout(timeout)
    status = sock.connect_ex((ipaddr, port))
    if status == 0:
        result.append(int(port))
    sock.close()

def scan(args):
    global result
    result = []
    ports = None
    if args['PORT']:
        ports = [int(args['PORT'])]
    else:
        ports = _port_array(args['PORTS'])
        if not ports:
            ports = [7, 9, 11, 13, 17, 18, 19, 20, 21, 22, 23,
                     25, 37, 39, 42, 43, 49, 50, 53, 63, 67,
                     68, 69, 79, 80, 88, 95, 101, 102, 107,
                     109, 110, 111, 113, 115, 117, 119, 123,
                     137, 138, 139, 143, 161, 162, 163, 164,
                     174, 177, 178, 179, 191, 194, 201, 202,
                     204, 209, 245, 347, 363, 369, 389, 427,
                     434, 435, 443, 444, 445, 464, 468, 487,
                     488, 496, 500, 535, 538, 546, 989, 990,
                     3306]
    # --------
    threads = []
    for port in ports:
        thread = threading.Thread(target=_tcpscan, args=(args['IP'], port))
        threads.append(thread)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    if result == []:
        result = None
    else:
        result.sort()
    return result

LIB_CONFIGURATION = {
    'NAME': 'port_scanner',
    'COMMANDS': {
        'ESCANEA': {
            'function': scan,
            'args': {
                'DE': 'IP',
                'EL PUERTO': 'PORT',
                '(LOS PUERTOS)*(DE)': 'PORTS'
            }
        }
    }
}
