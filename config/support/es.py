"""
Author: @CosasDePuma <kikefontanlorenzo@gmail.com>(https://github.com/cosasdepuma)
"""

import lib.std as lib

KEYWORDS = {
    '=':        'COMO',
    '<<':       'LO ANTERIOR',
    '$$':       'EL VALOR DE',

    'ADIOS':    lib.halt,
    'APRENDE':  lib.learn,
    'DEFINE':   lib.define,
    'EJECUTA':  lib.run,
    'DI':       lib.echo,
    'MUESTRA':  lib.show,
    'VETE':     lib.goto
}

CONTROLFLOW_KEYWORDS = {
    'label':    'RECUERDA ESTE MOMENTO COMO'
}
