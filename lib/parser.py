from nodes import *
from lexer import tokens
from ply.yacc import yacc
from os import EX_SOFTWARE
from sys import exit,stderr

def Parser():
    start = "program"

    def p_program(p):
        ''' program : ALFRED statements '''
        p[0] = p[2]

    def p_statements(p):
        ''' statements : statements statement
                       | statement
                       | empty
        '''
        if len(p) == 2:
            p[0] = InstructionList([p[1]])
        elif len(p) == 3:
            p[1].child.append(p[2])
            p[0] = p[1]

    def p_statement(p):
        ''' statement : method '''
        p[0] = p[1]

    def p_method(p):
        ''' method : stdin
                   | stdout
        '''
        p[0] = p[1]

    def p_stdin(p):
        ''' stdin : INPUT arg
        '''
        p[0] = Stdin(p[2])

    def p_stdout(p):
        ''' stdout : PRINT expression '''
        p[0] = Stdout(p[2],'')

    def p_stdout_nl(p):
        ''' stdout : PRINTLN expression '''
        p[0] = Stdout(p[2])

    def p_primitive(p):
        ''' expression : STRING
                       | INTEGER
        '''
        p[0] = Primitive(p[1])

    def p_arg1(p):
        ''' arg : expression
                | empty
        '''
        p[0] = p[1] if p[1] else Primitive("")

    def p_empty(p):
        ''' empty : '''
        pass

    def p_error(p):
        if p:
            print("[X] (Línea: {}) Syntaxis inválida: {}".format(
                p.lineno, p.value), file=stderr)
        else:
            print("[X] Fallo desconocido en la sintaxis.", file=stderr)
        exit(EX_SOFTWARE)

    return yacc(
        debug=False,
        write_tables=True
    )

parser = Parser()
