import sys
from core import parser


def main():
    if len(sys.argv) == 1:
        while True:
            repl = input(">>> ")
            parser.parse('Alfred,' + repl).eval()
    else:
        with open(sys.argv[1],'r') as f:
            res = parser.parse(f.read())
            for node in res:
                node.eval()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
