from ply import lex

IGNORECASE = 2

literals = [ ',' ]

reserved = {
    # Instructions
    'define': 'DEFINE',
    'escribe': 'PRINT',
    'adios': 'EXIT',
    # Modifiers
    'como': 'AS',
    'mas': 'ADD',
    'menos': 'SUB',
    'por': 'MUL',
    'entre': 'DIV',
    # Blocks
    'si': 'IF',
    'mientras': 'WHILE',
    'no': 'NOT',
    'entonces': 'THEN',
    'haz': 'DO',
    'fin': 'END',
    'y': 'AND'
}

tokens = [
    'INTEGER',
    'STRING',
    'NAME',

    'PLUS',
    'MINUS',
    'BYM',
    'BYD',
    'EQUALS'
] + list(reserved.values())


t_ignore_SPACES     = r'\s+'
t_ignore_COMMENT    = r'\(.*\)'

t_PLUS = r'\+'
t_MINUS = r'-'
t_BYM = r'\*'
t_BYD = r'/'
t_EQUALS = r'='

def t_NAME(t):
    r'[a-zA-Z_]\w*'
    t.type = reserved.get(t.value,'NAME')
    return t


def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]
    return t


def t_error(t):
    print("Invalid token '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex(
    debug=0,
    reflags=IGNORECASE)
