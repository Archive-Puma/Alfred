from lexer import lexer
from parser import parser

import sys

program = """
Define x = 3 + 3.
Define y como x + 3.
Si x, entonces
    Escribe x.
    Escribe y.
Fin.
Mientras x, haz
    Escribe x.
Fin.
Adiós Alfred.
"""

def main():
    """
    lexer.input(program)
    for token in lexer:
        print(token)
    print(end='\n\n')
    """
    if len(sys.argv) == 1:
        while True:
            repl = input(">>> ")
            parser.parse(repl)
    else:
        with open(sys.argv[1],'r') as f:
            parser.parse(f.read())

if __name__ == '__main__':
    main()
