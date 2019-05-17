from ply.lex import lex

IGNORECASE = 0b10

reserved = {
    "alfred":   "ALFRED",
    "di":       "PRINT",
    "muestra":  "PRINTLN",
    "pregunta": "INPUT"
}
tokens = [
    "ID",
    "STRING",
    "INTEGER"
] + list(reserved.values())

def Lexer():
    t_ignore = ".,"

    t_ignore_COMMENT = r'\(([^\)])*\)'
    t_ignore_WHITESPACE = r'\s+'

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

    def t_error(t):
        print("[Error] Caracter inválido ({},~{}): {}".format(
            lexer.lineno, lexer.lexpos, t.value[0]))
        t.lexer.skip(1)


    return lex(
        optimize=0,
        debug=False,
        reflags=IGNORECASE,
        lextab="alfredtab.py"
    )

lexer = Lexer()
