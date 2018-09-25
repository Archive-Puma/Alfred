import re

class Lexer:
    def __init__(self, _keywords):
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
        self.controlFlowKeywords = {
            'label': 'RECUERDA ESTE MOMENTO COMO'
        }

    # Encode the source code
    def format(self, _lineofcode):
        _lineofcode = re.sub('\ \"', ' ' + self.magicquotes['."'] + ' ', _lineofcode)
        _lineofcode = re.sub('\"', ' ' + self.magicquotes['".'] + ' ', _lineofcode)
        _lineofcode = re.sub('\n', ' ' + self.magicquotes['\n'] + ' ', _lineofcode)
        _lineofcode = re.sub(self.controlFlowKeywords['label'], ' ' +  self.magicquotes['label'] + ' ', _lineofcode, flags=re.I)
        _lineofcode = re.sub('\ {2,}',' ', _lineofcode)
        return _lineofcode.strip()


    def tokenizer(self, _lineofcode):
        tid = ''
        tmp = []
        self.tokens = []
        _lineofcode = self.format(_lineofcode)
        # Read the line of code word by word
        for word in _lineofcode.split(' '):
            # Get the args for the instructions
            if tid == 'keyword':
                if word not in self.magicquotes.values():
                    self.tokens.append({
                        'id': 'arg',
                        'value': word
                    })
                    tmp = []
            # Detect strings
            if word == self.magicquotes['."']:
                tid = 'char'
            elif word == self.magicquotes['".']:
                self.tokens.append({
                    'id': tid,
                    'value': ' '.join(tmp)
                })
                tid = ''
                tmp = []
            else:
                if tid != 'char':
                    # Get all the control flow labels
                    if word == self.magicquotes['label']:
                        tid = 'label'
                    elif word == self.magicquotes['\n'] and tid == 'label':
                        self.tokens.append({
                            'id': tid,
                            'value': ' '.join(tmp).upper()
                        })
                        tid = ''
                        tmp = []
                    # Get all the instructions in the line of code
                    if tid != 'label':
                        if word.upper() in self.keywords:
                            self.tokens.append({
                                'id': 'keyword',
                                'value': word.upper()
                            })
                            tmp = []
                            # Don't get the args in some cases
                            if word.upper() != 'DI': #FIXME
                                tid = 'keyword'
                            continue
                # Append the words to a temporally variable
                if word not in self.magicquotes.values():
                    tmp.append(word)
