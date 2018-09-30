"""
Author: @CosasDePuma <kikefontanlorenzo@gmail.com>(https://github.com/cosasdepuma)
"""

import lib.std as lib

KEYWORDS = {
    '=':        'AS',
    '<<':       'ABOVE',

    'BYE':      lib.halt,
    'DEFINE':   lib.define,
    'GO':       lib.goto,
    'LEARN':    lib.learn,
    'RUN':      lib.run,
    'SAY':      lib.echo,
    'SHOW':     lib.show
}

CONTROLFLOW_KEYWORDS = {
    'label':    'REMEMBER THIS MOMENT AS'
}
