    
    path = require('path')
    PyShell = require('python-shell').PythonShell
    
    options =
        mode: 'text'
        pythonOptions: [ '-u' ]
        args: [ '{ "domain": "http://faitic.uvigo.es" }' ]
        scriptPath: path.join __dirname, '../backend/works/'
    
    PyShell.run 'web/robots.py', options, (err, res) ->
        throw err if err
        console.log res.join '\n'
