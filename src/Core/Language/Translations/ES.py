# -*- coding: utf-8 -*-

Language = {
    'Invoke': 'alfred',
    'Syntax': {
        'a': {
            'adi[oó]s alfred': 'Base.Exit'
        },
        'c': {
            'crea un servidor echo(?: en el puerto (?P<port>\d+))?': 'Network.ECHO.Server',
            'crea un servidor discard(?: en el puerto (?P<port>\d+))?': 'Network.Discard.Server',
            'crea un servidor (?:web|http)(?: en el puerto (?P<port>\d+))?': 'Network.HTTP.Server'
        },
        'd': {
            'define la variable (?P<name>.+) como (?P<value>.+)': 'Standard.Define',
            'divide (?P<name>.+) entre (?P<number>\d+)': 'Math.Division'
        },
        'e': {
            'escribe "(?P<text>.+)"': 'IO.Write'
        },
        'm': {
            'muestra la variable (?P<name>.+)': 'IO.Show.Variable',
            'muestra el tipo de la variable (?P<name>.+)': 'IO.Show.Type',
            'muestra el valor de la variable (?P<name>.+)': 'IO.Show.Variable',
            'multiplica (?P<name>.+) por (?P<number>\d+)': 'Math.Multiplication'
        },
        'r': {
            'r[eé]stale (?P<number>\d+) a (?P<name>.+)': 'Math.Subtraction'
        },
        's': {
            's[uú]male (?P<number>\d+) a (?P<name>.+)': 'Math.Addition'
        },
        'v': {
            'vete al momento (?P<name>.+)': 'Control.Moments.Jump'
        },
        '?': ['define este momento como (?P<name>.+)']
    }
}
