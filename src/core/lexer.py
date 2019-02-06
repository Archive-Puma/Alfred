from ply import lex

IGNORECASE = 0b10

# --------------------------------------------------------------------------------
#     LITERALS  LITERALS  LITERALS  LITERALS  LITERALS  LITERALS  LITERALS
# --------------------------------------------------------------------------------

literals = [ '.', ',', ':' ]

# --------------------------------------------------------------------------------
#      RESERVED  RESERVED  RESERVED  RESERVED  RESERVED  RESERVED  RESERVED
# --------------------------------------------------------------------------------

reserved = {
    # Invoke
    'alfred':       'ALFRED',
    # Instructions
    'define':       'DEFINE',
    'escribe':      'PRINT',
    'adios':        'EXIT',
    # Binary Operations (Maths)
    'mas':          'ADD',
    'menos':        'SUB',
    'por':          'MUL',
    'entre':        'DIV',
    'elevado':      'EXP',
    'modulo':       'MOD',
    'decrementa':   'DEC',
    'incrementa':   'INC',
    # Binary Operations (Bool)
    'igual':        'SAME',
    'mayor':        'GREATER',
    'menor':        'LESS',
    # Blocks
    'si':           'IF',
    'haz':          'DO',
    'mientras':     'WHILE',
    'listo':        'END',
    # Auxiliary Words
    'a':            'TO',
    'e':            'AND_',
    'y':            'AND',
    'es':           'IS',
    'sea':          'BE',
    'no':           'NOT',
    'la':           'THE',
    'que':          'THAN',
    'como':         'AS',
    'funcion':      'FUNCTION',
}

# --------------------------------------------------------------------------------
#    TOKENS  TOKENS  TOKENS  TOKENS  TOKENS  TOKENS  TOKENS  TOKENS  TOKENS
# --------------------------------------------------------------------------------

tokens = [
    # ID
    'NAME',
    # Values
    'INTEGER',
    'STRING',
    # Binary Operations (Maths)
    'PLUS',         # +
    'MINUS',        # -
    'BYM',          # *
    'BYD',          # /
    'POW',          # ^ **
    'MODU',         # %
    'PLUSPLUS',     # ++
    'MINUSMINUS',   # --
    # Binary Operations (Bool)
    'EQUALS',       # ==
    'GT',           # >
    'LT',           # <
    # Assignation
    'EQ',           # =
] + list(reserved.values())

# --------------------------------------------------------------------------------
#     REGEXP  REGEXP  REGEXP  REGEXP  REGEXP  REGEXP  REGEXP  REGEXP  REGEXP
# --------------------------------------------------------------------------------

# Ignore
t_ignore_SPACES     = r'\s+'
t_ignore_COMMENT    = r'\(.*\)'

# Assignation
t_EQ                = r'='

# Binary Operations (Maths)
t_PLUS              = r'\+'
t_MINUS             = r'-'
t_BYM               = r'\*'
t_BYD               = r'/'
t_POW               = r'\^|\*\*'
t_MODU              = r'%'
t_PLUSPLUS          = r'\+\+'
t_MINUSMINUS        = r'--'

# Binary Operations (Bool)
t_EQUALS            = r'=='
t_GT                = r'>'
t_LT                = r'<'

# ID
def t_NAME(t):
    r'[a-zA-Z_]\w*'
    t.type = reserved.get(t.value.lower(),'NAME')
    return t

# Values
def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]
    return t

# --------------------------------------------------------------------------------
#     ERRORS  ERRORS  ERRORS  ERRORS  ERRORS  ERRORS  ERRORS  ERRORS  ERRORS
# --------------------------------------------------------------------------------
def t_error(t):
    print("Invalid token '%s'" % t.value[0])
    t.lexer.skip(1)

# --------------------------------------------------------------------------------
#   LEXER  LEXER  LEXER  LEXER  LEXER  LEXER  LEXER  LEXER  LEXER  LEXER  LEXER
# --------------------------------------------------------------------------------

lexer = lex.lex(
    debug=False,
    reflags=IGNORECASE)
