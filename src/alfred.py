import os.path as ospath
from sys import path as pypath
from sys import (argv,exit,stderr)
pypath.insert(0, ospath.join(ospath.dirname(ospath.abspath(__file__)), '..', 'lib'))

from repl import Repl
from parser import parser
from defines import (EXIT_SUCCESS,EXIT_FAILURE,EXIT_ERRFILE)

def main():
    try:
        if len(argv) == 2:
            try:
                with open(argv[1],'r') as f:
                    try:
                        nodes = parser.parse(f.read())
                        print(nodes)
                        for node in nodes:
                            node.eval()
                    except TypeError as err:
                        print(str(err), file=stderr)
                        exit(EXIT_FAILURE)
            except FileNotFoundError:
                print("[🐛] La ruta especificada no es un archivo válido.", file=stderr)
                exit(EXIT_ERRFILE)
        else:
            repl = Repl(parser)
            repl.interactive()
    except KeyboardInterrupt:
        print()

if __name__ == '__main__':
    main()
    exit(EXIT_SUCCESS)
