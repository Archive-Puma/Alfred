# -- Imports -------------------------------------------------------------------

from ply.yacc import yacc

from lexer import tokens
from nodes import (InstructionList, Identifier, Primitive, Assignment,
                   Stdin, Stdout, BinaryOp, Empty)


# -- Parser Definition ---------------------------------------------------------

def Parser():
    start = "program"
    precedence = (
        ('left', '+', '-', 'ADD', 'SUB'),
        ('left', '*', '/', 'BY', 'BTWN'),
    )

    # -- Structure -----------------------------------------------------------------

    def p_program(p):
        """ program : ALFRED statements """
        p[0] = p[2]

    def p_statements(p):
        """ statements : statements statement
                       | statement
                       | empty
        """
        if len(p) == 2:
            if not p[1]:
                p[1] = Empty()
            p[0] = InstructionList([p[1]])
        elif len(p) == 3:
            p[1].child.append(p[2])
            p[0] = p[1]

    def p_statement(p):
        """ statement : method """
        p[0] = p[1]

    # -- Variables -----------------------------------------------------------------

    def p_identifier(p):
        """ expression : id """
        p[0] = p[1]

    def p_id(p):
        """ id : ID """
        p[0] = Identifier(p[1])

    def p_primitive(p):
        """ expression : STRING
                       | INTEGER
        """
        p[0] = Primitive(p[1])

    def p_assignment(p):
        """ assignment : id '=' expression
           assignment : id IS expression
           assignment : id IS EQUAL TO expression
        """
        p[0] = Assignment(p[1], p[len(p) - 1])

    # -- Binary Operations ---------------------------------------------------------

    def p_binaryop(p):
        """ expression : expression '+' expression
                      | expression '-' expression
                      | expression '*' expression
                      | expression '/' expression

                      | expression ADD expression
                      | expression SUB expression
                      | expression BY expression
                      | expression BTWN expression
        """
        operation = p[2].lower()
        p[0] = BinaryOp(operation, p[1], p[3])

    # -- Methods -------------------------------------------------------------------


    def p_method(p):
        """ method : store
                   | stdin
                   | stdout
                   | assignment
        """
        p[0] = p[1]


    def p_store(p):
        """ store : STORE IN id """
        p[0] = Assignment(p[3])


    def p_stdin(p):
        """ stdin : INPUT arg """
        p[0] = Stdin(p[2])


    def p_stdout(p):
        """ stdout : PRINT expression """
        p[0] = Stdout(p[2], '')


    def p_stdout_nl(p):
        """ stdout : PRINTLN expression """
        p[0] = Stdout(p[2])

    # -- Others --------------------------------------------------------------------


    def p_onearg(p):
        """ arg : expression
                | empty
        """
        p[0] = p[1] if p[1] else Primitive("")


    def p_empty(p):
        """ empty : """
        Empty()

    # -- Error Handler -------------------------------------------------------------


    def p_error(p):
        if p:
            raise SyntaxError("[🐛] (Línea: {}) Sintaxis inválida: {}".format(
                p.lineno, p.value))
        else:
            raise SyntaxError("[🐛] Fallo desconocido en la sintaxis.")

    # -- Parser Declaration --------------------------------------------------------


    return yacc(
        debug=False,
        write_tables=True
    )

parser = Parser()
