"""
Author: @CosasDePuma <kikefontanlorenzo@gmail.com>(https://github.com/cosasdepuma)
"""

import lib.std as lib

KEYWORDS = {
    'std': {
        'ADIOS':    {
            'function': lib.halt,
            'args': {
                0: 'EXIT_CODE'
            },
        },
        'DI': {
            'function': lib.echo,
            'args': {
                '*': 'STRING',
                'VARS': 'VARIABLES'
            }
        },
        'DEFINE': {
            'function': lib.define,
            'args': {
                '*(COMO)': 'NAME',
                '(COMO)*': 'VALUE',
                'VARS': 'VARIABLES'
            }
        },
        'MUESTRA': {
            'function': lib.show,
            'args': {
                '(EL VALOR DE)*': 'NAME',
                'VARS': 'VARIABLES'
            }
        },
        'VETE': {
            'function': lib.goto,
            'args': {
                '(A)*': 'LABEL',
                '(A)*(SI)': 'CONDITIONAL JUMP',
                '(SI)*': 'CONDITIONAL',
                'JUMPS': 'JUMPS',
                'VARS': 'VARIABLES'
            }
        }
    },
    'import': {
        'APRENDE': { 'function': lib.learn  }
    },
    'variables': {
        'output': ['EL RESULTADO', 'LA SALIDA'],
        'endl': ['EL FIN DE LINEA', 'EL FIN DE LÍNEA'],
        'true': ['VERDAD'],
        'false': ['MENTIRA', 'FALSO'],
        'expression': 'ES'
    },
    'control': {
        'RECUERDA': {
            'args': { 'ESTE MOMENTO COMO': 'JUMP_POINT' }
        }
    },
    'third': {}
}
