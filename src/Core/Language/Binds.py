# -*- coding: utf-8 -*-

from ..Evaluator.Commands.IO        import (
    Show,Write)
from ..Evaluator.Commands.Base      import (
    Exit)
from ..Evaluator.Commands.Math      import (
    Addition,Subtraction,Multiplication,Division)
from ..Evaluator.Commands.Control   import (
    Moments)
from ..Evaluator.Commands.Standard  import (
    Define)
from ..Evaluator.Commands.Network import (
    ECHO,HTTP,Discard
)

Functions = {
    'Base': {
        'Exit': Exit()
    },
    'Standard': {
        'Define': Define()
    },
    'IO': {
        'Write': Write(),
        'Show': {
            'Type': Show.Type(),
            'Variable': Show.Variable()
        }
    },
    'Math': {
        'Addition': Addition(),
        'Division': Division(),
        'Multiplication': Multiplication(),
        'Subtraction': Subtraction()
    },
    'Control': {
        'Moments': {
            'Jump': Moments.Jump()
        }
    },
    'Network': {
        'ECHO': {
            'Server': ECHO.Server()
        },
        'Discard': {
            'Server': Discard.Server()
        },
        'HTTP': {
            'Server': HTTP.Server()
        }
    }
}
