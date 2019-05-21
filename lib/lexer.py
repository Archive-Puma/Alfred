# -- Imports -------------------------------------------------------------------

from sys import exit
from ply.lex import lex
from defines import EXIT_ERRDATA,IGNORECASE

# -- Tokens --------------------------------------------------------------------

literals = [ '+', '-', '*', '/', '=', '>', '<' ]
reserved = {
    "alfred":   "ALFRED",
    # Methods
    "di":       "PRINTLN",
    "escribe":  "PRINT",
    "pregunta": "INPUT",
    "guardalo": "STORE",
    "en":       "IN",
    # Conditionals
    "si":       "IF",
    "sino":     "ELSE",
    "listo":    "END",
    "mientras": "WHILE",
    # Binary Operations
    "mas":      "ADD",
    "menos":    "SUB",
    "por":      "BY",
    "entre":    "BTWN",

    "es":       "IS",
    "igual":    "EQUAL",
    "menor":    "LOWER",
    "mayor":    "GREATER",

    # Auxiliary
    "a":        "TO",
    "que":      "THAN"
}
tokens = [
    "ID",
    "STRING",
    "INTEGER",
] + list(reserved.values())

# -- Lexer Definition ----------------------------------------------------------

def Lexer():

# -- Ignored Tokens ------------------------------------------------------------

    t_ignore = ".,y"

    t_ignore_COMMENT = r'\(([^\)])*\)'
    t_ignore_WHITESPACE = r'\s+'

# -- Special Tokens ------------------------------------------------------------

    def t_ID(t):
        r'[a-zA-Z][a-zA-Z0-9_]*'
        t.value = t.value.lower()
        t.type = reserved.get(t.value,"ID")
        return t

    def t_STRING(t):
        r'"([^"\\]|\\.)*"'
        t.value = t.value[1:-1]
        t.value = t.value.replace("\\\"", "\"")
        t.type = reserved.get(t.value,"STRING")
        return t

    def t_INTEGER(t):
        r'[+-]?[0-9]+'
        t.value = int(t.value)
        t.type = reserved.get(t.value,"INTEGER")
        return t

# -- Error Handler -------------------------------------------------------------

    def t_error(t):
        raise TypeError("[🐛] Caracter inválido ({},~{}): {}".format(
            lexer.lineno, lexer.lexpos, t.value[0]))

# -- Lexer Declaration ---------------------------------------------------------

    return lex(
        optimize=0,
        debug=False,
        reflags=IGNORECASE,
        lextab="alfredtab.py"
    )

lexer = Lexer()
