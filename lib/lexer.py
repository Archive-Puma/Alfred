from ply.lex import lex

IGNORECASE = 0b10

reserved = {
    "alfred": "ALFRED"
}
tokens = [
    "ID"
] + list(reserved.values())

def Lexer():
    t_ignore = "., \t"

    def t_ID(t):
        r'[a-zA-Z][a-zA-Z0-9_]+'
        value = t.value.lower()
        t.type = reserved.get(value,"ID")
        return t

    def t_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_error(t):
        print("[Error] Caracter inválido ({},{}): {}".format(
            lexer.lexpos, lexer.lineno, t.value[0]))
        t.lexer.skip(1)


    return lex(
        optimize=0,
        debug=False,
        reflags=IGNORECASE,
        lextab="alfredtab.py"
    )

lexer = Lexer()
