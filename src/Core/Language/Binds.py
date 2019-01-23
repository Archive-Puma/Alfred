
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
    }
}