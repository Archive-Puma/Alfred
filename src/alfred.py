import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'lib'))

from parser import parser


def main():
    try:
        if len(sys.argv) == 2:
            with open(sys.argv[1],'r') as f:
                nodes = parser.parse(f.read())
            for node in nodes:
                node.eval()
    except KeyboardInterrupt:
        print()

if __name__ == '__main__':
    main()
