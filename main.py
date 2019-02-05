from lexer import lexer
from parser import parser

import sys

def main():
    if len(sys.argv) == 1:
        while True:
            repl = input(">>> ")
            parser.parse(repl)
    else:
        with open(sys.argv[1],'r') as f:
            parser.parse(f.read())

if __name__ == '__main__':
    main()
