from ply    import yacc
from lexer  import tokens

import sys

class Environment():
    def __init__(self):
        self._variables = dict()
    def add(self,variable):
        name,value = variable
        self._variables[name] = value
    def get(self,name):
        value = self._variables.get(name)
        if value is not None:
            return value
        else:
            raise NameError('La variable "%s" no ha sido inicializada' % name)

def p_program(p):
    '''
    program             : program statement DOT
                        | statement DOT
    '''
    p[0] = p[1]

def p_statement_while(p):
    '''
    statement           : loop_while loop_do END
    '''
    pass # TODO

def p_loop_while(p):
    '''
    loop_while          : WHILE expression COMMA
    '''
    p[0] = True if p[2] else False

def p_loop_do(p):
    '''
    loop_do             : DO program
    '''
    p[0] = p[2]

def p_statement_conditional(p):
    '''
    statement           : conditional_if conditional_then END
    '''
    if p[1]:
        p[0] = p[2]

def p_conditional_then(p):
    '''
    conditional_then    : COMMA program
    '''
    p[0] = p[2]

def p_conditional_if(p):
    '''
    conditional_if      : IF expression
    '''
    p[0] = True if p[2] else False

def p_statement_exit(p):
    '''
    statement           : EXIT ALFRED
                        | EXIT_ ALFRED
    '''
    sys.exit(0)

def p_statement_print(p):
    '''
    statement           : PRINT expression
    '''
    print(p[2])

def p_statement_define(p):
    '''
    statement           : DEFINE NAME EQUALS expression
                        | DEFINE NAME AS expression
    '''
    env.add((p[2],p[4]))

def p_expression_binaryop_add(p):
    '''
    expression          : expression PLUS expression
                        | expression ADD expression
    '''
    tl,tr = type(p[1]),type(p[3])
    if tl is not tr:
        if tl is str or tr is str:
            p[0] = str(p[1]) + str(p[3])
        else:
            p[0] = p[1] + p[3]
    else:
        p[0] = p[1] + p[3]

def p_expression_binaryop_sub(p):
    '''
    expression          : expression MINUS expression
                        | expression SUB expression
    '''
    p[0] = p[1] - p[3]

def p_expression_binaryop_mult(p):
    '''
    expression          : expression TIMES expression
                        | expression BY expression
    '''
    p[0] = p[1] * p[3]

def p_expression_binaryop_mult(p):
    '''
    expression          : expression DIV expression
    '''
    val = p[1] / p[3]
    if p[3] == 0:
        raise ZeroDivisionError()
    elif p[1] % p[3] == 0:
        p[0] = int(val)
    else:
        p[0] = val


def p_expression_value(p):
    '''
    expression          : STRING
                        | INTEGER
    '''
    p[0] = p[1]

def p_expression_name(p):
    '''
    expression          : NAME
    '''
    p[0] = env.get(p[1])


def p_error(p):
    # https://stackoverflow.com/questions/26979715/debugging-ply-in-p-error-to-access-parser-state-stack
    # get formatted representation of stack
    stack_state_str = ' '.join([symbol.type for symbol in parser.symstack][1:])

    if parser.state == 0:
        print("Comando no definido: '%s'" % p.value)
    else:
        print('Syntax error in input! Parser State:{} {} . {}'
              .format(parser.state,
                      stack_state_str,
                      p))

precedence = (
    ('left', 'ADD', 'SUB', 'BY'),
    ('left', 'PLUS', 'MINUS', 'TIMES'),
)
parser = yacc.yacc()
env = Environment()
