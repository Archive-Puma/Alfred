#!/usr/bin/python
# -*- coding: utf-8 -*-

# -- Imports (Python) ----------------------------------------------------------

import os.path as ospath
from sys import path as pypath
from sys import (exit,stderr)

# -- Python Path Modification  -------------------------------------------------

pypath.insert(0, # Fixing global imports in Linux
    ospath.join(ospath.dirname(ospath.abspath(__file__)), '..', 'lib'))

# -- Imports (Alfred) ----------------------------------------------------------

from repl import Repl
from arguments import argv
from morphology import parser
from defines import (EXIT_SUCCESS,EXIT_FAILURE,EXIT_ERRFILE)

# -- Methods -------------------------------------------------------------------

def main():
    try:
        if argv.archivo:
            try:
                with open(argv.archivo,'r') as f:
                    try:
                        nodes = parser.parse(f.read())
                        print(nodes)
                        # nodes.eval()
                    except Exception as err:
                        print(str(err), file=stderr)
                        exit(EXIT_FAILURE)
            except FileNotFoundError:
                print("[🐛] La ruta especificada no es un archivo válido.",
                    file=stderr)
                exit(EXIT_ERRFILE)
        elif argv.interactive:
            repl = Repl(parser)
            repl.interactive()
        else:
            argv.__parser__(["-h"])
    except (KeyboardInterrupt, EOFError):
        print()

# -- Entrypoint ----------------------------------------------------------------

if __name__ == '__main__':
    main()
    exit(EXIT_SUCCESS)
