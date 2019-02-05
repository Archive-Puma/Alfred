import ast
import sys

from ply    import yacc
from lexer import tokens


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


# --------------------------------------------------------------------------------
#    STATEMENTS  STATEMENTS  STATEMENTS  STATEMENTS  STATEMENTS  STATEMENTS
# --------------------------------------------------------------------------------

def p_program(p):
    ''' program : statements '''
    p[0] = p[1]

def p_statements(p):
    '''
    statements  : statement
                | statements statement
                | empty
    '''
    if len(p) == 1:
        p[0] = ast.InstructionList()
    elif len(p) == 2:
        p[0] = ast.InstructionList([p[1]])
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
    ''' if_statement : IF expression THEN statements IF NOT if_statement '''
    p[0] = ast.If(p[2],p[4],p[7])

def p_statement_if_else(p):
    ''' if_statement : IF expression THEN statements IF NOT statements END '''
    p[0] = ast.If(p[2],p[4],p[7])

def p_statement_if(p):
    ''' if_statement : IF expression THEN statements END '''
    p[0] = ast.If(p[2],p[4])

# --------------------------------------------------------------------------------
#   LOOPS  LOOPS  LOOPS  LOOPS  LOOPS  LOOPS  LOOPS  LOOPS  LOOPS  LOOPS  LOOPS
# --------------------------------------------------------------------------------

def p_statement_while(p):
    ''' statement : WHILE expression ',' statement '''
    p[0] = ast.While(p[2],ast.InstructionList([p[4]]))

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
        p[0] = ast.InstructionList([p[1]])
    elif len(p) == 4:
        p[1].child.append(p[3])
        p[0] = p[1]

def p_function_print(p):
    ''' statement : PRINT arguments '''
    p[0] = ast.Print(p[2])

# --------------------------------------------------------------------------------
#  DEFINITIONS  DEFINITIONS  DEFINITIONS  DEFINITIONS  DEFINITIONS  DEFINITIONS
# --------------------------------------------------------------------------------

def p_expression_let(p):
    ''' expression : DEFINE NAME '=' expression '''
    p[0] = ast.Define(ast.Name(p[2]),p[4])

def p_expression_id(p):
    ''' expression : NAME '''
    p[0] = ast.Name(p[1])

def p_expression_value(p):
    '''
    expression  : INTEGER
                | STRING
    '''
    p[0] = ast.Primitive(p[1])
    
def p_empty(p):
    ''' empty : '''
    p[0] = ast.Pass()


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
    ('left', 'ADD','SUB','BY','DIV'),
)
parser = yacc.yacc()
env = Environment()
