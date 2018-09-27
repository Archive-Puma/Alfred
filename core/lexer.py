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
            '."': '<*%QS',
            '".': '<*%QE',
            '\n': '<*%NL',
            'label': '<*%:'
        }
        # Set some control flow keywords (labels, conditionals...)
        self.controlflow_keywords = _controlflow_keywords

    # Encode the source code
    def format(self, _lineofcode):
        """ Avoid problematic characters """
        _lineofcode = re.sub('\\ \"', ' ' + self.magicquotes['."'] + ' ', _lineofcode)
        _lineofcode = re.sub('\"', ' ' + self.magicquotes['".'] + ' ', _lineofcode)
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
            # Check if the previous words contains a keyword
            if tid == 'keyword':
                # If the word is not an encoded character, it is an argument
                if word not in self.magicquotes.values():
                    self.tokens.append({
                        'id': 'arg',
                        'value': word
                    })
                    tmp = []
            # Check if the words are part of a string
            elif tid == 'char':
                # If we find a second quote mark, it is the final of the string
                if word == self.magicquotes['".']:
                    self.tokens.append({
                        'id': tid,
                        'value': ' '.join(tmp)
                    })
                    tid = ''
                    tmp = []
            # Check if the previous words contains a label command
            elif tid == 'label':
                # Create the label name when the line ends
                if word == self.magicquotes['\n']:
                    self.tokens.append({
                        'id': tid,
                        'value': ' '.join(tmp)
                    })
                    tid = ''
                    tmp = []
            else:
                # Start of the string
                if word == self.magicquotes['."']:
                    tid = 'char'
                # Start of the label
                elif word == self.magicquotes['label']:
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
