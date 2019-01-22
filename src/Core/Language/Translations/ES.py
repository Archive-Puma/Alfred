Language = {
    'Invoke': 'alfred',
    'Syntax': {
        'a': {
            'adi[oó]s alfred': 'Base.Exit'
        },
        'd': {
            'define la variable (?P<name>.+) como (?P<value>.+)': 'Standard.Define'
        },
        'e': {
            'escribe "(?P<text>.+)"': 'IO.Write'
        },
        'm': {
            'muestra la variable (?P<name>.+)': 'IO.Show.Variable',
            'muestra el tipo de la variable (?P<name>.+)': 'IO.Show.Type',
            'muestra el valor de la variable (?P<name>.+)': 'IO.Show.Variable',
        },
        'v': {
            'vete al momento (?P<name>.+)': 'Control.Moments.Jump'
        },
        '?': ['define este momento como (?P<name>.+)']
    }
}