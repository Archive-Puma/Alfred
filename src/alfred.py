import sys
from parser import parser

def main():
    if len(sys.argv) == 2:
        with open(sys.argv[1],'r') as f:
            print(parser.parse(f.read()))

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
