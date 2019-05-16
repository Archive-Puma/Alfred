from lexer import tokens
from ply.yacc import yacc

def Parser():
    def p_program(p):
        ''' program : entrypoint statements '''
        p[0] = p[2]

    def p_entrypoint(p):
        ''' entrypoint : ALFRED '''
        pass

    def p_statements(p):
        ''' statements : statements statement
                       | statement
                       | empty
        '''
        if len(p) == 2:
            p[0] = p[1]
        elif len(p) == 3:
            p[0] = p[1] + " " + p[2]

    def p_statement(p):
        ''' statement : identifier '''
        p[0] = p[1]

    def p_identifier(p):
        ''' identifier : ID '''
        p[0] = p[1]

    def p_empty(p):
        ''' empty : '''
        pass

    return yacc(
        debug=False,
        write_tables=True
    )

parser = Parser()
