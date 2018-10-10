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
                key_args = self.keywords[_token['lib']][_token['key']]['args']
                options = {}
                for arg in key_args:
                    if type(arg) is int:
                        match = _token['args'].split(' ')[arg]
                        options[key_args[arg]] = match
                    elif type(arg) is str:
                        if '*' in arg:
                            options[key_args[arg]] = get_asterisk_args(arg, _token['args'])
                        else:
                            options[key_args[arg]] = get_identifier_args(arg, _token['args'])
                self.instructions.append({
                    'key': _token['key'],
                    'args': options,
                    'lib': _token['lib']
                })
                self.ipointer = self.ipointer + 1

def get_asterisk_args(keys, arguments):
    upper = arguments.upper()
    _from, _to = keys.split('*', 1)
    _to = re.sub('[\\(\\)]', '', _to)
    _from = re.sub('[\\(\\)]', '', _from)
    if not _from in upper or not _to in upper:
        arguments = None
    else:
        if _to != '':
            if _to.isdigit():
                _to = int(_to)
                # TODO
            else:
                arguments = re.split(_to, arguments, flags=re.IGNORECASE)[-2]
        if _from != '':
            if _from.isdigit():
                _from = int(_from)
                # TODO
            else:
                arguments = re.split(_from, arguments, 1, flags=re.IGNORECASE)[1]
        arguments = arguments.strip()
    return arguments

def get_identifier_args(key, arguments):
    if key in arguments.upper():
        arguments = re.split(key, arguments, 1, flags=re.IGNORECASE)[1].strip()
        arguments = arguments.split(' ', 1)[0]
    else:
        arguments = None
    return arguments
