from ply.yacc import yacc
from os import EX_SOFTWARE
from sys import exit,stderr

from nodes import *
from lexer import tokens



def Parser():
    start = "program"

    precedence = (
        ('left', '+','-','ADD','SUB'),
        ('left', '*','/','BY','BTWN'),
    )


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
        ''' method : store
                   | stdin
                   | stdout
        '''
        p[0] = p[1]

    def p_store(p):
        ''' store : STORE IN id '''
        p[0] = Assignment(p[3])

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

    def p_identifier(p):
        ''' expression : id '''
        p[0] = p[1]

    def p_id(p):
        ''' id : ID '''
        p[0] = Identifier(p[1])

    def p_primitive(p):
        ''' expression : STRING
                       | INTEGER
        '''
        p[0] = Primitive(p[1])

    def p_binaryop(p):
        ''' expression : expression '+' expression
                       | expression '-' expression
                       | expression '*' expression
                       | expression '/' expression

                       | expression ADD expression
                       | expression SUB expression
                       | expression BY expression
                       | expression BTWN expression
        '''
        operation = p[2].lower()
        p[0] = BinaryOp(operation,p[1],p[3])

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
            print("[🐛] (Línea: {}) Syntaxis inválida: {}".format(
                p.lineno, p.value), file=stderr)
        else:
            print("[🐛] Fallo desconocido en la sintaxis.", file=stderr)
        exit(EX_SOFTWARE)

    return yacc(
        debug=False,
        write_tables=True
    )

parser = Parser()
