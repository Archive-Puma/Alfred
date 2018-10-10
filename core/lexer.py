# -*- encoding: utf-8 -*-
"""
Author: @CosasDePuma <kikefontanlorenzo@gmail.com>(https://github.com/cosasdepuma)
"""

import re

class Lexer:
    """ Lexer component to tokenize the code """
    def __init__(self, _keywords, _lang):
        self.lang = _lang
        self.keywords = _keywords

    def tokenizer(self, _lineofcode):
        token = None
        _lineofcode = _lineofcode.strip()
        splitted = _lineofcode.split(' ', 1)
        if len(splitted) == 1:
            splitted.append('')
        cmd = plainvowels(splitted[0].upper())
        if cmd in self.keywords['std']:
            token = {
                'id': 'keyword',
                'key': cmd,
                'args': splitted[1],
                'lib': 'std'
            }
        elif cmd in self.keywords['control']:
            token = {
                'id': 'control',
                'key': cmd,
                'args': splitted[1]
            }
        elif cmd in self.keywords['import']:
            lib = splitted[1].split(' ', 1)[1].lower()
            lib = re.sub(' ', '_', lib)
            options = {
                'lang': self.lang.lower(),
                'lib': lib,
                'keywords': self.keywords
            }
            self.keywords['third'] = self.keywords['import'][cmd]['function'](options)
        else:
            for lib in self.keywords['third']:
                if cmd in self.keywords['third']:
                    token = {
                        'id': 'keyword',
                        'key': cmd,
                        'args': splitted[1],
                        'lib': 'third'
                    }
        return token

def plainvowels(word):
    """ Avoid accents """
    word = re.sub('[ÁÀÂÄ]', 'A', word)
    word = re.sub('[ÉÈÊË]', 'E', word)
    word = re.sub('[ÍÌÎÏ]', 'I', word)
    word = re.sub('[ÓÒÔÖ]', 'O', word)
    word = re.sub('[ÚÙÛÜ]', 'U', word)
    return word
