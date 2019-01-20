
from ..Evaluator.Commands.IO        import Write
from ..Evaluator.Commands.Base      import Exit
from ..Evaluator.Commands.Standard  import Define

Functions = {
    'Base': {
        'Exit': Exit()
    },
    'Standard': {
        'Define': Define()
    },
    'IO': {
        'Write': Write()
    }
}