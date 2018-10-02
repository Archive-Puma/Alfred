"""
Author: @CosasDePuma <kikefontanlorenzo@gmail.com>(https://github.com/cosasdepuma)
"""

import re

class Lexer:
    """ Lexer component to tokenize the code """
    def __init__(self, _keywords, _controlflow_keywords):
        self.tokens = []
        self.keywords = _keywords
        # Avoid some problematic stuff with a custom encoding
        self.magicquotes = {
            '\n': '<*%NL',
            'label': '<*%:'
        }
        # Set some control flow keywords (labels, conditionals...)
        self.controlflow_keywords = _controlflow_keywords

    # Encode the source code
    def format(self, _lineofcode):
        """ Avoid problematic characters """
        _lineofcode = re.sub('\n', ' ' + self.magicquotes['\n'] + ' ', _lineofcode)
        _lineofcode = re.sub(self.controlflow_keywords['label'],
                             ' ' +  self.magicquotes['label'] + ' ', _lineofcode, flags=re.I)
        _lineofcode = re.sub('\\ {2,}', ' ', _lineofcode)
        return _lineofcode.strip()

    def tokenizer(self, _lineofcode):
        """ Tokenize the source code word by word """
        tid = ''
        tmp = []
        self.tokens = []
        _lineofcode = self.format(_lineofcode)
        # Read the line of code word by word
        for word in _lineofcode.split(' '):
            word = plainvowels(word)
            # Check if the previous words contains a keyword
            if tid == 'keyword':
                # If the word is not an encoded character, it is an argument
                if word not in self.magicquotes.values():
                    self.tokens.append({
                        'id': 'arg',
                        'value': word
                    })
                    tmp = []
            else:
                # Start of the label
                if word == self.magicquotes['label']:
                    tid = 'label'
                # Instruction
                elif word.upper() in self.keywords:
                    self.tokens.append({
                        'id': 'keyword',
                        'value': word.upper()
                    })
                    tmp = []
                    tid = 'keyword'
                    continue
            # Append the word to a temp variable
            if word not in self.magicquotes.values():
                tmp.append(word)


def plainvowels(word):
    """ Avoid accents """
    word = re.sub('[áàâä]', 'a', word)
    word = re.sub('[éèêë]', 'e', word)
    word = re.sub('[íìîï]', 'i', word)
    word = re.sub('[óòôö]', 'o', word)
    word = re.sub('[úùûü]', 'u', word)
    word = re.sub('[ÁÀÂÄ]', 'A', word)
    word = re.sub('[ÉÈÊË]', 'E', word)
    word = re.sub('[ÍÌÎÏ]', 'I', word)
    word = re.sub('[ÓÒÔÖ]', 'O', word)
    word = re.sub('[ÚÙÛÜ]', 'U', word)
    return word
