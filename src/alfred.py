import os.path as ospath
from sys import path as pypath

from os import (EX_OK,EX_OSFILE)
from sys import (argv,exit,stderr)

pypath.insert(0, ospath.join(ospath.dirname(ospath.abspath(__file__)), '..', 'lib'))

from repl import Repl
from parser import parser

def main():
    try:
        if len(argv) == 2:
            try:
                with open(argv[1],'r') as f:
                    nodes = parser.parse(f.read())
                for node in nodes:
                    node.eval()
            except FileNotFoundError:
                print("[🐛] La ruta especificada no es un archivo válido.", file=stderr)
                exit(EX_OSFILE)
        else:
            repl = Repl(parser)
            repl.interactive()
    except KeyboardInterrupt:
        print()

if __name__ == '__main__':
    main()
    exit(EX_OK)
