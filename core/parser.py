# -*- encoding: utf-8 -*-
"""
Author: @CosasDePuma <kikefontanlorenzo@gmail.com>(https://github.com/cosasdepuma)
"""

import re

class Parser:
    """ Parser component to create the instructions """
    def __init__(self, _keywords):
        self.jumps = {}
        self.ipointer = 0
        self.instructions = []
        self.keywords = _keywords

    def build(self, _token):
        if _token:
            if _token['id'] == 'control':
                for arg in self.keywords[_token['id']][_token['key']]['args']:
                    pattern = arg + '.*'
                    pattern = re.compile(pattern, re.IGNORECASE)
                    match = pattern.search(_token['args'])
                    if match:
                        match = re.sub('{0}\s+'.format(arg), '', match.group(), flags=re.IGNORECASE)
                        self.jumps[match] = self.ipointer
            elif _token['id'] == 'keyword':
                lib = None
                if _token['key'] in self.keywords['std']:
                    lib = 'std'
                options = {}
                for arg in self.keywords[lib][_token['key']]['args']:
                    if type(arg) is int:
                        match = _token['args'].split(' ')[arg]
                        options[self.keywords[lib][_token['key']]['args'][arg]] = match
                    elif type(arg) is str:
                        if arg == '*':
                            options[self.keywords[lib][_token['key']]['args'][arg]] = _token['args']
                        elif arg[0] == '(' and arg[-1] == '*':
                            avoids = int(re.sub('[\\(\\)\\*]', '', arg))
                            match = _token['args'].split(' ', avoids)[-1]
                            options[self.keywords[lib][_token['key']]['args'][arg]] = match
                        elif arg[0] == '*' and arg[-1] == ')':
                            until = re.sub('[\\(\\)\\*]', '', arg)
                            match = re.sub('\\s+{0}.*'.format(until), '', _token['args'], flags=re.IGNORECASE)
                            options[self.keywords[lib][_token['key']]['args'][arg]] = match
                        elif arg[-1] == '}' and arg[-2] == '*':
                            until = re.sub('\\{\\*\\}', '', arg)
                            if until in _token['args'].upper():
                                match = re.split(until, _token['args'], 1, flags=re.IGNORECASE)[1].strip()
                                options[self.keywords[lib][_token['key']]['args'][arg]] = match
                self.instructions.append({
                    'key': _token['key'],
                    'args': options,
                    'lib': lib
                })
                self.ipointer = self.ipointer + 1
