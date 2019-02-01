from ply import lex

reserved = {
    # Instructions
    'Define': 'DEFINE',
    'Escribe': 'PRINT',
    'Adios': 'EXIT',
    'Adiós': 'EXIT_',
    # Modifiers
    'como': 'AS',
    'mas': 'ADD',
    'menos': 'SUB',
    'por': 'BY',
    # Blocks
    'Si': 'IF',
    'Mientras': 'WHILE',
    'entonces': 'THEN',
    'haz': 'DO',
    'Fin': 'END',

    'Alfred': 'ALFRED'
}

tokens = [
    'EQUALS',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIV',
    'DOT',
    'COMMA',

    'INTEGER',
    'STRING',
    'NAME'
] + list(reserved.values())

t_EQUALS    = r'='
t_PLUS      = r'\+'
t_MINUS     = r'\-'
t_TIMES     = r'\*'
t_DOT       = r'\.'
t_COMMA     = r','
t_DIV       = r'/'

t_ignore_SPACES     = r'\s+'
t_ignore_COMMENT    = r'\(.*\)'

def t_NAME(t):
    r'[a-zA-Z_]\w*'
    t.type = reserved.get(t.value,'NAME')
    return t


def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'".*"'
    t.value = t.value[1:-1]
    return t


def t_error(t):
    print("Invalid token '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex(
    debug=0)
