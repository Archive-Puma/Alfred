# pylint: disable=unused-wildcard-import

import sys
from ply.yacc   import (yacc,NullLogger)

from .ast       import *
from .lexer     import tokens

# --------------------------------------------------------------------------------
#    STATEMENTS  STATEMENTS  STATEMENTS  STATEMENTS  STATEMENTS  STATEMENTS
# --------------------------------------------------------------------------------

def p_program(p):
    ''' program : statements '''
    for l in p[1]:
        print(l)
    p[0] = p[1]

def p_statements(p):
    '''
    statements  : statement
                | statements statement
                | empty
    '''
    if len(p) == 1:
        p[0] = InstructionList()
    elif len(p) == 2:
        p[0] = InstructionList([p[1]])
    elif len(p) == 3:
        p[1].child.append(p[2])
        p[0] = p[1]


def p_statement(p):
    '''
    statement   : expression
                | if_statement
    '''
    p[0] = p[1]

# --------------------------------------------------------------------------------
#     CONDITIONALS  CONDITIONALS  CONDITIONALS  CONDITIONALS  CONDITIONALS
# --------------------------------------------------------------------------------

def p_statement_if_else_if(p):
    ''' if_statement : IF expression ',' statements IF NOT ',' if_statement '''
    p[0] = If(p[2],p[4],p[8])

def p_statement_if_else(p):
    ''' if_statement : IF expression ',' statements IF NOT ',' statements END '''
    p[0] = If(p[2],p[4],p[8])

def p_statement_if(p):
    ''' if_statement : IF expression ',' statements END '''
    p[0] = If(p[2],p[4])

# --------------------------------------------------------------------------------
#   LOOPS  LOOPS  LOOPS  LOOPS  LOOPS  LOOPS  LOOPS  LOOPS  LOOPS  LOOPS  LOOPS
# --------------------------------------------------------------------------------

def p_statement_while(p):
    ''' statement : WHILE expression ',' statement '''
    p[0] = While(p[2],InstructionList([p[4]]))

# --------------------------------------------------------------------------------
#   FUNCTIONS  FUNCTIONS  FUNCTIONS  FUNCTIONS  FUNCTIONS  FUNCTIONS  FUNCTIONS
# --------------------------------------------------------------------------------

def p_arguments(p):
    '''
    arguments   : arguments ',' expression
                | expression
                | empty
    '''
    if len(p) == 2:
        p[0] = InstructionList([p[1]])
    elif len(p) == 4:
        p[1].child.append(p[3])
        p[0] = p[1]

def p_function_print(p):
    ''' statement : PRINT arguments '''
    p[0] = Print(p[2])

# --------------------------------------------------------------------------------
#  DEFINITIONS  DEFINITIONS  DEFINITIONS  DEFINITIONS  DEFINITIONS  DEFINITIONS
# --------------------------------------------------------------------------------

def p_expression_let(p):
    ''' expression : DEFINE NAME EQ expression '''
    p[0] = Define(Name(p[2]),p[4])

def p_expression_id(p):
    ''' expression : NAME '''
    p[0] = Name(p[1])

def p_expression_value(p):
    '''
    expression  : INTEGER
                | STRING
    '''
    p[0] = Primitive(p[1])

# --------------------------------------------------------------------------------
#   BINOP  BINOP  BINOP  BINOP  BINOP  BINOP  BINOP  BINOP  BINOP  BINOP  BINOP
# --------------------------------------------------------------------------------

def p_binaryop(p):
    '''
    expression  : expression ADD expression
                | expression SUB expression
                | expression MUL expression
                | expression DIV expression
                | expression MOD expression
                | expression EXP TO expression

                | expression SAME TO expression
                | expression GREATER THAN expression
                | expression LESS THAN expression

                | expression PLUS expression
                | expression MINUS expression
                | expression BYM expression
                | expression BYD expression
                | expression POW expression
                | expression MODU expression

                | expression EQUALS expression
                | expression GT expression
                | expression LT expression
    '''
    if len(p) == 4:
        p[0] = BinaryOp(p[2], p[1], p[3])
    elif len(p) == 5:
        p[0] = BinaryOp(p[2], p[1], p[4])

# --------------------------------------------------------------------------------
#   EMPTY  EMPTY  EMPTY  EMPTY  EMPTY  EMPTY  EMPTY  EMPTY  EMPTY  EMPTY  EMPTY
# --------------------------------------------------------------------------------
    
def p_empty(p):
    ''' empty : '''
    p[0] = Pass()


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
    ('left', 'ADD','SUB','MUL','DIV'),
    ('left', 'PLUS','MINUS','BYM','BYD')
)

parser = yacc(
    debug=False,
    write_tables=True,
    errorlog=NullLogger()
)
