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
                'COMO{*}': 'VALUE',
                'VARS': 'VARIABLES'
            }
        },
        'MUESTRA': {
            'function': lib.show,
            'args': {
                'EL VALOR DE{*}': 'NAME',
                'VARS': 'VARIABLES'
            }
        },
        'VETE': {
            'function': lib.goto,
            'args': {
                'A{*}': 'LABEL',
                'JUMPS': 'JUMPS'
            }
        }
#        'DEFINE':   lib.define,
#        'EJECUTA':  lib.run,
#        'MUESTRA':  lib.show,
    },
    'import': {
        'APRENDE': { 'function': lib.learn  }
    },
    'variables': {
        'output': ['EL RESULTADO', 'LA SALIDA'],
        'endl': ['EL FIN DE LINEA', 'EL FIN DE LÍNEA']
    },
    'control': {
        'RECUERDA': {
            'args': { 'ESTE MOMENTO COMO': 'JUMP_POINT' }
        }
    },
    'third': {}
}
