"""
Author: @CosasDePuma <kikefontanlorenzo@gmail.com>(https://github.com/cosasdepuma)
"""

import requests

def _ask_owned(email):
    base = 'https://haveibeenpwned.com/api/v2/breachedaccount/'
    headers = { 'User-Agent': 'Alfred' }
    url = base + email
    response = requests.get(url, headers=headers)
    hacked = "VERDAD" if response.status_code == 200 else "FALSO"
    return hacked

def check_pwned(args):
    email = None
    result = None
    for mail in args:
        if args[mail]:
            email = args[mail]
    if email:
         result = _ask_owned(email)
    return result

LIB_CONFIGURATION = {
    'NAME': 'haveibeenpwned',
    'COMMANDS': {
        'COMPRUEBA': {
            'function': check_pwned,
            'args': {
                '(SI HAN HACKEADO)*': 'EMAIL0',
                '(SI HAN HACKEADO A)*': 'EMAIL1',
                '(SI HA SIDO HACKEADO)*': 'EMAIL2',
                '(SI)*(HA SIDO HACKEADO)': 'EMAIL3'
            }
        }
    }
}
